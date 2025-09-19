# reportes.py
# Módulo para gestionar reportes del taller

def menu_reportes():
    while True:
        print("\n=== Módulo Reportes ===")
        print("1. Reporte de sueldos de empleados")
        print("2. Cantidad de paños de pintura pintados por mes")
        print("3. Días de chapa por vehículo")
        print("4. Productos más usados")
        print("5. Vehículos atendidos por mes")
        print("6. Consumo de materiales por orden")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            reporte_sueldos_empleados()
        elif opcion == "2":
            reporte_panos_pintura()
        elif opcion == "3":
            reporte_dias_chapa()
        elif opcion == "4":
            reporte_productos_mas_usados()
        elif opcion == "5":
            reporte_vehiculos_atendidos()
        elif opcion == "6":
            reporte_consumo_materiales()
        elif opcion == "0":
            break
        else:
            print("Opción inválida, intente nuevamente.")

# -------------------------------------------------
# Funciones de cada reporte con pre y post cond.
# -------------------------------------------------

def reporte_sueldos_empleados():
    """
    Pre: Se tiene una lista de empleados y su información salarial.
    Post: Muestra los sueldos de cada empleado filtrados por mes o período.
    """
    pass

def reporte_panos_pintura():
    """
    Pre: Se tiene registro de las órdenes de pintura realizadas.
    Post: Muestra la cantidad de paños de pintura pintados por mes, por vehículo o tipo de pintura.
    """
    pass

def reporte_dias_chapa():
    """
    Pre: Se tienen registros de ingreso y salida de vehículos en chapa.
    Post: Calcula y muestra la cantidad de días que cada vehículo pasó en chapa.
    """
    pass

def reporte_productos_mas_usados():
    """
    Pre: Se tiene registro del consumo de productos por orden.
    Post: Muestra los productos más utilizados por período.
    """
    pass

def reporte_vehiculos_atendidos():
    """
    Pre: Se tienen registros de las órdenes completadas.
    Post: Muestra la cantidad de vehículos atendidos por mes.
    """
    pass

def reporte_consumo_materiales():
    """
    Pre: Se tiene registro del uso de materiales por orden.
    Post: Muestra la cantidad de productos usados por orden de trabajo.
    """
    pass
