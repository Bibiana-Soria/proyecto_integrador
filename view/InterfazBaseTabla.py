# view/historial_base.py
import customtkinter as ctk
import os
from PIL import Image

class HistorialBase(ctk.CTkFrame):
    def __init__(self, interface, parent_navegar, ventana_principal ,campos,titulo_panel,):
        super().__init__(interface, fg_color="#FFF9F3")
        self.interface = interface
        self.parent_navegar = parent_navegar
        self.app = ventana_principal
        self.campos = campos
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.informacion_obtenida = {}

        self.configurar_grid_principal()
        self.crear_parte_superior(titulo_panel)

        # Frame donde cada hijo pondrá su tabla
        self.contenido = ctk.CTkFrame(self, fg_color="#FFF9F3")
        self.contenido.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=40, pady=(10,40))
        self.contenido.grid_columnconfigure(0, weight=1)
        self.contenido.grid_rowconfigure(0, weight=1)

    def configurar_grid_principal(self):
        self.grid_rowconfigure(0, weight=0)   # Parte superior
        self.grid_rowconfigure(1, weight=0)   # Título
        self.grid_rowconfigure(2, weight=8)   # Tabla
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def crear_parte_superior(self, titulo_panel):
        frame_sup = ctk.CTkFrame(self, fg_color="#FEF3E7")
        frame_sup.grid(row=0, column=0, columnspan=2, sticky="nsew")
        frame_sup.grid_propagate(False)
        frame_sup.grid_columnconfigure((0,1,2,3,4), weight=1)
        frame_sup.grid_rowconfigure(0, weight=1)

        # logo
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

        # título
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
        # Bienvenida e informacion sobre interfaz
        if titulo_panel == "Historial de Ventas":
            text_up = "Panel Historial de Ventas"
            text_down = "Revisamos algo\nGus?"
            self.informacion_formularios = "de ventas"
        elif titulo_panel == "Gastos":
            text_up = "Panel Gastos"
            text_down = "Registramos algo\nGus?"
            self.informacion_formularios = "en gastos"
        elif titulo_panel == "Insumos":
            text_up = "Panel Insumos"
            text_down = "Registramos algo\nGus?"
            self.informacion_formularios = "en Insumos"
        elif titulo_panel == "Productos":
            text_up = "Panel Productos"
            text_down = "Registramos algo\nGus?"
            self.informacion_formularios = "en Productos"

        frame_bienvenida_e_info = ctk.CTkFrame(
            frame_sup,
            fg_color="transparent"
        )
        frame_bienvenida_e_info.grid(row=0, column=1, sticky="w")
        lbl_up = ctk.CTkLabel(
            frame_bienvenida_e_info,
            text=text_up,
            font=("Poppins", 20),
            text_color="#C49A85"
        )
        lbl_up.grid(row = 0, column = 0, sticky = "sw")
        lbl_down = ctk.CTkLabel(
            frame_bienvenida_e_info,
            text=text_down,
            font=("Mochiy Pop One", 32),
            text_color="#7A5230",
            justify = "left"
        )
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
        ventana_emergente_agregar_registro = ctk.CTkToplevel(
            fg_color="#FFF9F3"
        )
        ventana_emergente_agregar_registro.title(f"{titulo_panel} - Agregar Registro")
        ventana_emergente_agregar_registro.geometry("700x700")
        ventana_emergente_agregar_registro.lift()
        ventana_emergente_agregar_registro.focus()
        ventana_emergente_agregar_registro.grab_set()
        # Layout básico
        ventana_emergente_agregar_registro.grid_columnconfigure(0, weight=1)
        ventana_emergente_agregar_registro.grid_rowconfigure(0, weight=0)
        ventana_emergente_agregar_registro.grid_rowconfigure(1, weight=1)
        ventana_emergente_agregar_registro.grid_rowconfigure(2, weight=0)

        info_obtenida = {}

        lbl_titulo = ctk.CTkLabel(
            ventana_emergente_agregar_registro,
            text=f"Agregar registo {self.informacion_formularios}",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230"
        )
        lbl_titulo.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="n")

        frame_para_entries = ctk.CTkScrollableFrame(ventana_emergente_agregar_registro,
        fg_color="#FEF3E7",
        corner_radius=20,
        width=440,
        height=280
    )
        frame_para_entries.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        frame_para_entries.grid_columnconfigure(0, weight=1)

        for i, nombre_campo in enumerate(self.campos):
            # saltar campo id 
            if nombre_campo.lower() == "id":
                continue
            # etiqueta
            lbl = ctk.CTkLabel(
                frame_para_entries,
                text=nombre_campo,
                font=("Poppins", 16),
                text_color="#7A5230",
                anchor="w"
            )
            lbl.grid(row=i*2, column=0, padx=20, pady=(10, 0), sticky="ew")

            # entry
            entry = ctk.CTkEntry(
                frame_para_entries,
                width=260,
                placeholder_text=f"Ingrese {nombre_campo.lower()}...",
                corner_radius=10,

            )
            entry.grid(row=i*2 + 1, column=0, padx=20, pady=(0, 10), sticky="ew")

            info_obtenida[nombre_campo] = entry
        
        frame_botones = ctk.CTkFrame(ventana_emergente_agregar_registro, fg_color="transparent")
        frame_botones.grid(row=2, column=0, pady=15)

        def guardar():
            self.informacion_obtenida = info_obtenida
            ventana_emergente_agregar_registro.destroy()

        btn_guardar = ctk.CTkButton(
            frame_botones,
            text="Guardar",
            font=("Mochiy Pop One", 18),
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230",
            corner_radius=12,
            border_width=2,
            border_color="#D8B59D",
            command=guardar
        )
        btn_guardar.grid(row=0, column=0, padx=10)

        btn_cancelar = ctk.CTkButton(
            frame_botones,
            text="Cancelar",
            font=("Mochiy Pop One", 18),
            fg_color="#F2A3A3",
            hover_color="#E57C7C",
            text_color="#7A5230",
            corner_radius=12,
            command=ventana_emergente_agregar_registro.destroy
        )
        btn_cancelar.grid(row=0, column=1, padx=10)

        


    def ventana_eliminar_registros(self,titulo_panel):
        ventana_emergente_eliminar_registros = ctk.CTkToplevel(
            fg_color="#FFF9F3"
        )
        ventana_emergente_eliminar_registros.title(f"{titulo_panel} - Agregar Registro")
        ventana_emergente_eliminar_registros.geometry("400x300")
        ventana_emergente_eliminar_registros.lift()
        ventana_emergente_eliminar_registros.focus()
        ventana_emergente_eliminar_registros.grab_set()
        # Layout básico
        ventana_emergente_eliminar_registros.grid_columnconfigure(0, weight=1)
        ventana_emergente_eliminar_registros.grid_rowconfigure(0, weight=0)
        ventana_emergente_eliminar_registros.grid_rowconfigure(1, weight=1)
        ventana_emergente_eliminar_registros.grid_rowconfigure(2, weight=0)

        info_obtenida = {}

        lbl_titulo = ctk.CTkLabel(
            ventana_emergente_eliminar_registros,
            text=f"Eliminar registo {self.informacion_formularios}",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230"
        )
        lbl_titulo.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="n")

        frame_para_entries = ctk.CTkScrollableFrame(ventana_emergente_eliminar_registros,
        fg_color="#FEF3E7",
        corner_radius=20,
        width=440,
        height=280
        )
        frame_para_entries.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        frame_para_entries.grid_columnconfigure(0, weight=1)

        
        # etiqueta
        lbl = ctk.CTkLabel(
                frame_para_entries,
                text="ID",
                font=("Poppins", 16),
                text_color="#7A5230",
                anchor="w"
            )
        lbl.grid(row=0, column=0, padx=20, pady=(10, 0), sticky="ew")

            # entry
        entry = ctk.CTkEntry(
                frame_para_entries,
                width=260,
                placeholder_text=f"Ingrese ID....",
                corner_radius=10,

            )
        entry.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")

        info_obtenida["ID"] = entry
        
        frame_botones = ctk.CTkFrame(ventana_emergente_eliminar_registros, fg_color="transparent")
        frame_botones.grid(row=2, column=0, pady=15)

        def guardar():
            self.informacion_obtenida = info_obtenida
            ventana_emergente_eliminar_registros.destroy()

        btn_guardar = ctk.CTkButton(
            frame_botones,
            text="Guardar",
            font=("Mochiy Pop One", 18),
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230",
            corner_radius=12,
            border_width=2,
            border_color="#D8B59D",
            command=guardar
        )
        btn_guardar.grid(row=0, column=0, padx=10)

        btn_cancelar = ctk.CTkButton(
            frame_botones,
            text="Cancelar",
            font=("Mochiy Pop One", 18),
            fg_color="#F2A3A3",
            hover_color="#E57C7C",
            text_color="#7A5230",
            corner_radius=12,
            command=ventana_emergente_eliminar_registros.destroy
        )
        btn_cancelar.grid(row=0, column=1, padx=10)


    def ventana_modificar_registros(self,titulo_panel):
        ventana_emergente_modificar_registros = ctk.CTkToplevel(
            fg_color="#FFF9F3"
        )
        ventana_emergente_modificar_registros.title(f"{titulo_panel} - Agregar Registro")
        ventana_emergente_modificar_registros.geometry("700x700")
        ventana_emergente_modificar_registros.lift()
        ventana_emergente_modificar_registros.focus()
        ventana_emergente_modificar_registros.grab_set()
        # Layout básico
        ventana_emergente_modificar_registros.grid_columnconfigure(0, weight=1)
        ventana_emergente_modificar_registros.grid_rowconfigure(0, weight=0)
        ventana_emergente_modificar_registros.grid_rowconfigure(1, weight=1)
        ventana_emergente_modificar_registros.grid_rowconfigure(2, weight=0)

        info_obtenida = {}

        lbl_titulo = ctk.CTkLabel(
            ventana_emergente_modificar_registros,
            text=f"Modificar registo {self.informacion_formularios}",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230"
        )
        lbl_titulo.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="n")

        frame_para_entries = ctk.CTkScrollableFrame(ventana_emergente_modificar_registros,
        fg_color="#FEF3E7",
        corner_radius=20,
        width=440,
        height=280
    )
        frame_para_entries.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        frame_para_entries.grid_columnconfigure(0, weight=1)

        for i, nombre_campo in enumerate(self.campos):
            # etiqueta
            lbl = ctk.CTkLabel(
                frame_para_entries,
                text=nombre_campo,
                font=("Poppins", 16),
                text_color="#7A5230",
                anchor="w"
            )
            lbl.grid(row=i*2, column=0, padx=20, pady=(10, 0), sticky="ew")

            # entry
            entry = ctk.CTkEntry(
                frame_para_entries,
                width=260,
                placeholder_text=f"Ingrese {nombre_campo.lower()}...",
                corner_radius=10,

            )
            entry.grid(row=i*2 + 1, column=0, padx=20, pady=(0, 10), sticky="ew")

            info_obtenida[nombre_campo] = entry
        
        frame_botones = ctk.CTkFrame(ventana_emergente_modificar_registros, fg_color="transparent")
        frame_botones.grid(row=2, column=0, pady=15)

        def guardar():
            self.informacion_obtenida = info_obtenida
            ventana_emergente_modificar_registros.destroy()

        btn_guardar = ctk.CTkButton(
            frame_botones,
            text="Guardar",
            font=("Mochiy Pop One", 18),
            fg_color="#FEE3D0",
            hover_color="#D8B59D",
            text_color="#7A5230",
            corner_radius=12,
            border_width=2,
            border_color="#D8B59D",
            command=guardar
        )
        btn_guardar.grid(row=0, column=0, padx=10)

        btn_cancelar = ctk.CTkButton(
            frame_botones,
            text="Cancelar",
            font=("Mochiy Pop One", 18),
            fg_color="#F2A3A3",
            hover_color="#E57C7C",
            text_color="#7A5230",
            corner_radius=12,
            command=ventana_emergente_modificar_registros.destroy
        )
        btn_cancelar.grid(row=0, column=1, padx=10)

    def crear_sidebar(self):
        # reutiliza tu Sidebar
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
