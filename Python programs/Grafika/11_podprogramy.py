import tkinter, random
vyska, sirka = 720, 1280

canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()

def kruh():
    x = random.randint(20, sirka - 40)
    y = random.randint(20, vyska - 40)
    r = random.randint(5, 10)
    farba = random.choice(("red","green","blue","magenta"))
    canvas.create_oval(x, y, x + r, y + r, fill=farba)

#HLAVNÝ PROGRAM

for i in range(100000):
    kruh()
    canvas.update()

canvas.mainloop()