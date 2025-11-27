from conexionBD import *

class Ventas:
    @staticmethod
    def insertar(id_usuario,id_producto,cantidad,precio_unitario,total):
        try:
            cursor.execute(
                "insert into ventas values (%s,%s,NOW(),%s,%s,%s)",
                (id_usuario,id_producto,cantidad,precio_unitario,total)
            )
            conexion.commit()
            return True
        except:
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
            cursor.execute(
                "select * from ventas where fecha_venta like '$%s$'"
                (fecha_venta,)
            )
            conexion.commit()
            return True
        except:
            return False
        