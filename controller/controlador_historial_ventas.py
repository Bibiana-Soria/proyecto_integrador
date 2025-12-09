from model.ventas import Ventas
from tkinter import messagebox
from conexionBD import cursor 

class ControladorHistorialVentas:
    def __init__(self):
        self.modelo = Ventas()

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(message="Action completed successfully", icon="info")
        else:
            messagebox.showerror(message="An error occurred during operation", icon="error")

    def obtener_todas_las_ventas(self, id_usuario_logueado):
        return self.modelo.consultar(id_usuario_logueado)

    def actualizar_venta(self, id_venta, id_usuario, id_producto, cantidad):
        try:
            # 1. Buscamos el precio actual del producto en la BD
            cursor.execute("SELECT precio FROM productos WHERE id_producto = %s", (id_producto,))
            resultado = cursor.fetchone()
            
            if not resultado:
                messagebox.showerror("Error", "Product Code does not exist")
                return

            precio_unitario = float(resultado[0])
            
            # 2. Calculamos el nuevo total
            total = float(cantidad) * precio_unitario

            # 3. Enviamos todo al modelo para actualizar
            exito = self.modelo.cambiar(id_usuario, id_producto, cantidad, precio_unitario, total, id_venta)
            self.respuesta_sql(exito)

        except Exception as e:
            print(f"Error en controlador actualizar venta: {e}")
            messagebox.showerror("Error", f"Error processing update: {e}")

    def eliminar_venta(self, id_venta):
        if not id_venta:
            messagebox.showerror("Error", "Must provide Sale Code")
            return
            
        # Confirmación de seguridad
        confirmacion = messagebox.askyesno("Confirm", "Are you sure you want to permanently delete this sale?")
        if confirmacion:
            exito = self.modelo.eliminar(id_venta)
            self.respuesta_sql(exito)