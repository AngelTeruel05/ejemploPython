lluvia = int(input("Ingrese los mm de lluvia acumulados: "))

# Version con if
if lluvia >= 0 and lluvia < 60:
    print("No hay ninguna alerta")
elif lluvia >= 60 and lluvia < 120:
    print("Hay alerta amarilla")
elif lluvia >= 120:
    print("Hay alerta roja")
else:
    print("Cantidad de lluvia no válida")

# Version con match
match lluvia:
    case x if x >= 0 and x < 60:
        print("No hay ninguna alerta")
    case x if x >= 60 and x < 120:
        print("Hay alerta amarilla")
    case x if x >= 120:
        print("Hay alerta roja")
    case _:
        print("Cantidad de lluvia no válida")