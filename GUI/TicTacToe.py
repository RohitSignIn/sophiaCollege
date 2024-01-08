from tkinter import *

app = Tk()
app.geometry("800x600")
app.title("Tic Tac Toe")

app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

MainFrame = Frame(app, bg="#2d2d2d")
MainFrame.grid(row=0, column=0, sticky="ewns")


MainFrame.grid_columnconfigure(0, weight=1)
MainFrame.grid_rowconfigure(0, weight=1)

tictactoeFrame = Frame(MainFrame, width=400, height=400, bg="red")
tictactoeFrame.grid(row=0, column=0, sticky="ew")

app.mainloop()