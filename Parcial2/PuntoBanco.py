import Principal as P

class Banco:
    def banco(self):
        Obj = P.Principal()
        Obj.regitrarse()
        Obj.login()
        Obj.asignarcredito()
        Obj.mostrarpilas()
#        while Id == -1:
#            try:
#                Id = int(input("\nIngresa el ID del cliente: "))
#            except ValueError:
#                        print("El valor ingresado no es valido.")

Pb = Banco()
Pb.banco()
