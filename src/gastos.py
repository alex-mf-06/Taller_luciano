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


def cargar_gastos():
    """
    """
    
    if not os.path.exists(RUTA_GASTOS):
        print("El archvio no existe. Se creara uno nuevo")
        return []   
    
    try:
        with open(RUTA_GASTOS, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Ups!. Archivo vacio")
        return []
    except FileNotFoundError:
        print("Ups. Archivo no encontrado")
        return []

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
    gastos = cargar_gastos()

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
    guardar_gastos(gastos)
    print("El gasto de guardo con exito.")
    return n_gasto


def mostrar_gasto(gasto):
    print("\n --- DETALLE DEL GASTO REGISTRADO ---")
    for clave, valor in gasto.items():
        print(f"{clave.capitalize()}: {valor}")

mostrar_gasto(n_gasto)

def listar_gasto():
    pass

def menu_gastos():
    pass
