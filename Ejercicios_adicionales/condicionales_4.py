#Ejercicio 4: Comparador de números
 #Objetivo: Comparar dos números con condicionales.
 #Instrucciones:
#1. Solicita dos números al usuario.
numero_uno=int(input("Ingrese un número:"))
numero_dos=int(input("Ingrese otro número:"))
#2. Si el primero es mayor, imprime: "El primer número ingresado es mayor".
if numero_uno>numero_dos:
    print("El primer número ingresado es mayor")
#3. Si el primero es menor, imprime: "El primer número ingresado es menor".
elif numero_uno<numero_dos:
    print("El primer número ingresado es menor")
#4. Si son iguales, imprime: "Los números ingresados son iguales".
elif numero_uno==numero_dos:
    print("Los números ingresados son iguales")
 #Preguntas de reflexión:
#• ¿Cómo modificarías el programa para comparar más de dos números?
#• ¿Qué pasa si se ingresan valores no numéricos?
#Da error pero se puede corregir asi:


try:
    numero_uno=int(input("Ingrese un número:")) 
    numero_dos=int(input("Ingrese otro número:"))
#2. Si el primero es mayor, imprime: "El primer número ingresado es mayor".
    if numero_uno>numero_dos:
        print("El primer número ingresado es mayor")
#3. Si el primero es menor, imprime: "El primer número ingresado es menor".
    elif numero_uno<numero_dos:
        print("El primer número ingresado es menor")
#4. Si son iguales, imprime: "Los números ingresados son iguales".
    elif numero_uno==numero_dos:
        print("Los números ingresados son iguales")

except ValueError:
    print("Error: Debe ingresar un número válido (entero).")