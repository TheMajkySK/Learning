import tkinter

def kil():
    n = p_najaz.get()
    ch = p_chc.get()
    d = p_dni.get()
    nch = int(ch)-int(n)
    c = nch / int(d)
    c = round(c, 2)

    label1 = tkinter.Label(text= c,font= "Arial 25 bold")
    canvas.create_window(400,160,window= label1)

canvas = tkinter.Canvas(width=700, height=300)
canvas.pack()

canvas.create_text(188, 20, text= "Počet najazdených KM:", font= "Arial 25 bold")
canvas.create_text(175, 55, text= "Koľko chceš najazdiť:", font= "Arial 25 bold")
canvas.create_text(168, 90, text= "Za počet daných dní:", font= "Arial 25 bold")
p_najaz = tkinter.Entry()
p_chc = tkinter.Entry()
p_dni = tkinter.Entry()
canvas.create_window(450, 20, window= p_najaz)
canvas.create_window(450,55,window= p_chc)
canvas.create_window(450,90,window= p_dni)

button = tkinter.Button(text=f"Výpočet KM na daný počet dní", command=kil)
canvas.create_window(600,55,window=button)
canvas.mainloop()