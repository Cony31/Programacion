a = [10, 9, 12, 15, 18]
b = [21, 8, 15, 3, 12]

print(a)

print(b)

print()

numeros = a + b

print("Concatenado", numeros)

numeros.insert(1, 30)
print("Numero 30 agregado", numeros)

numeros = list(set(numeros))
print("Ordenados", numeros)

c = [4, 5, 6]

numeros2 = numeros + c

print("Nueva lista insertada", numeros2)

S = sum(numeros2)
print("La suma de todos los numero es", (S))

print("la mediana de los numeros es", len(numeros2))

p = sum(numeros2) / len(numeros2)
print(
    "la media de los numeros es:",
    (p),
)
