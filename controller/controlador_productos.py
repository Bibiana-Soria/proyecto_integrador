from model.productos import Productos
from tkinter import messagebox
class ControladorProductos:
    def __init__(self):
        self.modelo = Productos()

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    def obtener_productos(self):
        """
        Retorna la lista de todos los productos registrados.
        """
        return self.modelo.consultar()

    def agregar_producto(self, nombre, tamano, precio):
        """
        Valida y envía los datos para crear un nuevo producto.
        """
        if not nombre or not precio:
            return False
        
        return self.modelo.insertar(nombre, tamano, precio)

    def actualizar_producto(self, nombre, tamano, precio, id_producto):
        """
        Actualiza la información de un producto existente.
        """
        return self.modelo.cambiar(nombre, tamano, precio, id_producto)

    def eliminar_producto(self, id_producto):
        return self.modelo.eliminar(id_producto)

    def buscar_producto(self, nombre):
        return self.modelo.buscar(nombre)