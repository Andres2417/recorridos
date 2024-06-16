from datetime import datetime
from src.model.Comentario import Comentario

class ControladorRecorridos:
    """
    Controlador para gestionar recorridos y usuarios.

    Attributes:
        recorridos (list): Lista de recorridos disponibles.
        usuarios (list): Lista de usuarios registrados.
        ultimo_id_comentario (int): Último ID asignado a un comentario.
    """

    def __init__(self):
        """
        Inicializa un nuevo ControladorRecorridos.
        """
        self.recorridos = []
        self.usuarios = []
        self.ultimo_id_comentario = 0

    def mostrarRecorridos(self):
        """
        Devuelve la lista de recorridos disponibles.

        Returns:
            list: Lista de objetos Recorrido.
        """
        return self.recorridos

    def obtenerDetalleRecorrido(self, id_recorrido):
        """
        Obtiene los detalles de un recorrido dado su ID.

        Args:
            id_recorrido (int): ID del recorrido.

        Returns:
            Recorrido or None: Objeto Recorrido o None si no se encuentra.
        """
        for recorrido in self.recorridos:
            if recorrido.id_recorrido == id_recorrido:
                return recorrido
        return None

    def agregarComentario(self, id_recorrido, comentario):
        """
        Agrega un comentario a un recorrido específico.

        Args:
            id_recorrido (int): ID del recorrido.
            comentario (Comentario): Objeto Comentario a agregar.
        """
        recorrido = self.obtenerDetalleRecorrido(id_recorrido)
        if recorrido:
            recorrido.agregarComentario(comentario)

    def autenticarUsuario(self, nombre_usuario, clave):
        """
        Autentica a un usuario dado su nombre de usuario y clave.

        Args:
            nombre_usuario (str): Nombre de usuario.
            clave (str): Clave de acceso.

        Returns:
            Usuario or None: Objeto Usuario autenticado o None si no se encuentra.
        """
        for usr in self.usuarios:
            if usr.nombre_usuario == nombre_usuario and usr.autenticar(clave):
                return usr
        return None

    def registrarUsuario(self, usuario):
        """
        Registra un nuevo usuario.

        Args:
            usuario (Usuario): Objeto Usuario a registrar.
        """
        self.usuarios.append(usuario)

    def registrarRecorrido(self, recorrido):
        """
        Registra un nuevo recorrido.

        Args:
            recorrido (Recorrido): Objeto Recorrido a registrar.
        """
        self.recorridos.append(recorrido)

    def crearComentario(self, texto, calificacion, usuario):
        """
        Crea un nuevo objeto Comentario.

        Args:
            texto (str): Texto del comentario.
            calificacion (int): Calificación del recorrido (1-5).
            usuario (Usuario): Objeto Usuario que realiza el comentario.

        Returns:
            Comentario: Objeto Comentario creado.
        """
        self.ultimo_id_comentario += 1
        fecha = datetime.now()
        comentario = Comentario(self.ultimo_id_comentario, texto, calificacion, fecha, usuario)
        return comentario
