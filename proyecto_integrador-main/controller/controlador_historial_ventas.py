from model.ventas import Ventas

class ControladorHistorialVentas:
    def __init__(self):
        self.modelo = Ventas()

    def obtener_todas_las_ventas(self):
        """
        Llama al modelo para obtener el historial de ventas.
        """
        return self.modelo.consultar()
