from model.usuarios import Usuarios
from tkinter import messagebox
class ControladorLogueo:
    def __init__(self):
        self.modelo = Usuarios()

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    def validar_login(self, usuario, password):
        """
        Verifica las credenciales. 
        Retorna los datos del usuario si es correcto, o None si falla.
        """
        if not usuario or not password:
            return None
            
        return self.modelo.validar(usuario, password)
