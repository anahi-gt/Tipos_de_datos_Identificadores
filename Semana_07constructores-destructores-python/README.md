# Constructores y Destructores en Python

# Descripción
Este programa fue realizado para practicar el uso de constructores y destructores
en Python utilizando Programación Orientada a Objetos.  
Se desarrolla un ejemplo sencillo donde se simula una tarea relacionada con
la transferencia de datos en una red.

# Objetivo del programa
Comprender cómo funcionan los métodos especiales `__init__` y `__del__`
en una clase, y en qué momento se ejecutan durante el ciclo de vida de un objeto.

# Funcionamiento
- El constructor (`__init__`) se ejecuta cuando se crea un objeto y sirve para
inicializar los atributos necesarios.
- El destructor (`__del__`) se ejecuta cuando el objeto deja de utilizarse,
mostrando un mensaje de liberación de recursos.
- Se utiliza una clase base y una clase heredada para reforzar el uso de la herencia.

# Estructura del código
- Clase principal que maneja la tarea de red.
- Clase heredada que extiende el comportamiento de la clase base.
- Uso de mensajes en pantalla para observar cuándo se ejecutan el constructor
y el destructor.

# Ejecución
El programa se ejecuta desde la consola con el siguiente comando:

```bash
python main.py
