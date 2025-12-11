import mysql.connector
from tkinter import messagebox

try:
    conexion=mysql.connector.connect(
        port=3306,
        host="localhost",
        user="root",
        password="Garcia_635",
        database="bd_Kunibo"
    )
    cursor=conexion.cursor(buffered=True)
except:
    messagebox.showerror(icon="error",message="...Ocurrio un error en la base de datos...")