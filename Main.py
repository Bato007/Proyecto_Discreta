# _______________________________________________________
# Universidad del Valle de Guatemala
# CC3056 - Programacion de Microprocesadores
# Andrea Amaya         | Brandon Hernández 
# Laura Tamath
# Proyecto Criptografía RSA
# Desencriptador de archivos
# _______________________________________________________
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from os import path
import os

root = Tk()
root.title('Proyecto | Matemática discreta')
root['bg'] = 'gray11' #ivory2
root.call('wm', 'iconphoto', root._w, PhotoImage(file='logo.png'))
root.resizable(False, False)
root.geometry('500x455')

# Primer frame
frame = Frame()
frame.pack()
label = Label(root, text= 'Criptografía RSA', font= ('Calibri Bold','40'), fg='gray99', bg='gray11')
label.place(x = 18, y = 5)

#Función para asegurar que el programa se cerrará
def closing():
    if messagebox.askokcancel("Close program","¿Seguro que quiere cerrar el programa?"):
        root.destroy()
        
#Diseño y funcionamiento de los botones   
Button(text = 'Abrir archivo', bg='coral', fg='black').place(x = 185,y = 105)
Button(text = '  Abrir llave  ', bg='gold', fg='black').place(x = 185, y = 150)
Button(text = '   Encriptar   ', bg='light sea green', fg='black').place(x = 185,y = 195)
Button(text = 'Desencriptar', bg='lime green', fg='black').place(x = 185,y = 240)




img = Image.open("imagen.jpg")
img = img.resize((275,150), Image.ANTIALIAS)
my_image =  ImageTk.PhotoImage(img)

lbl = Label(image = my_image).place(x=101,y=290)

#Out_put del cifrado
#out_put = Text(frame, width=20, height=10)
#out_put.grid(row=4, column=0, padx=10, pady=10)
#scroll_out = Scrollbar(frame, command=out_put.yview)
#scroll_out.grid(row=4, column=1, sticky="nsew")
#out_put.config(yscrollcommand=scroll_out.set)


# Termina Frame
root.protocol("WM_DELETE_WINDOW", closing)

root.mainloop()  # Para que no se cierre la ventana
