def registrar_pago(id_pago: int, cliente_dni: str, monto: float, fecha: str, metodo: str) -> dict:
    """
    Pre: 
        - Recibe id_pago como un numero entero positivo, unico.
        - Recibe cliente_dni que debe existir en la lista de clientes.
        - Recibe monto a pagar como un numero positivo.
        - Recibe fecha en formato válido (ejemplo: dd/mm/aaaa).
        - Recibe metodo de pago, que puede ser "efectivo", "tarjeta", "transferencia", etc.
    Post:
        - Devuelve un diccionario con los datos del pago registrado.
    """
    pass


def eliminar_pago(id_pago: int) -> bool:
    """
    Pre: 
        - Recibe id_pago como un numero entero positiivo que debe existir en los pagos.
    Post:
        - Devuelve True si se eliminó el pago, False si no se encontro.
    """
    pass


def listar_pagos(cliente_dni: str = None) -> list[dict]:
    """
    Pre: 
        - Recibe opcionalmente un cliente_dni existente (ya registrado) si se proporciona.
    Post:
        - Devuelve una lista con todos los pagos registrados, filtrados por cliente si se indicó el dni.
    """
    pass

