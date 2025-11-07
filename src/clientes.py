
from typing import List, Dict
import os
import utils as ut
from config import RUTA_CLIENTES






def menu_clientes() ->None:
    """
    Esta función muestra un menú para gestionar clientes, permitiendo registrar, modificar, eliminar y mostrar clientes.
    
    """
    try : 
        opciones = ("Salir","Registrar cliente","Modificar datos del cliente","Eliminar cliente","Mostrar clientes ",)
        while True:

            ut.opciones_menu("CLIENTES", opciones)
            opcion = input("Ingrese una de las opciones: ")
            if opcion == "1":
                break
            elif opcion == "2":
                ut.registrar_datos(RUTA_CLIENTES)

            elif opcion == "3":

                dni = ut.validar_dni()
                encontrado = ut.buscar_x_dni(dni, RUTA_CLIENTES)
                if encontrado:
                    print(f"Cliente encontrado: \n")
                    ut.modificar_datos(dni,RUTA_CLIENTES)
                    
                else : 
                    print("no se encontro el cliente\n")

            elif opcion == "4":
                dni = ut.validar_dni()
                eliminado = ut.eliminar_datos(dni,RUTA_CLIENTES)
                if eliminado:
                    print("Se ha eliminado la persona correctamente")
                else:
                    print("No se escontró a la persona en nuestro registro")

            elif opcion == "5":
                listas = ut.cargar_datos(RUTA_CLIENTES)
                ut.mostrar_info_diccionario(listas)

            else : 
                print("Opción no válida, intente nuevamente.")     
    except KeyboardInterrupt:
        print("\nSaliendo del menú de clientes...")      
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")


if __name__ == "__main__":
    
    menu_clientes()
