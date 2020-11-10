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

    #Se revisa que ya haya generado la llave publica
    if checkPublicKey():
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
        messagebox.showinfo(message = 'Se ha generado el encriptado', title = 'Completo')
    else:
        messagebox.showinfo(message = 'No se ha generado llave publica', title = 'Fatal')
    
#Funcion para generar el txt con la llave publica
def writePublicKey():
    try:
        os.remove("keys.txt") #Se elimina txt pasados de keys
        f= open("keys.txt","w+") #Se crea un nuevo txt keys
    except:
        f= open("keys.txt","w+") #Se crea un nuevo txt keys
    
    f.write(str(publicKey())) #Se escribe la publica
    f.close() #Se cierra
    
    messagebox.showinfo(message = 'Se ha generado la llave publica', title = 'Completo')
    
#Funcion para generar el txt con la llave privada
def writePrivateKey():
    try:
        f = open("encrypt.txt","r") #Se revisa que exista el encrypt
        f.close() #Se cierra
        f= open("keys.txt","w") #Se abre el texto de las llaves
        f.write(str(privateKey())) #Se escribe la privada
        f.close() #Se cierra
        
        messagebox.showinfo(message = 'Se ha generado la llave privada', title = 'Completo')
        
    except:
        messagebox.showinfo(message = 'Aun no hay nada encriptado', title = 'Fatal')
        
#Funcion para generar el txt con el desencriptado
def writeDecrypt():
    #Se revisa que ya haya generado la llave privada
    if checkPrivateKey():
        try:
            os.remove("decrypt.txt") #Se elimina txt pasados de decrypt
            f= open("decrypt.txt","w+") #Se crea un nuevo txt decrypt
            
        except:
            f= open("decrypt.txt","w+") #Se crea un nuevo txt decrypt
            
        f.write(decrypt()) #Se escribe
        f.close()
        messagebox.showinfo(message = 'Se ha generado el desencriptado', title = 'Completo')
        
    else:
        messagebox.showinfo(message = 'Aun no hay llave privada', title = 'Fatal')
    
#Función para asegurar que el programa se cerrará
def closing():
    if messagebox.askokcancel("Close program","¿Seguro que quiere cerrar el programa?"):
        root.destroy()

#Diseño y funcionamiento de los botones
Button(text = 'Llave publica', bg='gold', fg='black', command=writePublicKey).place(x = 185, y = 105)
Button(text = '  Encriptar  ', bg='coral', fg='black', command=encryptTxt).place(x = 185,y = 150) #recibe txt con texto a desencriptar
Button(text = 'Llave privada', bg='light sea green', fg='black', command=writePrivateKey).place(x = 185,y = 195)
Button(text = 'Desencriptar', bg='lime green', fg='black', command=writeDecrypt).place(x = 185,y = 240)


#Diseño de imagen
img = Image.open("imagen.jpg")
img = img.resize((275,150), Image.ANTIALIAS)
my_image =  ImageTk.PhotoImage(img)

lbl = Label(image = my_image).place(x=101,y=290)



# Termina Frame
root.protocol("WM_DELETE_WINDOW", closing)

root.mainloop()  # Para que no se cierre la ventana
