import customtkinter as ctk
import os
from PIL import Image
from view.InterfazPrincipalDashboard import MainInterface
from view.InterfazUsuarios  import Usuarios
from tkinter import messagebox
from view.InterfazPrincipalDashboard import MainInterface
from view.InterfazUsuarios  import Usuarios
from controller.controlador_logueo import ControladorLogueo # Importar el controlador

class LoginInterface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.controlador = ControladorLogueo()

        # Rutas base
        self.base_path = os.path.dirname(os.path.abspath(__file__))

        self.configurar_ventana()
        self.configurar_grid_principal()
        self.cargar_icono()
        self.crear_frame_superior()
        self.crear_frame_inferior()
        self.crear_contenido_superior()
        self.crear_contenido_inferior()

        # tamaño y estado
        self.minsize(800, 600)
        self.after(10, lambda: self.state("zoomed"))

    # --- Configuración general ---

    def configurar_ventana(self):
        self.title("Kunibo")
        self.resizable(False, False)
        self.configure(fg_color="#FFF9F3")

    def configurar_grid_principal(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def cargar_icono(self):
        icon_path = os.path.join(self.base_path, "images", "kunibo_icon.ico")
        self.iconbitmap(icon_path)

    # --- Frames principales ---

    def crear_frame_superior(self):
        self.frame_superior = ctk.CTkFrame(
            self,
            fg_color="#FFF9F3"
        )
        self.frame_superior.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        self.frame_superior.grid_columnconfigure(0, weight=1)
        self.frame_superior.grid_rowconfigure(0, weight=1)
        self.frame_superior.grid_propagate(False)

    def crear_frame_inferior(self):
        self.frame_inferior = ctk.CTkFrame(
            self,
            fg_color="#FFF9F3"
        )
        self.frame_inferior.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew"
        )
        self.frame_inferior.grid_propagate(False)

        # grid interno (parte de abajo)
        self.frame_inferior.grid_rowconfigure(0, weight=0)
        self.frame_inferior.grid_rowconfigure(1, weight=0)
        self.frame_inferior.grid_rowconfigure(2, weight=0)
        self.frame_inferior.grid_rowconfigure(3, weight=0)
        self.frame_inferior.grid_rowconfigure(4, weight=0)
        self.frame_inferior.grid_rowconfigure(5, weight=0)
        self.frame_inferior.grid_rowconfigure(6, weight=1)
        self.frame_inferior.grid_columnconfigure(0, weight=1)
        self.frame_inferior.grid_columnconfigure(1, weight=0)
        self.frame_inferior.grid_columnconfigure(2, weight=1)

    # --- Contenido superior (logo) ---

    def crear_contenido_superior(self):
        logo_path = os.path.join(self.base_path, "images", "Login_logo.png")
        img = Image.open(logo_path)

        self.logo_image = ctk.CTkImage(
            light_image=img,
            dark_image=img,
            size=(450, 450)
        )

        logo_label = ctk.CTkLabel(
            self.frame_superior,
            text="",
            image=self.logo_image
        )
        logo_label.grid(
            row=0,
            column=0,
            sticky="nsew",
            pady=(35, 0)
        )

    # --- Contenido inferior (login) ---

    def crear_contenido_inferior(self):
        self._crear_email()
        self._crear_password()
        self._crear_boton_ventana_emergente_usuarios()
        self._crear_boton_login()

    def _crear_email(self):
        email_label = ctk.CTkLabel(
            self.frame_inferior,
            text="E-mail",
            font=("Segoe UI", 19, "bold"),
            text_color="#111111"
        )
        email_label.grid(
            row=0,
            column=1,
            sticky="sw",
            pady=(80, 5)
        )

        self.email_entry = ctk.CTkEntry(
            self.frame_inferior,
            width=360,
            height=40,
            corner_radius=20,
            fg_color="#FEF3E7",
            border_color="#000000",
            border_width=2,
            placeholder_text="example@kunibo.com",
            placeholder_text_color="#111111"
        )
        self.email_entry.grid(
            row=1,
            column=1,
            pady=(0, 10)
        )

    def _crear_password(self):
        password_label = ctk.CTkLabel(
            self.frame_inferior,
            text="Password",
            font=("Segoe UI", 18, "bold"),
            text_color="#111111"
        )
        password_label.grid(
            row=3,
            column=1,
            sticky="sw",
            pady=(10, 5)
        )

        self.password_entry = ctk.CTkEntry(
            self.frame_inferior,
            width=360,
            height=40,
            corner_radius=20,
            fg_color="#FEF3E7",
            border_color="#000000",
            border_width=2,
            show="*"
        )
        self.password_entry.grid(
            row=4,
            column=1,
            pady=(0, 20)
        )

    def _crear_boton_ventana_emergente_usuarios(self):
        btn_crear_nuevo_usuario = ctk.CTkButton(
            self.frame_inferior,
            text="Crear un nuevo usuario",
            fg_color="#FFF9F3",
            hover_color="#FFF9F3",
            text_color="#171616",
            font=("Segoe UI", 16, "bold"),
            command= lambda: self._crear_ventana_emergente_agregar_usuarios()
        )
        btn_crear_nuevo_usuario.grid(
            row=5,
            column=1,
            pady=(0, 10)
        )

    def _crear_ventana_emergente_agregar_usuarios(self):
        ventana_emergente = Usuarios(self)


    def _crear_boton_login(self):
        login_button = ctk.CTkButton(
            self.frame_inferior,
            text="LOGIN",
            width=180,
            height=40,
            corner_radius=20,
            fg_color="#111111",
            hover_color="#333333",
            text_color="#FFFFFF",
            font=("Segoe UI", 16, "bold"),
            command=self.realizar_login
        )
        login_button.grid(
            row=6,
            column=1,
            pady=(0, 60)
        )

    def realizar_login(self):
        # 1. Obtener datos
        email = self.email_entry.get()
        password = self.password_entry.get()

        # 2. Validar con el controlador
        datos_usuario = self.controlador.validar_login(email, password)

        if datos_usuario:
            # Login exitoso
            self.switch_to_main()
        else:
            # Login fallido
            messagebox.showerror("Error de acceso", "E-mail o contraseña incorrectos")
            
    # --- Cambio a dashboard ---

    def switch_to_main(self):
        # destruir todo lo actual (login)
        for widget in self.winfo_children():
            widget.destroy()
        self.main_interface = MainInterface(self)
        self.main_interface.pack(fill="both", expand=True)



