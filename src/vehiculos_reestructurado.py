# descripción: maneja todo lo relacionado con los vehículos
# del taller (alta, baja, modificación, búsqueda, resumen, etc.)

import json
import os
import vehiculos
import re 

RUTA_VEHICULOS = os.path.join("datos","vehiculos.json")

def cargar_vehiculos():
    """Carga la lista de vehículos desde el archivo JSON."""
    if os.path.exists(RUTA_VEHICULOS):
        with open(RUTA_VEHICULOS, "r", encoding="UTF-8") as archivo:
            try:
                lista_vehiculos = json.load(archivo)
            except json.JSONDecodeError:
                lista_vehiculos = []
    else:
        lista_vehiculos = []
    
    return lista_vehiculos

def guardar_vehiculos(lista_vehiculos):
    """pre: Guarda la lista de vehículos en el archivo JSON definido por RUTA_VEHICULOS.
    post: Si ocurre un error durante la escritura, se muestra un mensaje."""
    with open(RUTA_VEHICULOS,"w", encoding="UTF-8") as archivo:
        try:
            json.dump(lista_vehiculos, archivo, indent=4)
        except FileNotFoundError:
            print("No se encontró la ruta del archivo")
        except Exception as e:
            print(f"Error al guardar vehículos:  {e}")


# Funciones CRUD

def agregar_vehiculo(lista_vehiculos):
    patron_patente = r"^[A-Z]{3}\d{3}$|^\d{2}[A-Z]{3}\d{2}$" # expresiones regulares para validación de datos
    patron_anio = r'^\d{4}$'
    patron_dni = r'^\d{7,8}$'

    while True:
        patente = input("Ingrese la patente del vehículo")
        patente = patente.upper()
        if not re.match(patron_patente,patente):
            print("Patente inválida. Debe ser ABC123 o 12ABC34")
        else:
            break
    
    marca = input("Ingrese la marca de su vehículo")
    modelo = input("Ingrese el modelo de su vehículo")
    while True:
        anio = input("ingrese el año de su vehículo")
        if not re.match(patron_anio,anio):
            print("el año debe contener 4 digitos")
        else:
            break

  
    tipo = input("Ingrese el tipo de vehículo(auto, camioneta, camión)")
    
    while True:
        dni = input("Ingrese su número de DNI")
        if not re.match(patron_dni,dni):
            print("DNI inválido")
        else: 
            dni = int(dni)
            break
    vehiculo = {
    "patente": patente,
    "marca": marca,
    "modelo": modelo,
    "anio": anio,
    "tipo": tipo,
    "dni_cliente": dni
    }
    lista_vehiculos.append(vehiculo)
    return lista_vehiculos


lista_vehiculos = cargar_vehiculos()

def buscar_x_patente(lista_vehiculos):
    patron_patente = r"^[A-Z]{3}\d{3}$|^\d{2}[A-Z]{3}\d{2}$"
    try:
        while True:
            patente = input("Ingrese la patente del vehículo a buscar")
            patente = patente.upper()
            if not re.match(patron_patente,patente):
                print("Patente invalida")
            else:
                break

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

def buscar_x_dni(lista_vehiculos):
    """
    Busca todos los vehículos de un cliente según su DNI.
    Muestra cada vehículo encontrado de manera legible.
    """
    patron_dni = r'^\d{7,8}$'
    try:
        while True:
            dni_input = input("Ingrese el DNI del cliente: ")
            if not re.match(patron_dni, dni_input):
                print("DNI inválido. Debe contener 7 u 8 dígitos.")
            else:
                dni = int(dni_input)
                break

        # Lista por comprensión para los vehículos asociados a un DNI   
        encontrados = [vehiculo for vehiculo in lista_vehiculos if vehiculo["dni_cliente"] == dni]
        
        if encontrados:
            print(f"\nSe encontraron {len(encontrados)} vehículo(s) para el DNI {dni}:")
            for i, vehiculo in enumerate(encontrados, start=1):
                print(f"\nVehículo {i}:")
                for clave, valor in vehiculo.items():
                    print(f"{clave.capitalize()}: {valor}")
        else:
            print("No se encontraron vehículos para ese DNI.")
            
    except Exception as e:
        print(f"Ocurrió un error al buscar vehículos por DNI: {e}")



def eliminar_vehiculo(lista_vehiculos):
    patron_patente = r"^[A-Z]{3}\d{3}$|^\d{2}[A-Z]{3}\d{2}$"
    try:
        while True:
            patente = input("Ingrese la patente del vehículo a buscar")
            patente = patente.upper()
            if not re.match(patron_patente,patente):
                print("Patente invalida")
            else:
                break

        for vehiculo in lista_vehiculos:
            if vehiculo["patente"] == patente:
                lista_vehiculos.remove(vehiculo)
                print(f"El vehículo con patente {patente}")
    except ValueError:
        print("Error al eliminar el vehículo")
    except KeyError:
        print("No se encontró esa patente en el registro")



def modificar_vehiculo(lista_vehiculos):
    patron_patente = r"^[A-Z]{3}\d{3}$|^\d{2}[A-Z]{3}\d{2}$" # expresiones regulares para validación de datos
    patron_anio = r'^\d{4}$'
    patron_dni = r'^\d{7,8}$'
    try:
        while True:
            patente = input("Ingrese la patente del vehículo a buscar")
            patente = patente.upper()
            if not re.match(patron_patente,patente):
                print("Patente invalida")
            else:
                break
    
        for vehiculo in lista_vehiculos:
            if vehiculos["patente"] == patente:
                break
        else:
            print("vehículo no encontrado")

        print("Ingrese ENTER para mantener el valor actual")

        nuevo_marca = input(f"Marca actual: {vehiculos['marcas']}:").strip()
        if nuevo_marca:
            vehiculos["modelo"] = nuevo_marca
        
        nuevo_modelo = input(f"Año (actual: {vehiculos['anio']}): ").strip()
        if nuevo_modelo:
            vehiculos["marca"] = nuevo_modelo
        while True:
            nuevo_anio = input(f"Año (actual: {vehiculo['anio']}): ").strip()
            if not nuevo_anio:  
                break
            if re.match(patron_anio, nuevo_anio):
                vehiculo['anio'] = nuevo_anio
                break
            print("Año inválido. Debe tener 4 dígitos.")

        nuevo_tipo = input(f"Tipo (actual: {vehiculo['tipo']}): ").strip()
        if nuevo_tipo:
            vehiculo['tipo'] = nuevo_tipo

        while True:
            nuevo_dni = input(f"DNI (actual: {vehiculo['dni_cliente']}): ").strip()
            if not nuevo_dni:
                break  
            if re.match(patron_dni, nuevo_dni):
                try:
                    vehiculo['dni_cliente'] = int(nuevo_dni)
                    break
                except ValueError:
                    print("DNI debe ser numérico.")
            else:
                print("DNI inválido. Debe tener 7 u 8 dígitos.")

        guardar_vehiculos(lista_vehiculos)
        print("Vehículo modificado correctamente.")

    except KeyError:
        print("Estructura de datos inesperada: falta alguna clave.")
        

def listar_vehiculos(lista_vehiculos):
    """
    Lista todos los vehículos cargados en el taller de manera legible.
    """
    try:
        if not lista_vehiculos:
            print("No hay vehículos cargados en el taller.")
            return

        print(f"\nListado de {len(lista_vehiculos)} vehículo(s):")
        for i, vehiculo in enumerate(lista_vehiculos, start=1):
            print(f"\nVehículo {i}:")
            for clave, valor in vehiculo.items():
                print(f"{clave.capitalize()}: {valor}")
    except (TypeError, KeyError):
        print("Error al listar los vehículos")
    except Exception as e:
        print(f"Ocurrió un error al listar los vehículos: {e}")




if __name__ == "__main__":

    lista_vehiculos = cargar_vehiculos()

    opciones = {
        "1": ("Agregar vehículo", lambda: agregar_vehiculo(lista_vehiculos)),
        "2": ("Modificar vehículo", lambda: modificar_vehiculo(lista_vehiculos)),
        "3": ("Eliminar vehículo", lambda: eliminar_vehiculo(lista_vehiculos)),
        "4": ("Buscar por patente", lambda: buscar_x_patente(lista_vehiculos)),
        "5": ("Buscar por DNI", lambda: buscar_x_dni(lista_vehiculos)),
        "6": ("Listar vehículos", lambda: listar_vehiculos(lista_vehiculos)),
        "7": ("Salir", None)
    }

    while True:
        print("\n--- MENÚ DE GESTIÓN DE VEHÍCULOS ---")
        for clave, (descripcion, _) in opciones.items():
            print(f"{clave}. {descripcion}")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion in opciones:
            if opcion == "7":
                print("Saliendo del sistema...")
                guardar_vehiculos(lista_vehiculos)  # guarda antes de salir
                break
            else:
                try:
                    opciones[opcion][1]()  # ejecuta la función asociada
                    guardar_vehiculos(lista_vehiculos)
                except KeyError:
                    print(f"Ingresaste un valor inválido")
        else:
            print("Opción inválida. Intente nuevamente.")
