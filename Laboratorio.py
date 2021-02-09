#-*-coding:utf-8-*-
try:
    from Tkinter import *
except:
    from tkinter import *

        
class Base:
    def __init__(self):
        self.titulo = "Analicis"
    def obtener(self):
        self.eGlucosa = DoubleVar()
        self.eAcido = DoubleVar()
        self.eColesterol = DoubleVar()
        self.screenTwo = Toplevel(screen)
        self.screenTwo.geometry("400x400")
        self.screenTwo.title(self.titulo)
        Label(self.screenTwo, text = self.titulo).place(x = 50, y = 0)
        
        #---------Opciones--------
        Label(self.screenTwo, text = "Glocosa").place(x = 50, y = 50)
        Label(self.screenTwo, text = "Acido urico").place(x = 50, y = 100)
        Label(self.screenTwo, text = "Colesteron").place(x = 50, y = 150)
        #---------Entradas--------
        gluco = Entry(self.screenTwo, textvariable = self.eGlucosa)
        gluco.place(x = 150, y = 50)
        acido = Entry(self.screenTwo, textvariable = self.eAcido)
        acido.place(x = 150, y = 100)
        coles = Entry(self.screenTwo, textvariable = self.eColesterol)
        coles.place(x = 150, y = 150)
        #---------Unidades---------
        Label(self.screenTwo, text = "mmol/L").place(x = 250, y = 50)
        Label(self.screenTwo, text = "mmol/L").place(x = 250, y = 100)
        Label(self.screenTwo, text = "mmol/L").place(x = 250, y = 150)
        self.calcular = Button(self.screenTwo, text = "Calcular", command = self.conversion).place(x = 50, y = 200)
        self.salir = Button(self.screenTwo, text = "Salir", command = self.cerrar_ventana).place(x = 150, y = 200)
    def cerrar_ventana(self):
        self.screenTwo.destroy()

class Qs3(Base):
    def __init__(self, titulo):
        self.titulo = titulo
        self.eGlucosa = DoubleVar()
        self.eAcido = DoubleVar()
        self.eColesterol = DoubleVar()  
    def conversion(self):
        self.cGlucosa = self.eGlucosa.get() * 18.02
        self.cAcido = self.eAcido.get() * 0.02
        self.cColes = self.eColesterol.get() * 380.66
        Label(self.screenTwo, text = "Glocosa " + str(self.cGlucosa) + " mg/dL").place(x = 50, y = 250)
        Label(self.screenTwo, text = "Acido urico " + str(self.cAcido) + " mg/dL").place(x = 50, y = 300)
        Label(self.screenTwo, text = "Colesteron " + str(self.cColes) + " mg/dL").place(x = 50, y = 350)


class Qs6(Base):
    def __init__(self, titulo):
        self.titulo = titulo
        self.eGlucosa = DoubleVar()
        self.eAcido = DoubleVar()
        self.eColesterol = DoubleVar() 
    def conversion(self):
        self.cGlucosa = self.eGlucosa.get() * 18.02
        self.cAcido = self.eAcido.get() * 0.02
        self.cColes = self.eColesterol.get() * 380.66
        Label(self.screenTwo, text = "Glocosa " + str(self.cGlucosa) + " mg/dL").place(x = 50, y = 250)
        Label(self.screenTwo, text = "Acido urico " + str(self.cAcido) + " mg/dL").place(x = 50, y = 300)
        Label(self.screenTwo, text = "Colesteron " + str(self.cColes) + " mg/dL").place(x = 50, y = 350)

def salir():
    screen.destroy()


screen = Tk()
screen.title("Laboratorio de Analisis Clinicos DM")
screen.geometry("400x150")
screen.resizable(0,0)

Label(screen, text = "Laboratorio de Analisis Clinicos DM", font = ("Arial", 14)).place(x = 50, y = 0)

opcion1 = Qs3("QS3")
opcion2 = Qs6("QS6")
qs3 = Button(screen, text = "QS3", font = ("Arial", 12), width = 8, height = 2, command = opcion1.obtener)
qs3.place(x = 60, y = 50)

qs6 = Button(screen, text = "QS6", font = ("Arial", 12), width = 8, height = 2, command = opcion2.obtener)
qs6.place(x = 160, y = 50)

salir = Button(screen, text = "Salir", font = ("Arial", 12), width = 8, height = 2, command = salir)
salir.place(x = 260, y = 50)

screen.mainloop()
