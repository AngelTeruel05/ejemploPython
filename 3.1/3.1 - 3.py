def calcularValorBruto(num:int, iva:str) -> float:
    """
    Función que calcula el valor bruto de un producto a partir del valor neto y el IVA.
    """
    if iva == "general":
        return num * 1.21
    elif iva == "reducido":
        return num * 1.10
    elif iva == "superreducido":
        return num * 1.04
    else:
        return "IVA no válido"

print(calcularValorBruto(100, "general"))
print(calcularValorBruto(100, "reducido"))
print(calcularValorBruto(100, "superreducido"))
print(calcularValorBruto(100, "invalido"))