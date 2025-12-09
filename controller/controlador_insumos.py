from model.insumos import Insumos
from tkinter import messagebox
class ControladorInsumos:
    def __init__(self):
        self.modelo = Insumos()

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo("OK", "Action completed successfully")
        else:
            messagebox.showerror("Error", "An error occurred during operation")

    def obtener_insumos(self):
        return self.modelo.consultar()

    def agregar_insumo(self, nombre, unidad, cantidad, precio, proveedor, descripcion):
        if not nombre or not precio:
            messagebox.showerror("Error", "All fields are required")
            return False

        # 1. Insertar el insumo primero
        resultado = self.modelo.insertar(nombre, unidad, cantidad, precio, proveedor, descripcion)

        if resultado:

            # 2. Obtener el último ID insertado
            id_insumo = self.modelo.ultimo_id()

            # 3. Crear egreso automáticamente
            from model.egresos import Egresos
            from datetime import date

            egreso = Egresos()

            monto = float(precio) * float(cantidad)

            egreso.insertar(
                id_insumo,
                proveedor,
                f"Supply Purchase: {nombre}",
                monto,
                cantidad
            )

            messagebox.showinfo("OK", "Supply and expense registered correctly")
            return True

        else:
            messagebox.showerror("Error", "Could not save supply")
            return False

    def actualizar_insumo(self, id_insumo, nombre, unidad, cantidad, precio):
        resultado = self.modelo.cambiar(nombre, unidad, cantidad, precio, id_insumo)
        self.respuesta_sql(resultado)
        return resultado

    def eliminar_insumo(self, id_insumo):
        resultado = self.modelo.eliminar(id_insumo)
        self.respuesta_sql(resultado)
        return resultado

    def buscar_insumo(self, nombre):
        return self.modelo.buscar(nombre)

