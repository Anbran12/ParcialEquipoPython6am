#Santiago Andres Echeverri Montoya
class Estudiante:
    def _init_(self, nombre, apellido, carnet, semestre, promedio):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.semestre = semestre
        self.promedio = promedio

def agrupar_estudiantes():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            nombre = input(f"Ingrese nombre del estudiante en [{i}][{j}]: ")
            apellido = input(f"Ingrese el apellido del estudiante en [{i}][{j}]: ")
            carnet = int(input(f"Ingrese el carnet del estudiante en [{i}][{j}]: "))
            semestre = int(input(f"Ingrese el semestre del estudiante en [{i}][{j}]: "))

            total_calificaciones = 0
            num_calificaciones = int(input(f"Ingrese cuántas calificaciones tiene {nombre}: "))

            for _ in range(num_calificaciones):
                calificacion = float(input(f"Ingrese calificación de {nombre}: "))
                total_calificaciones += calificacion

            promedio = total_calificaciones / num_calificaciones
            fila.append(Estudiante(nombre, apellido, carnet, semestre, promedio))
        
        matriz.append(fila)

    grupo_EncimaDe4 = []
    grupo_Entre4_3 = []
    grupo_Debajo3 = []

    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j].promedio > 4:
                grupo_EncimaDe4.append(matriz[i][j])
            elif 3 <= matriz[i][j].promedio <= 4:
                grupo_Entre4_3.append(matriz[i][j])
            else:
                grupo_Debajo3.append(matriz[i][j])

    print("\nEstudiantes con promedio encima de 4:")
    for estudiante in grupo_EncimaDe4:
        print(f"Nombre: {estudiante.nombre} {estudiante.apellido} | Carnet: {estudiante.carnet} | Semestre: {estudiante.semestre} | Promedio: {estudiante.promedio:.2f}")

    print("\nEstudiantes con promedio entre 3 y 4:")
    for estudiante in grupo_Entre4_3:
        print(f"Nombre: {estudiante.nombre} {estudiante.apellido} | Carnet: {estudiante.carnet} | Semestre: {estudiante.semestre} | Promedio: {estudiante.promedio:.2f}")

    print("\nEstudiantes con promedio debajo de 3:")
    for estudiante in grupo_Debajo3:
        print(f"Nombre: {estudiante.nombre} {estudiante.apellido} | Carnet: {estudiante.carnet} | Semestre: {estudiante.semestre} | Promedio: {estudiante.promedio:.2f}")
