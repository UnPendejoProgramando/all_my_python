import os #Se importo la libreia del sistema
class Triangulo: #Se crea la clase Triangulo
    def __init__(self): #Se inicializa el metodo constructor con el parametro self  
        print ("Calculo de area del triangulo") 
    def calcular_area(self): #Se crea el metodo que calculara el area y como parametros le damos self
        self.base = float(input("Ingresa la medida de la base en cm: ")) #Se declara la variable en la que ingresaremos la base, esta es de tipo flotante
        self.altura = float(input("Ingresa la medida de la altura en cm: ")) #Se declara la variable en la que ingresaremos la altura, esta es de tipo flotante
        self.resultado = (self.base * self.altura) / 2 #Se crea una variable llamada resultado en la que hara la operacion correspondiente
        print ("El area de tu triangulo en cm2 es: ", self.resultado) 

class Rectangulo:
    def __init__(self): #Se inicializa el metodo constructor con el parametro self
        print ("Calculo de area del rectangulo")
    def calcular_area(self): #Se crea el metodo que calculara el area y como parametros le damos self
        self.base = float(input("Ingresa la medida de la base en cm: ")) #Se declara la variable en la que ingresaremos la base, esta es de tipo flotante
        self.altura = float(input("Ingresa la medida de la altura en cm: "))#Se declara la variable en la que ingresaremos la altura, esta es de tipo flotante
        self.resultado = self.base * self.altura #Se crea una variable llamada resultado en la que hara la operacion correspondiente
        print ("El area de tu rectangulo en cm2 es: ", self.resultado)

class Circulo:
    def __init__(self): #Se inicializa el metodo constructor con el parametro self
        print ("Calculo de area de un circulo")
    def calcular_area(self): #Se crea el metodo que calculara el area y como parametros le damos self
        self.pi = 3.1416 #se crea una variable en la cual tiene el valor de pi
        self.radio = float(input("Ingresa la medida del radio en cm: "))  #Se declara la variable en la que ingresaremos el radio, esta es de tipo flotante
        self.resultado = self.pi * (self.radio * self.radio) #Se crea la variable resultado en el cual hara la operacion correspondiente
        print ("El area de tu circulo es en cm2 es: ", self.resultado)


class Menu:
    def __init__(self, opciones):#Se inicializa el metodo constructor con el parametro self y opciones
        self._opciones = opciones #se declara que self._opciones tiene como valor el arreglo opciones

    def mostrar(self): #Se crea el metodo que mostrara el menu y como parametros le damos self
        eleccion = 0 #se declara la variable eleccion en 0
        while float(eleccion) < float(1) or float(eleccion) > float(len(self._opciones)): #se crea un while en el que indicamos que miestras eleccion sea mayor a 1 o eleccion sea menor a la variavle self_opciones este se va arepetir 
            contador = 1 #declaramos la variable contador y a esta la igualamos a 0
            for opcion in self._opciones: #se usa un for para recorrer cada parte del arreglo opciones que se alamceno en la variable self._opciones
                print (contador, opcion) #Imprime en menu
                contador += 1 #incrementa el contador en 1
            eleccion = input("Elija una opcion: ") #se pide al usuario una opcion que sea del 1 al 4
        return eleccion #regresa lo que contenga la variable eleccion

        
menu = Menu(("Triangulo", "Rectangulo", "Circulo", "Salir")) #se crea la instancia u objeto, en el indicamos como parametro nuestro arreglo

opcion = 0 #Declaramos opcion es igual a 0
while float(opcion) < float(len(menu._opciones)): #se uso un while y dentro de esto indicamos que mientras opcion sea menor al areglo _opciones esto se va a repetircabe mencionar que usamos el objeto menu para llamar al arreglo
    os.system("cls") #Se utiliza para limpiar la consola
    print ("Calculadora de area de figuras geometricas")
    opcion =  menu.mostrar() #declaramos que opcion es igual al objeto que esta llamando al metodo mostrar, este muestra el menu y lee la eleccion que escojamos del 1 al 4
    if opcion == "1": #se inidica que si opcion es igual a 1 entonces el programa entra a esta opcion
        os.system("cls") #Se utiliza para limpiar la consola
        calculo = Triangulo() #se crea el objeto calculo e indicamos que pertenece a la clase Triangulo
        calculo.calcular_area() #se manda a llamar con el objeto el metodo que permitira leer la base y la altura de la figura, tambien hara que nos arroje un resultado
        continuar = input("Preciona ENTER para continuar\n")
    elif opcion == "2": #se inidica que si opcion es igual a 2 entonces el programa entra a esta opcion
        os.system("cls") #Se utiliza para limpiar la consola
        rec = Rectangulo()#se crea el objeto rec e indicamos que pertenece a la clase Rectangulo
        rec.calcular_area()#se manda a llamar con el objeto el metodo que permitira leer la base y la altura de la figura, tambien hara que nos arroje un resultado
        continuar = input("Preciona ENTER para continuar\n")
    elif opcion == "3":#se inidica que si opcion es igual a 3 entonces el programa entra a esta opcion
        os.system("cls") #Se utiliza para limpiar la consola
        cir = Circulo()#se crea el objeto cir e indicamos que pertenece a la clase Circulo
        cir.calcular_area()#se manda a llamar con el objeto el metodo que permitira leer el radio de la figura, tambien hara que nos arroje un resultado
        continuar = input("Preciona ENTER para continuar\n")
    elif opcion == "4": #se inidica que si opcion es igual a 4 entonces el programa entra a esta opcion, en este caso acabaria el programa
        os.system("cls") #Se utiliza para limpiar la consola
        print ("Hasta luego, vuelve pronto ") #Nos da la despedida
        opcion = 5 #Rompe el ciclo while y termina el programa
        continuar = input("Preciona ENTER para continuar\n")

