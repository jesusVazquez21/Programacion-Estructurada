#Un modulo es simplemente un archivo con extension py que contiene codigo de python (funciones clases variables etc.)

#Un paquete es una carpeta que contiene varios modulos (archivos py) y un archivo especial llamado __init__.py, que le indica a python que esa carpeta debe tratarse como un paquete.

import os

#Caso Num1
def solicitarDatos1():
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    print(f"Funcion 1: El nombre es: {nombre} y su telefono es: {tel}")

#Caso Num3
def solicitarDatos2(nombre,tel):
    nombre=nombre
    tel=tel
    print(f"Funcion 3: El nombre es: {nombre} y su telefono es: {tel}")


#Caso Num2
def solicitarDatos3():
    nombre=input("Nombre: ")
    tel=input("Telefono: ")
    resp=f"Funcion 2: El nombre es: {nombre} y su telefono es: {tel}"

#Caso Num4
def solicitarDatos4(nombre,tel):
    nom=nombre
    telefono=tel
    return nom,telefono

def borrarPantalla():
    os.system("cls")

def espereTecla():
    input("... Oprima una tecla para continuar ...")

def saludar(nombre):
    nom=nombre
    return f"Hola, bienvenido: {nom}!"