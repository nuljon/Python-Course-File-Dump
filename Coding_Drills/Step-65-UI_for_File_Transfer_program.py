################################################################################
#   Python 3.5
#   Step 65 - Programming Drill from Python Course at The Tech Academy
#   by Jon Nuljon
#   December, 2016
################################################################################
# THE FOLLOWING IS FROM THE ORIGINAL PROGRAMMING DRILL DESCRIPTION
# Title: UI for File Transfer project - Python 3.4 - IDLE
# Scenario: You recently created a script that will check a folder for new or modified files,
# and then copy those new or modified files to another location.
# Users are asking for a user interface to make using the script easier and more versatile.
# Desired features of the UI:
#  Allow the user to browse to and choose a specific folder that will contain the
#    files to be checked daily.
#  Allow the user to browse to and choose a specific folder that will receive the
#    copied files.
#  Allow the user to manually initiate the 'file check' process that is performed by
#    the scrip.
#  You have been asked to create this UI.
#  Guidelines:
#   Use Python 3.4 for this drill.
#   Use tkinter to create the UI.
#   The layout of the UI is up to you.
#   You should use IDLE for this Drill.
###############################################################################
from tkinter import *
from tkinter import filedialog
import FolderMonitor

# the FolderMonitor module has two functions:
# listUpdatedFiles(folder, hours)
#   given a folder and #hours to detect modifications it returns list of files
# copyFiles(fileList, Folder)
#   given a list of files and a folder it will copy those files to that folder

'''
from tkinter import ttk
from datetime import *
import shutil
import os
'''


class FileTransferApp:

    def __init__(self, parent): # this will initialize the instance call to whatever parent we have sent -- most likely root
        self.parent = parent # and we make a reference to our parent property
        # we should title the window
        self.parent.title("The Tech Academy Python Course Step 65 App")
        self.container = Frame(parent) # and we are a frame to hold the rest of  the class properties and methods (widgets and callbacks)
        self.container.pack()   # it follows we should pack into our parent so we will be seen
        # lets get an image in here to brand my school
        logoLabel = PhotoImage(file='TheTechAcademyLogo.gif')
        # put in the first row (row=0) and in the 2nd column (column=1), align it to the left or W on the compass
        logo=Label(self.container, image=logoLabel)
        # now garbage collection is making label a blank space
        # we need to make a reference so we don't lose the image
        logo.image = logoLabel
        # now lets place it in container so its visible
        logo.grid(row = 0, column = 1)
        # we need another label for the stagingFolder
        stagingLabel = "Please enter the path to the files you wish check:"
        Label(self.container, text=stagingLabel).grid(row=1, column=0, columnspan=3, sticky=W)
        # we need a entry text box for entering the source folder we monitor
        self.stagingFolder = Entry(self.container)
        self.stagingFolder["width"] = 60 # set the width
        self.stagingFolder.focus_set()  # set the begining focus for user
        self.stagingFolder.grid(row=2,column=0, columnspan=2)
        # now we need a browse button so the user can browse for the folder
        # use lambda to pass our browse function a value - source
        Button(self.container, text="Browse", command=lambda: self.browse_folder("source")).grid(row=2, column=3) # put it on the right
        # we need another label for the destinationFolder
        destinationLabel = "Please enter the destination where you wish to copy your updates:"
        Label(self.container, text=destinationLabel).grid(row=3, column=0, columnspan=3, sticky=W)
        # we need a entry text box for entering the destination folder we monitor
        self.destinationFolder = Entry(self.container)
        self.destinationFolder["width"] = 60
        self.destinationFolder.grid(row=4,column=0, columnspan=2)
        # now we need a browse button so the user can browse for the folder
        # use lambda to pass our browse function a value - destination
        Button(self.container, text="Browse", command=lambda: self.browse_folder("destination")).grid(row=4, column=3) # put it on the right of the text field

        # we need another label for the user to input # of hours to review for new or modified files
        hoursLabel = "Please input the number of hours to review for new or modified files:"
        Label(self.container, text=hoursLabel).grid(row=5, column=0, columnspan=3, sticky=W)
        # we need a entry text box for entering the destination folder we monitor
        self.hours = Entry(self.container)
        self.hours["width"] = 2 # allow 2 digits to acquire 72 hours for weekends
        self.hours.grid(row=6,column=1,sticky=E)
        # now we need a button to execute the updates
        Button(self.container, text="Copy Updates", command=self.copyUpdates).grid(row=6, column=3) # put it on the right of the text field


    # the browse folder method requires we pass the folder we're browsing
    def browse_folder(self,folder):
            # lets spawn a browse widget with a title - assign result
            self.browseFolder = filedialog.askdirectory(title="Select a folder...")
            # check for which folder we're browsing
            if (folder == "source"):
                # this will set the text of the self.stagingFolder field
                self.stagingFolder.insert(0,self.browseFolder)
            elif (folder == "destination"):
                # this will set the text of the self.destinationFolder field
                self.destinationFolder.insert(0,self.browseFolder)
            else: # this should not execute - so something has gone wrong if here
                print("Something has gone wrong - browsing undefined folder")

    # the copy updates method reads our entry fields and calls FolderMonitor functions
    def copyUpdates(self):
        folder = self.stagingFolder.get()
        Hours = self.hours.get()
        if Hours:
            Hours=int(Hours)
        else:
            Hours = 24
        files = FolderMonitor.listUpdatedFiles(folder, int(Hours))
        folder = self.destinationFolder.get()
        FolderMonitor.copyFiles(files, folder)
        quit()










# this is the main program  as a function to be called only if necessary
def main():
    root = Tk()   # create the top level application window called root
    myFileTransferApp = FileTransferApp(root) # create  instance of the  App Class  passing root as parent
    root.mainloop()     #  enter mainloop method  of Tk() class from our root  instance   - eternally watches for an intersting event, that is an event that is bound to a widget

if __name__ == "__main__": main()       # this  is  only executed if file run directly - formed thus , this file can become  a module
