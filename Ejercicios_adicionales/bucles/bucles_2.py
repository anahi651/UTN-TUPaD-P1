# Paso 1: Inicializar variables
suma = 0               # Acumula la suma total
contador = 0           # Cuenta cuántos números válidos se ingresaron

# Paso 2: Bucle while que sigue hasta que la suma supere 100
while suma <= 100:
    try:
        # Paso 3: Pedir número al usuario y convertirlo a float
        numero = float(input("Ingrese un número: "))
        
        # Paso 4: Sumar el número ingresado
        suma += numero
        
        # Paso 5: Aumentar el contador solo si el número fue válido
        contador += 1

    except ValueError:
        # Paso 6: Manejo de errores si el usuario no ingresa un número
        print("Entrada no válida. Por favor, ingrese un número válido.")

# Paso 7: Mostrar resultados finales
print("La suma total es:", suma)
print("Cantidad de números ingresados:", contador)
