def ejercicio1():
    print("--- Ejecutando Ejercicio 1 ---")
    lista = ["Manzana", "Pera", "Melocotón"]
    lista1 = ["Kiwi", "Sandía", "Melón"]
    lista.extend(lista1)
    print(f"Último elemento: {lista[-1]}")

def ejercicio2():
    print("\n--- Ejecutando Ejercicio 2 ---")
    # Ejemplo: Calcular el área de un cuadrado
    lado = float(input("Introduce el lado del cuadrado: "))
    area = lado * lado
    print(f"El área del cuadrado es: {area}")

def ejercicio3():
    print("\n--- Ejecutando Ejercicio 3 ---")
    # Ejemplo: Verificar si un número es par o impar
    numero = int(input("Introduce un número entero: "))
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

def main():
    # Aquí controlas el orden en el que se ejecutan
    ejercicio1()
    ejercicio2()
    ejercicio3()

if __name__ == "__main__":
    main()
