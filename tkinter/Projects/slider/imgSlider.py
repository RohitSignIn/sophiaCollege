from tkinter import *
from PIL import Image, ImageTk

root = Tk()



img1 = Image.open("./1.png").resize((600, 400))
img2 = Image.open("./2.png").resize((600, 400))
img3 = Image.open("./3.png").resize((600, 400))
img4 = Image.open("./4.jpg").resize((600, 400))
img5 = Image.open("./5.jpg").resize((600, 400))
img6 = Image.open("./6.jpg").resize((600, 400))


images =(
    img1,
    img2,
    img3,
    img4,
    img5,
    img6
)

def handleNext(indx):
    global nextBtn
    global prevBtn

    showImage(indx)

    if(indx == 5):
        nextBtn = Button(root, text="Next", state="disabled")
    else:
        nextBtn = Button(root, text="Next", command=lambda:handleNext(indx+1))

    prevBtn = Button(root, text="Prev", command=lambda:handlePrev(indx-1))

    prevBtn.grid(row=1, column=0)
    nextBtn.grid(row=1, column=1)

def handlePrev(indx):
    global nextBtn
    global prevBtn

    showImage(indx)

    if(indx == 0):
        prevBtn = Button(root, text="Prev", state="disabled")
    else:
        prevBtn = Button(root, text="Prev", command=lambda:handlePrev(indx-1))

    NextBtn = Button(root, text="Next", command=lambda:handleNext(indx+1))

    nextBtn.grid(row=1, column=0)
    prevBtn.grid(row=1, column=1)

def showImage(indx):
    print(indx)
    im = ImageTk.PhotoImage(images[indx])
    imgLabel = Label(root, image=im)
    imgLabel.image = im
    imgLabel.grid(row=0, column=0, columnspan=2)


showImage(0)

nextBtn = Button(root, text="Next", command=lambda:handleNext(1))

prevBtn = Button(root, text="Prev", state="disabled")

prevBtn.grid(row=1, column=0)
nextBtn.grid(row=1, column=1)

root.mainloop()