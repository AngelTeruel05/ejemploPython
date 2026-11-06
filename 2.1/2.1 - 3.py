edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad < 18:
    print("Eres menor de edad")
elif edad >= 120:
    print("Eres un vampiro")
elif edad < 0:
    print("Edad no válida")
else:
    print("Eres mayor de edad")