personajes_frieren = [
{
"nombre": "Frieren",
"raza": "Elfo",
"clase": "Mago",
"edad": 1000,
"afiliacion": ["Grupo de los Cuatro Héroes", "Grupo de Frieren"]
},
{
"nombre": "Himmel",
"raza": "Humano",
"clase": "Héroe",
"edad": 76,
"afiliacion": ["Grupo de los Cuatro Héroes"]
},
{
"nombre": "Fern",
"raza": "Humano",
"clase": "Mago",
"edad": 19,
"afiliacion": ["Grupo de Frieren", "Magos de Primera Clase"]
},

{
"nombre": "Stark",
"raza": "Humano",
"clase": "Guerrero",
"edad": 18,
"afiliacion": ["Grupo de Frieren"]
},
{
"nombre": "Heiter",
"raza": "Humano",
"clase": "Sacerdote",
"edad": 100,
"afiliacion": ["Grupo de los Cuatro Héroes"]
},
{
"nombre": "Eisen",
"raza": "Enano",
"clase": "Guerrero",
"edad": 120,
"afiliacion": ["Grupo de los Cuatro Héroes"]
},
{
"nombre": "Sein",
"raza": "Humano",
"clase": "Sacerdote",
"edad": 28,
"afiliacion": ["Grupo de Frieren"]
},
{
"nombre": "Ubel",
"raza": "Humano",
"clase": "Mago",
"edad": 19,
"afiliacion": ["Magos de Primera Clase"]
},
{
"nombre": "Aura la Guillotina",
"raza": "Demonio",
"clase": "Mago",
"edad": 500,
"afiliacion": ["Siete Sabios de la Destrucción"]
},
{
"nombre": "Denken",
"raza": "Humano",
"clase": "Mago",
"edad": 78,
"afiliacion": ["Magos de Primera Clase", "Asociación Continental de Magia"]

},
{
"nombre": "Serie",
"raza": "Elfo",
"clase": "Mago",
"edad": 2000,
"afiliacion": ["Asociación Continental de Magia"]
},
{
"nombre": "Sense",
"raza": "Humano",
"clase": "Mago",
"edad": 28,
"afiliacion": ["Magos de Primera Clase", "Asociación Continental de Magia"]
}
]

print("8. Muestra la edad media de los personajes humanos.")
contadorHumanos = 0
sumaEdadHumanos = 0
for personaje in personajes_frieren:
    if personaje["raza"] == "Humano":
        sumaEdadHumanos = sumaEdadHumanos + personaje["edad"]
        contadorHumanos = contadorHumanos + 1
print("La edad media de los personajes humanos es:", sumaEdadHumanos / contadorHumanos)



print()
print("9. Muestra el nombre y la raza de todos los personajes que sean magos de primera clase.")

for personaje in personajes_frieren:
    if "Magos de Primera Clase" in personaje["afiliacion"]:
        print(personaje["nombre"], personaje["raza"])

print()
print("10. Muestra el nombre, la raza y la edad de los personajes del grupo de los cuatro héroes.")

for personaje in personajes_frieren:
    if "Grupo de los Cuatro Héroes" in personaje["afiliacion"]:
        print(personaje["nombre"], personaje["raza"], personaje["edad"])

print()
print("11. Inserta al final de la lista un nuevo personaje que tenga todos los " \
"campos con algún valor con sentido (puedes inventártelos, pero que" \
" sean razonables).")
nuevo_personaje = {
    "nombre": "Metode",
    "raza": "Humano",
    "clase": "Mago",
    "edad": 25,
    "afiliacion": ["Magos de Primera Clase"]
}

personajes_frieren.append(nuevo_personaje)

print()
print("12. Elimina todos los personajes cuya raza sea demonio.")

for personaje in personajes_frieren:
    if personaje["raza"] == "Demonio":
        personajes_frieren.remove(personaje)
        print("Personaje eliminado:", personaje["nombre"], personaje["raza"])


print()
print("13. Añádele a todos los elfos la afiliación “Elfos Supervivientes del Examen de Python”")

for personaje in personajes_frieren:
    if personaje["raza"] == "Elfo":
        personaje["afiliacion"].append("Elfos Supervivientes del Examen de Python")
        print("Afiliación añadida a:", personaje["nombre"], personaje["raza"], personaje["afiliacion"])


print()
print("14. A todos los personajes que pertenezcan a la Asociación Continental de Magia, " \
"quítales esa afiliación.")

for personaje in personajes_frieren:
    if "Asociación Continental de Magia" in personaje["afiliacion"]:
        personaje["afiliacion"].remove("Asociación Continental de Magia")
        print("Afiliación eliminada a:", personaje["nombre"], personaje["raza"], personaje["afiliacion"])

print()
print("15. Modifica la raza de todos los humanos que tengan 100 o más años a “Zombie”.")

for personaje in personajes_frieren:
    if personaje["raza"] == "Humano" and personaje["edad"] >= 100:
        personaje ["raza"] = "Zombie"
        print("Raza modificada a:", personaje["nombre"], personaje["raza"], personaje["edad"])



