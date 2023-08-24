mensaje = "    Bienvenido... al curso de Phyton "

#metodo len,imprime el tamaño de longitud del string 
#print ("El texto original ",mensaje)
#print ("El tamaño del texto es de ", len(mensaje))

#funcion strip,quita espacios al inicio y al final del string 

sinEspacios = mensaje.strip()
#print ("El texto sin espacios es ",sinEspacios)
#print ("El tamaño del texto es sinEspacio de ", len(sinEspacios))

# UPPER mayúscula sostenida
#print("Texto en MAYUSCULA sotenida")
#print(sinEspacios.upper())

# lower minuscula
print("Texto en minúscula sotenida")
print(sinEspacios.lower())

# title inicial de cada palabra en Mayuscula

print("Inicial de cada palabra en Mayusucula")
print(sinEspacios.title())

#capitalice pone la primera inicial en mayuscula
print(sinEspacios.capitalize())

# slit separa la frase en dos opciones,framenta el texto en el indice que se le indique 
parrafo = sinEspacios.split("...")
print (parrafo[0])
print (parrafo[1])