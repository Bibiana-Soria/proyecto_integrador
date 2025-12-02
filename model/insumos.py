from conexionBD import *

class Insumos:
    @staticmethod
    def insertar(nombre_insumo,unidad_medida,cantidad,costo_unitario,proveedor,descripcion):
        try:
            cursor.execute(
                "insert into insumos values (%s,%s,%s,%s)",
                (nombre_insumo,unidad_medida,cantidad,costo_unitario)
            )
            id_insumo=cursor.lastrowid
            monto_egreso=cantidad*costo_unitario
            
            cursor.execute(
                "insert into egresos (id_insumo, proveedor, descripcion, monto, cantidad_comprada, fecha) values (%s,%s,%s,%s,%s,NOW())",
                (id_insumo, proveedor, descripcion, monto_egreso, cantidad)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from insumos")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def cambiar(nombre_insumo,unidad_medida,cantidad,costo_unitario,id_insumo):
        try:
            cursor.execute(
                "update insumos set nombre_insumo=%s,unidad_medida=%s,cantidad=%s,costo_unitario=%s where id_insumo=%s",
                (nombre_insumo,unidad_medida,cantidad,costo_unitario,id_insumo)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id_insumo):
        try:
            cursor.execute(
                "delete from insumos where id_insumo=%s",
                (id_insumo,)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def buscar(nombre_insumo):
        try:
            cursor.execute(
                "select * from insumos where nombre_insumo=%s'"
                (nombre_insumo,)
            )
            conexion.commit()
            return True
        except:
            return False
        