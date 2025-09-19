def agregar_empleado(dni: str, nombre: str, puesto: str, telefono: str, email: str = None) -> dict:
    """
    Pre: 
        - Recibe dni, nombre, puesto y teléfono. Todos son obligatorios.
        - El dni debe ser único, no puede estar repetido.
    Post:
        - Devuelve un diccionario con los datos del empleado agregado.
    """
    pass


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
