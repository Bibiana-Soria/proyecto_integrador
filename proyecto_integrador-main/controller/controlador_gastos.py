from model.egresos import Egresos

class ControladorGastos:
    def __init__(self):
        self.modelo = Egresos()

    def obtener_todos_los_gastos(self):
        """
        Llama al modelo para obtener todos los registros de egresos.
        Retorna una lista de tuplas.
        """
        return self.modelo.consultar()

    def agregar_gasto(self, id_insumo, proveedor, descripcion, monto, cantidad_comprada):
        """
        Pasa los datos al modelo para insertar un nuevo gasto.
        """
        if not id_insumo or not proveedor or not monto:
            return False
        
        return self.modelo.insertar(id_insumo, proveedor, descripcion, monto, cantidad_comprada)

    def eliminar_gasto(self, id_egreso):
        return self.modelo.eliminar(id_egreso)