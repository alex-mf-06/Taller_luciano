# Sistema de gestión para un taller de chapa y pintura

Trabajo final de **Algoritmos y Estructuras de Datos I** — UADE, 2025.

Aplicación de consola en Python para administrar la operación de un taller: clientes, vehículos,
órdenes de trabajo, empleados, facturación, gastos y reportes. Los datos se guardan en archivos
JSON.

## Ejecución

Requiere Python 3.12 o superior. No usa dependencias externas.

```bash
cd src
python main.py
```

## Módulos

| Módulo | Archivo | Funciones |
|---|---|---|
| Clientes | `clientes.py` | Alta, modificación, baja, listado y búsqueda por DNI |
| Vehículos | `vehiculos_reestructurado.py` | Alta, modificación, baja, listado y búsqueda por patente o por DNI del titular |
| Órdenes de trabajo | `ordenes.py` | Alta, listado, filtro por estado y cambio de estado (pendiente, en proceso, finalizada) |
| Empleados | `empleados.py` | Alta, modificación, baja, listado y búsqueda por DNI |
| Facturación | `facturacion.py` | Alta con ítems, búsqueda, listado y baja |
| Gastos | `gastos.py` | Registro por categoría y listado |
| Reportes | `reportes.py` | Gastos por categoría, vehículos atendidos y facturación por rango de fechas, productos más usados |

`utils.py` reúne las validaciones de entrada (DNI, teléfono, email, patente, montos y fechas,
con expresiones regulares) y las operaciones de lectura y escritura sobre los archivos.
`config.py` define las rutas de datos.

## Estructura

```
src/      código fuente
datos/    archivos JSON de persistencia, con datos de prueba
```

## Datos

| Archivo | Contenido | Relación |
|---|---|---|
| `clientes.json` | DNI, nombre, teléfono, email, dirección | — |
| `vehiculos.json` | Patente, marca, modelo, año, tipo | Cliente, por DNI |
| `ordenes.json` | Fecha, descripción, estado, costo estimado | Vehículo, por patente; empleado, por nombre |
| `empleados.json` | DNI, nombre, teléfono, email, dirección | — |
| `facturacion.json` | Número, tipo (A, B o C), fecha, forma de pago, ítems, total | Cliente y vehículo |
| `gastos.json` | Fecha, monto, categoría | — |

## Contenidos de la materia aplicados

Listas, tuplas y diccionarios; listas por comprensión; funciones con precondiciones y
postcondiciones; expresiones regulares; manejo de excepciones; persistencia en archivos.

## Autores

Alex Flores · Elisa Correa · David Rocha · Luciano Dominguez
