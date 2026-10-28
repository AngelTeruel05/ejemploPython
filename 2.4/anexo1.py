jugadores = [
    {
        "nombre": "Lionel Messi",
        "equipo": "Inter Miami",
        "dorsal": 10,
        "atributos": {"tiro": 10, "pase": 10, "regate": 10},
        "filigranas": ["ruleta", "caño", "sombrero", "bicicleta"]
    },
    {
        "nombre": "Vinicius Jr",
        "equipo": "Real Madrid",
        "dorsal": 7,
        "atributos": {"tiro": 8, "pase": 7, "regate": 9},
        "filigranas": ["elasticidad", "bicicleta", "ruleta"]
    },
    {
        "nombre": "Pedri",
        "equipo": "FC Barcelona",
        "dorsal": 8,
        "atributos": {"tiro": 6, "pase": 9, "regate": 8},
        "filigranas": ["ruleta", "caño"]
    },
    {
        "nombre": "Lamine Yamal",
        "equipo": "FC Barcelona",
        "dorsal": 19,
        "atributos": {"tiro": 8, "pase": 8, "regate": 9},
        "filigranas": ["bicicleta", "elasticidad"]
    },
    {
        "nombre": "Luka Modric",
        "equipo": "Real Madrid",
        "dorsal": 10,
        "atributos": {"tiro": 7, "pase": 10, "regate": 8},
        "filigranas": ["exterior", "ruleta"]
    },
    {
        "nombre": "Erling Haaland",
        "equipo": "Manchester City",
        "dorsal": 9,
        "atributos": {"tiro": 10, "pase": 5, "regate": 6},
        "filigranas": ["sombrero"]
    }
]

print("1.Muestra una lista solo con los nombres de todos los futbolistas.")
nombres = [j["nombre"] for j in jugadores]
print(nombres)


print()
print("2. Muestra la lista de los jugadores que llevan el dorsal número 10.")
dorsal10 = [j for j in jugadores if j["dorsal"] == 10];
print(dorsal10)

print()
print("3. Muestra una lista con los nombres de los jugadores que pertenecen al FC Barcelona.")
barcelona = [j["nombre"] for j in jugadores if j["equipo"] == "FC Barcelona"]
print(barcelona)


print()
print("4. Muestra una lista con los nombres de los jugadores que tienen una puntuación de pase igual o superior a 9 en sus atributos.")
pase = [j["nombre"] for j in jugadores if j["atributos"]["pase"] >= 9]
print(pase)

print()
print("5. Muestra la lista de los jugadores que saben hacer la filigrana 'ruleta'.")
ruleta = [j["nombre"] for j in jugadores if "ruleta" in j["filigranas"]]
print(ruleta)

print()
print("6. Muestra una lista con los jugadores que tienen tiro >= 8 Y regate >= 9.")
tiroRegate = [j["nombre"] for j in jugadores if j["atributos"]["tiro"] >=8 and j["atributos"]["regate"] >=9]
print(tiroRegate)

print()
print("7. Crea una lista de cadenas de texto con la forma 'Nombre (Equipo)' para cada jugador. Muéstrala.")
cadena = [j["nombre"] +" ("+ j["equipo"] +")" for j in jugadores]
print(cadena)

print()
print("8. Crea una lista de tuplas con el nombre del jugador y el texto 'Goleador' si su atributo de tiro es mayor o igual a 9, o 'Asistente' en caso contrario. Muéstrala.")
apodo=""
tuplas = [(j["nombre"],"Goleador") if j["atributos"]["tiro"] >= 9 else (j["nombre"],"Asistente") for j in jugadores]
print(tuplas)

print()
print("9. Muestra una lista con los nombres de los jugadores que dominan más de 2 filigranas distintas.")
dominan = [j["nombre"] for j in jugadores if len(j["filigranas"]) > 2]
print(dominan)

print()
print("10. Extrae en una única lista todas las filigranas de todos los jugadores (no importa si hay duplicadas) y muéstrala.")
todas = [f for j in jugadores for f in j["filigranas"]]
print(todas)



