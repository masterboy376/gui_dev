from tkinter import *

root = Tk()
root.geometry("800x400")

def upload():
    statusVar.set("working...")
    sbar.update() # neccesary, otherwise tkinter will ignore this
    import time
    time.sleep(2)
    statusVar.set("ready")

statusVar = StringVar()
statusVar.set("ready")

sbar = Label(root, textvariable=statusVar, relief=SUNKEN, anchor="w")
sbar.pack(side=BOTTOM, fill=X)

Button(root, text="Upload", command=upload).pack()

root.mainloop()