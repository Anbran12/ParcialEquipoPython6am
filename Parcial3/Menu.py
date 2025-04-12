import Metodos as M

P1 = M.Metodos() 


while True:
    try:
        print("\n¡Bienvenido!")
        print("\nMenú:\n1. Registrar personas.\n2. Mostrar personas registradas.\n3. Modificar información.\n0. Salir.")
        Opcion = int(input("\nIngresa una de las siguientes opciones (1 - 4) o cero (0) para salir: "))
        if Opcion in [1, 2, 3]:
            if Opcion == 1:
                P1.ingreso()
            elif Opcion == 2:
                P1.mostrarpersonas()
            elif Opcion == 3:
                P1.modificar()
#            elif Opcion == 4:
#                P4 = p4.Punto4()
#                P4.punto4()
        elif Opcion in [4]:
            print("En mantenimiento...")
        elif Opcion == 0:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")
    except ValueError:
        print("\nEl valor ingresado no es valido.")