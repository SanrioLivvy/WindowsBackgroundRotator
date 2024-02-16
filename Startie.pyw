import winreg
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    print("Script is running with administrative privileges.")
else:
    print("Script is not running with administrative privileges.")


def add_to_startup(file_path):
    # Open the "Run" key in the registry
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)

    # Set the path of the script to be run on startup
    winreg.SetValueEx(key, "DailyDesktopBackgroundRotator", 0, winreg.REG_SZ, file_path)

    # Close the registry key
    winreg.CloseKey(key)

if __name__ == "__main__":
    # Specify the path to the script you want to add to startup
    script_path = r"C:\insert\script\path\here\WindowsBackgroundRotator\DailyDesktopBackgroundRotator.pyw"

    # Add the script to startup
    add_to_startup(script_path)

    # Run the script immediately
    os.startfile(script_path)