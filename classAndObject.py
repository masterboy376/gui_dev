from tkinter import *

# root=self -> in class
# root=window -> in main

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x400")
    
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusbar = Label(self, textvariable=self.var, relief=SUNKEN, anchor="w")
        self.statusbar.pack(fill=X, side=BOTTOM)

    def btnClick(self):
        self.var.set("working...")
        self.statusbar.update()
        import time
        time.sleep(2)
        self.var.set("Ready")

    def btnCreate(self, text):
        Button(text=text, command=self.btnClick).pack()

if __name__ == '__main__':
    window = GUI()

    window.status()
    window.btnCreate("work")

    window.mainloop()