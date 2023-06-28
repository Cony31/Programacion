# Operadores

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

# ejemplo
bencina = True
encendido = True
edad = 19

# And
if bencina and encendido:
    print("El vehiculo puede avanzar")

else:
    print("El vehiculo no puede avanzar")

# Or
if bencina or encendido:
    print("El vehiculo puede avanzar")

else:
    print("El vehiculo no puede avanzar")

    # Not
    # if bencina not encendido: #Invierte el valor de  bencina
    print("El vehiculo puede avanzar")

    # else:
    print("El vehiculo no puede avanzar")

# Not con And
if not bencina and encendido:
    print("El vehiculo puede avanzar, Utilizando Not y And")

else:
    print("El vehiculo no puede avanzar")

# Not con Or
if not bencina or encendido:
    print("El vehiculo puede avanzar, Utilizando Not y Or")

else:
    print("El vehiculo no puede avanzar")

# Not con And y Or
if not bencina or (encendido and edad > 18):
    print("El vehiculo puede avanzar")

else:
    print("El vehiculo no puede arrancar")

# Condicinales

# Sentencia If
# if condicion: ejecutar un código

x = 15
if x > 10:
    print("x es mayor que 10")  # x es mayor que 10

# Sentencia else
# if condicion: ejecutar un código
# else: ejecutar un código distinto

x1 = 5
if x1 > 10:
    print("x es mayor que 10")

else:
    print("x es menor o igual que 10")  # x1 es menor o igual que 10

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
