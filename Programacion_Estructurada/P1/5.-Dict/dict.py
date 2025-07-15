'''
Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de tener como las listas indices numericos tiene alfanumericos. Es decir algo parecido como los Objetos

Tambien se conoce como un arreglo asosiativo y Objetivo JSON

El diccionario es una coleccion ordenada y modificable. 
No hay miembros duplicados
'''

import os 
os.system("cls")

#LISTA
#paises=["Mexico","Brasil","Canada","España"]

#Dict u Objeto
'''
pais_mexico={"nombre":"Mexico", 
       "Capital":"CDMX",
       "Poblacion":10000000,
       "Idioma":"Español",
       "Status":True
       }

pais_Brasil={"nombre":"Brasil", 
       "Capital":"Brasilia",
       "Poblacion":100000000,
       "Idioma":"Portugues",
       "Status":True
       }

pais_canada={"nombre":"Canada", 
       "Capital":"Ottawa",
       "Poblacion":100000,
       "Idioma":{"Ingles","Frances"},
       "Status":False
        }
        '''
#Objeto 2
alumno1={
    "nombre":"Daniel",
    "apellido1":"Hernandez",
    "apellido2":"Gonzalez",
    "carrera":"TI",
    "area":"Softare Multiplataforma",
    "modalidad":"Bilingue",
    "matricula":"123456",
    "semestre":"2"
}

#Mostrar el contenido del dict
print(alumno1)

for i in alumno1:
    print(f"{i} = {alumno1[i]}")

print("")
#Agregar un campo o atributo
alumno1["telefono"]="618128371"
for i in alumno1:
    print(f"{i} = {alumno1[i]}")