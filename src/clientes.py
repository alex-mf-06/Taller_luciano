from datetime import datetime

import re 
import json 
import os
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
        nombre = input("Ingrese el nombre del cliente: ")
        if nombre.strip():
            if confirmar_dato("nombre", nombre):
                break # Si el usuario confirma el nombre, salir del bucle principal
                
        else:
            print("Nombre inválido. No puede estar vacío.")

    while True:
        telefono = input("Ingrese el teléfono del cliente (7 a 15 dígitos): ")
        if regex_telefono.match(telefono):
            if confirmar_dato("teléfono", telefono):
                break # Si el usuario confirma el teléfono, salir del bucle principal
        else:
            print("Teléfono inválido. Debe contener solo números y tener entre 7 y 15 dígitos.")

    while True:
        email = input("Ingrese el email del cliente : ")
        if not email or regex_email.match(email) :
            if confirmar_dato("email", email if email else "sin email"): # llama la funcion para confirmar datos tanto si existe ek email o no 
                break # Si el usuario confirma el email, salir del bucle principal
            
        else:
            print("Email inválido.")

    ruta_archivo ='clientes.json'
    if os.path.exists(ruta_archivo): # Verificar si el archivo existe
        with open(ruta_archivo, 'r') as file: # Abrir el archivo en modo lectura
            try:
                clientes = json.load(file)
            except json.JSONDecodeError:
                print("El archivo JSON está corrupto o vacío.")
                clientes = []
    else:
        clientes = []
    for cliente in clientes:
        if cliente['dni'] == dni:
            print("El DNI ya está registrado.")
            return 

    cliente = {
        "dni": dni,
        "nombre": nombre,
        "telefono": telefono,
        "email": email,
        "fecha_registro":  datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
    }
    clientes.append(cliente)
    with open(ruta_archivo, 'w', encoding='utf-8') as file: # Abrir el archivo en modo  escritura y con codificación UTF-8
        json.dump(clientes, file, indent=4,ensure_ascii=False) # Guardar la lista actualizada en el archivo JSON
    print(f"Cliente {nombre} registrado exitosamente en {os.path.abspath(ruta_archivo)}")





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


def eliminar_cliente(dni: str) -> bool:
    """
    Pre:
        - dni: str no vacío, representa el documento del cliente.
    Post:
        - Elimina al cliente si está en la base de datos.
        - Retorna True si se eliminó, False si no se encontró.
    """
    pass


def listar_clientes() -> list:
    """
    Pre:
        - No recibe parámetros.
    Post:
        - Devuelve una lista de dicts, cada dict representa un cliente.
        - Si no hay clientes, devuelve lista vacía.
    """
    pass


def obtener_cliente_por_dni(dni: str) -> dict | None:
    """
    Pre:
        - dni: str no vacío.
    Post:
        - Devuelve el dict con los datos del cliente si existe.
        - Si no existe, devuelve None.
    """
    pass