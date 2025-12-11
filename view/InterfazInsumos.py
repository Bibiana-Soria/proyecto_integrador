from view.InterfazBaseTabla import HistorialBase
import customtkinter as ctk
from controller.controlador_insumos import ControladorInsumos

class interfaz_de_insumos(HistorialBase):
    def __init__(self, interface, parent_navegar, ventana_principal, id_usuario):
        
        self.id_usuario = id_usuario
        self.fila_seleccionada = None 
        self.datos_seleccionados = None  
        
        self.headers = [
            "Code", "Supply Name", "Unit", "Quantity", "Unit Cost"
        ]

        self.form_campos = [
            "Supply Name",
            "Unit",
            "Quantity",
            "Unit Cost",
            "Provider",
            "Description"
        ]

        self.controlador = ControladorInsumos()

        super().__init__(interface, parent_navegar, ventana_principal, self.form_campos, "Supplies")

        self.tabla = None
        self.crear_tabla()

    def crear_tabla(self):
        if self.tabla:
            self.tabla.destroy()

        self.tabla = ctk.CTkScrollableFrame(self.contenido, fg_color="#FEE3D0", corner_radius=20)
        self.tabla.grid(row=0, column=0, sticky="nsew")

        for col, text in enumerate(self.headers):
            lbl = ctk.CTkLabel(
                self.tabla, 
                text=text, 
                font=("Mochiy Pop One",20),
                text_color="#7A5230"
            )
            lbl.grid(row=0, column=col, padx=10, pady=10)

        self.actualizar_tabla()

    def actualizar_tabla(self):
        for widget in self.tabla.winfo_children()[len(self.headers):]:
            widget.destroy()

        datos = self.controlador.obtener_insumos(self.id_usuario)

        if not datos:
            lbl = ctk.CTkLabel(self.tabla, text="No supplies registered")
            lbl.grid(row=1, column=0, columnspan=len(self.headers), pady=10)
            return

        for i, fila in enumerate(datos, start=1):
            frame_fila = ctk.CTkFrame(self.tabla, fg_color="transparent")
            frame_fila.grid(row=i, column=0, columnspan=len(self.headers), sticky="ew")
            frame_fila.bind("<Button-1>", lambda e, datos_fila=fila: self.seleccionar_fila(datos_fila, e.widget))
            
            for col, valor in enumerate(fila):
                lbl = ctk.CTkLabel(
                    frame_fila,
                    text=str(valor), 
                    font=("Poppins", 16),
                    width=100
                )
                lbl.grid(row=0, column=col, padx=10, pady=5)
                lbl.bind("<Button-1>", lambda e, datos_fila=fila, frame=frame_fila: self.seleccionar_fila(datos_fila, frame))

    def seleccionar_fila(self, datos, widget):
        """Selecciona una fila y la resalta"""
        if self.fila_seleccionada:
            self.fila_seleccionada.configure(fg_color="transparent")
        
        self.datos_seleccionados = datos
        
        if isinstance(widget, ctk.CTkFrame):
            self.fila_seleccionada = widget
        else:
            self.fila_seleccionada = widget.master
            
        self.fila_seleccionada.configure(fg_color="#D8B59D")
        print(f"Fila seleccionada: {datos}")

    def on_data_changed(self):
        self.fila_seleccionada = None
        self.datos_seleccionados = None
        self.actualizar_tabla()

    def agregar_registro_form(self, datos):
        self.controlador.agregar_insumo(
            datos["Supply Name"],
            datos["Unit"],
            datos["Quantity"],
            datos["Unit Cost"],
            datos["Provider"],
            datos["Description"],
            self.id_usuario
        )
        self.actualizar_tabla()

    def modificar_registro_form(self, datos):
        self.controlador.actualizar_insumo(
            datos["id"],
            datos["Supply Name"],
            datos["Unit"],
            datos["Quantity"],
            datos["Unit Cost"]
        )
        self.actualizar_tabla()

    def eliminar_registro_form(self, id_eliminar):
        self.controlador.eliminar_insumo(id_eliminar)
        self.actualizar_tabla()

    def ventana_modificar_registros(self, titulo_panel):
        if not self.datos_seleccionados:
            from tkinter import messagebox
            messagebox.showwarning("Warning", "Please select a row from the table first")
            return
        
        id_insumo, nombre, unidad, cantidad, costo = self.datos_seleccionados
        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title("Supplies - Modify Record")
        ventana.geometry("700x600")
        ventana.grab_set()

        frame = ctk.CTkScrollableFrame(
            ventana, fg_color="#FEF3E7", width=440, height=380, corner_radius=20
        )
        frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        lbl_id = ctk.CTkLabel(frame, text="Code", font=("Poppins", 16), text_color="#7A5230")
        lbl_id.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")
        
        entry_id = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_id.insert(0, str(id_insumo))
        entry_id.configure(state="disabled")
        entry_id.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        lbl_name = ctk.CTkLabel(frame, text="Supply Name", font=("Poppins", 16), text_color="#7A5230")
        lbl_name.grid(row=2, column=0, padx=20, pady=(10, 0), sticky="ew")
        
        entry_name = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_name.insert(0, str(nombre))
        entry_name.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")

        lbl_unit = ctk.CTkLabel(frame, text="Unit", font=("Poppins", 16), text_color="#7A5230")
        lbl_unit.grid(row=4, column=0, padx=20, pady=(10, 0), sticky="ew")
        
        option_unit = ctk.CTkOptionMenu(
            frame,
            values=["Unit", "Kilogram (kg)", "Gram (g)", "Liter (L)", "Milliliter (ml)", 
                    "Piece (pz)", "Package", "Box", "Bag"],
            width=260,
            corner_radius=10
        )
        option_unit.set(str(unidad) if unidad else "Unit")
        option_unit.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

        lbl_qty = ctk.CTkLabel(frame, text="Quantity", font=("Poppins", 16), text_color="#7A5230")
        lbl_qty.grid(row=6, column=0, padx=20, pady=(10, 0), sticky="ew")
        
        entry_qty = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_qty.insert(0, str(cantidad))
        entry_qty.grid(row=7, column=0, padx=20, pady=(0, 10), sticky="ew")

        lbl_cost = ctk.CTkLabel(frame, text="Unit Cost", font=("Poppins", 16), text_color="#7A5230")
        lbl_cost.grid(row=8, column=0, padx=20, pady=(10, 0), sticky="ew")
        
        entry_cost = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_cost.insert(0, str(costo))
        entry_cost.grid(row=9, column=0, padx=20, pady=(0, 10), sticky="ew")

        def modificar():
            try:
                self.controlador.actualizar_insumo(
                    id_insumo,
                    entry_name.get(),
                    option_unit.get(),
                    entry_qty.get(),
                    entry_cost.get()
                )
                self.on_data_changed()
                ventana.destroy()
            except Exception as e:
                from tkinter import messagebox
                messagebox.showerror("Error", f"Error modifying: {e}")

        btn_guardar = ctk.CTkButton(
            ventana,
            text="Save changes",
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230",
            command=modificar
        )
        btn_guardar.grid(row=2, column=0, pady=20)

    def ventana_eliminar_registros(self, titulo_panel):
        if not self.datos_seleccionados:
            from tkinter import messagebox
            messagebox.showwarning("Warning", "Please select a row from the table first")
            return
        
        id_insumo = self.datos_seleccionados[0]
        
        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title("Supplies - Delete Record")
        ventana.geometry("400x250")
        ventana.grab_set()

        lbl = ctk.CTkLabel(
            ventana, text="Code to delete:", font=("Poppins", 18), text_color="#7A5230"
        )
        lbl.pack(pady=20)

        entry_id = ctk.CTkEntry(ventana, width=200, corner_radius=10)
        entry_id.insert(0, str(id_insumo))
        entry_id.configure(state="disabled")
        entry_id.pack(pady=10)

        def eliminar():
            self.controlador.eliminar_insumo(id_insumo)
            self.on_data_changed()
            ventana.destroy()

        btn = ctk.CTkButton(
            ventana, text="Delete", fg_color="#F2A3A3",
            hover_color="#E57C7C", text_color="#7A5230",
            command=eliminar
        )
        btn.pack(pady=20)