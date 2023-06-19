# Definir valores
Valor_inicial = int(500)
Aumento = int(44)

# Agregar en 'Total' el valor inicial
Total = []
Total.append(Valor_inicial)

# Ocupar el bucle while y Realizar las operaciones matematicas para agregar al 'Total'
while Valor_inicial < int(800):
    Valor_inicial = Valor_inicial - Aumento
    Total.append(Valor_inicial)
    Incrementa = Aumento + int(10)
    Aumento += int(12)
    Valor_inicial += Incrementa
    Total.append(Valor_inicial)

# Imprimir el total de numeros y la sumatoria de ellos
print("Los numeros son:", Total)
print()
print("La suma de todos los numeros es:", sum(Total))
