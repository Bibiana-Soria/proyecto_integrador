from tkinter import messagebox
from model.ventas import Ventas
from conexionBD import cursor

class ControladorHistorialVentas:
    def __init__(self):
        self.modelo = Ventas
        self.cursor = cursor

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(message="Action completed successfully", icon="info")
        else:
            messagebox.showerror(message="An error occurred during operation", icon="error")

    def obtener_todas_las_ventas(self, id_usuario_logueado):
        try:
            resultado = self.modelo.consultar(id_usuario_logueado)
            return resultado
        except Exception as e:
            print(f"Error obteniendo ventas: {e}")
            messagebox.showerror("Error", f"Error loading sales: {e}")
            return []

    def actualizar_venta(self, id_venta, id_usuario, id_producto, cantidad):
        try:
            self.cursor.execute("SELECT precio FROM productos WHERE id_producto = %s", (id_producto,))
            resultado = self.cursor.fetchone()
            
            if not resultado:
                messagebox.showerror("Error", "Product Code does not exist")
                return

            precio_unitario = float(resultado[0])
            exito = self.modelo.cambiar(id_usuario, id_producto, cantidad, precio_unitario, id_venta)
            self.respuesta_sql(exito)

        except Exception as e:
            print(f"Error en controlador actualizar venta: {e}")
            import traceback
            traceback.print_exc()
            messagebox.showerror("Error", f"Error processing update: {e}")

    def eliminar_venta(self, id_venta):
        try:
            exito = self.modelo.eliminar(id_venta)
            self.respuesta_sql(exito)
        except Exception as e:
            print(f"Error en controlador eliminar venta: {e}")
            messagebox.showerror("Error", f"Error processing deletion: {e}")