Num = int(input("Ingrese cualquier numero: "))

a = 1
b = 0

while a <= Num:
    if Num % a == 0:
        b = b + 1
    a = a + 1

if b == 2:
    print("El numero", Num, "No es un numero primo")
else:
    print("El numero", Num, "Si es un numero primo")

if Num % 2 == 0:
    print("El numero", Num, "Si es un numero par")
else:
    print("El numero", Num, "No es un numero impar")

if Num > 50:
    print("El numero", Num, "es mayor que 50")
else:
    print("El numero", Num, "es menor que 50")
