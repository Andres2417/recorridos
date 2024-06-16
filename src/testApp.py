import unittest
from datetime import datetime
from tkinter import Tk

from main import App
from src.model.ControladorRecorridos import ControladorRecorridos
from src.model.Recorrido import Recorrido
from src.model.Usuario import Usuario


class TestAplicacion(unittest.TestCase):
    def setUp(self):
        """
        Configura el entorno de prueba inicial.
        Registra un usuario y un recorrido para ser utilizados en las pruebas.
        """
        self.controlador = ControladorRecorridos()
        self.usuario1 = Usuario(1, "andres", "andres123")
        self.controlador.registrarUsuario(self.usuario1)
        self.recorrido1 = Recorrido(1, "Recorrido A", "Descripción A", "2 horas", 100.0)
        self.controlador.registrarRecorrido(self.recorrido1)

    def test_autenticar_usuario(self):
        """
        Prueba la autenticación de un usuario con credenciales correctas e incorrectas.

        Verifica que un usuario con credenciales correctas sea autenticado exitosamente
        y que un usuario con credenciales incorrectas no sea autenticado.
        """
        usuario = self.controlador.autenticarUsuario("andres", "andres123")
        self.assertIsNotNone(usuario)
        self.assertEqual(usuario.nombre_usuario, "andres")

        usuario_invalido = self.controlador.autenticarUsuario("andres", "clave_incorrecta")
        self.assertIsNone(usuario_invalido)

    def test_agregar_y_obtener_comentario(self):
        """
        Prueba agregar un comentario a un recorrido y verifica que se haya agregado correctamente.

        Crea un comentario, lo agrega a un recorrido, y verifica que el comentario esté presente
        en la lista de comentarios del recorrido.
        """
        comentario = self.controlador.crearComentario("Buen recorrido", 4, self.usuario1)
        self.controlador.agregarComentario(1, comentario)

        recorrido = self.controlador.obtenerDetalleRecorrido(1)
        self.assertEqual(len(recorrido.comentarios), 1)
        self.assertEqual(recorrido.comentarios[0].texto, "Buen recorrido")
        self.assertEqual(recorrido.comentarios[0].calificacion, 4)

    def test_obtener_nota_promedio(self):
        """
        Prueba el cálculo de la nota promedio de los comentarios de un recorrido.

        Agrega dos comentarios con diferentes calificaciones a un recorrido y verifica que la nota
        promedio se calcule correctamente.
        """
        comentario1 = self.controlador.crearComentario("Buen recorrido", 4, self.usuario1)
        comentario2 = self.controlador.crearComentario("Excelente recorrido", 5, self.usuario1)
        self.controlador.agregarComentario(1, comentario1)
        self.controlador.agregarComentario(1, comentario2)

        recorrido = self.controlador.obtenerDetalleRecorrido(1)
        nota_promedio = recorrido.obtenerNotaPromedio()
        self.assertEqual(nota_promedio, 4.5)

    def test_registrar_y_obtener_recorrido(self):
        """
        Prueba registrar un nuevo recorrido y verifica que se haya registrado correctamente.

        Registra un nuevo recorrido y verifica que la lista de recorridos contenga
        el nuevo recorrido registrado.
        """
        recorrido2 = Recorrido(2, "Recorrido B", "Descripción B", "3 horas", 150.0)
        self.controlador.registrarRecorrido(recorrido2)

        recorridos = self.controlador.mostrarRecorridos()
        self.assertEqual(len(recorridos), 2)
        self.assertEqual(recorridos[1].nombre, "Recorrido B")

    def test_gui_autenticacion(self):
        """
        Prueba la autenticación de usuario en la interfaz gráfica.

        Simula la entrada del usuario en la GUI para probar la autenticación
        y verifica que el usuario sea autenticado correctamente.
        """
        root = Tk()
        app = App(root)

        app.entry_usuario.insert(0, "andres")
        app.entry_clave.insert(0, "andres123")
        app.autenticar()

        self.assertIsNotNone(app.usuario_actual)
        self.assertEqual(app.usuario_actual.nombre_usuario, "andres")

        root.destroy()


if __name__ == "__main__":
    unittest.main()
