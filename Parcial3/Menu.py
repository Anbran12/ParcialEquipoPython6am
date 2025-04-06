#import gestiondealgo as gda

while True:
    try:
        print("\n¡Bienvenido!")
        print("\nMenú:\n1. Opción 1.\n2. Opción 2.\n3. Opción 3.\n4. Opción 4.\n0. Salir.")
        Opcion = int(input("\nIngresa una de las siguientes opciones (1 - 4) o cero (0) para salir: "))
        if Opcion in [1]:
            if Opcion == 1:
                pass
#                P1 = p1.Punto1()
#                P1.punto1()
#            elif Opcion == 2:
#                P2 = p2.Punto2()
#                P2.punto2()
#            elif Opcion == 3:
#                P3 = p3.Punto3()
#                P3.punto3()
#            elif Opcion == 4:
#                P4 = p4.Punto4()
#                P4.punto4()
        elif Opcion in [2,3,4]:
            print("En mantenimiento...")
        elif Opcion == 0:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")
    except ValueError:
        print("\nEl valor ingresado no es valido.")