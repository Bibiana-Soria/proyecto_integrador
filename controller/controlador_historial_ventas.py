from model.ventas import Ventas
from tkinter import messagebox
# Importamos conexión para poder buscar el precio del producto
from conexionBD import cursor 

class ControladorHistorialVentas:
    def __init__(self):
        self.modelo = Ventas()

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    def obtener_todas_las_ventas(self, id_usuario_logueado):
        return self.modelo.consultar(id_usuario_logueado)

    def actualizar_venta(self, id_venta, id_usuario, id_producto, cantidad):
        """
        Busca el precio del producto, recalcula el total y actualiza la venta.
        """
        try:
            # 1. Buscamos el precio actual del producto en la BD
            cursor.execute("SELECT precio FROM productos WHERE id_producto = %s", (id_producto,))
            resultado = cursor.fetchone()
            
            if not resultado:
                messagebox.showerror("Error", "El código de producto no existe")
                return

            precio_unitario = float(resultado[0])
            
            # 2. Calculamos el nuevo total
            total = float(cantidad) * precio_unitario

            # 3. Enviamos todo al modelo para actualizar
            exito = self.modelo.cambiar(id_usuario, id_producto, cantidad, precio_unitario, total, id_venta)
            self.respuesta_sql(exito)

        except Exception as e:
            print(f"Error en controlador actualizar venta: {e}")
            messagebox.showerror("Error", f"Error al procesar la actualización: {e}")