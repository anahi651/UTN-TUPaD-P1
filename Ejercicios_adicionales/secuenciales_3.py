# Ejercicio 3: Uso de booleanos
# Objetivo: Manipular variables booleanas y aplicar operadores lógicos.

# 1. Declarar dos variables booleanas
a = True
b = False

# 2. Realizar e imprimir los resultados de las operaciones
# a and b
resultado_and = a and b
print(f"a and b = {resultado_and}")  

# a or b
resultado_or = a or b
print(f"a or b = {resultado_or}")   

# not a, not b
resultado_not_a = not a
resultado_not_b = not b
print(f"not a = {resultado_not_a}")  
print(f"not b = {resultado_not_b}") 

# Preguntas de reflexión:

# ¿Cuál es la utilidad de los operadores lógicos en programas más complejos?
# Los operadores lógicos permiten tomar decisiones dentro del código. Se usan para evaluar condiciones en estructuras como if, while o funciones,
# lo que permite controlar el flujo del programa según si ciertas condiciones son verdaderas o falsas.

# ¿Qué representa cada operación?
# - a and b: solo será True si ambas variables son True.
# - a or b: será True si al menos una de las variables es True.
# - not a / not b: invierte el valor booleano (True pasa a False y viceversa).