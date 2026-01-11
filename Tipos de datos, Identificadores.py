"""
Programa: Cálculo del área de un rectángulo
Descripción: Este programa solicita al usuario sus datos y calcula
el área de un rectángulo a partir de la base y la altura ingresadas.
"""

# Solicitar el nombre del usuario (string)
nombre_usuario = input("Ingrese su nombre: ")

# Solicitar base y altura del rectángulo (float)
base_rectangulo = float(input("Ingrese la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

# Validar si los datos ingresados son positivos (boolean)
datos_validos = base_rectangulo > 0 and altura_rectangulo > 0

# Contador de intentos (int)
intentos = 1

# Verificar si los datos son correctos
if datos_validos:
    # Cálculo del área (float)
    area_rectangulo = base_rectangulo * altura_rectangulo

    # Mostrar resultado
    print(f"\nHola {nombre_usuario}")
    print(f"El área del rectángulo es: {area_rectangulo}")
else:
    print("\nError: La base y la altura deben ser mayores que cero.")