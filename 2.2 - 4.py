numero = int(input("Ingrese un numero: "))

if(numero < 0):
    print("El numero es incorrecto")
else:
    fibonacci = []
    a,b = 0,1
    while a <=numero:
        ##append() sirve para añadir un elemento al final de una lista.
        fibonacci.append(a)
        a,b = b, a+b
    print("Serie de Fibonacci: ",fibonacci)

