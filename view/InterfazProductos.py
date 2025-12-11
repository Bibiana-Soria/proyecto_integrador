from view.InterfazBaseTabla import HistorialBase
import customtkinter as ctk
from tkinter import messagebox
from controller.controlador_productos import ControladorProductos

class interfaz_de_productos(HistorialBase):
    def __init__(self, interface, parent_navegar, ventana_principal):
        self.controlador = ControladorProductos()
        self.fila_seleccionada = None  
        self.datos_seleccionados = None 
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

        for i, fila in enumerate(datos, start=1):
            frame_fila = ctk.CTkFrame(self.tabla, fg_color="transparent")
            frame_fila.grid(row=i, column=0, columnspan=len(self.headers), sticky="ew")
            
            frame_fila.bind("<Button-1>", lambda e, datos_fila=fila: self.seleccionar_fila(datos_fila, e.widget))
            
            for col, valor in enumerate(fila):
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
        """Selecciona una fila y la resalta visualmente"""
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

    def agregar_producto(self, nombre, tamano, precio):
        self.controlador.agregar_producto(nombre, tamano, precio)
        self.actualizar_tabla()

    def actualizar_producto(self, id_producto, nombre, tamano, precio):
        self.controlador.actualizar_producto(id_producto, nombre, tamano, precio)
        self.actualizar_tabla()

    def eliminar_producto(self, id_producto):
        self.controlador.eliminar_producto(id_producto)
        self.actualizar_tabla()

    def ventana_modificar_registros(self, titulo_panel):
        """Abre ventana de modificar con datos precargados"""
        if not self.datos_seleccionados:
            from tkinter import messagebox
            messagebox.showwarning("Warning", "Please select a row from the table first")
            return
        
        id_producto, nombre, tamano, precio = self.datos_seleccionados
        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title("Products - Modify Record")
        ventana.geometry("700x600")
        ventana.grab_set()

        frame = ctk.CTkScrollableFrame(
            ventana, fg_color="#FEF3E7", width=440, height=380, corner_radius=20
        )
        frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        ctk.CTkLabel(frame, text="Code", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_id = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_id.insert(0, str(id_producto))
        entry_id.configure(state="disabled")
        entry_id.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(frame, text="Name", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=2, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_name = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_name.insert(0, str(nombre))
        entry_name.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(frame, text="Size", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=4, column=0, padx=20, pady=(10, 0), sticky="ew")
        option_size = ctk.CTkOptionMenu(
            frame,
            values=["Small", "Large"],
            width=260,
            corner_radius=10
        )
        option_size.set(str(tamano) if tamano else "Small")
        option_size.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(frame, text="Price", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=6, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_price = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_price.insert(0, str(precio))
        entry_price.grid(row=7, column=0, padx=20, pady=(0, 10), sticky="ew")

        def modificar():
            try:
                nombre_val = entry_name.get().strip()
                tamano_val = option_size.get()
                precio_raw = entry_price.get().strip()
                
                if not nombre_val:
                    from tkinter import messagebox
                    messagebox.showerror("Error", "Name cannot be empty")
                    return
                
                if not precio_raw:
                    from tkinter import messagebox
                    messagebox.showerror("Error", "Price cannot be empty")
                    return
                
                try:
                    if hasattr(precio_raw, 'quantize'):  
                        precio_val = float(precio_raw)
                    else:
                        precio_val = float(str(precio_raw).replace(',', '.'))
                    print(f"Precio convertido: {precio_val}")
                except (ValueError, AttributeError) as e:
                    from tkinter import messagebox
                    messagebox.showerror("Error", f"Invalid price format: '{precio_raw}'")
                
                resultado = self.controlador.actualizar_producto(
                    id_producto,
                    nombre_val,
                    tamano_val,
                    precio_val
                )
                
                print(f"Resultado del controlador: {resultado}")
                
                if resultado:
                    print("Actualización exitosa, cerrando ventana...")
                    self.on_data_changed()
                    ventana.destroy()
                else:
                    messagebox.showerror("Error", "Failed to update product in database. Check console for details.")
                
            except ValueError as ve:
                from tkinter import messagebox
                messagebox.showerror("Error", f"Value error: {ve}")
                print(f"ValueError completo:")
                import traceback
                traceback.print_exc()
                
            except Exception as e:
                from tkinter import messagebox
                messagebox.showerror("Error", f"Unexpected error: {e}")
                print(f"ERROR COMPLETO:")
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
        """Abre ventana de eliminar con ID precargado"""
        if not self.datos_seleccionados:
            from tkinter import messagebox
            messagebox.showwarning("Warning", "Please select a row from the table first")
            return
        
        id_producto = self.datos_seleccionados[0]
        
        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title("Products - Delete Record")
        ventana.geometry("400x250")
        ventana.grab_set()

        ctk.CTkLabel(
            ventana, text="Code to delete:", font=("Poppins", 18), text_color="#7A5230"
        ).pack(pady=20)

        entry_id = ctk.CTkEntry(ventana, width=200, corner_radius=10)
        entry_id.insert(0, str(id_producto))
        entry_id.configure(state="disabled")
        entry_id.pack(pady=10)

        def eliminar():
            self.controlador.eliminar_producto(id_producto)
            self.on_data_changed()
            ventana.destroy()

        ctk.CTkButton(
            ventana, text="Delete", fg_color="#F2A3A3",
            hover_color="#E57C7C", text_color="#7A5230",
            command=eliminar
        ).pack(pady=20)