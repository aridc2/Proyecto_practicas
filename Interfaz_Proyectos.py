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
v1 = ["B19283746","Mi Empresa S.A.","As1",'Proyecto 1','Activo','Si','Pepe','2','4']

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
    Facturable = v1[5]
    Fecha_Inicio = '2024-01-01'  
    Fecha_Final = '2024-12-31'   
    Nombre_proyecto = v1[3]
    Estado = v1[4]
    Jefe_proyecto = v1[6]
    
    print("Introduce los valores que quieres modificar de la base de datos")
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
        
        Facturable = input("Facturable: ")
        Fecha_Inicio = input("Fecha de incio: ")
        Fecha_Final = input("Fecha de finalización: ") 
        Nombre_proyecto = input("Nombre: ")
        Estado = input("Estado: ")
        Jefe_proyecto = input("Jefe del proyecto: ")
        
        if Facturable!='':
            sql = 'UPDATE Proyecto SET Facturable = %s WHERE ID_proyecto = %s AND CIF = %s'
            valores = (Facturable, ID_proyecto, CIF)
            cursor.execute(sql, valores)
            
        if Fecha_Inicio!='':
            sql = 'UPDATE Proyecto SET Fecha_Inicio = %s WHERE ID_proyecto = %s AND CIF = %s'
            valores = (Fecha_Inicio, ID_proyecto, CIF)
            cursor.execute(sql, valores)
            
        if Fecha_Final!='':
            sql = 'UPDATE Proyecto SET Fecha_Final = %s WHERE ID_proyecto = %s AND CIF = %s'
            valores = (Fecha_Final, ID_proyecto, CIF)
            cursor.execute(sql, valores)
            
        if Nombre_proyecto!='':
            sql = 'UPDATE Proyecto SET Nombre_proyecto = %s WHERE ID_proyecto = %s AND CIF = %s'
            valores = (Nombre_proyecto, ID_proyecto, CIF)
            cursor.execute(sql, valores)
            
        if Estado!='':
            sql = 'UPDATE Proyecto SET Estado = %s WHERE ID_proyecto = %s AND CIF = %s'
            valores = (Estado, ID_proyecto, CIF)
            cursor.execute(sql, valores)
            
        if Jefe_proyecto!='':
            sql = 'UPDATE Proyecto SET Jefe_proyecto = %s WHERE ID_proyecto = %s AND CIF = %s'
            valores = (Jefe_proyecto, ID_proyecto, CIF)
            cursor.execute(sql, valores)
            
        con.commit() #Sirve para que los cambios que se hagan en la BBDD se guarden

        messagebox.showinfo("Status", "Proyecto Modificado correctamente")
        con.close()
               

def seleccionar_proyectos_por_empresa():
    print("Introduce el CIF de la empresa para ver sus proyectos:")
    CIF = input("CIF: ").strip() #Hace que aunque el usuasrio introduzca espacios estos no afecten a como lee los datos introducidos

    if CIF == "":
        print("Error: El CIF no puede estar vacío.")
        return

    # Conexión a la base de datos
    con = mysql.connect(
        host='localhost',
        user='root',
        password='josegras',
        database='gestionProyectos'
    )
    cursor = con.cursor()

    # Buscar información de la empresa
    cursor.execute("""
        SELECT CIF, Nombre, Tipo_sociedad, Sector, Localidad, N_Telefono
        FROM Empresa
        WHERE CIF = %s
    """, (CIF,))
    empresa = cursor.fetchone()

    if not empresa:
        print("No se encontró ninguna empresa con ese CIF.")
        con.close()
        return

    # Mostrar datos de la empresa
    print("\n Información de la Empresa:")
    print(f"  CIF: {empresa[0]}")
    print(f"  Nombre: {empresa[1]}")
    print(f"  Tipo de Sociedad: {empresa[2]}")
    print(f"  Sector: {empresa[3]}")
    print(f"  Localidad: {empresa[4]}")
    print(f"  Teléfono: {empresa[5]}")

    # Buscar proyectos asociados a esa empresa
    cursor.execute("""
        SELECT ID_proyecto, Facturable, Fecha_Inicio, Fecha_Final, Nombre_proyecto, Estado, Jefe_proyecto
        FROM Proyecto
        WHERE CIF = %s
    """, (CIF,))
    proyectos = cursor.fetchall() #Coge una tupla entera y la mete en una varialbe y la desempaqueta

    if proyectos:
        print("\n Proyectos Asociados:")
        for i, proyecto in enumerate(proyectos, start=1):
            print(f"\n  Proyecto {i}:")
            print(f"    ID: {proyecto[0]}")
            print(f"    Facturable: {proyecto[1]}")
            print(f"    Fecha de Inicio: {proyecto[2]}")
            print(f"    Fecha Final: {proyecto[3]}")
            print(f"    Nombre: {proyecto[4]}")
            print(f"    Estado: {proyecto[5]}")
            print(f"    Jefe de Proyecto: {proyecto[6]}")
    else:
        print("\nEsta empresa no tiene proyectos registrados.")

    con.close()

   
    
# insertar_datos()

# borrar = input("¿Quieres borrar Proyectos de la tabla?")
# if borrar.lower() in ["si", "s", "yes", "y"]:
#     borrar_datos()
    
# update = input("¿Quieres actualizar o modificar los datos?")
# if update.lower() in ["si", "s", "yes", "y"]:
#     update_proyecto()

seleccionar_proyectos_por_empresa()

