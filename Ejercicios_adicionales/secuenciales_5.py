#Ejercicio 6: Intercambio de variables
#Objetivo: Intercambiar valores sin usar una variable temporal.
# 1. Declarar dos variables
x = 10
y = 20

# 2. Mostrar valores antes del intercambio
print("Antes del intercambio:")
print("x =", x)
print("y =", y)

# 3. Intercambiar usando operaciones aritméticas
x = x + y  # x ahora vale 30
y = x - y  # y ahora vale 10 (30 - 20)
x = x - y  # x ahora vale 20 (30 - 10)

# 4. Mostrar valores después del intercambio
print("Después del intercambio:")
print("x =", x)
print("y =", y)
