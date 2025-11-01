import json
import os
import utils as ut
from datetime import datetime

RUTA_FACTURACION = os.path.join("datos", "facturacion.json")
RUTA_CLIENTES = os.path.join("datos", "clientes.json")
RUTA_VEHICULOS = os.path.join("datos","vehiculos.json")

lista_clientes = ut.cargar_json(RUTA_CLIENTES)
lista_vehiculos = ut.cargar_json(RUTA_VEHICULOS)
lista_facturas = ut.cargar_json(RUTA_FACTURACION)


def agregar_factura(lista_facturas, lista_clientes, lista_vehiculos):
    """Crea una nueva factura, validando datos y guardando en el JSON"""
    n_factura = ut.validar_n_factura()
    tipo_factura = ut.validar_tipo_factura()
    fecha =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    forma_pago = ut.validar_forma_pago()
    origen = ut.validar_origen()
    dni = ut.validar_dni()
    cliente_encontrado = ut.buscar_x_dni(lista_clientes,dni)
    if not cliente_encontrado:
        print("El cliente no está registrado. Debe cargarlo antes de facturar.")
        return lista_facturas

    vehiculo_cliente = None
    for vehiculo in lista_vehiculos:
        if vehiculo["dni_cliente"] == dni:
            vehiculo_cliente = vehiculo
            break

    if not vehiculo_cliente:
        print("No se encontró vehículo asociado al cliente.")
        return lista_facturas

    print("\nIngrese los ítems de la factura (ENTER para terminar):")
    items = []
    while True:
        descripcion = input("Descripción del ítem (ENTER para terminar): ").strip()
        if descripcion == "":
            break

        cantidad = input("Cantidad: ").strip()
        precio = input("Precio unitario: ").strip()

        try:
            cantidad = int(cantidad)
            precio = float(precio)
        except ValueError:
            print("Error: cantidad y precio deben ser números.")
            continue

        subtotal = cantidad * precio
        items.append({
            "descripcion": descripcion,
            "cantidad": cantidad,
            "precio_unitario": precio,
            "subtotal": subtotal
        })

    total = sum(item["subtotal"] for item in items) #lista por comprension en caso de que haya mas de un item
    factura = {
        "numero": n_factura,
        "tipo": tipo_factura,
        "fecha": fecha,
        "forma_pago": forma_pago,
        "origen": origen,
        "cliente": {
            "dni": cliente_encontrado["dni"],
            "nombre": cliente_encontrado["nombre"],
            "apellido": cliente_encontrado.get("apellido", "")
        },
        "vehiculo": {
            "patente": vehiculo_cliente["patente"],
            "marca": vehiculo_cliente["marca"],
            "modelo": vehiculo_cliente["modelo"],
            "anio": vehiculo_cliente["anio"]
        },
        "items": items,
        "total": total
    }

    lista_facturas.append(factura)
    ut.guardar_json(lista_facturas,RUTA_FACTURACION)

    print("\nFactura creada correctamente.")
    return lista_facturas


def eliminar_factura(lista_facturas):
    """
    Permite eliminar una factura por su número.
    """
    try:
        numero_factura = input("Ingrese el número de factura a eliminar: (formato 0001-00001234)").strip()

        for factura in lista_facturas:
            if factura["numero"] == numero_factura:
                lista_facturas.remove(factura)
                print(f"La factura {numero_factura} fue eliminada correctamente.")
                ut.guardar_json(lista_facturas, RUTA_FACTURACION)
                break 
        else:
            print("No se encontró una factura con ese número.")

    except ValueError:
        print("Error al eliminar la factura.")


def buscar_factura(lista_facturas):
    """
    Busca una factura por un criterio de búsqueda.

    Pre-condición:
        - Se necesita un criterio de búsqueda (ID de factura, patente o DNI del cliente).

    Post-condición:
        - Si se encuentra, muestra los detalles de la factura.
        - Si no se encuentra, notifica al usuario.
    """
    numero = input("Ingrese el número de factura a buscar: ").strip()
    factura_encontrada = None
    for factura in lista_facturas:
        if factura["numero"] == numero:
            factura_encontrada = factura
            break
    if factura_encontrada:
        print("\nFactura encontrada:")
        for clave, valor in factura_encontrada.items():
            print(f"{clave}: {valor}")
    else:
        print("No se encontró ninguna factura con ese número.")





def menu_facturacion():
    """
    Muestra el menú principal del módulo de facturación.
    """
    opciones = ("Agregar factura manualmente", "Buscar factura", "Listar facturas", "Eliminar factura")
    while True:
        
        ut.mostrar_opciones(opciones)

        try:
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                agregar_factura(lista_facturas, lista_clientes, lista_vehiculos)
            elif opcion == "2":
                buscar_factura(lista_facturas)
            elif opcion == "3":
                ut.listar_datos(lista_facturas)
            elif opcion == "4":
                eliminar_factura(lista_facturas)
            elif opcion == "0":
                break
            else:
                print("Opción inválida, intente nuevamente.")
        except ValueError:
            print("Valor invalido. Por favor, ingrese un numero.")
            continue


