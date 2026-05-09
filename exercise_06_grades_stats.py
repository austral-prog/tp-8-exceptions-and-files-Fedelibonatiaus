import os


def grades_stats(filename):

    if not os.path.exists(filename):
        raise FileNotFoundError

    estadisticas = {}

    with open(filename, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea != "":

                estudiante, notas = linea.split(":")

                notas = notas.split(",")

                notas_float = []

                for nota in notas:
                    notas_float.append(float(nota))

                promedio = sum(notas_float) / len(notas_float)

                maximo = max(notas_float)

                minimo = min(notas_float)

                estadisticas[estudiante] = (promedio, maximo, minimo)

    return estadisticas