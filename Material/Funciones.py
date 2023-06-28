#01-DECLARANDO LA PRIMERA FUNCIÓN
print("DECLARANDO UNA FUNCIÓN SIMPLE")

def La_primera_funcion():
    print("Esta es mi primera funcion")

La_primera_funcion()


#02-DECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS
print("\nDECLARANDO UNA FUNCIÓN Y UTILIZANDO LISTAS")

def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar()
print(concatenar(lista1,lista2))


#03-DECLARANDO UNA FUNCIÓN MULTIPLICACION PASANDO PARAMETROS
print("\nDECLARANDO UNA FUNCIÓN MULTIPLICACION PASANDO PARAMETROS")

def multiplicacion(num1,num2):
    return num1*num2

#multiplicacion()
print(multiplicacion(50,50))


#04-EJEMPLO DE UNA FUNCIÓN
print("\nFUNCIONES SUMA Y RESTA (POR TECLADO)")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

#Se llama a la función Suma
resultado = suma(a, b)
print("La suma es de:", resultado)

#Se llama a la función resta
resultado2 = resta(a, b)
print("La resta es de:", resultado2)


#05-PASANDO PARAMETROS POR VALOR
print("\n05-PASANDO PARÁMETROS POR VALOR")
def modificar_numero(x):
    x = 10  

x = 5
print("Antes de llamar a la función:", x)  
modificar_numero(x)
print("Después de llamar a la función:", x)  


#06-PASANDO PARAMETROS POR REFERENCIA
print("\n06-PASANDO PARÁMETROS POR REFERENCIA")

#Paso por referencia (objetos mutables)
def op_lista(lista):
    lista.append(4)  #Modificando la lista original

numeros = [1, 2, 3]
op_lista(numeros)  
print(numeros)  

#Paso por nombre de argumento
def saludar(nombre, mensaje):
    print(mensaje + " " + nombre)

saludar(mensaje="Hola,", nombre="Juan")  
