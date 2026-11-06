def factorial(n : int) -> int:
    """
    Función que calcula el factorial de un número entero.

    Args:
        n (int): Número entero del cual se calculará el factorial.

    Returns:
        int: El factorial del número entero.
    """
    if n < 0:
        raise ValueError("El número debe ser mayor o igual a 0.")
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    
    return resultado

print(factorial(5))  # Ejemplo de uso, debería imprimir 120