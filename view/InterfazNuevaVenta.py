import customtkinter as ctk
import os
from PIL import Image
from view.SideBar import Sidebar
from controller.controlador_nueva_venta import ControladorNuevaVenta
from tkinter import messagebox
from controller.controlador_dashboard import ControladorDashboard
class NuevaVenta(ctk.CTkFrame):
    def __init__(self, interface, 
                 parent_navegar):
        super().__init__(interface, fg_color="#FFF9F3")
        
        # REFERENCIAS DEL PADRE
        self.interface = interface                # MainInterface (contenedor)
        self.parent_navegar = parent_navegar      # router real

        # Instanciar el controlador
        self.controlador = ControladorNuevaVenta()
        self.controlador_dashboard =ControladorDashboard()

        self.mapa_productos_ids = {}
        self.carrito_items = {}
        self.contador_filas_carrito = 0

        self.total_var = ctk.StringVar(value="$0.00")
        self.base_path = os.path.dirname(os.path.abspath(__file__))

        # Cargar iconos
        self.icon_plus = ctk.CTkImage(
            light_image=Image.open(os.path.join(self.base_path,"images", "signo_plus_icon_ventas.png")),
            dark_image=Image.open(os.path.join(self.base_path, "images","signo_plus_icon_ventas.png")),
            size=(20, 20)
        )

        self.icon_minus = ctk.CTkImage(
            light_image=Image.open(os.path.join(self.base_path, "images","signo_minus_icon_ventas.png")),
            dark_image=Image.open(os.path.join(self.base_path, "images", "signo_minus_icon_ventas.png")),
            size=(20, 20)
        )

        self.icon_delete = ctk.CTkImage(
            light_image=Image.open(os.path.join(self.base_path, "images","signo_delete_icon_ventas.png")),
            dark_image=Image.open(os.path.join(self.base_path, "images","signo_delete_icon_ventas.png")),
            size=(20, 20)
        )

        self.cargar_mapa_productos()
        
        self.inicializador_nueva_venta()

    def inicializador_nueva_venta(self):
        self.configurar_grid()
        self.crear_parte_superior()
        self.crear_contenido_nueva_venta()

    def configurar_grid(self):
        self.grid_rowconfigure(0, weight=0)   # Parte superior
        self.grid_rowconfigure(1, weight=1)   # Título Nueva venta
        self.grid_rowconfigure(2, weight=3)   # Frames producto y carrito
        self.grid_columnconfigure(0, weight=1)  # columna izquierda
        self.grid_columnconfigure(1, weight=1)  # columna derecha

    def crear_parte_superior(self):
        datos=self.controlador_dashboard.obtener_resumen_global(self.interface.id_usuario)
        self.ingresos_totales = datos["ingresos_totales"]
        self.ventas_realizadas = datos["ventas_realizadas"]
        self.gastos_totales = datos.get("gastos_totales", 0)
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
            text="Panel Nueva Venta",
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
            text="¿Que vamos\na vender hoy?",
            font=("Mochiy Pop One", 32, "bold"),
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
            text=f"${self.ingresos_totales:,.2f}",
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
            text=f"${self.ingresos_totales:,.2f}",
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
            text=f"${self.gastos_totales:,.2f}",
            font=("Mochiy Pop One", 26),
            text_color="#7A5230"
        )
        lbl_cantidad_gasto_mes.grid(
            row=2,
            column=1,
            sticky="nw"
        )

    def crear_contenido_nueva_venta(self):
        self.label_nueva_venta()
        self.crear_frame_inferior()

    def crear_frame_inferior(self):
        frame_inferior = ctk.CTkFrame(self, fg_color="#FFF9F3")
        frame_inferior.grid(
            row = 2,
            column = 0,
            columnspan = 2,
            sticky = "nsew"
        )
        #configurar grid para el frame inferior
        frame_inferior.rowconfigure(0, weight=0) #fila unica
        frame_inferior.columnconfigure(0, weight= 2) #frame scroll bar productos 
        frame_inferior.columnconfigure(1, weight= 0) #frame scroll bar carrito 
        
        frame_productos = ctk.CTkFrame(
            frame_inferior,
            fg_color="#FEE3D0",
            border_width=4,
            border_color="#D8B59D" ,
            corner_radius=60
            )
        frame_productos.grid(
            row = 0,
            column = 0, 
            pady = (0, 40),
            padx = (50, 20),
            sticky ="nsew"
        )

        frame_productos.rowconfigure(0, weight=1)
        frame_productos.rowconfigure(1, weight=4)
        frame_productos.columnconfigure(0, weight=1)
        frame_productos.configure(height= 400)
        frame_productos.grid_propagate(False)

        #Creamos frame con label para productos disponibles 
        frame_lbl_productos_disponibles = ctk.CTkFrame(
            frame_productos,
            fg_color="#FEF3E7",
            border_width=4,
            border_color="#D8B59D",
            corner_radius=60
            )
        frame_lbl_productos_disponibles.grid(
            row = 0,
            column = 0,
            pady = (20,20),
            padx = (20,20),
            sticky = "NSEW"
        )
        frame_lbl_productos_disponibles.rowconfigure(0, weight=1)
        frame_lbl_productos_disponibles.columnconfigure(0, weight=1)
        lbl_productos_disponibles = ctk.CTkLabel(
            frame_lbl_productos_disponibles,
            text="Productos disponibles",
            font= ("Mochiy Pop One", 24),
            text_color = "#7A5230",
            anchor="w"
        )
        lbl_productos_disponibles.grid(
            column = 0,
            row = 0,
            sticky = "ew",
            padx=20,
            pady =15
        )

        frame_productos_disponibles = ctk.CTkFrame(
            frame_productos,
            fg_color="#FEF3E7",
            border_width=4,
            border_color="#D8B59D",
            corner_radius=60
        )
        frame_productos_disponibles.grid(
            column =0,
            row=1,
            sticky ="NSEW",
            padx = (20,20),
            pady = (0,20)
        )
        frame_productos_disponibles.rowconfigure(0, weight=1)
        frame_productos_disponibles.columnconfigure(0, weight=1)

        #frame donde ubicaremos todos los componentes del carrito
        frame_carrito = ctk.CTkFrame(
            frame_inferior, 
            fg_color="#FEE3D0",
            border_width=4,
            border_color="#D8B59D",
            corner_radius=60
            )
        frame_carrito.grid(
            row = 0,
            column = 1,
            pady = (0,40),
            padx = (30, 50),
            sticky = "NSEW"
        )

        #configuramos grid para el frame donde ira todo el carrito 
        frame_carrito.rowconfigure(0, weight=1) #este sera el frame para poner el texto "Carrito de compras"
        frame_carrito.rowconfigure(1, weight=3) #aqui ira el ctk scrollbar con los productos elegidos de prodctos disponibles 
        frame_carrito.rowconfigure(2, weight=1) #aqui ira la label del total junto con su frame
        frame_carrito.columnconfigure(0, weight=1) #fila unica 
        frame_para_lbl_carrito_de_compras = ctk.CTkFrame(
            frame_carrito, 
            fg_color="#FEF3E7",
            border_color="#D8B59D",
            corner_radius=60,
            border_width=4
        )
        frame_para_lbl_carrito_de_compras.grid(
            row = 0,
            column = 0,
            sticky = "nswe",
            pady = 20,
            padx = 20
        )

        #configuramos grid interno para para evitar problemas con weigth
        frame_para_lbl_carrito_de_compras.rowconfigure(0, weight=1)
        frame_para_lbl_carrito_de_compras.columnconfigure(0, weight=1)
        lbl_carrito_de_compras = ctk.CTkLabel(
            frame_para_lbl_carrito_de_compras,
            text="Carrito de compras",
            font= ("Mochiy Pop One", 24),
            text_color = "#7A5230",
            anchor="w"
        )
        lbl_carrito_de_compras.grid(
            column = 0,
            row = 0,
            sticky = "ew",
            padx=20,
            pady =15
        )
        frame_para_productos_carrito_de_compras = ctk.CTkFrame(
            frame_carrito, 
            fg_color="#FEF3E7",
            border_color="#D8B59D",
            corner_radius=60,
            border_width=4
        )
        frame_para_productos_carrito_de_compras.grid(
            row = 1,
            column = 0,
            sticky = "nswe",
            pady = (0,20),
            padx = 20
        )
        frame_para_lbl_total_carrito_de_compras = ctk.CTkFrame(
            frame_carrito, 
            fg_color="#FEF3E7",
            border_color="#D8B59D",
            corner_radius=60,
            border_width=4
        )
        frame_para_lbl_total_carrito_de_compras.grid(
            row = 2,
            column = 0,
            sticky = "nswe",
            pady = (0,20),
            padx = 20
        )

        #configuramos para evitar problemas con weight
        frame_para_lbl_total_carrito_de_compras.rowconfigure(0, weight=1) # palabra total
        frame_para_lbl_total_carrito_de_compras.rowconfigure(1, weight=1) # variable numerica
        frame_para_lbl_total_carrito_de_compras.rowconfigure(2, weight=1) #btn guardar
        frame_para_lbl_total_carrito_de_compras.columnconfigure(0,weight=1)
        lbl_total = ctk.CTkLabel(
            frame_para_lbl_total_carrito_de_compras,
            text="Total",
            font= ("Mochiy Pop One", 24),
            text_color = "#7A5230",
            anchor="w"
        )
        lbl_total.grid(
            column = 0,
            row = 0,
            sticky = "ew",
            padx=20,
            pady =15
        )
        lbl_total_numerica = ctk.CTkLabel(
            frame_para_lbl_total_carrito_de_compras,
            textvariable = self.total_var,
            font= ("Mochiy Pop One", 24),
            text_color = "#7A5230",
            anchor="center"
        )
        lbl_total_numerica.grid(
            column = 1,
            row = 0,
            sticky = "ew",
            padx=20,
            pady =15
        )
        btn_guardar_carrio = ctk.CTkButton(
            frame_para_lbl_total_carrito_de_compras,
            text="Guardar",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230",
            anchor= "e",
            corner_radius=10,
            border_width=2,
            border_color="#D8B59D",
            fg_color="#FEE3D0",
            command=self.guardar_ventas
        )
        btn_guardar_carrio.grid(
            column = 2,
            row = 0,
            sticky = "nsew",
            pady = 15,
            padx= 20
        )
        frame_para_productos_carrito_de_compras.rowconfigure(0,weight=0)
        frame_para_productos_carrito_de_compras.columnconfigure(0,weight=1)
        self.crear_barras_deslizantes_con_productos(frame_productos_disponibles,frame_para_productos_carrito_de_compras)
    
    def crear_barras_deslizantes_con_productos(self, frame_productos_disponibles, frame_para_productos_carrito_de_compras):
        # -------- SCROLL DE PRODUCTOS DISPONIBLES --------
        scrol_bar_productos = ctk.CTkScrollableFrame(
            frame_productos_disponibles,
            width=50,
            height=200,
            fg_color="#FEF3E7",
            scrollbar_button_color="#D8B59D",
            scrollbar_button_hover_color="#D0A68A"
        )
        scrol_bar_productos.grid(
            column=0,
            row=0,
            sticky="nsew",
            pady=(42, 58),
            padx=30
        )
        scrol_bar_productos.rowconfigure((0, 1, 2, 3), weight=1)
        scrol_bar_productos.columnconfigure((0, 1), weight=1)

        self.lista_botones_productos = []

        self.btn_producto_fresa = ctk.CTkButton(
            scrol_bar_productos,
            text="Fresa",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230",
            anchor="center",
            fg_color="#FFE3E8",
            hover_color="#FFB8C5",
            border_color="#FFB8C5",
            border_width=2,
            corner_radius=10,
            command=lambda: self.enviar_boton_a_carrito("Fresa", 30.0)
        )
        self.btn_producto_fresa.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")
        self.lista_botones_productos.append(self.btn_producto_fresa)

        self.btn_producto_chocolate = ctk.CTkButton(
            scrol_bar_productos,
            text="Chocolate",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230",
            anchor="center",
            fg_color="#D1AB89",
            hover_color="#543921",
            border_color="#543921",
            border_width=2,
            corner_radius=10,
            command=lambda: self.enviar_boton_a_carrito("Chocolate", 35.0)
        )
        self.btn_producto_chocolate.grid(row=0, column=1, pady=10, padx=10, sticky="nsew")
        self.lista_botones_productos.append(self.btn_producto_chocolate)

        self.btn_producto_nuez = ctk.CTkButton(
            scrol_bar_productos,
            text="Nuez",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230",
            anchor="center",
            fg_color="#B87C47",
            hover_color="#543921",
            border_color="#543921",
            border_width=2,
            corner_radius=10,
            command=lambda: self.enviar_boton_a_carrito("Nuez", 40.0)
        )
        self.btn_producto_nuez.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")
        self.lista_botones_productos.append(self.btn_producto_nuez)

        self.btn_producto_piña_coco = ctk.CTkButton(
            scrol_bar_productos,
            text="Piña coco",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230",
            anchor="center",
            fg_color="#FEFEE7",
            hover_color="#FCFCBA",
            border_color="#FCFCBA",
            border_width=2,
            corner_radius=10,
            command=lambda: self.enviar_boton_a_carrito("Piña coco", 42.0)
        )
        self.btn_producto_piña_coco.grid(row=1, column=1, pady=10, padx=10, sticky="nsew")
        self.lista_botones_productos.append(self.btn_producto_piña_coco)

        self.btn_producto_pistache = ctk.CTkButton(
            scrol_bar_productos,
            text="Pistache",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230",
            anchor="center",
            fg_color="#DFF4E4",
            hover_color="#C0E9C9",
            border_color="#C0E9C9",
            border_width=2,
            corner_radius=10,
            command=lambda: self.enviar_boton_a_carrito("Pistache", 45.0)
        )
        self.btn_producto_pistache.grid(row=2, column=0, pady=10, padx=10, sticky="nsew")
        self.lista_botones_productos.append(self.btn_producto_pistache)

        self.btn_producto_capuchino = ctk.CTkButton(
            scrol_bar_productos,
            text="Capuchino",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230",
            anchor="center",
            fg_color="#CAB098",
            hover_color="#A87E57",
            border_color="#A87E57",
            border_width=2,
            corner_radius=10,
            command=lambda: self.enviar_boton_a_carrito("Capuchino", 48.0)
        )
        self.btn_producto_capuchino.grid(row=2, column=1, pady=10, padx=10, sticky="nsew")
        self.lista_botones_productos.append(self.btn_producto_capuchino)

        self.btn_producto_vainilla = ctk.CTkButton(
            scrol_bar_productos,
            text="Vainilla",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230",
            anchor="center",
            fg_color="#FFFAF4",
            hover_color="#D8B59D",
            border_color="#D8B59D",
            border_width=2,
            corner_radius=10,
            command=lambda: self.enviar_boton_a_carrito("Vainilla", 32.0)
        )
        self.btn_producto_vainilla.grid(row=3, column=0, pady=10, padx=10, sticky="nsew")
        self.lista_botones_productos.append(self.btn_producto_vainilla)

        self.btn_producto_cafe = ctk.CTkButton(
            scrol_bar_productos,
            text="Cafe",
            font=("Mochiy Pop One", 24),
            text_color="#FFF9F3",
            anchor="center",
            fg_color="#674736",
            hover_color="#2F2019",
            border_color="#2F2019",
            border_width=2,
            corner_radius=10,
            command=lambda: self.enviar_boton_a_carrito("Cafe", 38.0)
        )
        self.btn_producto_cafe.grid(row=3, column=1, pady=10, padx=10, sticky="nsew")
        self.lista_botones_productos.append(self.btn_producto_cafe)

        # -------- SCROLL DEL CARRITO --------
        self.scrol_bar_productos = ctk.CTkScrollableFrame(
            frame_para_productos_carrito_de_compras,
            width=50,
            height=100,
            fg_color="#FEF3E7",
            scrollbar_button_color="#D8B59D",
            scrollbar_button_hover_color="#D0A68A"
        )
        self.scrol_bar_productos.grid(
            column=0,
            row=0,
            sticky="nsew",
            pady=15,
            padx=35
        )
        self.scrol_bar_productos.columnconfigure(0, weight=1)

    def enviar_boton_a_carrito(self, nombre, precio):
        if nombre in self.carrito_items:
            self.incrementar(nombre)
            return

        frame = ctk.CTkFrame(
            self.scrol_bar_productos,
            fg_color="#FEE3D0",
            corner_radius=20,
            border_width=2,
            border_color="#D8B59D"
        )
        frame.grid(
            row=self.contador_filas_carrito,
            column=0,
            padx=10,
            pady=5,
            sticky="we"
        )
        frame.grid_columnconfigure(0, weight=1)

        # cantidad ligada a este producto
        cantidad_var = ctk.IntVar(value=1)

        # Nombre del producto
        lbl_nombre = ctk.CTkLabel(
            frame,
            text=nombre,
            font=("Mochiy Pop One", 20),
            text_color="#7A5230"
        )
        lbl_nombre.grid(row=0, column=0, padx=15, pady=10, sticky="w")

        # Botón menos
        btn_minus = ctk.CTkButton(
            frame,
            text="",
            image=self.icon_minus,
            width=30,
            fg_color="transparent",
            hover_color="#F0C8A8",
            command=lambda n=nombre: self.decrementar(n)
        )
        btn_minus.grid(row=0, column=1, padx=5)

        # Cantidad
        lbl_cantidad = ctk.CTkLabel(
            frame,
            textvariable=cantidad_var,
            font=("Mochiy Pop One", 20),
            text_color="#7A5230"
        )
        lbl_cantidad.grid(row=0, column=2, padx=5)

        # Botón más
        btn_plus = ctk.CTkButton(
            frame,
            text="",
            image=self.icon_plus,
            width=30,
            fg_color="transparent",
            hover_color="#F0C8A8",
            command=lambda n=nombre: self.incrementar(n)
        )
        btn_plus.grid(row=0, column=3, padx=5)

        # Botón eliminar
        btn_delete = ctk.CTkButton(
            frame,
            text="",
            image=self.icon_delete,
            width=30,
            fg_color="transparent",
            hover_color="#F2A3A3",
            command=lambda n=nombre: self.eliminar_item(n)
        )
        btn_delete.grid(row=0, column=4, padx=10)

        # Guardar referencia de este producto
        self.carrito_items[nombre] = {
            "frame": frame,
            "cantidad": cantidad_var,
            "precio": precio
        }

        self.contador_filas_carrito += 1
        self.actualizar_total()
        self.actualizar_estado_botones_productos()

    def incrementar(self, nombre):
        item = self.carrito_items[nombre]
        item["cantidad"].set(item["cantidad"].get() + 1)
        self.actualizar_total()

    def decrementar(self, nombre):
        item = self.carrito_items[nombre]
        nueva = item["cantidad"].get() - 1

        if nueva <= 0:
            self.eliminar_item(nombre)
        else:
            item["cantidad"].set(nueva)
            self.actualizar_total()

    def eliminar_item(self, nombre):
        if nombre in self.carrito_items:
            self.carrito_items[nombre]["frame"].destroy()
            del self.carrito_items[nombre]
        
        self.reordenar_filas()
        self.actualizar_total()
        self.actualizar_estado_botones_productos()

    def reordenar_filas(self):
        # Reacomoda los frames del carrito después de borrar alguno.
        self.contador_filas_carrito = 0
        for item in self.carrito_items.values():
            item["frame"].grid_configure(row=self.contador_filas_carrito)
            self.contador_filas_carrito += 1

    def actualizar_total(self):
        total = 0.0
        for item in self.carrito_items.values():
            total += item["precio"] * item["cantidad"].get()

        self.total_var.set(f"${total:.2f}")

    def label_nueva_venta(self):
        lbl_nueva_venta = ctk.CTkLabel(
            self,
            text="Nueva Venta",
            font=("Mochiy Pop One", 36, "bold"),
            text_color="#7A5230"
        )
        lbl_nueva_venta.grid(
            row=1,
            column=0,
            sticky="wns",
            padx=(120, 0)
        )

    def crear_sidebar(self):
        self.sidebar = Sidebar(self, on_nav=self.navegar)
        self.sidebar.place(x=0, y=0, relheight=1)

        # Activar “detector” de click fuera
        self.bind("<Button-1>", self._click_fuera_sidebar)

    def navegar(self, destino: str):
        self.parent_navegar(destino)
    
    def _click_fuera_sidebar(self, event):
        SIDEBAR_WIDTH = 260
        # Si X es mayor al ancho de la sidebar, significa que tocó fuera
        if event.x > SIDEBAR_WIDTH:
            self.cerrar_sidebar()

    def cerrar_sidebar(self):
        
        self.sidebar.destroy()
        del self.sidebar

        # Quitamos el bind para que ya no esté escuchando clicks todo el tiempo
        self.unbind("<Button-1>")
    
    def cargar_mapa_productos(self):
        # Consulta la BD y mapea los nombres de botones a IDs reales
        try:
            lista_productos_bd = self.controlador.obtener_lista_productos()
            
            if not lista_productos_bd:
                print("No se encontraron productos en la BD")
                return
            
            for prod in lista_productos_bd:
                # Estructura asumiendo (id, nombre, tamano, precio)
                id_bd = prod[0]
                nombre_bd = prod[1]
                self.mapa_productos_ids[nombre_bd] = id_bd
            
            print(f"Productos cargados: {self.mapa_productos_ids}")
        except Exception as e:
            messagebox.showerror("Error", f"Error cargando productos: {e}")

    def actualizar_estado_botones_productos(self):
        # Si el carrito está vacío, habilitamos todos los botones
        if not self.carrito_items:
            # Habilitar todos los botones
            for btn in self.lista_botones_productos:
                btn.configure(state="normal")
            return
        
        # Si hay algo, obtenemos el nombre del producto que ya está en venta
        # (Como solo permitimos uno, tomamos la primera llave del diccionario)
        producto_activo = list(self.carrito_items.keys())[0]

        for btn in self.lista_botones_productos:
            # Si el texto del botón coincide con el producto activo, lo dejamos en estado normal
            if btn.cget("text") == producto_activo:
                btn.configure(state="normal")
            else:
                btn.configure(state="disabled")

    def guardar_ventas(self):
        # Envía la venta al controlador para guardarla en la BD
        # Validar que haya productos
        if not self.carrito_items:
            messagebox.showwarning("Carrito vacío", "No hay productos para guardar")
            return
        
        # Obtener datos del carrito
        nombre_producto_boton = list(self.carrito_items.keys())[0]
        datos_item = self.carrito_items[nombre_producto_boton]

        cantidad = datos_item["cantidad"].get()
        precio = datos_item["precio"]

        # Buscar el ID real
        id_producto_real = self.mapa_productos_ids.get(nombre_producto_boton)

        if id_producto_real is None:
            messagebox.showerror(
                "Error de datos",
                f"El producto '{nombre_producto_boton}' no coincide con la base de datos."
            )
            return
        
        id_usuario_actual = self.interface.id_usuario
        lista_para_guardar = [
            {
                "id_producto": id_producto_real,
                "cantidad": cantidad,
                "precio": precio
            }
        ]

        exito = self.controlador.registrar_venta(id_usuario_actual, lista_para_guardar)

        if exito:
            messagebox.showinfo("Exito", "Venta registrada correctamente")
            self.limpiar_todo_el_carrito()
        else:
            messagebox.showerror("Error", "No se pudo guardar la venta en la base de datos")
    
    def limpiar_todo_el_carrito(self):
        # Borra todo el contenido visual y lógico del carrito.
        items = list(self.carrito_items.keys())
        for i in items:
            self.eliminar_item(i)