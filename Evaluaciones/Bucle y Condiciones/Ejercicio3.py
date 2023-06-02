Set1 = {100, 250, 300, 1000}
Set2 = {150, 250, 500, 1000}

numero = 100

if numero in Set1 or Set2:
    print("El numero", numero, "esta presente en solo un conjunto")

else:
    print("El numero", numero, "Esta presente en ambos conjuntos")


numero2 = 700

if numero2 in Set1 and Set2:
    print("El numero", numero2, "está presente en ambos conjuntos")

else:
    print("El numero", numero2, "no está presente en ningun conjuntos")


numero3 = 500

if numero3 in Set1:
    print("El numero", numero3, "esta presente en el conjunto 1")

else:
    print("El numero", numero3, "esta presente en el conjunto 2")

# Potencia
set1 = {x**3 for x in Set1}
set2 = {x**3 for x in Set2}
print("El conjunto 1 elevado por 3", set1)
print("El conjunto 2 elevado por 3", set2)

# Union
Union = Set1.union(Set2)

print("La union de los 2 sets es", Union)
