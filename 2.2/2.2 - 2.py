numero = int(input("Ingrese un número: "))
resultado = 1

if numero < 1:
    print("El número es inválido")
else:
    for i in range(1, numero + 1):
        resultado = resultado * i

print("El factorial de ",numero, "es:", resultado)