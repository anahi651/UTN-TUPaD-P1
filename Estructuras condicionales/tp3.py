#1.Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

EDAD_MINIMA=18
edad= int(input("Ingrese su edad:"))

if edad>= EDAD_MINIMA:
    print("Es mayor de edad")
else:
    pass
#2.Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
NOTA_MINIMA=6
nota=int(input("Ingrese la nota: "))
if nota>=NOTA_MINIMA:
    print("APROBADO")
else:
    print("DESAPROBADO")
#3.Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
PAR=0
numero=int(input("Ingrese un número: "))
if (numero%2)==0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")
#4. Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
edad= int(input("Ingrese su edad:"))
if edad<12:
    print("Niño/a")
elif edad>=12 and edad<18:
    print("Adolescente")
elif edad>=18 and edad <30:
    print("Adulto/a joven")
elif edad>=30:
    print("Adulto/a:")
else:
    pass
#5.Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.
contasena=(input("Ingrese la contraseña:"))
longitud_contasena= len(contasena)

if longitud_contasena>=8 and longitud_contasena<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
#6.Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda=mode(numeros_aleatorios)
print(moda)
mediana=median(numeros_aleatorios)
print(mediana)
media=mean(numeros_aleatorios)
print(media)

if media>mediana and mediana>moda:
    print("Sesgo positivo o a la derecha")
elif media<mediana and mediana<moda:
    print("Sesgo negativo o a la izquierda")
elif media==mediana and mediana== moda:
    print("Sin sesgo")
else:
    print("No se puede determinar un sesgo claro")
#7.Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
frase=(input("Por favor ingrese una frase o palabra:"))
if frase.endswith(('a', 'e', 'i', 'o', 'u')):
    print(frase+"!")
else:
    print(frase)
#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre=(input("Por favor ingrese su nombre: "))
numero=int(input("Ingrese un número 1 ,2 o 3: "))
if numero == 1:
   print(nombre.upper())
elif numero==2:
    print(nombre.lower())
elif numero==3:
    print(nombre.title())
else:
    print("Ingrese un número válido")

# 9.Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# Menor que 3: "Muy leve" (imperceptible).
# Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)

magnitud=int(input("Indicar magnitud del terremoto en escala de Richter: "))

if magnitud < 3:
    print("Muy leve" )
elif magnitud >=3 and magnitud<4:
    print("Leve")
elif magnitud>=4 and magnitud<5:
    print("Moderado")
elif magnitud>=5 and magnitud<6:
    print("Fuerte")
elif magnitud>=6 and magnitud<7:
    print("Muy Fuerte")
elif magnitud>=7:
    print("Extremo")
else:
    print("El número indicado no se encuentra dentro de la escala de Richter ")

#10Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.


hemisferio = input("Ingrese N si se encuentra en el hemisferio norte o S si se encuentra en el hemisferio sur: ").lower()
mes = input("Ingrese mes: ").lower()
dia = int(input("Ingrese día: "))

if hemisferio == "n":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        print("INVIERNO")
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        print("PRIMAVERA")
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 21):
        print("VERANO")
    elif (mes == "septiembre" and dia >= 22) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        print("OTOÑO")
elif hemisferio == "s":
    if (mes == "diciembre" and dia >= 21) or mes in ["enero", "febrero"] or (mes == "marzo" and dia <= 20):
        print("VERANO")
    elif (mes == "marzo" and dia >= 21) or mes in ["abril", "mayo"] or (mes == "junio" and dia <= 20):
        print("OTOÑO")
    elif (mes == "junio" and dia >= 21) or mes in ["julio", "agosto"] or (mes == "septiembre" and dia <= 21):
        print("INVIERNO")
    elif (mes == "septiembre" and dia >= 22) or mes in ["octubre", "noviembre"] or (mes == "diciembre" and dia <= 20):
        print("PRIMAVERA")
else:
    print("Hemisferio inválido.")


