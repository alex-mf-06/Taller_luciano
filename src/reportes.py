import json 
import os 
import utils as ut
from config import RUTA_GASTOS, RUTA_CLIENTES, RUTA_ORDENES, RUTA_FACTURACION, RUTA_EMPLEADOS

ruta_gastos = RUTA_GASTOS
ruta_ordenes = RUTA_ORDENES
ruta_facturacion = RUTA_FACTURACION
ruta_empleados = RUTA_EMPLEADOS


def gastos_x_categoria(ruta_gastos: str):
    """ 
    Se encarga de hacer un reporte de gastos por categoria con el
    monto y su categoria
    
    Pre: EL archivo JSON debe cumplir lo siguiente:
        . Debe ser un archivo existente
        . Debe contener 'monto' y 'categoria'
    Post: Retorna un resumen de los gastos agrupados por categoria 
    """ 
    lista_gastos = ut.cargar_datos(ruta_gastos)

    if not lista_gastos:
        print("No hay datos cargados para generar el reporte")
        return 
    
    resumen = {}
    total_general = 0

    #El .get() Trabaja de la misma manera que if pero con un solo else
    for gasto in lista_gastos:
    #     if "categoria" in gasto:
    #         categoria = gasto["categoria"]
    #     else:
    #         categoria = gasto["Sin categoria"]
    
    #     print(f"Gasto en: {categoria}")
        try:
            categoria = gasto.get("categoria", "Sin categoria")
            monto = float(gasto.get("monto", 0))
            if categoria in resumen:
                resumen[categoria] += monto
            else:
                resumen[categoria] = monto
            total_general += monto
        except ValueError:
            print(f"El monto '{gasto.get('monto')}'no es un numero") 

    print("--- REPORTE: GASTOS POR CATEGORIA ---")
    print("=====================================")
    for categoria, total in sorted(resumen.items()):
        print(f"{categoria:<25} | ${total:>10,.2f}")
    print("--------------------------------")
    print(f"{'SUMA TOTAL DE GASTOS':<25} | ${total_general:10,.2f}")


def vehiculos_atendidos_x_mes(ruta_ordenes: str):
    """
    Genera un reporte de los vehiculos que se atendieron por mes

    Pre:El archivo JSON debe cumplir lo siguiente:
        . Debe ser un archivo existente
        . Debe contener 'estado' y 'fecha de finalizacion'
    Post: Devuelve la cantidad de ordenes con estado 'finalizada agrupados por meso y año
    """

    lista_ordenes = ut.cargar_datos(ruta_ordenes)

    if not lista_ordenes:
        print("No hay datos en ordenes para gener el reporte.")
        return

    resumen = {}
    total = 0

    for orden in lista_ordenes:
        estado = orden.get("estado")
        f_fin = orden.get("fecha_finalizacion")
        if estado == "Finalizada" and f_fin:
            periodo = ut.obtener_mes_anio(f_fin)
            if periodo in resumen:
                resumen[periodo] += 1
            else:
                resumen[periodo] = 1
            total += 1
    print("--- REPORTE: GASTOS VEHICULOS ATENDIDOS POR MES/AÑO ---")
    print("=======================================================")
    for periodo, cantidad in sorted(resumen.items()):
        print(f"{periodo:<25} | {cantidad:15} vehiculos")
    
    print(f"{'TOTAL GENERAL':<25} | {total:15} vehiculos")


def facturacion_mensual(ruta_facturacion: str):
    """
    Genera un reporte de la facturación total agrupada por mes y año.

    Pre: El archivo JSON debe cumplir lo siguiente:
        . Debe ser un archivo existente 
        . Debe contener 'monto_total' y 'fecha_emision'
    Post: Muestra la suma total de dinero facturado, agrupada por mes/año.
    """
    lista = ut.cargar_datos(ruta_facturacion)

    if not lista:
        print("No hay datos cargados para generar el reporte")
        return

    r_x_mes = {}
    total_general = 0
    for factura in lista:
        try:
            monto = float(factura.get("monto_total", 0.0))
            fecha_emision = factura.get("fecha_emision")
            if fecha_emision:
                periodo = ut.obtener_mes_anio(fecha_emision)
                if periodo in r_x_mes:
                    r_x_mes[periodo] += monto
                else:
                    r_x_mes[periodo] = monto
                total_general += monto
        except ValueError:
            print(f"El monto '{factura.get('monto_total')}' no es numerico")
        except Exception as e:
            print(f"No se puedo procesar la factura: {e}")
    
    print("=== REPORTE: FACTURACION TOTAL POR MES/AÑO ===")
    print("==============================================")
    for periodo, total in sorted(r_x_mes.items()):
        print(f"{periodo:<25} | ${total:15,.2f}")
    
    print(f"{'TOTAL POR MES FACTURADO': <25} | ${total_general:15,.2f}")


def productos_mas_usados(ruta_ordenes: str):
    """
    Genera un reporte que muesyttra los productos mas usados en ordenes de trabajo
    
    Pre: El archivo JSON debe contener lo siguiente:
        . Lista en el campo 'items_usados'
        . Con los campos 'nombre_producto'
        . Y 'cantidad_usada'
    Post: Muestra un listado de total de productos utilizados 
    """

    lista_ordenes = ut.cargar_datos(ruta_ordenes)
    if not lista_ordenes:
        print("No hay datos cargados para logar generar el reporte")
        return

    resumen = {}

    for orden in lista_ordenes:
        items = orden.get("items_usados", [])
        for valor in items:
            try:
                nombre = valor.get("nombre_producto", "Producto Desconocido")
                cantidad = float(valor.get("cantidad_usada", 0))
                if nombre in resumen:
                    resumen[nombre] += cantidad
                else:
                    resumen[nombre] = cantidad
            except ValueError:
                print(f"Cantidad '{valor.get('cantidad_usada')}' no es numerica")
            except Exception as e:
                print(f"No se logro procesar el: {e}")

    print("=== REPORTE: PRODUCTOS MAS USADOR ===")
    print("=====================================")
    ordenados = sorted(resumen.items(), key= lambda valor: valor[1], reverse= True)
    if not ordenados:
        print("No se encontro productos en las ordenes")
        return

    for nombre, cantidad in ordenados:
        print(f"{nombre:<25} | {cantidad:15.0f} unidades") 


def menu_reportes():
    opciones = (
        "Volver al menu principal",
        "Reporte de gastos por categoria",
        "Reporte de vehiculos atendidos por mes",
        "Reporte de facturacion mensual",
        "Reporte de productos mas usados",
    )

    while True:
        print("=== MODULO REPORTES ===")
        ut.mostrar_opciones(opciones)
        opcion = input("Seleccione la opcion deseada: ")
        if opcion == "1":
            break
        elif opcion == "2":
            gastos_x_categoria(ruta_gastos)
        elif opcion == "3": 
            vehiculos_atendidos_x_mes(ruta_ordenes)
        elif opcion == "4":
            facturacion_mensual(ruta_facturacion)
        elif opcion == "5":
            productos_mas_usados(ruta_ordenes)
        else:
            print("Opcion invalida. Vuelva a intentarlo")

if __name__ == "__main__":
    menu_reportes()