import os


def csv_to_dict(filename):

    if not os.path.exists(filename):
        raise FileNotFoundError

    personas = []

    with open(filename, "r") as archivo:

        lineas = archivo.readlines()

    if len(lineas) <= 1:
        return []

    header = lineas[0].strip().split(",")

    for linea in lineas[1:]:

        linea = linea.strip()

        if linea != "":

            valores = linea.split(",")

            persona = {
                header[0]: valores[0].strip(),
                header[1]: int(valores[1].strip()),
                header[2]: valores[2].strip()
            }

            personas.append(persona)

    return personas