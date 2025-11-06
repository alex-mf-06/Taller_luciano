import sys

import clientes as cl
import vehiculos_reestructurado as vh
import ordenes as ot
import empleados as emp
import facturacion as fa


menu = {
    "1": ("Gestión de clientes", cl.menu_clientes),
    "2": ("Gestión de vehículos", vh.menu_vehiculos),
    "3": ("Órdenes de trabajo", ot.menu_ordenes),
    "4": ("Empleados", emp.menu_empleados),
    "5": ("Facturación", fa.menu_facturacion),
    "0": ("Salir", lambda: sys.exit())
}


def main():
    """
    Muestra el menú principal del sistema.
    """

    while True:
        print("\n=== SISTEMA DE GESTIÓN DEL TALLER ===")

        # Mostrar todas las opciones del diccionario
        for key, (descripcion, _) in sorted(menu.items()):
            print(f"{key}. {descripcion}")

        opcion = input("Seleccione una opción: ")

        #  Validar la opción ingresada
        if opcion in menu:
            _, funcion = menu[opcion]
            try:
                funcion()  # Ejecutar la función correspondiente
            except Exception as e:
                print(f"Error al ejecutar la opción: {e}")
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
