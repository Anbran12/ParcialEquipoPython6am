from collections import deque
import ObjBanco as ObjB


class Principal:
    def __init__(self):
        DBancoUsuarios = deque()
        DBancoUsuariosTemporal = deque()
        self.DBancoUsuarios = DBancoUsuarios
        self.DBancoUsuariosTemporal = DBancoUsuariosTemporal

    def login(self):
        usuario = False
        Idlogin = -1
        while Idlogin < 0:
            try:
                Idlogin = int(input("\nIngresa tu ID para poder iniciar: "))
            except ValueError:
                print("El valor ingresado no es valido.")
            for i in range(len(self.DBancoUsuarios)):
                if self.DBancoUsuarios[i].idusuario == Idlogin:
                    usuario = self.DBancoUsuarios[i]
                    if usuario.rol == "cliente":
                        print(
                            "\nMenú:",
                            "\n1. Buscar credito",
                            "\n2. Solicitar credito",
                            "\n0. Salir",
                        )
                        opcion = -1
                        while opcion in [0, 1, 2]:
                            try:
                                opcion = int(input("\nIngresa la opción: "))
                            except ValueError:
                                print("Valor no valido.")
                        if opcion == 1:
                            pass
                        if opcion == 2:
                            pass
                        if opcion == 3:
                            pass
                        if opcion == 0:
                            pass
                    elif usuario.rol == "admin":
                        print(
                            "\nMenú:",
                            "\n1. Registrar credito",
                            "\n2. Registrar cliente",
                            "\n3. Asignar credito",
                            "\n0. Salir",
                        )
                        opcion = -1
                        while opcion in [0, 1, 2, 3]:
                            try:
                                opcion = int(input("\nIngresa la opción: "))
                            except ValueError:
                                print("Valor no valido.")
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
            if usuario == False:
                print("\nEl usuario no existe.")
                break

    def regitrarse(self):
        print("\nIngresa los datos del usuario:")
        Id, Nom, rol = -1, "", ""
        usuarionoexiste = True
        while usuarionoexiste:
            while Id < 0:
                try:
                    Id = int(input("\n- Ingresa el ID del cliente: "))
                except ValueError:
                    print("El valor ingresado no es valido.")
                for i in range(len(self.DBancoUsuarios)):
                    if self.DBancoUsuarios[i].idusuario == Id:
                        print("\nEl usuario ingresado ya registra en el sistema.")
                        usuarionoexiste = False
                if usuarionoexiste:
                    while Nom == "":
                        Nom = input("- Ingresa el nombre: ")
                        if Nom == "":
                            print("Debe indicar al menos un carácter.\n")
                    while rol not in ["cliente", "admin"]:
                        rol = input(
                            "- Ingresa el rol (si no aplica indicar cero (0)): "
                        )
                        if rol in ["admin"]:
                            rol = "admin"
                            print("Rol admin asignado correctamente\n")
                        elif rol.lower() in ["cliente", "cero", "0"]:
                            rol = "cliente"
                            print("\nFelicidades ahora eres cliente.")
                    self.DBancoUsuarios.append(ObjB.Usuarios(Id, Nom, rol))
                    usuarionoexiste = False

    def buscarcredito(self):
        print(
            "\nBajo que criterio desea realizar la busqueda:",
            "\n1. Nombre.",
            "\n2. Rango valor.",
            "\n0. Volver al menú anterior."
        )
        opcion = -1
        while opcion in [0, 1, 2]:
            try:
                opcion = int(input("\nIngresa la opción: "))
            except ValueError:
                print("Valor no valido.")
        if opcion == 1:
            CNombre = ""
            while CNombre == "":
                CNombre = input("\n- Ingresa el nombre del credito: ")
                if CNombre == "":
                    print("Debe indicar al menos un carácter.\n")
            for 
        if opcion == 2:
            CValorMinimo, CValorMaximo = -1.0, -1.0
            while CValorMinimo < 0:
                try:
                    CValorMinimo = float(input("\nIngresa el valor mínimo: "))
                except ValueError:
                    print("Valor no valido.")
            while CValorMaximo < 0:
                try:
                    CValorMaximo = float(input("\nIngresa el valor máximo: "))
                except ValueError:
                    print("Valor no valido.")

        if opcion == 0:
            pass
    def asignarcredito(self):
        print("\nIngresa los datos del usuario:")
        busquedacliente = True
        while busquedacliente:
            Idcliente = -1
            Objcliente = None
            while Idcliente < 0:
                try:
                    Idcliente = int(input("\n- Ingresa el ID del cliente: "))
                except ValueError:
                    print("El valor ingresado no es valido.")
            for i in range(len(self.DBancoUsuarios)):
                if self.DBancoUsuarios[i].idusuario == Idcliente:
                    busquedacliente = False
                    asignarmismocliente = True
                    while asignarmismocliente:
                        Objcliente = self.DBancoUsuarios[i]
                        print("\nIngresa los datos del credito a registrar:")
                        CNombre, CValor, CDuracion = "", -1.0, -1
                        while CNombre == "":
                            CNombre = input("\n- Ingresa el nombre del credito: ")
                            if CNombre == "":
                                print("Debe indicar al menos un carácter.\n")
                        while CValor < 0.0:
                            try:
                                CValor = float(input("- Ingresa el valor: "))
                            except ValueError:
                                print("El valor ingresado no es valido.")
                        while CDuracion < 0:
                            try:
                                CDuracion = int(
                                    input(
                                        "- Ingresa la duración del credito en meses: "
                                    )
                                )
                            except ValueError:
                                print("El valor ingresado no es valido.")

                        CanCreditos = len(Objcliente.creditos)
                        Objcliente.creditos[CanCreditos + 1] = ObjB.Creditos(
                            CNombre, CValor, CDuracion
                        )
                        print("Registro exitoso.")
                        otrocredito = ""
                        while otrocredito.lower() not in ["s", "n"]:
                            otrocredito = input(
                                "\n¿Desea ingresa otro credito para el mismo cliente? (S/N): "
                            )
                            if otrocredito.lower() == "n":
                                asignarmismocliente = False
                        clienteexite = True
            if clienteexite == False:
                print("\nEl usuario no existe.")
                otrabusqueda = ""
                while otrabusqueda.lower() not in ["s", "n"]:
                    otrabusqueda = input("\n¿Desea buscar otro cliente? (S/N): ")
                    if otrabusqueda.lower() == "n":
                        busquedacliente = False

    def mostrarpilas(self):
        EstadoPila = True
        print("\nPila usuarios: ")
        while self.DBancoUsuarios:
            for i in range(len(self.DBancoUsuarios)):
                estadocreditos = True
                print(
                    f"\nId: {self.DBancoUsuarios[i].idusuario}",
                    f"\nNombre: {self.DBancoUsuarios[i].nombreusuario}",
                    f"\nRol: {self.DBancoUsuarios[i].rol}",
                )
                for Ncredito, credito in self.DBancoUsuarios[i].creditos.items():
                    print(
                        f"\nCredito: {Ncredito}",
                        f"\nTipo: {credito.tipocredito}",
                        f"\nValor: {credito.valorcredito}",
                        f"\nDuración: {credito.duracion}",
                    )
                    estadocreditos = False
                if estadocreditos:
                    print("\nCreditos: Cliente sin creditos.")
            EstadoPila = False
            break
        if EstadoPila:
            print("\nPila clientes vacía.")
