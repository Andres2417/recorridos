class Usuario:
    def __init__(self, id_usuario, nombre_usuario, clave):
        self.id_usuario = id_usuario
        self.nombre_usuario = nombre_usuario
        self.clave = clave

    def autenticar(self, clave):
        return self.clave == clave
