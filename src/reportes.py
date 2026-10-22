import json 
import os 
import utils as ut
from config import RUTA_GASTOS, RUTA_CLIENTES, RUTA_ORDENES, RUTA_FACTURACION, RUTA_EMPLEADOS
from datetime import datetime
from typing import List,Dict
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


def solicitar_fecha(mensaje: str) -> datetime:
    """
    Solicita al usuario una fecha por teclado y valida su formato y coherencia.

    Pre:
        - Recibe un mensaje (str) para mostrar al usuario.
    
    Post:
        - Devuelve un objeto datetime válido (con hora 00:00:00).
        - Garantiza que la fecha no sea futura (mayor a la fecha actual).
        - Garantiza que la fecha exista en el calendario (ej: no permite 30 de febrero).
    """
    while True:
        fecha_str = input(mensaje)
        try:
            # Intentamos convertir el string. Esto valida formato y existencia real de la fecha.
            fecha_dt = datetime.strptime(fecha_str, "%Y-%m-%d")
            
            # Validamos que no sea una fecha futura
            if fecha_dt > datetime.now():
                print("❌ Error: La fecha no puede ser posterior al día de hoy.")
                continue 
            
            return fecha_dt

        except ValueError:
            print("❌ Error: Formato incorrecto o fecha inexistente. Use AAAA-MM-DD (ej: 2024-05-20).")

def generar_reporte_por_rango(ruta_ordenes: str) -> None:
    """
    Muestra las órdenes FINALIZADAS comprendidas en un rango de fechas definido por el usuario.

    Pre:
        - 'ruta_ordenes' debe ser una ruta válida a un archivo JSON existente.
        - El JSON debe contener una lista de diccionarios con las claves:
          'estado', 'fecha_de_creacion' (o fecha_finalizacion), 'id', 'patente', 'costo_estimado'.
        - El formato de fecha en el JSON debe ser "AAAA-MM-DD HH:MM:SS" o "AAAA-MM-DD".

    Post:
        - Solicita al usuario fecha de inicio y fin.
        - Imprime en pantalla una tabla con las órdenes que cumplan:
          1. Estado es "FINALIZADA".
          2. La fecha está dentro del rango (inclusive).
        - Muestra el total de vehículos encontrados o un mensaje si no hay datos.
    """
    
    # 1. Carga de datos
    ordenes = ut.cargar_datos(ruta_ordenes)

    # 2. Solicitar fechas con la función auxiliar
    print("\n--- FILTRO DE ÓRDENES FINALIZADAS ---")
    fecha_inicio = solicitar_fecha("Ingrese fecha de inicio (AAAA-MM-DD): ")
    fecha_fin = solicitar_fecha("Ingrese fecha de fin    (AAAA-MM-DD): ")

    # 3. Validar coherencia del rango
    if fecha_inicio > fecha_fin:
        print("\n❌ Error Lógico: La fecha de inicio es mayor a la fecha de fin.")
        return

    print(f"\nBuscando reportes desde {fecha_inicio.date()} hasta {fecha_fin.date()}...")
    print("=" * 80)
    print("{:<5} {:<15} {:<15} {:<25} {:<12}".format("ID", "FECHA", "PATENTE", "DESCRIPCIÓN", "COSTO"))
    print("-" * 80)

    cantidad_encontrada = 0

    for orden in ordenes:
        # Usamos .get() para evitar errores si falta una clave
        estado = orden.get("estado", "")
        
        # NOTA: Aquí uso 'fecha_de_creacion' basado en tu JSON. 
        # Si agregas 'fecha_finalizacion' al JSON, cambia esta clave.
        fecha_str_completa = orden.get("fecha_de_creacion", "") 

        if estado == "FINALIZADA" and fecha_str_completa:
            try:
                # El JSON viene con hora "2025-11-08 23:11:35", hacemos split para quedarnos con la fecha
                fecha_solo_dia = fecha_str_completa.split(" ")[0]
                fecha_orden_dt = datetime.strptime(fecha_solo_dia, "%Y-%m-%d")

                # Comparamos si está dentro del rango (inclusive)
                if fecha_inicio <= fecha_orden_dt and fecha_orden_dt <= fecha_fin:
                    
                    costo = f"${orden.get('costo_estimado', 0):.2f}"
                    
                    print("{:<5} {:<15} {:<15} {:<25} {:<12}".format(
                        orden.get("id"),
                        fecha_solo_dia,
                        orden.get("patente", "S/P"),
                        orden.get("descripcion", "")[:22] + "...", # Recorta descripciones largas
                        costo
                    ))
                    cantidad_encontrada += 1

            except ValueError:
                # Si una fecha en el JSON está mal formateada, la saltamos pero no rompemos el programa
                continue

    print("=" * 80)
    if cantidad_encontrada == 0:
        print("No se encontraron vehículos finalizados en ese rango de fechas.")
    else:
        print(f"TOTAL VEHÍCULOS ENCONTRADOS: {cantidad_encontrada}")

# Ejemplo de uso:
# generar_reporte_por_rango("ordenes.json")
def facturacion_por_rangos(ruta_facturacion: str) ->None:
    """
    Genera un reporte de la facturación total agrupada por mes y año.

    Pre: El archivo JSON debe cumplir lo siguiente:
        . Debe ser un archivo existente 
        . Debe contener 'monto_total' y 'fecha_emision'
    Post: Muestra la suma total de dinero facturado, agrupada por mes/año.
    """
    lista_facturas = ut.cargar_datos(ruta_facturacion)

    if not lista_facturas:
        print("No hay datos cargados para generar el reporte")
        return

    print("\n--- REPORTE DE FACTURACION POR RANGO DE FECHAS ---")
    Fecha_inicio = solicitar_fecha("Ingrese fecha de inicio (AAAA-MM-DD): ")
    fecha_fin = solicitar_fecha("Ingrese fecha de fin    (AAAA-MM-DD): ")
    if Fecha_inicio > fecha_fin:
        print( "La fecha de inicio no puede ser mayor a la fecha de fin.")
        return
    
    total_rango = 0
    cantidad_facturas = 0

    print("\n" + "="*60)
    print(f"FACTURACIÓN DEL {Fecha_inicio.date()} AL {fecha_fin.date()}")
    print("="*60)
    print("{:<10} {:<20} {:<15}".format("ID", "FECHA EMISIÓN", "MONTO"))
    print("-" * 60)

    for factura in lista_facturas:
        fecha_str = factura.get("fecha_emision")
        monto = factura.get("monto_total")

        if fecha_str and monto is not None:
            try:
                # Limpiamos la fecha (quitamos la hora si existe) para comparar
                # Ejemplo: "2025-11-08 15:30:00" -> "2025-11-08"
                fecha_solo_dia = fecha_str.split(" ")[0]
                fecha_dt = datetime.strptime(fecha_solo_dia, "%Y-%m-%d")

                # 2. Lógica de filtrado: ¿Está la fecha dentro del rango?
                if Fecha_inicio <= fecha_dt and fecha_dt <= fecha_fin:
                    monto_float = float(monto)
                    total_rango += monto_float
                    cantidad_facturas += 1

                    # Mostramos la linea
                    print("{:<10} {:<20} ${:<15,.2f}".format(
                        factura.get("id", "N/A"), 
                        fecha_solo_dia, 
                        monto_float
                    ))

            except ValueError:
                continue # Si la fecha o el monto están mal, saltamos esta factura

    print("=" * 60)
    if cantidad_facturas > 0:
        print(f"CANTIDAD DE FACTURAS: {cantidad_facturas}")
        print(f"TOTAL RECAUDADO:      ${total_rango:,.2f}")
    else:
        print("No se encontraron facturas en este rango de fechas.")


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
        "Reporte de vehiculos atendidos por el rango que desees de fecha",
        "Reporte de facturacion por fecha ingresada por el usuario",
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
            generar_reporte_por_rango(ruta_ordenes)
        elif opcion == "4":
            facturacion_por_rangos(ruta_facturacion)
        elif opcion == "5":
            productos_mas_usados(ruta_ordenes)
        else:
            print("Opcion invalida. Vuelva a intentarlo")
#aca esta mal algo 
if __name__ == "__main__":
    menu_reportes()