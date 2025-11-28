from conexionBD import *

class Usuarios:
    @staticmethod
<<<<<<< HEAD
    def insertar(nombre,apellido,email,contrasena):
        try:
            cursor.execute(
                "insert into usuarios values (%s,%s,%s,%s)",
                (nombre,apellido,email,contrasena)
=======
    def insertar(nombre, apellido, email, contrasena):
        try:
            cursor.execute(
                "insert into usuarios (nombre, apellido, email, contrasena) values (%s,%s,%s,%s)",
                (nombre, apellido, email, contrasena)
>>>>>>> 5718117065bf8efc8fa6b8cfb2bd703f5cab660d
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def consultar():
        try:
<<<<<<< HEAD
            cursor.execute(
                "select * from usuarios")
=======
            cursor.execute("select * from usuarios")
>>>>>>> 5718117065bf8efc8fa6b8cfb2bd703f5cab660d
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
<<<<<<< HEAD
    def cambiar(nombre,apellido,email,contrasena,id_usuario):
        try:
            cursor.execute(
                "update usuarios set nombre=%s,apellido=%s,email=%s where id_usuario=%s",
                (nombre,apellido,email,contrasena, id_usuario)
=======
    def cambiar(nombre, apellido, email, contrasena, id_usuario):
        try:
            # CORRECCIÓN: Faltaba setear contrasena en el SQL y el WHERE estaba confuso
            cursor.execute(
                "update usuarios set nombre=%s, apellido=%s, email=%s, contrasena=%s where id_usuario=%s",
                (nombre, apellido, email, contrasena, id_usuario)
>>>>>>> 5718117065bf8efc8fa6b8cfb2bd703f5cab660d
            )
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
    def eliminar(id_usuario):
        try:
<<<<<<< HEAD
            cursor.execute(
                "delete from usuarios where id_usuario=%s",
                (id_usuario,)
            )
=======
            cursor.execute("delete from usuarios where id_usuario=%s", (id_usuario,))
>>>>>>> 5718117065bf8efc8fa6b8cfb2bd703f5cab660d
            conexion.commit()
            return True
        except:
            return False
        
    @staticmethod
<<<<<<< HEAD
    def buscar(nombre,apellido):
        try:
            cursor.execute(
                "select * from usuarios where nombre and apellido like '$%s$'"
                (nombre,apellido)
            )
            conexion.commit()
            return True
        except:
            return False
        
=======
    def buscar(nombre):
        try:
            # CORRECCIÓN: Sintaxis de LIKE corregida
            cursor.execute(
                "select * from usuarios where nombre like %s",
                ('%' + nombre + '%',)
            )
            return cursor.fetchall()
        except:
            return []
        
    @staticmethod
    def validar(email, password):
        try:
            # CORRECCIÓN: Validamos por EMAIL
            cursor.execute(
                "select * from usuarios where email = %s and contrasena = %s",
                (email, password)
            )
            datos = cursor.fetchone()
            return datos
        except:
            return None
>>>>>>> 5718117065bf8efc8fa6b8cfb2bd703f5cab660d
