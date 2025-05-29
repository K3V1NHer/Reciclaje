# Resumen del proyecto 

El proyecto es una aplicación de consola diseñada para gestionar el registro y seguimiento de materiales reciclados por diferentes familias. Permite a los usuarios registrar nuevas familias en el sistema, ingresar los materiales reciclados por cada familia (especificando el tipo, peso y fecha), y visualizar resúmenes de la cantidad de materiales reciclados y los puntos acumulados por cada familia.

**Funcionalidades Clave:**

* **Registro de Familias:** Los usuarios pueden agregar información básica sobre las familias participantes (nombre, número de integrantes, dirección).
* **Registro de Materiales Reciclados:** El sistema permite registrar diferentes tipos de materiales (plástico, vidrio, papel) con su respectivo peso y fecha de reciclaje. A cada tipo de material se le asigna un sistema de puntuación diferente.
* **Resúmenes de Reciclaje:** La aplicación genera resúmenes que muestran la cantidad de cada material reciclado por familia y los puntos totales acumulados, lo que permite visualizar el esfuerzo de reciclaje de cada una.

**Estructura Técnica:**

* El proyecto sigue un patrón Modelo-Vista-Controlador (MVC) para organizar el código.
* **Modelo:** Define las clases para representar los datos (`Familia`, `MaterialReciclado`, `Plastico`, `Vidrio`, `Papel`) y la lógica de negocio (cálculo de puntos).
* **Vista:** Se encarga de la interacción con el usuario a través de la consola (mostrar menús, solicitar entradas, mostrar resultados).
* **Controlador:** Coordina las acciones entre el modelo y la vista, gestionando el flujo de la aplicación.

En resumen, este proyecto proporciona una herramienta básica pero funcional para llevar un registro del reciclaje a nivel familiar, con el objetivo de promover y facilitar la gestión de los esfuerzos de reciclaje.