def convertirTemperatura(num : float, unidad1 : str, unidad2 : str) -> float:
    """
    Función que convierte una temperatura de CelsiuS, Fahrenheit o Kelvin a otra unidad de temperatura.
    """

    if unidad1 == "C" and unidad2 == "F":
        return (num * 9/5) + 32
    elif unidad1 == "C" and unidad2 == "K":
        return num + 273.15
    elif unidad1 == "F" and unidad2 == "C":
        return (num - 32) * 5/9
    elif unidad1 == "F" and unidad2 == "K":
        return (num - 32) * 5/9 + 273.15
    elif unidad1 == "K" and unidad2 == "C":
        return num - 273.15
    elif unidad1 == "K" and unidad2 == "F":
        return (num - 273.15) * 9/5 + 32

print(convertirTemperatura(100, "C", "F"))
print(convertirTemperatura(100, "C", "K"))
print(convertirTemperatura(212, "F", "C"))
print(convertirTemperatura(212, "F", "K"))
print(convertirTemperatura(373.15, "K", "C"))
print(convertirTemperatura(373.15, "K", "F"))