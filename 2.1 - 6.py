correcta =  False;

while not correcta:
    contraseña = input("Ingrese la contraseña: ")
    if contraseña == "12345":
        print("Contraseña correcta, bienvenido")
        correcta = True
    else:
        print("Contraseña incorrecta, intente nuevamente")