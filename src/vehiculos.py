import os  
import clientes as cl 
import utils as ut 
# import json  # Para después conectar con archivo de datos

def menu_vehiculos():
    while True:
        opciones= (
        "\n=== Módulo Vehículos ===",
        "1. Gestionar vehículo (agregar, modificar, eliminar)",
        "2. Buscar / Listar vehículos",
        "3. Resumen del vehículo",
        "0. Volver al menú principal")
        ut.mostrar_opciones(opciones)
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_vehiculo()
        elif opcion == "2":
            buscar_listar_vehiculos()
        elif opcion == "3":
            resumen_vehiculo()
        elif opcion == "0":
            break
        else:
            print("Opción inválida, intente nuevamente.")

# ---------------------------------------------
# Funciones internas del módulo Vehículos
# ---------------------------------------------

def gestionar_vehiculo():
    while True:
        opciones = (
        "\n--- Gestionar Vehículo ---",
        "1. Agregar vehículo","2. Modificar vehículo",
        "3. Eliminar vehículo","0. Volver al menú anterior")
        ut.mostrar_opciones(opciones) 

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Función para agregar vehículo (pendiente de implementar)")
        elif opcion == "2":
            print("Función para modificar vehículo (pendiente de implementar)")
        elif opcion == "3":
            print("Función para eliminar vehículo (pendiente de implementar)")
        elif opcion == "0":
            break
        else:
            print("Opción inválida, intente nuevamente.")

def buscar_listar_vehiculos():
    while True:
        opciones = (
        "\n--- Buscar / Listar Vehículos ---",
        "1. Listar todos los vehículos activos","2. Buscar vehículo por patente",
        "3. Buscar vehículo por cliente", "0. Volver al menú anterior")
        ut.mostrar_opciones(opciones)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Función para listar vehículos (pendiente de implementar)")
        elif opcion == "2":
            print("Función para buscar por patente (pendiente de implementar)")
        elif opcion == "3":
            print("Función para buscar por cliente (pendiente de implementar)")
        elif opcion == "0":
            break
        else:
            print("Opción inválida, intente nuevamente.")

def resumen_vehiculo():
    patente = input("\nIngrese la patente del vehículo para ver resumen: ")
    print(f"Mostrando resumen del vehículo {patente} (pendiente de implementar)")


def menu_vehiculos():
    
    while True:
        opciones = (
        "\n=== Módulo Vehículos ===","1. Gestionar vehículo (agregar, modificar, eliminar)","2. Buscar / Listar vehículos",
        "3. Resumen del vehículo","0. Volver al menú principal")
        ut.mostrar_opciones(opciones)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_vehiculo()
        elif opcion == "2":
            buscar_listar_vehiculos()
        elif opcion == "3":
            resumen_vehiculo()
        elif opcion == "0":
            break
        else:
            print("Opción inválida, intente nuevamente.")

# ---------------------------------------------
# Funciones internas del módulo Vehículos
# ---------------------------------------------


def buscar_listar_vehiculos():
    while True:
        opciones =(
        "\n--- Buscar / Listar Vehículos ---","1. Listar todos los vehículos activos",
        "2. Buscar vehículo por patente","3. Buscar vehículo por cliente","0. Volver al menú anterior"
        )
        ut.mostrar_opciones(opciones)
        

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Función para listar vehículos (pendiente de implementar)")
        elif opcion == "2":
            print("Función para buscar por patente (pendiente de implementar)")
        elif opcion == "3":
            print("Función para buscar por cliente (pendiente de implementar)")
        elif opcion == "0":
            break
        else:
            print("Opción inválida, intente nuevamente.")

def resumen_vehiculo():
    patente = input("\nIngrese la patente del vehículo para ver resumen: ")
    print(f"Mostrando resumen del vehículo {patente} (pendiente de implementar)")
    # Aca mostrarían:
    # datos del vehículo (marca, modelo, tipo)
    # cliente asociado
    # total de órdenes realizadas
    # última fecha de trabajo
    # notas internas
menu_vehiculos()