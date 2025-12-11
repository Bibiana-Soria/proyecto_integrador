from conexionBD import *

class Ventas:
    @staticmethod
    def insertar(id_usuario, id_producto, cantidad, precio_unitario, total=None):
        try:
            cursor.execute(
                "INSERT INTO ventas (id_usuario, id_producto, fecha_venta, cantidad, precio_unitario) VALUES (%s, %s, NOW(), %s, %s)",
                (id_usuario, id_producto, cantidad, precio_unitario)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error SQL: {e}")
            return False
        
    @staticmethod
    def consultar(id_usuario):
        try:
            cursor.execute(
                "select id_venta, id_producto, fecha_venta, cantidad, precio_unitario, total from ventas where id_usuario = %s", (id_usuario,)
                )
            return cursor.fetchall()
        except Exception as e:
            print(f"Error consultando ventas: {e}")
            return []
        
    @staticmethod
    def cambiar(id_usuario, id_producto, cantidad, precio_unitario, id_venta):
        try:
            # NO incluimos 'total' porque es una columna generada automáticamente
            cursor.execute(
                "UPDATE ventas SET id_usuario=%s, id_producto=%s, cantidad=%s, precio_unitario=%s WHERE id_venta=%s",
                (id_usuario, id_producto, cantidad, precio_unitario, id_venta)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error en cambiar(): {e}")
            import traceback
            traceback.print_exc()
            return False
        
    @staticmethod
    def eliminar(id_venta):
        try:
            cursor.execute(
                "delete from ventas where id_venta=%s",
                (id_venta,)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def buscar(fecha_venta):
        try:
            cursor.execute(
                "select * from ventas where fecha_venta like %s",
                ('%' + fecha_venta + '%',) 
            )
            return cursor.fetchall()
        except:
            return []
        