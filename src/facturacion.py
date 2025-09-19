import os

def menu_facturacion():
    """
    Muestra el menú principal del módulo de facturación.
    """
    while True:
        print("\n=== Módulo Facturación ===")
        print("1. Crear factura a partir de una orden")
        print("2. Buscar factura")
        print("3. Listar facturas")
        print("0. Volver al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                crear_factura()
            elif opcion == 2:
                buscar_factura()
            elif opcion == 3:
                listar_facturas()
            elif opcion == 0:
                break
            else:
                print("Opción inválida, intente nuevamente.")
        except ValueError:
            print("Valor invalido. Por favor, ingrese un numero.")
            continue

# ---------------------------------------------
# Funciones principales (pendientes de implementar)
# ---------------------------------------------

def crear_factura():
    """
    Crea una nueva factura a partir de una orden de trabajo finalizada.

    Pre-condición:
        - Requiere el ID de una orden de trabajo.
        - La orden debe estar completa y con el estado 'Finalizada'.

    Post-condición:
        - Se crea un nuevo registro de factura con un ID único.
        - El registro contiene los datos del cliente, vehículo, ítems y el total.
        - El estado de la orden de trabajo se actualiza a 'Facturada'.
    """
    while True:
        try:
            print("\n--- Crear Nueva Factura ---")
            orden_id = input("Ingrese el ID de la orden de trabajo (o '0' para cancelar): ")
            
            if orden_id == '0':
                print("Creación de factura cancelada.")
                break
                
            # Validar que el ID sea un número
            orden_id = int(orden_id)
            
            print("Lógica para procesar la factura (pendiente de implementar)")
            break
            
        except ValueError:
            print("Entrada inválida. El ID de la orden debe ser un número.")
            continue

def buscar_factura():
    """
    Busca una factura por un criterio de búsqueda.

    Pre-condición:
        - Se necesita un criterio de búsqueda (ID de factura, patente o DNI del cliente).

    Post-condición:
        - Si se encuentra, muestra los detalles de la factura.
        - Si no se encuentra, notifica al usuario.
    """
    while True:
        print("\n--- Buscar Factura ---")
        print("1. Buscar por ID de factura")
        print("2. Buscar por DNI del cliente")
        print("3. Buscar por patente del vehículo")
        print("0. Volver al menú anterior")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                factura_id = input("Ingrese el ID de la factura: ")
                print(f"Buscando factura con ID {factura_id} (pendiente de implementar)")
                break
            elif opcion == 2:
                dni_cliente = input("Ingrese el DNI del cliente: ")
                print(f"Buscando factura(s) por DNI {dni_cliente} (pendiente de implementar)")
                break
            elif opcion == 3:
                patente_vehiculo = input("Ingrese la patente del vehículo: ")
                print(f"Buscando factura(s) por patente {patente_vehiculo} (pendiente de implementar)")
                break
            elif opcion == 0:
                break
            else:
                print("Opción inválida, por favor ingrese un número del 0 al 3.")
        
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue


def listar_facturas():
    """
    Muestra un listado de facturas según el criterio seleccionado.

    Pre-condición:
        - El archivo 'facturas.json' debe existir.

    Post-condición:
        - Se muestra una lista formateada de las facturas que coinciden con el criterio de búsqueda.
        - Si no hay coincidencias, se notifica al usuario.
    """
    while True:
        print("\n--- Listar Facturas ---")
        print("1. Mostrar todas las facturas")
        print("2. Mostrar facturas de un vehículo por patente")
        print("3. Mostrar facturas por ID de orden")
        print("0. Volver al menú anterior")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                print("Función para mostrar todas las facturas (pendiente de implementar)")
                break
            elif opcion == 2:
                patente_vehiculo = input("Ingrese la patente del vehículo: ")
                print(f"Buscando facturas para la patente {patente_vehiculo} (pendiente de implementar)")
                break
            elif opcion == 3:
                orden_id = input("Ingrese el ID de la orden: ")
                print(f"Buscando facturas para la orden #{orden_id} (pendiente de implementar)")
                break
            elif opcion == 0:
                break
            else:
                print("Opción inválida. Por favor, ingrese un número del 0 al 3.")
        
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")
            continue
