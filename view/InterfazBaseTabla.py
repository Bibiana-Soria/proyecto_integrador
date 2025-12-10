import customtkinter as ctk
import os
from PIL import Image
from tkinter import messagebox

class HistorialBase(ctk.CTkFrame):
    def __init__(self, interface, parent_navegar, ventana_principal, campos, titulo_panel):
        super().__init__(interface, fg_color="#FFF9F3")
        self.interface = interface
        self.parent_navegar = parent_navegar
        self.app = ventana_principal
        self.campos = campos
        try:
            if titulo_panel == "Supplies":
                from controller.controlador_insumos import ControladorInsumos
                self.controlador = ControladorInsumos()
            elif titulo_panel == "Expenses":
                from controller.controlador_gastos import ControladorGastos
                self.controlador = ControladorGastos()
            elif titulo_panel == "Products":
                from controller.controlador_productos import ControladorProductos
                self.controlador = ControladorProductos()
            else:
                self.controlador = None
        except Exception as e:
            print("Error assigning controller in HistorialBase:", e)
            self.controlador = None
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.informacion_obtenida = {}

        self.configurar_grid_principal()
        self.crear_parte_superior(titulo_panel)
        self.contenido = ctk.CTkFrame(self, fg_color="#FFF9F3")
        self.contenido.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=40, pady=(10,40))
        self.contenido.grid_columnconfigure(0, weight=1)
        self.contenido.grid_rowconfigure(0, weight=1)

    def configurar_grid_principal(self):
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=8) 
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def crear_parte_superior(self, titulo_panel):
        frame_sup = ctk.CTkFrame(self, fg_color="#FEF3E7")
        frame_sup.grid(row=0, column=0, columnspan=2, sticky="nsew")
        frame_sup.grid_propagate(False)
        frame_sup.grid_columnconfigure((0,1,2,3,4), weight=1)
        frame_sup.grid_rowconfigure(0, weight=1)
        try:
            logo_path = os.path.join(self.base_path, "images", "Logo.png")
            img = Image.open(logo_path)
            logo_img = ctk.CTkImage(light_image=img, dark_image=img, size=(200, 200))
            logo_btn = ctk.CTkButton(
                frame_sup, text="", image=logo_img,
                fg_color="transparent", hover_color="#FEF3E7",
                command=lambda: self.crear_sidebar()
            )
            logo_btn.image = logo_img
            logo_btn.grid(row=0, column=0, pady=10, sticky="w")
        except Exception:
            pass

        lbl_panel = ctk.CTkLabel(
            self,
            text=titulo_panel,
            font=("Mochiy Pop One", 24, "bold"),
            text_color="#7A5230"
        )
        lbl_panel.grid(
            row=1,
            column=0,
            sticky="wns",
            padx=(120, 0),
            pady = (20,20)
        )

        if titulo_panel == "Sales History":
            text_up = "Sales History Panel"
            text_down = "Checking something?"
            self.informacion_formularios = "sales"
        elif titulo_panel == "Expenses":
            text_up = "Expenses Panel"
            text_down = "Registering something?"
            self.informacion_formularios = "expenses"
        elif titulo_panel == "Supplies":
            text_up = "Supplies Panel"
            text_down = "Registering something?"
            self.informacion_formularios = "supplies"
        elif titulo_panel == "Products":
            text_up = "Products Panel"
            text_down = "Registering something?"
            self.informacion_formularios = "products"
        else:
            text_up = titulo_panel
            text_down = ""
            self.informacion_formularios = ""

        frame_bienvenida_e_info = ctk.CTkFrame(frame_sup, fg_color="transparent")
        frame_bienvenida_e_info.grid(row=0, column=1, sticky="w")
        lbl_up = ctk.CTkLabel(frame_bienvenida_e_info, text=text_up, font=("Poppins", 20), text_color="#C49A85")
        lbl_up.grid(row = 0, column = 0, sticky = "sw")
        lbl_down = ctk.CTkLabel(frame_bienvenida_e_info, text=text_down, font=("Mochiy Pop One", 32),
                                text_color="#7A5230", justify = "left")
        lbl_down.grid(row=1, column=0, sticky="nw")

        boton_agregar_registros = ctk.CTkButton(
            frame_sup,
            text= f"Add new\n{self.informacion_formularios} record",
            font=("Mochiy Pop One", 25),
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230",
            corner_radius=15,
            border_width=3,
            border_color="#D8B59D",
            command=lambda: self.ventana_agregar_registro(titulo_panel)
        )
        boton_agregar_registros.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

        boton_modificar_registros = ctk.CTkButton(
            frame_sup,
            text= f"Modify\n{self.informacion_formularios} record",
            font=("Mochiy Pop One", 25),
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230",
            corner_radius=15,
            border_width=3,
            border_color="#D8B59D",
            command=lambda: self.ventana_modificar_registros(titulo_panel)
        )
        boton_modificar_registros.grid(row=0, column=3, padx=20, pady=20, sticky="nsew")

        boton_eliminar_registros = ctk.CTkButton(
            frame_sup,
            text= f"Delete\n{self.informacion_formularios} record",
            font=("Mochiy Pop One", 25),
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230",
            corner_radius=15,
            border_width=3,
            border_color="#D8B59D",
            command=lambda: self.ventana_eliminar_registros(titulo_panel)
        )
        boton_eliminar_registros.grid(row=0, column=4, padx=20, pady=20, sticky="nsew")

    def ventana_agregar_registro(self, titulo_panel):
        if titulo_panel == "Sales History":
            self.navegar("New Sale")
            return

        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title(f"{titulo_panel} - Add Record")
        ventana.geometry("700x700")
        ventana.grab_set()

        info_obtenida = {}

        frame_para_entries = ctk.CTkScrollableFrame(
            ventana, fg_color="#FEF3E7", corner_radius=20, width=440, height=280
        )
        frame_para_entries.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        for i, nombre_campo in enumerate(self.campos):

            if nombre_campo.lower() == "id":
                continue

            # Etiqueta
            lbl = ctk.CTkLabel(
                frame_para_entries,
                text=nombre_campo,
                font=("Poppins", 16),
                text_color="#7A5230",
                anchor="w"
            )
            lbl.grid(row=i*2, column=0, padx=20, pady=(10, 0), sticky="ew")

            if nombre_campo.lower() in ["size", "tamaño", "tamano"]:

                widget = ctk.CTkOptionMenu(
                    frame_para_entries,
                    values=["Small", "Large"],
                    width=260,
                    corner_radius=10
                )

                widget.set("Small")  # valor por defecto

                widget.grid(row=i*2 + 1, column=0, padx=20, pady=(0, 10))
            elif nombre_campo.lower() in ["unit", "unidad", "unidad de medida", "unidad_medida"]:

                widget = ctk.CTkOptionMenu(
                    frame_para_entries,
                    values=[
                        "Unit",
                        "Kilogram (kg)",
                        "Gram (g)",
                        "Liter (L)",
                        "Milliliter (ml)",
                        "Piece (pz)",
                        "Package",
                        "Box",
                        "Bag"
                    ],
                    width=260,
                    corner_radius=10
                )
                widget.set("Unit")

                widget.grid(row=i*2 + 1, column=0, padx=20, pady=(0, 10))
            else:
                # Entry normal
                widget = ctk.CTkEntry(
                    frame_para_entries,
                    width=260,
                    placeholder_text=f"Enter {nombre_campo.lower()}...",
                    corner_radius=10
                )
                widget.grid(row=i*2 + 1, column=0, padx=20, pady=(0, 10), sticky="ew")

            info_obtenida[nombre_campo] = widget

        def guardar():
            datos = {}
            for campo, widget in info_obtenida.items():
                try:
                    datos[campo] = widget.get()
                except Exception:
                    datos[campo] = ""
            self.enviar_datos_al_controlador(titulo_panel, datos)
            try:
                self.on_data_changed()
            except Exception:
                pass

            ventana.destroy()

        btn_guardar = ctk.CTkButton(
            ventana,
            text="Save",
            command=guardar,
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230"
        )
        btn_guardar.grid(row=2, column=0, pady=20)

    def ventana_modificar_registros(self, titulo_panel):
        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title(f"{titulo_panel} - Modify Record")
        ventana.geometry("700x700")
        ventana.grab_set()

        info_obtenida = {}

        frame = ctk.CTkScrollableFrame(
            ventana, fg_color="#FEF3E7", width=440, height=380, corner_radius=20
        )
        frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        lbl_id = ctk.CTkLabel(frame, text="Code", font=("Poppins", 16), text_color="#7A5230", anchor="w")
        lbl_id.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")

        entry_id = ctk.CTkEntry(frame, width=260, placeholder_text="Enter Code...", corner_radius=10)
        entry_id.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        info_obtenida["id"] = entry_id
        fila = 2
        
        for nombre_campo in self.campos:

            if nombre_campo.lower() == "id":
                continue

            if titulo_panel == "Sales History":
                txt = nombre_campo.lower()
                if "product date" not in txt and "quantity" not in txt and "product\ncode" not in txt: 
                     if "product\ncode" not in txt and "quantity" not in txt:
                        continue

            lbl = ctk.CTkLabel(
                frame, text=nombre_campo, font=("Poppins", 16), text_color="#7A5230", anchor="w"
            )
            lbl.grid(row=fila, column=0, padx=20, pady=(10, 0), sticky="ew")

            if nombre_campo.lower() in ["size", "tamaño", "tamano"]:
                widget = ctk.CTkOptionMenu(
                    frame, values=["Small", "Large"], width=260, corner_radius=10
                )
                widget.set("Small")
                widget.grid(row=fila + 1, column=0, padx=20, pady=(0, 10), sticky="ew")

            elif nombre_campo.lower() in ["unit", "unidad", "unidad de medida", "unidad_medida"]:
                widget = ctk.CTkOptionMenu(
                    frame,
                    values=["Unit", "Kilogram (kg)", "Gram (g)", "Liter (L)", "Piece (pz)", "Package"],
                    width=260, corner_radius=10
                )
                widget.set("Unit")
                widget.grid(row=fila + 1, column=0, padx=20, pady=(0, 10), sticky="ew")
            else:
                widget = ctk.CTkEntry(
                    frame,
                    width=260,
                    placeholder_text=f"Enter {nombre_campo.lower()}...",
                    corner_radius=10,
                )
                widget.grid(row=fila + 1, column=0, padx=20, pady=(0, 10), sticky="ew")

            info_obtenida[nombre_campo] = widget
            fila += 2

        def modificar():
            datos = {campo: widget.get() for campo, widget in info_obtenida.items()}
            self.enviar_datos_modificar(titulo_panel, datos)

            try:
                self.on_data_changed()
            except Exception:
                pass

            ventana.destroy()

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

        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title(f"{titulo_panel} - Delete Record")
        ventana.geometry("400x250")
        ventana.grab_set()

        lbl = ctk.CTkLabel(
            ventana, text="Enter Code to delete", font=("Poppins", 18), text_color="#7A5230"
        )
        lbl.pack(pady=20)

        entry_id = ctk.CTkEntry(ventana, width=200, placeholder_text="Code...", corner_radius=10)
        entry_id.pack(pady=10)

        def eliminar():
            self.enviar_datos_eliminar(titulo_panel, entry_id.get())

            try:
                self.on_data_changed()
            except Exception:
                pass

            ventana.destroy()

        btn = ctk.CTkButton(
            ventana, text="Delete", fg_color="#F2A3A3",
            hover_color="#E57C7C", text_color="#7A5230",
            command=eliminar
        )
        btn.pack(pady=20)

    def enviar_datos_al_controlador(self, titulo_panel, datos):
        # PRODUCTOS
        if titulo_panel == "Products":
            self.controlador.agregar_producto(
                datos.get("Name"),
                datos.get("Size"),
                datos.get("Price")
            )

        # INSUMOS
        elif titulo_panel == "Supplies":
            # campos esperados por interfaz_de_insumos.form_campos
            nombre = datos.get("Supply Name")
            unidad = datos.get("Unit")
            cantidad = datos.get("Quantity")
            costo = datos.get("Unit Cost")
            proveedor = datos.get("Provider")
            descripcion = datos.get("Description")

            if not nombre or not cantidad or not costo:
                messagebox.showerror("Error", "Name, quantity and cost are required")
                return

            self.controlador.agregar_insumo(nombre, unidad, cantidad, costo, proveedor, descripcion, self.interface.id_usuario)

        # GASTOS
        elif titulo_panel == "Expenses":

            codigo = datos.get("Supply Code")

            if "-" in str(codigo):
                codigo = codigo.split(" - ")[0]

            proveedor = datos.get("Provider")
            descripcion = datos.get("Description")

            try:
                monto = float(datos.get("Amount"))
                cantidad = float(datos.get("Quantity Purchased"))
                codigo = int(codigo)
            except:
                messagebox.showerror("Error", "Code, Amount and Quantity must be valid numbers")
                return

            if not codigo or not monto or not cantidad:
                messagebox.showerror("Error", "Code, Amount and Quantity are required")
                return

            self.controlador.agregar_gasto(
                codigo,
                proveedor,
                descripcion,
                monto,
                cantidad,
                self.interface.id_usuario
            )

    def enviar_datos_modificar(self, titulo_panel, datos):
        # PRODUCTOS
        if titulo_panel == "Products":
            if not datos.get("id"):
                messagebox.showerror("Error", "Must enter an ID to modify")
                return
            self.controlador.actualizar_producto(
                datos.get("id"),
                datos.get("Name"),
                datos.get("Size"),
                datos.get("Price")
            )

        # INSUMOS
        elif titulo_panel == "Supplies":
            if not datos.get("id"):
                messagebox.showerror("Error", "Must enter an ID to modify")
                return
            self.controlador.actualizar_insumo(
                datos.get("id"),
                datos.get("Supply Name"),
                datos.get("Unit"),
                datos.get("Quantity"),
                datos.get("Unit Cost")
            )

        # GASTOS
        elif titulo_panel == "Expenses":
            if not datos.get("id"):
                messagebox.showerror("Error", "Must enter an ID to modify")
                return
            try:
                monto = float(datos.get("Amount"))
                cantidad = int(datos.get("Quantity Purchased"))
            except:
                messagebox.showerror("Error", "Amount and Quantity must be numbers")
                return
            self.controlador.actualizar_gasto(
                datos.get("id"),
                datos.get("Supply Code"),
                datos.get("Provider"),
                datos.get("Description"),
                monto,
                cantidad
            )

        # VENTAS
        elif titulo_panel == "Sales History":
            id_venta = datos.get("id")
            if not id_venta:
                messagebox.showerror("Error", "Must enter Sale ID")
                return

            try:
                id_producto = datos.get("Product\nCode")
                cantidad = float(datos.get("Quantity\n"))
                id_usuario = self.interface.usuario_logueado[0]

                self.controlador.actualizar_venta(
                    id_venta, 
                    id_usuario, 
                    id_producto, 
                    cantidad
                )
            except ValueError:
                messagebox.showerror("Error", "Quantity must be a number")
            except Exception as e:
                messagebox.showerror("Error", f"Error in data: {e}")

    def enviar_datos_eliminar(self, titulo_panel, id_registro):
        # PRODUCTOS
        if titulo_panel == "Products":
            if not id_registro:
                messagebox.showerror("Error", "Must enter ID to delete")
                return
            self.controlador.eliminar_producto(id_registro)

        # INSUMOS
        elif titulo_panel == "Supplies":
            if not id_registro:
                messagebox.showerror("Error", "Must enter ID to delete")
                return
            self.controlador.eliminar_insumo(id_registro)

        # GASTOS
        elif titulo_panel == "Expenses":
            if not id_registro:
                messagebox.showerror("Error", "Must enter ID to delete")
                return
            self.controlador.eliminar_gasto(id_registro)
            
        # HISTORIAL DE VENTAS
        elif titulo_panel == "Sales History":
            if not id_registro:
                messagebox.showerror("Error", "Must enter Sale Code")
                return
            self.controlador.eliminar_venta(id_registro)

    def crear_sidebar(self):
        from view.SideBar import Sidebar
        self.sidebar = Sidebar(self, on_nav=self.navegar)
        self.sidebar.place(x=0, y=0, relheight=1)
        self.bind("<Button-1>", self._click_fuera_sidebar)

    def navegar(self, destino: str):
        self.parent_navegar(destino)

    def _click_fuera_sidebar(self, event):
        SIDEBAR_WIDTH = 260
        if event.x > SIDEBAR_WIDTH:
            self.cerrar_sidebar()

    def cerrar_sidebar(self):
        self.sidebar.destroy()
        del self.sidebar
        self.unbind("<Button-1>")
