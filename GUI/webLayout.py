from tkinter import *
app = Tk()

app.geometry("800x600")
app.title("Web Layout")

app.grid_columnconfigure(0, weight=1)

# HEADER 
headerFrame = Frame(app, width=400, height=400, bg="red")
headerFrame.grid(row=0, column=0, sticky="ew")

headerFrame.columnconfigure(0, weight=1)

headerLabel = Label(headerFrame, text="Header", bg="red", font=("helvetica", 24), fg="#fff")
headerLabel.grid(row=0, column=0, pady="80")
# HEADER END 

mainFrame = Frame(app, width=400, height=400, bg="blue")
mainFrame.grid(row=1, column=0, sticky="ew")

mainFrame.columnconfigure(0, weight=1)
mainFrame.columnconfigure(1, weight=2)

sideFrame = Frame(mainFrame, width=400, height=400, bg="yellow")
sideFrame.grid(row=0, column=0, sticky="ew")

sideFrame.columnconfigure(0, weight=1)

contentFrame = Frame(mainFrame, width=400, height=400, bg="green")
contentFrame.grid(row=0, column=1, sticky="ew")

contentFrame.columnconfigure(0, weight=1)

app.mainloop()