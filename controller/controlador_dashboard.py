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
        insumos = self.modelo_insumos.consultar(id_usuario)
        egresos = self.modelo_egresos.consultar(id_usuario)

        total_ingresos = 0
        stock_bajo = 0
        total_gastos = 0
        if ventas:
            for v in ventas:
                try:
                    total_ingresos += float(v[5]) 
                except:
                    pass

        if insumos:
            for i in insumos:
                try:
                    if float(i[2]) < 5:
                        stock_bajo += 1
                except:
                    pass

        if egresos:
            for e in egresos:
                try:
                    total_gastos += float(e[4])
                except:
                    pass

        ganancia_neta = total_ingresos - total_gastos

        return {
            "ingresos_totales": total_ingresos,
            "ventas_realizadas": len(ventas) if ventas else 0,
            "alertas_stock": stock_bajo,
            "gastos_totales": total_gastos,
            "ganancia_neta": ganancia_neta
        }
    
    def obtener_ultimas_ventas(self, id_usuario):
        ventas = self.modelo_ventas.consultar(id_usuario)

        if not ventas:
            return []

        ventas_ordenadas = sorted(ventas, key=lambda v: v[2], reverse=True)
        return ventas_ordenadas[:10]
    
    def obtener_ultimos_egresos(self, id_usuario):
        egresos = self.modelo_egresos.consultar(id_usuario)

        if not egresos:
            return []
        
        egresos_ordenados = sorted(egresos, key=lambda e: e[6], reverse=True)
        return egresos_ordenados[:10]

            
            
