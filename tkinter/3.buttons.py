from tkinter import *

root = Tk()

def enterLabel():
    Label(root, text="Got Clicked").pack()

Button(root, text="Click Me", padx=50, pady=10, command=enterLabel).pack()

root.mainloop()