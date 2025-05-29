 #Ejercicio 5: Contador de vocales
 #Objetivo: Contar caracteres específicos en un string.
 #Instrucciones:
#1. Pide al usuario una cadena de texto.
#2. Cuenta y muestra cuántas vocales (a, e, i, o, u) contiene.

cadena=input("Ingrese frase:").lower()
contador=0
for letra in cadena:
    if letra in "aeiouáéíóú":
        contador=contador+1
print(f"La cantidad de vocales es de:{contador}")
