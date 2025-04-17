#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo (): #Se define la función  
    print("Hola Mundo!")  #Imprime texto solicitado 

# Programa principal

imprimir_hola_mundo()       # se llama a la funcion desde el programa principal

#2.Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de￾volver: “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

def saludar_usuario(nombre):                  #Se define la función con un argumento nombre
     print(f"Hola {nombre}!")                 # saludo personalizado utilizando el argumento


# Programa principal
nombre_usuario = input("¿Cuál es tu nombre? ")  # Solicita el nombre al usuario
saludar_usuario(nombre_usuario)                 # Llama a la función con ese nombre



#3. Crear una función llamada informacion_personal(nombre, apellido,edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pe￾dir los datos al usuario y llamar a esta función con los valores in￾gresados.


def informacion_personal(nombre, apellido,edad, residencia):
     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Programa principal
nombre_usuario = input("¿Cuál es tu nombre? ")  # Solicita el nombre al usuario
apellido_usuario=input("¿Cuál es tu apellido? ")# Solicita el apellido al usuario
edad_usuario=int(input("¿Cuántos años tenes? "))    #Solicita edad al usuario se guarda como int en caso de necesitar hacer algun calculo más adelante
residencia_usuario= input("¿Dónde vivis?")     #Solicita residencia al usuario
informacion_personal(nombre_usuario,apellido_usuario,edad_usuario,residencia_usuario)

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
#calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo.
#Solicitar el radio al usuario y llamar am￾bas funciones para mostrar los resultados.


# Al principio del programa necesitamos importar la librería math ya que la necesitaremos para utilizar el número pi
import math

def calcular_area_circulo(radio): # funcion calcular_area_circulo(radio) que reciba el radio como parámetro
     return math.pi * (radio **2)    #retorna area 

def calcular_perimetro_circulo(radio): #funcion calcular_perimetro_circulo(radio) que reciba el radio como parámetro
     return 2 * math.pi * radio           #retorna perimetro


#Programa principal
radio=float(input("Ingrese radio: ")) # solicita radio  al usuario 
print(f"El área del circulo es de: {calcular_area_circulo(radio)}")  #imprime area 
print(f"El perímetro  del circulo es de: {calcular_perimetro_circulo(radio)}") #imprime perimetro



#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mos￾trar el resultado usando esta función.

def segundos_a_horas(segundos):              #Función segundos_a_horas(segundos) parametro segundos
     return segundos / 3600                  #retorna la conversión de segundos a horas, sabiendo que una hora equivale a 3600 segundos


#Programa principal
cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: ")) # se solicita la cantidad de segundos al usuario

horas= segundos_a_horas(cantidad_segundos)                 
print(f"Equivale a {horas:.2f} ")                          # se imprime el resultado con la funcion se agrega 2f para poner solo dos decimales



#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la fun￾ción.


def tabla_multiplicar(numero):       #funcion
    for x in range(1, 11):                    #bucle del 1 al 10
        print(f"{numero} x {x} = {numero * x}")

# Programa principal
numero_multiplicar = int(input("Ingrese número para ver la tabla de multiplicar: ")) # se solicita numero para imprimir tabla 
print(f"\nLa tabla de multiplicar del {numero_multiplicar} es:")
tabla_multiplicar(numero_multiplicar)


#7.Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):  # funcion operaciones_basicas 
    suma = a + b               
    resta = a - b
    multiplicacion = a * b
    if b != 0:                    #restriccion division por 0
        division = a / b
    else:
        division = "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)    #retorna los resultados de las operaciones

# Programa principal
a = int(input("Ingrese un número: "))                #se solicita numero a y b al usuario
b = int(input("Ingrese otro número: "))

suma, resta, multiplicacion, division = operaciones_basicas(a, b)       #desempaqueta la tupla que devuelve la función operaciones_basicas(a, b) en cuatro variables separadas.

print(f"Resultados con {a} y {b}:")                                      
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    return round(peso / altura**2, 2)    #retorna IMC con dos decimales


peso_usuario=float(input("Ingrese su peso en Kilogramos:"))
altura_usuario=float(input("Ingrese su altura en metros:"))
imc= calcular_imc(peso_usuario, altura_usuario)
print(f"Su IMC es de :{imc}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
#  Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    temperatura_fahrenheit = round((9/5)*celsius+32, 2)
    return temperatura_fahrenheit

temperatura_celsius = float(input("Por favor, una temperatura en °C: ")) #pide al usuario que ingrese la temperatura  Celsius y almacenando su valor en la variable temperatura_celsius
Fahrenheit=celsius_a_fahrenheit(temperatura_celsius)
# Imprimimos por pantalla el resultado
print(f"{temperatura_celsius} °C equivalen a {Fahrenheit} °F.")

#10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio=(a+b+c)/3
    return promedio


a=int(input("Ingrese número:"))
b=int(input("Ingrese número :"))
c=int(input("Ingrese número :"))

promedio=calcular_promedio(a, b, c)
print(f"El promedio de {a},{b},{c} es de: {promedio}")