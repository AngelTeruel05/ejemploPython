from datos import personajes

def ejercicio1():
    print("EJERCICIO1")
    nuevo_personaje = {
        "nombre" : "Numero 18",
        "raza" : "Androide",
        "nivel_pelea" : 11000000,
        "tecnicas" : ["Galick HO", "FInal Flash","Big Bang Attack"],
        "atributos" : {"fuerza":103, "defensa":60,"velocidad":90}
    }
    personajes.append(nuevo_personaje)
    print("Personaje importado con exito")
    for personaje in personajes:
        print(personaje)

def ejercicio2():
    print("EJERCICIO2")
    for personaje in personajes:
        media_poder = (personaje["atributos"]["defensa"] + personaje["atributos"]["fuerza"] + personaje["atributos"]["velocidad"]) / 3
        if media_poder > 80:
            print(personaje)

def ejercicio3():
    print("EJERCICIO3")
    suma_velocidad=0
    contador=0
    for personaje in personajes:
        suma_velocidad = suma_velocidad + personaje["atributos"]["velocidad"]
        contador += 1

    media_velocidad = suma_velocidad / contador

    for personaje in personajes:
        if personaje["atributos"]["velocidad"] > media_velocidad:
            print(personaje)

def ejercicio4():
    print("EJERCICIO4")
    for personaje in personajes:
        if "Big Bang Attack" in personaje["tecnicas"]:
            personaje["atributos"]["fuerza"] =  personaje["atributos"]["fuerza"] + 10
            if personaje["atributos"]["fuerza"] > 100:
                personaje["atributos"]["fuerza"] = 100
        print(personaje["nombre"], personaje["atributos"]["fuerza"])

def ejercicio5():
    print("EJERCICIO5")
    for personaje in personajes:
        if personaje["atributos"]["defensa"] < personajes[0]["atributos"]["fuerza"]:
            print(personaje["nombre"], personaje["atributos"]["defensa"])

def ejercicio6():
    print("EJERCICIO6")
    for personaje in personajes[:]:
        if personaje["raza"] == "Saiyan":
            personajes.remove(personaje)

    for personaje in personajes:
        print(personaje)





         