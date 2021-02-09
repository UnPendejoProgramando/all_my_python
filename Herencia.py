try:
    from Tkinter import *
except:
    from tkinter import *

class Figuras_base:
    def __init__(self):
        self.titulo = "Area"
    def obtener_datos(self):
        self.mbase = DoubleVar()
        self.maltura = DoubleVar()
        self.screen2 = Toplevel(screen)
        #-----------Creacion del nuevo screen -----------
        self.screen2.title("Calculo del area de un " + self.titulo)
        self.screen2.geometry("600x250")
        #----------- Interior del screen ------------
        self.titulo = Label(self.screen2, text = "Calculo del area de un " + self.titulo, font = ("Aria"))
        self.titulo.place(x = 200, y = 0)
        self.base = Label(self.screen2, text = "indica la medida de la base: ")
        self.base.place(x = 100, y = 50)
        self.altura = Label(self.screen2, text = "indica la medida de la altura: ")
        self.altura.place(x = 100, y = 100)
        self.baseE = Entry(self.screen2, textvariable = self.mbase)
        self.baseE.place(x = 260, y = 50) 
        self.alturaa = Entry(self.screen2, textvariable = self.maltura)
        self.alturaa.place(x = 260, y = 100) 
        Button(self.screen2, text = "Calcular", command = self.calcular_area).place(x = 100, y = 200)
        Button(self.screen2, text = "Salir", command = self.salir).place(x = 350, y = 200)
    def salir(self):
        self.screen2.destroy()


class Triangulo(Figuras_base):
    def __init__(self, titulo):
        self.titulo = titulo
        self.mbase = DoubleVar()
        self.maltura = DoubleVar()
    def calcular_area(self):
        self.resultado = (self.mbase.get() * self.maltura.get()) / 2
        Label(self.screen2, text = "El area del triangulo es de " + str(self.resultado) + " cm2").place(x = 100, y = 150)
    
class Rectangulo(Figuras_base):
    def __init__(self, titulo):
        self.titulo = titulo
        self.mbase = DoubleVar()
        self.maltura = DoubleVar()
    def calcular_area(self):
        self.resultado = self.mbase.get() * self.maltura.get()
        Label(self.screen2, text = "El area del rectangulo es de " + str(self.resultado) + " cm2").place(x = 100, y = 150)

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
        Button(self.screen_cir, text = "Calcular", command = self.calcular).place(x = 100, y = 150)
        Button(self.screen_cir, text = "Salir", command = self.salir).place(x = 350, y = 150)
    def salir(self):
        self.screen_cir.destroy()
        
    def calcular(self):
        resultado = 3.1416 * (self.mradio.get() * self.mradio.get())
        Label(self.screen_cir, text = "El area del circulo es de " + str(resultado) + " cm2").place(x = 100, y = 100)

def destruir_pantalla():
    screen.destroy()

screen = Tk()
screen.geometry("800x500")
screen.resizable(0,0)
screen.title("Calculo del area del figuras geometricas")
Label(screen, text = "CALCULO DEL AREA DE FIGURAS GEOMETRICAS", font = ("Arial", 18)).place(x = 120, y = 0)

trian = Triangulo("Triangulo")
rec = Rectangulo("Rectangulo")
circulo = Circulo()

triangulo = Button(screen, text = "Triangulo", width = 80, height = 3, command = trian.obtener_datos)
triangulo.place(x = 120, y = 50)

rectangulo = Button(screen, text = "Rectangulo", width = 80, height = 3, command = rec.obtener_datos)
rectangulo.place(x = 120, y = 120)

circulo = Button(screen, text = "Circulo", width = 80, height = 3, command = circulo.calcular_area)
circulo.place(x = 120, y = 190)

salir = Button(screen, text = "Salir", width = 80, height = 3, command = destruir_pantalla)
salir.place(x = 120, y = 260)
screen.mainloop()