from model.ventas import Ventas
from model.egresos import Egresos
from model.insumos import Insumos
from model.productos import Productos
from tkinter import messagebox
from openpyxl import Workbook

class ControladorReportes:

    def exportar_ventas(self, id_usuario):
        datos = Ventas.consultar(id_usuario)
        self.crear_excel("Reporte de Ventas", 
                         ["ID Venta", "ID Producto", "Fecha", "Cantidad", "Precio Unitario", "Total"], 
                         datos,
                         "reporte_ventas.xlsx")

    def exportar_egresos(self):
        datos = Egresos.consultar()
        self.crear_excel("Reporte de Egresos", 
                         ["ID Egreso", "ID Insumo", "Proveedor", "Descripción", "Monto", "Cantidad", "Fecha"],
                         datos,
                         "reporte_egresos.xlsx")

    def exportar_insumos(self):
        datos = Insumos.consultar()
        self.crear_excel("Reporte de Insumos",
                         ["ID Insumo", "Nombre", "Unidad", "Cantidad", "Costo Unitario"],
                         datos,
                         "reporte_insumos.xlsx")

    def exportar_productos(self):
        datos = Productos.consultar()
        self.crear_excel("Reporte de Productos",
                         ["ID Producto", "Nombre", "Tamaño", "Precio"],
                         datos,
                         "reporte_productos.xlsx")

    # --------------------------------------------
    # FUNCIÓN REUTILIZABLE PARA GENERAR EXCEL
    # --------------------------------------------
    def crear_excel(self, titulo, encabezados, datos, nombre_archivo):
        try:
            wb = Workbook()
            ws = wb.active
            ws.title = titulo

            ws.append(encabezados)

            for fila in datos:
                ws.append(fila)

            wb.save(nombre_archivo)

            messagebox.showinfo("Éxito", f"Reporte generado: {nombre_archivo}")

        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el reporte:\n{e}")
