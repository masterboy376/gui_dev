from tkinter import *

root = Tk()

root.geometry("655x444")
root.title("Title")
root.wm_iconbitmap("icon.ico")
root.configure(background="grey")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
print(f"{w}x{h}")
Button(text="close1", command=root.destroy).pack()
Button(text="close2", command=quit).pack()


root.mainloop()