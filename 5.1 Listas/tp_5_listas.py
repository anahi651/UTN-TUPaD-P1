#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

#list(range(inicio. fin sin incluir, intervalo)) 4 porque es el primer multiplo. 101 para que incluya 100, 4 para que sean multiplos de 4

lista_uno_a_cien=list(range(4,101,4))  

print(lista_uno_a_cien)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

#Los índices empiezan en 0. Y los negativos van desde el final: -1 es el último, -2 el penúltimo, etc.

lista_cinco_elementos=[4,8,15,16,23]

penultimo=(lista_cinco_elementos[-2])

print(penultimo)

#Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
#  Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

#Se crea lista vacia
lista_vacia=[]

#Se agregan tres palabras con append
lista_vacia.append("casa")
lista_vacia.append("auto")
lista_vacia.append("gato")

#Se imprime lista
print(lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,respectivamente.
#  Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona 
# el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

#lista inicial

animales = ["perro", "gato", "conejo", "pez"]

animales[1]="loro"   # Reemplaza "gato"
animales[-1]="oso"   # Reemplaza "oso"

print(animales)


#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.

#Se nuestra lista inicial con 5 elementos
numeros=[8,15,3,22,7]
#Primero, max(numeros) calcula y devuelve 22.
#Luego, numeros.remove(22) busca la primera (y única) aparición de 22 en la lista y la elimina in situ, modificando la lista original.
numeros.remove(max(numeros))
#se imprime la lista sin el valor maximo
print(numeros)

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.

#Se crea lista con range inicia en 10 y temina en 30, porque el ultimo no esta incluido y el intervalo es de 5, para dar saltos de 5 en 5 
lista_diez_al_treinta=list(range(10,31,5))

# se imprime los dos primeros inicia en indice 0 y termina en indice 1 porque el 2 no esta incluido
print(lista_diez_al_treinta[0:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.
#autos = ["sedan", "polo", "suran", "gol"]

#Lista original
autos = ["sedan", "polo", "suran", "gol"]
# Reemplaza índices 1 y 2 de la lista “autos” por dos nuevos valores
autos[1:3] = ["Duster", "ka"]

#Se imprime lista con valores reemplazados
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla.

# Se crea una lista vacia llamada dobles 
dobles=[]
#Se utiliza append para agregar en la lista vacia el doble de 5,10,15
dobles.append((2*5))
dobles.append((2*10))
dobles.append((2*15))
print(dobles)


#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]

#Se agrega "jugo" a la lista del tercer cliente usando append.

compras[2].append("jugo")

#Se reemplaza "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1]="tallarines"

#Se elimina "pan" de la primer lista 
compras[0].remove("pan")

#Se imprime lista 
print(compras)

#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#"● Posición lista_anidada[2][2]: 30.6
#"● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla

lista_anidada=[[15],[True],[25.5,57.9,30.6],[False]]

print(lista_anidada)