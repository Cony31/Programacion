Num = int(input("Ingrese un numero: "))


def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero / 2) + 1):
        if numero % i == 0:
            return False
    return True


if Num % 2 == 0:
    print("El numero", Num, "Si es un numero par")
else:
    print("El numero", Num, "No es un numero impar")


if es_primo(Num):
    print("El numero", Num, "No es un numero primo")
else:
    print("El numero", Num, "Si es un numero primo")


if Num > 50:
    print("El numero", Num, "es mayor que 50")
else:
    print("El numero", Num, "es menor que 50")
