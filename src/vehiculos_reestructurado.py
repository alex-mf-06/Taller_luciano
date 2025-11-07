from typing import List, Dict,Tuple
import os
import utils as ut
from config import RUTA_VEHICULOS, RUTA_CLIENTES




lista_vehiculos = ut.cargar_datos(RUTA_VEHICULOS)
lista_clientes = ut.cargar_datos(RUTA_CLIENTES)


# Funciones CRUD

def agregar_vehiculo(lista_vehiculos: List[Dict])-> List[Dict]:
    """Agrega un nuevo vehículo al sistema y lo guarda en 'vehículos.Json'
    
    Pre: - Deben existir clientes cargados en 'clientes.Json'
         - Las funciones de validación deben devolver valores válidos
    
    Post: - Se agrega un nuevo diccionario conteniendo los datos del vehiculo a la lista
          - Se actualiza el archivo Json de vehículos
          - Retorna la lista actualizada """
    while True:
        patentes= cargar_patentes(RUTA_VEHICULOS)
        while True :
            patente = ut.Validar_patente()
            if patente in patentes:
                print("Esa matricula ya esta registrada en un auto")
            else:
                break
        marca = ut.validar_marca()
        modelo = ut.validar_modelo()
        anio = ut.validar_año()
        tipo = ut.validar_tipo()
        dni_clientes =ut.cargar_dni_(RUTA_CLIENTES)
        

        while True:
            
            dni = ut.validar_dni()
            
            if dni in dni_clientes: 
                break
            else:
                print("El DNI no está registrado. Debe registrar primero el cliente")
        vehiculo = {
            "patente": patente,
            "marca": marca,
            "modelo": modelo,
            "anio": anio,
            "tipo": tipo,
            "dni_cliente": dni
        }
        if ut.confirmar_informacion(vehiculo):

            lista_vehiculos.append(vehiculo)
            ut.agregar_dato(vehiculo,RUTA_VEHICULOS) 
            
            print("\nVehículo cargado correctamente:\n")
            for clave, valor in vehiculo.items():
                print(f"{clave.capitalize()}: {valor}")
            return lista_vehiculos



def buscar_x_patente(lista_vehiculos: List[Dict])-> None:
    """ Busca e imprime la información de un vehículo según su patente.

    Pre: - La lista de vehículos debe estar cargada previamente
         - El usuario debe ingresar una patente válida

    Post: - Muestra en consola los datos del vehículo si existe
          - Maneja excepciones en casos de error """
    try:
        patente = ut.Validar_patente()

        for vehiculo in lista_vehiculos:
            if vehiculo["patente"] == patente:
                print("vehículo encontrado:")
                for clave, valor in vehiculo.items():
                    print(f"{clave.capitalize()}: {valor}")
                break

        else:
            print("Vehiculo no encontrado")
    except Exception as e:
        print(f"ocurrió un error al buscar el vehículo: {e}")


def buscar_vehiculos_por_dni(lista_vehiculos: List[Dict])-> None:
    """ Usa la función genérica de utils para buscar vehículos por DNI.
    Pre:
        - La lista de vehículos debe estar cargada y tener la clave 'dni_cliente'.
    Post:
        - Imprime los vehículos coincidentes en consola.
        - No altera archivos ni estructuras."""
    ut.mostrar_x_dni(lista_vehiculos, "dni_cliente", "vehículos")

def cargar_patentes(RUTA_VEHICULOS: str) -> Tuple[str]:
    """
    
   Esta funcion se encarga de que ingresen la ruta de vehivulos para sacar las patentes 
   precondiciones: La ruta de vehiculos debe ser un string .
   postcondiciones devuelve una tupla con las patentes de los vehiculos.
    
    """
    try:
        # 1. CORRECCIÓN: Guardamos el resultado de la carga
        lista_vehiculos = ut.cargar_datos(RUTA_VEHICULOS)

        
        if not isinstance(lista_vehiculos, list):
            print(f"Error: los datos en {RUTA_VEHICULOS} no son una lista.")
            return ()

        
        patentes = tuple(v.get("patente") for v in lista_vehiculos if v.get("patente"))
        
        return patentes

    
    except Exception as e:
        print(f"Ocurrió un error inesperado al procesar las patentes: {e}")
        return () # Siempre devolvemos una tupla vacía en caso de error
    


def eliminar_vehiculo(lista_vehiculos: List[Dict])-> None:
    """Elimina un vehículo de la lista según su patente.
        Pre:
        - El usuario debe ingresar una patente existente
        - La lista de vehículos debe estar cargada
    Post:
        - El vehículo es eliminado de la lista y del archivo JSON
        - Muestra un mensaje indicando el resultado"""
    try:
        patente = ut.Validar_patente()


        for vehiculo in lista_vehiculos:
            if vehiculo["patente"] == patente:
                lista_vehiculos.remove(vehiculo)
                print(f"El vehículo con patente {patente} fue eliminado correctamente")
                ut.actualizar_datos(lista_vehiculos,RUTA_VEHICULOS) 
                return 
        else:
            print("No se encontró un vehículo con esa patente")
    
    except ValueError:
        print("Error al eliminar el vehículo")
    



def modificar_vehiculo(lista_vehiculos: List[Dict])-> None:
    """
    Modifica los datos de un vehículo identificado por su patente.

    Pre:
        - La lista debe contener al menos un vehículo.
        - El usuario debe ingresar una patente válida y existir en el JSON.
    Post:
        - Los campos modificados se actualizan en la lista y en el archivo JSON.
        - Si no se encuentra el vehículo, se notifica al usuario.
    """
    try:
        patente = ut.Validar_patente()  
        vehiculo = None

        for v in lista_vehiculos:
            if v["patente"] == patente:
                vehiculo = v
                break

        if not vehiculo:
            print("Vehículo no encontrado.")
            return

        print("Presione ENTER para mantener el valor actual.\n")

        nueva_marca = input(f"Marca (actual: {vehiculo['marca']}): ").strip()
        if nueva_marca:
            vehiculo["marca"] = nueva_marca

        nuevo_modelo = input(f"Modelo (actual: {vehiculo['modelo']}): ").strip()
        if nuevo_modelo:
            vehiculo["modelo"] = nuevo_modelo

        nuevo_anio = input(f"Año (actual: {vehiculo['anio']}): ").strip()
        if nuevo_anio:
            try:
                vehiculo["anio"] = int(nuevo_anio)
            except ValueError:
                print("El año debe ser numérico. Se mantiene el valor anterior.")

        nuevo_tipo = input(f"Tipo (actual: {vehiculo['tipo']}): ").strip()
        if nuevo_tipo:
            vehiculo["tipo"] = nuevo_tipo

        print(f"DNI del cliente (actual: {vehiculo['dni_cliente']}) [no modificable]")


        ut.guardar_json(lista_vehiculos, RUTA_VEHICULOS)
        print("Vehículo modificado correctamente.")

    except KeyError:
        print("Estructura de datos inesperada: falta alguna clave.")
        

def menu_vehiculos() -> None:
    """Muestra el menú del módulo de vehículos."""

    opciones = (
        "Salir",
        "Agregar vehículo",
        "Buscar vehículo por patente",
        "Buscar vehículo por DNI",
        "Eliminar vehículo",
        "Modificar vehículo",
        "Listar vehículos"
    )

    while True:
        try:
            ut.opciones_menu("MENÚ DE VEHÍCULOS", opciones)
            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                print("Volviendo al menú principal...")
                break
            elif opcion == "2":
                agregar_vehiculo(lista_vehiculos)
            elif opcion == "3":
                buscar_x_patente(lista_vehiculos)
            elif opcion == "4":
                buscar_vehiculos_por_dni(lista_vehiculos)
            elif opcion == "5":
                eliminar_vehiculo(lista_vehiculos)
            elif opcion == "6":
                modificar_vehiculo(lista_vehiculos)
            elif opcion == "7":
                ut.listar_datos(lista_vehiculos, "vehiculo")
            else:
                print("Opción no válida. Intente nuevamente.\n")
        except KeyboardInterrupt:
            print("\nOperación cancelada por el usuario.")
            break



if __name__ == "__main__":
    menu_vehiculos()