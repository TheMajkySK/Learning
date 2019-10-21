import tkinter
a = int(input("Zadaj dĺžku strany štvorca: "))
canvas = tkinter.Canvas(width = 1280,height = 720)
canvas.pack()
canvas.create_rectangle(50,50,a+50,a+50)
canvas.mainloop()