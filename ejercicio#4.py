#-*-coding:utf-8-*-
try:
    from Tkinter import *
except:
    from tkinter import *

class Triangulo:
    def calcular_area(self):
        #-----------Creacion del nuevo screen -----------
        self.mbase = DoubleVar()
        self.maltura = DoubleVar()
        self.screen_triangulo = Toplevel(screen)
        self.screen_triangulo.title("Area de un triangulo")
        self.screen_triangulo.geometry("600x250")
        #----------- Interior del screen ------------
        Label(self.screen_triangulo, text = "Calculo de area de un Triangulo", font = ("Aria")).place(x = 200, y = 0)
        base = Label(self.screen_triangulo, text = "indica la medida de la base: ")
        base.place(x = 100, y = 50)
        altura = Label(self.screen_triangulo, text = "indica la medida de la altura: ")
        altura.place(x = 100, y = 100)
        baseE = Entry(self.screen_triangulo, textvariable = self.mbase)
        baseE.place(x = 260, y = 50) 
        alturaa = Entry(self.screen_triangulo, textvariable = self.maltura)
        alturaa.place(x = 260, y = 100) 
        Button(self.screen_triangulo, text = "Calcular", command = self.calcular).place(x = 100, y = 150)
        Button(self.screen_triangulo, text = "Salir", command = self.salir).place(x = 100, y = 200)
    def salir(self):
        self.screen_triangulo.destroy()

    def calcular(self):
        resultado = (self.mbase.get() * self.maltura.get()) / 2
        Label(self.screen_triangulo, text = "El area del triangulo es de " + str(resultado) + " cm2").place(x = 260, y = 150)
        
class Rectangulo:
    def calcular_area(self):
        self.mbase = DoubleVar()
        self.maltura = DoubleVar()
        self.screen_rec = Toplevel(screen)
        self.screen_rec.title("Area de un Rectangulo")
        self.screen_rec.geometry("600x250")
        Label(self.screen_rec, text = "Calculo de area de un Rectangulo", font = ("Aria")).place(x = 200, y = 0)
        base = Label(self.screen_rec, text = "indica la medida de la base: ")
        base.place(x = 100, y = 50)
        altura = Label(self.screen_rec, text = "indica la medida de la altura: ")
        altura.place(x = 100, y = 100)

        baseE = Entry(self.screen_rec, textvariable = self.mbase)
        baseE.place(x = 260, y = 50) 
        alturaa = Entry(self.screen_rec, textvariable = self.maltura)
        alturaa.place(x = 260, y = 100) 
        Button(self.screen_rec, text = "Calcular", command = self.calcular).place(x = 100, y = 150)
        Button(self.screen_rec, text = "Salir", command = self.salir).place(x = 100, y = 200)
    def salir(self):
        self.screen_rec.destroy()
        
    def calcular(self):
        resultado = self.mbase.get() * self.maltura.get()
        Label(self.screen_rec, text = "El area del rectangulo es de " + str(resultado) + " cm2").place(x = 260, y = 150)
       

class Circulo:
    def calcular_area(self):
        self.mradio = DoubleVar()
        self.screen_cir = Toplevel(screen)
        self.screen_cir.title("Area de un Circulo")
        self.screen_cir.geometry("600x200")
        Label(self.screen_cir, text = "Calculo de area de un Circulo", font = ("Aria")).place(x = 200, y = 0)
        radio = Label(self.screen_cir, text = "indica la medida del radio: ")
        radio.place(x = 100, y = 50)

        radioo = Entry(self.screen_cir, textvariable = self.mradio)
        radioo.place(x = 260, y = 50) 
        Button(self.screen_cir, text = "Calcular", command = self.calcular).place(x = 100, y = 100)
        Button(self.screen_cir, text = "Salir", command = self.salir).place(x = 100, y = 150)
    def salir(self):
        self.screen_cir.destroy()
        
    def calcular(self):
        resultado = 3.1416 * (self.mradio.get() * self.mradio.get())
        Label(self.screen_cir, text = "El area del circulo es de " + str(resultado) + " cm2").place(x = 260, y = 100)
       

def salir():
    screen.destroy()

screen = Tk()
#screen.geometry("800x600")
screen.resizable(False, False)
screen.title("Figuras Geometricas")
triangulo = Triangulo()
rectangulo = Rectangulo()
circulo = Circulo()

titulo = Label(screen, text = "Calculadora de Areas")
titulo.grid(row = 0, column = 0, columnspan = 5)

trian = Button(screen, text = "Triangulo", bd = 2, width = 10, height = 2 , command = triangulo.calcular_area)
trian.grid(row = 1, column = 1)

recta = Button(screen, text = "Rectangulo", bd = 2, width = 10, height = 2, command = rectangulo.calcular_area)
recta.grid(row = 1, column = 2)

circ = Button(screen, text = "Circulo", bd = 2, width = 10, height = 2, command = circulo.calcular_area)
circ.grid(row = 1, column = 3)

adios = Button(screen, text = "Salir", bd = 2, width = 10, height = 2, command = salir)
adios.grid(row = 1, column = 4)

screen.mainloop()