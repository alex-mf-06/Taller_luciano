import json
import os
import facturacion
import re

RUTA_FACTURACION = os.path.join("datos", "facturacion.json")


def cargar_facturacion():
    """carga la lita de facturas desde el archivo json"""
    if os.path.exists(RUTA_FACTURACION):
        with open(RUTA_FACTURACION,"r", encoding="UTF-8") as archivo:
            try:
                lista_facturas = json.load(archivo)
            except json.JSONDecodeError:
                lista_facturas = []
    else: 
        lista_facturas = []

    return lista_facturas



def crear_factura():
    """
    Crea una nueva factura a partir de una orden de trabajo finalizada.

    Pre-condición:d
        - Requiere el ID de una orden de trabajo.
        - La orden debe estar completa y con el estado 'Finalizada'.

    Post-condición:
        - Se crea un nuevo registro de factura con un ID único.
        - El registro contiene los datos del cliente, vehículo, ítems y el total.
        - El estado de la orden de trabajo se actualiza a 'Facturada'.
    """
    

def buscar_factura():
    """
    Busca una factura por un criterio de búsqueda.

    Pre-condición:
        - Se necesita un criterio de búsqueda (ID de factura, patente o DNI del cliente).

    Post-condición:
        - Si se encuentra, muestra los detalles de la factura.
        - Si no se encuentra, notifica al usuario.
    """
    pass

def listar_facturas():
    """
    Muestra un listado de facturas según el criterio seleccionado.

    Pre-condición:
        - El archivo 'facturas.json' debe existir.

    Post-condición:
        - Se muestra una lista formateada de las facturas que coinciden con el criterio de búsqueda.
        - Si no hay coincidencias, se notifica al usuario.
    """
    pass

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
