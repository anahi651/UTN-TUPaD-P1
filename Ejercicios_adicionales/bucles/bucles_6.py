#Ejercicio 6: Números repetidos en una lista
 #Objetivo: Filtrar elementos duplicados manteniendo el orden.
 #Instrucciones:
#1. Dada una lista (ej: [3, 1, 3, 5, 1]), crea una nueva lista con los números que aparecen más de una vez (en este caso: [3, 1]).
#Preguntas de refexión:
#• ¿Por qué es importante mantener el orden de aparición?
#• ¿Cómo resolverías esto sin usar estructuras adicionales?

lista = [3, 1, 3, 5, 1]
duplicados = []

for numero in lista:
    if lista.count(numero) > 1 and numero not in duplicados:#lista.count(numero) cuenta cuántas veces aparece ese número.numero not in duplicados asegura que no agreguemos el mismo número más de una vez.
        duplicados.append(numero)#append(numero) agrega el número a la nueva lista manteniendo el orden original.

print(duplicados)
