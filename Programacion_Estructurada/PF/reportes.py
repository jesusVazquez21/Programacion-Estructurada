import inventario
import clientes
import proveedores

def borrarPantalla():
    import os
    os.system("cls")

def mostrar_menu_reportes():
    borrarPantalla()
    print("\n📊=== REPORTES DEL SISTEMA ===")
    print("1️⃣  📦 Reporte de Inventario")
    print("2️⃣  👥 Reporte de Clientes")
    print("3️⃣  🚚 Reporte de Proveedores")
    print("4️⃣  🧾 Reporte general del negocio")
    print("5️⃣  🔙 Volver al menú principal")

def reporte_inventario():
    print("\n📦 Reporte de Inventario:")
    if not inventario.inventario:
        print("📭 Inventario vacío.")
    else:
        for i, p in enumerate(inventario.inventario, 1):
            print(f"{i}. {p['nombre']} - {p['cantidad']} {p['unidad']}")

def reporte_clientes():
    print("\n👥 Reporte de Clientes:")
    if not clientes.clientes:
        print("📭 No hay clientes registrados.")
    else:
        for i, c in enumerate(clientes.clientes, 1):
            print(f"{i}. {c['nombre']} | Tel: {c['telefono']}")

def reporte_proveedores():
    print("\n🚚 Reporte de Proveedores:")
    if not proveedores.proveedores:
        print("📭 No hay proveedores registrados.")
    else:
        for i, p in enumerate(proveedores.proveedores, 1):
            print(f"{i}. {p['nombre']} | Productos: {p['productos']}")

def reporte_general():
    print("\n🧾 Reporte General del Negocio:")
    print(f"📦 Total de productos en inventario: {len(inventario.inventario)}")
    print(f"👥 Total de clientes registrados: {len(clientes.clientes)}")
    print(f"🚚 Total de proveedores registrados: {len(proveedores.proveedores)}")

def menu_reportes():
    while True:
        mostrar_menu_reportes()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == '1':
            reporte_inventario()
        elif opcion == '2':
            reporte_clientes()
        elif opcion == '3':
            reporte_proveedores()
        elif opcion == '4':
            reporte_general()
        elif opcion == '5':
            print("🔙 Volviendo al menú principal...")
            break
        else:
            print("❌ Opción no válida. Intenta nuevamente.")
