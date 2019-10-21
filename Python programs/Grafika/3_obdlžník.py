import tkinter
canvas = tkinter.Canvas(width = 1920, height = 1080)
canvas.pack()
canvas.create_rectangle(300,200,500,300,fill="blue")
canvas.mainloop()