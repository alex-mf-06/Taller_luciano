from datetime import datetime
from typing import List, Tuple
import re
import json
import os


def validar_iterable(lista: List) -> bool:
    """
    Pre:
        - lista: cualquier objeto.
    Post:
        - Devuelve True si el argumento se comporta como una lista y no está vacía.
        - Devuelve False si no se puede iterar o si está vacía.
    """
    try:
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
        confirmacion = (
            input(
                f"¿Confirma que el {etiqueta} '{valor}' es correcto? (s/n): ")
            .strip()
            .lower()
        )
        if confirmacion in ("s", "n"):
            return confirmacion == "s"
        print("Respuesta inválida. Por favor ingrese 's' o 'n'.")


def validar_dni() -> str:
    regex_dni = re.compile(r"^\d{7,8}$")
    while True:
        dni = input(
            "Ingrese el DNI del cliente (7 u 8 dígitos): "
        ).strip()  # Eliminar espacios en blanco al inicio y final

        if regex_dni.match(dni) and confirmar_dato("DNI", dni):
            return dni  # Si el usuario confirma el DNI, salir del bucle principal
        else:
            print(
                "DNI inválido. Debe contener solo números y tener entre 7 y 8 dígitos."
            )


def agregar_dato(dato: dict, ruta_archivo: str) -> bool:
    """
    Guarda una lista de datos en un archivo JSON de forma segura.
    Devuelve True si se guardó con éxito, False si hubo un error.
    """
    try:
        # --- PREVENCIÓN DE ERRORES ---
        # 1. Obtenemos el directorio y lo creamos si no existe para
        #    evitar un FileNotFoundError.
        directorio = os.path.dirname(ruta_archivo)
        os.makedirs(directorio, exist_ok=True)
        lista = cargar_datos(ruta_archivo)
        lista.append(dato)

        with open(ruta_archivo, "wt", encoding="utf-8") as file:
            # 3. Esta línea puede lanzar un TypeError si los datos no son serializables.
            json.dump(lista, file, indent=4, ensure_ascii=False)

        print(
            f"Datos guardados exitosamente en {os.path.abspath(ruta_archivo)}")
        return True  # La operación fue exitosa

    # --- MANEJO DE EXCEPCIONES ---
    except PermissionError:
        print(
            f"Error: No se tienen los permisos para escribir en la ruta '{ruta_archivo}'."
        )
        return False
    except TypeError:
        print(
            "Error: Los datos contienen un tipo de objeto que no se puede convertir a JSON (como un objeto datetime)."
        )
        return False
    except Exception as e:
        # Captura cualquier otro error inesperado
        print(f"Ocurrió un error inesperado al guardar el archivo: {e}")
        return False


def eliminar_datos(dni: str, RUTA_archivos: str) -> bool:
    """
    Pre:
        - dni: str no vacío, representa el documento del cliente.
    Post:
        - Elimina al cliente si está en la base de datos.
        - Retorna True si se eliminó, False si no se encontró.
    """
    try:
        # Se intenta cargar los datos. La función cargar_datos podría fallar
        # si el archivo no existe o está corrupto.
        datos = cargar_datos(RUTA_archivos)

        # Tu lógica original, que es muy buena y eficiente.
        datos_actualizados = [dato for dato in datos if dato.get("dni") != dni]

        if len(datos) > len(datos_actualizados):
            # Se intenta guardar los datos. Esta operación podría fallar
            # por falta de permisos (PermissionError) o datos inválidos (TypeError).
            actualizar_datos(datos_actualizados, RUTA_archivos)
            return True  # Eliminación exitosa
        else:
            return False  # No se encontró el DNI, no se eliminó nada

    except FileNotFoundError:
        # Error específico si 'cargar_datos' no encuentra el archivo.
        print(
            f"Error: No se pudo encontrar el archivo en la ruta '{RUTA_archivos}'.")
        return False

    except Exception as e:
        # Se captura cualquier otro error inesperado durante la carga o el guardado.
        print(
            f"Ocurrió un error inesperado durante la operación de eliminación: {e}")
        return False


def modificar_datos(dni: str, RUTA_archivo) -> None:
    """
    Esta funcion se encarga de modificar los datos de un cliente segun su dni.
    Pre:
        - dni: str no vacío, representa el documento del cliente ya registrado.
        - debe tener la ruta de archivo que quiere nodificar
    Post:
        - guarda los datos modificado si se encuentra a la persona segun su dni
        retorna true si la persona si se encuentra y la modifican y false si no
    """
    datos = cargar_datos(RUTA_archivo)
    encontrado = False
    for dato in datos:
        if dato.get("dni") == dni:
            nuevo_nombre = confirmar_nombre()
            nuevo_telefono = validar_numero()
            nueva_direccion = confirmar_direccion()
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
        actualizar_datos(datos, RUTA_archivo)


def validar_numero() -> str:
    """
    Solicita, valida y confirma un número de teléfono.
    El número debe tener entre 7 y 15 dígitos y puede comenzar con '+'.
    """
    regex_telefono = re.compile(r"^\+?\d{7,15}$")
    while True:
        telefono = input(
            "Ingrese el teléfono de la persona (7 a 15 dígitos): "
        ).strip()  # Eliminar espacios en blanco al inicio y final

        if regex_telefono.match(telefono) and confirmar_dato("teléfono", telefono):
            return telefono  # Si el usuario confirma el teléfono, salir del bucle principal
        else:
            print(
                "Teléfono inválido. Debe contener solo números y tener entre 7 y 15 dígitos."
            )


def cargar_datos(ruta_archivo: str) -> List[dict] | List[None]:
    """
    Carga los clientes desde un archivo JSON de forma segura.
    - Si el archivo existe y es válido, devuelve la lista de clientes.
    - Si el archivo NO existe, está vacío o corrupto, devuelve una lista vacía [].
    """
    try:
        # Intenta abrir y leer el archivo en modo lectura ('r').
        with open(ruta_archivo, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        # Si el archivo no existe, esta sección se ejecuta.
        print(
            f"Advertencia: El archivo '{ruta_archivo}' no se encontró. Se creará uno nuevo."
        )
        try:
            # Aseguramos que el directorio exista (igual que en guardar_datos).
            directorio = os.path.dirname(ruta_archivo)
            os.makedirs(directorio, exist_ok=True)

            # Creamos el archivo nuevo escribiendo una lista vacía en él.
            with open(ruta_archivo, "w", encoding="utf-8") as file:
                json.dump([], file)

            # Devolvemos una lista vacía, que es el contenido del archivo recién creado.
            return []

        except Exception as e:
            # Si hay un error al intentar crear el archivo (ej: permisos).
            print(
                f"Error crítico: No se pudo crear el archivo '{ruta_archivo}'. Razón: {e}"
            )
            return []

    except json.JSONDecodeError:
        # Se ejecuta si el archivo existe pero está vacío o corrupto.
        print(
            f"Advertencia: El archivo '{ruta_archivo}' tiene un formato inválido.")
        return []

    except Exception as e:
        # Captura cualquier otro error inesperado.
        print(f"Ocurrió un error inesperado al leer el archivo: {e}")
        return []


def actualizar_datos(datos: List[dict], ruta_archivo: str) -> bool:
    """
    Esta funcion se va a encargar de que se se actulice los datos que le envien y
    se sobrescriba en un archivo JSON .
    precondiciones: el parametro datos debe ser una lista de diccionarios y debe
    recibir una ruta de archivo que va a ser donde se va a guardar la
    informacion

    """
    ruta_temporal = ruta_archivo + ".tmp"
    try:
        # Asegura que el directorio de destino exista
        directorio = os.path.dirname(ruta_archivo)
        os.makedirs(directorio, exist_ok=True)

        # 1. Escribe toda la información en el archivo temporal
        with open(ruta_temporal, "w", encoding="utf-8") as file:
            json.dump(datos, file, indent=4, ensure_ascii=False)

        # 2. Si la escritura fue exitosa, renombra el temporal al nombre final.
        #    Esta operación es atómica y segura.
        os.rename(ruta_temporal, ruta_archivo)

        print(
            f"Datos guardados exitosamente en {os.path.abspath(ruta_archivo)}")
        return True

    except (TypeError, OSError) as e:
        # Si ocurre cualquier error de tipo de dato o del sistema de archivos...
        print(f"Ocurrió un error al guardar el archivo: {e}")

        # ...intenta eliminar el archivo temporal si es que se creó.
        if os.path.exists(ruta_temporal):
            os.remove(ruta_temporal)

        return False


def validar_email() -> str:
    """
    Solicita, valida y confirma un email. El email es opcional.

    Postcondiciones:
        - Devuelve un string (str) con el email válido si se ingresó uno.
        - Devuelve None si el usuario no ingresó un email y lo confirmó.
    """
    regex_email = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    while True:
        email = input("Ingrese el email de la persona : ").strip()
        if not email or regex_email.match(email):
            if confirmar_dato(
                "email", email if email else "sin email"
            ):  # llama la funcion para confirmar datos tanto si existe ek email o no
                return (
                    email  # Si el usuario confirma el email, salir del bucle principal
                )

        else:
            print("Email inválido.")


def confirmar_nombre() -> str:
    """solicita, valida y confirma un nombre de usuario.
    El nombre debe tener al menos 6 caracteres y  puede contener solo letras,
    acentos, 'ñ' y espacios."""
    regex_nombre = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{6,}$")

    while True:
        nombre = input("Ingrese el nombre de la persona :  ").strip()

        if nombre.strip() and regex_nombre.match(nombre):
            if confirmar_dato("nombre", nombre):
                return nombre  # Si el usuario confirma el nombre, salir del bucle principal

        else:
            print("Nombre inválido. No puede estar vacío.")


def obtener_mes_anio(fecha_str: str) -> str:
    """
    Recibe una fecha en formato string (YYYY-MM-DD) y devuelve
    un string con el mes y el año en español (ej: "Octubre 2025").
    """
    try:
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d")

        meses = {
            1: "Enero",
            2: "Febrero",
            3: "Marzo",
            4: "Abril",
            5: "Mayo",
            6: "Junio",
            7: "Julio",
            8: "Agosto",
            9: "Septiembre",
            10: "Octubre",
            11: "Noviembre",
            12: "Diciembre",
        }

        nombre_mes = meses.get(fecha.month, "Mes Desconocido")
        return f"{nombre_mes} {fecha.year}"

    except ValueError:
        return "Fecha Inválida"


def comfirmar_imformacion(informacion: dict) -> bool:
    """
    Esta funcion se encarga de que la persona vea la imformacion que paso
    como parametro para que la persona verifique si esta bien su ingormacion
    y retorna True si es positivo la informacion y False si no lo es.
    precondiciones : la funcion le deben dar como parametro un diccionario.
    postcondiciones: devuelve True si la persona confirma la informacion
    y False si no lo hace.

    """

    while True:
        for clave, valor in informacion.items():
            print(f"{clave}: {valor}\n")

        confirmacion = (
            input(f"¿Confirma que la informacion es correcta? (s/n): ").strip().lower()
        )
        if confirmacion in ("s", "n"):
            return confirmacion == "s"
        print("Respuesta inválida. Por favor ingrese 's' o 'n'.")


def registrar_datos(RUTA_ARCHIVO: str) -> None:
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
    clientes = cargar_dni_(RUTA_ARCHIVO)
    while True:
        # solicitud de datos
        dni = validar_dni()
        if dni in clientes:
            print("El DNI ya está registrado.")
            return

        nombre = confirmar_nombre()

        telefono = validar_numero()

        email = validar_email()

        direccion = confirmar_direccion()

        cliente = {
            "dni": dni,
            "nombre": nombre,
            "telefono": telefono,
            "email": email,
            "direccion": direccion,
            "fecha_registro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        if comfirmar_imformacion(cliente):
            break
    if validar_Ruta_archivo(RUTA_ARCHIVO):
        agregar_dato(cliente, RUTA_ARCHIVO)
        print(f"la persona {nombre} esta registrado exitosamente \n")
    else:
        crear_ruta_carpeta(os.path.dirname(RUTA_ARCHIVO))
        agregar_dato(cliente, RUTA_ARCHIVO)


def crear_ruta_carpeta(ruta: str) -> None:
    """
    Esta funcion se encarga de crear la ruta de una carpeta si no exite o si una persona lo elimino intencionalmente.
    debe crear el archivo si no exite en formato json . 
    precondiciones : se debe mandar una ruta en str
    postcondiciones : no devuelve nada solo crea la ruta de la carpeta si no existe.

    """
    try:
        if not os.path.exists(ruta):
            os.makedirs(ruta)
            print(f"La carpeta '{ruta}' ha sido creada.")

        else:
            print(f"La carpeta '{ruta}' ya existe.")
    except TypeError:
        print("La ruta proporcionada no es válida.")


def validar_Ruta_archivo(ruta: str) -> bool:
    """
    Esta funcion se encarga de validar que la ruta donde se enviaba los datos exista .
    precondiciones : se debe mandar una ruta en str
    postcondiciones : devuelve True si la ruta existe y False si no es asi.
    """
    try:
        ruta += ""
        if not os.path.exists(os.path.dirname(ruta)):
            print("La ruta no existe.")
            return False
        return True
    except TypeError:
        print("La ruta proporcionada no es válida.")
        return False


def confirmar_direccion() -> str:
    """
    esta funcion  se encarga de que el usuario ingrese la direccion de su  domicilio y que solo salga de la funcion si ingresa la direccion y confirma que si es correcta.
    """
    while True:
        direccion = input("ingrese la direccion : ").strip()
        if confirmar_dato("direccion", direccion):
            return direccion


def mostrar_opciones(opciones: tuple) -> None:
    """
    no retorna nada solo muestra un menu de opciones .
    """
    if validar_iterable(opciones):
        for i, opcion in enumerate(opciones, start=1):
            print(f"{i} - {opcion}\n")
    else:
        print("las opciones no se pueden mostrar por que hubo un fallo")


def Validar_patente() -> str:
    """
    se encarga de validar la pátente que ponga el usuario y ademas que confirme su opcion .
    retorna el str que seria la patente
    """
    patron_patente = re.compile(
        "^[A-Z]{3}\d{3}$|^\d{2}[A-Z]{3}\d{2}$"
    )  # expresiones regulares para validación de datos
    while True:
        patente = input("Ingrese la patente del vehículo :").upper()
        if patron_patente.match(patente) and confirmar_dato("patente", patente):
            return patente
        else:
            print("Patente inválida. Debe ser ABC123 o 12ABC34")


def cargar_dni_(RUTA_archivo: str) -> tuple:
    """

    Esta funcion se encarga de que le manden una ruta de archivo que ademas dentro
    de esta funcion se va a usar la de cargar datos para luego solo tener los dnis
    para funciones que se necesiten .
    precondiciones : se debe mandar una ruta que exista .
    postcondiciones : devuelve una tupla que solo va a tener los dnis del json
    que se necesite.

    """
    try:
        # 1. Se cargan los datos desde el archivo JSON
        datos = cargar_datos(RUTA_archivo)

        # 2. Se crea una tupla con los DNI usando una expresión generadora.
        #    Usar dato.get("dni") es más seguro que dato["dni"], ya que si un
        #    diccionario no tiene la clave "dni", no romperá el programa.
        #    El 'if dato.get("dni")' asegura que no se agreguen valores nulos.
        return tuple(dato.get("dni") for dato in datos if dato.get("dni"))

    except FileNotFoundError:
        # Se ejecuta si la función cargar_datos no encuentra el archivo
        print(
            f"Error: El archivo en la ruta '{RUTA_archivo}' no fue encontrado.")
        return ()  # Devuelve una tupla vacía


def validar_marca() -> str:
    """
    valida que si ponga la marca de un auto y ademas que confirme su eleccion solo asi sale de la funcion .
    """
    while True:
        marca = input("Ingrese la marca del vehículo : ").strip()
        if marca and confirmar_dato("marca", marca):
            return marca
        else:
            print("marca invalida")


def validar_modelo() -> str:
    """
    Se encarga de que ingrese un modelo del auto ejemplo : marca : ford , modelo : fiesta . solo sake de la funcion si confirma su eleccion .
    """
    while True:
        modelo = input("Ingrese el modelo del vehículo : ").strip()
        if modelo and confirmar_dato("modelo", modelo):
            return modelo
        else:
            print("modelo invalido")


def validar_año() -> str:
    """
    la funcion se encarga de de qie el usuario salga de la funcion si pone el año que sea valido y ademas que confirme la respuesta del usuario.
    """
    patron_anio = r"^\d{4}$"
    while True:
        anio = input("Ingrese el año del vehículo : ").strip()
        if patron_anio.match(anio) and confirmar_dato("año", anio):
            return anio
        else:
            print("año invalido")


def validar_tipo() -> str:
    """
    esta funcion se encarga de que el usuario ingrese el tipo de auto que tiene y solo se retorna cuando ponga un tipo de auto y confirme la
    respuesta del usuario.
    """
    while True:
        tipo = input(
            "Ingrese el tipo del vehículo (auto, camioneta, camión): ").strip()
        if confirmar_dato("tipo", tipo):
            return tipo
        else:
            print("tipo invalido")


def validar_n_factura():
    patron_n_factura = r"^\d{4}-\d{8}$"
    while True:
        n_factura = input(
            "Ingrese el número de factura (ej: 0001-00001234): ").strip()
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


def validar_fecha():
    patron_fecha = r"^\d{4}-\d{2}-\d{2}$"
    while True:
        fecha = input("Ingrese la fecha de emisión (YYYY-MM-DD): ").strip()
        if re.match(patron_fecha, fecha):
            if confirmar_dato("fecha de emisión", fecha):
                return fecha
        else:
            print("Fecha inválida. Formato correcto: YYYY-MM-DD")


def validar_items_factura():
    patron_item = r"^\d+$"
    items = []
    while True:
        cantidad = input(
            "Ingrese cantidad de un item (o ENTER para terminar): "
        ).strip()
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
        origen = input(
            "Seleccione origen de la factura: ").strip().capitalize()
        if origen.lower() in [o.lower() for o in opciones_origen]:
            if confirmar_dato("origen", origen):
                return origen
        else:
            print("Opción inválida. Debe elegir 'manual' o 'Arca'")


# MENU ----------------------------------------------------------------------------------------------------------

def opciones_menu(titulo: str, opciones: list) -> None:

    print(f"\n--- MENÚ: {titulo.upper()} ---")

    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
    print("-" * 60)


if __name__ == "__main__":
    nombre = confirmar_nombre()
    print(nombre)
