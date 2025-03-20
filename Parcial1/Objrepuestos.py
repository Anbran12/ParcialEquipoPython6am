class Repuestos:
    def __init__(self, nombre, descripcion, precio, disponibilidad):
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._disponibilidad = disponibilidad

    @property
    def nombre(self):
        return self._nombre   
    @property
    def descripcion(self):
        return self._descripcion
    @property
    def precio(self):
        return self._precio
    @property
    def disponibilidad(self):
        return self._disponibilidad
    
    @nombre.setter
    def nombre(self, nombre):
        if nombre != "":
            self._nombre = nombre
    @descripcion.setter
    def descripcion(self, descripcion):
        if descripcion != "":
            self._descripcion = descripcion
    @precio.setter
    def precio(self, precio):
        if precio > 0:
            self._precio = precio
    @disponibilidad.setter
    def disponibilidad(self, disponibilidad):
        if disponibilidad in [0,1]:
            self.disponibilidad = disponibilidad