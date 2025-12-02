import customtkinter as ctk
import os
from PIL import Image
from view.SideBar import Sidebar
from view.InterfazNuevaVenta import NuevaVenta
from view.InterfazHistorialDeVentas import Historial_de_ventas
from view.InterfazGastos import interfaz_de_gastos
from view.InterfazInsumos import interfaz_de_insumos
from view.InterfazProductos import interfaz_de_productos

class MainInterface(ctk.CTkFrame):
    def __init__(self, interface):
        super().__init__(interface, fg_color="#FFF9F3")
        self.interface = interface
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.Menu_Principal()
        
    def Menu_Principal(self):
        self.configurar_ventana()
        self.configurar_grid_principal()
        self.sidebar = Sidebar(self, on_nav=self.navegar)
        self.cargar_fuentes()
        self.crear_parte_superior()
        self.crear_parte_media_y_baja()
     
    # --- Config general ---

    def configurar_ventana(self):
        self.interface.title("Kunibo - Dashboard")

    def configurar_grid_principal(self):
        self.grid_rowconfigure(0, weight=0)   # Parte superior
        self.grid_rowconfigure(1, weight=1)   # Título Notificaciones
        self.grid_rowconfigure(2, weight=1)   # Mensaje notificaciones
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)  # columna izquierda
        self.grid_columnconfigure(1, weight=1)  # columna derecha

    def cargar_fuentes(self):
        font_path_Mochiy = os.path.join(self.base_path, "fonts", "MochiyPopOne-Regular.ttf")
        font_path_Poppins = os.path.join(self.base_path, "fonts", "Poppins-Regular.ttf")
        ctk.FontManager.load_font(font_path_Mochiy)
        ctk.FontManager.load_font(font_path_Poppins)

    # --- Parte superior del dashboard ---

    def crear_parte_superior(self):
        self.frame_superior_dashboard = ctk.CTkFrame(
            self,
            fg_color="#FEF3E7"
        )
        self.frame_superior_dashboard.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="nsew"
        )
        self.frame_superior_dashboard.grid_propagate(False)

        self.frame_superior_dashboard.grid_columnconfigure(0, weight=0)  # logo
        self.frame_superior_dashboard.grid_columnconfigure(1, weight=0)  # bienvenida
        self.frame_superior_dashboard.grid_columnconfigure(2, weight=1)  # ventas
        self.frame_superior_dashboard.grid_columnconfigure(3, weight=1)  # ganancias
        self.frame_superior_dashboard.grid_columnconfigure(4, weight=1)  # gasto
        self.frame_superior_dashboard.grid_rowconfigure(0, weight=1) # Linea unica

        self._crear_logo_dashboard()
        self._crear_bienvenida_y_saludo()
        self._crear_tarjeta_ventas_mes()
        self._crear_tarjeta_ganancias_mes()
        self._crear_tarjeta_gasto_mes()

    def _crear_logo_dashboard(self):
        logo_path = os.path.join(self.base_path, "images", "Logo.png")
        img = Image.open(logo_path)
        self.dashboard_logo_image = ctk.CTkImage(
            light_image=img,
            dark_image=img,
            size=(200, 200)
        )
        logo_Button_dashboard = ctk.CTkButton(
            self.frame_superior_dashboard,
            text="",
            image=self.dashboard_logo_image,
            fg_color="transparent", 
            hover_color="#FEF3E7",
            command=lambda: self.crear_sidebar()

        )
        logo_Button_dashboard.grid(
            row=0,
            column=0,
            sticky="nsew",
            pady=10
        )

    def _crear_bienvenida_y_saludo(self):
        frame_bienvenida = ctk.CTkFrame(
            self.frame_superior_dashboard,
            fg_color="#FEF3E7"
        )
        frame_bienvenida.grid(
            row=0,
            column=1,
            sticky="we",
            padx=(10, 0),
            pady=10
        )

        frame_bienvenida.grid_columnconfigure(0, weight=1)
        frame_bienvenida.grid_rowconfigure(0, weight=1)
        frame_bienvenida.grid_rowconfigure(1, weight=1)

        lbl_bienvenida = ctk.CTkLabel(
            frame_bienvenida,
            text="Panel de control de ventas",
            font=("Poppins", 20),
            text_color="#C49A85"
        )
        lbl_bienvenida.grid(
            row=0,
            column=0,
            sticky="w"
        )

        lbl_saludo = ctk.CTkLabel(
            frame_bienvenida,
            text="Bienvenido\nGus",
            font=("Mochiy Pop One", 40, "bold"),
            text_color="#7A5230",
            justify="left"
        )
        lbl_saludo.grid(
            row=1,
            column=0,
            sticky="w"
        )

    def _crear_tarjeta_ventas_mes(self):
        frame_ventas_mes = ctk.CTkFrame(
            self.frame_superior_dashboard,
            fg_color="#FEE3D0",
            border_width=4,
            border_color="#D8B59D",
            corner_radius=48
        )
        frame_ventas_mes.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=(15, 15),
            pady=(30, 30)
        )
        frame_ventas_mes.grid_propagate(False)

        frame_ventas_mes.grid_columnconfigure(0, weight=1)
        frame_ventas_mes.grid_columnconfigure(1, weight=3)
        frame_ventas_mes.grid_rowconfigure(0, weight=1)
        frame_ventas_mes.grid_rowconfigure(1, weight=0)
        frame_ventas_mes.grid_rowconfigure(2, weight=0)
        frame_ventas_mes.grid_rowconfigure(3, weight=1)

        path_grafica_subida = os.path.join(self.base_path, "images", "Grafica_de_subida.png")
        img_grafica_subida = Image.open(path_grafica_subida)
        self.grafica_de_subida_image = ctk.CTkImage(
            light_image=img_grafica_subida,
            dark_image=img_grafica_subida,
            size=(100, 100)
        )
        grafica_subida_label = ctk.CTkLabel(
            frame_ventas_mes,
            text="",
            image=self.grafica_de_subida_image
        )
        grafica_subida_label.grid(
            row=0,
            column=0,
            rowspan=4,
            sticky="w",
            pady=(15, 15),
            padx=(15, 10)
        )

        lbl_ventas_mes = ctk.CTkLabel(
            frame_ventas_mes,
            text="Ventas del mes",
            font=("Poppins", 20),
            text_color="#C49A85"
        )
        lbl_ventas_mes.grid(
            row=1,
            column=1,
            sticky="sw"
        )

        lbl_cantidad_ventas_mes = ctk.CTkLabel(
            frame_ventas_mes,
            text="$12,345.67",
            font=("Mochiy Pop One", 26),
            text_color="#7A5230"
        )
        lbl_cantidad_ventas_mes.grid(
            row=2,
            column=1,
            sticky="nw"
        )

    def _crear_tarjeta_ganancias_mes(self):
        frame_ganancias_mes = ctk.CTkFrame(
            self.frame_superior_dashboard,
            fg_color="#FEE3D0",
            border_width=4,
            border_color="#D8B59D",
            corner_radius=48
        )
        frame_ganancias_mes.grid(
            row=0,
            column=3,
            sticky="nsew",
            padx=(15, 15),
            pady=(30, 30)
        )
        frame_ganancias_mes.grid_propagate(False)

        frame_ganancias_mes.grid_columnconfigure(0, weight=1)
        frame_ganancias_mes.grid_rowconfigure(0, weight=1)
        frame_ganancias_mes.grid_rowconfigure(1, weight=0)
        frame_ganancias_mes.grid_rowconfigure(2, weight=0)
        frame_ganancias_mes.grid_rowconfigure(3, weight=1)

        lbl_ganancias_mes = ctk.CTkLabel(
            frame_ganancias_mes,
            text="Ganancias del mes",
            font=("Poppins", 20),
            text_color="#C49A85"
        )
        lbl_ganancias_mes.grid(
            row=1,
            column=0,
            sticky="sw",
            padx=(20, 0)
        )

        lbl_cantidad_ganancias_mes = ctk.CTkLabel(
            frame_ganancias_mes,
            text="$8,765.43",
            font=("Mochiy Pop One", 26),
            text_color="#7A5230"
        )
        lbl_cantidad_ganancias_mes.grid(
            row=2,
            column=0,
            sticky="nw",
            padx=(20, 0)
        )

    def _crear_tarjeta_gasto_mes(self):
        frame_gasto_mes = ctk.CTkFrame(
            self.frame_superior_dashboard,
            fg_color="#FEE3D0",
            border_width=4,
            border_color="#D8B59D",
            corner_radius=48
        )
        frame_gasto_mes.grid(
            row=0,
            column=4,
            sticky="nsew",
            padx=(15, 30),
            pady=(30, 30)
        )
        frame_gasto_mes.grid_propagate(False)

        frame_gasto_mes.grid_columnconfigure(0, weight=1)
        frame_gasto_mes.grid_columnconfigure(1, weight=3)
        frame_gasto_mes.grid_rowconfigure(0, weight=1)
        frame_gasto_mes.grid_rowconfigure(1, weight=0)
        frame_gasto_mes.grid_rowconfigure(2, weight=0)
        frame_gasto_mes.grid_rowconfigure(3, weight=1)

        path_grafica_bajada = os.path.join(self.base_path, "images", "Grafica_de_bajada.png")
        img_grafica_bajada = Image.open(path_grafica_bajada)
        self.grafica_de_bajada_image = ctk.CTkImage(
            light_image=img_grafica_bajada,
            dark_image=img_grafica_bajada,
            size=(100, 100)
        )
        grafica_bajada_label = ctk.CTkLabel(
            frame_gasto_mes,
            text="",
            image=self.grafica_de_bajada_image
        )
        grafica_bajada_label.grid(
            row=0,
            column=0,
            rowspan=4,
            sticky="w",
            pady=(15, 15),
            padx=(15, 15)
        )

        lbl_gasto_mes = ctk.CTkLabel(
            frame_gasto_mes,
            text="Gasto del mes",
            font=("Poppins", 20),
            text_color="#C49A85"
        )
        lbl_gasto_mes.grid(
            row=1,
            column=1,
            sticky="sw"
        )

        lbl_cantidad_gasto_mes = ctk.CTkLabel(
            frame_gasto_mes,
            text="$3,580.24",
            font=("Mochiy Pop One", 26),
            text_color="#7A5230"
        )
        lbl_cantidad_gasto_mes.grid(
            row=2,
            column=1,
            sticky="nw"
        )

    # --- Parte media y baja ---

    def crear_parte_media_y_baja(self):
        lbl_notificaciones = ctk.CTkLabel(
            self,
            text="Notificaciones",
            font=("Mochiy Pop One", 24, "bold"),
            text_color="#7A5230"
        )
        lbl_notificaciones.grid(
            row=1,
            column=0,
            sticky="wns",
            padx=(120, 0),
            pady = (20,20)
        )

        lbl_no_hay_notificaciones = ctk.CTkLabel(
            self,
            text="No hay notificaciones nuevas\n por mostrar",
            font=("Mochiy Pop One", 30),
            text_color="#E9DFD6"
        )
        lbl_no_hay_notificaciones.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

    def navegar(self, destino: str):
        if destino == "Panel Principal":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Dashboard")
            self.Menu_Principal()

        elif destino == "Nueva venta":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Nueva Venta")

            self.nueva_venta = NuevaVenta(
            interface=self,                    # contenedor
            parent_navegar=self.navegar
        )
            self.nueva_venta.pack(fill="both", expand=True)

        elif destino == "Historial de ventas":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Historial de ventas")
            self.historial_de_ventas = Historial_de_ventas(
                interface=self,
                parent_navegar=self.navegar,
                ventana_principal = self.interface

            )
            self.historial_de_ventas.pack(fill="both" ,expand = True)

        elif destino == "Gastos":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Gastos")
            self.historial_de_ventas = interfaz_de_gastos(
                interface=self,
                parent_navegar=self.navegar,
                ventana_principal = self.interface

            )
            self.historial_de_ventas.pack(fill="both" ,expand = True)
        elif destino == "Insumos":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Insumos")
            self.historial_de_ventas = interfaz_de_insumos(
                interface=self,
                parent_navegar=self.navegar,
                ventana_principal = self.interface

            )
            self.historial_de_ventas.pack(fill="both" ,expand = True)

        elif destino == "Productos":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Insumos")
            self.historial_de_ventas = interfaz_de_productos(
                interface=self,
                parent_navegar=self.navegar,
                ventana_principal = self.interface

            )
            self.historial_de_ventas.pack(fill="both" ,expand = True)




            
    
    def crear_sidebar(self):
        self.sidebar = Sidebar(self, on_nav=self.navegar)
        self.sidebar.place(x=0, y=0, relheight=1)

        # Activar “detector” de click fuera
        self.interface.bind_all("<Button-1>", self._click_fuera_sidebar)
    
    def _click_fuera_sidebar(self, event):
        SIDEBAR_WIDTH = 260
        if event.x > SIDEBAR_WIDTH:
            self.cerrar_sidebar()

    def cerrar_sidebar(self):
        
        self.sidebar.destroy()
        del self.sidebar

        # Quitamos el bind para que ya no esté escuchando clicks todo el tiempo
        self.interface.unbind_all("<Button-1>")
