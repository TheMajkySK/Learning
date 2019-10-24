import tkinter
canvas = tkinter.Canvas(width = 1280, height = 720)
canvas.pack()
for i in range(1,6):
    canvas.create_line(10, i * 5, 200, i * 15)
canvas.mainloop()