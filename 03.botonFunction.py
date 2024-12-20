import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()

ancho = 600
alto = 400
tamaño = str(ancho) + "x" + str(alto)
ventana.geometry(tamaño)   
ventana.title("Boton")

def click():
    print("Has hecho click en el boton")
    boton01.config(text="Has hecho click") #cambia el texto del boton

#ventana.iconbitmap("icon.ico") #Icono de la ventana
boton01 = ttk.Button(ventana, text="tecto")
boton01.pack()

boton02 = ttk.Button(ventana, text="tecto2_Click me", command=click)#nombre click funcion
boton02.pack()


ventana.mainloop()