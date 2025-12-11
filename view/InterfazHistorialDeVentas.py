from tkinter import messagebox
from view.InterfazBaseTabla import HistorialBase
import customtkinter as ctk
from controller.controlador_historial_ventas import ControladorHistorialVentas

class Historial_de_ventas(HistorialBase):
    def __init__(self, interface, parent_navegar, ventana_principal):
        self.fila_seleccionada = None
        self.datos_seleccionados = None
        
        self.headers = ["Code", "Product\nCode", "Date", "Quantity", "Price", "Total"]
        self.form_campos = ["Product\nCode", "Quantity"]
        super().__init__(interface, parent_navegar, ventana_principal, self.form_campos, titulo_panel="Sales History")
        self.controlador = ControladorHistorialVentas()
        
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
            lbl = ctk.CTkLabel(self.tabla, text=text,
                               font=("Mochiy Pop One", 20),
                               text_color="#7A5230")
            lbl.grid(row=0, column=col, padx=15, pady=10)

        id_usuario_actual = self.interface.usuario_logueado[0]
        datos = self.controlador.obtener_todas_las_ventas(id_usuario_actual)

        if not datos:
            lbl_vacio = ctk.CTkLabel(self.tabla, text="No sales registered", 
                                     font=("Poppins", 16), text_color="#7A5230")
            lbl_vacio.grid(row=1, column=0, columnspan=len(self.headers), pady=20)
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
        """Selecciona una fila y la resalta"""
        if self.fila_seleccionada:
            self.fila_seleccionada.configure(fg_color="transparent")
        
        self.datos_seleccionados = datos
        
        if isinstance(widget, ctk.CTkFrame):
            self.fila_seleccionada = widget
        else:
            self.fila_seleccionada = widget.master
            
        self.fila_seleccionada.configure(fg_color="#D8B59D")
    
    def on_data_changed(self):
        self.fila_seleccionada = None
        self.datos_seleccionados = None
        self.crear_tabla_ventas()

    def ventana_modificar_registros(self, titulo_panel):
        """Abre ventana de modificar con datos precargados"""
        if not self.datos_seleccionados:
            messagebox.showwarning("Warning", "Please select a row from the table first")
            return
        id_venta, id_producto, fecha, cantidad, precio_unitario, total = self.datos_seleccionados
        
        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title("Sales History - Modify Record")
        ventana.geometry("700x500")
        ventana.grab_set()

        frame = ctk.CTkScrollableFrame(
            ventana, fg_color="#FEF3E7", width=440, height=380, corner_radius=20
        )
        frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        ctk.CTkLabel(frame, text="Sale Code", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_id = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_id.insert(0, str(id_venta))
        entry_id.configure(state="disabled")
        entry_id.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        # Product Code
        ctk.CTkLabel(frame, text="Product Code", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=2, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_producto = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_producto.insert(0, str(id_producto))
        entry_producto.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")

        ctk.CTkLabel(frame, text="Quantity", font=("Poppins", 16), text_color="#7A5230", anchor="w").grid(row=4, column=0, padx=20, pady=(10, 0), sticky="ew")
        entry_cantidad = ctk.CTkEntry(frame, width=260, corner_radius=10)
        entry_cantidad.insert(0, str(cantidad))
        entry_cantidad.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

        def modificar():
            try:
                id_usuario = self.interface.usuario_logueado[0]
                id_producto_val = int(entry_producto.get())
                cantidad_val = float(entry_cantidad.get())
                
                self.controlador.actualizar_venta(
                    id_venta,
                    id_usuario,
                    id_producto_val,
                    cantidad_val
                )
                
                self.on_data_changed()
                ventana.destroy()
                
            except ValueError:
                messagebox.showerror("Error", "Product Code and Quantity must be valid numbers")
            except Exception as e:
                messagebox.showerror("Error", f"Error: {e}")

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
            messagebox.showwarning("Warning", "Please select a row from the table first")
            return
        
        id_venta = self.datos_seleccionados[0]
        
        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title("Sales History - Delete Record")
        ventana.geometry("400x250")
        ventana.grab_set()

        ctk.CTkLabel(
            ventana, text="Sale Code to delete:", font=("Poppins", 18), text_color="#7A5230"
        ).pack(pady=20)

        entry_id = ctk.CTkEntry(ventana, width=200, corner_radius=10)
        entry_id.insert(0, str(id_venta))
        entry_id.configure(state="disabled")
        entry_id.pack(pady=10)

        def eliminar():
            if messagebox.askyesno("Confirm", "Are you sure you want to delete this sale?"):
                try:
                    self.controlador.eliminar_venta(id_venta)
                    self.on_data_changed()
                    ventana.destroy()
                except Exception as e:
                    messagebox.showerror("Error", f"Error deleting sale: {e}")

        ctk.CTkButton(
            ventana, text="Delete", fg_color="#F2A3A3",
            hover_color="#E57C7C", text_color="#7A5230",
            command=eliminar
        ).pack(pady=20)