from tkinter import *

root = Tk()

# label1 = Label(root, text="Hello Buddy")
# label2 = Label(root, text="Hello Buddy1")

label1 =Label(root, text="Hello Buddy")
label2 =Label(root, text="Hello Buddy1")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)

root.mainloop()