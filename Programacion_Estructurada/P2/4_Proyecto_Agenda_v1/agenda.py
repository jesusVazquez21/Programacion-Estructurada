def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  print("\n\t\U0001F501 ...Oprima cualquier tecla para continuar... \U0001F501")
  input()  
  
def menuMain():
    print("\n\t\t \U0001F4DD ..::: Sistema de Gestión de Agenda de Contactos :::... \U0001F4DD \n")
    print("\t\t \u0031\uFE0F\u20E3  Agregar Contacto \U0001F4DD\n\t\t \u0032\uFE0F\u20E3  Mostrar Todos los contactos \U0001F4BE\n\t\t \u0033\uFE0F\u20E3  Buscar contacto por nombre \U0001F50D \n\t\t \u0034\uFE0F\u20E3  Modificar contacto \U0001F50D \n\t\t \u0035\uFE0F\u20E3  Elminar contacto \U0001F50D \n\t\t \u0036\uFE0F\u20E3  SALIR \U0001F6AA")
    opcion=input("\n\t\tElige una opción (1-4): ").upper()
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("..::  \U0001F4BE Agregar Contacto Nuevo \U0001F4BE ::..")
    nombre=input(" \U0001F464 Nombre del Contacto: ").upper().strip()
    if nombre in agenda:
        print("\n\t\tEl contacto ya existe")
    else:
        tel=input("Telefono: ").strip()
        email=input("Email: ").lower().strip()      
        # Agregar el atributo "nombre" al diccionario con los 
        # valores de telefono y email en una lista
        agenda[nombre]=[tel, email]
        print("\n\t\t ..::El Contacto se agrego correctamente::..")
        
def mostrar_contactos(agenda):
    borrarPantalla()
    print("\n\t\t ..:: Mostrar Contactos::..")
    if not agenda:
        print("\n\t\t No existen contactos")
    else:
        for i in agenda:
            print(f"{i} : {agenda[i]}")
        # for nombre, datos in agenda.items():
        #     print(f"\n\t{'Nombre'+nombre}\n\t\t{'Telefono: '+datos}")

def buscar_contacto(agenda):
    borrarPantalla()
    print("\U0001F50E  .:: Buscar Contacto ::. \n")
    nombre = input("Ingresa el nombre del contacto a buscar: ").upper().strip()

    if nombre in agenda:
        print(f"\n✅ Contacto encontrado: {nombre}")
        print(f"📞 Teléfono: {agenda[nombre][0]}")
        print(f"📧 Correo: {agenda[nombre][1]}")
    else:
        print("\n\t\u274C No se encontró el contacto.")
               
def borrar_contacto(agenda):
    borrarPantalla()
    print("\U0001F5D1  .:: Borrar Contacto ::. \n")
    
    if len(agenda) == 0:
        print("\n\t\u274C No hay contactos registrados.")
    else:
        nombre = input("Ingresa el nombre del contacto a borrar: ").upper().strip()
        if nombre in agenda:
            confirmar = input(f"¿Estás seguro de que deseas borrar a {nombre}? (SI/NO): ").upper().strip()
            if confirmar == "SI":
                agenda.pop(nombre)
                print(f"\n\t\u2705 Contacto {nombre} borrado exitosamente.")
            else:
                print("\n\t\u274C Operación cancelada.")
        else:
            print("\n\t\u274C Ese contacto no existe.")
            
def modificar_contacto(agenda):
    borrarPantalla()
    print("\U0001F501  .:: Modificar Contacto ::. \n")
    
    if len(agenda) == 0:
        print("\n\t\u274C No hay contactos registrados.")
    else:
        nombre = input("Ingresa el nombre del contacto que deseas modificar: ").upper().strip()
        if nombre in agenda:
            campos = ["📞 Teléfono", "📧 Correo"]
            for i in range(len(agenda[nombre])):
                actual = agenda[nombre][i]
                nuevo = input(f"{campos[i]} actual: {actual}\nNuevo {campos[i]} (Enter para dejar igual): ").strip()
                if nuevo != "":
                    agenda[nombre][i] = nuevo
            print("\n\t\u2705 Contacto actualizado correctamente.")
        else:
            print("\n\t\u274C Ese contacto no existe.")

        