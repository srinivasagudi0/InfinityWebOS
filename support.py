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