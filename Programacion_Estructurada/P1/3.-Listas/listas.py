import os 
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
'''
numeros=[23,45,56,78]
print(numeros)

for i in numeros:
    print(i)
    
for i in range(0, len(numeros)):
    print(numeros[i])
'''
#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra
'''
os.system("cls")
palabras=["Obtuso","Modular","Telefono","Dibujar"]


resp="Modular" in palabras
if resp:
    print("La palabra se encontró")
else:
    print("La palabra no se encontró")
    

palabra_buscar=input("Escriba la palabra a buscar: ")
print(f"El numero de veces que se encontro la palabra es: {palabras.count(palabra_buscar)}")
if palabra_buscar in palabras:
    print(f"Si encontró la palabra")
else:
    print(f"No se encontró la palabra")

palabra_buscar=input("Escriba la palabra a buscar: ")
encontro=False
for i in range(0, len(palabras)):
    if palabras[i]==palabra_buscar:
        encontro=True
        
if encontro:        
    print("Si se encontró la palabra")
else:
    print("No se encontró la palabra")
        
input("Oprima tecla")

'''

#3.-Añadir elementos a una lista

'''
os.system("cls")
numeros=[]
print(numeros)

opc=True
while opc:
    numero=float(input("Dame un numero entero o decimal"))
    numeros.append(numero)
    res=input=("¿Deseas volver a agregar otro elemento? ").lower()
    if res=="si": 
         opc=True
    else:
        opc=False
print(numeros)

'''
#Ejemplo 4 Crear una lista multidimensional que sea una agenda 
agenda=[
    ["Carlos","214692412"],
    ["Alberto","48917419"],
    ["Martin","482913892"],
]

print(agenda)

for i in agenda:
    print(i)

for i in range(0,3):
    for j in range(0,2):
        print(agenda[i][j])
    print()
    
cadena=""
for i in range(0,3):
    for j in range(0,2):
        cadena+=f"{agenda[i][j]}, "
    cadena+="\n"
print(cadena)