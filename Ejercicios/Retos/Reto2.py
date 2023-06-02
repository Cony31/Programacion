Nombre_estudiante = input("¿Cual es el nombre del estudiante?\n")
Nombre_asignatura = input("¿Cual es la asignatura?\n")
Nota_N1 = float(input("¿Cual es la nota del laboratorio N1"))
Nota_N2 = float(input("¿Cual es la nota del laboratorio N2"))
NotaFinal = float(Nota_N1 * 0.30 + Nota_N2 * 0.70)

print(
    "El nombre del estudiantes es",
    Nombre_estudiante,
    ", la asignatura es",
    Nombre_asignatura,
    ", la nota final del laboratorio N1 es",
    Nota_N1,
    ", la nota final del laboratorio N2 es",
    Nota_N2,
    ",y el promedio final es",
    NotaFinal,
)

datos = {
    "Nombre del estudiante": Nombre_estudiante,
    "Nombre de la asignatura": Nombre_asignatura,
    "Nota1": Nota_N1,
    "Nota2": Nota_N2,
    "Notafinal": round(NotaFinal, 1),
}

print(datos)
