import os
import subprocess

def open_system_app(command):
    command_lower = command.lower()

    # 1️⃣ Start Menu shortcuts
    start_menu_paths = [
        os.path.join(os.environ['ProgramData'], "Microsoft", "Windows", "Start Menu", "Programs"),
        os.path.join(os.environ['APPDATA'], "Microsoft", "Windows", "Start Menu", "Programs")
    ]
    for path in start_menu_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.lower().endswith(".lnk") and command_lower in file.lower():
                    shortcut_path = os.path.join(root, file)
                    subprocess.Popen(['powershell', '-Command', f'Start-Process "{shortcut_path}"'])
                    return f"Opening {file.replace('.lnk','')}"

    # 2️⃣ PATH search
    try:
        result = subprocess.run(f'where {command}', capture_output=True, text=True, shell=True)
        exe_path = result.stdout.strip().split('\n')[0]
        if os.path.exists(exe_path):
            subprocess.Popen([exe_path])
            return f"Opening {command}"
    except:
        pass

    # 3️⃣ AppData Local (recursive search for executables containing command)
    local_appdata = os.environ['LOCALAPPDATA']
    for root, dirs, files in os.walk(local_appdata):
        for file in files:
            if file.lower().endswith(".exe") and command_lower in file.lower():
                exe_path = os.path.join(root, file)
                subprocess.Popen([exe_path])
                return f"Opening {file.replace('.exe','')}"

    return f"Sorry, I cannot find the app '{command}'"
