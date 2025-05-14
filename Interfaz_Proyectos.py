###
# Interfaz De Proyectos (CRUD)
# # Despues borrar el fichero
###

import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as mysql
from config import *

import os
os.system("cls") 

p_1= Proyecto ("A12345678","Mi Empresa S.A.",1,'Proyecto 1','Activo','Si','Pepe','2','4')
v1 = ["B19283746","Mi Empresa S.A.","A1",'Proyecto 1','Activo','Si','Pepe','2','4']

def insertar_datos():
    ID_proyecto = str(v1[2])
    CIF = v1[0]
    Facturable = v1[5]
    Fecha_Inicio = '2024-01-01'  
    Fecha_Final = '2024-12-31'   
    Nombre_proyecto = v1[3]
    Estado = v1[4]
    Jefe_proyecto = v1[6]
    
    con = mysql.connect(
        host='localhost',
        user='root',
        password='josegras',
        database='gestionProyectos'
                )
    
    cursor = con.cursor()
    sql = "INSERT INTO Proyecto (ID_proyecto, CIF, Facturable, Fecha_Inicio, Fecha_Final, Nombre_proyecto, Estado, Jefe_proyecto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (ID_proyecto, CIF, Facturable, Fecha_Inicio, Fecha_Final, Nombre_proyecto, Estado, Jefe_proyecto)
    cursor.execute(sql, valores)
    con.commit()
    con.close()
    
def borrar_datos():
    print("Introduce los valores que quieres borrar de la base de datos")
    CIF = input("Introduzca el CIF de la empresa: ")
    ID_proyecto = input("Introduce el ID del proyecto que quieres borrar: ")
    
    if CIF == "" or ID_proyecto == "":
        print("Error. No se puede encontrar ese proyecto")
    else:
        con = mysql.connect(
            host='localhost',
            user='root',
            password='josegras',
            database='gestionProyectos'
        )
        cursor = con.cursor()

        # Borrar el proyecto con ese ID y CIF
        cursor.execute("DELETE FROM Proyecto WHERE ID_proyecto = %s AND CIF = %s", (ID_proyecto, CIF))
        con.commit()

        messagebox.showinfo("Status", "Proyecto borrado correctamente")
        con.close()
        
        
        
def update_proyecto():
    print("Introduce los valores que quieres borrar de la base de datos")
    CIF = input("Introduzca el CIF de la empresa: ")
    ID_proyecto = input("Introduce el ID del proyecto que quieres modifdicar o actualizar: ")
    
    if CIF == "" or ID_proyecto == "":
        print("Error. No se puede encontrar ese proyecto")
    else:
        con = mysql.connect(
            host='localhost',
            user='root',
            password='josegras',
            database='gestionProyectos'
        )
        cursor = con.cursor()
        
    

insertar_datos()
borrar = input("¿Quieres borrar Proyectos de la tabla?")
if borrar == "Si" or borrar == "SI" or borrar == "s" or borrar == "Yes" or borrar == "y":
    borrar_datos()
elif borrar =="No" or borrar == "NO" or borrar == "n":
    print("")