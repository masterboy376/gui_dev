from tkinter import *

root = Tk()
root.geometry("800x400")

def getVal():
    with open("data/foodChoice.txt","a") as f:
        f.write(f"{var.get()}\n")

var = IntVar()
var.set(1)

Label(root, text="what would you like to have sir?", justify = LEFT, padx=14, font="lucida 19 bold").pack()

r = Radiobutton(root, text = "Dosa", padx=14, variable=var, value=1).pack()
r = Radiobutton(root, text = "Paratha", padx=14, variable=var, value=2).pack()
r = Radiobutton(root, text = "Samosa", padx=14, variable=var, value=3).pack()
r = Radiobutton(root, text = "Momos", padx=14, variable=var, value=4).pack()
Button(root, text="send", command=getVal).pack()

root.mainloop()