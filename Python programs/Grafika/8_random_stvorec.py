import tkinter, random
canvas = tkinter.Canvas(width = 1280, height = 720)
for i in range(1,11):
    x = random.randrange(200)
    y = random.randrange(200)
    velkost = random.randint(30, 100)
    canvas.pack()
    canvas.create_rectangle(x, y, x + velkost, y + velkost)
    canvas.create_text(x + (velkost/2), y + (velkost/2), text=i, font="Arial 12 bold")
canvas.mainloop()