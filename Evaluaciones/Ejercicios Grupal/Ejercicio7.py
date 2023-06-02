#Pedir que ingrese un numero.
num = int(input("Ingrese un numero: "))
#Definir formula para sacar el factorial.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#Definir res como el factorial del numero ingresado.
res = factorial(num)
#Imprimir el factorial del numero ingresado
print(f"El factorial de {num} es : {res}")