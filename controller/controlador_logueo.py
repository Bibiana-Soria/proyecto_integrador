from model.usuarios import Usuarios

class ControladorLogueo:
    def __init__(self):
        self.modelo = Usuarios()

    def validar_login(self, usuario, password):
        """
        Verifica las credenciales. 
        Retorna los datos del usuario si es correcto, o None si falla.
        """
        if not usuario or not password:
            return None
            
        return self.modelo.validar(usuario, password)
