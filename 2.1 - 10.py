num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("Error: el primer número debe ser menor o igual que el segundo.")
else:
    print("Números primos dentro del rango:")

    for numero in range(num1, num2 + 1):
        if numero >= 2:
            primo = True

            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break

            if primo:
                print(numero)

