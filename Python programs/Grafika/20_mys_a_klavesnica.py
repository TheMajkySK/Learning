import tkinter
vyska, sirka = 720, 1280
canvas = tkinter.Canvas(height = vyska, width = sirka)
canvas.pack()

def kruzok(suradnice):
    x = suradnice.x
    y = suradnice.y
    canvas.create_oval(x-5, y-5, x+5, y+5, fill = "blue")
def stvorec(event):
    x = event.x
    y = event.y
    canvas.create_rectangle(x-10, y-10, x+10, y+10, fill = "red")

canvas.bind("<Button-1>", kruzok)     #button-1 automaticky odosiela informacie x a y, ktore sa poslu funkcii ktorá sa má vykonať

canvas.bind("<Button-3>", stvorec)


canvas.mainloop()