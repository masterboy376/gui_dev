from tkinter import *

root = Tk()

def getVals():
    print(userValue.get())
    print(passValue.get())

root.geometry("655x333")

username = Label(root, text="username")
password = Label(root, text="password")

username.grid()
password.grid(row=1)

# variable classes in tkinter
# BooleanVar,DoubleVar,IntVar,StringVar

userValue = StringVar()
passValue = StringVar()

userEntry = Entry(root, textvariable=userValue)
passEntry = Entry(root, textvariable=passValue)

userEntry.grid(column=1, row=0)
passEntry.grid(column=1, row=1)

Button(text="Submit", command=getVals).grid()

root.mainloop()