#Ejercicio 3: Clasificador de números
# Objetivo: Determinar el signo de un número.
# Instrucciones:
#1. Pide un número al usuario.
numero=float(input("Ingrese un numero:"))
#2. Si es positivo, imprime: "El número es positivo".
if numero > 0:
    print("El número es positivo")
#3. Si es negativo, imprime: "El número es negativo".
elif numero < 0:
    print("El número es negativo")
#4. Si es cero, imprime: "El número es cero".
elif numero == 0:
    print("El número es cero")


# Preguntas de reflexión:
#• ¿Qué ocurre si el usuario ingresa un texto?
#Error no se puede convertir un string en float
# Ejercicio 3: Clasificador de números
# Objetivo: Determinar el signo de un número.

# 1. Pide un número al usuario.
try:
    numero = float(input("Ingrese un número: "))

    # 2. Si es positivo
    if numero > 0:
        print("El número es positivo")

    # 3. Si es negativo
    elif numero < 0:
        print("El número es negativo")

    # 4. Si es cero
    else:
        print("El número es cero")

except ValueError:
    print("Error: Debe ingresar un número válido (entero o decimal).")

#• ¿Cómo adaptarías el código para números decimales?
#En este caso ya esta adaptado porque el input se convierte en float