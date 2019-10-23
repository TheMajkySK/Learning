import tkinter, random
sucet = 0
canvas = tkinter.Canvas(width = 1280, height = 720)
canvas.pack()
for i in range(10000):
    canvas.create_line(0, 0, random.randrange(200), 100)
    sucet += 1
canvas.mainloop()