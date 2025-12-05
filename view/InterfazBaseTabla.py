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
            if titulo_panel == "Insumos":
                from controller.controlador_insumos import ControladorInsumos
                self.controlador = ControladorInsumos()
            elif titulo_panel == "Gastos":
                from controller.controlador_gastos import ControladorGastos
                self.controlador = ControladorGastos()
            elif titulo_panel == "Productos":
                # si tienes controlador de productos, importa aquí
                from controller.controlador_productos import ControladorProductos
                self.controlador = ControladorProductos()
            else:
                # por defecto, lo dejamos None para evitar llamadas accidentales
                self.controlador = None
        except Exception as e:
            # debug por si hay problemas con las rutas de import
            print("⚠️ Error al asignar controlador en HistorialBase:", e)
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

        if titulo_panel == "Historial de Ventas":
            text_up = "Panel Historial de Ventas"
            text_down = "Revisamos algo?"
            self.informacion_formularios = "de ventas"
        elif titulo_panel == "Gastos":
            text_up = "Panel Gastos"
            text_down = "Registramos algo?"
            self.informacion_formularios = "en gastos"
        elif titulo_panel == "Insumos":
            text_up = "Panel Insumos"
            text_down = "Registramos algo?"
            self.informacion_formularios = "en Insumos"
        elif titulo_panel == "Productos":
            text_up = "Panel Productos"
            text_down = "Registramos algo?"
            self.informacion_formularios = "en Productos"
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
            text= f"Agregar nuevo\nregistro {self.informacion_formularios}",
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
            text= f"Modificar\nregistro {self.informacion_formularios}",
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
            text= f"Eliminar\nregistro {self.informacion_formularios}",
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
        if titulo_panel == "Historial de Ventas":
            self.navegar("Nueva venta")
            return

        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title(f"{titulo_panel} - Agregar Registro")
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

            if nombre_campo.lower() in ["tamaño", "tamano"]:

                widget = ctk.CTkOptionMenu(
                    frame_para_entries,
                    values=["Pequeño", "Grande"],
                    width=260,
                    corner_radius=10
                )

                widget.set("Pequeño")  # valor por defecto

                widget.grid(row=i*2 + 1, column=0, padx=20, pady=(0, 10))
            elif nombre_campo.lower() in ["unidad", "unidad de medida", "unidad_medida"]:

                widget = ctk.CTkOptionMenu(
                    frame_para_entries,
                    values=[
                        "Unidad",
                        "Kilogramo (kg)",
                        "Gramo (g)",
                        "Litro (L)",
                        "Mililitro (ml)",
                        "Pieza (pz)",
                        "Paquete",
                        "Caja",
                        "Bolsa"
                    ],
                    width=260,
                    corner_radius=10
                )
                widget.set("Unidad")

                widget.grid(row=i*2 + 1, column=0, padx=20, pady=(0, 10))
            else:
                # Entry normal
                widget = ctk.CTkEntry(
                    frame_para_entries,
                    width=260,
                    placeholder_text=f"Ingrese {nombre_campo.lower()}...",
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
            text="Guardar",
            command=guardar,
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230"
        )
        btn_guardar.grid(row=2, column=0, pady=20)

    def ventana_modificar_registros(self, titulo_panel):
        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title(f"{titulo_panel} - Modificar Registro")
        ventana.geometry("700x700")
        ventana.grab_set()

        info_obtenida = {}

        frame = ctk.CTkScrollableFrame(
            ventana, fg_color="#FEF3E7", width=440, height=380, corner_radius=20
        )
        frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # 1. Título "ID" alineado a la DERECHA (anchor="e")
        lbl_id = ctk.CTkLabel(frame, text="Código", font=("Poppins", 16), text_color="#7A5230", anchor="w")
        lbl_id.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")

        entry_id = ctk.CTkEntry(frame, width=260, placeholder_text="Ingrese Código...", corner_radius=10)
        entry_id.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        info_obtenida["id"] = entry_id
        fila = 2
        
        for nombre_campo in self.campos:

            if nombre_campo.lower() == "id":
                continue

            # --- FILTRO ESPECÍFICO PARA VENTAS ---
            # Solo mostramos "Código de Producto" y "Cantidad"
            if titulo_panel == "Historial de Ventas":
                # Convertimos a minúsculas para comparar fácil
                txt = nombre_campo.lower()
                # Si NO es código de producto Y NO es cantidad, saltamos esta vuelta
                if "código de\nproducto" not in txt and "cantidad" not in txt:
                    continue

            # 2. Títulos de campos alineados a la DERECHA (anchor="e")
            lbl = ctk.CTkLabel(
                frame, text=nombre_campo, font=("Poppins", 16), text_color="#7A5230", anchor="w"
            )
            lbl.grid(row=fila, column=0, padx=20, pady=(10, 0), sticky="ew")

            if nombre_campo.lower() in ["tamaño", "tamano"]:
                widget = ctk.CTkOptionMenu(
                    frame, values=["Pequeño", "Grande"], width=260, corner_radius=10
                )
                widget.set("Pequeño")
                widget.grid(row=fila + 1, column=0, padx=20, pady=(0, 10), sticky="ew")

            elif nombre_campo.lower() in ["unidad", "unidad de medida", "unidad_medida"]:
                widget = ctk.CTkOptionMenu(
                    frame,
                    values=["Unidad", "Kilogramo (kg)", "Gramo (g)", "Litro (L)", "Pieza (pz)", "Paquete"],
                    width=260, corner_radius=10
                )
                widget.set("Unidad")
                widget.grid(row=fila + 1, column=0, padx=20, pady=(0, 10), sticky="ew")
            else:
                widget = ctk.CTkEntry(
                    frame,
                    width=260,
                    placeholder_text=f"Ingrese {nombre_campo.lower()}...",
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
            text="Guardar cambios",
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230",
            command=modificar
        )
        btn_guardar.grid(row=2, column=0, pady=20)

    def ventana_eliminar_registros(self, titulo_panel):

        ventana = ctk.CTkToplevel(fg_color="#FFF9F3")
        ventana.title(f"{titulo_panel} - Eliminar Registro")
        ventana.geometry("400x250")
        ventana.grab_set()

        # CAMBIO: Texto actualizado a "Código" para consistencia
        lbl = ctk.CTkLabel(
            ventana, text="Ingrese el Código a eliminar", font=("Poppins", 18), text_color="#7A5230"
        )
        lbl.pack(pady=20)

        entry_id = ctk.CTkEntry(ventana, width=200, placeholder_text="Código...", corner_radius=10)
        entry_id.pack(pady=10)

        def eliminar():
            self.enviar_datos_eliminar(titulo_panel, entry_id.get())

            try:
                self.on_data_changed()
            except Exception:
                pass

            ventana.destroy()

        btn = ctk.CTkButton(
            ventana, text="Eliminar", fg_color="#F2A3A3",
            hover_color="#E57C7C", text_color="#7A5230",
            command=eliminar
        )
        btn.pack(pady=20)

    def enviar_datos_al_controlador(self, titulo_panel, datos):
    # PRODUCTOS
        if titulo_panel == "Productos":
            self.controlador.agregar_producto(
                datos.get("Nombre"),
                datos.get("Tamaño"),
                datos.get("Precio")
            )

        # INSUMOS
        elif titulo_panel == "Insumos":
            # campos esperados por interfaz_de_insumos.form_campos
            nombre = datos.get("Nombre del insumo")
            unidad = datos.get("Unidad")
            cantidad = datos.get("Cantidad")
            costo = datos.get("Costo unitario")
            proveedor = datos.get("Proveedor")
            descripcion = datos.get("Descripción")

            # validación mínima
            if not nombre or not cantidad or not costo:
                messagebox.showerror("Error", "Nombre, cantidad y costo son requeridos")
                return

            # llamar al controlador (ControladorInsumos debe estar asignado en la vista hija)
            self.controlador.agregar_insumo(nombre, unidad, cantidad, costo, proveedor, descripcion)

        # GASTOS
        elif titulo_panel == "Gastos":

            codigo = datos.get("Codigo Insumo")

            # Si viene del OptionMenu tipo: "3 - Azúcar", dejamos solo el número
            if "-" in str(codigo):
                codigo = codigo.split(" - ")[0]

            proveedor = datos.get("Proveedor")
            descripcion = datos.get("Descripcion")

            try:
                monto = float(datos.get("Monto"))
                cantidad = float(datos.get("Cantidad Comprada"))
                codigo = int(codigo)   # ← IMPORTANTE
            except:
                messagebox.showerror("Error", "Código, Monto y Cantidad deben ser números válidos")
                return

            if not codigo or not monto or not cantidad:
                messagebox.showerror("Error", "Código, Monto y Cantidad son obligatorios")
                return

            self.controlador.agregar_gasto(
                codigo,
                proveedor,
                descripcion,
                monto,
                cantidad
            )


    def enviar_datos_modificar(self, titulo_panel, datos):
        # PRODUCTOS
        if titulo_panel == "Productos":
            if not datos.get("id"):
                messagebox.showerror("Error", "Debe ingresar un ID para modificar")
                return
            self.controlador.actualizar_producto(
                datos.get("id"),
                datos.get("Nombre"),
                datos.get("Tamaño"),
                datos.get("Precio")
            )

        # INSUMOS
        elif titulo_panel == "Insumos":
            if not datos.get("id"):
                messagebox.showerror("Error", "Debe ingresar un ID para modificar")
                return
            self.controlador.actualizar_insumo(
                datos.get("id"),
                datos.get("Nombre del insumo"),
                datos.get("Unidad"),
                datos.get("Cantidad"),
                datos.get("Costo unitario")
            )

        # GASTOS
        elif titulo_panel == "Gastos":
            if not datos.get("id"):
                messagebox.showerror("Error", "Debe ingresar un ID para modificar")
                return
            try:
                monto = float(datos.get("Monto"))
                cantidad = int(datos.get("Cantidad Comprada"))
            except:
                messagebox.showerror("Error", "Monto y Cantidad deben ser números")
                return
            self.controlador.actualizar_gasto(
                datos.get("id"),
                datos.get("Codigo Insumo"),
                datos.get("Proveedor"),
                datos.get("Descripcion"),
                monto,
                cantidad
            )

        # --- VENTAS (MODIFICADO) ---
        elif titulo_panel == "Historial de Ventas":
            id_venta = datos.get("id")
            if not id_venta:
                messagebox.showerror("Error", "Debe ingresar el ID de la venta")
                return

            try:
                # Solo tomamos ID PRODUCTO y CANTIDAD, el precio se buscará automático
                id_producto = datos.get("Código de\nProducto")
                cantidad = float(datos.get("Cantidad\n"))
                id_usuario = self.interface.usuario_logueado[0]

                # Llamamos al controlador SIN el precio (él lo buscará)
                self.controlador.actualizar_venta(
                    id_venta, 
                    id_usuario, 
                    id_producto, 
                    cantidad
                )
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número")
            except Exception as e:
                messagebox.showerror("Error", f"Error en datos: {e}")


    def enviar_datos_eliminar(self, titulo_panel, id_registro):
        # PRODUCTOS
        if titulo_panel == "Productos":
            if not id_registro:
                messagebox.showerror("Error", "Debe ingresar el ID a eliminar")
                return
            self.controlador.eliminar_producto(id_registro)

        # INSUMOS
        elif titulo_panel == "Insumos":
            if not id_registro:
                messagebox.showerror("Error", "Debe ingresar el ID a eliminar")
                return
            self.controlador.eliminar_insumo(id_registro)

        # GASTOS
        elif titulo_panel == "Gastos":
            if not id_registro:
                messagebox.showerror("Error", "Debe ingresar el ID a eliminar")
                return
            self.controlador.eliminar_gasto(id_registro)
            
        # --- NUEVO: HISTORIAL DE VENTAS ---
        elif titulo_panel == "Historial de Ventas":
            if not id_registro:
                messagebox.showerror("Error", "Debe ingresar el Código de la venta")
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
