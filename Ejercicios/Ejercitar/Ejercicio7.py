# Ejercicio7 . Crear una lista con nombres de 5 trabajadores y otra lista con las edades de estos 5 trabajadores, Se solicita relacionar ambas listas en una sola estructura. La salida puede ser en tuplas o en un diccionario.

Nombres = ["Thomas", "Mathias", "Fernando", "Antonio", "Agusto"]
Edades = [45, 34, 43, 40, 39]

for tupla in zip(Nombres, Edades):
    print(tupla[0], tupla[1])
