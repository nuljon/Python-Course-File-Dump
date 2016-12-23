#!\C:\Users\Student\AppData\Local\Programs\Python\Python35-32
# deCalifornicator by Jon Nuljon Decemebr 2016
# an adaptation of  hello_local.py  by Barron Stone
# presenting Python GUI Development with Tkinter on lynda.com

from tkinter import *       # import the module  that ships with Python for GUI  App  devs  - uses tcl framework
from tkinter import ttk   # import  ttk  specifically as it  holds classes for each of the standard widgets 

class deCalifornicator:                 # define GUI application as a class so the  GUI can be a component within a larger OOP

    def __init__(self, master):     # all  tk objects are created with __init__ method requires we pass name of master window

        self.label = ttk.Label(master, text = "Where you from?")        # this is the master window  = root.label
        self.label.grid(row = 0, column = 0, columnspan = 2)        # this is the geometry for laying out children
        
        ttk.Button(master, text = "OR EE GUN",                                          # this is a button widget  labeld  OR EE GUN 
                   command = self.oregon_hello).grid(row = 1, column = 0) # this defines the event handler and button location

        ttk.Button(master, text = "WASH ING TON",                                # this is another button labeled  -  WASH ING TON
                   command = self.washington_hello).grid(row = 1, column = 1)   # this defines the event handler and button location

        ttk.Button(master, text = "CALLEE  FOR  iN  YA",                                # this is another button labeled  -  Cali FORNICATOR
                   command = self.california_hello).grid(row = 2, column = 0, columnspan=2)   # this defines the event handler and button location

    def oregon_hello(self):                                                                         # handler for OR EE GUN
        self.label.config(text = 'Where you going with all that beer?')

    def washington_hello(self):                                                                 # handler for WASH ING TON
        self.label.config(text = "Years before my founding, father George was dead!")

    def california_hello(self):                                                                 # handler for  Cali FORNICATOR
        self.label.config(text = "Turn that thing the other way! Californicator")
            
def main():            #this is the main program  as a function
    
    root = Tk()             # create the top level application window called root
    app = deCalifornicator(root)        # create  instance of the  HelloApp Class  pass (root) as master
    root.mainloop()     #  emter mainloop metod  of Tk() class from out root  instance   - waits for event
    
if __name__ == "__main__": main()       # here  is  only executed if file run directly - formed thus , this file can become  a module for the  deCalifornicator class
