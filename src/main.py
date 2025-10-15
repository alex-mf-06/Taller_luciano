
import sys
import facturacion
import stock
import reportes
import clientes as cl
import vehiculos as vh
import ordenes as ot
import empleados as emp


menu = {
    "1": {"descripcion": "Gestión de clientes", "funcion": cl},
    "2": {"descripcion": "Gestión de vehículos", "funcion": vh},
    "3": {"descripcion": "Órdenes de trabajo", "funcion": ot},
    "4": {"descripcion": "Empleados", "funcion": emp},  
    "0": {"descripcion": "Salir", "funcion": exit}
}


def main():
    menu_principal = (
    "=== SISTEMA DE GESTIÓN DEL TALLER ===",
    "1. Gestión de clientes",
    "2. Gestión de vehículos",
    "3. Órdenes de trabajo",
    "4. Empleados",
    "5. Facturación",
    "6. Stock",
    "7. Reportes",
    "8. Compras",
    "9. Pagos",
    "10. Gastos",
    "0. Salir"
)
    while True:
        
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
            facturacion.menu_facturacion()
        elif opcion == "6":
            stock.menu_stock()
        elif opcion == "7":
            reportes.menu_reportes()
        elif opcion == "8":
            #compras.menu_compras()
            pass
        elif opcion == "9":
            #pagos.menu_pagos()
            pass
        elif opcion == "10":
            pass
            #gastos.menu_gastos()
        elif opcion == "0":
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()

def mostrar_menu():
    for key, valor in sorted(menu.items()):
        print(f"{key}. {valor['descripcion']}")
    opcion = input("Seleccione una opción: ")
    if opcion in menu and menu[opcion]["funcion"]:
        menu[opcion]["funcion"]()
    else:
        print("Opción inválida o no implementada")

