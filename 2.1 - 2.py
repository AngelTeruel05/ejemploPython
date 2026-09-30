precio = float(input("Ingrese el precio del producto: "))
iva = input("General, Reducido o Superreducido: ").lower()

match iva:
    case "general":
        precio_final = precio * 1.21
        print("El precio final con IVA general es: ", precio_final)
    case "reducido":
        precio_final = precio * 1.10
        print("El precio final con IVA reducido es: ", precio_final)
    case "superreducido":
        precio_final = precio * 1.04
        print("El precio final con IVA superreducido es: ", precio_final)
    case _:
        print("Tipo de IVA no válido")