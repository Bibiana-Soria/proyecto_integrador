from conexionBD import *

class Usuarios:
    @staticmethod
    def insertar(nombre,apellido,email,contrasena):
        try:
            cursor.execute(
                "insert into usuarios values (%s,%s,%s,%s)",
                (nombre,apellido,email,contrasena)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from usuarios")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def cambiar(nombre,apellido,email,contrasena,id_usuario):
        try:
            cursor.execute(
                "update usuarios set nombre=%s,apellido=%s,email=%s where id_usuario=%s",
                (nombre,apellido,email,contrasena, id_usuario)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id_usuario):
        try:
            cursor.execute(
                "delete from usuarios where id_usuario=%s",
                (id_usuario,)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def buscar(nombre,apellido):
        try:
            cursor.execute(
                "select * from usuarios where nombre and apellido like '$%s$'"
                (nombre,apellido)
            )
            conexion.commit()
            return True
        except:
            return False
        