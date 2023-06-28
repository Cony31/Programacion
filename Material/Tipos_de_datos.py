Estudiantes = ("Fran", "Thomas", "Felipe")
Num = (1, 2, 4, 5, 6)

# ¿se pueden sumar listas?
print("suma de listas", Estudiantes + Num)

# ¿que hacen estas funciones?
print(list("python"))
print(list(rango(1, 5)))
print("\n")

# en el fichero de listas mostrara mas funciones

# Tuplas (no mutables)
newtupla = tuple()
grupo1 = ("daniel", "cristian", "felipe", "200", "100", "daniel")
print("#### 05-tuplas ####")
print(typle(grupo1))

# Accediendo al primer elemento de la tupla
print(grupo1(0))

# Consultando el elemento "daniel" cuantas veces se encuentra en el tupla
print("El elemento que se repite:", grupo1.count("daniel"))

# Muestra el indice del primer elemento buscando
print("Indice del elemento:", grupo1.index("daniel"))

# Reasignando el primer elemento de la tupla
grupo1[0] = "Constanza"
print(grupo1)

# ¿Se puede sumas las tuplas?

# Obteniendo un trozo de la tupla
grupo2 = ("Pedro", "100", "Felipe", "Diego", "2020", "Alejandra")
print("trozo de la tupla", grupo2[3:0])

# ¿Entonces como no puedo modificar una tupla, que puedo hacer?
grupo1 = list(grupo1)
print("La tupla ahora es de tipo", type(grupo1), "\n")
print("\n")

# Sets (Conjuntos) - Estructura fija
# Formas de inicializar un set
print("#### Sets ####")
Conjunto_vacio = set()
Conjunto_vacio1 = {}  # Diccionario o set?
print(type(Conjunto_vacio1))
conjunto_colores = set({"Azul", "Rojo", "Verde"})  # Utilizando la funcion set
Conjunto_Animales = {"Gato", "Perro", "Loro"}  # Utilizando llaves

print(Conjunto_Animales[0])  # Accediendo al primer elemento
conjunto_colores.add("celeste")
print("El set de colores lo conforman:", conjunto_colores)

Conjunto_Animales.add("Gato")
