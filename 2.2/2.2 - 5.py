filas = int(input("Ingrese el número de filas: "))

if filas < 0:
    print("El número de filas es incorrecto")
else:
    for i in range(filas):
        numero = 1
        for j in range(i + 1):
            ##El end=" " sirve para que no salte a la siguiente línea después de imprimir.
            print(numero, end=" ")
            ##El // significa división entera.
            numero = numero * (i - j) // (j + 1)
        print()