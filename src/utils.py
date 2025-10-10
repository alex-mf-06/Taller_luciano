from typing import List
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
    regex_dni = re.compile(r'^\d{7,8}$')
    while True:
        dni = input("Ingrese el DNI del cliente (7 u 8 dígitos): ").strip() # Eliminar espacios en blanco al inicio y final
        
        if regex_dni.match(dni) and confirmar_dato("DNI", dni):
                return dni # Si el usuario confirma el DNI, salir del bucle principal
        else:
            print("DNI inválido. Debe contener solo números y tener entre 7 y 8 dígitos.") 


def validar_numero() -> str : 
    regex_telefono = re.compile(r'^\+?\d{7,15}$')
    while True:
        telefono = input("Ingrese el teléfono de la persona (7 a 15 dígitos): ")
        if regex_telefono.match(telefono) and confirmar_dato("teléfono", telefono):
            return telefono # Si el usuario confirma el teléfono, salir del bucle principal
        else:
            print("Teléfono inválido. Debe contener solo números y tener entre 7 y 15 dígitos.")

def validar_email() -> str : 
    regex_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    while True:
        email = input("Ingrese el email de la persona : ")
        if not email or regex_email.match(email) :
            if confirmar_dato("email", email if email else "sin email"): # llama la funcion para confirmar datos tanto si existe ek email o no 
                return email # Si el usuario confirma el email, salir del bucle principal
            
        else:
            print("Email inválido.")

def confirmar_nombre () -> str : 
    regex_nombre = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]{6,}$")

    while True:
        nombre = input("Ingrese el nombre de la persona :  ")
        if nombre.strip() and regex_nombre.match(nombre):
            if confirmar_dato("nombre", nombre):
                return nombre # Si el usuario confirma el nombre, salir del bucle principal
                
        else:
            print("Nombre inválido. No puede estar vacío.")


def confirmar_direccion() -> str :
    while True:
        direccion = input("ingrese la direccion : ")
        if confirmar_dato("direccion",direccion):
            return direccion 

if __name__  == "__main__" :
    nombre = confirmar_nombre()
    print(nombre)