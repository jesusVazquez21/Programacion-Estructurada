'''
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutilizar con el simple hecho de invocarla es decir mandarla a llamar
Sintaxis:
def nombreMifuncion(parametros):
bloque de conjunto de instrucciones

nombremifuncion(parametros)

---Las funciones pueden ser de 4 tipos---
    -Funciones de tipo "Procedimiento"-
        1-Funcion que no recibe parametros y no regrsa valor
        3-Funcion que no recibe parametros y regresa valor
    -Funciones de tipo "Funcion"-
        2-Funcion que recibe parametros y no regresa valor
        4-Funcion que recibe parametros y regresa valor 
'''

# 1-Funcion que no recibe parametros y no regrsa valor
def solicitarDatos1():
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    print(f"Soy funcion 1: El nombre es: {nombre} y su numero telefonico es: {tel}")
    
#3-Funcion que no recibe parametros y regresa valor
def solicitarDatos3(nombre, tel):
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    print(f"Soy funcion 3: El nombre es: {nombre} y su numero telefonico es: {tel}")
    
nombre=input("Nombre; ")
tel=input("Telefono: ")

#2-Funcion que recibe parametros y no regresa valor
def solicitarDatos2():
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    return f"Soy funcion 2: El nombre es: {nombre} y su numero telefonico es: {tel}"

#4-Funcion que recibe parametros y regresa valor
def solicitarDatos4(nombre, tel):
    nom=input("Nombre: ")
    telefono=input("Telefono: ")
    return nom, telefono

#Llamar mis funciones
solicitarDatos1()
nom3=input("Nombre: ")
tel3=input("Telefono: ")
solicitarDatos3(nom3, tel3)
nom2, tel2=solicitarDatos2()
print(f"Nombre: {nom2} \n Telefono: {tel2}")
nom4=input("Nombre: ")
tel4=input("Telefono: ")
solicitarDatos4(nom4, tel4)
nom4, tel4=solicitarDatos4(nom4, tel4)
print(f"\tNombre: {nom4} \n Telefono: {tel4}")