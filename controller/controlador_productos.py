from model.productos import Productos
from tkinter import messagebox

class ControladorProductos:
    def __init__(self):
        self.modelo = Productos()

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(message="Action completed successfully", icon="info")
        else:
            messagebox.showerror(message="An error occurred during operation", icon="error")

    def obtener_productos(self):
        return self.modelo.consultar()

    def agregar_producto(self, nombre, tamano, precio):
        if not nombre or not precio:
            messagebox.showerror("Error", "Name and price are required")
            return False
        resultado = self.modelo.insertar(nombre, tamano, precio)
        self.respuesta_sql(resultado)
        return resultado

    def actualizar_producto(self, id_producto, nombre, tamano, precio):
        try:
            
            if not id_producto:
                print("ERROR: ID de producto vacío")
                messagebox.showerror("Error", "ID is required to modify")
                return False
            resultado = self.modelo.cambiar(nombre, tamano, precio, id_producto)
            self.respuesta_sql(resultado)
            return resultado
            
        except Exception as e:
            print(f"ERROR COMPLETO en controlador actualizar_producto:")
            import traceback
            traceback.print_exc()
            messagebox.showerror("Error", f"Controller error: {e}")
            return False

    def eliminar_producto(self, id_producto):
        if not id_producto:
            messagebox.showerror("Error", "ID is required to delete")
            return False
        resultado = self.modelo.eliminar(id_producto)
        self.respuesta_sql(resultado)
        return resultado

    def buscar_producto(self, nombre):
        return self.modelo.buscar(nombre)