import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as mysql
from clases import *


def ventana_inserccion_empresa():
    root.withdraw()
    insertar_win = tk.Toplevel()
    insertar_win.geometry('800x500')
    insertar_win.title('Gestor de proyectos')
    insertar_win.config(bg="#eaf2f8")

    def insert():
        CIF = CIF_entry.get()
        nombre_empresa = nombre_empresa_entry.get()
        tipo_sociedad = tipo_sociedad_combo.get()
        Sector = Sector_combo.get()
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
                tipo_sociedad_combo.set('')
                Sector_combo.set('')
                Localidad_entry.delete(0, 'end')
                telefono_empresa_entry.delete(0, 'end')

                con.close()
            except Exception as e: #Guarda el error y lo imprime en una ventana emergente
                tk.messagebox.showinfo('Error',str(e))

    def cerrar_e_ir_menu():
        insertar_win.destroy()
        root.deiconify()

    tipos_sociedad = [
    "Sociedad Anónima", "Sociedad Limitada", "Sociedad Cooperativa",
    "Sociedad Comanditaria", "Sociedad Civil", "Sociedad autonoma", "Sociedad colecctiva"
    ]

    sectores = [
    "Agricultura", "Pesca", "Minería", "Silvicultura", "Industria alimentaria",
    "Construcción", "Metalurgia", "Automoción", "Química", "Textil", "Manufactura",
    "Comercio", "Transporte y logística", "Hostelería y turismo", "Educación", "Sanidad",
    "Servicios financieros", "Consuloría", "Tecnología", "Software",
    "Consultoría especializada", "Startups tecnológicas", "ONG", "Asistencia social",
    "Servicios culturales", "Formación personal"
    ]

    titulo = tk.Label(insertar_win, text="Insertar Empresa", font=("Helvetica", 20, "bold"), bg="#eaf2f8", fg="#2e4053")
    titulo.pack(pady=20)

    form_frame = tk.Frame(insertar_win, bg="#eaf2f8")
    form_frame.pack(pady=10)

    
    label_style = {"font": ("Helvetica", 12), "bg": "#eaf2f8", "fg": "#2e4053"}
    entry_style = {"font": ("Helvetica", 12), "width": 30}

    
    tk.Label(form_frame, text="CIF:", **label_style).grid(row=0, column=0, sticky="e", padx=10, pady=10)
    CIF_entry = tk.Entry(form_frame, **entry_style)
    CIF_entry.grid(row=0, column=1)

    tk.Label(form_frame, text="Nombre Empresa:", **label_style).grid(row=1, column=0, sticky="e", padx=10, pady=10)
    nombre_empresa_entry = tk.Entry(form_frame, **entry_style)
    nombre_empresa_entry.grid(row=1, column=1)

    tk.Label(form_frame, text="Tipo de Sociedad:", **label_style).grid(row=2, column=0, sticky="e", padx=10, pady=10)
    tipo_sociedad_combo = ttk.Combobox(form_frame, values=tipos_sociedad, font=("Helvetica", 12), state="readonly", width=28)
    tipo_sociedad_combo.grid(row=2, column=1)

    tk.Label(form_frame, text="Sector:", **label_style).grid(row=3, column=0, sticky="e", padx=10, pady=10)
    Sector_combo = ttk.Combobox(form_frame, values=sectores, font=("Helvetica", 12), state="readonly", width=28)
    Sector_combo.grid(row=3, column=1)

    tk.Label(form_frame, text="Localidad:", **label_style).grid(row=4, column=0, sticky="e", padx=10, pady=10)
    Localidad_entry = tk.Entry(form_frame, **entry_style)
    Localidad_entry.grid(row=4, column=1)

    tk.Label(form_frame, text="Teléfono:", **label_style).grid(row=5, column=0, sticky="e", padx=10, pady=10)
    telefono_empresa_entry = tk.Entry(form_frame, **entry_style)
    telefono_empresa_entry.grid(row=5, column=1)

    
    btn_style = {
        "font": ("Helvetica", 12, "bold"),
        "width": 15,
        "height": 1,
        "bg": "#3498db",
        "fg": "white",
        "bd": 0,
        "activebackground": "#2980b9",
        "cursor": "hand2"
    }

    button_frame = tk.Frame(insertar_win, bg="#eaf2f8")
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Insertar", command=insert, **btn_style).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Volver", command=cerrar_e_ir_menu, **btn_style).grid(row=0, column=1, padx=10)

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




root = tk.Tk()
root.title("Gestión de Empresas")
root.geometry("600x600")
root.config(bg="#eaf2f8")

titulo = tk.Label(root, text="Gestor de Empresas", font=("Helvetica", 24, "bold"), bg="#eaf2f8", fg="#2e4053")
titulo.pack(pady=40)


boton_frame = tk.Frame(root, bg="#eaf2f8")
boton_frame.pack(pady=20)


btn_style = {
    "font": ("Helvetica", 14, "bold"),
    "width": 20,
    "height": 2,
    "bg": "#3498db",
    "fg": "white",
    "bd": 0,
    "activebackground": "#2980b9",
    "cursor": "hand2"
}


tk.Button(boton_frame, text="Insertar Empresa", command=ventana_inserccion_empresa, **btn_style).grid(row=0, column=0, pady=10, padx=20)
#tk.Button(boton_frame, text="Consultar Empresas", command=abrir_consultar, **btn_style).grid(row=1, column=0, pady=10, padx=20)
tk.Button(boton_frame, text="Actualizar Empresa", command=ventana_actualizar_empresa, **btn_style).grid(row=2, column=0, pady=10, padx=20)
tk.Button(boton_frame, text="Eliminar Empresa", command=ventana_eliminar_empresa, **btn_style).grid(row=3, column=0, pady=10, padx=20)


root.mainloop()
