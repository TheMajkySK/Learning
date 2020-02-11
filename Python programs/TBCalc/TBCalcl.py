import tkinter

def kil(n,j,d):
    v = (j-n) // d

    label1 = tkinter.Label()

canvas = tkinter.Canvas(width=1000, height=500)
canvas.pack()

canvas.create_text(188, 20, text = "Počet najazdených KM:", font = "Arial 25 bold")
canvas.create_text(175, 55, text = "Koľko chceš najazdiť:", font = "Arial 25 bold")
entry1 = tkinter.Entry()
canvas.create_window(450, 20, window = entry1)
canvas.mainloop()