######################################################################
#  Python 35-32
#  The Tech Academy - Python Course - GUI application design
#  Demo of filedialog widgett from tkinter module
#  adapted from generic code sample found on numerous web sites
#  by Jon Nuljon
#  December, 2016
#######################################################################
from tkinter import *       # import the module  that ships with Python for GUI  App  devs  - uses tcl framework
from tkinter import ttk   # import  ttk  specifically as it  holds classes for each of the standard widgets
from tkinter import filedialog
import datetime


class App:

    def __init__(self, master):
        self.master = master

        #call start to initialize to create the UI elemets
        self.start()

    def start(self):
        self.master.title("This is the title of the 'Window'")

        self.now = datetime.datetime.now()

        #CREATE A TEXT/LABEL
        #create a variable with text
        label01 = "This is some text"
        #put "label01" in "self.master" which is the window/frame
        #then, put in the first row (row=0) and in the 2nd column (column=1), align it to "West"/"W"
        Label(self.master, text=label01).grid(row=0, column=0, sticky=W)

        #CREATE A TEXTBOX
        self.filelocation = Entry(self.master)
        self.filelocation["width"] = 60
        self.filelocation.focus_set()
        self.filelocation.grid(row=1,column=0)

        #CREATE A BUTTON WITH "ASK TO OPEN A FILE"
        self.open_file = Button(self.master, text="Browse...", command=self.browse_file) #see: def browse_file(self)
        self.open_file.grid(row=1, column=1) #put it beside the filelocation textbox

        #CREATE RADIO BUTTONS
        RADIO_BUTTON = [
            ("This will display A", "A"),
            ("This will display B","B")
        ]

        #initialize a variable to store the selected value of the radio buttons
        #set it to A by default
        self.radio_var = StringVar()
        self.radio_var.set("A")

        #create a loop to display the RADIO_BUTTON
        i=0
        for text, item in RADIO_BUTTON:
            #setup each radio button. variable is set to the self.radio_var
            #and the value is set to the "item" in the for loop
            self.radio = Radiobutton(self.master, text=text, variable = self.radio_var, value = item)
            self.radio.grid(row=2, column=i)
            i += 1

        #now for a button
        self.submit = Button(self.master, text="Execute!", command=self.start_processing, fg="red")
        self.submit.grid(row=3, column=0)

    def start_processing(self):
        #more code here
        x=1

    def browse_file(self):
        #put the result in self.filename
        self.filename = filedialog.askopenfilename(title="Open a file...")

        #this will set the text of the self.filelocation
        self.filelocation.insert(0,self.filename)
root = Tk()             # create the top level application window called root
app = App(root)          # create  instance of the App class and set root as master
root.mainloop()         # call the event loop method for root - so it watches for interesting events
