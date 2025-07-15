'''
Sets.- Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

Set es una coleccion desordenada, inmutable y no indexada.
No hay miembros duplicados
'''
import os
os.system("cls")

personas={"Ramiro","Choche","Lupe"}
print(personas)
personas.add("Choche")
print(personas)

'''personas.pop()
print(personas)
personas.clear()
print(personas)
'''
varios=(3.12,3,True,"Hola")
print(varios)


#Ejemplo Crear un programa que solicite los emails de los alumnos de la UTD, almacenar en una lista y posteriormente mostrar en pantalla los emails sin duplicados 

os.system("cls")
opc="SI"
emails=[]
while opc=="SI":
    emails.append(input("Dame el Email: "))
    #print(emails)
    opc=input("¿Deseas solicitar otro email? SI/NO ").upper()

#Imprimir emails sin dupicados 
print(emails)
set1=set(emails)
print(set1)
emails=list(set1)
print(emails)