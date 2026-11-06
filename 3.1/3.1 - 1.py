def dni(c : str) -> bool:
    """
    Función que confirma si la letra de un DNI es correcta.
    """
    if len(c) != 9:
        return "Longitud incorrecta"

    lista = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B",
             "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

    num = int(c[:-1])  # Convertimos los primeros 8 caracteres a entero

    resto = num % 23  # Calculamos el resto de la división entre 23

    letra_correcta = lista[resto]  # Obtenemos la letra correcta según el resto
    if c[-1].upper() == letra_correcta:
        return True
    else:
        return False
print(dni("77797584S"))
print(dni("77797584L"))