### Sistema de Gestión para Taller de chapa y pintura
Proyecto Final – Algoritmos y Estructura de Datos I – UADE (2025)

Este proyecto es un sistema de gestión integral para talleres de chapa y pintura, desarrollado en Python como trabajo grupal para la materia Algoritmos y Estructuras de Datos I.
Su objetivo es facilitar el registro, control y consulta de la información más importante del negocio: clientes, vehículos, empleados, gastos, facturación y reportes generales.

El sistema utiliza archivos JSON para guardar los datos, lo que lo hace liviano, fácil de mantener y sin necesidad de instalar bases de datos externas.


### Módulos del sistema

# -Clientes

Permite registrar nuevos clientes con validaciones (DNI, teléfono, correo, dirección).
Guarda los datos en clientes.json.
Incluye funciones de alta, baja, modificación y búsqueda por DNI o nombre.

# -Vehículos

Relaciona cada vehículo con su cliente.
Permite registrar marca, modelo, patente, año y observaciones.
Guarda los datos en vehiculos.json.

# -Facturación

Genera facturas con número automático o manual, tipo (A, B o C), fecha, ítems, forma de pago y origen (manual o ARCA).
Guarda la información en facturacion.json.
Incluye validaciones mediante expresiones regulares y puede integrarse con sistemas externos.

# -Empleados

Registra empleados con sus datos básicos, cargo, sueldo y fecha de ingreso.
Permite calcular salarios totales o listar empleados activos.

# -Gastos

Permite registrar y clasificar gastos del taller (insumos, mantenimiento, servicios, etc.) con fecha y monto.
Se guarda en gastos.json.

# -Reportes

Genera reportes consolidados a partir de la información de los distintos módulos:

Facturación total por mes

Gastos vs. ingresos

Clientes activos

Vehículos por cliente
Los reportes pueden imprimirse por pantalla o exportarse a archivos

-----------------------------------------------------------------------------------------

#Tecnologías utilizadas

Python 3.10+

JSON (para persistencia)

Regex (re) (para validaciones)

os / datetime (manejo de rutas y fechas)

-----------------------------------------------------------------------------------------

Desarrollado por:

Alex Flores

Elisa Correa

David Rocha

Luciano Dominguez


