import json
import os
from datetime import datetime
import utils as ut
from config import RUTA_ORDENES, RUTA_EMPLEADOS, RUTA_VEHICULOS
from typing import List, Dict

# Pregunta si resgistro anteriormente vehiculo o empleado -------------------------------------------------------------------------------------------------------------------------------------


def preguntar(tipo_de_dato: str):
    while True:
        pregunta = input(
            f"ERROR - El dato ingresado no existe \n¿Registro {tipo_de_dato} del vehiculo antes de crear la orden? (si/no)").lower().strip()

        if pregunta == "si":
            return True

        elif pregunta == "no":
            print(
                "Debera registrar primero el vehiculo antes de crear una orden de trabajo.")
            return False

        else:
            print("La respuesta ingresada no es valida, intente denuevo")


# VALIDACIÓN DE EXISTENCIA DEL DATO -------------------------------------------------------------------------------------------------------------------

def existe_en_archivo(archivo_json: str, dato_a_buscar: str, tipo_dato: str) -> bool:
    """
    Verifica si existe el dato ingresado en el archivo json indicado en el parametro.

    """
    try:
        archivo = ut.cargar_datos(archivo_json)

        for dato in archivo:
            # Verifica si el dato existe en el archivo
            if dato.get(tipo_dato) == dato_a_buscar:
                return True

        return False
    except ValueError as ve:
        print(f"Error al procesar el archivo: {ve}")
        return False
    except TypeError:
        print("Error de tipo al procesar el archivo.")
        return False
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return False


# Sección ORDENES -------------------------------------------------------------------------------------------------------------------------------------




def crear_orden(ordenes: list, ruta_vehiculos: str, ruta_empleados: str, ruta_ordenes: str) -> list:

    # Genera un id automaticamente a la orden
    if ordenes:
        nuevo_id = ordenes[-1]["id"] + 1  # Toma el ultimo id y le suma 1
    else:
        nuevo_id = 1

    print(f"\n {"-"*20} Nueva orden de trabajo {"-"*20}")

    # Solicita y valida la existencia de la patente ingresada
    while True:
        patente = input("Ingrese la patente del vehiculo: ")
        if existe_en_archivo(ruta_vehiculos, patente, "patente"):
            break
        else:
            if not preguntar("la patente"):
                return ordenes

    # Solicita y Valida el nombre del empleado a cargo de la orden de trabajo
    while True:
        empleado = input("Ingrese el nombre completo del empleado: ")
        if existe_en_archivo(ruta_empleados, empleado, "nombre"):
            break
        else:
            if not preguntar("el empleado"):
                return ordenes

    while True:
        costo_est = input("Ingrese el costo estimado para dicha reparación: ")
        try:
            costo_estimado = float(costo_est)
            break
        except ValueError:
            print(
                "ERROR - El valor ingresado debe ser un valor numerico entero o decimal (Ej: 1234 o 1234.00)")

    # Solicita la descripción del problema del vehiculo a reparar
    descripcion = input(
        "Ingrese la descripción del problema que presenta el vehiculo: ").strip()

    # Crea el diccionario con todos los datos ingresados para la generar la orden
    nueva_orden = {
        "id": nuevo_id,
        "fecha_de_creacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "patente": patente,
        "empleado": empleado,
        "descripcion": descripcion,
        "estado": "PENDIENTE",
        "costo_estimado": costo_estimado
    }

    
    print(f"{"-"*20} La orden N°{nuevo_id} a sido creado con exito {"-"*20} ")

    # Se trata de guardar la orden creada en el archivo ordenes.json
    if ut.agregar_dato(nueva_orden, ruta_ordenes):
        return ordenes

    else:
        print("Error - La orden no pudo ser guardada en el disco duro.")


def mostrar_ordenes(ordenes: list):
    """
    Esta función muestra al usuario una lista con las ordenes existentes en el archivo ordenes.json.

    Pre: 
        - Recibe la lista de Ordenes

    Post:
        - Muestra en pantalla los elemento de la lista ordenes
    """

    # Caso: Si no hubiera ordenes
    if not ordenes:
        print(f"{"-"*20} No hay ordenes de trabajo registradas para mostrar {"-"*20}")
        return

    # Caso: Si existen ordenes
    else:
        print("\n" + "="*100)
        print("RESUMEN DE ÓRDENES DE TRABAJO")
        print("="*100)

        encabezado = "{:<5} {:<25} {:<10} {:<20} {:<12} {:<10}".format(
            "ID", "FECHA INGRESO", "PATENTE", "EMPLEADO", "ESTADO", "COSTO")
        print(encabezado)
        print("-" * 100)

        for orden in ordenes:

            # El costo se castea a un dato string y si el mismo no se ingreso se muestra (N/A).
            costo_str = f"${orden.get('costo_estimado', 0):.2f}" if orden.get(
                'costo_estimado') is not None else "N/A"

            linea_orden = "{:<5} {:<25} {:<10} {:<20} {:<12} {:<10}".format(
                orden.get('id', ''),
                orden.get('fecha_de_creacion', 'N/D'),
                orden.get('patente', 'N/D'),
                orden.get('empleado', 'N/D'),
                orden.get('estado', 'N/D'),
                costo_str
            )

            print(linea_orden)
        print("=" * 100)


def modificar_estado_de_orden(ordenes: list, ruta_ordenes: str) -> list:
    """
    Permite modificar el estado de una orden en: PENDIENTE, EN PROCESO o FINALIZADA.

    Pre: 
        - Recibe la lista 'ordenes' en memoria y la ruta de guardado (ruta_ordenes).

    Post: 
        - Retorna la lista modificada y guarda los cambios en disco.
    """

    if not ordenes:
        print("\nNo hay órdenes registradas para modificar.")
        return ordenes

    print("\n--- Modificar Estado de Orden ---")

    # Solicitar al usuario el ID a buscar -------
    orden_encontrada = None

    while True:
        try:
            id_a_buscar = int(
                input("Ingrese el ID de la orden a modificar (o 0 para cancelar): "))

            if id_a_buscar == 0:
                print("La modificación fue cancelada.")
                return ordenes

            orden_encontrada = next(
                (o for o in ordenes if o['id'] == id_a_buscar), None)

            if orden_encontrada:
                break
            else:
                print(
                    f"Error - No se encontró ninguna orden con ID: {id_a_buscar}.")

        except ValueError:
            print("Error - Ingrese un ID numérico válido.")

    # Seleccionar y validar el nuevo estado de la orden -----
    estados_validos = ["PENDIENTE", "EN PROCESO", "FINALIZADA"]

    print(
        f"\nEstado actual de la Orden N°{orden_encontrada['id']}: {orden_encontrada['estado']}")
    print("Opciones de estado: 1. PENDIENTE | 2. EN PROCESO | 3. FINALIZADA")

    while True:
        opcion_estado_str = input(
            "Seleccione el número del nuevo estado (1, 2 o 3): ").strip()

        if opcion_estado_str in ["1", "2", "3"]:
            indice = int(opcion_estado_str) - 1
            nuevo_estado = estados_validos[indice]
            break
        else:
            print("Error - Opción no válida. Ingrese 1, 2 o 3.")

    # Guardado del cambio
    orden_encontrada['estado'] = nuevo_estado

    print(
        f"\nEstado de la Orden N°{orden_encontrada['id']} actualizado a: {nuevo_estado}")

    if ut.agregar_dato(orden_encontrada, ruta_ordenes):
        pass

    else:
        print("Advertencia: La modificación de la orden se realizó en memoria, pero no se pudo guardar en el disco.")

    return ordenes


def mostrar_ordenes_filtradas(ordenes: list) -> None:
    """
    Muestra las órdenes filtradas por estado (PENDIENTE, EN PROCESO o FINALIZADA).

    Pre:
        - Recibe la lista 'ordenes'.
    Post:
        - Muestra las órdenes según el estado seleccionado.
    """

    # Caso: lista vacía
    if not ordenes:
        print(f"{'-'*20} No hay órdenes registradas para filtrar {'-'*20}")
        return

    # Estados válidos
    estados_validos = ["PENDIENTE", "EN PROCESO", "FINALIZADA"]

    # Menú de selección
    print("\n" + "="*80)
    print("FILTRAR ÓRDENES POR ESTADO")
    print("="*80)
    print("1. PENDIENTE \n2. EN PROCESO \n3. FINALIZADA")
    print("0. Volver al menú anterior")
    print("-"*80)

    # Leer opción del usuario
    while True:
        opcion = input("Seleccione una opción (0-3): ").strip()
        if opcion == "0":
            print("Volviendo al menú anterior...")
            return
        elif opcion in ["1", "2", "3"]:
            estado_seleccionado = estados_validos[int(opcion) - 1]
            break
        else:
            print("Error - Opción inválida. Ingrese 0, 1, 2 o 3.")

    # Filtrar las órdenes
    ordenes_filtradas = [o for o in ordenes if o.get(
        "estado") == estado_seleccionado]

    # Mostrar resultado
    print("\n" + "="*100)
    print(f"ÓRDENES EN ESTADO: {estado_seleccionado}")
    print("="*100)

    if not ordenes_filtradas:
        print(f"No se encontraron órdenes con estado '{estado_seleccionado}'.")
        return

    # Encabezado con  formato igual al de mostrar_ordenes()
    encabezado = "{:<5} {:<25} {:<10} {:<20} {:<12} {:<10}".format(
        "ID", "FECHA INGRESO", "PATENTE", "EMPLEADO", "ESTADO", "COSTO"
    )
    print(encabezado)
    print("-" * 100)

    # Filas de las órdenes filtradas
    for orden in ordenes_filtradas:
        costo_str = f"${orden.get('costo_estimado', 0):.2f}" if orden.get(
            'costo_estimado') is not None else "N/A"

        linea_orden = "{:<5} {:<25} {:<10} {:<20} {:<12} {:<10}".format(
            orden.get('id', ''),
            orden.get('fecha_de_creacion', 'N/D'),
            orden.get('patente', 'N/D'),
            orden.get('empleado', 'N/D'),
            orden.get('estado', 'N/D'),
            costo_str
        )
        print(linea_orden)

    print("=" * 100)


# MENÚ   -----------------------------------------------------------------------

def menu_ordenes() -> None:
    """
    Muestra el menú principal del módulo de órdenes de trabajo.
    """
    ordenes = ut.cargar_datos(RUTA_ORDENES)

    opciones = (
        "Volver al menu anterior",
        "Crear nueva orden de trabajo",
        "Mostrar todas las órdenes",
        "Mostrar ordenes filtradas por estado",
        "Modificar estado de una orden"
    )

    while True:
        ut.opciones_menu("ORDENES DE TRABAJO", opciones)

        opcion = input("Ingrese la opción (1-5): ").strip()

        if opcion == "1":
            print("\nCerrando el sistema. ¡Hasta pronto!")
            break

        elif opcion == "2":
            ordenes_actualizadas = crear_orden(
                ordenes, RUTA_VEHICULOS, RUTA_EMPLEADOS, RUTA_ORDENES)
            if ordenes_actualizadas is not None:
                ordenes = ordenes_actualizadas   # Actualiza la lista principal en RAM

        elif opcion == "3":
            mostrar_ordenes(ordenes)

        elif opcion == "4":
            mostrar_ordenes_filtradas(ordenes)

        elif opcion == "5":
            ordenes_actualizadas = modificar_estado_de_orden(
                ordenes, RUTA_ORDENES)

            if ordenes_actualizadas is not None:
                ordenes = ordenes_actualizadas  # Actualiza la lista principal en RAM

        else:
            print("\nERROR: Opción no válida. Por favor, ingrese un número del 1 al 5.")


if __name__ == "__main__":
    menu_ordenes()
