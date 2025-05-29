# Resumen del proyecto 

El proyecto es una aplicación de consola diseñada para gestionar el registro y seguimiento de materiales reciclados por diferentes familias. Permite a los usuarios registrar nuevas familias en el sistema, ingresar los materiales reciclados por cada familia (especificando el tipo, peso y fecha), y visualizar resúmenes de la cantidad de materiales reciclados y los puntos acumulados por cada familia.


**Estructura del Proyecto (MVC):**

El código se organiza en los siguientes componentes clave, siguiendo el patrón MVC:

* **`main.py` (Punto de Entrada):**
    * Este archivo actúa como el punto de inicio de la aplicación.
    * Su función principal es crear una instancia de la clase `Controlador` (del archivo `Reciclaje_controller.py`) y llamar al método `ejecutar()` para poner en marcha la aplicación.
* **`Reciclaje_controller.py` (Controlador):**
    * **Clase `Controlador`:**
        * `__init__(self)`: Inicializa la lista `familias`, que almacena objetos de la clase `Familia`.
        * `ejecutar(self)`:
            * Muestra el menú principal de la aplicación (`Reciclaje_view.py`).
            * Gestiona la entrada del usuario para seleccionar opciones del menú.
            * Llama a otros métodos del `Controlador` para realizar las acciones correspondientes (registrar familia, registrar material, mostrar resúmenes).
            * Controla el flujo principal de la aplicación.
        * `registrar_familia(self)`:
            * Llama a la función `pedir_familia()` (`Reciclaje_view.py`) para obtener los datos de la nueva familia.
            * Crea un objeto `Familia` (`Reciclaje_model.py`) con los datos ingresados.
            * Añade el objeto `Familia` a la lista `familias`.
        * `registrar_material(self)`:
            * Verifica si hay familias registradas.
            * Llama a la función `seleccionar_familia()` (`Reciclaje_view.py`) para que el usuario elija una familia.
            * Llama a la función `pedir_material()` (`Reciclaje_view.py`) para obtener los datos del material reciclado.
            * Crea un objeto de la clase correspondiente al tipo de material (`Plastico`, `Vidrio`, o `Papel` - `Reciclaje_model.py`).
            * Añade el objeto del material a la lista de materiales de la familia seleccionada.
        * `mostrar_resumenes(self)`:
            * Verifica si hay familias registradas.
            * Itera sobre la lista `familias` y llama a la función `mostrar_resumen()` (`Reciclaje_view.py`) para mostrar el resumen de cada familia.
* **`Reciclaje_model.py` (Modelo):**
    * **Clase `MaterialReciclado`:**
        * Clase base para representar cualquier material reciclable.
        * `__init__(self, tipo, peso, fecha)`: Inicializa los atributos `tipo`, `peso` y `fecha`.
        * `calcular_puntos(self)`: Método para calcular los puntos (implementación base).
    * **Clases `Plastico`, `Vidrio`, `Papel`:**
        * Heredan de `MaterialReciclado`.
        * Sobrescriben el método `calcular_puntos()` para implementar el cálculo específico de puntos para cada tipo de material.
    * **Clase `Familia`:**
        * Representa a una familia.
        * `__init__(self, nombre, integrantes, direccion)`: Inicializa los datos de la familia.
        * `agregar_material(self, material)`: Añade un objeto de material reciclado a la lista de materiales de la familia.
        * `obtener_resumen(self)`:
            * Calcula el resumen de reciclaje de la familia (lista de materiales con sus puntos y el total de puntos).
            * Devuelve el resumen y el total.
* **`Reciclaje_view.py` (Vista):**
    * Contiene funciones para la interacción con el usuario a través de la consola.
    * `mostrar_menu()`: Muestra el menú principal de la aplicación.
    * `pedir_familia()`: Solicita al usuario los datos para registrar una nueva familia.
    * `seleccionar_familia(familias)`: Permite al usuario seleccionar una familia de la lista.
    * `pedir_material()`: Solicita al usuario los datos para registrar un material reciclado.
    * `mostrar_resumen(familia)`: Muestra el resumen de reciclaje de una familia.

**Flujo General de la Aplicación:**

1.  `main.py` inicia la aplicación creando un `Controlador`.
2.  El `Controlador` presenta el menú principal (a través de la `Vista`).
3.  El usuario selecciona una opción.
4.  El `Controlador` procesa la opción, interactuando con el `Modelo` para manipular los datos y con la `Vista` para mostrar información al usuario.
5.  La aplicación continúa hasta que el usuario elige salir.

