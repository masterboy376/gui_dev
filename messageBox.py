from tkinter import *
import tkinter.messagebox as tmsg
root = Tk()

def help():
    tmsg.showinfo("help", "i will help you")
def ques():
    a = tmsg.askquestion("my question", "was your experience good?")
    print(a)
    msg=""
    if(a=="yes"):
        msg="rate us on play store"
    else:
        msg="sorry for that, will call you soon"
    tmsg.showinfo("we say", msg)
def beFri():
    a = tmsg.askretrycancel("divya se dosti kar lo", "sorry divya nhi banegi apki dost")
    print(a)
    if(a):
        print("koi fayda ni hoga retry ka")
    else:
        print("mature decision")

root.geometry("800x400")

# non drop down menu 
# myMenu = Menu(root)
# myMenu.add_command(label="File", command=quit)
# myMenu.add_command(label="Exit", command=quit)
# root.config(menu = myMenu)

# drop down menu 
drp = Menu(root)
m1 = Menu(drp, tearoff=0)
m1.add_command(label="save", command=quit)
m1.add_command(label="save as", command=quit)
m1.add_command(label="print", command=quit)
m1.add_separator()
m1.add_command(label="delete", command=quit)
m1.add_command(label="rename", command=quit)
drp.add_cascade(label="File", menu = m1)

m2 = Menu(drp, tearoff=0)
m2.add_command(label="help", command=help)
m2.add_command(label="question", command=ques)
m2.add_command(label="befriend divya", command=beFri)
drp.add_cascade(label="Edit", menu = m2)

root.config(menu=drp)

root.mainloop()