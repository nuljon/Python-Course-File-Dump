################################################################################
#   Python 3.5
#   Step 66 - Programming Drill from Python Course at The Tech Academy
#   by Jon Nuljon
#   December, 2016
#
#  This softeware program is dedicated to Norman Olds Jr. died December 19 2016
#  In his honour I pursure graphic interface design and user control styling
#  Norman was a graphic artist and a my creative partner among other things
################################################################################
#  THE FOLLOWING IS FROM THE ORIGINAL PROGRAMMING DRILL DESCRIPTION
#  Title: Database functionality for File Transfer - Python 3.4 – IDLE
#  Scenario: You recently created a script that will check a folder for new or
#  modified files, and then copy those new or modified files to another location.
#  You also created a UI that makes using the script easier and more versatile.
#  Users are reporting issues with the current system you've made. Specifically,
#  they are having to manually initiate the 'file check' script at the same time
#  each day. Because they aren't doing this at the EXACT same time each day, some
#  files that were edited right around the time the script was meant to be run were
#  missed, and weren't copied to the outgoing files destination. This means you
#  will have to provide for recording the last time the 'file check' process was
#  performed, so that you can be sure to cover the entire time period in which new
#  or edited files could occur. To do this, you will need to create a database with
#  a table that can store the date and time of the last 'file check' process. That
#  way, you can use that date/time as a reference point in terms of finding new or
#  modified files. As part of this project, the users are asking that their UI
#  display the date and time of the last 'file check' process. You have been asked
#  to implement this functionality. This means that you will need to
#  • create a database and a table
#  • modify your script to both record date/time of 'file check' runs and to
#    retrieve that data for use in the 'file check' process, and
#  • modify the UI to display the last 'file check' date/time
#
#  Guidelines:
#  Use Python 3.4 for this drill.
#  Use sqlite for your database functionality.
#  Use tkinter module for the UI.
#  The layout of the UI is up to you.
#  You should use IDLE or any text editor that you are comfortable with for the
#   Drill.
###################################################################################
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from datetime import datetime
#from Pillow import Image, ImageTk
import FolderMonitor

# this is the Application Class for the FileTransferApp
# all of the GUI layout and controls are contained in here
class FileTransferApp:

    def __init__(self, parent): # this will initialize the instance call to whatever parent we have sent -- most likely root
        self.parent = parent # and we make a reference to our parent property
        # we should title the window
        self.parent.title("The Tech Academy Python Course Step 65 App")
        self.container = ttk.Frame(parent) # and we are a frame to hold the rest of  the class properties and methods (widgets and callbacks)
        self.container.pack()   # it follows we should pack into our parent so we will be seen
        # lets get an image in here to brand my school
        #pilImage = Image.open("TheTechAcademyLogo.png")
        #logolabel = ImageTk.PhotoImage(pilImage)
        logoLabel = PhotoImage(file='TheTechAcademyLogo.png')
        # put in the first row (row=0) and in the 2nd column (column=1), align it to the left or W on the compass
        self.logo=ttk.Label(self.container, image=logoLabel)
        # now garbage collection is making label a blank space
        # we need to make a reference so we don't lose the image
        self.logo.image = logoLabel
        # now lets place it in container so its visible
        self.logo.grid(row = 0, column = 0, columnspan=3)
        # we need another label for the stagingFolder
        stagingLabel = "Please enter or browse the folder you want checked for updated files:"
        ttk.Label(self.container, text=stagingLabel).grid(row=1, column=0, columnspan=2, sticky=W)
        # we need a entry text box for entering the source folder we monitor
        self.stagingFolder = ttk.Entry(self.container)
        self.stagingFolder["width"] = 60 # set the width
        self.stagingFolder.focus_set()  # set the begining focus for user
        self.stagingFolder.grid(row=2,column=0, columnspan=2, sticky=E)
        # now we need a browse button so the user can browse for the folder
        # use lambda to pass our browse function a value - source
        ttk.Button(self.container, text="Browse", command=lambda: self.browse_folder("source")).grid(row=2, column=2, sticky=W) # put it on the right
        # we need another label for the destinationFolder
        destinationLabel = "Please enter the destination where you wish to copy your updates:"
        ttk.Label(self.container, text=destinationLabel).grid(row=3, column=0, columnspan=2, sticky=W)
        # we need a entry text box for entering the destination folder we monitor
        self.destinationFolder = ttk.Entry(self.container)
        self.destinationFolder["width"] = 60
        self.destinationFolder.grid(row=4,column=0, columnspan=2, sticky=E)
        ttk.Button(self.container, text="Browse", command=lambda: self.browse_folder("destination")).grid(row=4, column=2, sticky=W) # put it on the right
        # get the last Update
        self.lastUpdate = FolderMonitor.getLastUpdate()
        # if it is datetime
        if isinstance(self.lastUpdate,datetime):
            # assign it as formatted tect to show the user
            updateText=self.lastUpdate.ctime()
        else:   #it's a string already, let's split off the microseconds
            updateListText=self.lastUpdate.split('.',1)
            # assign the text to show the user
            updateText=updateListText[0]
        # display labelFrame to enclose updateText
        self.labelframe = ttk.LabelFrame(self.container, text='Last update:', width=500, height=100, style='update.TLabelframe')
        self.labelframe.grid(row=5, column=0,columnspan=2, rowspan=2,sticky=W)
        self.updateLabel=ttk.Label(self.labelframe, text=updateText)
        self.updateLabel.pack()

        # now we need a button to execute the file check and copy updates
        ttk.Button(self.container, text="Check For File Updates", command=self.copyUpdates, style='Gold.TButton').grid(row=5, column=2, rowspan=2, sticky=W) # right of the text field

        # format our datetime update
        cupdate = datetime.now()
        labelText = cupdate.strftime("%A %I:%M %p")
        # make a label frame with our destination as label
        self.filesDisplayLabel = ttk.LabelFrame(self.container, text=labelText,
                                                width=510, style='update.TLabelframe')
        # place it in the grid so we can see it - span all 3 columns
        self.filesDisplayLabel.grid(row=7, column=0, columnspan = 3)
        # assign a property to reference our listbox which is 80 chars wide
        self.filesDisplay=Listbox(self.filesDisplayLabel, width=85)
        # make it visible by packing it into the labelframe
        self.filesDisplay.pack()

        # now lets call our styling method to make it look good
        self.styling()

    # create method for grouping the styling code
    def styling(self):
        # style object to  capture our style settings
        style = ttk.Style()

    ########################################################################
    #        these are for debug and information
    #
    #    print(style.theme_names())         # gives available style name values
    #    print(self.labelframe.winfo_class())   # gives the layout organization
    #    print(style.element_options('LabelFrame.label'))   # all settable opts
    #    print(style.layout('TLabelframe'))       # the layout control elements

        #style.theme_use('classic')              # assign 1 theme for use
        #style.theme_use('vista')
        #style.theme_use('xpnative')
        style.theme_use('winnative')
        #style.theme_use('default')
        #style.theme_use('clam')
        #style.theme_use('alt')

        self.container.configure(padding=30)   # margin for main window
        self.logo.configure(padding=10)        # space around the graphic
        style.configure('update.TLabelframe', borderwidth=10, relief=SUNKEN)
        style.configure('TButton',padding=5)   # space around the buttons
        self.updateLabel.configure(style='Frame.TLabel')
        style.configure('Frame.TLabel', width=57, anchor='CENTER')
        #style.configure('Gold.TButton', background="gold")
        style.configure('Gold.TButton', foreground = 'green',
                        font = ('Arial', 9, 'bold'))
        style.map('Gold.TButton', background = [('pressed', 'white'),
                                                 ('active', 'gold'),
                                                 ('focus','green')])
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

    # this method contains the main sequence of code execution for the class
    # Here we get data from the class widgets, call functions from our module FolderMonitor.py and output a debug trace to the console
    def copyUpdates(self):
        # if lastUpdate is a string then make a datetime object, assign and output
        if isinstance(self.lastUpdate, str):
            update = datetime.strptime(self.lastUpdate, "%Y-%m-%d %H:%M:%S.%f")
            print("from datime.strptime") #debug

        # if lastUpdate is a datetime object then assign and output
        elif isinstance(self.lastUpdate,datetime):
            update = self.lastUpdate
            print(str(update) + "self.lastUpdate") # debug

        # get the staging folder
        folderS = self.stagingFolder.get()
        print (folderS) # debug

        # get the destination folder
        folderD= self.destinationFolder.get()
        print (folderD) # debug

        # call function to check for files we need to update
        files = FolderMonitor.listFilesToUpdate(folderS,update)
        print ("\n---> Files to be copied: ") # debug
        print (files)
        #initialize row counter
        row = 1
        # assign text for first row: we made some copies
        topText = "Your update order generated the following copies of your files for transfer: "
        # insert the update message into first line of the listbox
        self.filesDisplay.insert(row,topText)
        for item in files:
            # insert a row in our gui message box
            row=row+1
            self.filesDisplay.insert(row,item)

        # copy the files
        FolderMonitor.copyFiles(files, folderD)
        print("\n---> No errors on the copy attempt") #  debug

        # we can assign a new datetime for our Log
        update = datetime.now()

        # package data as a tuple of strings and handoff to log
        dataPackage = (str(update),str(files),folderS,folderD)
        print("\n---> LOG DATA PACKAGE: ") # debug
        print(dataPackage)
        FolderMonitor.logData(dataPackage)
        # quit, we're done!
        #quit()

# this is the main program  as a function to be called only if necessary
def main():
    root = Tk()   # create the top level application window called root
    myFileTransferApp = FileTransferApp(root) # create  instance of the  App Class  passing root as parent
    root.mainloop()     #  enter mainloop method  of Tk() class from our root  instance   - eternally watches for an intersting event, that is an event that is bound to a widget

if __name__ == "__main__": main()       # this  is  only executed if file run directly - formed thus , this file can become  a module
