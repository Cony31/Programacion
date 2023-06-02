Notas = int(input("Ingrese el número de calificaciones: "))



if Notas < 10:
    print("Debe haber al menos 10 calificaciones.")

calificaciones = []
for i in range(Notas):
    calificacion = float(input("Ingrese la calificación: "))

    if calificacion < 1.0 or calificacion > 7.0:
        print("La calificación debe estar entre 1.0 y 7.0.")
        
       calificaciones.append(calificacion):

cali_altas = 0
cali_bajas = 0

# Media
M = sum(calificaciones) / len(calificaciones)


print("La media de notas es:", M)
print("Cantidad de calificaciones más altas que la media:", cali_altas)
print("Cantidad de calificaciones más bajas que la media:", cali_bajas)
