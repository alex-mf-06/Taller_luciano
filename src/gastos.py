import json
import utils as ut
import os 
from datetime import datetime

# Se guarda la carpeta donde esta gastos.py
script_dir = os.path.dirname(__file__)

# Sube un nivel para llegar hasta la estructura 
# Asume que 'datos' esta en la raiz 
project_root = os.path.dirname(script_dir)

# Construye la ruta de todo a 'datos.json' dento de la carpeta '   datos'
RUTA_GASTOS = os.path.join(project_root, 'datos', 'gastos.json')


def guardar_gastos(gastos: list):
    """
    Guarda una lista actualiada de gastos en el archivo JSON
    """
    try:
        with open(RUTA_GASTOS, 'w', encoding='utf-8') as archivo:
            json.dump(gastos, archivo,ensure_ascii=False, indent=4)
    
    except FileNotFoundError:
        print("Ups!. Carpeta no existente")
        return []
    except PermissionError:
        print("Este usuario no tiene permiso de guardar el archivo")
        return []
    except TypeError:
        print("Ups!. El dato no es serializable")
        return []
    except Exception as e:
        print(f"Ocuriio un error inesperado {e}")
        return []


def registrar_gasto():
    """
    Registra un nuevo gasto en el archivo JSON
    """
    gastos = ut.cargar_datos(RUTA_GASTOS)

    if gastos:  
        nuevo_id = max(gasto['id'] for gasto in gastos) + 1
    else:
        nuevo_id = 1   
    fecha = ut.validar_fecha()
    monto = ut.validar_monto()
    categoria = ut.validar_categoria()

    n_gasto = {
        "id" : nuevo_id,
        "fecha" : fecha,
        "monto" : monto,
        "categoria" : categoria
    }
    gastos.append(n_gasto)
    ut.actualizar_datos(gastos, RUTA_GASTOS)
    print("El gasto de guardo con exito.")
    return n_gasto


def mostrar_gasto(gasto):
    print("\n --- DETALLE DEL GASTO REGISTRADO ---")
    for clave, valor in gasto.items():
        print(f"{clave.capitalize()}: {valor}")


def listar_gasto():
    """
    Lista todos los gastos registrados de manera legibile.
    """

    gastos = ut.cargar_gastos()
    if not gastos:
        print("No hay registro de gastos disponibles")
        return[]
    print("\n--- LISTA DE GASTOS ---\n")
    for gasto in gastos:
        id_gasto = gasto.get("id", 0)
        fecha = gasto.get("fecha", "N/A")
        categoria = gasto.get("categoria", "N/A")
        monto = gasto.get("monto", 0.0)
        descripcion = gasto.get("descripcion", "N/A")
        
        print(f"{id_gasto} | {fecha} | {categoria} | ${monto:,.2f} | {descripcion}")


def menu_gastos():
    opciones = ("Registrar gasto", "Listar gasto", "Volver al menú principal")
    
    while True:
        print("\n--- MENU DE GASTOS ---")
        ut.mostrar_opciones(opciones)
        try:
            opcion = int(input("Ingrese la opcion deseada (1-3): "))

            if opcion not in [1,2,3]:
                raise ValueError("Opcion fuera de rango")

            print(f"Elegiste la opcion {opcion}")
            info = {"opcion elegida": opciones[(opcion)-1]}
            if ut.confirmar_informacion(info):
                if opcion == 1:
                    registrar_gasto()
                elif opcion == 2:
                    listar_gasto()
                elif opcion == 3:
                    print("Volviendo al menu principal")
                    break
                else:
                    print("Opcion no disponible")
        except ValueError:
            print("Caracter no valido")
        except TypeError:
            print("Tipo de dato no compatible. Vuelva a intentarlo")
        except KeyboardInterrupt:
            print("Comando no valido")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")



if __name__ == "__main__":
    menu_gastos()
