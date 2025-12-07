from conexionBD import *

class Egresos:
    @staticmethod
    def insertar(id_insumo, proveedor, descripcion, monto, cantidad_comprada, id_usuario):
        try:
            # Validar que el insumo exista
            cursor.execute("SELECT id_insumo FROM insumos WHERE id_insumo=%s", (id_insumo,))
            resultado = cursor.fetchone()

            if not resultado:
                print("ERROR: El insumo no existe")
                return False

            # Agregamos id_usuario a la consulta SQL
            sql = """
                INSERT INTO egresos
                (id_insumo, proveedor, descripcion, monto, cantidad_comprada, fecha, id_usuario)
                VALUES (%s, %s, %s, %s, %s, NOW(), %s)
            """

            cursor.execute(sql, (id_insumo, proveedor, descripcion, monto, cantidad_comprada, id_usuario))
            conexion.commit()

            return True

        except Exception as e:
            print("ERROR insertar egreso:", e)
            return False
 
    @staticmethod
    # Agregamos el parametro id_usuario para filtrar
    def consultar(id_usuario):
        try:
            # Filtramos con WHERE id_usuario
            cursor.execute(
                "select * from egresos where id_usuario = %s", (id_usuario,))
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
        