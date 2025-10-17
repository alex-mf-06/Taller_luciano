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

def registrar_clientes(RUTA_ARCHIVO: str) -> None:
    
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
    dni = ut.validar_dni()

    nombre = ut.confirmar_nombre()

    telefono = ut.validar_numero()

    email = ut.validar_email()

    direccion = ut.confirmar_direccion()

    clientes = cargar_clientes(RUTA_ARCHIVO)

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
    guardar_clientes(clientes,RUTA_ARCHIVO)
    print(f"la persona {nombre} esta registrado exitosamente \n")


def modificar_datos(dni: str,RUTA_archivo) ->None:
    """
    Pre:
        - dni: str no vacío, representa el documento del cliente ya registrado.
        - debe tener la ruta de archivo que quiere nodificar 
    Post:
        - guarda los datos modificado si se encuentra a la persona segun su dni 
        retorna true si la persona si se encuentra y la modifican y false si no 
    """
    datos = cargar_clientes(RUTA_archivo)
    encontrado = False
    for dato in datos :
        if dato.get("dni") == dni :
           nuevo_nombre = ut.confirmar_nombre()
           nuevo_telefono = ut.validar_numero()
           nueva_direccion = ut.confirmar_direccion()
           if nuevo_nombre:
               dato["nombre"] = nuevo_nombre
           if nuevo_telefono: 
               dato["telefono"] = nuevo_telefono
           if nueva_direccion:
               dato["direccion"] = nueva_direccion

           print("Datos actualizados.")
           encontrado = True 
           break 
    if encontrado:
        guardar_clientes(datos,RUTA_archivo)
    

def eliminar_datos(dni: str,RUTA_archivos: str) -> bool:
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


def listar_clientes(RUTA_ARCHIVO) -> list:
    """
    Pre:
        debe recibir un ruta para cargar los datos 
    Post:
        - Devuelve una lista de dicts, cada dict representa un cliente.
        - Si no hay clientes, devuelve lista vacía.
    """
    datos = cargar_clientes(RUTA_ARCHIVO)
    return datos


def obtener_cliente_por_dni(dni: str,RUTA_archivo:str) -> bool:
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
            return True # Devuelve el diccionario del cliente
    return False # Si el bucle termina, no lo encontró


def mostrar_opciones (opciones:tuple) ->None: 
    """
    no retorna nada solo muestra un menu de opciones .
    """
    if ut.validar_iterable(opciones):
        for i , opcion in enumerate(opciones,start=1):
            print(f"{i} - {opcion}\n")
    else : 
        print("las opciones no se pueden mostrar por que hubo un fallo")

def menu_clientes() ->None:
    opciones = ("Salir","Registrar cliente","Modificar datos del cliente","Eliminar cliente","Mostrar clientes ",)
    while True:
        
        mostrar_opciones(opciones)
        opcion=input("Ingrese una de las opciones: ")
        if opcion == "1":
            break
        elif opcion == "2":
            registrar_clientes(RUTA_clientes)

        elif opcion == "3":
            
            dni = ut.validar_dni()
            encontrado = obtener_cliente_por_dni(dni,RUTA_clientes)
            if encontrado : 
                print(f"Cliente encontrado: \n")
                modificar_datos(dni,RUTA_clientes)
                
            else : 
                print("no se encontro el cliente\n")
            
        elif opcion == "4":
            dni = ut.validar_dni()
            eliminado = eliminar_datos(dni,RUTA_clientes)
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
            print("opción no válida, intente nuevamente \n")
if __name__ == "__main__":
    menu_clientes()
    