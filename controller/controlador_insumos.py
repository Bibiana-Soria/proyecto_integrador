from model.insumos import Insumos
from tkinter import messagebox
class ControladorInsumos:
    def __init__(self):
        self.modelo = Insumos()

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    def obtener_insumos(self):
        return self.modelo.consultar()

    def agregar_insumo(self, nombre, unidad, cantidad, precio, proveedor, descripcion):
        """
        Pasa los 6 argumentos necesarios al modelo
        """
        if not nombre or not precio:
            return False
        # Orden: nombre, unidad, cantidad, costo, proveedor, descripcion
        return self.modelo.insertar(nombre, unidad, cantidad, precio, proveedor, descripcion)

    def actualizar_insumo(self, nombre, unidad, cantidad, precio, id_insumo):
        # El modelo 'cambiar' solo actualiza datos del insumo, no proveedor/descripción
        return self.modelo.cambiar(nombre, unidad, cantidad, precio, id_insumo)

    def eliminar_insumo(self, id_insumo):
        return self.modelo.eliminar(id_insumo)

    def buscar_insumo(self, nombre):
        return self.modelo.buscar(nombre)