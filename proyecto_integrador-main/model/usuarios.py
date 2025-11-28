from conexionBD import *

class Usuarios:
    @staticmethod
    def insertar(nombre, apellido, email, contrasena):
        try:
            cursor.execute(
                "insert into usuarios (nombre, apellido, email, contrasena) values (%s,%s,%s,%s)",
                (nombre, apellido, email, contrasena)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute("select * from usuarios")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def cambiar(nombre, apellido, email, contrasena, id_usuario):
        try:
            # CORRECCIÓN: Faltaba setear contrasena en el SQL y el WHERE estaba confuso
            cursor.execute(
                "update usuarios set nombre=%s, apellido=%s, email=%s, contrasena=%s where id_usuario=%s",
                (nombre, apellido, email, contrasena, id_usuario)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id_usuario):
        try:
            cursor.execute("delete from usuarios where id_usuario=%s", (id_usuario,))
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def buscar(nombre):
        try:
            # CORRECCIÓN: Sintaxis de LIKE corregida
            cursor.execute(
                "select * from usuarios where nombre like %s",
                ('%' + nombre + '%',)
            )
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def validar(email, password):
        try:
            # CORRECCIÓN: Validamos por EMAIL
            cursor.execute(
                "select * from usuarios where email = %s and contrasena = %s",
                (email, password)
            )
            datos = cursor.fetchone()
            return datos
        except:
            return None