from random import *
import tkinter
canvas = tkinter.Canvas(bg="black", width=1000, height=800)
canvas.pack()

x=10
y=10
for i in range(1,26):
    x+=20
    y+=20
    canvas.create_line(x,10,510,y,fill="white",width=2)
    canvas.create_line(510,y,510-x,510,fill="white",width=2)
    canvas.update()
    canvas.after(50)
canvas.mainloop()