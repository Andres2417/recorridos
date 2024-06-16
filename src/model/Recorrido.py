class Recorrido:
    def __init__(self, id_recorrido, nombre, descripcion, duracion, precio):
        """
        Inicializa un nuevo objeto Recorrido.

        Args:
            id_recorrido (int): ID único del recorrido.
            nombre (str): Nombre del recorrido.
            descripcion (str): Descripción del recorrido.
            duracion (float): Duración del recorrido en horas.
            precio (float): Precio del recorrido.
        """
        self.id_recorrido = id_recorrido
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.precio = precio
        self.fotos = []
        self.comentarios = []

    def obtenerNotaPromedio(self):
        """
        Calcula la nota promedio de los comentarios del recorrido.

        Returns:
            float: Nota promedio (0 si no hay comentarios).
        """
        if not self.comentarios:
            return 0
        total = sum([comentario.calificacion for comentario in self.comentarios])
        return total / len(self.comentarios)

    def agregarComentario(self, comentario):
        """
        Agrega un comentario al recorrido.

        Args:
            comentario (Comentario): Objeto Comentario a agregar.
        """
        self.comentarios.append(comentario)
