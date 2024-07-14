# File Organizer-v3
# Concise and streamlined for readability and simplicity

import os
import shutil
from pathlib import Path

my_directory = '/Users/Edan/Desktop/a very nice folder'

os.chdir(my_directory)

folders = {
    "Images Folder": ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp'],
    "Music Folder": ['.mp3', '.wav', '.flac', '.m4p', '.m4a', '.flv', '.wma', '.wv', '.m4b'],
    "Video Folder": ['.mp4', '.mov', '.wmv', '.avi', '.avchd', '.mkv', '.webm', '.flv', '.f4v', '.swf'],
    "Documents Folder": ['.pdf', '.txt', '.docx', '.imp', '.xls', '.ods', '.xlsx', '.ppt', '.pptx', '.dat', '.vcf', '.xps', 
                         '.epub', '.mobi', '.html', '.eml', '.asc', '.msg', '.pages', '.rtf', '.log', '.ipynb', '.md'],
    "Misc Folder": []
}

for folder in folders:
    os.makedirs(folder, exist_ok = True)

files_moved = False

for file in os.listdir():
    if file == "Backup Folder" or os.path.isdir(file):
        continue
    f = Path(file)
    name, ext = f.stem, f.suffix

    filename = name.replace(" ", "-")
    new_filename = f"{filename}{ext}"

    f.rename(new_filename)

    try:
        for folder, extensions in folders.items():
            if ext in extensions or folder == "Misc Folder":
                shutil.move(new_filename, folder)
                files_moved = True
                print(f"Moved {new_filename} to {folder}.")
                break
    except Exception as e:
        print(f"Failed to move {new_filename}: {e}")


if files_moved:
    print("Files organized successfully!")
else:
    print("No files were moved.")

