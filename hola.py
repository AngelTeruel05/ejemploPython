diccionario = {
    "nombre" : "Pepe",
    "apellido" : "López",
    "edad" : 18
}
diccionario["edad"] = 20
diccionario["direccion"] = "calle 1"
print(diccionario)

estudiante = [
    {
        "nombre" : "Joselin",
        "apellido" : "Flores",
        "modulos" : ["Acceso a datos", "python", "Proyecto"]
    },
    {
        "nombre" : "Lucas",
        "apellido": "Moura",
        "modulos" : ["Acceso a datos", "Desarrollo de interfaces"]
    }
]

print(estudiante[1]["modulos"])

conjunto = {1,2,3,3,4,5}
conjunto.add(7)
conjunto.remove(3)
print(conjunto)

def main():
    print("Este es mi main")