import platform
import subprocess

def open_calculator():
    # This function will open the calculator application based on the operating system
    os_name = platform.system()

    if os_name == "Windows":
        subprocess.Popen("calc.exe")
    elif os_name == "Darwin":  # macOS
        subprocess.Popen(["open", "-a", "Calculator"])
    elif os_name == "Linux":
        subprocess.Popen(["gnome-calculator"])
    else:
        print("Unsupported operating system")

def open_notepad():
    # This function will open the notepad application based on the operating system
    os_name = platform.system()

    if os_name == "Windows":
        subprocess.Popen("notepad.exe")
    elif os_name == "Darwin":  # macOS
        subprocess.Popen(["open", "-a", "Notes"])
    elif os_name == "Linux":
        subprocess.Popen(["gedit"])
    else:
        print("Unsupported operating system")

def open_file_explorer():
    # This function will open the file explorer based on the operating system
    os_name = platform.system()

    if os_name == "Windows":
        subprocess.Popen("explorer.exe")
    elif os_name == "Darwin":  # macOS
        subprocess.Popen(["open", "."])
    elif os_name == "Linux":
        subprocess.Popen(["nautilus", "."])
    else:
        print("Unsupported operating system")

def open_settings():
    # This function will open the settings application based on the operating system
    os_name = platform.system()

    if os_name == "Windows":
        subprocess.Popen("ms-settings:")
    elif os_name == "Darwin":  # macOS
        subprocess.Popen(["open", "-a", "System Preferences"])
    elif os_name == "Linux":
        subprocess.Popen(["gnome-control-center"])
    else:
        print("Unsupported operating system")

def open_music_player():
    # This function will open the music player application based on the operating system
    os_name = platform.system()

    if os_name == "Windows":
        # check if spotify is installed, if not open windows media player
        try:
            subprocess.Popen("spotify.exe")
        except FileNotFoundError:
            subprocess.Popen("wmplayer.exe")
    elif os_name == "Darwin":  # macOS
        try:
            subprocess.Popen(["open", "-a", "Spotify"])
        except FileNotFoundError:
            subprocess.Popen(["open", "-a", "Music"])
    elif os_name == "Linux":
        subprocess.Popen(["rhythmbox"])
    else:
        print("Unsupported operating system")