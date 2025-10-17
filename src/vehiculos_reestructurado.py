import json
import os
import vehiculos
import re 
import utils as ut

RUTA_VEHICULOS = os.path.join("datos","vehiculos.json")
RUTA_CLIENTES = os.path.join("datos","clientes.json")


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

def cargar_clientes():
    """carga la lista de vehículos desde el archvio JSON."""
    if os.path.exists(RUTA_CLIENTES):
        with open(RUTA_CLIENTES, "r", encoding="UTF-8") as archivo_clientes:
            try:
                lista_clientes = json.load(archivo_clientes)
            except json.JSONDecodeError:
                lista_clientes = []
    else:
        lista_clientes = []
    
    return lista_clientes
    

lista_vehiculos = cargar_vehiculos()
lista_clientes = cargar_clientes()

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
    patente = ut.Validar_patente()
    marca = ut.validar_marca()
    modelo = ut.validar_modelo()
    anio = ut.validar_año()
    tipo = ut.validar_tipo()
    

    while True:
        dni = ut.validar_dni()
        dni_clientes = [c["dni"] for c in lista_clientes] #lista por comprensión de todos los dni cargados en el json de clientes
        if dni in lista_clientes: #si encuentra el DNI
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
    lista_vehiculos.append(vehiculo)
    guardar_vehiculos(lista_vehiculos)  
    return lista_vehiculos



def buscar_x_patente(lista_vehiculos):
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

def buscar_x_dni(lista_vehiculos):
    """
    Busca todos los vehículos de un cliente según su DNI.
    Muestra cada vehículo encontrado de manera legible.
    """
    
    try:
       
        dni = ut.validar_dni()
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
    try:
        patente = ut.Validar_patente()


        for vehiculo in lista_vehiculos:
            if vehiculo["patente"] == patente:
                lista_vehiculos.remove(vehiculo)
                print(f"El vehículo con patente {patente} fue eliminado correctamente")
                guardar_vehiculos(lista_vehiculos)  
        else:
            print("No se encontró un vehículo con esa patente")
    
    except ValueError:
        print("Error al eliminar el vehículo")
    


def modificar_vehiculo(lista_vehiculos):
    try:
        patente = ut.Validar_patente()
    
        for vehiculo in lista_vehiculos:
            if vehiculos["patente"] == patente:
                break
        else:
            print("vehículo no encontrado")

        print("Ingrese ENTER para mantener el valor actual")

        nuevo_marca = input(f"Marca actual: {vehiculos['marcas']}: ").strip()
        if nuevo_marca:
            vehiculos["modelo"] = nuevo_marca
        
        nuevo_modelo = input(f"Año (actual: {vehiculos['anio']}): ").strip()
        if nuevo_modelo:
            vehiculos["marca"] = nuevo_modelo
        
        nuevo_anio = ut.validar_año()
        if nuevo_anio:
            vehiculos["anio"] = nuevo_anio
        

        nuevo_tipo = input(f"Tipo (actual: {vehiculo['tipo']}): ").strip()
        if nuevo_tipo:
            vehiculo['tipo'] = nuevo_tipo

        while True:
            nuevo_dni = input(f"DNI (actual: {vehiculo['dni_cliente']}): ").strip()
            if not nuevo_dni:
                break  
            if re.match(ut.validar_dni, nuevo_dni):
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


def menu_vehiculos():
    opciones = ("Salir", "Agregar vehículo", "Buscar vehículo por patente", "Buscar vehículo por DNI", "Eliminar vehículo","Modificar vehículo", "Listar vehículos")
    while True:
        
        ut.mostrar_opciones(opciones)
        opcion = input("Ingrese una de las opciones: ")
        if opcion == "1":
            break

        elif opcion == "2":
            agregar_vehiculo(lista_vehiculos)
        elif opcion == "3":
            buscar_x_patente(lista_vehiculos)
        elif opcion == "4":
            buscar_x_dni(lista_vehiculos)
        elif opcion == "5":
            eliminar_vehiculo(lista_vehiculos)
        elif opcion == "6":
            modificar_vehiculo(lista_vehiculos)
        elif opcion == "7":
            listar_vehiculos(lista_vehiculos)
        else:
            print("opción no válida, intente nuevamente \n")


if __name__ == "__main__":
    menu_vehiculos()