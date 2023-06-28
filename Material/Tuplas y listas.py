#TUPLAS

#Declarando dos tuplas (también se puede hacer sin parentesis)
t = 1, 2, 3
tuplita = "Pedrito", "Tito", "Andre", "Barry"

#Se puede ordenar una tupla con Sorted (pero el resultado es una lista ordenada)
tuplaordenada = sorted(tuplita)
print(tuplaordenada)

print(type(t))
print(type(tuplita))

alumnas = [("Lorena", 6.5, 6.9), ("Maria", 3.9, 4.1), ("Anais", 5.4, 4.8)]
print(alumnas)

for estudiante in alumnas:
    print(estudiante)

promedios = []

for i in alumnas:
    nombre = i[0]
    lab1   = i[1]
    lab2   = i[2]
    promedio = round((lab1 * 0.6) + (lab2 * 0.4),2)
    promedios.append((nombre, promedio))

print(promedios)


#LISTAS
newlist = [0,1,2,[10,20,30]]

#Como consultar el tercer elemento? especificamente el primer elemento de la sub lista?
print(newlist[3][0])

l = list(range(1,11))
print(sum(l)) #sumando todos los elementos de una lista