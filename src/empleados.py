import os
import json
import re
import clientes as cl
import utils as ut
from config import RUTA_EMPLEADOS


def menu_empleados() -> None:
    """Muestra el menú de opciones del módulo de empleados"""
    opciones = [
        "Salir",
        "Agregar Empleado",
        "Modificar empleado",
        "Eliminar empleados",
        "Mostrar empleados",
    ]

    while True:
        cl.mostrar_opciones(opciones)
        opcion = input("Ingrese una de las opciones que se les mostro :  \n")
        if opcion == "1":
            break
        elif opcion == "2":
            ut.registrar_clientes(RUTA_EMPLEADOS)
            
        elif opcion == "3":

            dni = ut.validar_dni()
            encontrado = ut.obtener_cliente_por_dni(dni,RUTA_EMPLEADOS)
            if encontrado : 
                print(f"Cliente encontrado: \n")
                ut.modificar_datos(dni,RUTA_EMPLEADOS)
                
            else : 
                print("no se encontro el cliente\n")

        elif opcion == "4":
            dni = ut.validar_dni()
            eliminado = ut.eliminar_datos(dni,RUTA_EMPLEADOS)
            if eliminado:
                print("se ah eliminado la persona correctamente")
            else:
                print("no se escontro a la persona en nuestro registro")

        elif opcion == "5":
            listas = ut.listar_datos(RUTA_EMPLEADOS)
            
            for cliente in listas:
                for clave, valor in cliente.items():
                    print(f"{clave.capitalize()}: {valor}")
                print("-" * 30)
        else:
            print("opcion invalida ingrese una de las que se les mostro \n")


if __name__ == "__main__":

    menu_empleados()
