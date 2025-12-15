from conexionBD import *
class Insumos:

    @staticmethod
    def insertar(nombre_insumo, unidad_medida, cantidad, costo_unitario, proveedor, descripcion, id_usuario):
        try:
            cursor.execute(
                """
                INSERT INTO insumos (nombre_insumo, unidad_medida, cantidad, costo_unitario)
                VALUES (%s, %s, %s, %s)
                """,
                (nombre_insumo, unidad_medida, cantidad, costo_unitario)
            )

            cursor.execute("SELECT LAST_INSERT_ID()")
            id_insumo = cursor.fetchone()[0]

            print("ID INSUMO CREADO:", id_insumo)
            monto_egreso = float(cantidad) * float(costo_unitario)

            cursor.execute(
                """
                INSERT INTO egresos
                (id_insumo, proveedor, descripcion, monto, cantidad_comprada, fecha, id_usuario)
                VALUES (%s, %s, %s, %s, %s, NOW(), %s)
                """,
                (id_insumo, proveedor, descripcion, monto_egreso, cantidad, id_usuario)
            )

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback() 
            print("ERROR insertar insumo y egreso:", e)
            return False

    @staticmethod
    def consultar(id_usuario=None):
        try:
            cursor.execute("SELECT * FROM insumos")
            return cursor.fetchall()
        except Exception as e:
            print("ERROR consultar:", e)
            return []

    @staticmethod
    def cambiar(nombre_insumo, unidad_medida, cantidad, costo_unitario, id_insumo):
        try:
            cursor.execute(
                """
                UPDATE insumos
                SET nombre_insumo=%s, unidad_medida=%s, cantidad=%s, costo_unitario=%s
                WHERE id_insumo=%s
                """,
                (nombre_insumo, unidad_medida, cantidad, costo_unitario, id_insumo)
            )

            monto = float(cantidad) * float(costo_unitario)

            cursor.execute(
                """
                UPDATE egresos
                SET monto=%s,
                    cantidad_comprada=%s,
                    descripcion=%s
                WHERE id_insumo=%s
                """,
                (monto, cantidad, f"Actualización automática del insumo {nombre_insumo}", id_insumo)
            )

            conexion.commit()
            return True

        except Exception as e:
            print("ERROR cambiar:", e)
            return False 
        
    @staticmethod
    def eliminar(id_insumo):
        try:
            cursor.execute("DELETE FROM insumos WHERE id_insumo=%s", (id_insumo,))
            conexion.commit()
            return True
        except Exception as e:
            print("ERROR eliminar:", e)
            return False

    @staticmethod
    def buscar(nombre_insumo, id_usuario=None):
        try:
            cursor.execute(
                "SELECT * FROM insumos WHERE nombre_insumo LIKE %s",
                ("%" + nombre_insumo + "%",)
            )
            return cursor.fetchall()
        except Exception as e:
            print("ERROR buscar:", e)
            return []
        
    @staticmethod
    def ultimo_id():
        cursor.execute("SELECT LAST_INSERT_ID()")
        return cursor.fetchone()[0]