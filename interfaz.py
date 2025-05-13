import tkinter as tk
import tkinter.messagebox
import mysql.connector as mysql


def ventana_inserccion_empresa():

    root = tk.Tk()
    root.geometry('800x400')
    root.title('Gestor de proyectos')

    def insert():
        CIF = CIF_entry.get()
        nombre_empresa = nombre_empresa_entry.get()
        tipo_sociedad = tipo_sociedad_entry.get()
        Sector = Sector_entry.get()
        Localidad = Localidad_entry.get()
        telefono_empresa = telefono_empresa_entry.get()

        if CIF == '' or nombre_empresa == '' or telefono_empresa == '' or tipo_sociedad=='' or Sector=='' or Localidad== '':
            tk.messagebox.showinfo('ALERT', 'Por favor introduzca todos los datos')
        else:
            try:
                con = mysql.connect(
                    host='localhost',
                    user='root',
                    password='josegras',
                    database='gestionProyectos'
                )
                cursor = con.cursor()
                sql = "INSERT INTO Empresa (CIF, Nombre, Tipo_sociedad, Sector, Localidad, N_Telefono) VALUES (%s, %s, %s, %s, %s, %s)"
                valores = (CIF, nombre_empresa, tipo_sociedad, Sector, Localidad, telefono_empresa)
                cursor.execute(sql, valores)
                con.commit()
                tk.messagebox.showinfo('Status', 'Insertado correctamente')

                CIF_entry.delete(0, 'end')
                nombre_empresa_entry.delete(0, 'end')
                tipo_sociedad_entry.delete(0, 'end')
                Sector_entry.delete(0, 'end')
                Localidad_entry.delete(0, 'end')
                telefono_empresa_entry.delete(0, 'end')

                con.close()
            except Exception as e: #Imprime el error en una ventana emergente 
                tk.messagebox.showinfo('Error',str(e))

    tk.Label(root, text='Introduzca CIF: ', font=('verdana', 13)).place(x=50, y=30)
    CIF_entry = tk.Entry(root, font=('verdana', 13))
    CIF_entry.place(x=220, y=30)

    tk.Label(root, text='Nombre empresa: ', font=('verdana', 13)).place(x=50, y=80)
    nombre_empresa_entry = tk.Entry(root, font=('verdana', 13))
    nombre_empresa_entry.place(x=220, y=80)

    tk.Label(root, text='Tipo de sociedad: ', font=('verdana', 13)).place(x=50, y=130)
    tipo_sociedad_entry = tk.Entry(root, font=('verdana', 13))
    tipo_sociedad_entry.place(x=220, y=130)

    tk.Label(root, text='Sector: ', font=('verdana', 13)).place(x=50, y=180)
    Sector_entry = tk.Entry(root, font=('verdana', 13))
    Sector_entry.place(x=220, y=180)

    tk.Label(root, text='Localidad: ', font=('verdana', 13)).place(x=50, y=230)
    Localidad_entry = tk.Entry(root, font=('verdana', 13))
    Localidad_entry.place(x=220, y=230)

    tk.Label(root, text='Teléfono empresa: ', font=('verdana', 13)).place(x=50, y=280)
    telefono_empresa_entry = tk.Entry(root, font=('verdana', 13))
    telefono_empresa_entry.place(x=220, y=280)

    tk.Button(root, text='Insertar', command=insert, font=('verdana', 13)).place(x=100, y=320)

    root.mainloop()

def ventana_eliminar_empresa():
    root = tk.Tk()
    root.geometry('800x400')
    root.title('Gestor de proyectos')

    def delet():
        CIF = CIF_entry.get()

        if CIF == '':
            tk.messagebox.showinfo('ALERT', 'Por favor introduzca el CIF para eliminar la empresa')
        else:
            try:
                con = mysql.connect(
                    host='localhost',
                    user='root',
                    password='josegras',
                    database='gestionProyectos'
                )
                cursor = con.cursor()
                cursor.execute("DELETE FROM Proyecto WHERE CIF = %s", (CIF))
                cursor.execute("DELETE FROM Empresa WHERE CIF = %s", (CIF))
                con.commit()
                CIF_entry.delete(0, 'end')
                tk.messagebox.showinfo('Status', 'Borrado correctamente')

                con.close()
            except Exception as e:
                tk.messagebox.showinfo('Error',str(e))

    tk.Label(root, text='Introduzca CIF: ', font=('verdana', 13)).place(x=50, y=30)
    CIF_entry = tk.Entry(root, font=('verdana', 13))
    CIF_entry.place(x=220, y=30)

    tk.Button(root, text='Borrar', command=delet, font=('verdana', 13)).place(x=100, y=320)

    root.mainloop()

def ventana_actualizar_empresa():

    root = tk.Tk()
    root.geometry('800x400')
    root.title('Gestor de proyectos')

    def update():
        CIF = CIF_entry.get()
        nombre_empresa = nombre_empresa_entry.get()
        tipo_sociedad = tipo_sociedad_entry.get()
        Sector = Sector_entry.get()
        Localidad = Localidad_entry.get()
        telefono_empresa = telefono_empresa_entry.get()

        if CIF == '':
            tk.messagebox.showinfo('ALERT', 'Por favor introduzca el CIF para poder actualizar los datos')
        else:
            try:
                con = mysql.connect(
                    host='localhost',
                    user='root',
                    password='josegras',
                    database='gestionProyectos'
                )
                cursor = con.cursor()
                
                if nombre_empresa!= '':
                    sql ='UPDATE Empresa SET Nombre = %s WHERE CIF = %s'
                    valores = (nombre_empresa,CIF)
                    cursor.execute(sql, valores)

                if tipo_sociedad!= '':
                    sql ='UPDATE Empresa SET Tipo_sociedad = %s WHERE CIF = %s'
                    valores = (tipo_sociedad,CIF)
                    cursor.execute(sql, valores)

                if Sector!= '':
                    sql ='UPDATE Empresa SET Sector = %s WHERE CIF = %s'
                    valores = (Sector,CIF)
                    cursor.execute(sql, valores)

                if Localidad!= '':
                    sql ='UPDATE Empresa SET Localidad = %s WHERE CIF = %s'
                    valores = (Localidad,CIF)
                    cursor.execute(sql, valores)

                if telefono_empresa!= '':
                    sql ='UPDATE Empresa SET N_Telefono = %s WHERE CIF = %s'
                    valores = (telefono_empresa,CIF)
                    cursor.execute(sql, valores)

                con.commit()
                if cursor.rowcount == 0:
                    tk.messageBox.showinfo('Resultado', 'No se encontró ninguna empresa con ese CIF')
                else:
                    tk.messagebox.showinfo('Status', 'Datos actualizados correctamente')

                    CIF_entry.delete(0, 'end')
                    nombre_empresa_entry.delete(0, 'end')
                    tipo_sociedad_entry.delete(0, 'end')
                    Sector_entry.delete(0, 'end')
                    Localidad_entry.delete(0, 'end')
                    telefono_empresa_entry.delete(0, 'end')

                con.close()
            except Exception as e:
                tk.messagebox.showinfo('Error',str(e))

    tk.Label(root, text='Introduzca CIF: ', font=('verdana', 13)).place(x=50, y=30)
    CIF_entry = tk.Entry(root, font=('verdana', 13))
    CIF_entry.place(x=220, y=30)

    tk.Label(root, text='Nombre empresa: ', font=('verdana', 13)).place(x=50, y=80)
    nombre_empresa_entry = tk.Entry(root, font=('verdana', 13))
    nombre_empresa_entry.place(x=220, y=80)

    tk.Label(root, text='Tipo de sociedad: ', font=('verdana', 13)).place(x=50, y=130)
    tipo_sociedad_entry = tk.Entry(root, font=('verdana', 13))
    tipo_sociedad_entry.place(x=220, y=130)

    tk.Label(root, text='Sector: ', font=('verdana', 13)).place(x=50, y=180)
    Sector_entry = tk.Entry(root, font=('verdana', 13))
    Sector_entry.place(x=220, y=180)

    tk.Label(root, text='Localidad: ', font=('verdana', 13)).place(x=50, y=230)
    Localidad_entry = tk.Entry(root, font=('verdana', 13))
    Localidad_entry.place(x=220, y=230)

    tk.Label(root, text='Teléfono empresa: ', font=('verdana', 13)).place(x=50, y=280)
    telefono_empresa_entry = tk.Entry(root, font=('verdana', 13))
    telefono_empresa_entry.place(x=220, y=280)

    tk.Button(root, text='Update', command=update, font=('verdana', 13)).place(x=100, y=320)

    root.mainloop()



ventana_inicio=tk.Tk()
ventana_inicio.title('Practica')
ventana_inicio.geometry('600x400+650+200')#los dos ultimos valores para las posiciones
ventana_inicio.minsize(400,300)
ventana_inicio.maxsize(800,600)
ventana_inicio.iconbitmap("C:/Users/Ari/Documents/PRACTICAS/PYTHON/tkinter/icono.ico")
ventana_inicio.configure(bg='lightblue')
btn_insert_empresa=tk.Button(ventana_inicio,command=ventana_inserccion_empresa,text='Insertar empresa')
btn_insert_empresa.pack()
btn_delet_empresa=tk.Button(ventana_inicio,command=ventana_eliminar_empresa,text='Borrar empresa')
btn_delet_empresa.pack()
btn_update_empresa=tk.Button(ventana_inicio,command=ventana_actualizar_empresa,text='Actualizar empresa')
btn_update_empresa.pack()

ventana_inicio.mainloop()