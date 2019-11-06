"""
spravte program ktory bude simulovat semafor, 
vytvorte funkciu kruh kde budeme zadavat suradnice a farbu
"""
import tkinter
vyska, sirka = 720, 1280
canvas = tkinter.Canvas(height = vyska, width = sirka)
canvas.pack()
def kruh(S1, S2, farba):
    canvas.create_oval(S1,S2,S1+50,S2+50, fill = farba)
t = 0
while True:
    if t < 10:
        canvas.delete("all")
        canvas.create_rectangle(630,15,700,200,fill="black")
        kruh(640,20,"red")
        t+=1
    elif t < 15:
        kruh(640,80,"orange")
        t+=1
    elif t < 30:
        canvas.delete("all")
        canvas.create_rectangle(630,15,700,200,fill="black")
        kruh(640,140,"green")
        t+=1
    elif t < 40:
        canvas.delete("all")
        canvas.create_rectangle(630,15,700,200,fill="black")
        kruh(640,80,"orange")
        t += 1
    elif t < 45:
        t = 0
    canvas.update()
    canvas.after(200)


canvas.mainloop()