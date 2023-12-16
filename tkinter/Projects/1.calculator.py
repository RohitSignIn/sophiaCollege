from tkinter import *
root = Tk()

root.title("Calculator")

e = Entry(root)
e.grid(sticky='we', columnspan=4)

def handleNumberClick(num):
    newInsert = e.get() + str(num)
    e.delete(0, END)
    e.insert(0, newInsert)

def handleOperation(opr):
    global FirstNum
    global Operation
    FirstNum = e.get()
    e.delete(0, END)
    Operation = opr

def handleClear():
    e.delete(0, END)

def handleCalculation():
    currNum = e.get()
    e.delete(0, END)
    if(Operation == "+"):
        e.insert(0, int(float(FirstNum))+int(float(currNum)))
    elif(Operation == "-"):
        e.insert(0, int(float(FirstNum))-int(float(currNum)))
    elif(Operation == "*"):
        e.insert(0, int(float(FirstNum))*int(float(currNum)))
    elif(Operation == "/"):
        e.insert(0, int(float(FirstNum))/int(float(currNum)))



# For Numbers 
button1 = Button(root, text="1", width=8, pady=10, command=lambda: handleNumberClick(1))
button2 = Button(root, text="2", width=8, pady=10, command=lambda: handleNumberClick(2))
button3 = Button(root, text="3", width=8, pady=10, command=lambda: handleNumberClick(3))

button4 = Button(root, text="4", width=8, pady=10, command=lambda: handleNumberClick(4))
button5 = Button(root, text="5", width=8, pady=10, command=lambda: handleNumberClick(5))
button6 = Button(root, text="6", width=8, pady=10, command=lambda: handleNumberClick(6))

button7 = Button(root, text="7", width=8, pady=10, command=lambda: handleNumberClick(7))
button8 = Button(root, text="8", width=8, pady=10, command=lambda: handleNumberClick(8))
button9 = Button(root, text="9", width=8, pady=10, command=lambda: handleNumberClick(9))

button0 = Button(root, text="0", width=8, pady=10, command=lambda: handleNumberClick(0))

# For Operations 
buttonClr = Button(root, text="C", width=8, pady=10, command=handleClear)
buttonAdd = Button(root, text="+", width=8, pady=10, command=lambda: handleOperation("+"))
buttonSub = Button(root, text="-", width=8, pady=10, command=lambda: handleOperation("-"))
buttonMul = Button(root, text="*", width=8, pady=10, command=lambda: handleOperation("*"))
buttonDiv = Button(root, text="/", width=8, pady=10, command=lambda: handleOperation("/"))

buttonEqu = Button(root, text="=", width=8, pady=10, command=handleCalculation)


# GUI for Numbers 
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

# GUI for Operations
buttonClr.grid(row=1, column=3)
buttonAdd.grid(row=2, column=3)
buttonSub.grid(row=3, column=3)
buttonMul.grid(row=4, column=1)
buttonDiv.grid(row=4, column=2)
buttonEqu.grid(row=4, column=3)


root.mainloop()