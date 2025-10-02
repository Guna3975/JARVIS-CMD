import os
import subprocess

def open_system_app(command):
    command = command.lower().strip()

    # Common folders
    folders = {
        "documents": os.path.join(os.environ['USERPROFILE'], 'Documents'),
        "downloads": os.path.join(os.environ['USERPROFILE'], 'Downloads'),
        "desktop": os.path.join(os.environ['USERPROFILE'], 'Desktop'),
        "this pc": "C:\\"
    }

    for key, path in folders.items():
        if key in command:
            try:
                os.startfile(path)
                return True, f"Opening {key}..."
            except Exception as e:
                return False, f"Failed to open {key}: {e}"

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
                    try:
                        subprocess.Popen(['powershell', '-Command', f'Start-Process "{shortcut_path}"'])
                        app_name = file.rsplit('.', 1)[0]  # Remove .lnk
                        return True, f"Opening {app_name}..."
                    except Exception as e:
                        return False, f"Failed to open {file}: {e}"

    return False, f"Sorry, I cannot find any app matching '{command}'."
