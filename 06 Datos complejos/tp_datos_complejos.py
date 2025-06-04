#1)

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}

precios_frutas['Naranja'] = 1200      #se añade Naranja = 1200
precios_frutas['Manzana'] = 1500      #se añade Manzana = 1500
precios_frutas['Pera'] = 2300         #se añade Pera = 2300

print(precios_frutas)

#2) 

precios_frutas['Banana'] = 1330 # Se actualiza valor  Banana = 1330
precios_frutas['Manzana'] = 1700 # Se actualiza valor  Manzana = 1700
precios_frutas['Melón'] = 2800 # Se actualiza valor  Melón = 2800

print(precios_frutas)

#3)

lista_frutas=list(precios_frutas.keys())

print(lista_frutas)

#4)

contactos={}

nombre=0
telefono=0

#Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.

for i in range(0,5):
    nombre=(input("Ingrese nombre del contacto:"))
    telefono=(input("Ingrese número de telefono:"))
    contactos[nombre]=telefono


print( contactos)
#Luego, pedí un nombre y mostrale el número asociado, si existe.
buscar_nombre=input("Ingrese contacto para buscar nombre:")

if buscar_nombre in contactos:
    print(f"El número de {buscar_nombre} es {contactos[buscar_nombre]}")
else:
    print("Ese contacto no existe.")