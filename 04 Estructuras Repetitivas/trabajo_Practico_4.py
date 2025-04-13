#1.Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for x in range(101): # comenzando desde 0 por defecto, y se incrementa de 1 (por defecto), y finaliza en un número indicado sin incluir .
    print(x)

#2. Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero=int(input("Ingrese un número entero: "))#Se solicita un núemero entero al usuario



# Si el número es 0, tiene 1 dígito
if numero == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0
    while numero > 0:
        numero = numero // 10  # División entera, elimina el último dígito
        cantidad_digitos += 1  # Contamos ese dígito

print("El número tiene", cantidad_digitos, "dígitos.")
  
#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores
numero= int(input("Ingrese un número :"))
numero_dos= int(input("Ingrese un segundo número :"))
suma=0
if numero > numero_dos:
    temp = numero           # guarda el mayor
    numero = numero_dos     # poguarda  el menor en numero
    numero_dos = temp       # y guarda el mayor en numero_dos
for x in range (numero+1 , numero_dos):
    suma +=x #suma=suma +x
print("La suma de los números entre", numero, "y", numero_dos, "es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
CORTE=0    #constante corte como valor 0

numero= int(input("Ingrese un número entero: "))
suma=0 #inicializa la suma 
while numero != CORTE: #si es distinto a 0 entra en el bucle 
    suma+=numero #= suma cada número ingresado 
    numero= int(input("Ingrese otro número entero:"))
    
print("El total acumulado es de:", suma)#si se ingreso 0 sale del bucle y muestra el acumulado


print("//////////////////////////////////////////")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

from random import *#Importa todas las funciones del módulo 'random' permite generar numeros aleatorios 
numero_aleatorio=randint(0, 9)
suma=0 #inicializa suma para contar intentos 
numero_ingresado= int(input("Adivine el número, es entre el 0 y el 9: "))#Pide al usuario que ingrese un número y lo convierte en entero. Este es el primer intento

while numero_ingresado!= numero_aleatorio:   # Mientras el número ingresado sea distinto del número aleatorio, repite el bucle
    suma=suma+1                                # Suma 1 a la variable 'suma' por cada intento incorrecto
    numero_ingresado = int(input("Adivine de nuevo: "))     # Pide al usuario otro número en cada vuelta del bucle

print("¡Correcto!")#sale del bucle si adivino 
print("La cantidad de intentos necesarios para adivinar el número fue:", suma + 1)#suma 1 para incluir el primer intento

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for x in range(100,-1,-2):# inicia en 100,hasta -1 sin incluir (0) y va de dos en dos en forma decreciente para tomar los pares
    print(x)