#Un modulo es simplemente un archivo con extenion .py que contiene codigo de python ( Funciones, clases, variables, etc)
#un paquete es una carpeya que contiene varios modulos (archivos .py) y un archivo especial llamado __init__.py que le indica a python que esa carptea debe tratarse como un paquete
# 1-Funcion que no recibe parametros y no regrsa valor
import os
def solicitarDatos1():
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    print(f"Soy funcion 1: El nombre es: {nombre} y su numero telefonico es: {tel}")
    
#3-Funcion que no recibe parametros y regresa valor
def solicitarDatos3(nombre, tel):
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    print(f"Soy funcion 3: El nombre es: {nombre} y su numero telefonico es: {tel}")

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

#5.-Borrar pantalla
def borrarPantalla():
    os.system("cls")

#6.-Esperar tecla  
def esperarTecla():
    input("...:Oprima una tecla para continuar:...")
    
#7 Saludo  
def saludar(nombre):
    nom=nombre
    return f"Hola, bienvenido: {nom}"

