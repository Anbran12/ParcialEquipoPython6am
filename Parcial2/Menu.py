import PuntoBanco as pb

while True:
    try:
        print("\n 1. Banco\n 2. En Mantenimiento.\n 3. En Mantenimiento.")
        Opcion = int(input("\nIngresa una de las siguientes opciones (1 - 3) o cero (0) para salir: "))
        if Opcion in [1]:
            if Opcion == 1:
                Pb = pb.Banco()
                Pb.banco()
        elif Opcion in [2,3,4,5,6,7,8,9,10]:
            print("En mantenimiento...")
        elif Opcion == 0:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")
    except ValueError:
        print("\nEl valor ingresado no es valido.")