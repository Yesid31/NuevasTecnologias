modulos=["Logica","Base Datos","HTML5","Moviles"]
print(modulos)  

print ("Elmento inicial de la lista ------------>", modulos[0])
# -1 Va A Decir Cual Es El Último Elemento De La Lista
print("Elemento final de la lista -------------->", modulos[-1])

print ("Numero de Elementos Que Tiene La Lista -->", len(modulos))

print ("Agregar un elemento a mi lista... Metodologias Agiles ")
modulos.append("Metodologias Agiles")
modulos.insert(1,"Web2")
print(modulos)
print ("Ultimo elemento de la lista  ------------>",modulos [ len(modulos)-1])

#Cantidad qde veces que aparece un elemento en la lista Count
print ("Cantidad  de veces que aparece HTML ----->",modulos.count("HTML5"))

#Lista Ordenada Sort 
print ("Lista Ordenada alfabeticamente")
modulos.sort()
#print(modulos)

#pop para eliminar un elemento de nuestra lista 
print("-----------------------------------------------------------")
i=1
for indice in modulos:
    print(i, indice)
    i=i+1


