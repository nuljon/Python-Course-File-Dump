#############################################################
#   Python 2.7
#   Step 64 - Programming Drill from Python Course at The Tech Academy
#   by Jon Nuljon
#   December, 2016
#############################################################
# THE FOLLOWING IS FROM THE ORIGINAL PROGRAMMING DRILL DESCRIPTION
# Title: Daily File Transfer scripting project - Python 2.x - IDLE
# Scenario: Your company's users create or edit a collection of text files
# throughout the day. These text files represent data about customer
# orders.
# Once per day, any files that are new, or that were edited within the
# previous 24 hours, must be sent to the home office. To facilitate this,
# these new or updated files need to be copied to a specific 'destination'
# folder on a computer, so that a special file transfer program can grab
# them and transfer them to the home office.
# The process of figuring out which files are new or recently edited, and
# copying them to the 'destination' folder, is currently being done
# manually. This is very expensive in terms of manpower.
# You have been asked to create a script that will automate this task,
# saving the company a lot of money over the long term.
# Guidelines:
# Use Python 2.x for this drill.
# You should create two folders; one to hold the files that get created or
# modified throughout the day, and another to receive the folders that your
# script determines should be copied over daily.
# To aid in your development efforts, you should create .txt files to add
# to the first folder, using Notepad or similar program. You should also
# copy some older text files in there if you like. You should use files
# that you can edit, so that you can control whether they are meant to be
# detected as 'modified in the last 24 hours' by your program.
# You should use IDLE for this Drill.
# Once you create a functioning script that is approved by your instructor,
# save it for later use. Do not modify this saved copy during subsequent
# drills.
import os
from datetime import *
import shutil

# a function listing updated files in a folder within a time range in hours
def listUpdatedFiles (folder, Hours=24):
    # set our cut off for accepting changes
    review  = datetime.now() - timedelta(hours=Hours)
    # initialize our list of updates
    updateList = []
    # iterate through the items in the folder
    for items in os.listdir(folder):
        # assemble path to items
        item = os.path.join(folder, items)
        # print item  + "\n"    # debug
        # check if it is a file
        if os.path.isfile(item):
            # and if it is a change within review period
            # print review
           #  print os.path.getmtime(item)  # debug
            # convert getmtime timestamp to datetime compare to review limit
            if (review <= datetime.fromtimestamp(os.path.getmtime(item))):
               # append this item to our update list
                updateList.append(item)
            else: #item is a file but not within review limit so continue
                continue
        else: # item is not a file so continue
            continue
    # we are done iterating so return with the update list
    return updateList


# a function to copy a list of pathed files to a destinaion
def copyFiles (files, destination):
    # for each of the files in the list
    for file in files:
        # copy file to destination
        shutil.copy(file, destination)
    # done iteration - nothing to return
    return

if __name__ == '__main__':

    ### define CONSTANTS
    # staging yard to look for new files or ones that have recently been modified
    stagingYard = "C:\\Users\\Student\\Desktop\\stage"
    # "destination" where we put a copy of the files for transport to home office
    destination = "C:\\Users\\Student\\Desktop\\updates"
    # time we will look back in hours
    hoursToReview = 24

    # run the funtions to get list of updates and copy them to destination
    updates = listUpdatedFiles(stagingYard, hoursToReview)
    copyFiles(updates, destination)

    # Then try getmtime - format and print for debug
    # print time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(filePath)))
