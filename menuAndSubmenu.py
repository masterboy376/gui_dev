from tkinter import *
root = Tk()

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
root.config(menu=drp)

root.mainloop()