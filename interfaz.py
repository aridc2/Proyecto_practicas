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

        if CIF == '' or nombre_empresa == '' or telefono_empresa == '':
            tk.messagebox.showinfo('ALERT', 'Por favor introduzca todos los datos')
        else:
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
            con.close()

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
            con = mysql.connect(
                host='localhost',
                user='root',
                password='josegras',
                database='gestionProyectos'
            )
            cursor = con.cursor()
            cursor.execute("DELETE FROM Proyecto WHERE CIF = %s", (CIF,))
            cursor.execute("DELETE FROM Empresa WHERE CIF = %s", (CIF,))
            con.commit()
            tk.messagebox.showinfo('Status', 'Borrado correctamente')
            con.close()

    tk.Label(root, text='Introduzca CIF: ', font=('verdana', 13)).place(x=50, y=30)
    CIF_entry = tk.Entry(root, font=('verdana', 13))
    CIF_entry.place(x=220, y=30)

    tk.Button(root, text='Borrar', command=delet, font=('verdana', 13)).place(x=100, y=320)

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


ventana_inicio.mainloop()