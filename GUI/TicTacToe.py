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

def handleBtnClick(btnNum):
    print(btnNum)

def initialStruc():
    btn0 = Button(tictactoeFrame, width=8, height=4, bg="#fff", command=lambda: handleBtnClick(0))
    
    btn1 = Button(tictactoeFrame, width=8, height=4, bg="#fff", command=lambda: handleBtnClick(1))
    
    btn2 = Button(tictactoeFrame, width=8, height=4, bg="#fff", command=lambda: handleBtnClick(2))
    
    btn3 = Button(tictactoeFrame, width=8, height=4, bg="#fff", command=lambda: handleBtnClick(3))
    
    btn4 = Button(tictactoeFrame, width=8, height=4, bg="#fff", command=lambda: handleBtnClick(4))
    
    btn5 = Button(tictactoeFrame, width=8, height=4, bg="#fff", command=lambda: handleBtnClick(5))
    
    btn6 = Button(tictactoeFrame, width=8, height=4, bg="#fff", command=lambda: handleBtnClick(6))

    btn7 = Button(tictactoeFrame, width=8, height=4, bg="#fff", command=lambda: handleBtnClick(7))
    
    btn8 = Button(tictactoeFrame, width=8, height=4, bg="#fff", command=lambda: handleBtnClick(8))

    btn0.grid(row=0, column=0, padx=5, pady=5)
    btn1.grid(row=0, column=1, padx=5, pady=5)
    btn2.grid(row=0, column=2, padx=5, pady=5)
    btn3.grid(row=1, column=0, padx=5, pady=5)
    btn4.grid(row=1, column=1, padx=5, pady=5)
    btn5.grid(row=1, column=2, padx=5, pady=5)
    btn6.grid(row=2, column=0, padx=5, pady=5)
    btn7.grid(row=2, column=1, padx=5, pady=5)
    btn8.grid(row=2, column=2, padx=5, pady=5)
    


tictactoeFrame = Frame(MainFrame, width=400, height=400, bg="#2d2d2d")
tictactoeFrame.grid(row=0, column=0)


initialStruc()


app.mainloop()