# . Crear 20 numeros, que se encuentren en el intervarlo 40 al 350 y los almacene en una
# lista y luego pida buscar algun numero dentro de los almacenados. Ademas que muestre 
# la cantidad de ocurrencias de ese numero buscado. (Se permite el uso de la Biblioteca Random

import random
#Definir la lista.
numeros = []
#Definir cantidad de numeros a buscar.
for i in range(20):
    #Buscar numeros aleatorios en el rango elegido.
    numeros.append(random.randrange(40,350))
#Imprimir los numeros encontrados.
print(numeros)
#Pedir que ingrese un numero a buscar en la lista.
buscar = int(input("Ingrese el numero que desea buscar: "))
#Buscar e imprimir la cantidad de ocurrencias del numero a buscar.
rep = numeros.count(buscar)
print(f"El numero {buscar}, aparece {rep} veces en la lista")