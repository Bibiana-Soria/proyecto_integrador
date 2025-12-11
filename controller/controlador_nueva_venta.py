from model.productos import Productos
from model.ventas import Ventas
from tkinter import messagebox

class ControladorNuevaVenta:
    def __init__(self):
        self.modelo_productos = Productos()
        self.modelo_ventas = Ventas()

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(message="Action completed successfully", icon="info")
        else:
            messagebox.showerror(message="An error occurred during operation", icon="error")

    def obtener_lista_productos(self):
        """
        Obtiene productos para mostrarlos en la búsqueda o lista de selección.
        """
        return self.modelo_productos.consultar()

    def buscar_producto(self, nombre):
        return self.modelo_productos.buscar(nombre)

    def registrar_venta(self, id_usuario, lista_items_carrito):
        """
        Recibe el ID del usuario actual y una lista de diccionarios/objetos del carrito.
        Estructura esperada de item: {'id_producto': x, 'cantidad': y, 'precio': z, 'total': w}
        """
        if not lista_items_carrito:
            return False

        exito_total = True
        for item in lista_items_carrito:
            id_prod = item.get('id_producto')
            cant = item.get('cantidad')
            prec_unit = item.get('precio')

            resultado = self.modelo_ventas.insertar(id_usuario, id_prod, cant, prec_unit)
            
            if not resultado:
                exito_total = False
        
        return exito_total