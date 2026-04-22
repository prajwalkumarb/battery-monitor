# 🔋 Battery Monitor (Windows)

A lightweight Windows background application that monitors battery status and provides real-time notifications for charging events, battery levels, and critical conditions.

---

## 🚀 Features

* 🔌 Instant charging / discharging detection
* 🔋 Battery level alerts (configurable: 85%, 90%, 95%, 100%)
* ⚠️ Low battery alert
* 🔴 Critical battery alert with sound
* 🔔 Windows toast notifications
* 📝 Logging with timestamps
* 🔄 Auto-start on system login
* 📦 Installer-based deployment

---

## 📁 Project Structure

```
battery-monitor/
│
├── battery_monitor.py      # Main application
├── config.json             # Configuration file
├── fav.ico                 # Application icon
├── installer.iss           # Inno Setup installer script
├── requirements.txt        # Python dependencies
└── README.md
```

---

## ⚙️ Configuration

Edit `config.json` to customize behavior:

```json
{
  "fast_check": 3,
  "slow_check": 60,
  "levels": [85, 90, 95],
  "low_battery": 30,
  "critical_battery": 15
}
```

---

## 🛠 Installation (End User)

1. Run the installer:

   ```
   BatteryMonitorSetup.exe
   ```

2. After installation:

   * App starts automatically
   * Runs in background
   * Notifications begin immediately

---

## 🧪 Run from Source (Developer)

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Run script

```bash
python battery_monitor.py
```

---

## 📦 Build EXE

Using PyInstaller:

```bash
pyinstaller --onefile --icon=fav.ico --add-data "config.json;." --noconsole battery_monitor.py
```

Output:

```
dist/battery_monitor.exe
```

---

## 📦 Build Installer

Using Inno Setup:

Download Inno Setup Compiler
https://github.com/jrsoftware/issrc/releases/download/is-6_7_1/innosetup-6.7.1.exe
and open installer.iss file 

### Command:

```bash
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" installer.iss
```

Output:

```
installer_output/BatteryMonitorSetup.exe
```

---

## 🔄 Auto Start Behavior

The application is configured to:

* Start automatically on system login
* Run in background
* Prevent multiple instances

---

## 📝 Logs

Logs are stored at:

```
C:\Users\<User>\AppData\Roaming\BatteryMonitor\battery.log
```

Each log entry includes timestamp and event details.

---

## ❌ Uninstallation

During uninstall:

* Running process is terminated
* Installed files are removed
* Installation folder is deleted
* Startup entry is removed

---

## ⚠️ Notes

* This application **does NOT control charging hardware**
* It only provides **notifications and monitoring**
* Temperature monitoring depends on system support

---

## 👨‍💻 Author

**Prajwal Kumar**
Software Engineer

---

## 📄 License

This project is for internal / personal use. Customize as needed.
