from conexionBD import *

class Egresos:
    @staticmethod
    def insertar(id_insumo, proveedor, descripcion, monto, cantidad_comprada, id_usuario):
        try:
            cursor.execute("SELECT id_insumo FROM insumos WHERE id_insumo=%s", (id_insumo,))
            resultado = cursor.fetchone()

            if not resultado:
                print("ERROR: El insumo no existe")
                return False

            sql = """
                INSERT INTO egresos
                (id_insumo, proveedor, descripcion, monto, cantidad_comprada, fecha)
                VALUES (%s, %s, %s, %s, %s, NOW())
            """

            cursor.execute(sql, (id_insumo, proveedor, descripcion, monto, cantidad_comprada))
            conexion.commit()

            return True

        except Exception as e:
            print("ERROR insertar egreso:", e)
            return False
 
    @staticmethod
    def consultar(id_usuario):
        try:
            cursor.execute("SELECT * FROM egresos")
            return cursor.fetchall()
        except Exception as e:
            print("ERROR consultar:", e)
            return []
        
    @staticmethod
    def cambiar(id_insumo, proveedor, descripcion, monto, cantidad_comprada, id_egreso):
        try:
            cursor.execute(
                "UPDATE egresos SET id_insumo=%s, proveedor=%s, descripcion=%s, monto=%s, cantidad_comprada=%s, fecha=NOW() WHERE id_egreso=%s",
                (id_insumo, proveedor, descripcion, monto, cantidad_comprada, id_egreso)
            )
            conexion.commit()
            return True
        except Exception as e:
            print("ERROR cambiar:", e)
            return False
        
    @staticmethod
    def eliminar(id_egreso):
        try:
            cursor.execute(
                "DELETE FROM egresos WHERE id_egreso=%s",
                (id_egreso,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print("ERROR eliminar:", e)
            return False
        
    @staticmethod
    def buscar(proveedor):
        try:
            cursor.execute(
                "SELECT * FROM egresos WHERE proveedor LIKE %s",
                ("%" + proveedor + "%",)
            )
            return cursor.fetchall()
        except Exception as e:
            print("ERROR buscar:", e)
            return []