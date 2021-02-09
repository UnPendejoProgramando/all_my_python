try:
    from Tkinter import *
except:
    from tkinter import *


class Nayeon:
    def mostrar(self):
        self.screen_nayeon = Toplevel(screen)
        self.screen_nayeon.title("Nayeon")
        self.imagen = PhotoImage(file = "Nayeon.png")
        self.fondo = Label(self.screen_nayeon, image = self.imagen)
        self.fondo.pack()

screen = Tk()
screen.title("Twice")
screen.resizable(0,0)
screen.config(bg = "Pink")

#----Instancias-----
nayeon = Nayeon()


tit = Label(screen, text = "TWICE", width = 10)
tit.grid(row = 0, column = 1)
#----Botones-------
nayeon = Button(screen, text = "Nayeon", width = 10, height = 2, command = nayeon.mostrar)
nayeon.grid(row = 1, column = 0)

jeong = Button(screen, text = "Jeongyeon", width = 10, height = 2)
jeong.grid(row = 1, column = 1)

momo = Button(screen, text = "Momo", width = 10, height = 2)
momo.grid(row = 1, column = 2)

sana = Button(screen, text = "Sana", width = 10, height = 2)
sana.grid(row = 2, column = 0)

jihyo = Button(screen, text = "Jihyo", width = 10, height = 2)
jihyo.grid(row = 2, column = 1)

mina = Button(screen, text = "Mina", width = 10, height = 2)
mina.grid(row = 2, column = 2)

dahyun = Button(screen, text = "Dahyun", width = 10, height = 2)
dahyun.grid(row = 3, column = 0)

chae = Button(screen, text = "Chae-Young", width = 10, height = 2)
chae.grid(row = 3, column = 1)

tzuyu = Button(screen, text = "Tzuyu", width = 10, height = 2)
tzuyu.grid(row = 3, column = 2)













screen.mainloop()