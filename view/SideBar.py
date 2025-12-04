import customtkinter as ctk
from PIL import Image
import os

class Sidebar(ctk.CTkFrame):
    def __init__(self, interface, on_nav):
        super().__init__(interface, fg_color="#FCEEDF")
        base = os.path.dirname(os.path.abspath(__file__))
        self.base_path = base
        self.on_nav = on_nav
         
        self.cargar_fuentes()
        self._configurar_grid()
        self._crear_logo()
        self._crear_botones()

    def cargar_fuentes(self):
        font_path_Mochiy = os.path.join(self.base_path, "fonts", "MochiyPopOne-Regular.ttf")
        font_path_Poppins = os.path.join(self.base_path, "fonts", "Poppins-Regular.ttf")
        ctk.FontManager.load_font(font_path_Mochiy)
        ctk.FontManager.load_font(font_path_Poppins)
    
    def _configurar_grid(self):
        self.grid_rowconfigure(0, weight=0)  # logo
        self.grid_rowconfigure(1, weight=0)  # Boton panel principal
        self.grid_rowconfigure(8, weight=20) # espaciado y presion
        self.grid_columnconfigure(0, weight=1) # fila unica

    def _crear_logo(self):
        logo_path = os.path.join(self.base_path, "images", "Logo.png")
        img = Image.open(logo_path)
        self.logo_image = ctk.CTkImage(
            light_image=img, 
            dark_image=img, 
            size=(200, 200)
            )
        lbl = ctk.CTkButton(
            self, 
            text="", 
            image=self.logo_image, 
            hover_color="#FCEEDF", 
            fg_color="transparent", 
            command=lambda: self.Destruir_sidebar()
                            )
        lbl.grid(
            row=0, 
            column=0,
            sticky = "nsew",)

    def _crear_botones(self):
        #codigo que necesitaremos en cada uno
        base = os.path.dirname(os.path.abspath(__file__))
        #Boton panel principal
         #imagen icon home 
        icon_home_path = os.path.join(base, "images", "Icon_home_sidebar.png")
        img_home = Image.open(icon_home_path)
        
        self.home_dashoard_image = ctk.CTkImage(
            light_image=img_home,
            dark_image=img_home,
            size=(24,24)
        )
       
        btn_panel_principal = ctk.CTkButton(
            self,
                text="Panel principal",
                corner_radius=20,
                image = self.home_dashoard_image,
                compound= "left",
                anchor="w",
                height=40, 
                font= ("Mochiy Pop One", 11),
                fg_color="#F9D5B8",
                text_color="#654028",
                hover_color="#F0C6A5",
                border_color="#D8B59D",
                border_width=2,
                command=lambda on_nav="Panel Principal": self.on_nav(on_nav)
            )
        btn_panel_principal.grid(
            row=1,
            column=0,
            sticky="new",
            pady=(0,10),
            padx= 10
        )
        #Boton ventas con imagen
        icon_carrito_path = os.path.join(base, "images", "Icon_carrito_sidebar.png")
        img_carrito = Image.open(icon_carrito_path)
        self.carrito_dashoard_image = ctk.CTkImage(
            light_image=img_carrito,
            dark_image=img_carrito,
            size=(24,24)
        )
        btn_nueva_venta = ctk.CTkButton(
            self,
                text="Nueva Venta",
                corner_radius=20,
                image = self.carrito_dashoard_image,
                compound= "left",
                anchor="w",
                height=40,
                font= ("Mochiy Pop One", 11),
                fg_color="#F9D5B8",
                text_color="#654028",
                hover_color="#F0C6A5",
                border_color="#D8B59D",
                border_width=2,
                command=lambda on_nav="Nueva venta": self.on_nav(on_nav)
            )
        btn_nueva_venta.grid(
            row=2,
            column=0,
            sticky="new",
            pady=(0,10),
            padx= 10
        )
        #Boton Historial de ventas con imagen 
        icon_historial_de_ventas_path = os.path.join(base, "images", "Icon_historial_de_ventas_sidebar.png")
        img_historial_de_ventas = Image.open(icon_historial_de_ventas_path)
        self.historial_de_ventas_dashboard = ctk.CTkImage(
            light_image=img_historial_de_ventas,
            dark_image=img_historial_de_ventas,
            size=(24,24)
        )
        btn_historial_de_ventas = ctk.CTkButton(
            self,
                text="Historial de ventas",
                corner_radius=20,
                image = self.historial_de_ventas_dashboard,
                compound= "left",
                anchor="w",
                height=40,
                font= ("Mochiy Pop One", 11),
                fg_color="#F9D5B8",
                text_color="#654028",
                hover_color="#F0C6A5",
                border_color="#D8B59D",
                border_width=2,
                command=lambda on_nav="Historial de ventas": self.on_nav(on_nav)
            )
        btn_historial_de_ventas.grid(
            row=3,
            column=0,
            sticky="new",
            pady=(0,10),
            padx= 10
            )
        #Boton Gastos con imagen
        icon_gastos_path = os.path.join(base, "images", "Icon_gastos_sidebar.png")
        img_gastos = Image.open(icon_gastos_path)
        self.gastos_dashboard = ctk.CTkImage(
            light_image=img_gastos,
            dark_image=img_gastos,
            size=(24,24)
        )
        btn_gastos = ctk.CTkButton(
            self,
                text="Gastos",
                corner_radius=20,
                image = self.gastos_dashboard, 
                compound= "left",
                anchor="w",
                height=40,
                font= ("Mochiy Pop One", 11),
                fg_color="#F9D5B8",
                text_color="#654028",
                hover_color="#F0C6A5",
                border_color="#D8B59D",
                border_width=2,
                command=lambda on_nav="Gastos": self.on_nav(on_nav)
            )
        btn_gastos.grid(
            row=4,
            column=0,
            sticky="new",
            pady=(0,10),
            padx= 10
        )
        #Boton Insumos con imagen
        icon_insumos_sidebar = os.path.join(base, "images", "Icon_insumos_sidebar.png")
        img_insumos_sidebar = Image.open(icon_insumos_sidebar)
        self.insumos_dashboard = ctk.CTkImage(
            light_image=img_insumos_sidebar,
            dark_image=img_insumos_sidebar,
            size=(24,24)
        ) 
        btn_insumos = ctk.CTkButton(
            self,
                text="Insumos",
                corner_radius=20,
                image = self.insumos_dashboard, 
                compound= "left",
                anchor="w",
                height=40,
                font= ("Mochiy Pop One", 11),
                fg_color="#F9D5B8",
                text_color="#654028",
                hover_color="#F0C6A5",
                border_color="#D8B59D",
                border_width=2,
                command=lambda on_nav="Insumos": self.on_nav(on_nav)
            )
        btn_insumos.grid(
            row=5,
            column=0,
            sticky="new",
            pady=(0,10),
            padx= 10
        )
        #Boton productos con imagen
        icon_productos_sidebar = os.path.join(base, "images", "Icon_productos_sidebar.png")
        img_productos_sidebar = Image.open(icon_productos_sidebar)
        self.productos_dashboard = ctk.CTkImage(
            light_image=img_productos_sidebar,
            dark_image=img_productos_sidebar,
            size=(24,24) 
        ) 
        btn_prodcutos = ctk.CTkButton(
            self,
                text="Productos",
                corner_radius=20,
                image = self.productos_dashboard, 
                compound= "left",
                anchor="w",
                height=40,
                font= ("Mochiy Pop One", 11),
                fg_color="#F9D5B8",
                text_color="#654028",
                hover_color="#F0C6A5",
                border_color="#D8B59D",
                border_width=2,
                command=lambda on_nav="Productos": self.on_nav(on_nav)
            )
        btn_prodcutos.grid(
            row=6,
            column=0,
            sticky="new",
            pady=(0,10),
            padx= 10
        )

    def Destruir_sidebar(self):
        self.destroy()

