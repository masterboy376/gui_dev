from tkinter import *

root = Tk()
root.geometry("800x400")

def getVal():
    with open("data/rating.txt","a") as f:
        f.write(f"{s.get()}\n")

# s = Scale(root, from_=0, to=455)
# s = Scale(root, from_=0, to=455, orient=HORIZONTAL)
s = Scale(root, from_=0, to=10, orient=HORIZONTAL, tickinterval=2)
s.set(5)
s.pack()
Button(root, text="Rate", command=getVal).pack()

root.mainloop()