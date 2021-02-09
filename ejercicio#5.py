class Estudiantes:
    _nombre = ""
    _matricula = ""

    def __init__(self, n, m):
        self._nombre = n
        self._matricula = m

class Grupo:
    estudiante = Estudiantes("","")
    _nombre = ""
    _carrera = ""
    _cuatrimestre = ""
    _estudiantes = [estudiante]

    def __init__(self,n, c, ct):
        self._nombre = n
        self._carrera = c
        self._cuatrimestre = ct

    def agregar_estudiante(self):
        nombre = input("Escribe el nombre del estudiante: ")
        matricula = input("Escribe la matricula del estudiante: ")
        estudiante = Estudiantes(nombre, matricula)
        self._estudiantes.append(estudiante)


grupo = Grupo("A", "ISW", "2")

print("Grupo: " + grupo._carrera + " " + grupo._cuatrimestre + grupo._nombre)
continuar = "S"
while(continuar == "S"):
    grupo.agregar_estudiante()
    continuar = input("Deseas registrar otro estudiante: (s/n)")

for estudiante in grupo._estudiantes:
    print(estudiante._matricula + " " + estudiante._nombre)