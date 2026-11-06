base = int(input("Ingrese la base: "))
potencia = int(input("Ingrese la potencia: "))

resultado = 1

if base < 0 or potencia < 0:
    print ("La base o la potencia son inválidas")
else:
    for i in range(1,potencia +1):
        resultado = resultado * base

    print("El resultado de", base, "elevado a", potencia, "es:", resultado)
