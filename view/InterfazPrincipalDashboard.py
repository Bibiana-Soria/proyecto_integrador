import customtkinter as ctk
import os
from PIL import Image
from view.SideBar import Sidebar
from view.InterfazNuevaVenta import NuevaVenta
from view.InterfazHistorialDeVentas import Historial_de_ventas
from view.InterfazGastos import interfaz_de_gastos
from view.InterfazInsumos import interfaz_de_insumos
from view.InterfazProductos import interfaz_de_productos
from controller.controlador_dashboard import ControladorDashboard
from controller.controlador_reportes import ControladorReportes

class MainInterface(ctk.CTkFrame):
    def __init__(self, interface, usuario_logueado=None):
        super().__init__(interface, fg_color="#FFF9F3")
        self.interface = interface
        self.usuario_logueado = usuario_logueado
        self.id_usuario=usuario_logueado[0] if usuario_logueado else None
        self.controlador=ControladorDashboard()
        self.controlador_reportes = ControladorReportes()
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.Menu_Principal()
        
    def Menu_Principal(self):
        self.configurar_ventana()
        self.configurar_grid_principal()
        self.sidebar = Sidebar(self, on_nav=self.navegar)
        self.cargar_fuentes()
        
        self.crear_parte_superior()
        self.crear_parte_media_y_baja()
        self.crear_listados_inferiores()

    def configurar_ventana(self):
        self.interface.title("Kunibo - Dashboard")

    def configurar_grid_principal(self):
        self.grid_rowconfigure(0, weight=0) 
        self.grid_rowconfigure(1, weight=1) 
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def cargar_fuentes(self):
        font_path_Mochiy = os.path.join(self.base_path, "fonts", "MochiyPopOne-Regular.ttf")
        font_path_Poppins = os.path.join(self.base_path, "fonts", "Poppins-Regular.ttf")
        ctk.FontManager.load_font(font_path_Mochiy)
        ctk.FontManager.load_font(font_path_Poppins)

    def crear_parte_superior(self):
        datos=self.controlador.obtener_resumen_global(self.id_usuario)
        self.ingresos_totales = datos["ingresos_totales"]
        self.ventas_realizadas = datos["ventas_realizadas"]
        self.alertas_stock = datos["alertas_stock"]
        self.gastos_totales = datos["gastos_totales"]
        self.ganancia_neta = datos["ganancia_neta"]
        
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

        self.frame_superior_dashboard.grid_columnconfigure(0, weight=0)  
        self.frame_superior_dashboard.grid_columnconfigure(1, weight=0)  
        self.frame_superior_dashboard.grid_columnconfigure(2, weight=1)  
        self.frame_superior_dashboard.grid_columnconfigure(3, weight=1) 
        self.frame_superior_dashboard.grid_columnconfigure(4, weight=1) 
        self.frame_superior_dashboard.grid_rowconfigure(0, weight=1) 

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
            text="Sales Control Panel",
            font=("Poppins", 20),
            text_color="#C49A85"
        )
        lbl_bienvenida.grid(
            row=0,
            column=0,
            sticky="w"
        )

        nombre_a_mostrar = "Usuario"
        if self.usuario_logueado:
            try:
                nombre_a_mostrar = self.usuario_logueado[1]
            except IndexError:
                nombre_a_mostrar = str(self.usuario_logueado[0])

        lbl_saludo = ctk.CTkLabel(
            frame_bienvenida,
            text=f"Welcome\n{nombre_a_mostrar}",
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
            text="Monthly Sales",
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
            text="Monthly Earnings",
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
            text=f"${self.ganancia_neta:,.2f}",
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
            text="Monthly Expenses",
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

    def crear_parte_media_y_baja(self):
        pass

    def navegar(self, destino: str):
        if destino == "Main Dashboard":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Dashboard")
            self.Menu_Principal()

        elif destino == "New Sale":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - New Sale")

            self.nueva_venta = NuevaVenta(
            interface=self,    
            parent_navegar=self.navegar
        )
            self.nueva_venta.pack(fill="both", expand=True)

        elif destino == "Sales History":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Sales History")
            self.historial_de_ventas = Historial_de_ventas(
                interface=self,
                parent_navegar=self.navegar,
                ventana_principal = self.interface

            )
            self.historial_de_ventas.pack(fill="both" ,expand = True)

        elif destino == "Expenses":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Expenses")
            self.historial_de_ventas = interfaz_de_gastos(
                interface=self,
                parent_navegar=self.navegar,
                ventana_principal = self.interface,
                id_usuario=self.id_usuario
            )
            self.historial_de_ventas.pack(fill="both" ,expand = True)

        elif destino == "Supplies":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Supplies")
            self.historial_de_ventas = interfaz_de_insumos(
                interface=self,
                parent_navegar=self.navegar,
                ventana_principal = self.interface,
                id_usuario=self.id_usuario

            )
            self.historial_de_ventas.pack(fill="both" ,expand = True)

        elif destino == "Products":
            for widget in self.winfo_children():
                widget.destroy()
            self.interface.title("Kunibo - Products")
            self.historial_de_ventas = interfaz_de_productos(
                interface=self,
                parent_navegar=self.navegar,
                ventana_principal = self.interface

            )
            self.historial_de_ventas.pack(fill="both" ,expand = True)

        elif destino == "Products":
             pass

        elif destino == "Logout":
            self.destroy()
            try:
                self.interface.restaurar_login()
            except AttributeError:
                print("Error: No se pudo restaurar el login en la ventana padre.")

    def crear_listados_inferiores(self):
        frame_listas = ctk.CTkFrame(self, fg_color="#FFF9F3")
        frame_listas.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=20, pady=(20, 5))

        frame_listas.grid_columnconfigure(0, weight=1)
        frame_listas.grid_columnconfigure(1, weight=1)
        frame_listas.grid_rowconfigure(0, weight=1)
        frame_ventas = ctk.CTkFrame(frame_listas, fg_color="#FEE3D0",
                                    border_width=4, border_color="#D8B59D",
                                    corner_radius=30)
        frame_ventas.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        lbl_v = ctk.CTkLabel(frame_ventas, text="Recent Sales",
                            font=("Mochiy Pop One", 22), text_color="#7A5230")
        lbl_v.pack(pady=10)

        ultimas_ventas = self.controlador.obtener_ultimas_ventas(self.id_usuario)

        if not ultimas_ventas:
            ctk.CTkLabel(frame_ventas, text="No recent sales",
                        font=("Poppins", 16)).pack(pady=10)
        else:
            for venta in ultimas_ventas:
                id_venta, id_producto, fecha, cant, precio_u, total = venta
                texto = f"{fecha}  |  ${total}"
                ctk.CTkLabel(frame_ventas, text=texto,
                            font=("Poppins", 16), text_color="#7A5230").pack(pady=3)

        frame_egresos = ctk.CTkFrame(frame_listas, fg_color="#FEE3D0",
                                    border_width=4, border_color="#D8B59D",
                                    corner_radius=30)
        frame_egresos.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        lbl_g = ctk.CTkLabel(frame_egresos, text="Recent Expenses",
                            font=("Mochiy Pop One", 22), text_color="#7A5230")
        lbl_g.pack(pady=10)

        ultimos_egresos = self.controlador.obtener_ultimos_egresos(self.id_usuario)

        if not ultimos_egresos:
            ctk.CTkLabel(frame_egresos, text="No recent expenses",
                        font=("Poppins", 16)).pack(pady=10)
        else:
            for egreso in ultimos_egresos:
                id_e, id_i, id_u, prov, desc, monto, cant, fecha = egreso
                texto = f"{fecha}  |  ${monto}"
                ctk.CTkLabel(frame_egresos, text=texto,
                            font=("Poppins", 16), text_color="#7A5230").pack(pady=3)

        frame_botones = ctk.CTkFrame(self, fg_color="#FFF9F3")
        frame_botones.grid(row=2, column=0, columnspan=2, pady=(5, 20), padx=20, sticky="ew")

        frame_botones.grid_columnconfigure(0, weight=1)
        frame_botones.grid_columnconfigure(1, weight=1)
        frame_botones.grid_rowconfigure(0, weight=1)
        frame_botones.grid_rowconfigure(1, weight=1)

        btn_exportar_ventas = ctk.CTkButton(
            frame_botones,
            text="Export Sales Report",
            height=60,
            fg_color="#C49A85",
            hover_color="#A67C65",
            font=("Poppins", 18, "bold"),
            corner_radius=20,
            command=lambda: self.controlador_reportes.exportar_ventas(self.id_usuario)
        )
        btn_exportar_ventas.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        btn_exportar_gastos = ctk.CTkButton(
            frame_botones,
            text="Export Expenses Report",
            height=60,
            fg_color="#C49A85",
            hover_color="#A67C65",
            font=("Poppins", 18, "bold"),
            corner_radius=20,
            command=self.controlador_reportes.exportar_egresos
        )
        btn_exportar_gastos.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

        btn_exportar_insumos = ctk.CTkButton(
            frame_botones,
            text="Export Supplies Report",
            height=60,
            fg_color="#C49A85",
            hover_color="#A67C65",
            font=("Poppins", 18, "bold"),
            corner_radius=20,
            command=self.controlador_reportes.exportar_insumos
        )
        btn_exportar_insumos.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        btn_exportar_productos = ctk.CTkButton(
            frame_botones,
            text="Export Products Report",
            height=60,
            fg_color="#C49A85",
            hover_color="#A67C65",
            font=("Poppins", 18, "bold"),
            corner_radius=20,
            command=self.controlador_reportes.exportar_productos
        )
        btn_exportar_productos.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

    def crear_sidebar(self):
        self.sidebar = Sidebar(self, on_nav=self.navegar)
        self.sidebar.place(x=0, y=0, relheight=1)

        self.interface.bind_all("<Button-1>", self._click_fuera_sidebar)
    
    def _click_fuera_sidebar(self, event):
        SIDEBAR_WIDTH = 260
        if event.x > SIDEBAR_WIDTH:
            self.cerrar_sidebar()

    def cerrar_sidebar(self):
        self.sidebar.destroy()
        del self.sidebar
        self.interface.unbind_all("<Button-1>")
