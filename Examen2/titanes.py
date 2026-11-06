from datos import personajes

def ejercicio1():
    lista = [p["nombre"] for p in personajes if p["afiliación"] == "Cuerpo de Exploración"]
    print(lista)

def ejercicio2():
    lista2 = [p["nombre"] for p in personajes if "Sigilo" in p["habilidades"] or "Supervivencia" in p["habilidades"]]
    print(lista2)

def ejercicio3():
    tupla = [(p["nombre"],p["afiliación"]) for p in personajes if p["afiliación"] != "Cuerpo de Exploración" ]
    print(tupla)

def ejercicio4():
    cadena = [f"{p["nombre"]} {p["afiliación"]}" for p in personajes if p["registro_combate"]["misiones_completadas"] >= 20]
    print(cadena)

def ejercicio5():
    tupla2 = [(p["nombre"], p["estatura_m"]*100) for p in personajes if p["estatura_m"] > 1.70]
    print(tupla2)

def ejercicio6():
    habilidades = [p["habilidades"] for p in personajes]
    print(habilidades)

def ejercicio7():
    killers = [p["nombre"] for p in personajes if (p["registro_combate"]["titanes_solo"] + p["registro_combate"]["titanes_equipo"])  > 5]
    print(killers)

def ejercicio8():
    diccionario = [{"Nombre:" : p["nombre"], "Titanes_totales:" :
                    (p["registro_combate"]["titanes_solo"] + p["registro_combate"]["titanes_equipo"])} for p in personajes ]
    print(diccionario)


def ejercicio9():
    media_altura = sum(p["estatura_m"]   / len(personajes) for p in personajes)
    print("Media de altura:",media_altura)

def ejercicio10():
    media_altura = sum(p["estatura_m"]   / len(personajes) for p in personajes)
    tupla10 = [(p["nombre"],p["estatura_m"]) for p in personajes if p["estatura_m"] > media_altura]
    print(tupla10)