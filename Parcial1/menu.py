import Punto6 as p6
import Punto7 as p7
while True:
    try:
        print("\n 1. En Mantenimiento.\n 2. En Mantenimiento.\n 3. En Mantenimiento.\n 4. En Mantenimiento.\n 5. En Mantenimiento.\n 6. Registro repuestos motos Yamaha.\n 7. Promedio de estudiantes.\n 8. En Mantenimiento.\n 9. En Mantenimiento.\n 10. En Mantenimiento.")
        Opcion = int(input("\nIngresa una de las siguientes opciones (1 - 10) o cero (0) para salir: "))
        if Opcion in [6,7]:
            if Opcion == 6:
                P6 = p6.Punto6()
                P6.punto6()
            if Opcion == 7:
                P7 = p7.agrupar_estudiantes()

        elif Opcion in [1,2,3,4,5,7,8,9,10]:
            print("En mantenimiento...")
        elif Opcion == 0:
            print("Saliendo...")
            break
        else:
            print("Opcion no valida.")
    except ValueError:
        print("\nEl valor ingresado no es valido.")