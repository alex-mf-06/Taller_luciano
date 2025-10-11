import os 
import json 
import re 
from datetime import datetime
import clientes as cl 
import utils as ut

script_dir = os.path.dirname(os.path.abspath(__file__))
# Sube un nivel en el directorio para llegar a la raíz del proyecto (Taller_Luciano)
project_root = os.path.dirname(script_dir)
# Construye la ruta completa y correcta al archivo .json
RUTA_empleados = os.path.join(project_root, 'datos', 'empleados.json') 




def modificar_empleado(dni: str, nombre: str = None, puesto: str = None, telefono: str = None, email: str = None) -> bool:
    """
    Pre: 
        - Recibe un dni que debe existir en la lista de empleados.
        - Al menos un dato a modificar debe ser proporcionado.
    Post:
        - Devuelve True si se actualizaron los datos, False si no se encontró al empleado.
    """
    pass


def listar_empleados() -> list[dict]:
    """
    Pre: 
        - No recibe ningún parámetro.
    Post:
        - Devuelve una lista con todos los empleados registrados.
    """
    pass

def menu_empleados() -> None :
    opciones = ["Salir","Agregar Empleado","Modificar empleado","Eliminar empleados","Mostrar empleados"]
    
    while True:
        cl.mostrar_opciones(opciones)
        opcion = input("Ingrese una de las opciones que se les mostro :  \n")
        if opcion == "1":
            break
        elif opcion == "2":
            cl.registrar_clientes(RUTA_empleados)
            
        elif opcion == "3":
            
            dni = ut.validar_dni()
            encontrado = cl.obtener_cliente_por_dni(dni,RUTA_empleados)
            if encontrado : 
                print(f"Cliente encontrado: \n")
                cl.modificar_datos(dni,RUTA_empleados)
                
            else : 
                print("no se encontro el cliente\n")

        elif opcion == "4":
            dni = ut.validar_dni()
            eliminado = cl.eliminar_datos(dni,RUTA_empleados)
            if eliminado:
                print("se ah eliminado la persona correctamente")
            else: 
                print("no se escontro a la persona en nuestro registro")

        elif opcion == "5":
            listas = cl.listar_clientes(RUTA_empleados)
            
            for cliente in listas:
                for clave, valor in cliente.items():
                    print(f"{clave.capitalize()}: {valor}")
                print("-" * 30)
        else : 
            print("opcion invalida ingrese una de las que se les mostro \n")
if __name__ == "__main__":

    menu_empleados()