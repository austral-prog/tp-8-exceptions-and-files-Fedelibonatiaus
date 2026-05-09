import os


def safe_average(filename):

    if not os.path.exists(filename):
        raise FileNotFoundError

    numeros = []

    with open(filename, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea != "":

                try:
                    numero = float(linea)
                    numeros.append(numero)

                except ValueError:
                    pass

    if len(numeros) == 0:
        raise ValueError("no valid numbers")

    promedio = sum(numeros) / len(numeros)

    return promedio