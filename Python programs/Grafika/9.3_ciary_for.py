import tkinter
canvas = tkinter.Canvas(width = 1280, height = 720)
canvas.pack()
x = 10 
for i in range(1,11):
    canvas.create_line(x, 100, x, 100)
    x += 10
canvas.mainloop()