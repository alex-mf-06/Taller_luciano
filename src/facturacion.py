import os
import utils as ut
from datetime import datetime
from typing import List, Dict
from config import RUTA_FACTURACION, RUTA_CLIENTES, RUTA_VEHICULOS , RUTA_ORDENES

lista_clientes = ut.cargar_datos(RUTA_CLIENTES)  
lista_vehiculos = ut.cargar_datos(RUTA_VEHICULOS)
lista_facturas = ut.cargar_datos(RUTA_FACTURACION)
lista_ordenes = ut.cargar_datos(RUTA_ORDENES)


def agregar_factura(lista_facturas: List[Dict], lista_clientes: List[Dict], lista_vehiculos: List[Dict], lista_ordenes: List[Dict]) -> List[Dict]:
    """
    Crea una nueva factura validando cliente, vehículo y datos de ítems.

    Pre:
        - Deben existir clientes y vehículos cargados en sus respectivos JSON.
        - Las funciones de validación deben devolver valores válidos.
    Post:
        - Se agrega una nueva factura al archivo 'facturacion.json'.
        - Se calcula automáticamente el total.
        - Devuelve la lista de facturas actualizada.
    """
    try:
        if lista_ordenes:
            n_factura = ut.encontrar_n_factura(RUTA_ORDENES)
            tipo_factura = ut.validar_tipo_factura()
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            forma_pago = ut.validar_forma_pago()
            origen = ut.validar_origen()
            dni = ut.validar_dni()
            cliente_encontrado_vehiculo = ut.buscar_x_dni_ruta_vehiculos(dni,RUTA_VEHICULOS)
            cliente_encontrado=ut.buscar_x_dni(dni,RUTA_CLIENTES)
            
            if not cliente_encontrado_vehiculo:
                print("El cliente no está registrado. Debe cargarlo antes de facturar.")
                return lista_facturas

            vehiculo_cliente = None
            for vehiculo in lista_vehiculos:
                if vehiculo.get("dni_cliente") == dni:
                    vehiculo_cliente = vehiculo
                    break

            if not vehiculo_cliente:
                print("No se encontró vehículo asociado al cliente.")
                return lista_facturas

            print("\nIngrese los ítems de la factura (ENTER para terminar):")
            items = []
            while True:
                descripcion = input("Descripción del ítem (ENTER para terminar): ").strip()
                if descripcion == "":
                    break

                cantidad = input("Cantidad: ").strip()
                precio = input("Precio unitario: ").strip()

                try:
                    cantidad = int(cantidad)
                    precio = float(precio)
                except ValueError:
                    print("Error: cantidad y precio deben ser números.")
                    continue

                subtotal = cantidad * precio
                items.append(
                    {
                        "descripcion": descripcion,
                        "cantidad": cantidad,
                        "precio_unitario": precio,
                        "subtotal": subtotal,
                    }
                )

            total = sum(
                item["subtotal"] for item in items
            )  # lista por comprension en caso de que haya mas de un item
            factura = {
                "numero": n_factura,
                "tipo": tipo_factura,
                "fecha": fecha,
                "forma_pago": forma_pago,
                "origen": origen,
                "cliente": {
                    "dni": cliente_encontrado["dni"],
                    "nombre": cliente_encontrado["nombre"],
                    
                },
                "vehiculo": {
                    "patente": vehiculo_cliente["patente"],
                    "marca": vehiculo_cliente["marca"],
                    "modelo": vehiculo_cliente["modelo"],
                    "anio": vehiculo_cliente["anio"],
                },
                "items": items,
                "total": total,
            }

            
            ut.agregar_dato(factura, RUTA_FACTURACION)

            print("\nFactura creada correctamente.")
            return lista_facturas
    except TypeError:
        print("Error al crear la factura.")
        return lista_facturas
    except ValueError:
        print("Error en los datos ingresados.")
        return lista_facturas
    except KeyboardInterrupt:
        print("\nOperación cancelada por el usuario.")
        return lista_facturas

def eliminar_factura(lista_facturas):
    """
    Permite eliminar una factura por su número.
    """
    try:
        numero_factura = input(
            "Ingrese el número de factura a eliminar: (formato 0001-00001234)"
        ).strip()

        for factura in lista_facturas:
            if factura["numero"] == numero_factura:
                lista_facturas.remove(factura)
                print(f"La factura {numero_factura} fue eliminada correctamente.")
                ut.actualizar_datos(lista_facturas, RUTA_FACTURACION)
                break
        else:
            print("No se encontró una factura con ese número.")

    except ValueError:
        print("Error al eliminar la factura.")


def buscar_factura(lista_facturas):
    """
    Busca una factura por un criterio de búsqueda.

    Pre-condición:
        - Se necesita un criterio de búsqueda (ID de factura, patente o DNI del cliente).

    Post-condición:
        - Si se encuentra, muestra los detalles de la factura.
        - Si no se encuentra, notifica al usuario.
    """
    numero = input("Ingrese el número de factura a buscar: ").strip()
    factura_encontrada = None
    for factura in lista_facturas:
        if factura["numero"] == numero:
            factura_encontrada = factura
            break
    if factura_encontrada:
        print("\nFactura encontrada:")
        for clave, valor in factura_encontrada.items():
            print(f"{clave}: {valor}")
    else:
        print("No se encontró ninguna factura con ese número.")

def menu_facturacion() -> None:
    """Muestra el menú del módulo de facturación."""

    opciones = (
        "Salir",
        "Agregar factura manualmente",
        "Buscar factura",
        "Listar facturas",
        "Eliminar factura"
    )

    while True:
        try: 
            ut.opciones_menu("MENÚ DE FACTURACIÓN", opciones)
            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                print("Volviendo al menú principal...")
                break

            elif opcion == "2":
                print("\n--- Agregar factura ---")
                agregar_factura(lista_facturas, lista_clientes, lista_vehiculos, lista_ordenes)


            elif opcion == "3":
                print("\n--- Buscar factura ---")
                buscar_factura(lista_facturas)

            elif opcion == "4":
                print("\n--- Listado de facturas ---")
                ut.listar_datos(lista_facturas, "factura")

            elif opcion == "5":
                print("\n--- Eliminar factura ---")
                eliminar_factura(lista_facturas)

            else:
                print("Opción no válida. Intente nuevamente.\n")
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario.")
            break


if __name__ == "__main__":
    menu_facturacion()