num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primer número debe ser menor o igual al segundo número")
else: 
    for i in range(num1, num2 + 1):
        if i % 2 == 0:
            print(i)

if num1 > num2:
    print("El primer número debe ser menor o igual al segundo número")
else:
    while num1 <= num2:
        if num1 % 2 == 0:
            print(num1)
        num1 += 1
