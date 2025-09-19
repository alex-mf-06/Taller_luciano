import os

def menu_gastos():
    """
    Muestra el menú principal del módulo de gastos.
    """
    while True:
        print("\n=== Módulo de Gastos ===")
        print("1. Registrar un gasto")
        print("2. Buscar un gasto")
        print("3. Listar gastos")
        print("0. Volver al menú principal")
        
        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                registrar_gasto()
            elif opcion == 2:
                buscar_gasto()
            elif opcion == 3:
                listar_gasto()
            elif opcion == 0:
                break
            else:
                print("❌ Opción inválida. Por favor, ingrese un número del 0 al 3.")
        
        except ValueError:
            print("❌ Entrada inválida. Por favor, ingrese un número.")

# ---------------------------------------------
# Funciones principales (pendientes de implementar)
# ---------------------------------------------

def registrar_gasto():
    """
    Registra un nuevo gasto en el sistema.

    Pre-condición:
        - El usuario proporciona la información necesaria para el nuevo gasto (ej. descripción, monto, tipo).

    Post-condición:
        - Se crea un nuevo registro de gasto con un ID único.
        - El registro se guarda en el archivo de datos.
    """
    while True:
        try:
            print("\n--- Registrar Gasto ---")
            descripcion = input("Ingrese la descripción del gasto (o '0' para cancelar): ")
            
            if descripcion == '0':
                print("Registro de gasto cancelado.")
                break
            
            # Lógica para solicitar el monto, tipo, etc. (pendiente de implementar)
            
            print("Lógica para crear y guardar el registro (pendiente de implementar)")
            break
            
        except ValueError:
            print("Entrada inválida. Intente de nuevo.")
            continue

def buscar_gasto():
    """
    Busca uno o varios gastos por un criterio de búsqueda.

    Pre-condición:
        - Se necesita un criterio de búsqueda (ej. ID de gasto, tipo de gasto, rango de fecha).

    Post-condición:
        - Si se encuentra, muestra los detalles del gasto o gastos.
        - Si no se encuentra, notifica al usuario.
    """
    while True:
        print("\n--- Buscar Gasto ---")
        print("1. Buscar por ID de gasto")
        print("2. Buscar por tipo de gasto")
        print("0. Volver al menú anterior")

        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                gasto_id = input("Ingrese el ID del gasto: ")
                print(f"Buscando gasto con ID {gasto_id} (pendiente de implementar)")
                break
            elif opcion == 2:
                tipo_gasto = input("Ingrese el tipo de gasto (ej. repuestos, servicios): ")
                print(f"Buscando gastos de tipo '{tipo_gasto}' (pendiente de implementar)")
                break
            elif opcion == 0:
                break
            else:
                print("Opción inválida. Por favor, ingrese un número del 0 al 2.")

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue

def listar_gasto():
    """
    Muestra un listado de todos los gastos o un subconjunto filtrado.

    Pre-condición:
        - El archivo 'gastos.json' debe existir y ser legible.

    Post-condición:
        - Se muestra una lista clara y formateada de los gastos existentes.
    """
    print("\n--- Listado de Gastos ---")
    print("Lógica para cargar y mostrar los gastos (pendiente de implementar)")
