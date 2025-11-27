from conexionBD import *

class Productos:
    @staticmethod
    def insertar(nombre,tamano,precio):
        try:
            cursor.execute(
                "insert into productos values (%s,%s,%s,%s)",
                (nombre,tamano,precio)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from productos")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def cambiar(nombre,tamano,precio, id_producto):
        try:
            cursor.execute(
                "update productos set nombre=%s,tamano=%s,precio=%s where id_producto=%s",
                (nombre,tamano,precio, id_producto)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id_producto):
        try:
            cursor.execute(
                "delete from productos where id_producto=%s",
                (id_producto,)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def buscar(nombre):
        try:
            cursor.execute(
                "select * from productos where nombre like '$%s$'"
                (nombre,)
            )
            conexion.commit()
            return True
        except:
            return False
        