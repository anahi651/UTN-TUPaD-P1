 #Ejercicio 4: Tabla de multiplicar del 7
 #Objetivo: Usar un bucle para generar patrones.
 #Instrucciones:
#1. Imprime la tabla de multiplicar del 7 (desde 7x1=7 hasta 7x10=70).
# Preguntas de reflexión:


contador=0

for i in range(1,11,1):
  
    multiplicacion=7*i
    print(f"7 x {i}={multiplicacion}")
#• ¿Cómo adaptarías el código para que el usuario elija la tabla?

numero=int(input("Ingrese un núemero para ver su tabla de multiplicar:"))

contador=0

for i in range(1,11,1):
  
    multiplicacion=numero*i
    print(f"{numero} x {i}={multiplicacion}")

#• ¿Qué estructura usarías para almacenar los resultados?
resultado=[]

numero=int(input("Ingrese un núemero para ver su tabla de multiplicar:"))

contador=0
resultado=[]
for i in range(1,11,1):
  
    multiplicacion=numero*i
    resultado.append(f"{numero} x {i}={multiplicacion}")
    print(f"{numero} x {i}={multiplicacion}")

print(resultado)