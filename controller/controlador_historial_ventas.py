from model.ventas import Ventas
from tkinter import messagebox
class ControladorHistorialVentas:
    def __init__(self):
        self.modelo = Ventas()

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    def obtener_todas_las_ventas(self, id_usuario_logueado):
        """
        Llama al modelo para obtener el historial de ventas de un usuario en específico.
        """
        return self.modelo.consultar(id_usuario_logueado)
