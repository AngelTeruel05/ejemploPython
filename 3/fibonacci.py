def fibonacci(n : int) -> list:
    """
    Función que calcula los primeros n números de la secuencia de Fibonacci.

    Args:
        n (int): Número de términos de la secuencia de Fibonacci a calcular.

    Returns:
        list: Una lista que contiene los primeros n números de la secuencia de Fibonacci.
    """
    if n < 1:
        raise ValueError("El número debe ser mayor o igual a 1.")
    
    lista = []
    a, b = 0, 1
    for _ in range(n):
        lista.append(a)
        a, b = b, a + b
    
    return lista

print(fibonacci(10))  # Ejemplo de uso, debería imprimir los primeros 10 números de Fibonacci