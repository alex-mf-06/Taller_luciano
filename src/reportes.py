import json 
import os 
import utils as ut

ruta_gastos = os.path.join("datos", "gastos.json")
ruta_ordenes = os.path.join("datos", "ordenes.json")
ruta_facturacion = os.path.join("datos", "facturacion.json")
ruta_empleados = os.path.join("datos", "empleados.json")

def cargar_datos(r_archivo: str) -> list:
    """
    Se encarga de cargar los datos de un archivo JSON
    Devuelve una lista vacia [] si:
        . El archivo no exite
        . El archivo se encuentra vacio
    """

    if not os.path.exists(r_archivo): # verifica si existe el archivo
        return []
    
    try:
        with open(r_archivo, 'r', encoding= 'utf-8') as hoja:
            datos = json.load(hoja)
            if isinstance(datos, list):
                return datos
            else:
                return []
                
    except json.JSONDecodeError: #rotos o invalidos
        return []
    except Exception: # cualquier otro error
        return []


def gatos_x_categoria(ruta_gastos: str):
    """
    Se encarga de hacer un reporte de gastos por categoria con el
    monto y su categoria
    
    Pre: EL archivo JSON debe cumplir lo siguiente:
        . Debe ser un archivo existente
        . Debe contener 'monto' y 'categoria'
    Post: Retorna un resumen de los gastos agrupados por categoria 
    """ 
    lista_gastos = cargar_datos(ruta_gastos)

    if not lista_gastos:
        print("No hay datos cargados para generar el reporte")
        return 
    
    resumen = {}
    total = 0

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
        except ValueError:
            print(f"El monto '{gasto.get('monto')}'no es un numero") 

    print("--- REPORTE: GASTOS POR CATEGORIA ---")
    print("=====================================")
    for categoria, total in sorted(resumen.items()):
        print(f"{categoria:<25} | ${total:>10,.2f}")
    print("--------------------------------")
    print(f"{'SUMA TOTAL DE GASTOS':<25} | ${total:10,.2f}")


def vehiculos_atendidos_x_mes(ruta_ordenes: str):
    """
    Genera un reporte de los vehiculos que se atendieron por mes

    Pre:El archivo JSON debe cumplir lo siguiente:
        . Debe ser un archivo existente
        . Debe contener 'estado' y 'fecha de finalizacion'
    Post: Devuelve la cantidad de ordenes con estado 'finalizada agrupados por meso y año
    """

    lista_ordenes = cargar_datos(ruta_datos)

    if not lista_ordenes:
        print("No hay datos en ordenes para gener el reporte.")
        return

    resumen = {}
    total = 0

    for orden in lista_ordenes:
        estado = orden.get("estado")
        f_fin = orden.get("Fecha_finalizacion")
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

