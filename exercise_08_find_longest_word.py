import os


def find_longest_word(filename):

    if not os.path.exists(filename):
        raise FileNotFoundError

    with open(filename, "r") as archivo:

        contenido = archivo.read()

    palabras = contenido.split()

    if len(palabras) == 0:
        raise ValueError("file has no words")

    palabra_mas_larga = palabras[0]

    for palabra in palabras:

        if len(palabra) > len(palabra_mas_larga):

            palabra_mas_larga = palabra

    return palabra_mas_larga