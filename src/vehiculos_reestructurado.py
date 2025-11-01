from typing import List
from datetime import datetime
import json
import os
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
        if dni in lista_clientes: 
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
    ut.guardar_json(lista_vehiculos,RUTA_VEHICULOS) 
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

def buscar_vehiculos_por_dni(lista_vehiculos):
    """
    Usa la función genérica de utils para buscar vehículos por DNI.
    """
    ut.mostrar_x_dni(lista_vehiculos, "dni_cliente", "vehículos")


def eliminar_vehiculo(lista_vehiculos):
    try:
        patente = ut.Validar_patente()


        for vehiculo in lista_vehiculos:
            if vehiculo["patente"] == patente:
                lista_vehiculos.remove(vehiculo)
                print(f"El vehículo con patente {patente} fue eliminado correctamente")
                ut.guardar_json(lista_vehiculos,RUTA_VEHICULOS)  
        else:
            print("No se encontró un vehículo con esa patente")
    
    except ValueError:
        print("Error al eliminar el vehículo")
    


def modificar_vehiculo(lista_vehiculos):
    try:
        patente = ut.Validar_patente()
    
        for vehiculo in lista_vehiculos:
            if vehiculo["patente"] == patente:
                break
        else:
            print("vehículo no encontrado")

        print("Ingrese ENTER para mantener el valor actual")

        nuevo_marca = input(f"Marca actual: {vehiculo['marcas']}: ").strip()
        if nuevo_marca:
            vehiculo["modelo"] = nuevo_marca
        
        nuevo_modelo = input(f"Año (actual: {vehiculo['anio']}): ").strip()
        if nuevo_modelo:
            vehiculo["marca"] = nuevo_modelo
        
        nuevo_anio = ut.validar_año()
        if nuevo_anio:
            vehiculo["anio"] = nuevo_anio
        

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

        ut.guardar_json(lista_vehiculos,RUTA_VEHICULOS)
        print("Vehículo modificado correctamente.")

    except KeyError:
        print("Estructura de datos inesperada: falta alguna clave.")
        

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
            ut.buscar_x_dni(lista_vehiculos)
        elif opcion == "5":
            eliminar_vehiculo(lista_vehiculos)
        elif opcion == "6":
            modificar_vehiculo(lista_vehiculos)
        elif opcion == "7":
            ut.listar_datos(lista_vehiculos,"vehiculos")
        else:
            print("opción no válida, intente nuevamente \n")


if __name__ == "__main__":
    menu_vehiculos()