from conexionBD import *

class Egresos:
    @staticmethod
    def insertar(id_insumo,proveedor,descripcion,monto,cantidad_comprada):
        try:
            cursor.execute(
                "insert into egresos values (%s,%s,%s,%s,%s,NOW())",
                (id_insumo,proveedor,descripcion,monto,cantidad_comprada)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
            cursor.execute(
                "select * from egresos")
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def cambiar(id_insumo,proveedor,descripcion,monto,cantidad_comprada,id_egreso):
        try:
            cursor.execute(
                "update egresos set id_insumo=%s,proveedor=%s,descripcion=%s,monto=%s,cantidad_comprada=%s,fecha=NOW() where id_egreso=%s",
                (id_insumo,proveedor,descripcion,monto,cantidad_comprada,id_egreso)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id_egreso):
        try:
            cursor.execute(
                "delete from egresos where id_egreso=%s",
                (id_egreso,)
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def buscar(proveedor):
        try:
            cursor.execute(
                "select * from egresos where proveedor like '$%s$'",
                (proveedor,)
            )
            conexion.commit()
            return True
        except:
            return False
        