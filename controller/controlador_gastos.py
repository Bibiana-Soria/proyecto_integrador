from model.egresos import Egresos
from tkinter import messagebox

class ControladorGastos:
    def __init__(self):
        self.modelo = Egresos()
    
    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    def obtener_todos_los_gastos(self):
        return self.modelo.consultar()

    def agregar_gasto(self, id_insumo, proveedor, descripcion, monto, cantidad_comprada):

        if not id_insumo or str(id_insumo) == "None":
            print("ID vacío, no se crea egreso")
            return True

        resultado = self.modelo.insertar(
            id_insumo,
            proveedor,
            descripcion,
            monto,
            cantidad_comprada
        )

        self.respuesta_sql(resultado)
        return resultado
 
    def actualizar_gasto(self, id_egreso, id_insumo, proveedor, descripcion, monto, cantidad_comprada):
        if not id_egreso:
            messagebox.showerror("Error", "ID Egreso es requerido para modificar")
            return False
        resultado = self.modelo.cambiar(id_insumo, proveedor, descripcion, monto, cantidad_comprada, id_egreso)
        self.respuesta_sql(resultado)
        return resultado
    
    def eliminar_gasto(self, id_egreso):
        resultado = self.modelo.eliminar(id_egreso)
        self.respuesta_sql(resultado)
        return resultado