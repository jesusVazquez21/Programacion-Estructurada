'''
Crear un programa que calcule e imprima cualquier tabla de mmultiplicar
'''

#VERSION 1
numero=int(input("Dame el numero de la tabla de multiplicar que quieras calcular: "))
multi=numero*1
print(f"{numero} x 1 = {multi}")
multi=numero*2
print(f"{numero} x 2 = {multi}")
multi=numero*3
print(f"{numero} x 3 = {multi}")
multi=numero*4
print(f"{numero} x 4 = {multi}")
multi=numero*5
print(f"{numero} x 5 = {multi}")
multi=numero*6
print(f"{numero} x 6 = {multi}")
multi=numero*7
print(f"{numero} x 7 = {multi}")
multi=numero*8
print(f"{numero} x 8 = {multi}")
multi=numero*9
print(f"{numero} x 9 = {multi}")
multi=numero*10
print(f"{numero} x 10 = {multi}")

#VERSION 2
numero=int(input("Dame el numero de la tabla de multiplicar que quieras calcular: "))
for i in range ("1, 11"):
    multi=numero*i
    print(f"numero x {i} = {multi}")
    
numero=int(input("Dame el numero de la tabla de multiplicar que quieras calcular: "))
while i<10:
    multi=numero*i
    print(f"{numero} x {i} = {multi}")
    i+=1
       
#VERSION 3
'''
Crear un programa que calcule e imprima cualquier tabla de multiplicar con funciones que regresa valor y utilize parametros
'''
def tablaMultiplicar():
    numero=int(input=("Dame el numero de la tabla de multiplicar que quieras calcular: "))
    while i<10:
        multi=numero*i
        i+=1
    return i, multi

numero, i, multi=tablaMultiplicar()
print(f"{numero} x {i} = {multi}")  
def tabla(num):
    number=num
    respuesta=""
    for i in range (1, 11):
        multi=num*i
        respuesta=f"\t{num} x {i} = {multi}\n"
    return respuesta

num=int(input("Dame el numero de la tabla que queiras calcular"))
print("Tabla de multiplicar")
resultado=tabla(numero)
print(f"{resultado}")      
