# Ejercicio9

numeros = [4, 3, 8, 12, 6, 10, 14, 3, 6]

print(numeros)

print()

p = sum(numeros) / len(numeros)

numeros.pop(8)
numeros.insert(0, 2)
numeros = list(set(numeros))
print(
    "la mediana de la lista es:",
    len(numeros),
)
print(
    "la media de la lista es:",
    round(p),
)
print(numeros)
