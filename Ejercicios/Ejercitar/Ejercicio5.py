# Ejercicio 5

Nota1 = float(input("Ingrese la nota del primer laboratorio\n: "))
Nota2 = float(input("Ingrese la nota del segundo laboratorio\n: "))
Nota3 = float(input("Ingrese la nota del tercer laboratorio:\n: "))

p = Nota1 * 0.3 + Nota2 * 0.4 + Nota3 * 0.3
print(f"el promedio ponderado del estudiante es:\n{p:.1f}")

if p >= 1.0 and p <= 3.9:
    print("El estudiante reprobo la asignatura:\n")

elif p <= 5.9 and p >= 3.9:
    print("El estudiante aprobo la asignatura:\n")

else:
    p >= 5.9 and p == 7.0
    print("El estudiante aprobo la asignatura con distincion:\n")
