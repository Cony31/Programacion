# Ejercicio3

a = float(input("Ingrese el primero lado\n: "))
b = float(input("Ingrese el segundo lado\n: "))
c = float(input("Ingrese el tercer lado\n: "))

if a == b and b == c:
    print("El triangulo es equilatero\n")

elif a == b or b == c or c == a:
    print("El triangulo es isosceles\n")

else:
    print("El triangulo es escaleno\n")

p = a + b + c
p1 = p / 2

area = p1 * (p1 - a) * (p1 - b) * (p1 - c)
area1 = area**0.5
print("El area del triangulo es:", round(area1))
