max_valor = 30
numero_minimo = 2
suma_divisible_por_5 = 0
suma_impares = 0

while numero_minimo < max_valor:
    if numero_minimo % 5 == 0:
        suma_divisible_por_5 += numero_minimo

    if numero_minimo % 2 != 0:
        suma_impares += numero_minimo

    numero_minimo += 3

print(
    "La suma de los enteros generados de 3 en 3 divisibles por 5 es:",
    suma_divisible_por_5,
)
print("La suma de los enteros generados de 3 en 3 impares es:", suma_impares)
