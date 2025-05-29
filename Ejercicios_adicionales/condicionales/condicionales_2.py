#Ejercicio 2: Identificador de vocales
 #Objetivo: Clasificar caracteres usando condicionales.
 #Instrucciones:
#1. Solicita una letra al usuario.
letra=input("Ingrese letra:").lower()
#2. Si es una vocal (a, e, i, o, u, en mayúscula o minúscula), imprime: "La letra
#ingresada es una vocal".
if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print(f"La letra ingresada:{letra}, es una vocal")
#3. En otro caso, imprime: "La letra ingresada no es una vocal".
else:
    print(f"La letra ingresada:{letra},no es una vocal")
 #Preguntas de reflexión:
#• ¿Cómo manejarías vocales acentuadas (á, é)?
if letra in "aeiouáéíóú":
    pass
#• ¿Qué estructura usarías para simplificar las comparaciones?
if letra in "aeiouáéíóú":
    pass