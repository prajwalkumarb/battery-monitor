import psutil
from winotify import Notification, audio
import time
import winsound
import json
import logging
import threading
import os
import sys

# ---- LOAD CONFIG ----
def get_base_path():
    if getattr(sys, 'frozen', False):
        return sys._MEIPASS  # PyInstaller temp folder
    return os.path.dirname(__file__)

base_path = get_base_path()
config_path = os.path.join(base_path, "config.json")

with open(config_path) as f:
    config = json.load(f)

FAST_CHECK = config["fast_check"]
SLOW_CHECK = config["slow_check"]
LEVELS = config["levels"]
LOW_BATTERY = config["low_battery"]
CRITICAL_BATTERY = config["critical_battery"]

# ---- LOGGER ----
log_dir = os.path.join(os.getenv("APPDATA"), "BatteryMonitor")
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "battery.log")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def log(msg):
    print(msg)
    logging.info(msg)

# ---- NOTIFICATION ----
def notify(title, msg):
    log(f"{title} - {msg}")
    toast = Notification(
        app_id="Battery Monitor",
        title=title,
        msg=msg,
        duration="short",
        icon=os.path.join(base_path, "fav.ico")
    )
    toast.set_audio(audio.Default, loop=False)
    toast.show()

def alert_sound(critical=False):
    if critical:
        winsound.Beep(1500, 700)
        winsound.Beep(1500, 700)
    else:
        winsound.Beep(1000, 500)

# ---- MAIN LOGIC ----
def monitor():
    battery = psutil.sensors_battery()
    last_plugged = battery.power_plugged

    last_level_check = 0
    notified_levels = set()
    low_battery_notified = False

    log("🔋 Battery Monitor Started")

    while True:
        battery = psutil.sensors_battery()
        percent = battery.percent
        plugged = battery.power_plugged
        current_time = time.time()

        # ⚡ Plug detection
        if plugged != last_plugged:
            if plugged:
                notify("Charging Started 🔌", "Charger connected")
            else:
                notify("Charging Stopped ⚡", "Charger disconnected")
            last_plugged = plugged

        # 🐢 Battery checks
        if current_time - last_level_check >= SLOW_CHECK:
            log(f"Battery: {percent}% | Plugged: {plugged}")

            for lvl in LEVELS:
                if percent >= lvl and lvl not in notified_levels:
                    notify("Battery Level", f"Reached {lvl}%")
                    notified_levels.add(lvl)

            if percent >= 100:
                alert_sound(critical=False)
                if plugged:
                    notify("Battery Full ✅", "Unplug charger")
                else:
                    notify("Battery Full ✅", "Battery is fully charged")

            if percent <= LOW_BATTERY and not low_battery_notified:
                notify("Low Battery ⚠️", f"{percent}% remaining")
                low_battery_notified = True

            if percent <= CRITICAL_BATTERY:
                alert_sound(critical=True)
                notify("Critical Battery 🔴", f"{percent}% remaining")

            if percent < min(LEVELS):
                notified_levels.clear()

            if percent > LOW_BATTERY:
                low_battery_notified = False

            last_level_check = current_time

        time.sleep(FAST_CHECK)

# ---- RUN ----
if __name__ == "__main__":
    monitor()