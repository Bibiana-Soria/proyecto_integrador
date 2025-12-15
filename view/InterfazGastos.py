from view.InterfazBaseTabla import HistorialBase
import customtkinter as ctk
from controller.controlador_gastos import ControladorGastos

class interfaz_de_gastos(HistorialBase):
    def __init__(self, interface, parent_navegar, ventana_principal, id_usuario):
        self.controlador = ControladorGastos()
        self.id_usuario = id_usuario
        self.fila_seleccionada = None
        self.datos_seleccionados = None
        self.headers = ["Code", "Supply Code", "Provider", "Description", "Amount", "Quantity", "Date"]
        self.form_campos = ["Supply Code", "Provider", "Description", "Amount", "Quantity Purchased"]

        super().__init__(
            interface, 
            parent_navegar, 
            ventana_principal,
            self.form_campos, 
            titulo_panel="Expenses"
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
        for widget in list(self.tabla.winfo_children())[len(self.headers):]:
            widget.destroy()

        datos = self.controlador.obtener_todos_los_gastos(self.id_usuario)

        if not datos:
            lbl_vacio = ctk.CTkLabel(self.tabla, text="No expenses registered", font=("Poppins", 16), text_color="#7A5230")
            lbl_vacio.grid(row=1, column=0, columnspan=len(self.headers), pady=20)
            return

        for i, fila in enumerate(datos, start=1):
            frame_fila = ctk.CTkFrame(self.tabla, fg_color="transparent")
            frame_fila.grid(row=i, column=0, columnspan=len(self.headers), sticky="ew")
            
            frame_fila.bind("<Button-1>", lambda e, datos_fila=fila: self.seleccionar_fila(datos_fila, e.widget))
            
            fila_visual = (fila[0], fila[1], fila[3], fila[4], fila[5], fila[6], fila[7])
            
            for col, valor in enumerate(fila_visual):
                lbl = ctk.CTkLabel(
                    frame_fila, 
                    text=str(valor),
                    font=("Poppins", 16),
                    text_color="#7A5230",
                    width=100
                )
                lbl.grid(row=0, column=col, padx=15, pady=5)
                lbl.bind("<Button-1>", lambda e, datos_fila=fila, frame=frame_fila: self.seleccionar_fila(datos_fila, frame))
    
    def seleccionar_fila(self, datos, widget):
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

    def agregar_gasto(self, id_insumo, proveedor, descripcion, monto, cantidad):
        self.controlador.agregar_gasto(id_insumo, proveedor, descripcion, monto, cantidad, self.id_usuario)
        self.actualizar_tabla()

    def actualizar_gasto(self, id_egreso, id_insumo, proveedor, descripcion, monto, cantidad):
        self.controlador.actualizar_gasto(id_egreso, id_insumo, proveedor, descripcion, monto, cantidad)
        self.actualizar_tabla()

    def eliminar_gasto(self, id_egreso):
        self.controlador.eliminar_gasto(id_egreso)
        self.actualizar_tabla()
    
    def ventana_modificar_registros(self, titulo_panel):
        if not self.datos_seleccionados:
            from tkinter import messagebox
            messagebox.showwarning("Warning", "Please select a row from the table first")
            return

        id_egreso, id_insumo, id_usuario, proveedor, descripcion, monto, cantidad, fecha = self.datos_seleccionados
        
        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title("Expenses - Modify Record")
        ventana.geometry("700x700")
        ventana.grab_set()

        frame = ctk.CTkScrollableFrame(
            ventana, fg_color="#FEF3E7", width=440, height=380, corner_radius=20
        )
        frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        ctk.CTkLabel(frame, text="Code", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_id = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_id.insert(0, str(id_egreso))
        entry_id.configure(state="disabled")
        entry_id.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(frame, text="Supply Code", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=2, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_supply = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_supply.insert(0, str(id_insumo) if id_insumo else "")
        entry_supply.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(frame, text="Provider", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=4, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_prov = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_prov.insert(0, str(proveedor) if proveedor else "")
        entry_prov.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(frame, text="Description", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=6, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_desc = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_desc.insert(0, str(descripcion) if descripcion else "")
        entry_desc.grid(row=7, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(frame, text="Amount", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=8, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_amount = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_amount.insert(0, str(monto))
        entry_amount.grid(row=9, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(frame, text="Quantity", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=10, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_qty = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_qty.insert(0, str(cantidad))
        entry_qty.grid(row=11, column=0, padx=20, pady=(0, 10), sticky="ew")

        def modificar():
            try:
                supply_val = entry_supply.get().strip()
                prov_val = entry_prov.get().strip()
                desc_val = entry_desc.get().strip()
                amount_val = entry_amount.get().strip()
                qty_val = entry_qty.get().strip()
                
                if not amount_val or not qty_val:
                    from tkinter import messagebox
                    messagebox.showerror("Error", "Amount and Quantity cannot be empty")
                    return
                
                try:
                    amount_val_clean = amount_val.replace(',', '.')
                    monto_val = float(amount_val_clean)
                    print(f"  Amount convertido: {monto_val}")
                except ValueError as e:
                    from tkinter import messagebox
                    messagebox.showerror("Error", f"Invalid Amount format: '{amount_val}'\nMust be a number (e.g., 150.50)")
                    return
                
                try:
                    cantidad_val = int(float(qty_val))
                    print(f"  Quantity convertido: {cantidad_val}")
                except ValueError as e:
                    from tkinter import messagebox
                    messagebox.showerror("Error", f"Invalid Quantity format: '{qty_val}'\nMust be a whole number (e.g., 10)")
                    return
                
                if supply_val:
                    try:
                        id_insumo_mod = int(supply_val)
                    except ValueError:
                        from tkinter import messagebox
                        messagebox.showerror("Error", f"Supply Code must be a number, got: '{supply_val}'")
                        return
                else:
                    id_insumo_mod = None
                resultado = self.controlador.actualizar_gasto(
                    id_egreso,
                    id_insumo_mod,
                    prov_val,
                    desc_val,
                    monto_val,
                    cantidad_val
                )
                
                self.on_data_changed()
                ventana.destroy()
                
            except Exception as e:
                from tkinter import messagebox
                messagebox.showerror("Error", f"Unexpected error: {e}")
                print(f"DEBUG - Error completo:")
                import traceback
                traceback.print_exc()

        ctk.CTkButton(
            ventana,
            text="Save changes",
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230",
            command=modificar
        ).grid(row=2, column=0, pady=20)

    def ventana_eliminar_registros(self, titulo_panel):
        if not self.datos_seleccionados:
            from tkinter import messagebox
            messagebox.showwarning("Warning", "Please select a row from the table first")
            return
        
        id_egreso = self.datos_seleccionados[0]
        
        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title("Expenses - Delete Record")
        ventana.geometry("400x250")
        ventana.grab_set()

        ctk.CTkLabel(ventana, text="Code to delete:", font=("Poppins", 18), text_color="#7A5230").pack(pady=20)

        entry_id = ctk.CTkEntry(ventana, width=200, corner_radius=10)
        entry_id.insert(0, str(id_egreso))
        entry_id.configure(state="disabled")
        entry_id.pack(pady=10)

        def eliminar():
            self.controlador.eliminar_gasto(id_egreso)
            self.on_data_changed()
            ventana.destroy()

        ctk.CTkButton(
            ventana, text="Delete", fg_color="#F2A3A3",
            hover_color="#E57C7C", text_color="#7A5230",
            command=eliminar
        ).pack(pady=20)