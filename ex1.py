from tkinter import *
from PIL import Image,ImageTk

root = Tk()

# -------------------------------------------design and logic start-------------------------------------------
root.title("Top News On Your Desk")

root.geometry("900x650")
root.minsize(900,650)

interface_header = Label(text="Top News On Your Desk", pady=10, font=("comicsansms 20 bold"))
interface_header.pack()
interface_header = Label(text="Top News On Your Desk", pady=10, font=("comicsansms 15"))
interface_header.pack()

f1 = Frame(root, padx=10, pady=10)
f1.pack(side=TOP, fill=X)
f2 = Frame(root, padx=10, pady=10)
f2.pack(side=TOP, fill=X)
f3 = Frame(root, padx=10, pady=10)
f3.pack(side=TOP, fill=X)

img= (Image.open("assets/%s.png"%(1)))
resized_image= img.resize((150,100))
i1 = ImageTk.PhotoImage(resized_image)

img= (Image.open("assets/%s.png"%(2)))
resized_image= img.resize((150,100))
i2 = ImageTk.PhotoImage(resized_image)

img= (Image.open("assets/%s.png"%(3)))
resized_image= img.resize((150,100))
i3 = ImageTk.PhotoImage(resized_image)

l1 = Label(f1, image=i1)
l1.pack(side=LEFT)
l1 = Label(f2, image=i2)
l1.pack(side=LEFT)
l1 = Label(f3, image=i3)
l1.pack(side=LEFT)

read1 = ""
read2 = ""
read3 = ""

with open("assets/1.txt",'r',encoding = 'utf-8') as f:
   read1 = f.readline()
with open("assets/2.txt",'r',encoding = 'utf-8') as f:
   read2 = f.readline()
with open("assets/3.txt",'r',encoding = 'utf-8') as f:
   read3 = f.readline()

l1 = Label(f1, text=read1, wraplength=700)
l1.pack(side=RIGHT)
l1 = Label(f2, text=read2, wraplength=700)
l1.pack(side=RIGHT)
l1 = Label(f3, text=read3, wraplength=700)
l1.pack(side=RIGHT)
# -------------------------------------------design and logic end-------------------------------------------

root.mainloop()