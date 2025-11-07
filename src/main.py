import sys
import facturacion
import reportes

import clientes as cl
import vehiculos_reestructurado as vh
import ordenes as ot
import empleados as emp
import facturacion as fa
import reportes as rep
import gastos as gs


menu = {
    "1": ("Gestión de clientes", cl.menu_clientes),
    "2": ("Gestión de vehículos", vh.menu_vehiculos),
    "3": ("Órdenes de trabajo", ot.menu_ordenes),
    "4": ("Empleados", emp.menu_empleados),
    "5": ("Facturación", fa.menu_facturacion),
    "6": ("Reportes", rep.menu_reportes),
    "0": ("Salir", lambda: sys.exit())
}


def main():
    menu_principal = (
        "=== SISTEMA DE GESTIÓN DEL TALLER ===",
        "1. Gestión de clientes",
        "2. Gestión de vehículos",
        "3. Órdenes de trabajo",
        "4. Empleados",
        "5. Facturación",
        "6. Reportes",
        "7. Compras",
        "8. Gastos",
        "0. Salir"
    )

    while True:
        print("\n=== SISTEMA DE GESTIÓN DEL TALLER ===")
        print()
        for opcion in menu_principal:
            print(opcion)

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cl.menu_clientes()
        elif opcion == "2":
            vh.menu_vehiculos()
        elif opcion == "3":
            ot.menu_ordenes()
        elif opcion == "4":
            emp.menu_empleados()
        elif opcion == "5":
            fa.menu_facturacion()
        elif opcion == "6":
            rep.menu_reportes()
        elif opcion == "7":
            rep.menu_reportes()
        elif opcion == "8":
            gs.menu_gastos()
        elif opcion == "0":
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()


def mostrar_menu():
    for key, valor in sorted(menu.items()):
        print(f"{key}. {valor[0]}")
    opcion = input("Seleccione una opción: ")
    if opcion in menu and menu[opcion][1]:
        menu[opcion][1]()
    else:
        print("Opción inválida o no implementada")
