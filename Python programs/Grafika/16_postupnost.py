import tkinter
vyska, sirka = 720, 1280
canvas = tkinter.Canvas(height = vyska, width = sirka)
#canvas.pack()
def kruh(S1, S2, r, farba):
    canvas.create_oval(S1,S2,S1+r,S2+r, fill = farba)
def nty_clen(n):
    return (5+n**2)/(n+2)
#canvas.create_line(1000,10,10,10,10,700)
for i in range(1,1001):
    print(i,"=",nty_clen(i))
    #kruh((5*i)+10,(200-100*nty_clen(i))+10,5,"black")
    #canvas.update()
    #canvas.after(50)





#canvas.mainloop()