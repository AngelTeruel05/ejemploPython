from datos import series

print("1. Muestra una lista con los títulos de las series que sean de Animación.")
animacion = [s["titulo"] for s in series if "Animación" in s["generos"]]
print(animacion)

print()
print("2. Muestra los títulos de las series que sean de Fantasía o Misterio.")
titulos = [s["titulo"] for s in series if "Fantasía" in s["generos"] or "Misterio" in s["generos"] ]
print(titulos)


print()
print("3. Muestra los títulos de las series que tengan una nota igual o superior a 9 y que además tengan 3 o más géneros.")
titulos2 = [s["titulo"] for s in series if s["nota"] >= 9 and len(s["generos"]) >= 3]
print(titulos2)


print()
print("4. Muestra una lista de tuplas (titulo_serie, nota_dada) de las reseñas dejadas por el usuario Elena.")
tupla = [(s["titulo"], r["nota"]) for s in series for r in s["reseñas"] if r["usuario"] == "Elena"]
print(tupla)


print()
print("5. Muestra una lista con los comentarios que tengan más de 40 caracteres.")
comentario = [r["comentario"] for s in series for r in s["reseñas"] if len(r["comentario"]) > 40]
print(comentario)


print()
print("6. Muestra una lista de cadenas con el formato “La serie {titulo} tiene {n} reseñas”, para todas las series.")
cadenas = [f"La serie {s["titulo"]} tiene {len(s["reseñas"])} reseñas. " for s in series]
print(cadenas)

print()
print("7. Muestra una lista de tuplas (titulo_serie, comentario) para todas las reseñas que hayan dado una puntuación de 10.")
tuplas2 = [(s["titulo"], r["comentario"]) for s in series for r in s["reseñas"] if r["nota"] == 10]
print(tuplas2)

print()
print("8. Muestra una lista de tuplas que incluya el título de la serie y “Obra maestra” si las notas medias dadas en las reseñas es igual o superior a 9, y “Gran serie” en caso contrario.")

tuplas3 = [(s["titulo"],
  "Obra maestra" if sum(r["nota"] for r in s["reseñas"]) / len(s["reseñas"]) >= 9
  else "Gran serie")
 for s in series]

print(tuplas3)

print()
print("9. Muestra una lista con todos los géneros de todas las series. No importa si hay géneros duplicados.")
generos = [g for s in series for g in s["generos"]]
print(generos)

print()
print("10. Muestra una lista con todos los nombres de los usuarios que hayan opinado en alguna serie de Drama. No importa si hay nombres repetidos.")
usuarios = [r["usuario"] for s in series for r in s["reseñas"] if "Drama" in s["generos"]]
print(usuarios)


