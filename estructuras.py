numero = int(input("Ingrese un número: "))
if numero > 0:
   print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero") 

dia = input("Ingrese un día de la semana: ")
match dia:
    case "lunes":
        print("Hoy es lunes")
    case "martes":
        print("Hoy es martes")
    case "miércoles":
        print("Hoy es miércoles")
    case "jueves":
        print("Hoy es jueves")
    case "viernes":
        print("Hoy es viernes")
    case "sábado":
        print("Hoy es sábado")
    case "domingo":
        print("Hoy es domingo")
    case _:
        print("Día no válido")

dia2 = input("Ingrese un día de la semana: ")
match dia2:
    case "lunes" | "martes" | "miércoles" | "jueves" | "viernes":
        print("Es un día laboral")
    case "sábado" | "domingo":
        print("Es fin de semana")
    case _:
        print("Día no válido")