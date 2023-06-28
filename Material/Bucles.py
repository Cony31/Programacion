# While
contador = 0

while contador < 5:
    print("El contador es:", contador)
    contador += 1

print("Fin del bucle while")

# En este ejemplo, inicializamos la variable contador con el valor 0.
# Luego, establecemos la condición del bucle while utilizando la expresión contador < 5.
# Esto significa que el bucle se ejecutará siempre que la variable contador sea menor que 5
# Después de imprimir el valor del contador, incrementamos su valor en 1 usando el operador +=.
# El bucle while continuará ejecutándose mientras se cumpla la condición contador < 5.
# Una vez que la condición se vuelva falsa (es decir, el contador sea igual o mayor a 5),
# el bucle while se detendrá y el programa imprimirá "Fin del bucle while".

print()
# For
for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    print(i)

print()

newlista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in newlista:
    print(i)

print()

for i in range(11):
    print(i)

print()

frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print("Me gusta", fruta)

print("Fin del bucle for")

# En este ejemplo, tenemos una lista llamada frutas que contiene tres elementos: "manzana", "banana" y "cereza".
# Utilizamos el bucle for para recorrer cada elemento de la lista frutas.
# En cada iteración, la variable fruta toma el valor del elemento actual de la lista.
# Dentro del bucle, imprimimos la frase "Me gusta" seguida de la fruta actual utilizando la función print().
# El bucle for se ejecutará automáticamente para cada elemento de la lista frutas.
# Una vez que se hayan procesado todos los elementos de la lista, el bucle for finalizará y se imprimirá "Fin del bucle for".

print()
# Bucle For (Definida)
frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print("Me gusta", fruta)

print()
# Bucle While (No definida)
contador = 0

while contador < 5:
    print("El contador es:", contador)
    contador += 1

# Bucle do-while (simulado con un bucle while y una condición de salida)
respuesta = "si"

while respuesta == "si":
    print("Haciendo algo...")
    respuesta = input("¿Desea continuar? (si/no): ")

print("Fin del programa")
