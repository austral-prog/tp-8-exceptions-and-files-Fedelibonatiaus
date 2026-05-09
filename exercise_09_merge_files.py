def merge_files(file1, file2, output):

    with open(file1, "r") as archivo1:
        contenido1 = archivo1.read()

    with open(file2, "r") as archivo2:
        contenido2 = archivo2.read()

    with open(output, "w") as salida:
        salida.write(contenido1)
        salida.write(contenido2)