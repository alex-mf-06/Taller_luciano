from typing import List

def validar_lista(lista: List) -> bool:
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
