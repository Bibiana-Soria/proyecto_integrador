from view.InterfazBaseTabla import HistorialBase
import customtkinter as ctk
from controller.controlador_gastos import ControladorGastos

class interfaz_de_gastos(HistorialBase):
    def __init__(self, interface, parent_navegar, ventana_principal, id_usuario):
        self.controlador = ControladorGastos()
        self.id_usuario = id_usuario
        
        self.headers = ["Codigo", "Codigo Insumo", "Proveedor", "Descripcion", "Monto", "Cantidad Comprada", "Fecha"]
        
        self.form_campos = ["Codigo Insumo", "Proveedor", "Descripcion", "Monto", "Cantidad Comprada"]

        super().__init__(
            interface, 
            parent_navegar, 
            ventana_principal,
            self.form_campos, 
            titulo_panel="Gastos"
        )
        
        self.tabla = None
        self.crear_tabla_gastos()

    def crear_tabla_gastos(self):
        if self.tabla is not None:
            self.tabla.destroy()

        self.tabla = ctk.CTkScrollableFrame(
            self.contenido,
            fg_color="#FEE3D0",
            border_width=4,
            border_color="#D8B59D",
            corner_radius=40,
            width=800, height=400
        )
        self.tabla.grid(row=0, column=0, sticky="nsew")

        for col, text in enumerate(self.headers):
            lbl = ctk.CTkLabel(self.tabla, text=text,
                               font=("Mochiy Pop One", 20),
                               text_color="#7A5230")
            lbl.grid(row=0, column=col, padx=15, pady=10)

        self.actualizar_tabla()

    def actualizar_tabla(self):
        # Limpiar filas anteriores (preservando headers)
        for widget in list(self.tabla.winfo_children())[len(self.headers):]:
            widget.destroy()

        datos = self.controlador.obtener_todos_los_gastos(self.id_usuario)

        if not datos:
            lbl_vacio = ctk.CTkLabel(self.tabla, text="No hay gastos registrados", font=("Poppins", 16), text_color="#7A5230")
            lbl_vacio.grid(row=1, column=0, columnspan=len(self.headers), pady=20)
            return

        for i, fila in enumerate(datos, start=1):
            for col, valor in enumerate(fila[:-1]):
                lbl = ctk.CTkLabel(self.tabla, text=str(valor),
                                   font=("Poppins", 16),
                                   text_color="#7A5230")
                lbl.grid(row=i, column=col, padx=15, pady=5)
    
    def on_data_changed(self):
        self.actualizar_tabla()

    def agregar_gasto(self, id_insumo, proveedor, descripcion, monto, cantidad):
        self.controlador.agregar_gasto(id_insumo, proveedor, descripcion, monto, cantidad, self.id_usuario)
        self.actualizar_tabla()

    def actualizar_gasto(self, id_egreso, id_insumo, proveedor, descripcion, monto, cantidad):
        self.controlador.actualizar_gasto(id_egreso, id_insumo, proveedor, descripcion, monto, cantidad)
        self.actualizar_tabla()

    def eliminar_gasto(self, id_egreso):
        self.controlador.eliminar_gasto(id_egreso)
        self.actualizar_tabla()
