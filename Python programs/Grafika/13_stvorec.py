"""
vytvorte funkciu ktora vykresli stvorec zo zadanych suradnic stredu
"""
import tkinter, random, math
vyska,sirka = 720, 1280
canvas = tkinter.Canvas(width=sirka, height=vyska)
canvas.pack()
def stvorec(SX, SY, a):
    x = SX
    y = SY
    canvas.create_rectangle(SX-a, SY-a, SX+a, SY+a, outline="red")
    u = a * math.sqrt(2)
    return u

print(stvorec(200,300,65))
canvas.mainloop()