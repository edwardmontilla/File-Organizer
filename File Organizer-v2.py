# File Organizer-v2
# Separates files and moves them to specific folders

import os
import shutil
from pathlib import Path

my_directory = '/Users/Edan/Desktop/a very nice folder'

os.chdir(my_directory)

img_files = False
music_files = False
video_files = False
doc_files = False
other_files = False


if not os.path.exists("Images Folder"):
    os.mkdir("Images Folder")

if not os.path.exists("Music Folder"):
    os.mkdir("Music Folder")

if not os.path.exists("Video Folder"):
    os.mkdir("Video Folder")

if not os.path.exists("Documents Folder"):
    os.mkdir("Documents Folder")

if not os.path.exists("Misc Folder"):
    os.mkdir("Misc Folder")

for file in os.listdir():
    if file == "Backup Folder" or os.path.isdir(file):
        continue
    f = Path(file)
    name, ext = f.stem, f.suffix

    filename = name.replace(" ", "-")
    new_filename = f"{filename}{ext}"

    f.rename(new_filename)

    try:
        if ext in ['.png', '.jpg', '.jpeg', '.svg', '.gif', '.webp']:
            shutil.move(new_filename, "Images Folder")
            img_files = True
        elif ext in ['.mp3', '.wav', '.flac', '.m4p', '.m4a', '.flv', '.wma', '.wv', '.m4b']:
            shutil.move(new_filename, "Music Folder")
            music_files = True
        elif ext in ['.mp4', '.mov', '.wmv', '.avi', '.avchd', '.mkv', '.webm', '.flv', '.f4v', '.swf']:
            shutil.move(new_filename, "Video Folder")
            video_files = True
        elif ext in ['.pdf', '.txt', '.docx', '.imp', '.xls', '.ods', '.xlsx', '.ppt', '.pptx', '.dat', '.vcf', '.xps', 
                     '.e.pub', '.mobi', '.html', '.eml', '.asc', '.msg', '.pages', '.rft', '.log', '.ipynb', '.md']:
            shutil.move(new_filename, "Documents Folder")
            doc_files = True
        else:
            shutil.move(new_filename, "Misc Folder")
            other_files = True

    except Exception as e:
        print(f"Failed to move {new_filename}: {e}")


if img_files or music_files or video_files or doc_files or other_files:
    print("Files organized successfully!")
else:
    print("No files were moved.")

