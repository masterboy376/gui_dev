from tkinter import *

root = Tk()

canvas_width = 800
canvas_height= 400

root.geometry(f"{canvas_width}x{canvas_height}")

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

can_widget.create_line(0,0,800,400)
can_widget.create_line(0,400,800,0)

# top left and bottom right 
can_widget.create_rectangle(20,20,400,400)

# top left and bottom right and border radius
can_widget.create_oval(100,100,300,300)

can_widget.create_text(200,200, text="python is awsome")

root.mainloop()
