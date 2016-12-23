# Tkinter Action controls
## 1. Using Callback Functions via Command Property
If the GUI control widget has a command property, assign it to a callback to perform an action upon user interaction. A callback is a function that will be executed when the control is clicked. STRANGELY however, if we need to pass an argument, it is necessary to assign an anonymous and intermediary function, called *lambda*, to the command property instead. This is because, rather than the name reference of the callback function, the **command property** is assigned the return value of the callback function at instantiation, which is typically *none* and therefore results in no action when clicked. Lambda, however, will cause the callback function to execute until clicked and can pass an argument.

** Tk Widgets with Command Properties**
-  Button
-  Checkbutton
-  Radiobutton
-  Spinbox
-  Scale
-  Scrollbar (also xscroll and yscroll command properties)

##  2.  Binding Events to Handler Functions
The bind method uses a string parameter that equals a special formated representation of an Event Type, such as <Key>, <KeyPress>, <KeyPress-Delete>, <KeyRelease-Esc>, <Return> or <Control-c>,  followed by the name of the handler function which you wish to bind the event. Once again, if you wish to pass an argument to the handler, we will need to use the lambda function but this time we must allow lambda a parameter to receive the event object the bind method will pass.

Binding an event propogates down through children. It is only effective on window with focus, unless using bind.all

** Common Tk Event Types **
- ButtonPress
- ButtonRelease
- Enter
- Leave
- Motion
- KeyPress

## 3. Virtual Events
User defined events are called virtual events. These can consist of existing user configured virtual events such as <<copy>> is <Control-c>. You can define new virtual events as well and create event bindings.
