"""
vytvorte funkciu ktora bude kreslit kruh so zadanymi suradnicami stredu
"""
import tkinter, random
vyska, sirka = 720, 720

canvas = tkinter.Canvas(bg="black", width=sirka, height=vyska)
canvas.pack()

def kruh_stred(SX, SY):            #SX, SY budeme nazyvať paramentre funkcie(alebo vstupne parametre)
    r = 20
    x = SX
    y = SY
    c = random.randint(0,255)
    g = random.randint(0,255)           #rgb color generator
    b = random.randint(0,255)
    rgb = "#%02x%02x%02x" % (c,g,b)
    canvas.create_oval(x,y,x+r,y+r, fill=rgb)
x = 10
y = 10
while x < 700 or y < 700:
    canvas.delete("all")
    kruh_stred(x,y)
    x += 2
    y += 2
    canvas.update()
    canvas.after(10)
canvas.mainloop()