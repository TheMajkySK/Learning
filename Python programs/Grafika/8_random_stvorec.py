import tkinter, random
canvas = tkinter.Canvas(width = 720, height = 720)
canvas.pack()
for i in range(1,1000):
    farba = random.choice(("blue", "red", "magenta", "black", "white", "green"))
    x = random.randrange(720)
    y = random.randrange(720)
    velkost = random.randint(30, 720)
    canvas.create_rectangle(x, y, x + velkost, y + velkost, outline=farba, width=10)
    canvas.create_text(x + (velkost/2), y + (velkost/2), text=i, font="Arial 12 bold")
    canvas.update()
canvas.mainloop()