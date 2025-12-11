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
            print(f"ERROR en insertar producto: {e}")
            import traceback
            traceback.print_exc()
            return False
            
    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM productos")
            return cursor.fetchall()
        except Exception as e:
            print(f"ERROR en consultar productos: {e}")
            return []
        
    @staticmethod
    def cambiar(nombre, tamano, precio, id_producto):
        try:
            print(f"MODELO - cambiar() llamado")
            print(f"  nombre: '{nombre}'")
            print(f"  tamano: '{tamano}'")
            print(f"  precio: {precio}")
            print(f"  id_producto: {id_producto}")
            
            cursor.execute("SELECT id_producto FROM productos WHERE id_producto=%s", (id_producto,))
            existe = cursor.fetchone()
            print(f"MODELO - ¿Producto existe? {existe}")
            
            if not existe:
                print(f"ERROR: Producto con id {id_producto} no existe en la base de datos")
                return False
            
            # Ejecutar UPDATE
            print(f"MODELO - Ejecutando UPDATE...")
            cursor.execute(
                "UPDATE productos SET nombre=%s, tamano=%s, precio=%s WHERE id_producto=%s",
                (nombre, tamano, precio, id_producto)
            )
            
            filas_afectadas = cursor.rowcount
            print(f"MODELO - Filas afectadas: {filas_afectadas}")
            
            conexion.commit()
            print(f"MODELO - Commit exitoso")
            
            return True
            
        except Exception as e:
            print(f"ERROR COMPLETO en modelo cambiar:")
            import traceback
            traceback.print_exc()
            try:
                conexion.rollback()
            except:
                pass
            return False
        
    @staticmethod
    def eliminar(id_producto):
        try:
            cursor.execute(
                "SELECT COUNT(*) FROM ventas WHERE id_producto=%s",
                (id_producto,)
            )
            cantidad_ventas = cursor.fetchone()[0]
            
            if cantidad_ventas > 0:
                from tkinter import messagebox
                confirmacion = messagebox.askyesno(
                    "Warning",
                    f"This product has {cantidad_ventas} associated sale(s).\n\n"
                    f"Deleting this product will also delete all its sales records.\n\n"
                    f"Are you sure you want to continue?"
                )
                
                if not confirmacion:
                    print("Usuario canceló la eliminación")
                    return False

            cursor.execute(
                "DELETE FROM productos WHERE id_producto=%s",
                (id_producto,)
            )
            conexion.commit()
            
            if cantidad_ventas > 0:
                print(f"Producto eliminado junto con {cantidad_ventas} venta(s)")
            else:
                print("Producto eliminado sin ventas asociadas")
            
            return True
            
        except Exception as e:
            print(f"ERROR en eliminar producto: {e}")
            import traceback
            traceback.print_exc()
            try:
                conexion.rollback()
            except:
                pass
            return False
        
    @staticmethod
    def buscar(nombre):
        try:
            cursor.execute(
                "SELECT id_producto, nombre, tamano, precio FROM productos WHERE nombre LIKE %s",
                ("%" + nombre + "%",)
            )
            return cursor.fetchall()
        except Exception as e:
            print(f"ERROR en buscar producto: {e}")
            return []