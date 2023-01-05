from tkinter import *
# from PIL import Image,ImageTk

root = Tk()

# width x height
root.geometry("733x434");

# width, heigth
root.minsize(0,0)
root.maxsize(2000,2000)

# title
root.title("Unified Targeting System")

# PhotoImage
# for jpg
# image = Image.open("file_name.jpg")
# photo = ImageTk.photoImage(image)
# for png
# photo = PhotoImage(file="file_name.png")

# label 

# --------------------------------------- important label options ---------------------------------------
# text - add the Text 
# bg - background
# fg-foreground
# 1. font=("comicsansms", 19, "bold")
# 2. font=("comicsansms 19 bold") 
# padx - padding in x 
# paddy - padding in Y
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
# --------------------------------------- important pack options ---------------------------------------
# anchor = ne,nw,se,sw 
# side=BOTTOM, TOP(default), LEFT, RIGHT
# fill = X,Y 

# first_label = Label(text="❤❤Welcome to pycharm!❤❤", image=photo)
first_label = Label(text="❤❤Welcome to pycharm!❤❤", bg="black", fg="white", padx=113, pady=94, font=("comicsansms 19 bold"), borderwidth=5, relief=SUNKEN)

first_label.pack(side=BOTTOM, anchor="se", fill=X)
first_label.pack(side=LEFT, anchor="se", fill=Y, padx=40, pady=40)

root.mainloop()