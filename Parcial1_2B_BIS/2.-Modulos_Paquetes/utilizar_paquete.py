from paquete1 import modulos

print(modulos.saludar("Jesus Vazquez Hernandez"))

modulos.borrarPantalla()
nom,tel=modulos.solicitarDatos2()
print(f"\n..:Agenda Telefonica:..\n\t\tNombre: {nom}\n\t\t Telefono: {tel}")
modulos.espereTecla()