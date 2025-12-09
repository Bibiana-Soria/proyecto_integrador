# view/InterfazProductos.py
from view.InterfazBaseTabla import HistorialBase
import customtkinter as ctk
from controller.controlador_productos import ControladorProductos

class interfaz_de_productos(HistorialBase):
    def __init__(self, interface, parent_navegar, ventana_principal):
        self.controlador = ControladorProductos()
        self.headers = ["Code", "Name", "Size", "Price"]  
        self.form_campos = ["Name", "Size", "Price"]
        

        super().__init__(
            interface,
            parent_navegar,
            ventana_principal,
            self.form_campos,
            "Products"
        )

        self.tabla = None
        self.crear_tabla_ventas()

    def crear_tabla_ventas(self):
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
            lbl = ctk.CTkLabel(
                self.tabla,
                text=text,
                font=("Mochiy Pop One", 20),
                text_color="#7A5230"
            )
            lbl.grid(row=0, column=col, padx=15, pady=10)

        self.actualizar_tabla()

    def actualizar_tabla(self):
        for widget in list(self.tabla.winfo_children())[len(self.headers):]:
            widget.destroy()

        datos = self.controlador.obtener_productos()

        if not datos:
            no_data = ctk.CTkLabel(
                self.tabla,
                text="No products registered",
                font=("Poppins", 16),
                text_color="#7A5230"
            )
            no_data.grid(row=1, column=0, columnspan=4, pady=10)
            return

        # Agregar filas
        for i, fila in enumerate(datos, start=1):
            for col, valor in enumerate(fila):
                lbl = ctk.CTkLabel(
                    self.tabla,
                    text=str(valor),
                    font=("Poppins", 16),
                    text_color="#7A5230"
                )
                lbl.grid(row=i, column=col, padx=15, pady=5)

    def on_data_changed(self):
        self.actualizar_tabla()

    def agregar_producto(self, nombre, tamano, precio):
        self.controlador.agregar_producto(nombre, tamano, precio)
        self.actualizar_tabla()

    def actualizar_producto(self, id_producto, nombre, tamano, precio):
        self.controlador.actualizar_producto(id_producto, nombre, tamano, precio)
        self.actualizar_tabla()

    def eliminar_producto(self, id_producto):
        self.controlador.eliminar_producto(id_producto)
        self.actualizar_tabla()
