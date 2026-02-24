# ProyectoCalculadoraMicrokernel

## Descripción de la actividad:
los equipos deberán diseñar e implementar una calculadora extensible empleando el patrón de arquitectura Microkernel.
El objetivo es entender cómo separar el núcleo funcional (core system) de los módulos externos (plug-ins o servicios), y cómo estos pueden comunicarse mediante interfaces bien definidas.
El microkernel será responsable de:

Gestionar la comunicación entre los módulos.

Cargar, registrar y ejecutar operaciones.

Proveer servicios básicos comunes (por ejemplo, logging, validación de entrada, etc.).

Los módulos externos implementarán diferentes operaciones matemáticas, las cuales deberán ser fácilmente añadidas o removidas sin modificar el núcleo principal.

## Requisitos funcionales mínimos:
### Microkernel (Core):

Recibe la operación solicitada y sus parámetros.

Localiza el módulo correspondiente.

Ejecuta la operación y retorna el resultado.

Maneja errores y logs de ejecución.

### Módulos (Plug-ins):

Cada módulo implementa una operación específica, por ejemplo:

Suma

Resta

Multiplicación

División

Potencia

### otras funciones (puntos extra)
Los módulos se cargan dinámicamente (por ejemplo, desde una carpeta o registro).

## Interfaz de comunicación:

El microkernel debe definir una interfaz común que los módulos implementen.
Ejemplo: IOperation con métodos como getName() y execute(a, b).

## Extensibilidad:

Debe ser posible agregar nuevas operaciones sin modificar el código del microkernel.

Interfaz de usuario (opcional):

Puede ser una CLI, GUI o API sencilla para probar el sistema.
