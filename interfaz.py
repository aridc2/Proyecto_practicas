from tkinter import *
import tkinter.messagebox as MessageBox
#import mysql.connector as mysql

root = Tk()
root.geometry('800x400')
root.title('Gestor de proyectos')

CIF = Label(root, text='Introduzca CIF: ', font=('verdana 13'))
CIF.place(x=50, y=30)
CIF_entry=Entry(root, font=('verdana 13'))
CIF_entry.place(x=220,y=30)

nombre_empresa = Label(root, text='Nombre empresa: ', font=('verdana 13'))
nombre_empresa.place(x=50, y=80)
nombre_empresa_entry=Entry(root, font=('verdana 13'))
nombre_empresa_entry.place(x=220,y=80)

telefono_empresa = Label(root, text='Telefono empresa: ', font=('verdana 13'))
telefono_empresa.place(x=50, y=130)
telefono_empresa_entry=Entry(root, font=('verdana 13'))
telefono_empresa_entry.place(x=220,y=130)

btnInsert=Button(root, text='Insert', font=(' verdana 13')).place(x=100, y=190)

root.mainloop()