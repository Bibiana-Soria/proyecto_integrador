import customtkinter as ctk


class Usuarios():
    def __init__(self, root):
        self.root = root 
        self.campos = ["ID", "Nombre", "Apellido", "Email", "Contraseña"]
        self.informacion_obtenida = {}
        self.crear_ventana_creacion_de_usuarios()

    def crear_ventana_creacion_de_usuarios(self):
        ventana_emergente_crear_usuario = ctk.CTkToplevel(
            fg_color="#FFF9F3"
        )
        ventana_emergente_crear_usuario.title("Kunibo - Agregar Usuario")
        ventana_emergente_crear_usuario.geometry("700x500")
        ventana_emergente_crear_usuario.lift()
        ventana_emergente_crear_usuario.focus()
        ventana_emergente_crear_usuario.grab_set()
        # Layout básico
        ventana_emergente_crear_usuario.grid_columnconfigure(0, weight=1)
        ventana_emergente_crear_usuario.grid_rowconfigure(0, weight=0)
        ventana_emergente_crear_usuario.grid_rowconfigure(1, weight=1)
        ventana_emergente_crear_usuario.grid_rowconfigure(2, weight=0)

        info_obtenida = {}

        lbl_titulo = ctk.CTkLabel(
            ventana_emergente_crear_usuario,
            text=f"Agregar usuario",
            font=("Mochiy Pop One", 24),
            text_color="#7A5230"
        )
        lbl_titulo.grid(row=0, column=0, pady=(20, 10), padx=20, sticky="n")

        frame_para_entries = ctk.CTkScrollableFrame(ventana_emergente_crear_usuario,
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
        
        frame_botones = ctk.CTkFrame(ventana_emergente_crear_usuario, fg_color="transparent")
        frame_botones.grid(row=2, column=0, pady=15)

        def guardar():
            self.informacion_obtenida = info_obtenida
            ventana_emergente_crear_usuario.destroy()

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
            command=ventana_emergente_crear_usuario.destroy
        )
        btn_cancelar.grid(row=0, column=1, padx=10)

