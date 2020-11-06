# _______________________________________________________
# Universidad del Valle de Guatemala
# CC3056 - Programacion de Microprocesadores
# Andrea Amaya         | Brandon Hernández 
# Laura Tamath
# Proyecto Criptografía RSA
# Desencriptador de archivos
# _______________________________________________________
from tkinter import *

root = Tk()
#root.resizable(0, 0)

# Primer frame
frame = Frame(root, width=1200, height=600)
frame.pack()

#Out_put del cifrado
out_put = Text(frame, width=20, height=10)
out_put.grid(row=4, column=0, padx=10, pady=10)
scroll_out = Scrollbar(frame, command=out_put.yview)
scroll_out.grid(row=4, column=1, sticky="nsew")
out_put.config(yscrollcommand=scroll_out.set)


# Termina Frame

root.mainloop()  # Para que no se cierre la ventana
