from collections import deque 

class Personas:
    def __init__(self, nombre, cedula, edad, auxilio, discapacitado, estrato, estado):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.auxilio = auxilio
        self.discapacitado = discapacitado
        self.estrato = estrato
        self.estado = estado
        
class Metodos:
    def __init__(self):
        persona = deque()
        self.persona = persona
        
    def ingreso(self):
        print("\nIngresa los datos de la persona: ")
        nom, cc, edad, aux, disc, est = "", -1, -1, -1.0, "", -1
        while nom == "":
            nom = input("\nIngresa el nombre: ")
        while cc < 0:
            try:
                cc = int(input("Ingresa el número de cédula: "))
            except ValueError:
                print("Valor no valido.")
        while edad not in range(120):
            try:
                edad = int(input("Ingresa la edad: "))
            except ValueError and edad > 0 and edad < 120:
                print("Valor no valido.")
        if edad > 18:
            aux = 1400000
        elif edad < 18 and edad > 0:
            aux = 1120000
        while disc not in [False,True]:
            try:
                disc = input("Tiene alguna discapacidad (si/no): ")
                if disc.lower() == "si":
                    disc = True
                elif disc.lower() == "no":
                    disc = False
            except ValueError and disc not in [False,True]:
                print("Valor no valido.")
        while est not in range(7):
            try:
                est = int(input("Ingresa el estrato (1 a 6): "))
            except ValueError:
                print("Valor no valido.")
                
        estadobusqueda = True
        if self.persona:
            for i in range(len(self.persona)):
                validaciondeexistencia = self.persona[i].cedula
                if validaciondeexistencia == cc:
                    print(f"\nLa persona {nom} con ID: {cc} ya existe, se actualiza registro con información indicada.")
                    self.persona[i].edad = edad
                    self.persona[i].auxilio = aux
                    self.persona[i].discapacitado = disc
                    self.persona[i].estrato = est
                    estadobusqueda = False
            if estadobusqueda:
                self.persona.append(Personas(nom, cc, edad, aux, disc, est, estado="VIGENTE"))
                print("\nRegistro exitoso.")
                estadobusqueda = True
        else: 
            self.persona.append(Personas(nom, cc, edad, aux, disc, est, estado="VIGENTE"))
            print("\nRegistro exitoso.")
            estadobusqueda = True

    def modificar(self):
        print("\nModulo modificador de cliente:")
        cc = -1
        while cc < 0:
            try:
                cc = int(input("\nIngresa el número de cédula: "))
            except ValueError:
                print("Valor no valido.")
                
        estadobusqueda = True
        if self.persona:
            for i in range(len(self.persona)):
                validaciondeexistencia = self.persona[i].cedula
                if validaciondeexistencia == cc:
                    print(f"\nLa persona {self.persona[i].nombre} con ID: {cc} registra con las siguientes caracteristicas:",
                            f"\nNombre: {self.persona[i].nombre}",
                            f"\nId: {self.persona[i].cedula}",
                            f"\nEdad: {self.persona[i].edad}",
                            f"\nAuxilio: {self.persona[i].auxilio}",
                            f"\nDiscapacidad: {self.persona[i].discapacitado}",
                            f"\nEstrato: {self.persona[i].estrato}",
                            f"\nEstado: {self.persona[i].estado}")

                    print(f"\nQue dato desea modificar:",
                            f"\n1. Edad.",
                            f"\n2. Discapacidad.",
                            f"\n3. Estrato.",
                            f"\n4. Estado.")

                    opcion = -1
                    while opcion not in [1,2,3,4,5]:
                        try:
                            opcion = int(input("\nIngresa una opción: "))
                        except ValueError:
                            print("Valor no valido.")
                    newedad, newaux, newdisc, newest, newestado = -1, -1.0, "", -1,""
                    if opcion == 1:
                        while newedad not in range(120):
                            try:
                                newedad = int(input("Ingresa la nueva edad: "))
                            except ValueError and newedad > 0 and newedad < 120:
                                print("Valor no valido.")
                        if newedad > 18:
                            newaux = 1400000
                        elif newedad < 18 and newedad > 0:
                            newaux = 1120000
                        self.persona[i].auxilio = newaux
                        self.persona[i].edad = newedad
                        print("Valor modificado con exito.")
                    elif opcion == 2:
                        while newdisc not in [False,True]:
                            try:
                                newdisc = input("Tiene alguna discapacidad (si/no): ")
                                if newdisc.lower() == "si":
                                    newdisc = True
                                elif newdisc.lower() == "no":
                                    newdisc = False
                            except ValueError and newdisc not in [False,True]:
                                print("Valor no valido.")
                        self.persona[i].discapacitado = newdisc
                        print("Valor modificado con exito.")
                    elif opcion == 3:
                        while newest not in range(7):
                            try:
                                newest = int(input("Ingresa el nuevo estrato (1 a 6): "))
                            except ValueError:
                                print("Valor no valido.")                                
                        self.persona[i].estrato = newest
                        print("Valor modificado con exito.")
                    elif opcion == 4:
                        while newestado not in ["VIGENTE", "FALLECIDO"]:
                            try:
                                newestado = int(input("Ingresa el nuevo estado (1. VIGENTE a 2. FALLECIDO): "))
                                if newestado == 1:
                                    newestado = "VIGENTE"
                                elif newestado == 2:
                                    newestado = "FALLECIDO"
                            except ValueError and newestado < 0 and newestado > 2:
                                print("Valor no valido.")                                
                        self.persona[i].estado = newestado
                        print("Valor modificado con exito.")


                    estadobusqueda = False
            if estadobusqueda:
                print("\nPersona buscada no existe.")
                estadobusqueda = True
        else: 
            print("\nNo hay registros disponibles para la busqueda.")
            estadobusqueda = True
        

    def mostrarpersonas(self):
        if self.persona:
            contador = 0
            for i in range(len(self.persona)):
                contador += 1
                print(f"\nPersona {contador}:",
                      f"\nNombre: {self.persona[i].nombre}",
                      f"\nId: {self.persona[i].cedula}",
                      f"\nEdad: {self.persona[i].edad}",
                      f"\nAuxilio: {self.persona[i].auxilio}",
                      f"\nDiscapacidad: {self.persona[i].discapacitado}",
                      f"\nEstrato: {self.persona[i].estrato}",
                      f"\nEstado: {self.persona[i].estado}")
        else: 
            print("\nNo hay personas registradas.")