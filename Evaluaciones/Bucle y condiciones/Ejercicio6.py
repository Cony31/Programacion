# Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos
# de un dıa desde las 00:00:00 horas hasta las 23:59:59 horas.
import time
import os

# Definir valores.
hora = 00
min = 00
seg = 00
# Definir el rango de la hora,minuto y segundo.
for hora in range(24):
    for min in range(60):
        for seg in range(60):
            # Formato a imprimir
            print(f"{hora} : {min}: {seg}: ")
            # Definir tiempo a espera hasta que digite el siguiente valor.
            time.sleep(1)
            # Limpiar la terminal despues de digitar un numero.
            os.system("cls")
            # Hacer que el valor de cada segundo incremente en uno de forma consecutiva.
            seg = seg + 1
        else:
            # Cuando seg sea igual a 60, min incrementara en 1 y seg volvera a 0.
            min = min + 1
            seg = 0
    else:
        # Cuando min sea igual a 60, hora incrementara en 1 y min volvera a 60
        hora = hora + 1
        min = 0
