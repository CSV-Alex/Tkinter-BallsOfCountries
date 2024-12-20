import tkinter as tk

ventana = tk.Tk()

ancho = 800
alto = 600
tamaño = str(ancho) + "x" + str(alto)
ventana.geometry(tamaño)

ventana.title("Primera ventana")
ventana.mainloop() #Siempre debems poner al final




