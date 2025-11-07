import sys
import facturacion as fac
import reportes
import clientes as cl
import vehiculos_reestructurado as vh
import ordenes as ot
import empleados as emp
import gastos as gs


def main():
    menu_principal = (
    "=== SISTEMA DE GESTIÓN DEL TALLER ===",
    "1. Gestión de clientes",
    "2. Gestión de vehículos",
    "3. Órdenes de trabajo",
    "4. Empleados",
    "5. Facturación",
    "6. Reportes",
    "7. Gastos",
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
            fac.menu_facturacion()
        elif opcion == "6":
            reportes.menu_reportes()
        elif opcion == "7":
            gs.menu_gastos()
        elif opcion == "0":
            print("Saliendo del sistema...")
            sys.exit()
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()

