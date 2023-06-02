# Ejercicio 6

grupo1 = ["Marcos", "Gabriela", "Benjamin", "Mathias"]
grupo2 = ["Marcos", "Nicolas", "Diego", "Mathias"]

# fusion de los 2 listas
grupo1_2 = grupo1 + grupo2

# eliminacion de los nombres duplicados en la 2 listas
Grupoduplicados = set()
dup = [x for x in grupo1_2 if x in Grupoduplicados or (Grupoduplicados.add(x) or False)]

print("Los estudiantes que estan duplicados en los dos grupos son: ")
print(dup)
