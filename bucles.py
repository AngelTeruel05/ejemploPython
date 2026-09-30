for i in range(1,10):
    print(i)

print("De dos en dos")
for i in range(1,10,2):
    print(i)

print("For en decreciente")
for i in range(10,1,-1):
    print(i)

juegos = [
    {
        
        "nombre" : "FIFA",
        "plataforma" : "PS5"
    },
    {
        "nombre" : "GTA",
        "plataforma" : "PC"
    }
    
]

for juego in juegos:
    print(juego["nombre"])

palabra = "hOLA MUNDO"

for letra in palabra:
    print(letra.lower())

##WHILE
print("Bucles While")
contador = 0
while contador <= 10:
    print(contador)
    contador += 1


animales = ["perro", "gato", "conejo"]

while animales:
    animal = animales.pop(0)
    print(animal)




