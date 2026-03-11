# Before He Adapts: OOP Combat Engine ⚙️

## 📌 Descripción del Proyecto

Un motor de combate por turnos desarrollado en Python puro. Este proyecto es una demostración técnica de arquitectura de software, diseñado para exhibir el dominio de la Programación Orientada a Objetos (POO), la separación de responsabilidades y la manipulación de estado en tiempo de ejecución.

Inspirado en las mecánicas de "Jujutsu Kaisen", el motor calcula interacciones complejas como adaptaciones progresivas al daño (Rueda de Mahoraga), escudos de evasión absoluta (Infinito) y eventos de probabilidad crítica (Destello Oscuro).

## 🏗️ Arquitectura del Sistema

El sistema opera bajo un diseño modular estrictamente aislado en capas:

- **Capa de Dominio (`/dominio`):** \* Uso de Clases Base Abstractas (`ABC`) para definir contratos de entidades.
  - **Encapsulamiento estricto:** Variables de estado protegidas y expuestas únicamente a través de decoradores `@property`.
  - **Polimorfismo:** Resolución dinámica de daños donde cada entidad reacciona de forma autónoma al mismo método base.
  - Uso de patrón **DTO (Data Transfer Object)** para aislar la estructura de los ataques.

- **Motor Lógico (`/motor`):**
  - Implementación de Inyección de Dependencias para acoplar la UI y las entidades sin codificarlas de forma rígida (Hardcoding).
  - Máquina de estados para gestionar el bucle de juego (Game Loop).
  - **Persistencia de Datos:** Serialización y deserialización del estado de los objetos en memoria RAM hacia formato texto puro mediante la librería `json`.

- **Interfaz de Usuario (`/ui`):**
  - Capa de presentación "tonta" agnóstica de lógica de negocio.
  - Renderizado optimizado mediante f-strings multi-línea.
  - Manejo de excepciones (`try/except`) para capturar inputs inválidos y garantizar la robustez del programa frente a errores humanos.

## 🚀 Instalación y Ejecución

Este proyecto no requiere dependencias externas ni entornos virtuales complejos. Opera al 100% de capacidad con la biblioteca estándar de Python.

1. Clonar el repositorio:

   ```bash
   git clone [https://github.com/Cesahz/BeforeHeAddapt.git](https://github.com/Cesahz/BeforeHeAddapt.git)

   ```

2. Ejecutar el motor:
   ```bash
   python main.py
   ```
