def obtener_promedioasignatura(notas):
    suma = sum(notas)
    promedio = suma / len(notas)
    return round(promedio, 1)

def obtener_notaminima(notas):
    return round(min(notas), 1)

def obtener_notamaxima(notas):
    return round(max(notas), 1)

def obtener_promediofinal(promedios):
    suma = sum(promedios)
    promedio_final = suma / len(promedios)
    return round(promedio_final, 1)

def principal():
    asignatura1 = input("Ingrese el nombre de la primera asignatura: ")
    asignatura2 = input("Ingrese el nombre de la segunda asignatura: ")
    
    notas_asignatura1 = []
    notas_asignatura2 = []

    for i in range(3):
        nota = float(input(f"Ingrese la nota de laboratorio {i+1} para {asignatura1}: "))
    while nota < 1.0 or nota > 7.0:
        print("La nota debe estar entre 1.0 y 7.0")
        nota = float(input(f"Ingrese la nota de laboratorio {i+1} para {asignatura1}: "))
    notas_asignatura1.append(nota)

    for i in range(3):
        nota = float(input(f"Ingrese la nota de laboratorio {i+1} para {asignatura2}: "))
        while nota < 1.0 or nota > 7.0:
            print("La nota debe estar entre 1.0 y 7.0")
            nota = float(input(f"Ingrese la nota de laboratorio {i+1} para {asignatura2}: "))
    notas_asignatura2.append(nota)

    promedio_asignatura1 = obtener_promedioasignatura(notas_asignatura1)
    promedio_asignatura2 = obtener_promedioasignatura(notas_asignatura2)

    nota_minima_asignatura1 = obtener_notaminima(notas_asignatura1)
    nota_minima_asignatura2 = obtener_notaminima(notas_asignatura2)

    nota_maxima_asignatura1 = obtener_notamaxima(notas_asignatura1)
    nota_maxima_asignatura2 = obtener_notamaxima(notas_asignatura2)

    promedio_final = obtener_promediofinal([promedio_asignatura1, promedio_asignatura2])

    print("Resultados:")
    print(f"Promedio de {asignatura1}: {promedio_asignatura1}")
    print(f"Promedio de {asignatura2}: {promedio_asignatura2}")
    print(f"Nota mínima de {asignatura1}: {nota_minima_asignatura1}")
    print(f"Nota mínima de {asignatura2}: {nota_minima_asignatura2}")
    print(f"Nota máxima de {asignatura1}: {nota_maxima_asignatura1}")
    print(f"Nota máxima de {asignatura2}: {nota_maxima_asignatura2}")
    print(f"Promedio final: {promedio_final}")


principal()
