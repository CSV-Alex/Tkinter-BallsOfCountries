import tkinter as tk
from tkinter import ttk
ventana = tk.Tk()

ancho = 600
alto = 400
tamaño = str(ancho) + "x" + str(alto)
ventana.geometry(tamaño)   
ventana.title("Boton")

#ventana.iconbitmap("icon.ico") #Icono de la ventana
boton = ttk.Button(ventana, text="tecto")
boton.pack()
ventana.mainloop()