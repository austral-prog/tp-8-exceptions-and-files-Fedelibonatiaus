import os


def parse_log(filename):

    if not os.path.exists(filename):
        raise FileNotFoundError

    logs = {}

    with open(filename, "r") as archivo:

        for linea in archivo:

            linea = linea.strip()

            if linea != "":

                if ":" not in linea:
                    raise ValueError("invalid log line")

                nivel, mensaje = linea.split(":", 1)

                nivel = nivel.strip()

                mensaje = mensaje.strip()

                if nivel in logs:
                    logs[nivel].append(mensaje)

                else:
                    logs[nivel] = [mensaje]

    return logs