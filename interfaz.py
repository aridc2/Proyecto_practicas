import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector as mysql
from clases import *


###################################################
# ~~~~~~~~~~~~~~~~~~~EMPRESAS~~~~~~~~~~~~~~~~~~~~ #
###################################################

#Importar los posibles valores de tipos de sociedad y sectores
tipos_sociedad = Empresa.tipos_sociedad
sectores = Empresa.sectores

#ventana ocupada de la accion de rellenar los datos de inserccion de empresa y de ejecutar la funcion insert
def ventana_inserccion_empresa():


    root.withdraw()
    insertar_win = tk.Toplevel()
    insertar_win.geometry('800x500')
    insertar_win.minsize(600,500)
    insertar_win.title('Gestor de proyectos')
    insertar_win.config(bg="#eaf2f8")

    def insert():
        CIF = CIF_entry.get().strip()
        nombre_empresa = nombre_empresa_entry.get().strip()
        tipo_sociedad = tipo_sociedad_combo.get().strip()
        Sector = Sector_combo.get()
        Localidad = Localidad_entry.get()
        telefono_empresa = telefono_empresa_entry.get().strip()

        if CIF == '' or nombre_empresa == '' or telefono_empresa == '' or tipo_sociedad=='' or Sector=='' or Localidad== '':
            tk.messagebox.showerror('ALERT', 'Por favor introduzca todos los datos')
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
                tk.messagebox.showerror('Error',str(e))

    def cerrar_e_ir_menu():
        insertar_win.destroy()
        root.deiconify()

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

#ventana ocupada de la accion de rellenar el cif y eliminarlo con la funcion delete
def ventana_eliminar_empresa():

    root.withdraw()
    eliminar_win = tk.Toplevel()
    eliminar_win.geometry('600x300')
    eliminar_win.minsize(600,300)
    eliminar_win.title('Gestor de proyectos')
    eliminar_win.config(bg="#eaf2f8")

    def delet():
        CIF = CIF_entry.get().strip()

        if CIF == '':
            tk.messagebox.showerror('Error', 'Por favor introduzca el CIF para eliminar la empresa')
        else:
            try:
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
                CIF_entry.delete(0, 'end')
                tk.messagebox.showinfo('Status', 'Borrado correctamente')

                con.close()
            except Exception as e:
                tk.messagebox.showerror('Error',str(e))

    def cerrar_e_ir_menu():
        eliminar_win.destroy()
        root.deiconify()

    titulo = tk.Label(eliminar_win, text="Eliminar Empresa", font=("Helvetica", 20, "bold"), bg="#eaf2f8", fg="#2e4053")
    titulo.pack(pady=20)

    
    form_frame = tk.Frame(eliminar_win, bg="#eaf2f8")
    form_frame.pack(pady=10)

    tk.Label(form_frame, text="CIF de la empresa:", font=("Helvetica", 13), bg="#eaf2f8").grid(row=0, column=0, padx=10, pady=10)
    CIF_entry = tk.Entry(form_frame, font=("Helvetica", 13), width=30)
    CIF_entry.grid(row=0, column=1, padx=10, pady=10)

    
    btn_frame = tk.Frame(eliminar_win, bg="#eaf2f8")
    btn_frame.pack(pady=20)

    btn_style = {
        "font": ("Helvetica", 12, "bold"),
        "width": 15,
        "height": 2,
        "bg": "#e74c3c",
        "fg": "white",
        "bd": 0,
        "activebackground": "#c0392b",
        "cursor": "hand2"
    }

    tk.Button(btn_frame, text="Eliminar", command=delet, **btn_style).grid(row=0, column=0, padx=10)

    tk.Button(btn_frame, text="Volver", command=cerrar_e_ir_menu, bg="#3498db", fg="white", activebackground="#7f8c8d", font=("Helvetica", 12, "bold"), width=15, height=2, bd=0, cursor="hand2").grid(row=0, column=1, padx=10)

    eliminar_win.mainloop()

#Ventana para introducir el cif y si encuentra la empresa abre otra ventana para introducir los datos a actualizar
def ventana_actualizar_empresa():
    root.withdraw()
    actualizar_win = tk.Toplevel()
    actualizar_win.geometry('800x300')
    actualizar_win.minsize(500,300)
    actualizar_win.title('Gestor de proyectos')
    actualizar_win.config(bg="#eaf2f8")

    def buscar():
        CIF = CIF_entry.get().strip()
        
        if CIF == '':
            tk.messagebox.showerror('Error', 'Por favor introduzca el CIF para poder actualizar los datos')
        else:
            try:
                con = mysql.connect(
                    host='localhost',
                    user='root',
                    password='josegras',
                    database='gestionProyectos'
                )
                cursor = con.cursor()
                cursor.execute("SELECT 1 FROM Empresa WHERE CIF = %s LIMIT 1", (CIF,))
                resultado = cursor.fetchone()
                if resultado == None:
                    tk.messagebox.showinfo('Resultado', 'No se encontró ninguna empresa con ese CIF')
                else:
                    ventana_rellenar_campos(CIF)

                    CIF_entry.delete(0, 'end')
                    

                con.close()
            except Exception as e:
                tk.messagebox.showerror('Error',str(e))

    def cerrar_e_ir_menu():
        actualizar_win.destroy()
        root.deiconify()

    def ventana_rellenar_campos(CIF):
        CIF_buscado=CIF
        actualizar_win.withdraw()
        actualizar_campos_win = tk.Toplevel()
        actualizar_campos_win.geometry('800x500')
        actualizar_campos_win.minsize(500,500)
        actualizar_campos_win.title('Gestor de proyectos')
        actualizar_campos_win.config(bg="#eaf2f8")

        def cerrar_e_ir_menu():
            actualizar_campos_win.destroy()
            actualizar_win.deiconify()
        def update(CIF_buscado):

            nombre_empresa = nombre_empresa_entry.get().strip()
            tipo_sociedad = tipo_sociedad_combo.get()
            Sector = Sector_combo.get()
            Localidad = Localidad_entry.get().strip()
            telefono_empresa = telefono_empresa_entry.get().strip()

            
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
                    valores = (nombre_empresa,CIF_buscado)
                    cursor.execute(sql, valores)

                if tipo_sociedad!= '':
                    sql ='UPDATE Empresa SET Tipo_sociedad = %s WHERE CIF = %s'
                    valores = (tipo_sociedad,CIF_buscado)
                    cursor.execute(sql, valores)

                if Sector!= '':
                    sql ='UPDATE Empresa SET Sector = %s WHERE CIF = %s'
                    valores = (Sector,CIF_buscado)
                    cursor.execute(sql, valores)

                if Localidad!= '':
                    sql ='UPDATE Empresa SET Localidad = %s WHERE CIF = %s'
                    valores = (Localidad,CIF_buscado)
                    cursor.execute(sql, valores)

                if telefono_empresa!= '':
                    sql ='UPDATE Empresa SET N_Telefono = %s WHERE CIF = %s'
                    valores = (telefono_empresa,CIF_buscado)
                    cursor.execute(sql, valores)

                con.commit()
                if nombre_empresa == '' and telefono_empresa == '' and tipo_sociedad=='' and Sector=='' and Localidad== '':
                    tk.messagebox.showerror('Error', 'No se ha modificado ningun campo')
                else:
                    tk.messagebox.showinfo('Status', 'Datos actualizados correctamente')

                    
                    nombre_empresa_entry.delete(0, 'end')
                    tipo_sociedad_combo.delete(0, 'end')
                    Sector_combo.delete(0, 'end')
                    Localidad_entry.delete(0, 'end')
                    telefono_empresa_entry.delete(0, 'end')

                con.close()
            except Exception as e:
                tk.messagebox.showerror('Error',str(e))

        titulo = tk.Label(actualizar_campos_win, text="Actualizar Empresa", font=("Helvetica", 20, "bold"), bg="#eaf2f8", fg="#2e4053")
        titulo.pack(pady=20)

        
        form_frame = tk.Frame(actualizar_campos_win, bg="#eaf2f8")
        form_frame.pack(pady=10)

        label_style = {"font": ("Helvetica", 12), "bg": "#eaf2f8", "fg": "#2e4053"}
        entry_style = {"font": ("Helvetica", 12), "width": 30}


        tk.Label(form_frame, text="Nombre empresa:", **label_style).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        nombre_empresa_entry = tk.Entry(form_frame, **entry_style)
        nombre_empresa_entry.grid(row=1, column=1)

        tk.Label(form_frame, text="Tipo de sociedad:", **label_style).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        tipo_sociedad_combo = ttk.Combobox(form_frame, values=tipos_sociedad, font=("Helvetica", 12), state="readonly", width=28)
        tipo_sociedad_combo.grid(row=2, column=1)

        tk.Label(form_frame, text="Sector:", **label_style).grid(row=3, column=0, sticky="e", padx=10, pady=10)
        Sector_combo = ttk.Combobox(form_frame, values=sectores, font=("Helvetica", 12), state="readonly", width=28)
        Sector_combo.grid(row=3, column=1)

        tk.Label(form_frame, text="Localidad:", **label_style).grid(row=4, column=0, sticky="e", padx=10, pady=10)
        Localidad_entry = tk.Entry(form_frame, **entry_style)
        Localidad_entry.grid(row=4, column=1)

        tk.Label(form_frame, text="Teléfono empresa:", **label_style).grid(row=5, column=0, sticky="e", padx=10, pady=10)
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

        button_frame = tk.Frame(actualizar_campos_win, bg="#eaf2f8")
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Actualizar", command=lambda:update(CIF_buscado), **btn_style).grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Volver", command=cerrar_e_ir_menu, **btn_style).grid(row=0, column=1, padx=10)
    

    titulo = tk.Label(actualizar_win, text="Actualizar Empresa", font=("Helvetica", 20, "bold"), bg="#eaf2f8", fg="#2e4053")
    titulo.pack(pady=20)

    
    form_frame = tk.Frame(actualizar_win, bg="#eaf2f8")
    form_frame.pack(pady=10)

    label_style = {"font": ("Helvetica", 12), "bg": "#eaf2f8", "fg": "#2e4053"}
    entry_style = {"font": ("Helvetica", 12), "width": 30}

    tk.Label(form_frame, text="CIF:", **label_style).grid(row=0, column=0, sticky="e", padx=10, pady=10)
    CIF_entry = tk.Entry(form_frame, **entry_style)
    CIF_entry.grid(row=0, column=1)

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

    button_frame = tk.Frame(actualizar_win, bg="#eaf2f8")
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Buscar", command=buscar, **btn_style).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Volver", command=cerrar_e_ir_menu, **btn_style).grid(row=0, column=1, padx=10)

    actualizar_win.mainloop()

#Ventana para introducir el cif y si encuentra la empresa imprime sus datos
def ventana_consultar_empresa():
    root.withdraw()
    consultar_win = tk.Toplevel()
    consultar_win.geometry('800x400')
    consultar_win.minsize(800,400)
    consultar_win.title('Gestor de proyectos')
    consultar_win.config(bg="#eaf2f8")

    def select():
        CIF = CIF_entry.get().strip()

        if CIF == '':
            tk.messagebox.showerror('ALERT', 'Por favor introduzca el CIF para buscar la empresa')
        else:
            try:
                con = mysql.connect(
                    host='localhost',
                    user='root',
                    password='josegras',
                    database='gestionProyectos'
                )
                cursor = con.cursor()
                cursor.execute("SELECT Nombre, Tipo_sociedad, Sector, Localidad, N_Telefono FROM Empresa WHERE CIF = %s", (CIF,))
                resultado = cursor.fetchone()
                CIF_entry.delete(0, 'end')
                con.close()

                if resultado:
                    # Crear instancia de Empresa
                    nombre, tipo, sector, localidad, telefono = resultado
                    empresa = Empresa(CIF, nombre, tipo, sector, localidad, telefono)
                    
                    resultado_label.config(text=str(empresa), justify="left")
                    tk.Button(form_frame, text="Ver proyectos",command= lambda: ventana_gestionar_proyectos(CIF), **btn_style ).grid(row=2, column=3, sticky="nw", padx=(5, 10), pady=(70, 10))
                    
                else:
                    resultado_label.config(text="No se encontró ninguna empresa con ese CIF.")




            except Exception as e:
                tk.messagebox.showinfo('Error',str(e))

    def cerrar_e_ir_menu():
        consultar_win.destroy()
        root.deiconify()

    def ventana_gestionar_proyectos(CIF):
        consultar_win.withdraw()
        listado_proyectos_empresa_win = tk.Toplevel()
        listado_proyectos_empresa_win.geometry('800x500')
        listado_proyectos_empresa_win.minsize(600,500)
        listado_proyectos_empresa_win.title('Gestor de proyectos')
        listado_proyectos_empresa_win.config(bg="#eaf2f8")

        def seleccionar_proyectos_por_empresa(CIF):


            # Conexión a la base de datos
            con = mysql.connect(
                host='localhost',
                user='root',
                password='josegras',
                database='gestionProyectos'
            )
            cursor = con.cursor()

            # Buscar proyectos asociados a esa empresa
            cursor.execute("""
                SELECT ID_proyecto, Facturable, Fecha_Inicio, Fecha_Final, Nombre_proyecto, Estado, Jefe_proyecto
                FROM Proyecto
                WHERE CIF = %s
            """, (CIF,))
            proyectos = cursor.fetchall() #Coge una tupla entera y la mete en una varialbe y la desempaqueta

            con.close()
            return proyectos


        
        def mostrar_detalles_ventana(proyecto):
            listado_proyectos_empresa_win.withdraw()
            detalle_win = tk.Toplevel()
            detalle_win.title("Detalles del Proyecto")
            detalle_win.geometry("500x300")
            detalle_win.config(bg="#eaf2f8")

            label_style = {"font": ("Helvetica", 12, "bold"), "bg": "#eaf2f8", "fg": "#2e4053"}
            value_style = {"font": ("Helvetica", 12), "bg": "#eaf2f8", "fg": "#2e4053"}

            tk.Label(detalle_win, text="ID Proyecto:", **label_style).pack(anchor="w", padx=20, pady=(20, 0))
            tk.Label(detalle_win, text=proyecto[0], **value_style).pack(anchor="w", padx=40)
            
            tk.Label(detalle_win, text="Nombre:", **label_style).pack(anchor="w", padx=20, pady=(10, 0))
            tk.Label(detalle_win, text=proyecto[4], **value_style).pack(anchor="w", padx=40)

            tk.Label(detalle_win, text="Fecha de Inicio:", **label_style).pack(anchor="w", padx=20, pady=(10, 0))
            tk.Label(detalle_win, text=proyecto[2], **value_style).pack(anchor="w", padx=40)

            tk.Label(detalle_win, text="Fecha de Finalización:", **label_style).pack(anchor="w", padx=20, pady=(10, 0))
            tk.Label(detalle_win, text=proyecto[3], **value_style, wraplength=400, justify="left").pack(anchor="w", padx=40)

            tk.Label(detalle_win, text="Estado:", **label_style).pack(anchor="w", padx=20, pady=(10, 0))
            tk.Label(detalle_win, text=proyecto[5], **value_style).pack(anchor="w", padx=40)
            
            tk.Label(detalle_win, text="Facturable:", **label_style).pack(anchor="w", padx=20, pady=(10, 0))
            tk.Label(detalle_win, text=proyecto[1], **value_style).pack(anchor="w", padx=40)
            
            tk.Label(detalle_win, text="Jefe de proyecto:", **label_style).pack(anchor="w", padx=20, pady=(10, 0))
            tk.Label(detalle_win, text=proyecto[6], **value_style).pack(anchor="w", padx=40)


        def mostrar_detalles(event):
            seleccion = lista_proyectos.curselection()
            if seleccion:
                index = seleccion[0]
                proyecto = lista_proyectos.proyectos_data[index]
                mostrar_detalles_ventana(proyecto)

        tk.Label(listado_proyectos_empresa_win, text="Listado de Proyectos", font=("Helvetica", 18, "bold"), bg="#eaf2f8", fg="#2e4053").pack(pady=20)

        lista_proyectos = tk.Listbox(listado_proyectos_empresa_win, width=60, height=10, font=("Helvetica", 12), bg="#d6eaf8",fg="#2e4053", bd=2, relief="solid", selectmode="browse")
        lista_proyectos.pack(pady=10)

        proyectos = seleccionar_proyectos_por_empresa(CIF)
        lista_proyectos.proyectos_data = proyectos  # Guardamos los proyectos completos

        for proyecto in proyectos:
            lista_proyectos.insert(tk.END, proyecto[4])  # Mostramos solo el nombre en la lista

        lista_proyectos.bind("<Double-Button-1>", mostrar_detalles)

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

        boton_frame = tk.Frame(listado_proyectos_empresa_win, bg="#eaf2f8")
        boton_frame.pack(pady=20)

        tk.Button(boton_frame, text="Insertar", **btn_style).grid(row=0, column=0, padx=10)
        tk.Button(boton_frame, text="Eliminar", **btn_style).grid(row=0, column=1, padx=10)

        listado_proyectos_empresa_win.mainloop()
    
    
    
    form_frame = tk.Frame(consultar_win, bg="#eaf2f8")
    form_frame.pack(pady=10)
    form_frame.grid_columnconfigure(0, weight=1)  # espacio izquierda
    form_frame.grid_columnconfigure(1, weight=0)  # label CIF
    form_frame.grid_columnconfigure(2, weight=0)  # entrada CIF
    form_frame.grid_columnconfigure(3, weight=1)  # espacio derecha

    label_style = {"font": ("Helvetica", 12, "bold"), "bg": "#eaf2f8", "fg": "#2e4053"}
    entry_style = {"font": ("Helvetica", 12), "width": 30}

    titulo = tk.Label(form_frame, text="Consultar Empresa", font=("Helvetica", 20, "bold"), bg="#eaf2f8", fg="#2e4053")
    titulo.grid(row=0, column=0, columnspan=4, pady=(10, 20))

    # CIF label y entrada
    tk.Label(form_frame, text="CIF:", **label_style).grid(row=1, column=0, sticky="e", padx=10, pady=10)
    CIF_entry = tk.Entry(form_frame, **entry_style)
    CIF_entry.grid(row=1, column=1, sticky="w", padx=10, pady=10)

    # Resultado label alineado con el formulario
    resultado_label = tk.Label(form_frame, font=("Helvetica", 12, 'bold'), bg="#d6eaf8", fg="#2e4053",width=40, height=8, anchor="w", justify="left", bd=2, relief="solid")
    resultado_label.grid(row=2, column=0,columnspan=2, sticky="w", padx=10, pady=(10, 10))


    
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

    button_frame = tk.Frame(consultar_win, bg="#eaf2f8")
    button_frame.pack(pady=10)

    

    tk.Button(button_frame, text="Buscar", command=select, **btn_style).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Volver", command=cerrar_e_ir_menu, **btn_style).grid(row=0, column=1, padx=10)

    consultar_win.mainloop()


root = tk.Tk()
root.title("Gestión de Empresas")
root.geometry("700x700+0+0")
root.minsize(600,700)
root.config(bg="#eaf2f8")

logo = tk.PhotoImage(file="C:/Users/Ari/Documents/PRACTICAS/PYTHON/proyecto_practicas/logo_sinfondo.png")


titulo = tk.Label(root, image=logo)
titulo.pack(pady=20)


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
tk.Button(boton_frame, text="Consultar Empresas", command=ventana_consultar_empresa, **btn_style).grid(row=1, column=0, pady=10, padx=20)
tk.Button(boton_frame, text="Actualizar Empresa", command=ventana_actualizar_empresa, **btn_style).grid(row=2, column=0, pady=10, padx=20)
tk.Button(boton_frame, text="Eliminar Empresa", command=ventana_eliminar_empresa, **btn_style).grid(row=3, column=0, pady=10, padx=20)


root.mainloop()