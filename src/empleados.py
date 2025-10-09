import os 
import json 
import re 
from datetime import datetime
import clientes as cl 

script_dir = os.path.dirname(os.path.abspath(__file__))
# Sube un nivel en el directorio para llegar a la raíz del proyecto (Taller_Luciano)
project_root = os.path.dirname(script_dir)
# Construye la ruta completa y correcta al archivo .json
RUTA_empleados = os.path.join(project_root, 'datos', 'empleados.json') 


def registar_empleado( ) -> None:
    """
    permite agregar y guardar los datos en un archivo JSON.

    Precondiciones:
        - El usuario debe ingresar correctamente los siguientes datos:
            * DNI: numérico, de 7 u 8 dígitos.
            * Nombre: no vacío.
            * Teléfono: de 7 a 15 dígitos (puede comenzar con '+').
            * Email: formato válido (opcional, puede dejarse vacío).
        - El archivo 'clientes.json' puede existir o no.
    
    Postcondiciones:
        - Si el archivo no existe, se crea automáticamente.
        - Si el archivo existe, se actualiza agregando el nuevo cliente.
        - Si el DNI ya está registrado, no se agrega un nuevo cliente.
        - Los datos se almacenan en formato JSON con indentación y codificación UTF-8.
        - Se imprime un mensaje informando el resultado de la operación.
    """

    
    #Expreciones regulares para validar los campos
    regex_dni = re.compile(r'^\d{7,8}$')
    regex_telefono = re.compile(r'^\+?\d{7,15}$')
    regex_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    #solicitud de datos
    while True:
        dni = input("Ingrese el DNI del cliente (7 u 8 dígitos): ").strip() # Eliminar espacios en blanco al inicio y final
        if regex_dni.match(dni): # Validar el formato del DNI
            if cl.confirmar_dato("DNI", dni):
                break # Si el usuario confirma el DNI, salir del bucle principal
        else:
            print("DNI inválido. Debe contener solo números y tener entre 7 y 8 dígitos.")

    while True:
        nombre = input("Ingrese el nombre del cliente: ")
        if nombre.strip():
            if cl.confirmar_dato("nombre", nombre):
                break # Si el usuario confirma el nombre, salir del bucle principal
                
        else:
            print("Nombre inválido. No puede estar vacío.")

    while True:
        telefono = input("Ingrese el teléfono del cliente (7 a 15 dígitos): ")
        if regex_telefono.match(telefono):
            if cl.confirmar_dato("teléfono", telefono):
                break # Si el usuario confirma el teléfono, salir del bucle principal
        else:
            print("Teléfono inválido. Debe contener solo números y tener entre 7 y 15 dígitos.")

    while True:
        email = input("Ingrese el email del cliente : ")
        if not email or regex_email.match(email) :
            if cl.confirmar_dato("email", email if email else "sin email"): # llama la funcion para confirmar datos tanto si existe ek email o no 
                break # Si el usuario confirma el email, salir del bucle principal
            
        else:
            print("Email inválido.")
    while True:
        direccion = input("ingrese la direccion : ")
        if cl.confirmar_dato("direccion",direccion):
            break 

    
    clientes = cl.cargar_clientes(RUTA_empleados)

    for cliente in clientes:
        if cliente['dni'] == dni:
            print("El DNI ya está registrado.")
            return 

    cliente = {
        "dni": dni,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "fecha_registro":  datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
    }
    clientes.append(cliente)
    cl.guardar_clientes(clientes,RUTA_empleados)
    print(f"Cliente {nombre} registrado exitosamente ")


def eliminar_empleado(dni: str) -> bool:
    """
    Pre: 
        - Recibe un dni que debe existir en la lista de empleados.
    Post:
        - Devuelve True si se eliminó al empleado, False si no se encontró.
    """
    pass


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
        opcion = input("Ingrese una de las opciones que se les mostro : ")
        if opcion == "1":
            break
        elif opcion == "2":
            registar_empleado()
        elif opcion == "3":
            pass
        elif opcion == "4":
            pass
        elif opcion == "5":
            pass
        else : 
            print("opcion invalida ingrese una de las que se les mostro ")
menu_empleados()