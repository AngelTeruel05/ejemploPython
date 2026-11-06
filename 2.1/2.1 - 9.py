numero = int(input("Ingrese un número: "))


if numero < 2:
    primo = False
else:
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo:
    print("El número es primo")
else:
    print("El número no es primo")