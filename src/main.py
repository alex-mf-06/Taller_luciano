import sys
import facturacion as fac
import reportes
import clientes as cl
import vehiculos_reestructurado as vh
import ordenes as ot
import empleados as emp
import gastos as gs
import utils as ut


def main():
    menu_principal = (
    " Gestión de clientes",
    " Gestión de vehículos",
    " Órdenes de trabajo",
    " Empleados",
    " Facturación",
    " Reportes",
    " Gastos",
    " Salir"
)
    while True:
        try: 
            ut.opciones_menu("=== SISTEMA DE GESTIÓN DEL TALLER ===",menu_principal)
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
            elif opcion == "8":
                print("Saliendo del sistema...")
                sys.exit()
            else:
                print("Opción no válida, intente de nuevo.")
        except KeyboardInterrupt:
            print("Saliendo del sistema...")
            return


if __name__ == "__main__":
    main()

