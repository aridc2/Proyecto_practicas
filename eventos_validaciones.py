import re
import tkinter as tk
from tkinter import messagebox, ttk


def validar_cif(cif):
    patron = r"^[A-Z][0-9]{8}$|^[0-9]{8}[A-Z]$"
    return re.match(patron, cif) is not None

def validacion_CIF(event):
    valor = event.widget.get()
    if not validar_cif(valor):
        event.widget.config(bg="#e98a92")
        messagebox.showerror("Error de validación", 'El CIF consta de 8 numeros y una letra, al final o al inicio')
        
    else:
        event.widget.config(bg="white")


def validar_telefono(formato):
    patron = r"^\+\d{1,4} \d{9}$"
    return bool(re.match(patron, formato)) # Intenta hacer coincidir el formato (formato del telefono) con el patron (la expresión regular) desde el inicio de la cadena.
    # # Si hay coincidencia devuelve un match (true)
    # # Si no hay coincidencia devuelve un none (false)
    
def validacion_telefono(event):
    valor = event.widget.get()
    if not validar_telefono(valor):
        event.widget.config(bg="#e98a92")
        messagebox.showerror("Error de validación", "El Telefono no sigue la estructura definida")
    else:
        event.widget.config(bg="white")

# Cambiar que tambien admita numeros
def validar_nombres(nombre):
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúñÑ0-9\s\.\-]{3,200}$" # \s\.\- Permite los espacios, los puntos y los -
    return bool(re.match(patron, nombre))

def validacion_nombre(event):
    valor = event.widget.get()
    if not validar_nombres(valor):
        event.widget.config(bg="#e98a92")
        messagebox.showerror("Error de validación", "El nombre no sigue la estructura definida")
    else:
        event.widget.config(bg="white")
        
def validar_nombrev2(nombre):
    patron = r"^[A-Za-zÁÉÍÓÚáéíóúñÑs\.\-]{3,200}$" # \s\.\- Permite los espacios, los puntos y los -
    return bool(re.match(patron, nombre))

def validacion_nombrev2(event):
    valor = event.widget.get()
    if not validar_nombres(valor):
        event.widget.config(bg="#e98a92")
        messagebox.showerror("Error de validación", "El nombre de la localidad no sigue la estructura definida")
    else:
        event.widget.config(bg="white")
        
def validar_ID(ID):
    patron = r"^P[0-9]{3}$"
    return bool(re.match(patron, ID))

def validacion_ID(event):
    valor = event.widget.get()
    if not validar_ID(valor):
        event.widget.config(bg="#e98a92")
        messagebox.showerror("Error de validación", "El ID no sigue la estructura definida")
    else:
        event.widget.config(bg="white")
        

class FormularioEmpresa:
    def __init__(self, **kwargs):

        self.campos = {}

        if 'CIF_entry' in kwargs and 'error_cif' in kwargs:
            self.campos['CIF'] = {
                'entry': kwargs['CIF_entry'],
                'error_label': kwargs['error_cif'],
                'validator': validar_cif,
                'error_msg': "Formato inválido. Ej: A12345678"
            }

        if 'nombre_empresa_entry' in kwargs and 'error_nombre' in kwargs:
            self.campos['nombre'] = {
                'entry': kwargs['nombre_empresa_entry'],
                'error_label': kwargs['error_nombre'],
                'validator': validar_nombres,
                'error_msg': "Nombre no válido"
            }

        if 'Localidad_entry' in kwargs and 'error_localidad' in kwargs:
            self.campos['localidad'] = {
                'entry': kwargs['Localidad_entry'],
                'error_label': kwargs['error_localidad'],
                'validator': validar_nombrev2,
                'error_msg': "Localidad no válida"
            }

        if 'telefono_empresa_entry' in kwargs and 'error_telefono' in kwargs:
            self.campos['telefono'] = {
                'entry': kwargs['telefono_empresa_entry'],
                'error_label': kwargs['error_telefono'],
                'validator': validar_telefono,
                'error_msg': "Ej: +34 123456789"
            }

    def validar_campo(self, nombre_campo):
        campo = self.campos[nombre_campo]
        entry = campo['entry']
        label = campo['error_label']
        validator = campo['validator']
        error_msg = campo['error_msg']

        valor = entry.get().strip()
        entry.config(bg="white")
        label.config(text="")
        if valor == '':
            return True
        if not validator(valor):
            entry.config(bg="#e98a92")
            label.config(text=error_msg)
            return False
        return True

    def validar(self):
        valido = True
        for nombre in self.campos:
            if not self.validar_campo(nombre):
                valido = False
        return valido

    
    

class FormularioProyecto:
    def __init__(self, **kwargs):
        
        self.campos = {}
        
        if 'ID_proyecto_entry' in kwargs and 'error_ID_proyecto' in kwargs:
            self.campos['ID'] = {
                'entry': kwargs['ID_proyecto_entry'],
                'error_label': kwargs['error_ID_proyecto'],
                'validator': validar_ID,
                'error_msg': "Formato inválido. Ej: P001"
            }
            
        if 'nombre_proyecto_entry' in kwargs and 'error_nombre_proyecto' in kwargs:
            self.campos['nombre'] = {
                'entry': kwargs['nombre_proyecto_entry'],
                'error_label': kwargs['error_nombre_proyecto'],
                'validator': validar_nombres,
                'error_msg': "Formato inválido. Ej: Scooby Doo Msterios S.A"
            }
            
        if 'jefe_proyecto_entry' in kwargs and 'error_jefe_proyecto' in kwargs:
            self.campos['jefe'] = {
                'entry': kwargs['jefe_proyecto_entry'],
                'error_label': kwargs['error_jefe_proyecto'],
                'validator': validar_nombrev2,
                'error_msg': "Formato inválido. Ej: Mugiwara no Luffy"
            }
    
    def validar_campo(self, nombre_campo):
        campo = self.campos[nombre_campo]
        entry = campo['entry']
        label = campo['error_label']
        validator = campo['validator']
        error_msg = campo['error_msg']

        valor = entry.get().strip()
        entry.config(bg="white")
        label.config(text="")
        if valor == '':
            return True
        if not validator(valor):
            entry.config(bg="#e98a92")
            label.config(text=error_msg)
            return False
        return True

    def validar(self):
        valido = True
        for nombre in self.campos:
            if not self.validar_campo(nombre):
                valido = False
        return valido