class Menu():
    def __init__(self, opciones):
        self._opciones = opciones
    def mostrar_menu(self):
        for i in self._opciones:
            print(i)

menu = Menu(["Altas", "Bajas", "Salir"])
menu.mostrar_menu()