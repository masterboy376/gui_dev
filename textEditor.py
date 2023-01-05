from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.h=int(355)
        self.w=int((self.h)*7/4)
        self.geometry(f"{self.w}x{self.h}")
        self.title("Untitled - Notepad")
        self.wm_iconbitmap("icon.ico")
        self.file = None

    def newFile(self):
        self.title("Untitled - Notepad")
        self.file = None
        self.textArea.delete(1.0,END)

    def openFile(self):
        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
        if self.file=="":
            self.file = open
        else:
            self.title(os.path.basename(self.file) + " - Notepad")
            self.textArea.delete(1.0,END)
            f = open(self.file, "r")
            self.textArea.insert(1.0,f.read())
            f.close()

    def saveFile(self):
        if self.file==None:
            self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
            if self.file=="":
                self.file=None
            else:
                f = open(self.file, 'w')
                f.write(self.textArea.get(1.0,END))
                f.close()
                self.title(os.path.basename(self.file) + " - Notepad")
        else:
            f = open(self.file, 'w')
            f.write(self.textArea.get(1.0,END))
            f.close()
            self.title(os.path.basename(self.file) + " - Notepad")

    def saveAsFile(self):
        self.file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt")])
        if self.file=="":
            self.file=None
        else:
            f = open(self.file, 'w')
            f.write(self.textArea.get(1.0,END))
            f.close()
            self.title(os.path.basename(self.file) + " - Notepad")

    def quitApp(self):
        self.destroy()

    def cut(self):
        self.textArea.event_generate(("<<Cut>>"))

    def copy(self):
        self.textArea.event_generate(("<<Copy>>"))

    def paste(self):
        self.textArea.event_generate(("<<Paste>>"))

    def textAreaCreate(self):
        self.textArea = Text(self, font="lucida 13", borderwidth=0)
        scrollbar = Scrollbar(self.textArea)
        scrollbar.pack(side=RIGHT,fill=Y)
        scrollbar.config(command=self.textArea.yview)
        self.textArea.config(yscrollcommand=scrollbar.set)
        self.textArea.pack(expand=True, fill=BOTH)
    
    def menuBarCreate(self):
        self.menuBar = Menu(self)
        # file menu strats
        self.fileMenu = Menu(self.menuBar, tearoff=0)
        self.fileMenu.add_command(label="New", command=self.newFile)
        self.fileMenu.add_command(label="Open", command=self.openFile)
        self.fileMenu.add_command(label="Save", command=self.saveFile)
        self.fileMenu.add_command(label="Save as", command=self.saveAsFile)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.quitApp)

        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        # file menu ends

        # edit menu starts
        self.editMenu = Menu(self.menuBar, tearoff=0)
        self.editMenu.add_command(label="Cut", command=self.cut)
        self.editMenu.add_command(label="Copy", command=self.copy)
        self.editMenu.add_command(label="Paste", command=self.paste)

        self.menuBar.add_cascade(label="Edit", menu=self.editMenu)
        # edit menu ends

        self.config(menu=self.menuBar)
        

if __name__ == '__main__':
    window = GUI()

    window.menuBarCreate()
    window.textAreaCreate()

    window.mainloop()