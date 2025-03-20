import Objrepuestos as Obj1

class Metodos:
    def crearyllenarmatriz(self):
        dim = int(input("Ingresa la dimensión de la matriz: "))
        matriz = [[None for i in range(dim)]for j in range(dim)]
        self.matriz = matriz
        disponibles = []
        self.disponibles = disponibles

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                N,D,P,D1 = "","",0.0,None
                while N == "":
                    try:
                        N = input("\nIngresa el nombre del repuesto: ")                        
                    except ValueError:
                        print("El valor ingresado no es valido.")
                while D == "":
                    try:
                        D = input("Ingresa la descripción: ")                                                
                    except ValueError:
                        print("El valor ingresado no es valido.")
                while P == 0.0:
                    try:
                        P = int(input("Ingresa el precio: "))                        
                    except ValueError:
                        print("El valor ingresado no es valido.")
                while D1 == None:
                    try:
                        D1 = int(input("Ingresa la disponibilidad (0 / 1): "))
                    except ValueError:
                        print("El valor ingresado no es valido.")
                
                self.matriz[i][j] = Obj1.Repuestos(N,D,P,D1)

    def productosdisponibles(self):
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                Vdisponible = self.matriz[i][j].disponibilidad
                Objeto = self.matriz[i][j]
                if Vdisponible == 1:
                    self.disponibles.append(Objeto)
                    
    def mostrartodoslosproductos(self):
        print("\nTodos los productos: ")        
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                dispo = ""
                dispo1 = self.matriz[i][j].disponibilidad
                if dispo1 == 0:
                    dispo = "No disponible."
                if dispo1 == 1:
                    dispo = "Disponible."
                print(f"\nNombre: {self.matriz[i][j].nombre}\nDescripción: {self.matriz[i][j].descripcion}\nPrecio: {self.matriz[i][j].precio}\nDisponible: {dispo}")
    
    def mostrardisponibles(self):
        print("\nProductos disponibles: ")
        for i in range(len(self.disponibles)):
            print(f"\nNombre: {self.disponibles[i].nombre}\nDescripción: {self.disponibles[i].descripcion}\nPrecio: {self.disponibles[i].precio}")