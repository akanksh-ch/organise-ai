from config import load_config
import os
import shutil

config = load_config()

for directory in config['watch_directories']:
    for file in os.listdir(os.path.expanduser(directory)):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            dest_folder = config['file_destinations'][ext.lower()]
            dest_folder = os.path.expanduser(dest_folder)
            if os.path.exists(dest_folder):
                shutil.move(file_path, os.path.join(dest_folder, file))
                print(f"Moved {file} to {dest_folder}") 