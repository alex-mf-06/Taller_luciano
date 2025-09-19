import json 
import os 
from datetime import datetime

archivos_ordenes = "ordenes.json"
if os.path.exists(archivos_ordenes): # si el archivo existe
    with open(archivos_ordenes,"r",encoding="utf-8") as file: # abrir el archivo
        ordenes = json.load(file) # cargar el archivo
else:
    ordenes = [] # lista vacia
def guardar_ordenes():
    """
    Guarda las ordenes en un archivo json
    """
    pass
def crear_orden():

    pass   

def mostrar_ordenes():
    """
    Muestra todas las ordenes
    """
    pass