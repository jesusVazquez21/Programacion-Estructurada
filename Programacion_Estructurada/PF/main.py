import clientes.clientes
import inventario
import clientes
import inventario.inventario
import proveedores
import proveedores.proveedores
import reportes

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\nPresiona ENTER para continuar...")

opcion = True
while opcion:
    borrarPantalla()
    print("\n\t\t\t..::: 🍔 CHIVATAS BURGUER :::...\n\t\t..::: Sistema Administrativo :::...\n")
    print("\t\t 1.- Inventario 📦")
    print("\t\t 2.- Clientes 👥")
    print("\t\t 3.- Proveedores 🚚")
    print("\t\t 4.- Reportes 📊")
    print("\t\t 5.- Salir 🚪")
    
    entrada = input("\n\t\tElige una opción: ").upper()

    match entrada:
        case "1":
            inventario.inventario.menu_inventario()
            esperarTecla()
        case "2":
            clientes.clientes.menu_clientes()
            esperarTecla()
        case "3":
            proveedores.proveedores.menu_proveedores()
            esperarTecla()
        case "4":
            reportes.menu_reportes()
            esperarTecla()
        case "5":
            opcion = False
            borrarPantalla()
            print("\n\t👋 Terminaste la ejecución del sistema. ¡Hasta pronto!")
        case _:
            input("\n❌ Opción inválida, vuelve a intentarlo...")









'''
def borrarPantalla():
    import os
    os.system("cls")

def mostrar_menu():
    borrarPantalla()
    print("\n🍔=== SISTEMA ADMINISTRATIVO: CHIVATAS BURGUER ===🍟")
    print("1️⃣  📦 Gestión de Inventario")
    print("2️⃣  👥 Gestión de Clientes")
    print("3️⃣  🚚 Gestión de Proveedores")
    print("4️⃣  📊 Reportes")
    print("5️⃣  ❌ Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == '1':
            try:
                import inventario
                inventario.menu_inventario()
            except ModuleNotFoundError:
                print("⚠️  Módulo de inventario no disponible aún.")
        elif opcion == '2':
            try:
                import clientes
                clientes.menu_clientes()
            except ModuleNotFoundError:
                print("⚠️  Módulo de clientes no disponible aún.")
        elif opcion == '3':
            try:
                import proveedores
                proveedores.menu_proveedores()
            except ModuleNotFoundError:
                print("⚠️  Módulo de proveedores no disponible aún.")
        elif opcion == '4':
            try:
                import reportes
                reportes.menu_reportes()
            except ModuleNotFoundError:
                print("⚠️  Módulo de reportes no disponible aún.")
        elif opcion == '5':
            print("👋 Saliendo del sistema... ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()

'''