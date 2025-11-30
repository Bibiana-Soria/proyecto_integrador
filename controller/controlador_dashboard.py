from model.ventas import Ventas
from model.insumos import Insumos
from model.egresos import Egresos

class ControladorDashboard:
    def __init__(self):
        self.modelo_ventas = Ventas()
        self.modelo_insumos = Insumos()
        self.modelo_egresos = Egresos()

    def obtener_resumen_global(self):
        """
        Retorna un diccionario con datos para las tarjetas del dashboard.
        Ejemplo: Cantidad de ventas, alertas de stock, etc.
        """
        ventas = self.modelo_ventas.consultar()
        insumos = self.modelo_insumos.consultar()
        
        total_ingresos = 0
        stock_bajo = 0
        
        # Calcular ingresos totales (sumando la columna total de ventas)
        if ventas:
            for v in ventas:
                # Asumiendo que el total está en la columna 5 (índice 5) según tu modelo ventas
                # Ajusta el índice si tu tupla es diferente
                try:
                    total_ingresos += float(v[5]) 
                except:
                    pass

        # Calcular insumos con stock bajo (ejemplo: menos de 5 unidades)
        if insumos:
            for i in insumos:
                # Asumiendo cantidad en índice 2
                try:
                    if float(i[2]) < 5: 
                        stock_bajo += 1
                except:
                    pass

        return {
            "ingresos_totales": total_ingresos,
            "ventas_realizadas": len(ventas) if ventas else 0,
            "alertas_stock": stock_bajo
        }