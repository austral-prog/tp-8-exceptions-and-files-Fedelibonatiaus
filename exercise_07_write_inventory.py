def write_inventory(filename, inventory):

    with open(filename, "w") as archivo:

        items_ordenados = sorted(inventory)

        for item in items_ordenados:

            archivo.write(f"{item}:{inventory[item]}\n")