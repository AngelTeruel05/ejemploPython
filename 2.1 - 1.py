nota = int(input("Ingresa una nota: "))

if nota >= 0 and nota < 5:
    print("Suspenso")
elif nota >= 5 and nota < 7:
    print("Aprobado")
elif nota >= 7 and nota < 9:
    print("Notable")
elif nota >= 9 and nota <= 10:
    print("Sobresaliente")
else:
    print("Nota no válida")

match nota:
    case 0| 1 | 2 | 3 | 4:
        print("Suspenso")
    case 5 | 6:
        print("Aprobado")
    case 7| 8:
        print("Notable")
    case 9 | 10:
        print("Sobresaliente")
    case _:
        print("Nota no válida")
