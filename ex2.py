from tkinter import *

root = Tk()

width = 800;
height = 400;


def resize():
    root.geometry(f"{widthValue.get()}x{heightValue.get()}")

root.geometry(f"{width}x{height}")

widthLabel = Label(root, text="width")
heightLabel = Label(root, text="height")

widthValue = StringVar()
heightValue = StringVar()
widthEntry = Entry(root, textvariable=widthValue)
heightEntry = Entry(root, textvariable=heightValue)

widthLabel.pack()
widthEntry.pack()
heightLabel.pack()
heightEntry.pack()

btn = Button(root, text="resize", command=resize)
btn.pack()

root.mainloop()
