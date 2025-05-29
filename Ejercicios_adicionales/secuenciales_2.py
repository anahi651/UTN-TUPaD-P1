# Ejercicio 2: Conversión de grados Celsius a Fahrenheit
# Objetivo: Realizar la conversión de temperatura de Celsius a Fahrenheit.

# 1. Solicitar al usuario una temperatura en grados Celsius.
temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# 2. Convertirla a Fahrenheit con la fórmula: F = (C * 9/5) + 32.
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32

# 3. Mostrar el resultado en pantalla.
print("La temperatura en",temperatura_celsius, "Fahrenheit es:",temperatura_fahrenheit)
# Preguntas de reflexión:

# ¿Qué resultado se obtiene al ingresar 0°C?
# Se obtiene como resultado 32.0°F. Esto se debe a que al aplicar la fórmula: (0 * 9/5) + 32, el resultado es 32.

# ¿Cómo se adaptaría este ejercicio para convertir a Kelvin?
# Para convertir de grados Celsius a Kelvin, se usaría la fórmula: K = C + 273.15.
# Por ejemplo: si se ingresa 0°C, el resultado en Kelvin sería 273.15K.