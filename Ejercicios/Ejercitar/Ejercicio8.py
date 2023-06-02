# Ejercicio8: Elaborar un algoritmo que permita al usuario ingresar un mes y arroje la estacion correspondiente a ese mes: verano, otoño, invierno o primavera

print(
    "Meses: Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre, Octubre, Noviembre, Diciembre"
)
Mes = input("Ingrese el mes que desea saber en que estacion pertenece\n: ")

print()

Estaciones = {
    "Enero": "Verano",
    "Febrero": "Verano",
    "Marzo": "Otoño",
    "Abril": "Otoño",
    "Mayo": "Otoño",
    "Junio": "Invierno",
    "Julio": "Invierno",
    "Agosto": "Invierno",
    "Septiembre": "Primavera",
    "Octubre": "Primavera",
    "Noviembre": "Primavera",
    "Diciembre": "Verano",
}

if Mes in Estaciones:
    Estacion = Estaciones[Mes]
    print(
        "La estacion que usted escribio:", Mes, "Corresponde a la estacion: ", Estacion
    )

else:
    print(
        "El mes que usted escribio no es valido, porfavor ingrese el mes correctamente"
    )
