class Usuarios:
    def __init__(self, idusuario, nombreusuario, rol, creditos=None):
        if creditos is None:
            creditos = {}  # Se inicializa un nuevo diccionario
        self._idusuario = idusuario
        self._nombreusuario = nombreusuario
        self._rol = rol
        self._creditos = creditos  # Diccionario de créditos

    @property
    def nombreusuario(self):
        return self._nombreusuario

    @property
    def idusuario(self):
        return self._idusuario

    @property
    def rol(self):
        return self._rol

    @property
    def creditos(self):
        return self._creditos

    @nombreusuario.setter
    def nombreusuario(self, nombreusuario):
        if nombreusuario != "":
            self._nombreusuario = nombreusuario

    @idusuario.setter
    def idusuario(self, idusuario):
        if idusuario != 0:
            self._idusuario = idusuario

    @rol.setter
    def rol(self, rol):
        if rol.lower() in ["cliente", "admin"]:
            self._rol = rol

    @creditos.setter
    def creditos(self, creditos):
        #        if creditos.lower() in ["cliente","admin"]:
        self._creditos = creditos


class Creditos:
    def __init__(self, tipocredito, valorcredito, duracion):
        self._tipocredito = tipocredito
        self._valorcredito = valorcredito
        self._duracion = duracion

    @property
    def valorcredito(self):
        return self._valorcredito

    @property
    def tipocredito(self):
        return self._tipocredito

    @property
    def duracion(self):
        return self._duracion

    @valorcredito.setter
    def valorcredito(self, valorcredito):
        if valorcredito != 0.0:
            self._valorcredito = valorcredito

    @tipocredito.setter
    def tipocredito(self, tipocredito):
        if tipocredito != "":
            self._tipocredito = tipocredito

    @duracion.setter
    def duracion(self, duracion):
        if duracion != 0:
            self._duracion = duracion
