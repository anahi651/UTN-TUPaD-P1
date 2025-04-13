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