import os

# --- Ruta base del proyecto (carpeta Taller_luciano) ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --- Carpeta de datos ---
DATA_DIR = os.path.join(BASE_DIR, "datos")

# --- Rutas a archivos JSON ---
RUTA_CLIENTES = os.path.join(DATA_DIR, "clientes.json")
RUTA_EMPLEADOS = os.path.join(DATA_DIR, "empleados.json")
RUTA_FACTURACION = os.path.join(DATA_DIR, "facturacion.json")
RUTA_ORDENES = os.path.join(DATA_DIR, "ordenes.json")
RUTA_REPORTES = os.path.join(DATA_DIR, "reportes.json")
RUTA_VEHICULOS = os.path.join(DATA_DIR, "vehiculos.json")
