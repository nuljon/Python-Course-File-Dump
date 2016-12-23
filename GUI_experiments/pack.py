# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

ttk.Label(root, text = 'Yellow',
          background = 'yellow').pack(side = LEFT, anchor = 'nw')
ttk.Label(root, text = 'blue',
          background = 'blue').pack(side = LEFT, padx = 10, pady = 10)
label = ttk.Label(root, text = 'green',
          background = 'green')
label.pack(side = LEFT, ipadx = 10, ipady = 10)
print(label)

for widget in root.pack_slaves():  # returns list of all widgets managed by root pack manager
    widget.pack_configure(fill = BOTH, expand = True)
    print(widget.pack_info())  # returns the pack related attribute name:value pairs for the managed widgets

label.pack_forget() # the label.pack will get forgotten

root.mainloop()
