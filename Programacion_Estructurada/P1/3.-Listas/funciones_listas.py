'''
List (array)
Son colecciones o conjunto de datos/valores bajo un mismo nombre para acceder a los valpres se hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable.
Permite miembros duplicados

'''
import os

os.system("cls")
#Funciones mas comuen en las listas

paises=["México", "Brasil", "España", "Canadá"]

numeros=[23, 12, 100, 34]

#--Ordenar Ascendentemente--

#Ordenar Numeros
print(numeros)
numeros.sort()
print(numeros)

#Ordenar Paises
print(paises)
paises.sort()
print(paises)

#--Añadir o Ingresar elementos a una lista

#Primer forma 
print(paises)
paises.append("Honduras")

#Segunda Forma
paises.insert(1,"Honduras")
print(paises)


#--Eliminar/Borrar/Quitar elementos

#1era Forma con el Indice
paises.pop(1)
print(paises)

#2da Forma con el valor 
paises.remove("Honduras")
print(paises)

#--Buscar un elemento dentro de una lista--

#1er forma
resp="Brasil" in paises
if resp:
    print("Si encontré el país")
else:
    print("No encontré el país")
    
#2da forma
'''
pais_buscar=input("Dame el país a buscar: ")
for i in range(0, len(paises)):
    if paises[i]==pais_buscar:
        print("Si encontré el país")
    else:
        print("No encontré el país")
        '''
#--Cuantas veces aparece un elemento dentro de una lista--

print(f"Este numero 12 aparece: {numeros.count(12)} vez o veces")

numeros.append(12)
print(f"Este numero 12 aparece: {numeros.count(12)} vez o veces")

#--Identificar el indice de un valor--
indice=paises.index("España")
print(indice)
paises.pop(indice)
print(paises)

#--Recorrer los valores de una lista--

#1era forma con los valores
for i in paises:
    print(i)
    
#2da forma con los indices 
for i in range(0, len(paises)):
    print(f"El valor {i} es: {paises[i]}")    
    
#Unir contenido de listas
print(paises)
print(numeros)
paises.extend(numeros)
print(paises) 
