numero = int(input("ingrese un numero:  "))
# Para sacar el primer numero inpar
inpar = (numero * (numero - 1)) + 1
print(inpar)
# Variable acumular es para acumular las sumas
acum = 0
# Para sumar los numeros inpares
for i in range(numero):
    acum = acum + inpar
    if i == (numero - 1):
        break
    # Para que nuestra variable se vaya incrementando en 2
    inpar = inpar + 2
    print(inpar)
print(f"el cubo de {numero} es: {acum}")
