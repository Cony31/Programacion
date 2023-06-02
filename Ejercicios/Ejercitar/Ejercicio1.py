# Ejercicio1

No1 = int(input("Ingrese el primer valor\n: "))
No2 = int(input("Ingrese el segundo valor\n: "))
No3 = int(input("Ingrese el tercer valor\n: "))

if No1 > No2 and No2 > No3:
    print(No3, No1)

elif No1 > No3 and No3 > No2:
    print(No2, No1)

elif No2 > No1 and No1 > No3:
    print(No3, No2)

elif No2 > No3 and No3 > No1:
    print(No1, No2)

elif No3 > No2 and No2 > No1:
    print(No1, No3)

else:
    No3 > No1 and No1 > No2
    print(No2, No3)
