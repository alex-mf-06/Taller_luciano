# compras.py
# Módulo para gestionar compras del taller

def menu_compras():
    while True:
        print("\n=== Módulo Compras ===")
        print("1. Compras de repuestos")
        print("2. Compras de materiales de pintura")
        print("3. Orden de compra automática")
        print("4. Costos totales de compras por mes")
        print("0. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            compras_repuestos()
        elif opcion == "2":
            compras_pintura()
        elif opcion == "3":
            orden_compra_automatica()
        elif opcion == "4":
            costos_compras_mes()
        elif opcion == "0":
            break
        else:
            print("Opción inválida, intente nuevamente.")

# ------------------------------
# Funciones internas del módulo
# ------------------------------

def compras_repuestos():
    """
    Pre: Ingreso al módulo de compras de repuestos.
    Post: Registro o consulta de compras de repuestos.
    """
    while True:
        print("\n--- Compras de repuestos ---")
        print("1. Registrar nueva compra de repuesto")
        print("2. Consultar historial de compras de repuestos")
        print("0. Volver al menú anterior")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_compra_repuesto()
        elif opcion == "2":
            historial_compras_repuestos()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

def compras_pintura():
    """
    Pre: Ingreso al módulo de compras de materiales de pintura.
    Post: Registro o consulta de compras de pintura.
    """
    while True:
        print("\n--- Compras de materiales de pintura ---")
        print("1. Registrar nueva compra de material")
        print("2. Consultar historial de compras de materiales")
        print("0. Volver al menú anterior")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_compra_material()
        elif opcion == "2":
            historial_compras_materiales()
        elif opcion == "0":
            break
        else:
            print("Opción inválida")

def orden_compra_automatica():
    """
    Pre: Ingreso al módulo de orden de compra automática.
    Post: Se sugiere orden de compra basada en stock mínimo y consumo histórico.
    """
    pass

def costos_compras_mes():
    """
    Pre: Ingreso al módulo de costos de compras.
    Post: Muestra costos totales de compras por mes.
    """
    pass

# ------------------------------
# Funciones a implementar
# ------------------------------

def registrar_compra_repuesto():
    pass

def historial_compras_repuestos():
    pass

def registrar_compra_material():
    pass

def historial_compras_materiales():
    pass
