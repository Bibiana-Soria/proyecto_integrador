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

            if nombre_campo.lower() == "tamano":
                widget = ctk.CTkOptionMenu(
                    frame_para_entries,
                    values=["pequeño", "grande"],
                    width=260,
                    corner_radius=10
                )
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

        lbl_id = ctk.CTkLabel(frame, text="ID", font=("Poppins", 16), text_color="#7A5230")
        lbl_id.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="w")

        entry_id = ctk.CTkEntry(frame, width=260, placeholder_text="Ingrese ID...", corner_radius=10)
        entry_id.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        info_obtenida["id"] = entry_id
        fila = 2
        for nombre_campo in self.campos:

            if nombre_campo.lower() == "id":
                continue

            lbl = ctk.CTkLabel(
                frame, text=nombre_campo, font=("Poppins", 16), text_color="#7A5230"
            )
            lbl.grid(row=fila, column=0, padx=20, pady=(10, 0), sticky="ew")

            if nombre_campo.lower() == "tamano":
                widget = ctk.CTkOptionMenu(
                    frame,
                    values=["Pequeño", "Grande"],
                    width=260,
                    corner_radius=10
                )
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

        lbl = ctk.CTkLabel(
            ventana, text="Ingrese el ID a eliminar", font=("Poppins", 18), text_color="#7A5230"
        )
        lbl.pack(pady=20)

        entry_id = ctk.CTkEntry(ventana, width=200, placeholder_text="ID...", corner_radius=10)
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
        if titulo_panel == "Productos":
            self.controlador.agregar_producto(
                datos.get("Nombre"),
                datos.get("Tamaño"),
                datos.get("Precio")
            )

    def enviar_datos_modificar(self, titulo_panel, datos):
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

    def enviar_datos_eliminar(self, titulo_panel, id_registro):
        if titulo_panel == "Productos":
            if not id_registro:
                messagebox.showerror("Error", "Debe ingresar el ID a eliminar")
                return
            self.controlador.eliminar_producto(id_registro)

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
