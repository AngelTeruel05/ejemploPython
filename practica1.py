def main():
    lista = ["Manzana", "Pera", "Melon"]
    lista2 = ["Kiwi", "Sandia", "Melon"]

    lista.extend(lista2)

    print("Ultimo elemento: ", lista[-1])

    tupla1 = [3,5,7]

    print(tupla1[0])

    inicio = int(input("Introduce el inicio: "))
    fin = int(input("Introduce el fin: "))
    salto = int(input("Introduce el salto: "))
    
    rango = range(inicio, fin, salto)

    print("Rango: ",rango)
if __name__ == "__main__":
    main()