import mysql.connector
from tkinter import messagebox

try:
    conexion=mysql.connector.connect(
        port=3306,
        host="localhost",
        user="root",
<<<<<<< HEAD
        password="Garcia_635",
=======
        password="admin",
>>>>>>> ef4e9085bbbea9f50da6f50471fc8b21b819e54e
        database="bd_Kunibo"
    )
    cursor=conexion.cursor(buffered=True)
except:
    messagebox.showerror(icon="error",message="...Ocurrio un error en la base de datos...")