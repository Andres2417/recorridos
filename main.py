import tkinter as tk

from tkinter import messagebox

from src.model.ControladorRecorridos import ControladorRecorridos
from src.model.Foto import Foto
from src.model.Recorrido import Recorrido
from src.model.Usuario import Usuario


class App:
    def __init__(self, root):
        self.root = root
        self.controlador = ControladorRecorridos()

        # Crear algunos usuarios y recorridos de prueba
        usuario1 = Usuario(1, "andres", "andres123")
        self.controlador.registrarUsuario(usuario1)
        recorrido1 = Recorrido(1, "Yarumos", "Visita al parque natural los Yarumos", "2 horas", 20000)
        recorrido2 = Recorrido(2, "Catedral", "Fundadores a la catedral de Manizales con paradas temáticas", "1 hora", 10000)
        recorrido1.fotos.append(Foto("https://th.bing.com/th/id/R.a5ab211c8e7989c38ec5614016e5c79f?rik=fQXqwpGjGMIZ1w&pid=ImgRaw&r=0", "Descripción de foto A"))
        recorrido2.fotos.append(Foto("https://th.bing.com/th/id/OIP.15NzRhBC0bjd-OwNSUS6-QHaEK?rs=1&pid=ImgDetMain", "Descripción de foto B"))
        self.controlador.registrarRecorrido(recorrido1)
        self.controlador.registrarRecorrido(recorrido2)

        # Variables
        self.usuario_actual = None

        # Configurar ventana principal
        self.root.title("Aplicación de Recorridos Guiados en Manizales")
        self.root.geometry("800x600")

        # ventana de autenticación
        self.frame_login = tk.Frame(self.root)
        self.label_usuario = tk.Label(self.frame_login, text="Nombre de usuario:")
        self.entry_usuario = tk.Entry(self.frame_login)
        self.label_clave = tk.Label(self.frame_login, text="Clave:")
        self.entry_clave = tk.Entry(self.frame_login, show="*")
        self.button_login = tk.Button(self.frame_login, text="Ingresar", command=self.autenticar)

        self.label_usuario.grid(row=0, column=0, pady=10)
        self.entry_usuario.grid(row=0, column=1, pady=10)
        self.label_clave.grid(row=1, column=0, pady=10)
        self.entry_clave.grid(row=1, column=1, pady=10)
        self.button_login.grid(row=2, columnspan=2, pady=10)

        self.frame_login.pack(pady=50)

    def autenticar(self):
        nombre_usuario = self.entry_usuario.get()
        clave = self.entry_clave.get()
        usuario = self.controlador.autenticarUsuario(nombre_usuario, clave)

        if usuario:
            self.usuario_actual = usuario
            messagebox.showinfo("Éxito", "Autenticación exitosa")
            self.mostrar_recorridos()
        else:
            messagebox.showerror("Error", "Autenticación fallida. Usuario o clave incorrectos.")

    def mostrar_recorridos(self):
        self.frame_login.pack_forget()
        self.frame_recorridos = tk.Frame(self.root)

        recorridos = self.controlador.mostrarRecorridos()
        self.listbox_recorridos = tk.Listbox(self.frame_recorridos)

        for recorrido in recorridos:
            self.listbox_recorridos.insert(tk.END, f"{recorrido.id_recorrido}: {recorrido.nombre}")

        self.button_seleccionar = tk.Button(self.frame_recorridos, text="Seleccionar",
                                            command=self.seleccionar_recorrido)
        self.listbox_recorridos.pack(pady=10)
        self.button_seleccionar.pack(pady=10)
        self.frame_recorridos.pack(pady=50)

    def seleccionar_recorrido(self):
        seleccion = self.listbox_recorridos.curselection()
        if seleccion:
            id_recorrido = int(self.listbox_recorridos.get(seleccion).split(":")[0])
            recorrido = self.controlador.obtenerDetalleRecorrido(id_recorrido)
            if recorrido:
                self.mostrar_detalle_recorrido(recorrido)

    def mostrar_detalle_recorrido(self, recorrido):
        self.frame_recorridos.pack_forget()
        self.frame_detalle = tk.Frame(self.root)

        label_nombre = tk.Label(self.frame_detalle, text=f"Nombre: {recorrido.nombre}")
        label_descripcion = tk.Label(self.frame_detalle, text=f"Descripción: {recorrido.descripcion}")
        label_duracion = tk.Label(self.frame_detalle, text=f"Duración: {recorrido.duracion}")
        label_precio = tk.Label(self.frame_detalle, text=f"Precio: {recorrido.precio}")

        label_nombre.pack(pady=5)
        label_descripcion.pack(pady=5)
        label_duracion.pack(pady=5)
        label_precio.pack(pady=5)

        label_fotos = tk.Label(self.frame_detalle, text="Fotos:")
        label_fotos.pack(pady=5)
        for foto in recorrido.fotos:
            label_foto = tk.Label(self.frame_detalle, text=f"  - {foto.descripcion} \n ({foto.url})")
            label_foto.pack(pady=2)

        label_comentarios = tk.Label(self.frame_detalle, text="Comentarios:")
        label_comentarios.pack(pady=5)
        for comentario in recorrido.comentarios:
            label_comentario = tk.Label(self.frame_detalle,
                                        text=f"  - {comentario.texto} (Calificación: {comentario.calificacion}, Usuario: {comentario.usuario.nombre_usuario}, Fecha: {comentario.fecha})")
            label_comentario.pack(pady=2)

        nota_promedio = tk.Label(self.frame_detalle, text=f"Nota promedio (1-5): {recorrido.obtenerNotaPromedio()}")
        nota_promedio.pack(pady=5)

        self.label_input1 = tk.Label(self.frame_detalle, text="Comentario:")
        self.entry_comentario = tk.Entry(self.frame_detalle)
        self.label_input2 = tk.Label(self.frame_detalle, text="Calificación:")
        self.entry_calificacion = tk.Entry(self.frame_detalle)

        self.label_input1.pack(pady=5)
        self.entry_comentario.pack(pady=5)
        self.label_input2.pack(pady=5)
        self.entry_calificacion.pack(pady=5)


        self.button_comentar = tk.Button(self.frame_detalle, text="Comentar",
                                         command= lambda: self.escribir_comentario(recorrido))

        self.button_comentar.pack(pady=5)

        self.frame_detalle.pack(pady=50)

    def escribir_comentario(self, recorrido):
        texto = self.entry_comentario.get()
        calificacion = int(self.entry_calificacion.get())
        comentario = self.controlador.crearComentario(texto, calificacion, self.usuario_actual)
        self.controlador.agregarComentario(recorrido.id_recorrido, comentario)
        messagebox.showinfo("Éxito", "Comentario guardado exitosamente")
        self.frame_detalle.pack_forget()
        self.mostrar_recorridos()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
