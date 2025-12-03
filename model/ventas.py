from conexionBD import *

class Ventas:
    @staticmethod
    def insertar(id_usuario, id_producto, cantidad, precio_unitario, total=None):
        try:
            # CORRECCIÓN IMPORTANTE:
            # 1. Especificamos las columnas: (id_usuario, id_producto, fecha_venta, cantidad, precio_unitario)
            # 2. Ignoramos 'id_venta' (es auto-increment) y 'total' (es generado automático)
            cursor.execute(
                "INSERT INTO ventas (id_usuario, id_producto, fecha_venta, cantidad, precio_unitario) VALUES (%s, %s, NOW(), %s, %s)",
                (id_usuario, id_producto, cantidad, precio_unitario)
            )
            conexion.commit()
            return True
        except Exception as e:
            # Agregamos este print para que veas el error en la consola si falla
            print(f"Error SQL: {e}")
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from ventas")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def cambiar(id_usuario,id_producto,cantidad,precio_unitario,total,id_venta):
        try:
            cursor.execute(
                "update ventas set id_usuario=%s,id_producto=%s,cantidad=%s,precio_unitario=%s,total=%s where id_venta=%s",
                (id_usuario,id_producto,cantidad,precio_unitario,total,id_venta)
            )
            conexion.commit()
            return True
        except:
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
            # Corregido: Se agregó la coma antes de los parámetros y se ajustó el LIKE
            cursor.execute(
                "select * from ventas where fecha_venta like %s",
                ('%' + fecha_venta + '%',) 
            )
            # Corregido: Buscar debe devolver datos, no True/False
            return cursor.fetchall()
        except:
            return []
        