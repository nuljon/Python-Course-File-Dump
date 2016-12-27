# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

root = Tk()

button1 = ttk.Button(root, text = 'Button 1')
button2 = ttk.Button(root, text = 'Button 2')
button1.pack()
button2.pack()

style = ttk.Style()     #create style object to  capture oure style settings

print(style.theme_names())      # gives available style name values
print(style.theme_use())        # assign  theme for use
style.theme_use('classic')
style.theme_use('vista')
#style.theme_use('clam')

print(button1.winfo_class())
style.configure('TButton', foreground = 'blue')
style.configure('Alarm.TButton', foreground = 'red',
                font = ('Arial', 24, 'bold'))
button2.configure(style = 'Alarm.TButton')
style.map('Alarm.TButton', foreground = [('pressed', 'pink'),
                                         ('disabled', 'grey')])
#button2.state(['disabled'])

print(style.layout('TButton')) #lists  elements in a style
print(style.element_options('Button.label')) #lists  available for customization
print(style.lookup('TButton', 'foreground')) #lookups style TButton foreground setting

root.mainloop()
