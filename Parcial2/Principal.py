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
        while Idlogin < 0:
            try:
                Idlogin = int(input("\nIngresa tu ID para poder iniciar: "))
            except ValueError:
                print("El valor ingresado no es valido.")

            for i in range(len(self.DBancoUsuarios)):
                if self.DBancoUsuarios[i].idusuario == Idlogin:
                    self.usuario = self.DBancoUsuarios[i]
                    break
            if not self.usuario:
                print("\nEl usuario no existe.")
                break
        if self.usuario.rol == "cliente":
            print(
                "\nMenú:", "\n1. Buscar credito", "\n2. Solicitar credito", "\n0. Salir"
            )
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
            print(
                "\nMenú:",
                "\n1. Registrar credito",
                "\n2. Registrar cliente",
                "\n3. Asignar credito",
                "\n0. Salir",
            )
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
            # Registrarse
            pass

    def regitrarse(self):
        print("\nIngresa los datos del usurio:")
        Id, Nom, rol = -1, "", ""
        while Id < 0:
            try:
                Id = int(input("\nIngresa el ID del cliente: "))
            except ValueError:
                print("El valor ingresado no es valido.")
        while Nom == "":
            Nom = input("Ingresa el nombre: ")
            if Nom == "":
                print("Debe indicar al menos un carácter.\n")
        while rol not in ["cliente", "cero", "0"]:
            rol = input("Ingresa el rol (si no aplica indicar cero (0)): ")
            if rol in ["admin"]:
                print("Rol admin asignado correctamente\n")
            elif rol.lower() in ["cliente", "cero", "0"]:
                print("\nFelicidades ahora eres cliente.")
        self.DBancoUsuarios.append(ObjB.Usuarios(Id, Nom, rol))

    def registrarcredito(self):
        print("\nIngresa los datos del credito a registrar:")
        NomCredito, ValorCredito, Duracion = "", -1.0, -1
        while NomCredito == "":
            NomCredito = input("\nIngresa el nombre del credito: ")
            if NomCredito == "":
                print("Debe indicar al menos un carácter.\n")
        while ValorCredito < 0.0:
            try:
                ValorCredito = float(input("Ingresa el valor del credito: "))
            except ValueError:
                print("El valor ingresado no es valido.")
        while Duracion < 0:
            try:
                Duracion = int(input("Ingresa la duración del credito en meses: "))
            except ValueError:
                print("El valor ingresado no es valido.")

        self.DBancoCreditos.append(ObjB.Creditos(NomCredito, ValorCredito, Duracion))
        print("Registro exitoso.")

    def asignarcredito(self):
        print("\nIngresa los datos del usuario y el credito a asignar:")
        Idcliente, Nombrecredito, credito = -1, "", ""
        cliente, credito = None, None
        estadocliente, estadocredito = True, True
        while Idcliente < 0:
            try:
                Idcliente = int(input("\nIngresa el ID del cliente: "))
            except ValueError:
                print("El valor ingresado no es valido.")

        while self.DBancoUsuarios:
            for i in range(len(self.DBancoUsuarios)):
                if self.DBancoUsuarios[i].idusuario == Idcliente:
                    cliente = self.DBancoUsuarios[i]
                    estadocliente = False
                    while Nombrecredito == "":
                        Nombrecredito = input("Ingresa nombre del credito: ")
                    while self.DBancoCreditos:
                        for i in range(len(self.DBancoCreditos)):
                            if self.DBancoCreditos[i].tipocredito == Nombrecredito:
                                credito = self.DBancoCreditos[i]
                                self.DBancoUsuariosCredito.append(cliente, credito)
                                estadocredito = False
                        if estadocredito:
                            print("El credito buscado no existe.")
                    break
            if not estadocliente:
                print("\nEl usuario no existe.")
                break

    def mostrarpilas(self):
        (
            estadocliente,
            estadocredito,
            estadoclientecredito,
        ) = (
            True,
            True,
            True,
        )
        print("\nPila usuarios: ")
        while self.DBancoUsuarios:
            for i in range(len(self.DBancoUsuarios)):
                print(
                    f"\nId: {self.DBancoUsuarios[i].idusuario}\nNombre: {self.DBancoUsuarios[i].nombreusuario}\nRol: {self.DBancoUsuarios[i].rol}"
                )
            estadocliente = False
        if estadocliente:
            print("\nPila clientes vacía.")

        print("\nPila creditos: ")
        while self.DBancoCreditos:
            for i in range(len(self.DBancoCreditos)):
                print(
                    f"\nTipo: {self.DBancoCreditos[i].tipocredito}\nValor: {self.DBancoCreditos[i].valorcredito}\nDuración: {self.DBancoCreditos[i].duracion}"
                )
            estadocliente = False
        if estadocredito:
            print("\nPila creditos vacía.")

        print("\nPila clientes con credito: ")
        while self.DBancoUsuariosCredito:
            for i in range(len(self.DBancoUsuariosCredito)):
                print(
                    f"\nId: {self.DBancoUsuariosCredito[i].idusuario}\nNombre: {self.DBancoUsuariosCredito[i].nombreusuario}\nRol: {self.DBancoUsuariosCredito[i].rol}\nTipo: {self.DBancoCreditos[i].tipocredito}\nValor: {self.DBancoCreditos[i].valorcredito}\nDuración: {self.DBancoCreditos[i].duracion}"
                )
            estadocliente = False
        if estadoclientecredito:
            print("\nPila creditos con clientes vacía.")
