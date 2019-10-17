import tkinter
canvas = tkinter.Canvas()        
canvas.pack()                       #toto musi mat kazdy program v ktorom pouzivame grafiku
canvas.mainloop()
canvas.create_line(10,10,50,70, fill="red")