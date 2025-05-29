#Ejercicio 1: Validación de contraseña
#Objetivo: Analizar un programa existente que verifica una contraseña.
#Instrucciones:
#1. Lee el siguiente código y explica qué hace:
#contrasena_correcta = "programacion1"
#contrasena_usuario = input("Introduce la contraseña: ")
#if contrasena_usuario == contrasena_correcta:
 #print("Contraseña correcta. Bienvenido.")
#else:
 #print("Contraseña incorrecta. Intenta de nuevo.")
# Preguntas de reflexión:
#• ¿Qué pasa si el usuario ingresa la contraseña con mayúsculas?
#No lo reconoce se puede cambiar agregando un funcion que cambie a minusculas cualquier contraseña ingresada
#contrasena_correcta = "programacion1"
#if contrasena_usuario == contrasena_correcta:
 #print("Contraseña correcta. Bienvenido.")
#else:
 #print("Contraseña incorrecta. Intenta de nuevo.")
#• ¿Cómo mejorarías el programa para dar más intentos?

#  Validar la contraseña con hasta 3 intentos

contrasena_correcta = "programacion1"

# Primer intento
contrasena_usuario = input("Introduce la contraseña: ").lower()
if contrasena_usuario == contrasena_correcta:
    print("Contraseña correcta. Bienvenido.")
else:
    # Segundo intento
    contrasena_usuario = input("Contraseña incorrecta. Intenta de nuevo: ").lower()
    if contrasena_usuario == contrasena_correcta:
        print("Contraseña correcta. Bienvenido.")
    else:
        # Tercer intento
        contrasena_usuario = input("Último intento: ").lower()
        if contrasena_usuario == contrasena_correcta:
            print("Contraseña correcta. Bienvenido.")
        else:
            print("Has superado el número de intentos. Acceso denegado.")
