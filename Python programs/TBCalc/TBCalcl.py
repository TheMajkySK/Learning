import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

canvas.create_text(65, 10, text = "Počet najazdených KM")

canvas.mainloop()