from tkinter import *

def func1(event):
    print(f"even triggered at {event.x} , {event.y}")
def func2(event):
    print(f"even triggered at {event.x} , {event.y}")

root = Tk()

width = 800
height= 400

root.title("events")
root.geometry(f"{width}x{height}")

btn = Button(root, text='Click me please')
btn.pack()
btn.bind('<Button-1>', func1)
btn.bind('<Double-1>', quit)

root.mainloop()