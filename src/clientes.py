def registrar_cliente(dni: str, nombre: str, telefono: str, email: str = None, direccion: str = None) -> dict:
    """
    Pre:
        - dni: str no vacío, debe ser único (representa el documento del cliente).
        - nombre: str no vacío, representa el nombre y apellido del cliente.
        - telefono: str no vacío, representa un número de contacto.
        - email: str (puede ser None o ""), representa el correo electrónico.
        - direccion: str (puede ser None o ""), representa el domicilio.
    Post:
        - Registra un cliente en la base de datos usando su dni como identificador único.
        - Devuelve un dict con las claves: {"dni": str, "nombre": str, "telefono": str, "email": str, "direccion": str}.
    """
    pass


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