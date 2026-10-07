entero = int(input("Ingrese un número entero: "))

suma = 0

if entero < 1:
    print("El numero es invalido")
else :
    for i in range(1, entero + 1):
        suma = i + suma

print("La suma de los números enteros desde 1 hasta", entero, "es:", suma)