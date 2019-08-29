import os
import time
from functions_amatei import win7_notifications, win10_notifications, windows_version
from pathlib import Path

# Notifications for Windows 7
global notification
if windows_version.windows_version() == '7':
   notification = win7_notifications.WindowsBalloonTip()

#Creates a new directory "dir_name" in a given path
def create_new_dir(path,dir_name):
    already_exists = False
    dir_path=rf"{path}\{dir_name}"
    for file in os.listdir(path):
        if file == dir_name:
            already_exists = True
    if not already_exists:
        os.mkdir(dir_path, 0o77)
        print(f'{dir_path} has been created succesfully!')

        # Windows notifications initialiser:
        if windows_version.windows_version() == '7':
            notification.ShowWindow("download_manager.py notification!",f'{dir_path} has been created succesfully!')
        elif windows_version.windows_version() == '10':
            win10_notifications.win10toast_notifier(title="download_manager.py notification!",
                                                    message=f'{dir_path} has been created succesfully!'
                                                    )

#Search for all files whith extension "file_ext" in a given path "path_to_search_files" and moves to "path_to_move"
def get_files_of_type_and_move(path_to_search_files,file_ext,path_to_move):
    path_to_search = Path(path_to_search_files)
    duplicate_index=0
    for file in path_to_search.glob(file_ext):
        time.sleep(0.1)
        dest_file_name=file.name
        duplicate = True

        # Checking if in the target directory exists another file with the same name with our file we want to move
        while duplicate:
            check = False
            for f in os.listdir(path_to_move):
                if dest_file_name == f:
                    check = True
                    duplicate_index+=1
                    dest_file_name=f"({duplicate_index})" + file.name
            if not check:duplicate = False

        # Move the downloaded file to destination folder
        os.rename(f"{path_to_search_files}\{file.name}", f"{path_to_move}\{dest_file_name}")
        print(f"{file} has been moved to {path_to_move}")
        # Windows notifications initialiser:
        if windows_version.windows_version() == '7':
            notification.ShowWindow("download_manager.py notification!", f"{file} has been moved to {path_to_move}")
        elif windows_version.windows_version() == '10':
            win10_notifications.win10toast_notifier(title="download_manager.py notification!",
                                                    message=f"{file} has been moved to {path_to_move}"
                                                    )