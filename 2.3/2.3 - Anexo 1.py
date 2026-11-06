pokemons = [
{
"nombre": "Bulbasaur",
"generacion": 1,

"categoria": "Semilla",
"tipos": ["Planta", "Veneno"],
"peso_kg": 6.9,
"altura_m": 0.7
},
{
"nombre": "Charizard",
"generacion": 1,
"categoria": "Llama",
"tipos": ["Fuego", "Volador"],
"peso_kg": 90.5,
"altura_m": 1.7
},
{
"nombre": "Squirtle",
"generacion": 1,
"categoria": "Tortuguita",
"tipos": ["Agua"],
"peso_kg": 9.0,
"altura_m": 0.5
},
{
"nombre": "Pikachu",
"generacion": 1,
"categoria": "Ratón",
"tipos": ["Eléctrico"],
"peso_kg": 6.0,
"altura_m": 0.4
},
{
"nombre": "Jigglypuff",
"generacion": 1,
"categoria": "Globo",
"tipos": ["Normal", "Hada"],
"peso_kg": 5.5,
"altura_m": 0.5
},
{
"nombre": "Eevee",
"generacion": 1,
"categoria": "Evolución",
"tipos": ["Normal"],
"peso_kg": 6.5,
"altura_m": 0.3
},
{
"nombre": "Lucario",
"generacion": 4,

"categoria": "Aura",
"tipos": ["Lucha", "Acero"],
"peso_kg": 54.0,
"altura_m": 1.2
},
{
"nombre": "Gardevoir",
"generacion": 3,
"categoria": "Envolvente",
"tipos": ["Psíquico", "Hada"],
"peso_kg": 48.4,
"altura_m": 1.6
},
{
"nombre": "Greninja",
"generacion": 6,
"categoria": "Ninja",
"tipos": ["Agua", "Siniestro"],
"peso_kg": 40.0,
"altura_m": 1.5
}
]

print("1. Muestra en una sóla línea el nombre y el peso del pokémon con más peso.")
pokemon_mas_pesado = pokemons[0]
nueva_lista = [pokemon for pokemon in pokemons if pokemon["peso_kg"] > pokemon_mas_pesado]


for pokemon in pokemons:
    if pokemon["peso_kg"] > pokemon_mas_pesado["peso_kg"]:
        pokemon_mas_pesado = pokemon
print(pokemon_mas_pesado["nombre"], pokemon_mas_pesado["peso_kg"])

print()
print("2. Muestra la media de altura de todos los pokemons")
suma = 0
for pokemon in pokemons:
    suma = suma + pokemon["altura_m"]
pokemon_media_altura = suma / len(pokemons)
print("Media de altura de todos los pokemons es de: ", pokemon_media_altura)

print()
print("3. Muestra el nombre y la altura de todos los pokémons que " \
"midan menos que la media.")

for pokemon in pokemons:
    if(pokemon["altura_m"] < pokemon_media_altura):
        print(pokemon["nombre"], pokemon["altura_m"])


print()
print("4. Muestra el nombre y los tipos de los pokémons que sean de tipo agua.")

for pokemon in pokemons:
    if "Agua" in pokemon["tipos"]:
        print(pokemon["nombre"], pokemon["tipos"])

print()
print("5. Muestra los pokémons que tengan un tipo que acabe en “a”.")
for pokemon in pokemons:
    if pokemon["tipos"][0].endswith("a"):
        print(pokemon["nombre"], pokemon["tipos"])

print()
print("6. Inserta al final de la lista un nuevo pokémon que tenga " \
"todos los campos con algún valor con sentido (puedes inventártelos, " \
"pero que sean razonables).")

nuevo_pokemon = {
    "nombre": "Mewtwo",
    "generacion": 1,
    "categoria": "Místico",
    "tipos": ["Psíquico"],
    "peso_kg": 122.0,
    "altura_m": 2.0
}
pokemons.append(nuevo_pokemon)
print("Nuevo pokémon insertado:", nuevo_pokemon["nombre"])

print()
print("7. Elimina todos los pokémons de tipo normal.")

for pokemon in pokemons:
    if "Normal" in pokemon["tipos"]:
        pokemons.remove(pokemon)
        print("Pokémon de tipo normal eliminado:", pokemon["nombre"])

