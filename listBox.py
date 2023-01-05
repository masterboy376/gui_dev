from tkinter import *

root = Tk()
root.geometry("800x400")

i=0;

def add():
    global i # to modify value of global variable in a func
    lbx.insert(ACTIVE, f"{i}")
    i+=1

lbx = Listbox(root)
lbx.pack()
lbx.insert(END, "first")
Button(root, text="add", command=add).pack()

root.mainloop()