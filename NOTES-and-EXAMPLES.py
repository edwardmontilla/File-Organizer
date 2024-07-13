# NOTES on how to create a File Organizer

# This will provide examples on how to:
# NAVIGATE between directories
# RENAME existing files
# MOVE files to a directory
# DELETE files



# TO NAVIGATE           <---------->

# to get the current directory:
# print(os.getcwd())

# to change to the directory of the folder we want to organize:
# os.chdir('Path/Here/')

# make sure to double check the directory using 'print(os.getcwd())'

import os
os.chdir('/Users/Edan/Desktop/a very nice folder')

# to get a list of the different file names in the folder:                          ----#
# print(os.listdir())                                                                   #
                                                                                        #
# Example OUTPUT:                                                                       #
# File Organizer.py                                                                     #
# dog.png                                                                               #
# cat.mp3                                                                           ----#    
                                                                                        #
# if we want to ignore a particular file,                                               #
# we can choose to ignore it by adding an 'if' condition                                #
                                                                                        #
# for file in os.listdir():                                                             #
#     if file == 'File Organizer.py':                                                   #
#         continue                                                                      #
#     print(file)                                                                       #
                                                                                        #
                                                                                        #
# Example OUTPUT:                                                                       #
# dog.png                                                                               #
# cat.mp3                                                                           ----#


# TO RENAME             <---------->

# split the base name from the extension (ex. filename.png --> filename .png)       ----#
                                                                                        #
# for file in os.listdir():                                                             #
#     if file == 'File Organizer.py':                                                   #
#         continue                                                                      #
#     name, ext = os.path.splitext(file)                                                #
#     print(name)                                                                       #
#     print(ext)                                                                        #
                                                                                        #
# Example OUTPUT:                                                                       #
# dog                                                                                   #
# .png                                                                                  #
# cat                                                                                   #
# .mp3                                                                              ----#

# we can choose to replace spaces in the file name to a hyphen                      ----#
# the .replace() method                                                                 #

import os
os.chdir('/Users/Edan/Desktop/a very nice folder')

# for file in os.listdir():                                                         ----#
#     if file == 'File Organizer.py':                                                   #
#         continue                                                                      #
                                                                                        #
#     name, ext = os.path.splitext(file)                                                #
                                                                                        #
#     filename = name.replace(" ", "-")                                                 #
#     new_filename = f"{filename}{ext}"                                                 #
                                                                                        #
    # to execute the script uncomment line below:                                       #
    # os.rename(file, new_filename)                                                     #
                                                                                        #
# Example OUTPUT:                                                                       #
# dog and cat.png --> dog-and-cat.png                                               ----#


# Using the Pathlib Module                                                          ----#
# begin by importing the pathlib                                                        #

import os
from pathlib import Path

# os.chdir('/Users/Edan/Desktop/a very nice folder')                                ----#
                                                                                        #
# for file in os.listdir():                                                             #
#     if file == 'File Organizer.py':                                                   #
#         continue                                                                      #
#     f = Path(file)                                                                    #
#     name, ext = f.stem, f.suffix                                                      #
                                                                                        #
#     filename = name.replace(" ", "-")                                                 #
#     new_filename = f"{filename}{ext}"                                                 #
                                                                                        #
    # to execute the script uncomment line below:                                       #
    # f.rename(new_filename)                                                        ----#



# TO MOVE               <---------->

# create a directory named "My Folder" if it doesn't already exist                  ----#
# Path("Name of folder").mkdir(does_it_exist = True)                                    #
# to move files we'll import the shutil module                                          #
                                                                                        #
import os
import shutil
from pathlib import Path

os.chdir('/Users/Edan/Desktop/a very nice folder')

# Path("My Folder").mkdir(exist_ok = True)                                          ----#
# if not os.path.exists("My Folder"):                                                   #
#     os.mkdir("My Folder")                                                             #
                                                                                        #
# for file in os.listdir():                                                             #
#     # adding file == "My Folder" will ensure that it doesn't read that directory      #
#     # when listing                                                                    #
#     if file == 'File Organizer.py' or file == "My Folder":                            #
#         continue                                                                      #
                                                                                        #
#     # Copy method will copy all files in the newly created folder "My Folder"         #
#     shutil.copy(file, "My Folder")                                                    #
                                                                                        #
#     # To keep the timestamp and meta data add "copy2"                                 #
#     shutil.copy2(file, "My Folder")                                                   #
                                                                                        #
#     # Move method will move all files in the newly created folder "My Folder"         #
#     # shutil.move(file, "My Folder")                                              ----#



# TO DELETE             <---------->

# to remove directory

import os
import shutil
from pathlib import Path

os.chdir('/Users/Edan/Desktop/a very nice folder')

# os.remove("filename")                                                             ----#
                                                                                        #
# Uncomment to execute line below:                                                      #
# shutil.rmtree("New folder")                                                       ----#






