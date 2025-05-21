import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import mysql.connector as mysql
from config import *
from validaciones import FormularioEmpresa, FormularioProyecto



# Añadir campos desplegables para seleccionar el CIF
# Que el usuario pida el nombre de la empresa

###################################################
# ~~~~~~~~~~~~~~~~~~~EMPRESAS~~~~~~~~~~~~~~~~~~~~ #
###################################################

#Importar los posibles valores de tipos de sociedad y sectores
tipos_sociedad = Empresa.v_tipos_sociedad
sectores = Empresa.v_sectores

#Importar los posibles valores de tipos de Estado y Facturabilidad
estado = Proyecto.v_estado
facturable = Proyecto.v_facturable


def cerrar_ventana(ventana_cerrar,ventana_abrir):
    ventana_cerrar.destroy()
    ventana_abrir.deiconify()

def extraer_todas_las_Empresas():
        try:
            con = mysql.connect(
                host='localhost',
                user='root',
                password='josegras',
                database='gestionProyectos'
            )
            cursor = con.cursor()
            cursor.execute("SELECT CIF, Nombre FROM Empresa")
            resultado = cursor.fetchall()
            
            con.close()
            return resultado
        except Exception as e:
            tk.messagebox.showinfo('Error',str(e))



def campos_validos_empresa_insertar(CIF_entry, error_cif,nombre_empresa_entry, error_nombre,Localidad_entry, error_localidad,telefono_empresa_entry, error_telefono):
    formulario = FormularioEmpresa(
        CIF_entry=CIF_entry, error_cif=error_cif,
        nombre_empresa_entry=nombre_empresa_entry, error_nombre=error_nombre,
        Localidad_entry=Localidad_entry, error_localidad=error_localidad,
        telefono_empresa_entry=telefono_empresa_entry, error_telefono=error_telefono
    )
    return formulario.validar()

def campos_validos_empresa_actualizar(nombre_empresa_entry, error_nombre,Localidad_entry, error_localidad,telefono_empresa_entry, error_telefono):
    formulario = FormularioEmpresa(
        nombre_empresa_entry=nombre_empresa_entry, error_nombre=error_nombre,
        Localidad_entry=Localidad_entry, error_localidad=error_localidad,
        telefono_empresa_entry=telefono_empresa_entry, error_telefono=error_telefono
    )
    return formulario.validar()

def campos_validos_proyecto_insertar(ID_proyecto_entry, error_ID_proyecto, nombre_proyecto_entry, error_nombre_proyecto,jefe_proyecto_entry, error_jefe_proyecto):
    formulario = FormularioProyecto(
        ID_proyecto_entry = ID_proyecto_entry, error_ID_proyecto = error_ID_proyecto, 
        nombre_proyecto_entry = nombre_proyecto_entry, error_nombre_proyecto = error_nombre_proyecto, 
        jefe_proyecto_entry= jefe_proyecto_entry, error_jefe_proyecto = error_jefe_proyecto
    )
    return formulario.validar()

def campos_validos_proyectos_actualizar(nombre_proyecto_entry, error_nombre_proyecto,jefe_proyecto_entry, error_jefe_proyecto):
    formulario = FormularioProyecto(
        nombre_proyecto_entry = nombre_proyecto_entry, error_nombre_proyecto = error_nombre_proyecto, 
        jefe_proyecto_entry= jefe_proyecto_entry, error_jefe_proyecto = error_jefe_proyecto
    )
    return formulario.validar()
#ventana ocupada de la accion de rellenar los datos de inserccion de empresa y de ejecutar la funcion insert
def ventana_inserccion_empresa():

    root.withdraw()
    insertar_win = tk.Toplevel()
    insertar_win.geometry('800x500')
    insertar_win.minsize(600,500)
    insertar_win.title('Gestor de proyectos')
    insertar_win.config(bg="#eaf2f8")


    def insert():
        if not campos_validos_empresa_insertar(CIF_entry, error_cif,nombre_empresa_entry, error_nombre,Localidad_entry, error_localidad,telefono_empresa_entry, error_telefono):
            return #Si algún campo no pasa la validación, salida sin insertar    
        
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

    def buscar():

        no_existe=True
        CIF = CIF_entry.get().strip()
        
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
            con.close()
            if resultado != None:
                tk.messagebox.showinfo('Resultado', 'Se ha encontrado ya una empresa con ese CIF')
                no_existe=False
                return no_existe
            else:
                return no_existe
            

        except Exception as e:
            tk.messagebox.showerror('Error',str(e))
    
    def comprobacion_de_cif():
        if buscar()==True:
            insert()
        else:
            return
    
    titulo = tk.Label(insertar_win, text="Insertar Empresa", font=("Helvetica", 20, "bold"), bg="#eaf2f8", fg="#2e4053")
    titulo.pack(pady=20)

    form_frame = tk.Frame(insertar_win, bg="#eaf2f8")
    form_frame.pack(pady=10)

    
    label_style = {"font": ("Helvetica", 12), "bg": "#eaf2f8", "fg": "#2e4053"}
    entry_style = {"font": ("Helvetica", 12), "width": 30}

    
    tk.Label(form_frame, text="CIF:", **label_style).grid(row=0, column=0, sticky="e", padx=10, pady=10)
    CIF_entry = tk.Entry(form_frame, **entry_style)
    CIF_entry.grid(row=0, column=1)
    # CIF_entry.bind("<FocusOut>", validacion_CIF) # <FocusOut> es el evento que permite que al salir de la caja compruebe si lo introducido sigue las restricciones
    error_cif = tk.Label(form_frame, text="", fg="red", bg="#eaf2f8", font=("Helvetica", 9))
    error_cif.grid(row=0, column=2, sticky="w")


    tk.Label(form_frame, text="Nombre Empresa:", **label_style).grid(row=1, column=0, sticky="e", padx=10, pady=10)
    nombre_empresa_entry = tk.Entry(form_frame, **entry_style)
    nombre_empresa_entry.grid(row=1, column=1)
    #nombre_empresa_entry.bind("<FocusOut>", validacion_nombre)
    error_nombre = tk.Label(form_frame, text="", fg="red", bg="#eaf2f8", font=("Helvetica", 9))
    error_nombre.grid(row=1, column=2, sticky="w")


    tk.Label(form_frame, text="Tipo de Sociedad:", **label_style).grid(row=2, column=0, sticky="e", padx=10, pady=10)
    tipo_sociedad_combo = ttk.Combobox(form_frame, values=tipos_sociedad, font=("Helvetica", 12), state="readonly", width=28)
    tipo_sociedad_combo.grid(row=2, column=1)
    
    
    tk.Label(form_frame, text="Sector:", **label_style).grid(row=3, column=0, sticky="e", padx=10, pady=10)
    Sector_combo = ttk.Combobox(form_frame, values=sectores, font=("Helvetica", 12), state="readonly", width=28)
    Sector_combo.grid(row=3, column=1)


    tk.Label(form_frame, text="Localidad:", **label_style).grid(row=4, column=0, sticky="e", padx=10, pady=10)
    Localidad_entry = tk.Entry(form_frame, **entry_style)
    Localidad_entry.grid(row=4, column=1)
    # Localidad_entry.bind("<FocusOut>", validacion_nombre)
    error_localidad = tk.Label(form_frame, text="", fg="red", bg="#eaf2f8", font=("Helvetica", 9))
    error_localidad.grid(row=4, column=2, sticky="w")


    tk.Label(form_frame, text="Teléfono:", **label_style).grid(row=5, column=0, sticky="e", padx=10, pady=10)
    telefono_empresa_entry = tk.Entry(form_frame, **entry_style)
    telefono_empresa_entry.grid(row=5, column=1)
    # telefono_empresa_entry.bind ("<FocusOut>", validacion_telefono)
    error_telefono = tk.Label(form_frame, text="", fg="red", bg="#eaf2f8", font=("Helvetica", 9))
    error_telefono.grid(row=5, column=2, sticky="w")

    
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

    tk.Button(button_frame, text="Insertar", command=comprobacion_de_cif, **btn_style).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Volver", command=lambda: cerrar_ventana(insertar_win,root), **btn_style).grid(row=0, column=1, padx=10)
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

    tk.Button(btn_frame, text="Volver", command=lambda: cerrar_ventana(eliminar_win,root), bg="#3498db", fg="white", activebackground="#7f8c8d", font=("Helvetica", 12, "bold"), width=15, height=2, bd=0, cursor="hand2").grid(row=0, column=1, padx=10)

    eliminar_win.mainloop()

#Ventana para introducir el cif y si encuentra la empresa abre otra ventana para introducir los datos a actualizar
def ventana_actualizar_empresa():
    root.withdraw()
    actualizar_win = tk.Toplevel()
    actualizar_win.geometry('800x300')
    actualizar_win.minsize(500,300)
    actualizar_win.title('Gestor de proyectos')
    actualizar_win.config(bg="#eaf2f8")

    empresas_totales=extraer_todas_las_Empresas()
    empresa_dict = {nombre: cif for cif, nombre in empresas_totales}
    nombres_empresas=list(empresa_dict.keys())

    def buscar():
        nombre_seleccionado = empresa_combo.get()
        CIF = empresa_dict.get(nombre_seleccionado)
        
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

                con.close()
                empresa_combo.set('')

            except Exception as e:
                tk.messagebox.showerror('Error',str(e))

    def ventana_rellenar_campos(CIF):
        CIF_buscado=CIF
        actualizar_win.withdraw()
        actualizar_campos_win = tk.Toplevel()
        actualizar_campos_win.geometry('800x500')
        actualizar_campos_win.minsize(500,500)
        actualizar_campos_win.title('Gestor de proyectos')
        actualizar_campos_win.config(bg="#eaf2f8")
        
        # if not campos_validos_empresa(CIF_entry, error_cif,nombre_empresa_entry, error_nombre,Localidad_entry, error_localidad,telefono_empresa_entry, error_telefono):
            #return #Si algún campo no pasa la validación, salida sin insertar  

        def update(CIF_buscado):
            if not campos_validos_empresa_actualizar(nombre_empresa_entry, error_nombre,Localidad_entry, error_localidad,telefono_empresa_entry, error_telefono):
                return #Si algún campo no pasa la validación, salida sin insertar    
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
                    tipo_sociedad_combo.set('')
                    Sector_combo.set('')
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
        error_nombre = tk.Label(form_frame, text="", fg="red", bg="#eaf2f8", font=("Helvetica", 9))
        error_nombre.grid(row=1, column=2, sticky="w")

        tk.Label(form_frame, text="Tipo de sociedad:", **label_style).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        tipo_sociedad_combo = ttk.Combobox(form_frame, values=tipos_sociedad, font=("Helvetica", 12), state="readonly", width=28)
        tipo_sociedad_combo.grid(row=2, column=1)

        tk.Label(form_frame, text="Sector:", **label_style).grid(row=3, column=0, sticky="e", padx=10, pady=10)
        Sector_combo = ttk.Combobox(form_frame, values=sectores, font=("Helvetica", 12), state="readonly", width=28)
        Sector_combo.grid(row=3, column=1)

        tk.Label(form_frame, text="Localidad:", **label_style).grid(row=4, column=0, sticky="e", padx=10, pady=10)
        Localidad_entry = tk.Entry(form_frame, **entry_style)
        Localidad_entry.grid(row=4, column=1)
        error_localidad = tk.Label(form_frame, text="", fg="red", bg="#eaf2f8", font=("Helvetica", 9))
        error_localidad.grid(row=4, column=2, sticky="w")

        tk.Label(form_frame, text="Teléfono empresa:", **label_style).grid(row=5, column=0, sticky="e", padx=10, pady=10)
        telefono_empresa_entry = tk.Entry(form_frame, **entry_style)
        telefono_empresa_entry.grid(row=5, column=1)
        error_telefono = tk.Label(form_frame, text="", fg="red", bg="#eaf2f8", font=("Helvetica", 9))
        error_telefono.grid(row=5, column=2, sticky="w")

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
        tk.Button(button_frame, text="Volver", command=lambda: cerrar_ventana(actualizar_campos_win,actualizar_win), **btn_style).grid(row=0, column=1, padx=10)
    

    titulo = tk.Label(actualizar_win, text="Actualizar Empresa", font=("Helvetica", 20, "bold"), bg="#eaf2f8", fg="#2e4053")
    titulo.pack(pady=20)

    
    form_frame = tk.Frame(actualizar_win, bg="#eaf2f8")
    form_frame.pack(pady=10)

    label_style = {"font": ("Helvetica", 12), "bg": "#eaf2f8", "fg": "#2e4053"}
    entry_style = {"font": ("Helvetica", 12), "width": 30}

    tk.Label(form_frame, text="Empresa:", **label_style).grid(row=0, column=0, sticky="e", padx=10, pady=10)
    empresa_combo = ttk.Combobox(form_frame, values=nombres_empresas, font=("Helvetica", 12), state="readonly", width=28)
    empresa_combo.grid(row=0, column=1, sticky="w", padx=10, pady=10)

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
    tk.Button(button_frame, text="Volver", command=lambda: cerrar_ventana(actualizar_win,root), **btn_style).grid(row=0, column=1, padx=10)

    actualizar_win.mainloop()

#Ventana para introducir el cif y si encuentra la empresa imprime sus datos
def ventana_consultar_empresa():
    root.withdraw()
    consultar_win = tk.Toplevel()
    consultar_win.geometry('800x400')
    consultar_win.minsize(800,400)
    consultar_win.title('Gestor de proyectos')
    consultar_win.config(bg="#eaf2f8")

    empresas_totales=extraer_todas_las_Empresas()
    empresa_dict = {nombre: cif for cif, nombre in empresas_totales}
    nombres_empresas=list(empresa_dict.keys())

    def info_empresas():

        def select(CIF):
            
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
        
        nombre_seleccionado = empresa_combo.get()
        CIF = empresa_dict.get(nombre_seleccionado)
        select(CIF)

    def ventana_gestionar_proyectos(CIF):
        consultar_win.withdraw()
        listado_proyectos_empresa_win = tk.Toplevel()
        listado_proyectos_empresa_win.geometry('800x500')
        listado_proyectos_empresa_win.minsize(600,500)
        listado_proyectos_empresa_win.title('Gestor de proyectos')
        listado_proyectos_empresa_win.config(bg="#eaf2f8")

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

        def seleccionar_proyectos_por_empresa(CIF):


            # Conexión a la base de datos
            con = mysql.connect(
                host='localhost',
                user='root',
                password='josegras',
                database='gestionProyectos'
            )
            cursor = con.cursor()
            #Buscar nombre empresa
            cursor.execute("SELECT Nombre FROM Empresa WHERE CIF = %s", (CIF,))
            Nombre_empresa_tupla = cursor.fetchone()
            Nombre_empresa=Nombre_empresa_tupla[0]
            # Buscar proyectos asociados a esa empresa
            cursor.execute("""
                SELECT ID_proyecto, Nombre_proyecto, Estado, Facturable, Jefe_proyecto, Fecha_Inicio, Fecha_Final
                FROM Proyecto
                WHERE CIF = %s
            """, (CIF,))
            proyectos_sin_datos_empresa = cursor.fetchall() 

            proyectos=[]
            for p in proyectos_sin_datos_empresa:
                proyecto = Proyecto(
                    CIF=CIF,
                    nombre_empresa=Nombre_empresa,
                    ID=p[0],
                    nombre=p[1],
                    estado=p[2],
                    facturable=p[3],
                    jefe_pr=p[4],
                    fecha_in=p[5],
                    fecha_fin=p[6]
                )
                proyectos.append(proyecto)
            con.close()
            return proyectos

        def imprimir_proyectos():
            proyectos = seleccionar_proyectos_por_empresa(CIF)
            if not proyectos:
                tk.messagebox.showinfo('Status', 'No hay proyectos')
                lista_proyectos.proyectos_data = []  
            else:
                lista_proyectos.proyectos_data = proyectos
                for proyecto in proyectos:
                    lista_proyectos.insert(tk.END, f'  {proyecto.nombre}')# Mostramos solo el nombre en la lista
        
        def mostrar_detalles_ventana(proyecto):
        
            listado_proyectos_empresa_win.withdraw()
            detalle_win = tk.Toplevel()
            detalle_win.title("Detalles del Proyecto")
            detalle_win.geometry("550x400")
            detalle_win.config(bg="#eaf2f8")

            def ventana_actualizar_proyecto(proyecto):
                detalle_win.withdraw()
                actualizar_proyecto_win = tk.Toplevel()
                actualizar_proyecto_win.geometry('800x500')
                actualizar_proyecto_win.minsize(600,500)
                actualizar_proyecto_win.title('Gestor de proyectos')
                actualizar_proyecto_win.config(bg="#eaf2f8")
                
                def update_proyecto(proyecto):
                    
                    if not campos_validos_proyectos_actualizar(nombre_proyecto_entry, error_nombre_proyecto,jefe_proyecto_entry, error_jefe_proyecto):
                        return
                    
                    nombre_proyecto = nombre_proyecto_entry.get().strip()
                    estado = estado_combo.get()
                    facturable = facturable_combo.get()
                    jefe_proyecto = jefe_proyecto_entry.get().strip()
                    fecha_Inicio = fecha_Inicio_entry.get()
                    fecha_Final = fecha_Final_entry.get()
                    CIF=proyecto.CIF
                    ID_proyecto=proyecto.ID
                    
                    try:
                        con = mysql.connect(
                            host='localhost',
                            user='root',
                            password='josegras',
                            database='gestionProyectos'
                        )
                        cursor = con.cursor()
                        
                        if nombre_proyecto!='':
                            sql = 'UPDATE Proyecto SET Nombre_proyecto = %s WHERE ID_proyecto = %s AND CIF = %s'
                            valores = (nombre_proyecto, ID_proyecto, CIF)
                            cursor.execute(sql, valores)
                            
                        if estado!='':
                            sql = 'UPDATE Proyecto SET Estado = %s WHERE ID_proyecto = %s AND CIF = %s'
                            valores = (estado, ID_proyecto, CIF)
                            cursor.execute(sql, valores)
                        
                        if facturable!='':
                            sql = 'UPDATE Proyecto SET Facturable = %s WHERE ID_proyecto = %s AND CIF = %s'
                            valores = (facturable, ID_proyecto, CIF)
                            cursor.execute(sql, valores)
                            
                        if jefe_proyecto!='':
                            sql = 'UPDATE Proyecto SET Jefe_proyecto = %s WHERE ID_proyecto = %s AND CIF = %s'
                            valores = (jefe_proyecto, ID_proyecto, CIF)
                            cursor.execute(sql, valores)    
                            
                        if fecha_Inicio!='':
                            sql = 'UPDATE Proyecto SET Fecha_Inicio = %s WHERE ID_proyecto = %s AND CIF = %s'
                            valores = (fecha_Inicio, ID_proyecto, CIF)
                            cursor.execute(sql, valores)
                            
                        if fecha_Final!='':
                            sql = 'UPDATE Proyecto SET Fecha_Final = %s WHERE ID_proyecto = %s AND CIF = %s'
                            valores = (fecha_Final, ID_proyecto, CIF)
                            cursor.execute(sql, valores)
                            

                        con.commit() #Sirve para que los cambios que se hagan en la BBDD se guarden

                        if nombre_proyecto == '' and estado == '' and facturable == '' and jefe_proyecto == '' and fecha_Inicio == '' and fecha_Final == '':
                            tk.messagebox.showinfo('Status', 'Ningun dato ha sido actualizado')
                        else:
                            tk.messagebox.showinfo('Status', 'Datos actualizados correctamente')
                            
                            nombre_proyecto_entry.delete(0, 'end')
                            estado_combo.delete(0, 'end')
                            facturable_combo.delete(0, 'end')
                            jefe_proyecto_entry.delete(0, 'end')
                            fecha_Inicio_entry.delete(0, 'end')
                            fecha_Final_entry.delete(0, 'end')

                        #cursor.execute('SELECT * FROM Proyecto WHERE ID_proyecto = %s AND CIF = %s',(ID_proyecto,CIF))
                        #resultado= cursor.fetchone()
                        #proyecto=Proyecto(resultado[0],resultado[1],resultado[2],resultado[3],resultado[4],resultado[5],resultado[6],resultado[7],resultado[8])
                        con.close()

                        actualizar_proyecto_win.withdraw()
                        mostrar_detalles_ventana(proyecto)

                        
                    except Exception as e: #Guarda el error y lo imprime en una ventana emergente
                        tk.messagebox.showerror('Error',str(e))
                        
                titulo = tk.Label(actualizar_proyecto_win, text="Actualizar Proyecto", font=("Helvetica", 20, "bold"), bg="#eaf2f8", fg="#2e4053")
                titulo.pack(pady=20)

                form_frame = tk.Frame(actualizar_proyecto_win, bg="#eaf2f8")
                form_frame.pack(pady=10)
    
                
                label_style = {"font": ("Helvetica", 12), "bg": "#eaf2f8", "fg": "#2e4053"}
                entry_style = {"font": ("Helvetica", 12), "width": 30}
                
                tk.Label(form_frame, text="Nombre:", **label_style).grid(row=1, column=0, sticky="e", padx=10, pady=10)
                nombre_proyecto_entry = tk.Entry(form_frame, **entry_style)
                nombre_proyecto_entry.grid(row=1, column=1)
                error_nombre_proyecto = tk.Label(form_frame, text="", fg='red', bg="#eaf2f8", font=("Helvetica", 9))
                error_nombre_proyecto.grid(row=1, column=2, sticky="w")

                tk.Label(form_frame, text="Estado:", **label_style).grid(row=2, column=0, sticky="e", padx=10, pady=10)
                estado_combo = ttk.Combobox(form_frame, values=estado, font=("Helvetica", 12), state="readonly", width=28)
                estado_combo.grid(row=2, column=1)

                tk.Label(form_frame, text="Facturable:", **label_style).grid(row=3, column=0, sticky="e", padx=10, pady=10)
                facturable_combo = ttk.Combobox(form_frame, values=facturable, font=("Helvetica", 12), state="readonly", width=28)
                facturable_combo.grid(row=3, column=1)

                tk.Label(form_frame, text="Jefe Proyecto:", **label_style).grid(row=4, column=0, sticky="e", padx=10, pady=10)
                jefe_proyecto_entry = tk.Entry(form_frame, **entry_style)
                jefe_proyecto_entry.grid(row=4, column=1)
                error_jefe_proyecto = tk.Label(form_frame, text="", fg='red',bg="#eaf2f8", font=("Helvetica", 9))
                error_jefe_proyecto.grid(row=4, column=2, sticky="w")

                tk.Label(form_frame, text="Fecha Inicio:", **label_style).grid(row=5, column=0, sticky="e", padx=10, pady=10)
                fecha_Inicio_entry = DateEntry(form_frame, date_pattern='yyyy-mm-dd', font=("Helvetica", 12), width=28)
                fecha_Inicio_entry.grid(row=5, column=1)
                fecha_Inicio_entry.delete(0, 'end')

                
                tk.Label(form_frame, text="Fecha Finlaización:", **label_style).grid(row=6, column=0, sticky="e", padx=10, pady=10)
                fecha_Final_entry = DateEntry(form_frame, date_pattern='yyyy-mm-dd', font=("Helvetica", 12), width=28)
                fecha_Final_entry.grid(row=6, column=1)
                fecha_Final_entry.delete(0, 'end')

                
                btn_style = {
                "font": ("Helvetica", 12, "bold"),
                "width": 20,
                "height": 1,
                "bg": "#3498db",
                "fg": "white",
                "bd": 0,
                "activebackground": "#2980b9",
                "cursor": "hand2"
            }
    
                tk.Button(form_frame, text="Volver", command=lambda: cerrar_ventana(actualizar_proyecto_win, detalle_win), **btn_style).grid(row=8, column=0, pady=20)
                tk.Button(form_frame, text="Actualizar informacion",command=lambda: update_proyecto(proyecto), **btn_style).grid(row=8, column=1, pady=20)

            frame_contenido = tk.Frame(detalle_win, bg="#eaf2f8")
            frame_contenido.pack(padx=20, pady=20, fill="both")

            label_style = {"font": ("Helvetica", 12, "bold"), "bg": "#eaf2f8", "fg": "#416286"}
            value_style = {"font": ("Helvetica", 12, "bold"), "bg": "#eaf2f8", "fg": "#2e4053"}

            # Etiquetas y valores usando grid dentro del frame
            tk.Label(frame_contenido, text="Empresa:", **label_style).grid(row=0, column=0, sticky="w", pady=(0, 10))
            tk.Label(frame_contenido, text=proyecto.nombre_empresa, **value_style).grid(row=0, column=1, sticky="w", pady=(0, 10))

            tk.Label(frame_contenido, text="ID Proyecto:", **label_style).grid(row=1, column=0, sticky="w", pady=(0, 10))
            tk.Label(frame_contenido, text=proyecto.ID, **value_style).grid(row=1, column=1, sticky="w", pady=(0, 10))

            tk.Label(frame_contenido, text="Nombre:", **label_style).grid(row=2, column=0, sticky="w", pady=(0, 10))
            tk.Label(frame_contenido, text=proyecto.nombre, **value_style).grid(row=2, column=1, sticky="w", pady=(0, 10))

            tk.Label(frame_contenido, text="Fecha de Inicio:", **label_style).grid(row=3, column=0, sticky="w", pady=(0, 10))
            tk.Label(frame_contenido, text=proyecto.fecha_in, **value_style).grid(row=3, column=1, sticky="w", pady=(0, 10))

            tk.Label(frame_contenido, text="Fecha de Finalización:", **label_style).grid(row=4, column=0, sticky="w", pady=(0, 10))
            tk.Label(frame_contenido, text=proyecto.fecha_fin, **value_style, wraplength=300, justify="left").grid(row=4, column=1, sticky="w", pady=(0, 10))

            tk.Label(frame_contenido, text="Estado:", **label_style).grid(row=5, column=0, sticky="w", pady=(0, 10))
            tk.Label(frame_contenido, text=proyecto.estado, **value_style).grid(row=5, column=1, sticky="w", pady=(0, 10))

            tk.Label(frame_contenido, text="Facturable:", **label_style).grid(row=6, column=0, sticky="w", pady=(0, 10))
            tk.Label(frame_contenido, text=proyecto.facturable, **value_style).grid(row=6, column=1, sticky="w", pady=(0, 10))

            tk.Label(frame_contenido, text="Jefe de proyecto:", **label_style).grid(row=7, column=0, sticky="w", pady=(0, 10))
            tk.Label(frame_contenido, text=proyecto.jefe_pr, **value_style).grid(row=7, column=1, sticky="w", pady=(0, 10))

            btn_style = {
                "font": ("Helvetica", 12, "bold"),
                "width": 20,
                "height": 1,
                "bg": "#3498db",
                "fg": "white",
                "bd": 0,
                "activebackground": "#2980b9",
                "cursor": "hand2"
            }

        
            tk.Button(frame_contenido, text="Volver", command=lambda: cerrar_ventana(detalle_win, listado_proyectos_empresa_win), **btn_style).grid(row=8, column=0, pady=20,padx=20)
            tk.Button(frame_contenido, text="Actualizar informacion",command=lambda:ventana_actualizar_proyecto(proyecto),**btn_style).grid(row=8, column=1, pady=20,padx=10)
            
        def eliminar_proyecto(proyecto):
            CIF = proyecto.CIF
            ID_proyecto = proyecto.ID
            
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

            tk.messagebox.showinfo("Status", "Proyecto borrado correctamente")
            con.close()
            lista_proyectos.delete(0, tk.END)
            imprimir_proyectos()

        def mostrar_detalles(event):
            seleccion = lista_proyectos.curselection()
            if seleccion:
                index = seleccion[0]
                proyecto = lista_proyectos.proyectos_data[index]
                mostrar_detalles_ventana(proyecto)

        def seleccion_eliminar_proyecto():
            seleccion=lista_proyectos.curselection()
            if seleccion:
                index = seleccion[0]
                proyecto = lista_proyectos.proyectos_data[index]
                eliminar_proyecto(proyecto)

        ####
        # # Ventana para insertar un nuevo proyecto a la empresa
        def ventana_insertar_proyecto(CIF):
            listado_proyectos_empresa_win.withdraw()
            insertar_proyecto_win=tk.Toplevel()
            insertar_proyecto_win.geometry('800x500')
            insertar_proyecto_win.minsize(600,500)
            insertar_proyecto_win.title('Gestor de Proyectos')
            insertar_proyecto_win.config(bg="#eaf2f8")
            
            def generar_id_proyecto():
                try:
                    con = mysql.connect(
                        host='localhost',
                        user='root',
                        password='josegras',
                        database='gestionProyectos'
                    )
                    cursor = con.cursor()
                    cursor.execute("SELECT ID_proyecto FROM Proyecto ORDER BY ID_proyecto DESC LIMIT 1")    
                    resultado = cursor.fetchone()
                    con.close()
                    
                    if resultado:
                        ultimo_id = resultado[0]
                        numero = int(ultimo_id[1:]) + 1 #Quita la P y suma
                        
                    else:
                        numero = 1
                        
                    nuevo_id = f'P{numero:03d}' # Mantiene siempre el formato p001, p002...
                    return nuevo_id
                    
                except Exception as e:
                    tk.messagebox.showerror('Error al generar el ID', str(e))
                    return ''
            
            def insertar_proyecto(CIF):
                
                if not campos_validos_proyecto_insertar(ID_proyecto_entry, error_ID_proyecto, nombre_proyecto_entry, error_nombre_proyecto,jefe_proyecto_entry, error_jefe_proyecto):
                    return 
 
                ID_proyecto = ID_proyecto_entry.get() 
                nombre_proyecto = nombre_proyecto_entry.get()
                estado = estado_combo.get()
                facturable = facturable_combo.get()
                jefe_proyecto = jefe_proyecto_entry.get()
                fecha_Inicio = fecha_Inicio_entry.get()
                fecha_Final = fecha_Final_entry.get()

                if ID_proyecto == '' or nombre_proyecto == '' or estado == '' or facturable == '' or jefe_proyecto == '' or fecha_Inicio == '' or fecha_Final == '':
                    tk.messagebox.showerror('ALERT, Por favor introduzca todos los valores para insertar un nuevo proyecto')
                else:
                    try:
                        con = mysql.connect(
                            host='localhost',
                            user='root',
                            password='josegras',
                            database='gestionProyectos'
                        )
                        cursor = con.cursor()
                        
                        cursor.execute("SELECT COUNT(*) FROM Proyecto WHERE ID_proyecto = %s", (ID_proyecto,))
                        if cursor.fetchone()[0] > 0:
                            tk.messagebox.showerror("Error", f"El ID de proyecto '{ID_proyecto}' ya existe")
                            return
                        
                        sql = "INSERT INTO Proyecto (CIF, ID_proyecto, Nombre_proyecto, Estado, Facturable, Jefe_proyecto, Fecha_Inicio, Fecha_Final) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)"
                        valores = (CIF,ID_proyecto, nombre_proyecto, estado, facturable, jefe_proyecto, fecha_Inicio, fecha_Final)
                        cursor.execute(sql, valores)
                        con.commit()
                        tk.messagebox.showinfo("Status", "Proyecto insertado correctamente.")
                        
                        ID_proyecto_entry.delete(0, 'end')
                        nombre_proyecto_entry.delete(0, 'end')
                        estado_combo.set("")
                        facturable_combo.set("")
                        jefe_proyecto_entry.delete(0, 'end')
                        fecha_Inicio_entry.delete(0, 'end')
                        fecha_Final_entry.delete(0, 'end')
                        
                        con.close()
                        lista_proyectos.delete(0, tk.END)
                        imprimir_proyectos()
                    except Exception as e: #Guarda el error y lo imprime en una ventana emergente
                        tk.messagebox.showerror('Error',str(e))
                    

            titulo = tk.Label(insertar_proyecto_win, text="Insertar Proyecto", font=("Helvetica", 20, "bold"), bg="#eaf2f8", fg="#2e4053")
            titulo.pack(pady=20)

            form_frame = tk.Frame(insertar_proyecto_win, bg="#eaf2f8")
            form_frame.pack(pady=10)

            
            label_style = {"font": ("Helvetica", 12), "bg": "#eaf2f8", "fg": "#2e4053"}
            entry_style = {"font": ("Helvetica", 12), "width": 30}

            
            tk.Label(form_frame, text="ID Proyecto:", **label_style).grid(row=0, column=0, sticky="e", padx=10, pady=10)
            ID_proyecto_entry = tk.Entry(form_frame, **entry_style)
            ID_proyecto_entry.grid(row=0, column=1)
            error_ID_proyecto = tk.Label(form_frame, text="", fg="red", bg="#eaf2f8", font=("Helvetica", 9))
            error_ID_proyecto.grid(row=0, column=2, sticky="w")
            
            #Aqui generas el ID solo una vez al abrir la ventana
            ID_generado = generar_id_proyecto()
            ID_proyecto_entry.insert(0,ID_generado)

            tk.Label(form_frame, text="Nombre:", **label_style).grid(row=1, column=0, sticky="e", padx=10, pady=10)
            nombre_proyecto_entry = tk.Entry(form_frame, **entry_style)
            nombre_proyecto_entry.grid(row=1, column=1)
            error_nombre_proyecto = tk.Label(form_frame, text="", fg="red", bg="#eaf2f8", font=("Helvetica", 9))
            error_nombre_proyecto.grid(row=1, column=2, sticky="w")


            tk.Label(form_frame, text="Estado:", **label_style).grid(row=2, column=0, sticky="e", padx=10, pady=10)
            estado_combo = ttk.Combobox(form_frame, values=estado, font=("Helvetica", 12), state="readonly", width=28)
            estado_combo.grid(row=2, column=1)

            tk.Label(form_frame, text="Facturable:", **label_style).grid(row=3, column=0, sticky="e", padx=10, pady=10)
            facturable_combo = ttk.Combobox(form_frame, values=facturable, font=("Helvetica", 12), state="readonly", width=28)
            facturable_combo.grid(row=3, column=1)

            tk.Label(form_frame, text="Jefe Proyecto:", **label_style).grid(row=4, column=0, sticky="e", padx=10, pady=10)
            jefe_proyecto_entry = tk.Entry(form_frame, **entry_style)
            jefe_proyecto_entry.grid(row=4, column=1)
            error_jefe_proyecto = tk.Label(form_frame, text="", fg="red", bg="#eaf2f8", font=("Helvetica", 9))
            error_jefe_proyecto.grid(row=4, column=2, sticky="w")

            tk.Label(form_frame, text="Fecha Inicio:", **label_style).grid(row=5, column=0, sticky="e", padx=10, pady=10)
            fecha_Inicio_entry = DateEntry(form_frame, date_pattern='yyyy-mm-dd', font=("Helvetica", 12), width=28)
            fecha_Inicio_entry.grid(row=5, column=1)
            
            tk.Label(form_frame, text="Fecha Finalización:", **label_style).grid(row=6, column=0, sticky="e", padx=10, pady=10)
            fecha_Final_entry = DateEntry(form_frame, date_pattern='yyyy-mm-dd', font=("Helvetica", 12), width=28)
            fecha_Final_entry.grid(row=6, column=1)

            fecha_Inicio_entry.delete(0, 'end')
            fecha_Final_entry.delete(0, 'end')
            
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

            button_frame = tk.Frame(insertar_proyecto_win, bg="#eaf2f8")
            button_frame.pack(pady=20)

            tk.Button(button_frame, text="Insertar", command=lambda:insertar_proyecto(CIF), **btn_style).grid(row=0, column=0, padx=10)
            tk.Button(button_frame, text="Volver", command=lambda:cerrar_ventana(insertar_proyecto_win,listado_proyectos_empresa_win), **btn_style).grid(row=0, column=1, padx=10)


        tk.Label(listado_proyectos_empresa_win, text="Listado de Proyectos", font=("Helvetica", 18, "bold"), bg="#eaf2f8", fg="#2e4053").pack(pady=20)



        lista_proyectos = tk.Listbox(listado_proyectos_empresa_win, width=60, height=10, font=("Helvetica", 12, 'bold'), bg="#d6eaf8",fg="#2e4053", bd=2, relief="solid", selectmode="browse")
        lista_proyectos.pack(pady=10)

        imprimir_proyectos()

        lista_proyectos.bind("<Double-Button-1>", mostrar_detalles)


        boton_frame = tk.Frame(listado_proyectos_empresa_win, bg="#eaf2f8")
        boton_frame.pack(pady=20)

        tk.Button(boton_frame, text="Insertar",command=lambda: ventana_insertar_proyecto(CIF), **btn_style).grid(row=0, column=0, padx=10)
        tk.Button(boton_frame, text="Eliminar",command=seleccion_eliminar_proyecto, **btn_style).grid(row=0, column=1, padx=10)
        tk.Button(boton_frame, text="Volver",command=lambda: cerrar_ventana(listado_proyectos_empresa_win,consultar_win), **btn_style).grid(row=0, column=2, padx=10)

        listado_proyectos_empresa_win.mainloop()
    
    
    
    form_frame = tk.Frame(consultar_win, bg="#eaf2f8")
    form_frame.pack(pady=10)
    form_frame.grid_columnconfigure(0, weight=1)  # espacio izquierda
    form_frame.grid_columnconfigure(1, weight=0)  # label CIF
    form_frame.grid_columnconfigure(2, weight=0)  # entrada CIF
    form_frame.grid_columnconfigure(3, weight=1)  # espacio derecha

    label_style = {"font": ("Helvetica", 12, "bold"), "bg": "#eaf2f8", "fg": "#2e4053"}
    #entry_style = {"font": ("Helvetica", 12), "width": 30, "bg": "#ffffff",}

    titulo = tk.Label(form_frame, text="Consultar Empresa", font=("Helvetica", 20, "bold"), bg="#eaf2f8", fg="#2e4053")
    titulo.grid(row=0, column=0, columnspan=4, pady=(10, 20))

    tk.Label(form_frame, text="Empresa:", **label_style).grid(row=1, column=0, sticky="e", padx=10, pady=10)
    empresa_combo = ttk.Combobox(form_frame, values=nombres_empresas, font=("Helvetica", 12), state="readonly", width=28)
    empresa_combo.grid(row=1, column=1, sticky="w", padx=10, pady=10)
    

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

    tk.Button(button_frame, text="Buscar", command=info_empresas, **btn_style).grid(row=0, column=0, padx=10)
    tk.Button(button_frame, text="Volver", command=lambda: cerrar_ventana(consultar_win,root), **btn_style).grid(row=0, column=1, padx=10)

    consultar_win.mainloop()


root = tk.Tk()
root.title("Gestión de Empresas")
root.geometry("700x700+0+0")
root.minsize(600,700)
root.config(bg="#eaf2f8")

# logo = tk.PhotoImage(file="C:/Users/User/Documents/PRACTICAS/PYTHON/proyecto_practicas/logo_sinfondo.png")


# titulo = tk.Label(root, image=logo)
# titulo.pack(pady=20)


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