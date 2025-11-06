
from typing import List
import re 
import os
import utils as ut

# --- CÁLCULO DE LA RUTA ABSOLUTA Y SEGURA ---
# Obtiene la ruta del directorio donde está el script (la carpeta src)
script_dir = os.path.dirname(os.path.abspath(__file__))
# Sube un nivel en el directorio para llegar a la raíz del proyecto (Taller_Luciano)
project_root = os.path.dirname(script_dir)
# Construye la ruta completa y correcta al archivo clientes.json
RUTA_clientes = os.path.join(project_root, "datos", "clientes.json")



def listar_clientes(RUTA_ARCHIVO) -> list:
    """
    Pre:
        debe recibir un ruta para cargar los datos
    Post:
        - Devuelve una lista de dicts, cada dict representa un cliente.
        - Si no hay clientes, devuelve lista vacía.
    """
    datos = ut.cargar_json(RUTA_ARCHIVO)
    datos = ut.cargar_datos(RUTA_ARCHIVO)
    return datos


def buscar_cliente_por_dni(lista_clientes):
    """
    Usa la función genérica de utils para buscar clientes por DNI.
    """
    ut.buscar_x_dni(lista_clientes, "dni", "clientes")
    
    clientes = ut.cargar_dni_(RUTA_archivo) # Usamos la función que carga el json pero solo los dni 
    if dni in clientes:
        return True 
    return False 

def mostrar_opciones(opciones: tuple) -> None:
    """
    no retorna nada solo muestra un menu de opciones .
    """
    if ut.validar_iterable(opciones):
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i} - {opcion}\n")
    else:
        print("las opciones no se pueden mostrar por que hubo un fallo")


def menu_clientes() -> None:
    opciones = (
        "Salir",
        "Registrar cliente",
        "Modificar datos del cliente",
        "Eliminar cliente",
        "Mostrar clientes ",
    )
def menu_clientes() ->None:
    opciones = ("Salir","Registrar cliente","Modificar datos del cliente","Eliminar cliente","Mostrar clientes ",)
    while True:

        mostrar_opciones(opciones)
        opcion = input("Ingrese una de las opciones: ")
        if opcion == "1":
            break
        elif opcion == "2":
            ut.registrar_datos(RUTA_clientes)

        elif opcion == "3":

            dni = ut.validar_dni()
            encontrado = ut.buscar_x_dni(dni, RUTA_clientes)
            if encontrado:
                print(f"Cliente encontrado: \n")
                ut.modificar_datos(dni,RUTA_clientes)
                
            else : 
                print("no se encontro el cliente\n")

        elif opcion == "4":
            dni = ut.validar_dni()
            eliminado = ut.eliminar_datos(dni,RUTA_clientes)
            if eliminado:
                print("Se ha eliminado la persona correctamente")
            else:
                print("No se escontró a la persona en nuestro registro")

        elif opcion == "5":
            listas = listar_clientes(RUTA_clientes)          
            for cliente in listas:
                for clave, valor in cliente.items():
                    print(f"{clave.capitalize()}: {valor}")
                print("-" * 30)

        else : 
            print("Opción no válida, intente nuevamente.")           


if __name__ == "__main__":
    menu_clientes()
