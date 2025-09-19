def registrar_producto():
    """
    Pre: Debe recibir los datos de un producto (nombre, categoría, cantidad inicial, unidad, proveedor, stock mínimo).
    Post: Agrega el producto al inventario con su información básica y stock inicial.
    """
    pass


def registrar_entrada():
    """
    Pre: Debe existir el producto en el inventario.
    Post: Incrementa la cantidad del producto según la reposición o compra realizada.
    """
    pass


def registrar_salida():
    """
    Pre: Debe existir el producto en el inventario y haber suficiente cantidad disponible.
    Post: Disminuye la cantidad del producto utilizado en reparaciones u órdenes de trabajo.
    """
    pass


def consultar_stock():
    """
    Pre: Debe existir al menos un producto registrado en el inventario.
    Post: Devuelve el listado completo de productos con sus cantidades actuales.
    """
    pass


def buscar_producto():
    """
    Pre: Recibe un nombre o código de producto válido.
    Post: Devuelve la información del producto si existe en el inventario.
    """
    pass


def reporte_stock_bajo():
    """
    Pre: Debe existir al menos un producto en el inventario con stock registrado.
    Post: Muestra los productos que se encuentran por debajo de su stock mínimo.
    """
    pass


def reporte_por_categoria():
    """
    Pre: Debe existir al menos un producto en el inventario con su categoría definida.
    Post: Devuelve un listado de productos agrupados por categoría y sus cantidades actuales.
    """
    pass


def menu_stock():
    """
    Pre: El usuario debe estar autenticado en el sistema y acceder a la sección de stock.
    Post: Muestra las opciones del módulo Stock y ejecuta la funcionalidad elegida.
    """
    while True:
        print("\n--- MÓDULO STOCK ---")
        print("1. Gestión de productos")
        print("2. Consultas")
        print("3. Reportes")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n--- GESTIÓN DE PRODUCTOS ---")
            print("1. Registrar nuevo producto")
            print("2. Registrar entrada de stock")
            print("3. Registrar salida de stock")
            print("0. Volver")
            subopcion = input("Seleccione una opción: ")

            if subopcion == "1":
                registrar_producto()
            elif subopcion == "2":
                registrar_entrada()
            elif subopcion == "3":
                registrar_salida()
            elif subopcion == "0":
                continue

        elif opcion == "2":
            print("\n--- CONSULTAS ---")
            print("1. Consultar stock disponible")
            print("2. Buscar producto específico")
            print("0. Volver")
            subopcion = input("Seleccione una opción: ")

            if subopcion == "1":
                consultar_stock()
            elif subopcion == "2":
                buscar_producto()
            elif subopcion == "0":
                continue

        elif opcion == "3":
            print("\n--- REPORTES ---")
            print("1. Reporte de stock bajo")
            print("2. Reporte por categoría")
            print("0. Volver")
            subopcion = input("Seleccione una opción: ")

            if subopcion == "1":
                reporte_stock_bajo()
            elif subopcion == "2":
                reporte_por_categoria()
            elif subopcion == "0":
                continue

        elif opcion == "0":
            break
        else:
            print("Opción no válida. Intente de nuevo.")
