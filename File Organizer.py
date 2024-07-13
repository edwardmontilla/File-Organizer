# File Organizer
# Organizes files within a specific directory
# Added a print statement and condition if files were moved successfully or not

import os
import shutil
from pathlib import Path

os.chdir('/Users/Edan/Desktop/a very nice folder')

files_moved = False

if not os.path.exists("Weird Folder"):
    os.mkdir("Weird Folder")

for file in os.listdir():
    if file == "Weird Folder" or os.path.isdir(file):
        continue
    f = Path(file)
    name, ext = f.stem, f.suffix

    filename = name.replace(" ", "-")
    new_filename = f"{filename}{ext}"

    f.rename(new_filename)

    try:
        shutil.move(new_filename, "Weird Folder")
        files_moved = True
    except Exception as e:
        print(f"Failed to move {new_filename}: {e}")


if files_moved:
    print("Files organized successfully!")
else:
    print("No files were moved.")

