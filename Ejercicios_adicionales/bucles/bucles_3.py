#Eercicio 3: Filtrar palabras por letra inicial
 #Objetivo: Iterar sobre una lista y aplicar filtros.
 #Instrucciones:
#1. Dada una lista de palabras (ej: ["apple", "banana", "avocado"]), imprime solo las que empiezan con "a".
# Preguntas de reflexión:
#• ¿Cómo harías que la comparación sea case-insensitive (ej: "Apple" también se cuente)?
#• ¿Qué método de strings es útil para esto?
palabras = ["apple", "banana", "avocado"]
lista_nueva = []

for palabra in palabras:  #  Recorremos cada palabra de la lista original
    if palabra.lower().startswith("a"):  # Comprobamos si empieza con "a" (ignorando mayúsculas/minúsculas)
        lista_nueva.append(palabra)  # Agregamos la palabra a la nueva lista

print("Palabras que comienzan con 'a':", lista_nueva)

      