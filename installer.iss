[Setup]
AppName=Battery Monitor
AppVersion=1.0
DefaultDirName={autopf}\BatteryMonitor
DefaultGroupName=Battery Monitor
PrivilegesRequired=admin
OutputDir=installer_output
OutputBaseFilename=BatteryMonitorSetup
Compression=lzma
SolidCompression=yes
AppPublisher=Prajwal Kumar
SetupIconFile=fav.ico
UninstallDisplayIcon={app}\battery_monitor.exe

[Files]
Source: "dist\battery_monitor.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "fav.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Start Menu
Name: "{group}\Battery Monitor"; Filename: "{app}\battery_monitor.exe"

; Desktop (optional)
Name: "{commondesktop}\Battery Monitor"; Filename: "{app}\battery_monitor.exe"; Tasks: desktopicon

; ✅ ONLY ONE startup entry
Name: "{commonstartup}\Battery Monitor"; Filename: "{app}\battery_monitor.exe"

[Tasks]
Name: "desktopicon"; Description: "Create Desktop Icon"; GroupDescription: "Additional Icons:"

[Run]
Filename: "{app}\battery_monitor.exe"; Flags: nowait postinstall skipifsilent

[UninstallRun]
Filename: "taskkill"; Parameters: "/IM battery_monitor.exe /F"; Flags: runhidden; RunOnceId: "KillBatteryMonitor"

[UninstallDelete]
Type: filesandordirs; Name: "{app}"