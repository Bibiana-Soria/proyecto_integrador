from model.ventas import Ventas
from model.insumos import Insumos
from model.egresos import Egresos
from tkinter import messagebox

class ControladorDashboard:
    def __init__(self):
        self.modelo_ventas = Ventas()
        self.modelo_insumos = Insumos()
        self.modelo_egresos = Egresos()

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(message="Acción realizada con éxito", icon="info")
        else:
            messagebox.showerror(message="Ocurrió un error en la operación", icon="error")

    def obtener_resumen_global(self, id_usuario):

        ventas = self.modelo_ventas.consultar(id_usuario)
        insumos = self.modelo_insumos.consultar()
        egresos = self.modelo_egresos.consultar()

        total_ingresos = 0
        stock_bajo = 0
        total_gastos = 0
        
        # Calcular ingresos totales
        if ventas:
            for v in ventas:
                try:
                    total_ingresos += float(v[5]) 
                except:
                    pass

        # Calcular stock bajo
        if insumos:
            for i in insumos:
                try:
                    if float(i[2]) < 5:
                        stock_bajo += 1
                except:
                    pass

        # Calcular gastos totales
        if egresos:
            for e in egresos:
                try:
                    total_gastos += float(e[4])   # ← monto correcto
                except:
                    pass


        return {
            "ingresos_totales": total_ingresos,
            "ventas_realizadas": len(ventas) if ventas else 0,
            "alertas_stock": stock_bajo,
            "gastos_totales": total_gastos
        }
    
    def obtener_ultimas_ventas(self, id_usuario):
        ventas = self.modelo_ventas.consultar(id_usuario)

        if not ventas:
            return []

        # Ordenadas por fecha_venta (posición 2)
        ventas_ordenadas = sorted(ventas, key=lambda v: v[2], reverse=True)

        return ventas_ordenadas[:10]
    
    def obtener_ultimos_egresos(self):
        egresos = self.modelo_egresos.consultar()

        if not egresos:
            return []

        # Ordenados por fecha (posicion 6)
        egresos_ordenados = sorted(egresos, key=lambda e: e[6], reverse=True)

        return egresos_ordenados[:10]

            
            
