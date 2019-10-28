import tkinter, random
vyska, sirka = 1000, 1900

canvas = tkinter.Canvas(bg="black", width=sirka, height=vyska)
canvas.pack()

def kruh():                          #kruh je teraz nova funkcia ktoru možeme vyvolat v hlavnom programe
    r = random.randint(0,255)
    g = random.randint(0,255)           #rgb color generator
    b = random.randint(0,255)
    rgb = "#%02x%02x%02x" % (r,g,b)
    x = random.randint(0, sirka)
    y = random.randint(0, vyska)              #x,y,r su lokalne premenne
    r = random.randint(1, 2)                       #vznikaju (vytvoria sa v pamäti) po zavolani funkcie
    #farba = random.choice(("red","green","blue","magenta"))    # a zaniknu po jej ukoncení
    canvas.create_oval(x, y, x + r, y + r, fill=rgb)               # vyska a sirka su globalne premenne, mozeme ich pouzit v definicii funkcie aj v hlavnom programe
                                                                    #lokalne premenne nie su viditelne v hlavnom programe
#HLAVNÝ PROGRAM

for i in range(20000):
    kruh()
    canvas.update()

canvas.mainloop()