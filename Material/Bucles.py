#WHILE
edad = 15
num = 0

#Bucle infito
"""while edad < 18:
    print("Eres menor de edad, no puedes manejar")"""

#Bucle infinito
"""while True:
    print(num)
    num +=2"""

#¿Qué hace este bucle?
print("01 - WHILE")
print('\nImpresión de numeros de 0 al 100 (Incrementando de 2 en 2)')

num = 0
while num <= 100:
    print(num)
    num += 2
    #num = num + 2
print("Primer Bucle terminado!\n")

#Combinando While y else
print('\nImpresión de numeros de 100 al 200 (Incrementando de 2 en 2) + Condicion ELSE')

while num <= 200:
    print(num)
    num += 2
else: 
    print("Mi condicion es igual o mayor a 200")
print("Segundo Bucle terminado!")


#Combinando While y if
print('\nImpresión de numeros de 200 al 300 (Incrementando de 2 en 2) + IF en 250')

while num <= 300:
    print(num)
    num += 2
    if num == 250:  #Mover if izquierda
        print("Mi condicion es igual a 250")
print("Tercer Bucle terminado!\n")

#Utilizando el break
print('\nImpresión de numeros de 300 al 400 (Incrementando de 2 en 2) + Break a los 350')

while num <= 400:
    print(num)
    num += 2
    if num == 350:  #mover if izquierda
        print("Se detiene la ejecución")
        break
print(num)
print("Cuarto Bucle terminado!\n")


#Utilizando el continue
print('\nImpresión de numeros de 0 al 50 (Incrementando de 1 en 1) + continue if == 40')
num = 0
while num <= 50:
    num += 1
    if num == 40:
        continue
    print(num)

#Loop Infinito + Break
"""while True:
    parametro = input(">")
    if parametro == "exit":
        break
    else:
        print(parametro)"""

#Bucle For
print("02 - FOR")


print('\nImpresión de una lista de 10 elementos de forma vertical (Utilizando FOR)')
print('\nFOR N°1')

#No esta bien optimizado
for i in (1,2,3,4,5,6,7,8,9,10):
    print(i)

print('\nFOR N°2')
newlista = [1,2,3,4,5,6,7,8,9,10]
for i in newlista:
    print(i)

print('\nFOR N°3')
for i in range(1,11):
    print(i)


print("\n03 - ITERADOR E ITERABLES")
#Aprendiendo los conceptos de iterador e iterable
iterador = iter(newlista)

print(next(iterador))  #Imprime 1
print(next(iterador))  #Imprime 2
print(next(iterador))  #Imprime 3
print(next(iterador))  #Imprime 4
print(next(iterador))  #Impreme 5 ... 
