import subprocess

# This function has the role to determine if the current OS is Windows7 or Windows10 or none of them

def windows_version():
    win_version = str(subprocess.check_output("wmic os get Caption", shell=True))
    win_version = win_version.split(" ")
    if "Windows" in win_version:
        if "7" in win_version:
            # Windows 7
            return "7"
        elif "10" in win_version:
            # Windows 10
            return "10"
        else:
            return "Not a Windows OS"

