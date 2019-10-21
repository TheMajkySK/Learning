import tkinter
canvas = tkinter.Canvas()
canvas.pack()
canvas.create_line(60,10,10,100,110,100,60,10,fill="blue")
canvas.create_line(110,10,60,100,160,100,110,10,fill="red")
canvas.mainloop()