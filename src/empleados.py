import os
import json
import re
import clientes as cl
import utils as ut
from config import RUTA_EMPLEADOS


def menu_empleados() -> None:
    """Muestra el menú de opciones del módulo de empleados
    
    """
    try:
        opciones = (
            "Salir",
            "Registrar empleado",
            "Modificar empleado",
            "Eliminar empleado",
            "Mostrar empleados",
            "Mostrar empleado por DNI"
        )


        while True:
            ut.opciones_menu("EMPLEADOS", opciones)
            opcion = input("Seleccione una opción: ").strip()
            if opcion == "1":
                break
            elif opcion == "2":
                ut.registrar_datos(RUTA_EMPLEADOS)
                
            elif opcion == "3":

                dni = ut.validar_dni()
                encontrado = ut.buscar_x_dni(dni,RUTA_EMPLEADOS)
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
                listas = ut.cargar_datos(RUTA_EMPLEADOS)
                
                ut.mostrar_info_diccionario(listas)
            elif opcion == "6":
                ut.mostrar_persona_x_dni(RUTA_EMPLEADOS)
            else:
                print("opcion invalida ingrese una de las que se les mostro \n")
    except KeyboardInterrupt:
        print("\nSaliendo del menú de empleados...")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")




if __name__ == "__main__":

    menu_empleados()
