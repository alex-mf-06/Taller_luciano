import json
import os
from datetime import datetime
import utils as ut


# Preguntar -------------------------------------------------------------------------------------------------------------------------------------

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


# CARGA DE DATOS A LA MEMORIA RAM ----------------------------------------------------------------------------------------------------------------

def cargar_archivo(archivo_json):
    """
    Trae el archivo json ingresado como parametro
    """

    if os.path.exists(archivo_json):  # verifica si el archivo existe
        with open(archivo_json, "r", encoding="utf-8") as file:  # abrir el archivo
            try:
                return json.load(file)

            except json.JSONDecodeError:  # Si el archivo esta vacio o da error, retorna una lista vacia
                return []
    else:
        return []


# VALIDACIÓN DE EXISTENCIA DEL DATO -------------------------------------------------------------------------------------------------------------------

def existe_en_archivo(archivo_json: str, dato_a_buscar: str, tipo_dato: str) -> bool:
    """
    Verifica si existe el dato ingresado en el archivo json indicado en el parametro.

    """

    archivo = cargar_archivo(archivo_json)

    for dato in archivo:
        if dato.get(tipo_dato) == dato_a_buscar:
            return True

    return False


# Sección ORDENES -------------------------------------------------------------------------------------------------------------------------------------

def guardar_ordenes(ordenes: list, ruta: str):
    """
    Esta función se encarga de guardar la orden creada en ordenes.json (Disco duro)

    Pre: 
        - Recibe la lista Ordenes
        - Recibe la ruta donde se encuentra el archivo ordenes.json donde sera guardado con los nuevos datos

    Post: Sobreescribe el archivo ordenes.json con los datos nuevos.
    """
    try:
        with open(ruta, "w", encoding="utf-8") as file:
            json.dump(ordenes, file, indent=4)

        print(
            f"Se ha guardado con existo {len(ordenes)} ordenes en el registro de ordenes.")
        return True

    except IOError as ioe:
        print(f"{"-"*70} \nERROR - Ha ocurrido un error en el sistema y no se pudieron guardar los datos \nDetalle del error: {ioe}")
        return False

    except Exception as e:
        print(
            "ERROR - Ha ocurrido un fallo desconocido al intentar guardar los datos. \nDetalle del error: {e}")


def crear_orden(ordenes: list, ruta_vehiculos: str, ruta_empleados: str, ruta_ordenes: str) -> list:

    # Genera un id automaticamente a la orden
    if ordenes:
        nuevo_id = ordenes[-1]["id"] + 1
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
        "Ingrese la descripción del problema que presenta el vehiculo").strip()

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

    # Se agrega la nueva orden al final de la lista Ordenes
    ordenes.append(nueva_orden)
    print(f"{"-"*20} La orden N°{nuevo_id} a sido creado con exito {"-"*20} ")

    # Se trata de guardar la orden creada en el archivo ordenes.json
    if guardar_ordenes(ordenes, ruta_ordenes):
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
        print("\n" + "="*80)
        print("RESUMEN DE ÓRDENES DE TRABAJO")
        print("="*80)

        encabezado = "{:<5} {:<19} {:<10} {:<20} {:<12} {:<10}".format(
            "ID", "FECHA INGRESO", "PATENTE", "EMPLEADO", "ESTADO", "COSTO")
        print(encabezado)
        print("-" * 80)

        for orden in ordenes:

            # El costo se castea a un dato string y si el mismo no se ingreso se muestra (N/A).
            costo_str = f"${orden.get('costo_estimado', 0):.2f}" if orden.get(
                'costo_estimado') is not None else "N/A"

            linea_orden = "{:<5} {:<19} {:<10} {:<20} {:<12} {:<10}".format(
                orden.get('id', ''),
                orden.get('fecha_de_creacion', 'N/D'),
                orden.get('patente', 'N/D'),
                orden.get('empleado', 'N/D'),
                orden.get('estado', 'N/D'),
                costo_str
            )
            print(linea_orden)
        print("=" * 80)


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

    if guardar_ordenes(ordenes, ruta_ordenes):
        pass

    else:
        print("Advertencia: La modificación de la orden se realizó en memoria, pero no se pudo guardar en el disco.")

    return ordenes


# MENÚ   -----------------------------------------------------------------------


def menu_ordenes() -> None:

    ARCHIVO_VEHICULOS = "datos/vehiculos.json"
    ARCHIVO_EMPLEADOS = "datos/empleados.json"
    ARCHIVO_ORDENES = "datos/ordenes.json"
    ordenes = cargar_archivo(ARCHIVO_ORDENES)

    opciones = [
        "Crear nueva orden de trabajo",
        "Mostrar todas las órdenes",
        "Modificar estado de una orden",
        "Salir del sistema"
    ]

    while True:
        ut.opciones_menu("ORDENES DE TRABAJO", opciones)

        opcion = input("Ingrese la opción (1-4): ").strip()

        if opcion == "1":
            # Llama a crear_orden, que maneja el guardado interno.
            ordenes_actualizadas = crear_orden(
                ordenes, ARCHIVO_VEHICULOS, ARCHIVO_EMPLEADOS, ARCHIVO_ORDENES)
            if ordenes_actualizadas is not None:
                ordenes = ordenes_actualizadas  # Actualiza la lista principal en RAM

        elif opcion == "2":
            mostrar_ordenes(ordenes)

        elif opcion == "3":
            # Llama a modificar_estado_de_orden, que maneja el guardado interno.
            ordenes_actualizadas = modificar_estado_de_orden(
                ordenes, ARCHIVO_ORDENES)
            if ordenes_actualizadas is not None:
                ordenes = ordenes_actualizadas  # Actualiza la lista principal en RAM

        elif opcion == "4":
            print("\nCerrando el sistema. ¡Hasta pronto!")
            break  # Sale del bucle while True, finalizando el programa

        else:
            print("\nERROR: Opción no válida. Por favor, ingrese un número del 1 al 4.")
