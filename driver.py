# _______________________________________________________
# Universidad del Valle de Guatemala
# Andrea Amaya | Brandon Hernández | Laura Tamath
# Proyecto Criptografía RSA
# Desencriptador de archivos
# _______________________________________________________
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from os import path
import os
from func import * #FUNCIONES

root = Tk()
root.title('Proyecto | Matemática discreta')
root['bg'] = 'gray11' #ivory2
root.call('wm', 'iconphoto', root._w, PhotoImage(file='logo.png'))
root.resizable(False, False)
root.geometry('500x455')

route = ''


# Primer frame
frame = Frame()
frame.pack()
label = Label(root, text= 'Criptografía RSA', font= ('Calibri Bold','40'), fg='gray99', bg='gray11')
label.place(x = 18, y = 5)

#Funcion para encriptar
def encryptTxt():
    global route
    file = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
    route = file
    
    file1= open(file,"r") #Se abre el texto a encriptar
    Lines = file1.readlines() #Se guarda en una variable el contenido
    
    try:
        os.remove("encrypt.txt") #Se elimina txt pasados de encrypt
        f= open("encrypt.txt","w+") #Se crea un nuevo txt encrypt
    except:
        f= open("encrypt.txt","w+") #Se crea un nuevo txt encrypt
    
    for line in Lines: 
        txtEncriptado = encrypt(''.join(line)) #Se encripta
        listToString = ''.join([str(elem) for elem in txtEncriptado]) #Se pasa de lista de ints a string
        f.write(listToString) #Se escribe
    
    f.close() #Se cierra
    file1.close() #Se cierra
    
#Función para asegurar que el programa se cerrará
def closing():
    if messagebox.askokcancel("Close program","¿Seguro que quiere cerrar el programa?"):
        root.destroy()

#Diseño y funcionamiento de los botones
Button(text = '  Encriptar  ', bg='coral', fg='black', command=encryptTxt).place(x = 185,y = 105) #recibe txt con texto a desencriptar
Button(text = 'Llave publica', bg='gold', fg='black').place(x = 185, y = 150)
Button(text = 'Llave privada', bg='light sea green', fg='black').place(x = 185,y = 195)
Button(text = 'Desencriptar', bg='lime green', fg='black').place(x = 185,y = 240)


#Diseño de imagen
img = Image.open("imagen.jpg")
img = img.resize((275,150), Image.ANTIALIAS)
my_image =  ImageTk.PhotoImage(img)

lbl = Label(image = my_image).place(x=101,y=290)



# Termina Frame
root.protocol("WM_DELETE_WINDOW", closing)

root.mainloop()  # Para que no se cierre la ventana
