# 1. Obtener la cantidad de veces que se repite la palabra “universidad”
# dentro del siguiente parrafo:

# Guardar las palabras encontradas dentro de una tupla.

parrafo = """La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribución significativa al desarrollo sostenible del territorio. Como Universidad sus pilares
fundamentales se basan en la inclusión, pluralismo, conciencia ambiental y participación democrática."""

# Saber cuantas veces se repite la palabra "universidad" tanto como con mayuscula y con minuscula.
rep1 = parrafo.count("universidad")
rep2 = parrafo.count("Universidad")
rep = rep1 + rep2
# Imprimir la respuesta
print("las veces que se repite la palabra 'universidad' en el parrafo es de: ", rep)

# Guardar e imprimir las palabras encontradas en una tupla.
palabra = ("Universidad", "universidad", "Universidad")
print(palabra)

