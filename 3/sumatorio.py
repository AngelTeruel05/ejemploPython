def sumatorio(n : int) -> int:
    """
    Función que calcula el sumatorio de los números enteros desde 1 hasta n.

    Args:
        n (int): Número entero hasta el cual se calculará el sumatorio.

    Returns:
        int: La suma de los números enteros desde 1 hasta n.
    """
    if n < 1:
        raise ValueError("El número debe ser mayor o igual a 1.")
    
    suma = 0
    for i in range(1, n + 1):
        suma += i
    
    return suma

print(sumatorio(5))  # Ejemplo de uso, debería imprimir 15
