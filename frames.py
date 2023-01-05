from tkinter import *

root = Tk()

# -------------------------------------------design and logic start-------------------------------------------
root.title("Top News On Your Desk")

root.geometry("900x650")
root.minsize(900,650)

f1 = Frame(root, bg="gray", borderwidth=2, relief=SUNKEN, padx=30)
f1.pack(side=LEFT, fill=Y)
f2 = Frame(root, bg="blue", borderwidth=2, relief=SUNKEN, padx=30)
f2.pack(side=TOP, fill=X)
l1 = Label(f1, text="poject tkinter - Pycharm", bg="gray")
l1.pack()
l1 = Label(f2, text="poject tkinter - Pycharm", bg="blue")
l1.pack()
# -------------------------------------------design and logic end-------------------------------------------

root.mainloop()