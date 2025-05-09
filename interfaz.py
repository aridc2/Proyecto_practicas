from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

root = Tk()
root.geometry('800x400')
root.title('Gestor de proyectos')

def insert():
    CIF = CIF_entry.get()
    nombre_empresa = nombre_empresa_entry.get()
    tipo_sociedad = tipo_sociedad_entry.get()
    Sector = Sector_entry.get()
    Localidad = Localidad_entry.get()
    telefono_empresa = telefono_empresa_entry.get()

    if(CIF==''or nombre_empresa=='' or telefono_empresa==''):
        MessageBox.showinfo('ALERT','Porfavor introduzca todos los datos')
    else:
        con = mysql.connect(host='localhost', user='root', password='josegras', database='gestionProyectos' )
        cursor = con.cursor()
        sql = "INSERT INTO Empresa (CIF, Nombre,Tipo_sociedad,Sector,Localidad, N_Telefono) VALUES (%s, %s, %s,%s, %s, %s)"
        valores = (CIF, nombre_empresa, tipo_sociedad, Sector, Localidad, telefono_empresa)
        cursor.execute(sql, valores)
        con.commit()
        MessageBox.showinfo('Status','Insertado correctamente')
        con.close();


CIF = Label(root, text='Introduzca CIF: ', font=('verdana 13'))
CIF.place(x=50, y=30)
CIF_entry=Entry(root, font=('verdana 13'))
CIF_entry.place(x=220,y=30)

nombre_empresa = Label(root, text='Nombre empresa: ', font=('verdana 13'))
nombre_empresa.place(x=50, y=80)
nombre_empresa_entry=Entry(root, font=('verdana 13'))
nombre_empresa_entry.place(x=220,y=80)

tipo_sociedad = Label(root, text='Tipo de sociedad: ', font=('verdana 13'))
tipo_sociedad.place(x=50, y=130)
tipo_sociedad_entry=Entry(root, font=('verdana 13'))
tipo_sociedad_entry.place(x=220,y=130)

Sector = Label(root, text='Sector: ', font=('verdana 13'))
Sector.place(x=50, y=180)
Sector_entry=Entry(root, font=('verdana 13'))
Sector_entry.place(x=220,y=180)

Localidad = Label(root, text='Localidad: ', font=('verdana 13'))
Localidad.place(x=50, y=230)
Localidad_entry=Entry(root, font=('verdana 13'))
Localidad_entry.place(x=220,y=230)

telefono_empresa = Label(root, text='Telefono empresa: ', font=('verdana 13'))
telefono_empresa.place(x=50, y=280)
telefono_empresa_entry=Entry(root, font=('verdana 13'))
telefono_empresa_entry.place(x=220,y=280)

btnInsert=Button(root, text='Insert',command=insert, font=(' verdana 13')).place(x=100, y=320)

root.mainloop()