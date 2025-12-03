from conexionBD import *

class Productos:
    @staticmethod
    def insertar(nombre, tamano, precio):
        try:
            cursor.execute(
                "INSERT INTO productos (nombre, tamano, precio) VALUES (%s, %s, %s)",
                (nombre, tamano, precio)
            )
            conexion.commit()
            return True
        except Exception as e:
            print("Error en insertar:", e)
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
    def buscar(id_producto):
        try:
            cursor.execute(
                "SELECT id_producto, nombre, tamano, precio FROM productos WHERE id_producto = %s",
                (id_producto,)
            )
            conexion.commit()
            return True
        except:
            return False
        