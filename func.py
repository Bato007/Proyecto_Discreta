from random import *

e = 0 #Es global porque se usa para privateKey
lcm = 0 #Es global porque se usa para privateKey
n = 0 #Es global porque se usa para descifrar
c = 0 #Es global porque se usa para descifrar

def encrypt(mensaje):
    global n, lcm, e, c
    
    #Se necesita que ambos numeros primos esten alejados
    prime1 = generatePrime(500, 1000) #Numeros entre 500 y 1000
    prime2 = generatePrime(5000, 7000) #Numeros entre 5000 y 7000
    
    prime1 = 773
    prime2 = 907
    
    n = prime1*prime2 #Se multiplican los numeros primos
    lcm = lcm(prime1-1, prime2-1) #Se busca el mcm de los numeros-1
    
    e = publicKey(lcm) #e se genera con el mcm
    
    c = ciphertext(mensaje, e, n) #Se genera el cifrado
    
    return c #Se retorna el mensaje cifrado

#Se genera un numero primo
def generatePrime(rango1, rango2):
    generate = True
    while(generate): #Se busca numero primo hasta encontrarlo
        possiblePrime = randint(rango1, rango2) #Numeros entre rango1 y rango2
        
        #Revisando si es numero primo
        for divisor in range(2, possiblePrime):
            if (possiblePrime % divisor) == 0: 
                break #No es primo
            else:
                generate = False #Si es primo
    return possiblePrime #Se retorna
        
        
#Carmichael’s totient for n (el mcm)
def lcm(primo1, primo2):
    #El numero mayor siempre sera el primo2
    mayor = primo2
    
    while(True):
        if((mayor % primo2 == 0) and (mayor % primo1 == 0)): #Buscamos el divisor
            lcm = mayor
            break
        else:
            mayor+=1 #Sumamos 1 al primo2
            
    return mayor #Es el mcm
    
#Se genera la llave publica
def publicKey(lcm):
    e = 65537 #Numero definido para e
    return e

#Se genera el ciphertext
def ciphertext(mensaje, e, n):
    c = (mensaje**e)%n
    return c #Encriptado del mensaje

#Se genera la llave privada
def privateKey():
    global e, lcm
    print("Este es e" , e, "Este es el mcm", lcm)
    d = mod_Inv(e, lcm) #modular inverso
    return d #Llave para descifrar

#Modular inverso
def mod_Inv(x,y):
    for i in range(y):
        if (x*i)%y==1:
            return i #Se retorna
    return 1
        
#Se desencripta
def decrypt(privateKey):
    global c, n
    mensaje = (c**privateKey)%n
    return mensaje #Mensaje descifrado


print("Encriptado ", encrypt(10))
print("Discifrado ", decrypt(privateKey()))