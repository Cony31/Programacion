# Declarando la funciona en Python


def La_primera_funcion():
    print("Esta es mi primera funcion")


La_primera_funcion()

# Declarando una funcion y utilizando listas


def Concatenar(lista1, lista2):
    return lista1 + lista2


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

Concatenar()
print(Concatenar(lista1, lista2))

# Declarando una funcion de multiplicacion


def multiplicacion(num1, num2):
    return num1 + num2


multiplicacion()
print(multiplicacion(10, 2))

# ejemplo de una funcion suma y resta


def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


# se llama a la funcion de suma
resultado = suma(a, b)
print("la suma es de:", resultado)

# se llama a la funcion de resta
resultado2 = resta(a, b)
print("la resta es de:", resultado2)


def saludo(nombre):
    print(f"Hola, mi nombre es + {nombre}")


saludo("Tomas")
# Saludo: la llamada a la funcion, imprime "Hola, mi nombre es Tomas"
