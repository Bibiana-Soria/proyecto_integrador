from view.InterfazBaseTabla import HistorialBase
import customtkinter as ctk
from controller.controlador_insumos import ControladorInsumos

class interfaz_de_insumos(HistorialBase):

    def __init__(self, interface, parent_navegar, ventana_principal):

        self.headers = [
            "ID", "Nombre del insumo", "Unidad", "Cantidad", "Costo unitario"
        ]

        # CAMPOS PARA FORMULARIO
        self.form_campos = [
            "Nombre del insumo",
            "Unidad",
            "Cantidad",
            "Costo unitario",
            "Proveedor",
            "Descripción"
        ]

        self.controlador = ControladorInsumos()

        super().__init__(interface, parent_navegar, ventana_principal, self.form_campos, "Insumos")

        self.tabla = None
        self.crear_tabla()

    def crear_tabla(self):

        if self.tabla:
            self.tabla.destroy()

        self.tabla = ctk.CTkScrollableFrame(self.contenido, fg_color="#FEE3D0", corner_radius=20)
        self.tabla.grid(row=0, column=0, sticky="nsew")

        # Encabezados
        for col, text in enumerate(self.headers):
            lbl = ctk.CTkLabel(
                self.tabla, 
                text=text, 
                font=("Mochiy Pop One",20),
                text_color="#7A5230"
            )
            lbl.grid(row=0, column=col, padx=10, pady=10)
            lbl.grid(row=0, column=col, padx=10, pady=10)

        self.actualizar_tabla()

    def actualizar_tabla(self):

        for widget in self.tabla.winfo_children()[len(self.headers):]:
            widget.destroy()

        datos = self.controlador.obtener_insumos()

        if not datos:
            lbl = ctk.CTkLabel(self.tabla, text="No hay insumos registrados")
            lbl.grid(row=1, column=0, columnspan=len(self.headers), pady=10)
            return

        for i, fila in enumerate(datos, start=1):
            for col, valor in enumerate(fila):
                lbl = ctk.CTkLabel(self.tabla, text=str(valor), font=("Poppins", 16))
                lbl.grid(row=i, column=col, padx=10, pady=5)

    def on_data_changed(self):
        self.actualizar_tabla()

    # --- Control del formulario ---
    def agregar_registro_form(self, datos):
        self.controlador.agregar_insumo(
            datos["Nombre del insumo"],
            datos["Unidad"],
            datos["Cantidad"],
            datos["Costo unitario"],
            datos["Proveedor"],
            datos["Descripción"]
        )
        self.actualizar_tabla()

    def modificar_registro_form(self, datos):
        self.controlador.actualizar_insumo(
            datos["id"],
            datos["Nombre del insumo"],
            datos["Unidad"],
            datos["Cantidad"],
            datos["Costo unitario"]
        )
        self.actualizar_tabla()

    def eliminar_registro_form(self, id_eliminar):
        self.controlador.eliminar_insumo(id_eliminar)
        self.actualizar_tabla()
