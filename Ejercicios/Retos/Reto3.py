# Reto3

Ciudades = ("Santiago", "Temuco", "Osorno", "Punta Arena")
ICA = (134, 99, 245, 50)

CICA = list(zip(Ciudades, ICA))

print(CICA)

print()

print(
    Ciudades[3],
    "tiene un ICA de",
    ICA[3],
    "es la ciudad con menos contaminacion del aire",
)

print(
    Ciudades[2],
    "tiene un ICA de",
    ICA[2],
    "es la ciudad con mas contaminacion del aire",
)

print()

print(Ciudades[3], "tiene un ICA de", ICA[3], ":Buena (0 - 50)")

print(Ciudades[1], "tiene un ICA de", ICA[1], ":Moderada (51 - 100)")

print(
    Ciudades[0],
    "tiene un ICA de",
    ICA[0],
    ":Dañina a la salud para grupoa sensibles (101 - 150)",
)

print("Ninguna ciudad esta en la categoria de :Dañina a la salud (151 - 200)")

print(
    Ciudades[2],
    "tiene un ICA de",
    ICA[2],
    ":Muy dañina a la salud (201 - 300)",
)

print("Ninguna ciudad esta en la categoria de :Peligrosa (Superior a 300)")
