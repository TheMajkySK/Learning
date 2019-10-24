import tkinter
canvas = tkinter.Canvas(width = 1280, height = 720)
canvas.pack()
x = 10
for i in range(1,6):
    canvas.create_line(x, i * 5, 200, i * 5)
    x += 10
canvas.mainloop()