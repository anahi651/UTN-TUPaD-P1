#1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario
#Función recursiva que calcule el factorial de un número
def factorial(n):
    # Caso base: si n es 0  su factorial es 1
    if n == 0:
        return 1
    # Llamada recursiva
    else:
        return n * factorial(n - 1)
    
#Pedir número al usuario
ultimo_factorial=int(input("Ingrese un número entero positivo:"))

# calcular  factorial de todos los números enteros entre 1 y el número que indique el usuario
#Recorre los números desde 1 hasta el número ingresado (inclusive).
for i in range(1, ultimo_factorial + 1): 
#Llama a la función factorial(i) para calcular el factorial de ese número.
    print(f"{i}! = {factorial(i)}")           

#2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci_recursivo(posicion):
#Cuando la posición es 0 o 1, se devuelve ese mismo número.Primeros dos términos de la secuencia.
    if posicion==0:
        return 0
    elif posicion ==1:
        return 1
    else:
#Llamada recursiva.Para cualquier posición ≥ 2, se calcula
        return fibonacci_recursivo(posicion-1)+ fibonacci_recursivo(posicion-2)

#Muestra la serie completa hasta la posición que el usuario especifique. 
#Solicitar posicion

Ultima_posicion=int(input("Ingrese un número entero positivo:"))

for i in range (Ultima_posicion):
    print(f"En la posicion {i} obtenemos el valor de fibonacci:{fibonacci_recursivo(i)}")


#3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1)
#. Prueba esta función en un algoritmo general.

#Funcion recursiva que calcula la potencia parametros base y el expnente

def potencia_recursiva(base, exponente):
#si el exponente es 1 el resultado es 0, esta es la condicion base de la funcion 
    if exponente==0:
        return 1
#Si el exponente no es 0 devolvemos la recursion la funcion se llama a sí misma con el exponente reducido en 1y multiplica la base por ese resultado
    else:
        return base * potencia_recursiva(base, exponente-1)
    
#. Prueba esta función en un algoritmo general. 
# Solicitar los valores al usuario
base = int(input("Ingresá la base (número entero): "))
exponente = int(input("Ingresá el exponente (entero positivo): "))

if exponente<0:
    print("Solo se permite el ingreso de exponente positivo.")
else:
    resultado=potencia_recursiva(base,exponente)
    print(f"{base}^{exponente}= {resultado}")