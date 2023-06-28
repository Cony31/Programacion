# Operaciones Aritmeticas
# Operador Nombre Ejemplo
# +        Suma   a + b = 8
# -        Resta  a - b = 4
# *   Multiplicación a * b = 12
# /      División a / b = 3
# %        Módulo a % b = 0
# **    Exponente a ** b = 36
# //     Cociente a // b = 3

# Operaciones Comparacion
# ==      Igual   a == b
# !=     Distinto a != b
# >       Mayor   a > b
# <       Menor   a < b
# >=    Mayor o igual a >= b
# <=    Menor o igual a <= b

# Operaciones Logicas
# Operador Lógico Interpretación
# and      Función lógica “y”
# or       Función lógica “o”
# not      Función lógica “no”

# And
# A          B          A and B
# False      False      False
# False      True       False
# True       False      False
# True       True       True

# Or
# A          B          A and B
# False      False      False
# False      True       False
# True       False      False
# True       True       True

# Not
# A          B
# False      True
# True       False

#Ejemplo
bencina = True
encendido = False
edad = 19

#Utilizando el operador AND
if bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador OR
if bencina or encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al AND
if not bencina and encendido:
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al OR
if not bencina or encendido:
    print("Utilizando NOT Y OR:  El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

#Utilizando el operador NOT junto al AND y OR
if not bencina or (encendido and edad >= 18):
    print("El vehiculo puede avanzar")
else:
    print("El vehiculo no puede arrancar")

# Sentencia Elif
# if condicion: ejecutar un código
# elif otra_condicion: ejecutar otro código
# else: ejecutar un código distinto

x2 = 7
if x2 > 10:
    print("x2 es mayor que 10")
elif x < 10:
    print("x2 es menor que 10")
else:
    print("x2 es 10")  # x2 es menor que 10


