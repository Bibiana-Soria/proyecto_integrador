from view.InterfazBaseTabla import HistorialBase
import customtkinter as ctk
<<<<<<< HEAD
=======
from controller.controlador_gastos import ControladorGastos
>>>>>>> 5718117065bf8efc8fa6b8cfb2bd703f5cab660d

class interfaz_de_gastos(HistorialBase):
    def __init__(self, interface, parent_navegar, ventana_principal):
        self.headers = ["ID", "Insumo", "Proveedor", "Descripcion", "Monto", "Cantidad comprada", "Fecha"]
<<<<<<< HEAD
        super().__init__(interface, parent_navegar, ventana_principal,self.headers, titulo_panel="Gastos")
        self.crear_tabla_ventas()

    def crear_tabla_ventas(self):
=======
        self.controlador = ControladorGastos()
        super().__init__(interface, parent_navegar, ventana_principal,self.headers, titulo_panel="Gastos")
        self.crear_tabla_gastos()

    def crear_tabla_gastos(self):
>>>>>>> 5718117065bf8efc8fa6b8cfb2bd703f5cab660d
        tabla = ctk.CTkScrollableFrame(
            self.contenido,
            fg_color="#FEE3D0",
            border_width=4,
            border_color="#D8B59D",
            corner_radius=40,
            width=800, height=400
        )
        tabla.grid(row=0, column=0, sticky="nsew")

<<<<<<< HEAD
        self.headers = ["ID", "Insumo", "Proveedor", "Descripcion", "Monto", "Cantidad comprada", "Fecha"]
=======
>>>>>>> 5718117065bf8efc8fa6b8cfb2bd703f5cab660d
        for col, text in enumerate(self.headers):
            lbl = ctk.CTkLabel(tabla, text=text,
                               font=("Mochiy Pop One", 20),
                               text_color="#7A5230")
            lbl.grid(row=0, column=col, padx=15, pady=10)

        # Datos de ejemplo o traídos de la BD 
<<<<<<< HEAD
        datos = [
            (1, "Lechera", "Sams's Club", "Leche condensada", "$458", "10", "11/23/2025"),
        ]
=======
        datos = self.controlador.obtener_todos_los_gastos()

        if not datos:
            lbl_vacio = ctk.CTkLabel(tabla, text="No hay gastos registrados", font=("Poppins", 16))
            lbl_vacio.grid(row=1, column=0, columnspan=len(self.headers), pady=20)
            return
>>>>>>> 5718117065bf8efc8fa6b8cfb2bd703f5cab660d

        for i, fila in enumerate(datos, start=1):
            for col, valor in enumerate(fila):
                lbl = ctk.CTkLabel(tabla, text=str(valor),
                                   font=("Poppins", 16),
                                   text_color="#7A5230")
                lbl.grid(row=i, column=col, padx=15, pady=5)
