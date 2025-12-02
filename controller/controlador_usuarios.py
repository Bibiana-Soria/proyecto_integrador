from model.usuarios import Usuarios
from tkinter import messagebox
class ControladorUsuarios:
    def __init__(self):
        self.modelo = Usuarios()
    
    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    def obtener_usuarios(self):
        return self.modelo.consultar()

    def agregar_usuario(self, nombre, apellido, email, contrasena):
        """
        Registra un nuevo usuario en el sistema.
        """
        if not nombre or not email or not contrasena:
            return False
            
        return self.modelo.insertar(nombre, apellido, email, contrasena)

    def actualizar_usuario(self, nombre, apellido, email, contrasena, id_usuario):
        return self.modelo.cambiar(nombre, apellido, email, contrasena, id_usuario)

    def eliminar_usuario(self, id_usuario):
        return self.modelo.eliminar(id_usuario)

    def buscar_usuario(self, nombre):
        return self.modelo.buscar(nombre)