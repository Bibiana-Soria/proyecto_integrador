from view.InterfazBaseTabla import HistorialBase
import customtkinter as ctk
from controller.controlador_historial_ventas import ControladorHistorialVentas
class Historial_de_ventas(HistorialBase):
    def __init__(self, interface, parent_navegar, ventana_principal):
        self.headers = ["ID", "Vendedor", "Productos", "Cantidad", "Total", "Ganancia Total"]

        self.controlador = ControladorHistorialVentas()


from controller.controlador_historial_ventas import ControladorHistorialVentas


class Historial_de_ventas(HistorialBase):
    def __init__(self, interface, parent_navegar, ventana_principal):
        self.headers = ["ID", "Vendedor", "Productos", "Cantidad", "Total", "Ganancia Total"]

        self.controlador = ControladorHistorialVentas()

        super().__init__(interface, parent_navegar, ventana_principal,self.headers, titulo_panel="Historial de Ventas")
        self.crear_tabla_ventas()

    def crear_tabla_ventas(self):
        tabla = ctk.CTkScrollableFrame(
            self.contenido,
            fg_color="#FEE3D0",
            border_width=4,
            border_color="#D8B59D",
            corner_radius=40,
            width=800, height=400
        )
        tabla.grid(row=0, column=0, sticky="nsew")

        self.headers = ["ID", "Vendedor", "Productos", "Cantidad", "Total", "Ganancia Total"]
        for col, text in enumerate(self.headers):
            lbl = ctk.CTkLabel(tabla, text=text,
                               font=("Mochiy Pop One", 20),
                               text_color="#7A5230")
            lbl.grid(row=0, column=col, padx=15, pady=10)

        # Datos de ejemplo o traídos de la BD 

        datos = [
            (1, "Gustavo", "Piña coco,\nFresa", "Piña coco: 2\n Fresa :2", "$458", "$126"),
        ]

        datos = [
            (1, "Gustavo", "Piña coco,\nFresa", "Piña coco: 2\n Fresa :2", "$458", "$126"),
        ]

        datos = self.controlador.obtener_todas_las_ventas()

        if not datos:
            lbl_vacio = ctk.CTkLabel(tabla, text="No hay ventas registradas", font=("Poppins", 16))
            lbl_vacio.grid(row=1, column=0, columnspan=len(self.headers), pady=20)
            return


        for i, fila in enumerate(datos, start=1):
            for col, valor in enumerate(fila):
                lbl = ctk.CTkLabel(tabla, text=str(valor),
                                   font=("Poppins", 16),
                                   text_color="#7A5230")
                lbl.grid(row=i, column=col, padx=15, pady=5)
