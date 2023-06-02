def longitud():
    frase = input("Porfavor, ingrese una frase: ")
    palabras = frase.split()
    diccionario = {}

    for palabra in palabras:
        diccionario[palabra] = len(palabra)

    return diccionario


resultado = longitud()
print(resultado)
