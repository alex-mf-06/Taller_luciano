from datetime import datetime
from typing import List
import re 
import json 
import os
import utils as ut

# --- CÁLCULO DE LA RUTA ABSOLUTA Y SEGURA ---
# Obtiene la ruta del directorio donde está el script (la carpeta src)
script_dir = os.path.dirname(os.path.abspath(__file__))
# Sube un nivel en el directorio para llegar a la raíz del proyecto (Taller_Luciano)
project_root = os.path.dirname(script_dir)
# Construye la ruta completa y correcta al archivo clientes.json
RUTA_clientes = os.path.join(project_root, 'datos', 'clientes.json')


def cargar_clientes(ruta_archivo: str ) -> list:
    """
    Carga los clientes desde un archivo JSON de forma segura.
    - Si el archivo existe y es válido, devuelve la lista de clientes.
    - Si el archivo NO existe, está vacío o corrupto, devuelve una lista vacía [].
    """
    # Si el archivo NO existe, entrega una lista vacía y termina.
    if not os.path.exists(ruta_archivo):
        return []

    # Si el archivo SÍ existe, intenta leerlo.
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        try:
            # Si tiene contenido JSON válido, lo devuelve.
            return json.load(file)
        except json.JSONDecodeError:
            # Si está vacío o corrupto, entrega una lista vacía.
            return []

def guardar_clientes(clientes: List, ruta_archivo: str ) -> None:
    """Guarda la lista de clientes en un archivo JSON con formato legible."""
    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        json.dump(clientes, file, indent=4, ensure_ascii=False)
    print(f"Datos guardados exitosamente en {os.path.abspath(ruta_archivo)}")

def confirmar_dato(etiqueta: str, valor: str) -> bool:
    """
    Solicita al usuario que confirme si un dato ingresado es correcto.
    Precondiciones:
        - etiqueta: str, la etiqueta del dato (por ejemplo, "DNI", "nombre").
        - valor: str, el valor del dato a confirmar.
    Postcondiciones:
        - Devuelve True si el usuario confirma que el dato es correcto ('s') y False si no lo confirma.
    """

    while True:
        confirmacion = input(f"¿Confirma que el {etiqueta} '{valor}' es correcto? (s/n): ").strip().lower()
        if confirmacion in ['s', 'n']:
            return confirmacion == 's'
        print("Respuesta inválida. Por favor ingrese 's' o 'n'.")

def registrar_clientes() -> None:
    
    """
    Permite registrar clientes validados con expresiones regulares y guardar los datos en un archivo JSON.

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
            if confirmar_dato("DNI", dni):
                break # Si el usuario confirma el DNI, salir del bucle principal
        else:
            print("DNI inválido. Debe contener solo números y tener entre 7 y 8 dígitos.")

    while True:
        nombre = input("Ingrese el nombre de la persona :  ")
        if nombre.strip():
            if confirmar_dato("nombre", nombre):
                break # Si el usuario confirma el nombre, salir del bucle principal
                
        else:
            print("Nombre inválido. No puede estar vacío.")

    while True:
        telefono = input("Ingrese el teléfono de la persona (7 a 15 dígitos): ")
        if regex_telefono.match(telefono):
            if confirmar_dato("teléfono", telefono):
                break # Si el usuario confirma el teléfono, salir del bucle principal
        else:
            print("Teléfono inválido. Debe contener solo números y tener entre 7 y 15 dígitos.")

    while True:
        email = input("Ingrese el email de la persona : ")
        if not email or regex_email.match(email) :
            if confirmar_dato("email", email if email else "sin email"): # llama la funcion para confirmar datos tanto si existe ek email o no 
                break # Si el usuario confirma el email, salir del bucle principal
            
        else:
            print("Email inválido.")
    while True:
        direccion = input("ingrese la direccion : ")
        if confirmar_dato("direccion",direccion):
            break 

    
    clientes = cargar_clientes(RUTA_clientes)

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
    guardar_clientes(clientes,RUTA_clientes)
    print(f"Cliente {nombre} registrado exitosamente ")



def modificar_cliente(dni: str, nombre: str = None, telefono: str = None, email: str = None, direccion: str = None) -> dict | None:
    """
    Pre:
        - dni: str no vacío, representa el documento del cliente ya registrado.
        - nombre, telefono, email, direccion: str o None. Si es None, ese campo no se modifica.
    Post:
        - Si el cliente existe, devuelve un dict con sus datos actualizados.
        - Si no existe, devuelve None.
    """
    pass


def eliminar_cliente(dni: str,RUTA_archivos: str) -> bool:
    """
    Pre:
        - dni: str no vacío, representa el documento del cliente.
    Post:
        - Elimina al cliente si está en la base de datos.
        - Retorna True si se eliminó, False si no se encontró.
    """
    datos = cargar_clientes(RUTA_archivos)
    datos_actualizados = [dato for dato in datos if dato.get("dni") != dni]
    if len(datos) > len(datos_actualizados):
        # 4. Si hubo un cambio, guardar la lista actualizada
        guardar_clientes(datos_actualizados, RUTA_archivos) # Asumo una función genérica guardar_datos
        return True # Eliminación exitosa
    else:
        return False # No se encontró el DNI, no se eliminó nada


def listar_clientes() -> list:
    """
    Pre:
        - No recibe parámetros.
    Post:
        - Devuelve una lista de dicts, cada dict representa un cliente.
        - Si no hay clientes, devuelve lista vacía.
    """
    pass


def obtener_cliente_por_dni(dni: str,RUTA_archivo:str) -> dict | None:
    """
    Pre:
        - dni: str no vacío.
    Post:
        - Devuelve el dict con los datos del cliente si existe.
        - Si no existe, devuelve None.
    """
    
    clientes = cargar_clientes(RUTA_archivo) # Usamos la función que carga el json 
    for cliente in clientes:
        if cliente['dni'] == dni:
            return cliente # Devuelve el diccionario del cliente
    return None # Si el bucle termina, no lo encontró

def mostrar_opciones (opciones:tuple) ->None: 
    """
    no retorna nada solo muestra un menu de opciones .
    """
    if ut.validar_iterable(opciones):
        for i , opcion in enumerate(opciones,start=1):
            print(f"{i} - {opcion}")
    else : 
        print("las opciones no se pueden mostrar por que hubo un fallo")
def menu_clientes() ->None:
    opciones = ("Salir","Registrar cliente","Modificar datos del cliente","Eliminar cliente","Mostrar clientes ",)
    regex_dni = re.compile(r'^\d{7,8}$')
    while True:
        
        mostrar_opciones(opciones)
        opcion=input("Ingrese una opcion de las que se les muestran :")
        if opcion == "1":
            break
        elif opcion == "2":
            registrar_clientes()
        elif opcion == "3":
            
            while True: 
                dni = input("Ingrese el Dni del Cliente : ")
                if regex_dni.match(dni) and confirmar_dato("DNI",dni):
                     break 
                else : 
                    print("Dni invalido ingrese nuevamente ")
            encontrado = obtener_cliente_por_dni(dni)
            if encontrado : 
                print(f"Cliente encontrado: {encontrado['nombre']}")
                
            else : 
                print("no se encontro el cliente")
        elif opcion == "4":
            while True: 
                dni = input("Ingrese el Dni del Cliente : ")
                if regex_dni.match(dni) and confirmar_dato("DNI",dni):
                     break 
                else : 
                    print("Dni invalido ingrese nuevamente ")
            eliminado = eliminar_cliente(dni,RUTA_clientes)
            if eliminado:
                print("se ah eliminado la persona correctamente")
            else: 
                print("no se escontro a la persona en nuestro registro")
        elif opcion == "5":
            pass
        else : 
            print("opcion invalida ingrese una de las que se les mostro ")
if __name__ == "__main__":
    menu_clientes()