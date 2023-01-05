from tkinter import *
 
root = Tk()

def hello():
    print("hi i am tkinter")

root.geometry("655x333")
frame = Frame(root, borderwidth=6, bg="gray", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame, bg="black", fg="white", text="print now", command=hello)
b1.pack()

root.mainloop()
