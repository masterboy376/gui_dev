from tkinter import *

class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.h=int(500)
        self.w=int((self.h)*3/5)
        self.minsize(self.w,self.h)
        self.maxsize(self.w,self.h)
        self.geometry(f"{self.w}x{self.h}")
        self.title("Calculator")
        self.wm_iconbitmap("icon.ico")
        self.configure(background="#333333")

    def btnClick(self,event):
        text = event.widget.cget("text")
        if text=="=":
            try:
                if self.screenVal.get().isdigit():
                    value = int(self.screenVal.get())
                else:
                    value = eval(self.screenVal.get())
                self.screenVal.set(value) 
                self.screen.update()
            except:
                self.screenVal.set("invalid!") 
                self.screen.update()
                import time
                time.sleep(2)
                self.screenVal.set("") 
                self.screen.update()
        elif text=="C":
            self.screenVal.set("") 
            self.screen.update()
        elif text=="<":
            str = self.screenVal.get()
            self.screenVal.set(str[:len(str)-1]) 
            self.screen.update()
        else:
            self.screenVal.set(self.screenVal.get()+text) 
            self.screen.update()

    def btnLeftCreate(self, text, parent):
        if text!="":
            b = Button(parent, text=text, font="lucida 25 bold", borderwidth=0, bg="#1B2125", fg="#F5F5F5", width=3, height=1)
            b.bind("<Button-1>", self.btnClick)
            b.pack(side=LEFT, padx=2, pady=2)

    def frameCreate(self):
        return Frame(self,bg="#333333")
    

    def displayCreate(self):
        self.screenVal = StringVar()
        self.screenVal.set("")
        f = self.frameCreate()
        self.screen = Entry(f, textvariable=self.screenVal, font="lucida 30 bold", borderwidth=0, bg="#333333", fg="#F5F5F5")
        self.screen.pack(padx=10, pady=40)
        f.pack()

    def btnRowCreate(self, t1,t2,t3,t4):
        f = self.frameCreate()
        self.btnLeftCreate(t1,f)
        self.btnLeftCreate(t2,f)
        self.btnLeftCreate(t3,f)
        self.btnLeftCreate(t4,f)
        f.pack(side=BOTTOM)

    

if __name__ == '__main__':
    window = GUI()

    window.displayCreate()

    window.btnRowCreate("%","=","C","<")
    window.btnRowCreate("+","*","-","/")
    window.btnRowCreate("1","0","(",")")
    window.btnRowCreate("5","4","3","2")
    window.btnRowCreate("9","8","7","6")

    window.mainloop()
