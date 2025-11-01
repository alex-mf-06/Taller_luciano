from typing import List
import json
import os
import re

def validar_iterable(lista: List) -> bool:
    """
    Pre:
        - lista: cualquier objeto.
    Post:
        - Devuelve True si el argumento se comporta como una lista y no está vacía.
        - Devuelve False si no se puede iterar o si está vacía.
    """
    try:
        # Intenta obtener su longitud (si falla, no es tipo lista o similar)
        if len(lista) == 0:
            return False
        
        # Intenta iterar (si falla, no es una secuencia válida)
        for _ in lista:
            pass
        
        return True

    except TypeError:
        # Si no se puede obtener la longitud o iterar, no es lista
        return False
    except Exception as e:
        # Cualquier otro error inesperado
        print("Error al validar la lista:", e)
        return False
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

def validar_dni () -> str :
    """pre: Solicita al usuario que ingrese su DNI
     post: Valida que el DNI contenga 7 u 8 digitos, en caso de no ser así vuelve a pedir el dato hasta que sea correcto"""
    regex_dni = re.compile(r'^\d{7,8}$')
    while True:
        dni = input("Ingrese el DNI del cliente (7 u 8 dígitos): ").strip() # Eliminar espacios en blanco al inicio y final
        
        if regex_dni.match(dni) and confirmar_dato("DNI", dni):
                return dni # Si el usuario confirma el DNI, salir del bucle principal
        else:
            print("DNI inválido. Debe contener solo números y tener entre 7 y 8 dígitos.") 


def validar_numero() -> str : 
    """
    Solicita, valida y confirma un número de teléfono.
    El número debe tener entre 7 y 15 dígitos y puede comenzar con '+'. En caso de no ser así vuelve a pedir el dato
    """
    regex_telefono = re.compile(r'^\+?\d{7,15}$')
    while True:
        telefono = input("Ingrese el teléfono de la persona (7 a 15 dígitos): ").strip() # Eliminar espacios en blanco al inicio y final
        
        if regex_telefono.match(telefono) and confirmar_dato("teléfono", telefono):
            return telefono # Si el usuario confirma el teléfono, salir del bucle principal
        else:
            print("Teléfono inválido. Debe contener solo números y tener entre 7 y 15 dígitos.")

def validar_email() -> str : 
    """
    Solicita, valida y confirma un email. El email es opcional.

    Postcondiciones:
        - Devuelve un string (str) con el email válido si se ingresó uno.
        - Devuelve None si el usuario no ingresó un email y lo confirmó.
    """
    regex_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    while True:
        email = input("Ingrese el email de la persona : ").strip()
        if not email or regex_email.match(email) :
            if confirmar_dato("email", email if email else "sin email"): # llama la funcion para confirmar datos tanto si existe ek email o no 
                return email # Si el usuario confirma el email, salir del bucle principal
            
        else:
            print("Email inválido.")

def confirmar_nombre () -> str : 
    """solicita, valida y confirma un nombre de usuario.
    El nombre debe tener al menos 6 caracteres y  puede contener solo letras,
    acentos, 'ñ' y espacios."""
    regex_nombre = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{6,}$")

    while True:
        nombre = input("Ingrese el nombre de la persona :  ").strip()

        if nombre.strip() and regex_nombre.match(nombre):
            if confirmar_dato("nombre", nombre):
                return nombre # Si el usuario confirma el nombre, salir del bucle principal
                
        else:
            print("Nombre inválido. No puede estar vacío.")


def confirmar_direccion() -> str :
    """
    esta funcion  se encarga de que el usuario ingrese la direccion de su  domicilio y que solo salga de la funcion si ingresa la direccion y confirma que si es correcta.
    """
    while True:
        direccion = input("ingrese la direccion : ").strip()
        if confirmar_dato("direccion",direccion):
            return direccion 
def mostrar_opciones (opciones:tuple) ->None: 
    """
    no retorna nada solo muestra un menu de opciones .
    """
    if validar_iterable(opciones):
        for i , opcion in enumerate(opciones,start=1):
            print(f"{i} - {opcion}\n")
    else : 
        print("las opciones no se pueden mostrar por que hubo un fallo")

def Validar_patente() -> str : 
     """
     se encarga de validar la pátente que ponga el usuario y ademas que confirme su opcion .
     retorna el str que seria la patente 
     """
     patron_patente = r"^[A-Z]{3}\d{3}$|^\d{2}[A-Z]{3}\d{2}$" # expresiones regulares para validación de datos
     while True:
        patente = input("Ingrese la patente del vehículo :").upper() 
        if patron_patente.match(patente) and confirmar_dato("patente",patente):
            return patente
        else:
            print("Patente inválida. Debe ser ABC123 o 12ABC34")

def validar_marca () -> str : 
    """
    valida que si ponga la marca de un auto y ademas que confirme su eleccion solo asi sale de la funcion . 
    """
    while True:
        marca = input("Ingrese la marca del vehículo : ").strip()
        if marca and confirmar_dato("marca",marca):
            return marca
        else:
            print("marca invalida")

def validar_modelo () -> str : 
    """
    Se encarga de que ingrese un modelo del auto ejemplo : marca : ford , modelo : fiesta . solo sake de la funcion si confirma su eleccion . 
    """
    while True:
        modelo = input("Ingrese el modelo del vehículo : ").strip()
        if modelo and confirmar_dato("modelo",modelo):
            return modelo
        else:
            print("modelo invalido")
    
def validar_año() -> str : 
    """
    la funcion se encarga de de qie el usuario salga de la funcion si pone el año que sea valido y ademas que confirme la respuesta del usuario.
    """
    patron_anio = r'^\d{4}$'
    while True:
        anio = input("Ingrese el año del vehículo : ").strip()
        if patron_anio.match(anio) and confirmar_dato("año",anio):
            return anio
        else:
            print("año invalido")

def validar_tipo() -> str : 
    """
    esta funcion se encarga de que el usuario ingrese el tipo de auto que tiene y solo se retorna cuando ponga un tipo de auto y confirme la 
    respuesta del usuario.
    """
    while True:
        tipo = input("Ingrese el tipo del vehículo (auto, camioneta, camión): ").strip()
        if confirmar_dato("tipo",tipo):
            return tipo
        else:
            print("tipo invalido")


def validar_n_factura():
    """pre: Solicita al usuario el número de factura a ingresar
    post: En caso de ser válido se carga en el json, de no ser así vuelve a pedir el dato"""
    patron_n_factura = r"^\d{4}-\d{8}$"
    while True:
        n_factura = input("Ingrese el número de factura (ej: 0001-00001234): ").strip()
        if re.match(patron_n_factura, n_factura):
            if confirmar_dato("número de factura", n_factura):
                return n_factura
        else:
            print("Número de factura inválido. Formato correcto: 0001-00001234")

def validar_tipo_factura():
    patron_tipo_factura = r"^[ABC]$"
    while True:
        tipo = input("Ingrese tipo de factura (A/B/C): ").strip().upper()
        if re.match(patron_tipo_factura, tipo):
            if confirmar_dato("tipo de factura", tipo):
                return tipo
        else:
            print("Tipo de factura inválido. Debe ser A, B o C")


def validar_items_factura():
    patron_item = r"^\d+$"
    items = [] #lista para guardar las cantidades de los productos incluidos en la factura
    while True:
        cantidad = input("Ingrese cantidad de un item (o ENTER para terminar): ").strip()
        if cantidad == "":
            break
        if re.match(patron_item, cantidad):
            if confirmar_dato("cantidad del item", cantidad):
                items.append(int(cantidad))
        else:
            print("Cantidad inválida. Debe ser un número entero positivo")
    return items

def validar_forma_pago():
    opciones_pago = ["Efectivo", "Transferencia", "Tarjeta"]
    while True:
        mostrar_opciones(opciones_pago)
        pago = input("Seleccione forma de pago: ").strip().capitalize()
        if pago in opciones_pago:
            if confirmar_dato("forma de pago", pago):
                return pago
        else:
            print("Opción inválida. Debe elegir una de las opciones mostradas")

def validar_origen():
    opciones_origen = ["manual", "Arca"]
    while True:
        mostrar_opciones(opciones_origen)
        origen = input("Seleccione origen de la factura: ").strip().capitalize()
        if origen.lower() in [o.lower() for o in opciones_origen]:
            if confirmar_dato("origen", origen):
                return origen
        else:
            print("Opción inválida. Debe elegir 'manual' o 'Arca'")

def buscar_x_dni(lista_datos, dni):
    """Devuelve el primer elemento que coincide con el DNI, o None si no existe"""
    for item in lista_datos:
        if item["dni"] == dni:   
            return item
    return None


def mostrar_x_dni(lista_datos, clave_dni, nombre_lista):
    """
    Busca elementos en una lista según una clave de DNI.
    """
    try:
        dni = validar_dni() 
        encontrados = [item for item in lista_datos if item[clave_dni] == dni]

        if encontrados:
            print(f"\nSe encontraron {len(encontrados)} {nombre_lista} para el DNI {dni}:")
            for i, item in enumerate(encontrados, start=1):
                print(f"\n{nombre_lista.capitalize()} {i}:")
                for clave, valor in item.items():
                    print(f"{clave.capitalize()}: {valor}")
        else:
            print(f"No se encontraron {nombre_lista} para ese DNI.")
    except Exception as e:
        print(f"Ocurrió un error al buscar {nombre_lista} por DNI: {e}")

def guardar_json(lista,ruta):
    """pre: Guarda el archivo JSON.
    post: Si ocurre un error durante la escritura, se muestra un mensaje."""
    with open(ruta,"w", encoding="UTF-8") as archivo:
        try:
            json.dump(lista, archivo, indent=4)
        except FileNotFoundError:
            print("No se encontró la ruta del archivo")
        except Exception as e:
            print(f"Error al guardar el archivo:  {e}")

def cargar_json(ruta: str) -> list:
    """
    Carga un archivo JSON de forma segura.
    - Si el archivo existe y es válido, devuelve la lista cargada.
    - Si el archivo NO existe, está vacío o corrupto, devuelve una lista vacía [].
    """
    # Si el archivo NO existe, entrega una lista vacía y termina.
    if not os.path.exists(ruta):
        return []

    # Si el archivo SÍ existe, intenta leerlo.
    with open(ruta, "r", encoding="utf-8") as file:
        try:
            # Si tiene contenido JSON válido, lo devuelve.
            return json.load(file)
        except json.JSONDecodeError:
            # Si está vacío o corrupto, entrega una lista vacía.
            return []
            
def listar_datos(lista_datos, nombre_tipo="dato"):
    """
    Lista cualquier tipo de datos cargados de manera legible.
    - lista_datos: lista de diccionarios con los datos a mostrar
    - nombre_tipo: string para mostrar el tipo de dato (ej: 'vehículo', 'cliente')
    """
    try:
        if not lista_datos:
            print(f"No hay {nombre_tipo}s cargados.")
            return

        print(f"\nListado de {len(lista_datos)} {nombre_tipo}(s):")
        for i, item in enumerate(lista_datos, start=1):
            print(f"\n{nombre_tipo.capitalize()} {i}:")
            for clave, valor in item.items():
                print(f"{clave.capitalize()}: {valor}")
    except (TypeError, KeyError):
        print(f"Error al listar los {nombre_tipo}s")
    except Exception as e:
        print(f"Ocurrió un error al listar los {nombre_tipo}s: {e}")


if __name__  == "__main__" :
    nombre = confirmar_nombre()
    print(nombre)