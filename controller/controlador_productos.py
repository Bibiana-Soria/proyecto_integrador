from model.productos import Productos
from tkinter import messagebox

class ControladorProductos:
    def __init__(self):
        self.modelo = Productos()

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    def obtener_productos(self):
        return self.modelo.consultar()

    def agregar_producto(self, nombre, tamano, precio):
        if not nombre or not precio:
            messagebox.showerror("Error", "Nombre y precio son requeridos")
            return False
        resultado = self.modelo.insertar(nombre, tamano, precio)
        self.respuesta_sql(resultado)
        return resultado

    def actualizar_producto(self, id_producto, nombre, tamano, precio):
        if not id_producto:
            messagebox.showerror("Error", "ID es requerido para modificar")
            return False
        resultado = self.modelo.cambiar(nombre, tamano, precio, id_producto)
        self.respuesta_sql(resultado)
        return resultado

    def eliminar_producto(self, id_producto):
        if not id_producto:
            messagebox.showerror("Error", "ID es requerido para eliminar")
            return False
        resultado = self.modelo.eliminar(id_producto)
        self.respuesta_sql(resultado)
        return resultado

    def buscar_producto(self, nombre):
        return self.modelo.buscar(nombre)
