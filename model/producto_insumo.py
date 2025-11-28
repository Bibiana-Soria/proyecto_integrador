from conexionBD import *

class producto_insumo:
    @staticmethod
    def insertar(id_producto,id_insumo,cantidad):
        try:
            cursor.execute(
                "insert into producto_insumo values (%s,%s,%s)",
                (id_producto,id_insumo,cantidad)
            )
            cursor.execute(
                "UPDATE insumos SET cantidad = cantidad - %s WHERE id_insumo = %s",
                (cantidad, id_insumo)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from producto_insumo")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def cambiar(id_producto, id_insumo, cantidad, id):
        try:
            cursor.execute(
                "update producto_insumo set id_producto=%s,id_insumo=%s,cantidad=%s where id=%s",
                (id_producto, id_insumo, cantidad, id)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "delete from producto_insumo where id_=%s",
                (id,)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def buscar(id):
        try:
            cursor.execute(
                "select * from producto_insumo where id=%s"
                (id,)
            )
            conexion.commit()
            return True
        except:
            return False
        