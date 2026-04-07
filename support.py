# working here just a placeholder for now..
def open_calculator():
    # This function will open the calculator application based on the operating system
    import platform
    import subprocess

    os_name = platform.system()

    if os_name == "Windows":
        subprocess.Popen("calc.exe")
    elif os_name == "Darwin":  # macOS
        subprocess.Popen(["open", "-a", "Calculator"])
    elif os_name == "Linux":
        subprocess.Popen(["gnome-calculator"])
    else:
        print("Unsupported operating system")



open_calculator()