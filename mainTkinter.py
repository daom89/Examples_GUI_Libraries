# https://docs.python.org/es/3/library/tkinter.html
# Viene incluida en la instalacion de python
# https://www.youtube.com/watch?v=YXPyB4XeYLA
# https://customtkinter.tomschimansky.com/

import tkinter as tk
import customtkinter as ctk

from Ejercicio1 import Ejercicio1

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Creamos la ventana principal
ventana = ctk.CTk()
ventana.title("Ejercicio 1 - Calcular Cociente")
ventana.geometry("300x300")

title = ctk.CTkLabel(ventana, text="Ejercicio 1 - Calcular Cociente", fg_color="transparent",
                     text_color="white", font=("Helvetica", 18))
title.pack()
# title.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

etiqueta1 = ctk.CTkLabel(ventana, text="Ingrese el primer valor:")
etiqueta1.pack()

# Creamos un campo de texto para que el usuario ingrese el primer valor
number_1 = ctk.CTkEntry(ventana, placeholder_text="0")
number_1.pack()
# number_1.place(relx=0.5, rely=0.4, anchor=customtkinter.CENTER)


# Creamos una etiqueta para indicar al usuario que ingrese el segundo valor
etiqueta2 = ctk.CTkLabel(ventana, text="Ingrese el segundo valor:")
etiqueta2.pack()

number_2 = ctk.CTkEntry(ventana, placeholder_text="0")
number_2.pack()
# number_2.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Creamos una etiqueta para mostrar el resultado o el mensaje de error
etiqueta3 = ctk.CTkLabel(ventana, text="", fg_color="transparent", text_color="green", font=("Helvetica", 16))
etiqueta3.pack()


# etiqueta3.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)


# Definimos una función que se ejecutará cuando el usuario presione el botón de calcular
def calcular():
    # Obtenemos los valores ingresados por el usuario
    a = number_1.get()
    b = number_2.get()
    # Intentamos convertirlos a enteros
    try:
        a = int(a)
        b = int(b)
        # Si el segundo valor es cero, mostramos un mensaje de error
        if b == 0:
            etiqueta3.configure(text="No se puede dividir por cero")
        # Si no, calculamos el cociente y lo mostramos
        else:
            cociente = a / b
            etiqueta3.configure(text="El cociente es: " + str(cociente))
    # Si los valores no son enteros, mostramos otro mensaje de error
    except ValueError:
        etiqueta3.configure(text="Los valores deben ser enteros")


# Creamos un botón para que el usuario pueda calcular el cociente
boton = ctk.CTkButton(master=ventana, text="Calcular", command=calcular)
boton.pack()
# boton.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

# Iniciamos el bucle principal de la ventana
ventana.mainloop()
