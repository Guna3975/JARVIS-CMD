from Speech.speak import speak
from datetime import datetime
import os
import subprocess

def open_system_app(command):
    command = command.lower()

    # Common folders
    folders = {
        "documents": os.path.join(os.environ['USERPROFILE'], 'Documents'),
        "downloads": os.path.join(os.environ['USERPROFILE'], 'Downloads'),
        "desktop": os.path.join(os.environ['USERPROFILE'], 'Desktop'),
        "this pc": "C:\\"
    }

    for key, path in folders.items():
        if key in command:
            os.startfile(path)
            return f"Opening {key}"

    # Start Menu shortcuts
    start_menu_paths = [
        os.path.join(os.environ['ProgramData'], "Microsoft", "Windows", "Start Menu", "Programs"),
        os.path.join(os.environ['APPDATA'], "Microsoft", "Windows", "Start Menu", "Programs")
    ]

    for path in start_menu_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith(".lnk") and command in file.lower():
                    shortcut_path = os.path.join(root, file)
                    subprocess.Popen(['powershell', '-Command', f'Start-Process "{shortcut_path}"'])
                    return f"Opening {file.replace('.lnk','')}"

    return "Sorry, I cannot find that app"
