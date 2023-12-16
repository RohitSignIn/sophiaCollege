from tkinter import *

root = Tk()

def clickMe():
    Label(root, text=e.get()).pack()

def enterLabel():
    Label(root, text="Got Clicked").pack()

e = Entry(root, fg="white", bg="black", width=50)
e.pack()
e.insert(0, "Enter your name: ")

Button(root, text="Submit", padx=50, pady=10, command=clickMe).pack()

root.mainloop()