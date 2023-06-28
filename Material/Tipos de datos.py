#Estructura de datos 26/04
# {} = llaves
# [] = corchetes
# () = parentecis
# / = division
# = exponente

#1 DATOS DE TIPO NÚMERICO
edad = 29
estatura = 1.71
peso = 70.5
complejo = 1 + 41  # complejos

print("01. datos numericos")
print(f"mi estatura es de {estatura} y el peso es de {peso}")
print("impresion de un numero complejo:", complejo, "\n")

#Transformacion de entero a real
print(peso)
print("transformando un valor real a entero:", int(peso))

#Operaciones aritmeticas basicas
imc = peso / (estatura * 2)
print("Mi IMC es de:", imc, "\n")

print(
    "Mi IMC es de: {:.2f}".format(imc), "\n"
)


#2 DATOS DE TIPO CADENA DE CARACTERES
asignatura = "programacion"
carrera = "Ingenieria Civil en Informatica"
print("#### 02-strings ####")
print("La asignatura de", asignatura, "corresponde a la carrera de", carrera)

# UTILIZANDO LA FUNCION LEN (cuenta la cantidad de caracteres)
print("la cantidad de caracteres de la palabra", asignatura, "es de:", len(asignatura))
print("la cantidad de caracteres de la palabra", carrera, "es de:", len(carrera))


#3 VALORES DE VERDADERO Y FALSO
ampolleta = False
interruptor = True

print("##### 03-BOOLEANS #####")
print(ampolleta, interruptor)
print(
    "La variable ampolleta es de tipo:", type(interruptor), "\n"
)#type reconoce el tipo de dato que se esta trabajando

#Podemos transformar cualquier valor a un booleano al igual que un string, int, etc
#Booleano es un tipo de dato
print(bool(0))
print(bool(""))
print(bool(false))
print(bool("true"))
print(bool(1))
print("\n")


#4 DATOS DE TIPO LIST (objetos de tipo colección) - (mutable)
print("##### 04 - LISTA #####")

#Inicializando lista de 2 maneras
nueva_lista = list()
otra_lista = []
print("esta es una lista vacia:", nueva_lista)
print("esta es otra lista vacia:", otra_lista)
print(type(otra_lista))

#Declarando tres listas diferentes
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian", "Marco"]
num = [1, 2, 3, 4, 5, 6]
lenguaje = list(["Python","Dart"])
mixta = ["Juan", 18, "Pepe", 14]

#Se puede realizar una lista de datos cumpuestos
data = ["osorno", {"UV": "nivel bajo", "Temp *C": 15}, {-40.5725, -72.1353}]
listamixta = ["Felipe", 100, True]

print("Lista de cadena de caracteres:", estudiantes)
print("Lista de numeros:", num)
print("Lista de un elemento:", lenguaje)
print("Esta es una lista mixta:", listamixta)
print("Esto igual es una lista", data)
print(len(listamixta))  # para saber la cantidad de elementos de una lista
print(estudiantes.count("Marco"))  # cuenta la cantidad de elementos de Marco
print(num.count(5000))  # cantidad de ocurrencias de un elemtento en especifico

lenguaje = ["javascript"]
print("Nuevo valor del arreglode un elemento:", lenguaje)

#¿Como accedo a un alemento especifico de la lista?
print(estudiantes[0])  # correcto (1° elemento de la lista)
print(estudiantes[1])  # (2° elemento de la lista)
#Print(estudiantes[5]) #incorrecto
print("posicion -2", estudiantes[-2])

#Reasignando el valor de la 3° posicion de la lista
estudiantes[3] = "Gabriela"
print("El nuevo arreglo de estudiantes es:",estudiantes)

#Inicializando otra lista de datos mixtos
data_asig = [10023,"Programación",1,True]

#¿Que hace este código?    #Desempaquetando elementos de la lista (data_asig) a variables
cod,ramo,semestre,estado = data_asig
print(ramo)

#¿Se pueden sumar listas?
print("suma de listas", estudiantes + num)

#¿Que hacen estas funciones?
print(list("python"))
print(list(range(1, 5)))
print("\n")

#5 TUPLAS (No mutables)
newtupla = tuple()
grupo1 = ("daniel", "cristian", "felipe", "200", "100", "daniel")
print("#### 05-tuplas ####")
print(tuple(grupo1))

#Accediendo al primer elemento de la tupla
print(grupo1(0))

#Consultando el elemento "daniel" cuantas veces se encuentra en el tupla
print("El elemento que se repite:", grupo1.count("daniel"))

#Muestra el indice del primer elemento buscando
print("Indice del elemento:", grupo1.index("daniel"))

#Caracteristicas de los Tuplas
# 1:ORDENADA (Los elementos dentro de ella están indexados y se accede a ellos a través de una posición)
# 2:INMUTABLES DINAMICA EFICIENTES (Significa que una vez creada una tupla no se puede modificar, es decir no se puede agregar ni eliminar elementos)
# 3:DINAMICA EFICIENTES (Significa que una vez creada una tupla no se puede modificar, es decir no se puede agregar ni eliminar elementos Puede contener diferentes tipos de datos. Es decir, soportar elementos como números, strings, listas, diccionarios y otras tuplas)
# 4:EFICIENTES (Son más eficientes en términos de espacio y tiempo que las listas cuando se trata de operaciones que no implican modificaciones)

#Reasignando el primer elemento de la tupla
grupo1[0] = "Constanza"
print(grupo1)

#¿Se puede sumas las tuplas?
print("Suma de listas:",estudiantes + num)

#Obteniendo un trozo de la tupla
grupo2 = ("Pedro", "100", "Felipe", "Diego", "2020", "Alejandra")
print("trozo de la tupla", grupo2[3:0])

#¿Entonces como no puedo modificar una tupla, que puedo hacer?
grupo1 = list(grupo1)
print("La tupla ahora es de tipo", type(grupo1), "\n")
print("\n")

#6 SETS (Conjuntos) - Estructura fija
#Formas de inicializar un set
print("#### Sets ####")
Conjunto_vacio = set()
Conjunto_vacio1 = {}  # Diccionario o set?
print(type(Conjunto_vacio1))
conjunto_colores = set({"Azul", "Rojo", "Verde"})  # Utilizando la funcion set
Conjunto_Animales = {"Gato", "Perro", "Loro"}  # Utilizando llaves

print(Conjunto_Animales[0])  # Accediendo al primer elemento
conjunto_colores.add("celeste")
print("El set de colores lo conforman:", conjunto_colores)

#Conjunto_animales.add("Gato")
print("El set de animales lo conforman:",conjunto_animales,"\n") #un set no acepta duplicados, a diferencia de las listas que si.


#7 DICCIONARIO (Clave-Valor)
print("06-DICCIONARIOS")

diccionario1 = dict()
diccionario2 = {}

datos_personales = {
    "Nombre":"Victor",
    "Institucion":"Ulagos",
    "Edad":29
    }

print(datos_personales)

datos_personales = {
    "Nombre":"Victor",
    "Institucion":"Ulagos",
    "Edad": 29,
    "Asignaturas": {"Estructura de Datos", "Programación"}
    }

print("Diccionario inicial:",datos_personales)

#Consulta la cantidad de elementos del Diccionario
print(len(datos_personales))

#Es facilmente accesible a los elementos dentro de un diccionario
print(datos_personales["Institucion"])

#¿Como actualizamos el valor de una clave dentro de un diccionario?
datos_personales["Institucion"] = "USS" 
print("Diccionario actualizado:",datos_personales)

#Agregando un nuevo clave al diccionario
datos_personales["Ciudad"] = "Osorno"
print(datos_personales)
print("Diccionario con el nuevo campo:",datos_personales)

#Eliminando un campo del diccionario
del datos_personales["Ciudad"]
print("Diccionario con el campo eliminado:",datos_personales)

hospital = dict(
    nombre = "Hospital San Jose",
    direccion = "Dr. Guillermo Buhler 1765",
    ciudad = "Osorno"
)
