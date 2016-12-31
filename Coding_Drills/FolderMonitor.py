###############################################################################
#   Python 3.5
#   Step 66 - Programming Drill from Python Course at The Tech Academy
#   by Jon Nuljon
#   December, 2016
###############################################################################
#   Module containing functions to support the Class FileTransferApp
#
#   FolderMonitor.
#         listUpdatedFiles
#                   - checks a given folder for updates within a given # of hours
#         listFilesToUpdate
#                   - checks a given folder for updates since a given timestamp
#         copyFiles
#                   - copies a list of files to a destination unless they exist
#         logData
#                   - stores the datetime of updates and other details in db
#         getLastUpdate
#                   - retrieves the datetime of last update from db
#         getDefaultValue
#                   - provides a default value of 24 hours for last update
#         closeDb
#                   - closes the updateLog.db connection
#
################################################################################
import os
from datetime import *
import shutil
import sqlite3

# function for storage of update details - time, files updated, folders used
def logData (dataPackage):
    # open a sqlite db
    with sqlite3.connect('updateLog.db') as connection:
        # assign the cursor for easy reference
        c = connection.cursor()
        # create the table if not already done
        c.execute("CREATE TABLE IF NOT EXISTS Log(updateTime TEXT, fileList TEXT, stagingFolder TEXT, destinationFolder TEXT)")
        # insert the data we were passed
        c.execute("INSERT INTO Log VALUES(?,?,?,?)", dataPackage)
        # commit changes and close connection to db
        connection.commit()


# function to retrieve the Max updateTime
def getLastUpdate():
    # preload a table check constant with SQLite code
    table_check = "SELECT name FROM sqlite_master WHERE type='table' AND name='Log';"
    # open a sqlite db
    with sqlite3.connect('updateLog.db') as connection:
        # assign the cursor for easy reference
        c = connection.cursor()
        # check if we have the Log yet
        c.execute(table_check)
        # fetch the first result as table
        table=c.fetchone()
        # if nothing is there
        print(table,) #debug
        if not table:
            # we don't have the Log table yet so this must be our first run
            # we will use default values
            update=getDefaultValue()
            print (str(update) + " default value since no Log \n***") # debug
            return(update) # so return the default
        else:   # we must have a Log table
            # query Log for data - specifically the last updateTime
            c.execute("SELECT updateTime FROM Log ORDER BY updateTime DESC LIMIT 1")
            # lets fetch the update returned by our query
            update = c.fetchone()
            if not update:  # the query of Log table returned None so use default
                update = getDefaultValue()
                print(str(update) + " default value since Log empty\n***") # debug
                return(update) # so return the default
            # the update appears to be from the Log so break it out of the tuple
            update, = update
            # debug output
            print (str(update) + " from the Log table of our db\n")
    # return the result of query, i.e. the last update from the Log
    return(update)

# function to return default value for last update
def getDefaultValue():
    # assign default to update - i.e. 24 hours ago
    update = datetime.now() - timedelta(hours=24)
    return(update)

# function to close the db connection
def closeDb():
    connection.close()

# a function listing updated files in a folder since last update
def listFilesToUpdate (folder, lastUpdate):
    # lets calc review time limt
    review  = lastUpdate
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

# this is the main program and will not execute unless this file is executed from the command line or by double clicking from a file manager. Currently it is set to output a brief message and close since this file was written to serve as a support module
def main():
    print ("\nDON'T TRY TO RUN ME. I AM A MODULE AND DO NOT WORK UP FRONT!\n")
    quit()

if __name__ == "__main__": main()
# main() is  only executed if this file is run from the command line
