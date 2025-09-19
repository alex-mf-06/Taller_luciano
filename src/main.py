import sys

import clientes
import vehiculos
import ordenes
import empleados
import facturacion
import stock
import reportes
import stock



def mostrar_menu():
    print("\n=== SISTEMA DE GESTIÓN DEL TALLER ===")
    print("1. Gestión de clientes")
    print("2. Gestión de vehículos")
    print("3. Órdenes de trabajo")
    print("4. Empleados")
    print("5. Facturación")
    print("6. Stock")
    print("7. Reportes")
    print("8. Compras")
    print("9. Pagos")
    print("10. Gastos")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clientes.menu_clientes()
        elif opcion == "2":
            vehiculos.menu_vehiculos()
        elif opcion == "3":
            ordenes.menu_ordenes()
        elif opcion == "4":
            empleados.menu_empleados()
        elif opcion == "5":
            facturacion.menu_facturacion()
        elif opcion == "6":
            stock.menu_stock()
        elif opcion == "7":
            reportes.menu_reportes()
        elif opcion == "8":
            compras.menu_compras()
        elif opcion == "9":
            pagos.menu_pagos()
        elif opcion == "10":
            gastos.menu_gastos()
        elif opcion == "0":
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
