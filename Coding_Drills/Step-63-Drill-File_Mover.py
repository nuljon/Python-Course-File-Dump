###############################################################
#   Python 2.7
#   Step 63 - Programming Drill from Python Course at The Tech Academy
#   by Jon Nuljon
#   December, 2016
#############################################################
# Title: File Mover – Python 2.7 – IDLE
# Scenario: Your employer wants a program to move all his .txt files
# from one folder to another with the click of a click of a button.
# On your desktop make 2 new folders. Call one Folder A and the second
# Folder B. Create 4 random .txt files & put them in Folder A.
# Plan:
# - Move the files from Folder A to Folder B.
# - Print out each file path that got moved onto the shell.
# - Upon viewing Folder A after the execution, the moved files should not be there.
# Guidelines:
# ● Use Python 2.7 .x on this drill.
# ● Import the shutil module.
# ● Run it on the python shell.
# ● Use the IDLE for this Drill.
# Once you have created the program, show your work to the instructor for a pass
###############################################################################
from shutil import *
import os

# path to folder A
pathFolderA = "C:\Users\Student\Desktop\FolderA"
# list files in folder and assign them
filesList = os.listdir(pathFolderA)
# path to folder B
pathFolderB = "C:\Users\Student\Desktop\FolderB"

# iterate over the fileList
for files in filesList:
    # assemble path
    filePath = os.path.join(pathFolderA, files)
    # move the file to the destination folderB
    move(filePath,pathFolderB)
    # update the poth to file in folderB
    filePath = os.path.join(pathFolderB, files)
    # outout the url of the file to console
    print filePath + "\n"






# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
