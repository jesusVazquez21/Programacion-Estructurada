# 1er utilizar los modulos
import modulos

print(modulos.saludar("Jesus Vazquez"))

# 2da forma de utilizar modulos

from modulos import saludar,borrarPantalla

borrarPantalla()
print(saludar("Daniel Contreras Renecio"))

nombre=input("Ingresa el nombre del contacto: ")
telefono=input("Ingresa su numero de telefono: ")
nom,tel=modulos.solicitarDatos4(nombre,telefono)
print(f"\t Nombre completo: {nom} \n\tTelefono: {tel}")
