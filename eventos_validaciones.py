import re
import tkinter as tk
from tkinter import messagebox, ttk
def validar_cif(cif):
    patron = r"^[A-Z]\d{8}$|^\d{8}[A-Z]$"
    if re.match(patron,cif)== True:
        valido=True
    else:
        valido=False
    return valido

def validacion_CIF(event):
    valor = event.widget.get()
    if not validar_cif(valor):
        event.widget.config(bg="#e98a92")
        messagebox.showerror("Error de validación", 'El CIF consta de 8 numeros y una letra, al final o al inicio')
        
    else:
        event.widget.config(bg="white")


def validar_telefono(formato):
    patron = r"^\+\d{1,4} \d{3} \d{3} \d{3}$"
    return bool(re.match(patron, formato)) # Intenta hacer coincidir el formato (formato del telefono) con el patron (la expresión regular) desde el inicio de la cadena.
    # # Si hay coincidencia devuelve un match (true)
    # # Si no hay coincidencia devuelve un none (false)
    
def validacion_telefono(event):
    valor = event.widget.get()
    if not validar_telefono(valor):
        event.widget.config(bg="#e98a92")
        messagebox.showerror("Error de validación", "El Telefono no sigue la estructura definida")
        event.widget.config(bg="white")
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
        event.widget.config(bg="white")
    else:
        event.widget.config(bg="white")
        
def validar_ID(ID):
    patron = r"^PROY-[0-9]{3}$"
    return bool(re.match(patron, ID))

def validacion_ID(event):
    valor = event.widget.get()
    if not validar_ID(valor):
        event.widget.config(bg="#e98a92")
        messagebox.showerror("Error de validación", "El ID no sigue la estructura definida")
        event.widget.config(bg="white")
    else:
        event.widget.config(bg="white")