# Tarea: Aplicación de Conceptos de POO en Python
# Autor: [Anahi Grefa]
# Descripción: Ejemplo de herencia, encapsulación y polimorfismo

# 1. CLASE BASE (Demuestra Encapsulación)
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        # Atributo privado (__salario) para aplicar ENCAPSULACIÓN
        self.__salario = salario

    # Método Getter para acceder al salario de forma segura
    def get_salario(self):
        return self.__salario

    # Método Setter para modificar el salario con validación
    def set_salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self.__salario = nuevo_salario
        else:
            print("Error: El salario debe ser mayor a 0")

    # Método que será sobrescrito (Polimorfismo)
    def calcular_salario(self):
        return self.__salario

    def mostrar_info(self):
        print(f"Empleado: {self.nombre} | Salario Base: ${self.get_salario()}")


# 2. CLASE DERIVADA (Demuestra HERENCIA)
class EmpleadoAdministrativo(Empleado):
    def __init__(self, nombre, salario, bono):
        # Uso de super() para heredar atributos de la clase padre
        super().__init__(nombre, salario)
        self.bono = bono

    # 3. POLIMORFISMO (Sobrescritura de método)
    # Modificamos el comportamiento de calcular_salario para incluir el bono
    def calcular_salario(self):
        return self.get_salario() + self.bono

    # Sobrescritura de mostrar_info para mostrar detalles específicos
    def mostrar_info(self):
        print(f"Empleado Administrativo: {self.nombre} | "
              f"Salario Total (con bono): ${self.calcular_salario()}")


# 4. PROGRAMA PRINCIPAL (Instanciación de OBJETOS)
if __name__ == "__main__":
    print("--- Demostración de POO ---")

    # Creación de objetos
    empleado1 = Empleado("Jaela", 600)
    empleado2 = EmpleadoAdministrativo("Anahi", 850, 150)

    # Uso de métodos y Polimorfismo
    # Aunque ambos tienen el mismo método, actúan diferente
    empleado1.mostrar_info()
    empleado2.mostrar_info()

    print("\n--- Demostración de Encapsulación ---")
    # Intentamos cambiar el salario del empleado1 usando el Setter
    print(f"Salario antiguo de {empleado1.nombre}: ${empleado1.get_salario()}")
    empleado1.set_salario(750)
    print(f"Nuevo salario de {empleado1.nombre}: ${empleado1.get_salario()}")
