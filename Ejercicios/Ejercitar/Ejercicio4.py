# Ejercicio4

Nombre1 = str(input("ingrese el primer nombre\n: "))
Nombre2 = str(input("Ingrese el segundo nombre\n: "))

if Nombre1[0] == Nombre2[0]:
    print("Los dos nombres que usted ingreso comienzan con la misma letra")

elif Nombre1[0] != Nombre2[0]:
    print("Los dos nombres que usted ingreso no comienzan con la misma letra")

elif Nombre1[-1] != Nombre2[-1]:
    print("Los dos nombres que usted ingreso no comienzan con la misma letra")

else:
    Nombre1[-1] == Nombre2[-1]
    print("Los dos nombres que usted ingreso terminan con la misma letra")
