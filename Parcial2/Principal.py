from collections import deque
import ObjBanco as ObjB

class Principal:
    def __init__(self):
        DBancoUsuarios = deque()
        DBancoCreditos = deque()
        DBancoUsuariosCredito = deque()
        self.DBancoUsuarios = DBancoUsuarios
        self.DBancoCreditos = DBancoCreditos
        self.DBancoUsuariosCredito = DBancoUsuariosCredito


    def login(self):
        Idlogin = -1
        self.usuario = None
        while Idlogin == -1:
            try:
                Idlogin = int(input("\nIngresa tu ID para poder iniciar: "))
            except ValueError:
                        print("El valor ingresado no es valido.")
        while self.DBancoUsuarios:
            for i in range(len(self.DBancoUsuarios)):
                if self.DBancoUsuarios[i].idusuario == Idlogin:
                    self.usuario = self.DBancoUsuarios[i]
                    break
            if not self.usuario:
                print("\nEl usuario no existe.")
                break
        if self.usuario.rol == "cliente":
            print("\nMenú:",
                  "\n1. Buscar credito",
                  "\n2. Solicitar credito",
                  "\n0. Salir")
            opcion = int(input("\nIngresa la opción: "))
            if opcion == 1:
                pass
            if opcion == 2:
                pass
            if opcion == 3:
                pass
            if opcion == 0:
                pass
        elif self.usuario.rol == "admin":
            print("\nMenú:",
                  "\n1. Registrar credito",
                  "\n2. Registrar cliente",
                  "\n3. Asignar credito",
                  "\n0. Salir")
            opcion = int(input("\nIngresa la opción: "))
            if opcion == 1:
                pass
            if opcion == 2:
                pass
            if opcion == 3:
                pass
            if opcion == 0:
                pass
        else:
            #Registrarse
            pass
                
    def regitrarse(self):
        print("\nIngresa los datos del usurio:")
        Id,Nom,rol = -1,"",""
        while Id == -1:
            try:
                Id = int(input("\nIngresa el ID del cliente: "))
            except ValueError:
                        print("El valor ingresado no es valido.")
        while Nom == "":
            Nom = input("Ingresa el nombre: ")
            if Nom == "":
                print("Debe indicar al menos un carácter.\n")
        while rol == "":
            rol = input("Ingresa el rol (si no aplica indicar cero (0)): ")
            if rol in ["admin"]:
                print("Rol admin asignado correctamente\n")
            elif rol.lower() in ["cliente","cero", "0"]:
                print("\nFelicidades ahora eres cliente.")
        self.DBancoTUsuarios.append(ObjB.Usuarios(Id,Nom,rol))
        
    def registrarcredito(self):
        print("\nIngresa los datos del credito a registrar:")
        NomCredito,ValorCredito,Duracion = "",-1.0,-1
        while NomCredito == "":
            NomCredito = input("Ingresa el nombre del credito: ")
            if NomCredito == "":
                print("Debe indicar al menos un carácter.\n")
        while ValorCredito == -1.0:
            try:
                ValorCredito = float(input("\nIngresa el valor del credito: "))
            except ValueError:
                        print("El valor ingresado no es valido.")
        while Duracion == -1:
            try:
                Duracion = int(input("\nIngresa la duración del credito en meses: "))
            except ValueError:
                        print("El valor ingresado no es valido.")

        self.DBancoTUsuarios.append(ObjB.Creditos(NomCredito,ValorCredito,Duracion))
        
    def asignarcredito(self):
        print("\nIngresa los datos del usuario:")
        Idcliente, Nombrecredito, credito = -1,"",""
        cliente,credito = None,None
        estadocliente, estadocredito = True,True
        while Idcliente == -1:
            try:
                Id = int(input("\nIngresa el ID del cliente: "))
            except ValueError:
                        print("El valor ingresado no es valido.")

        while self.DBancoUsuarios:
            for i in range(len(self.DBancoUsuarios)):
                if self.DBancoUsuarios[i].idusuario == Idcliente:
                    cliente = self.DBancoUsuarios[i]
                    while credito == "":
                        credito = input("\nIngresa el ID del cliente: ")
                    while self.DBancoCreditos:
                        for i in range(len(self.DBancoCreditos)):
                            if self.DBancoCreditos[i].tipocredito == credito:
                                 credito = self.DBancoCreditos[i]
                                 self.DBancoUsuariosCredito.append(cliente,credito)
                        if estadocredito:
                             print("El credito buscado no existe.")

                    break
            if not self.usuario:
                print("\nEl usuario no existe.")
                break