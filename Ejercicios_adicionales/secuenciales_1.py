#Ejercicio 1: Cálculo del área y el perímetro de un rectángulo
#Objetivo: Calcular el área y el perímetro a partir de medidas dadas por el usuario.
#1. Pedir al usuario que ingrese el ancho y el alto de un rectángulo.

ancho_del_rectangulo=int(input("Ingrese ancho del rectangulo:"))
alto_del_rectangulo=int(input("Ingrese alto del rectangulo:"))

#2. Calcular el área usando la fórmula: ancho * alto.
area=ancho_del_rectangulo*alto_del_rectangulo

#3. Calcular el perímetro con la fórmula: (ancho * 2) + (alto * 2).

perimetro=(ancho_del_rectangulo*2+alto_del_rectangulo*2)

#4. Mostrar ambos resultados en pantalla.

print(f"El area es de : {area}")
print(f"El perimetro es de :{perimetro}")

#¿Qué sucede si se ingresan valores negativos?
#Si el usuario ingresa valores negativos para el ancho o el alto, el programa realiza las operaciones de todas formas,
#  pero los resultados no tienen sentido físico, ya que las dimensiones de un rectángulo no pueden ser negativas. 
# Por eso, sería recomendable incluir una validación que impida ingresar números menores que cero y que informe al usuario del error.

#¿Podría adaptarse este cálculo a otras figuras geométricas?
#Sí, el cálculo puede adaptarse a otras figuras geométricas modificando las fórmulas según las características de cada una. 
# Por ejemplo, para un triángulo se puede calcular el área con la fórmula (base × altura) ÷ 2,
#  y para un círculo se usaría π × radio² para el área y 2 × π × radio para el perímetro. 
# Esto requeriría pedir al usuario datos diferentes y aplicar las fórmulas correspondientes a cada figura.







