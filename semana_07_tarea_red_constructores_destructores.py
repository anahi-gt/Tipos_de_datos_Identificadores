# =========================================================
# Tarea: Implementación de Constructores y Destructores
# Tema: Gestión de Transferencia de Datos en Red
# =========================================================

class TareaRed:
    """
    Clase base que representa una tarea de red (como una descarga).
    Demuestra la inicialización de recursos mediante __init__.
    """

    def __init__(self, id_tarea, recurso, tamano_kb):
        """
        CONSTRUCTOR: Se activa al iniciar la transferencia.
        """
        self.id_tarea = id_tarea
        self.recurso = recurso
        self.tamano_kb = tamano_kb
        self.estado = "Conectando..."

        print(f"[RED] Iniciando tarea #{self.id_tarea}: Preparando '{self.recurso}'")
        print(f"[RED] Ancho de banda reservado para {self.tamano_kb} KB.")

    def ejecutar(self):
        self.estado = "Descargando"
        print(f"[INFO] Tarea {self.id_tarea} en progreso... Estado: {self.estado}")

    def __del__(self):
        """
        DESTRUCTOR: Se activa al finalizar la tarea o perder la conexión.
        Asegura que el 'puerto' virtual se libere.
        """
        print(f"[LIMPIEZA] Cerrando socket de la tarea #{self.id_tarea}.")
        print(f"[LIMPIEZA] Puerto liberado. Recurso '{self.recurso}' finalizado.")


class DescargaSegura(TareaRed):
    """
    Clase derivada que añade una capa de cifrado.
    Muestra el uso de constructores heredados y polimorfismo.
    """

    def __init__(self, id_tarea, recurso, tamano_kb, protocolo="HTTPS"):
        """
        CONSTRUCTOR HIJO: Llama al padre y añade atributos propios.
        """
        super().__init__(id_tarea, recurso, tamano_kb)
        self.protocolo = protocolo
        self.cifrado_activo = True
        print(f"[SEGURIDAD] Capa SSL/TLS activada usando protocolo {self.protocolo}.")

    def ejecutar(self):
        """
        Redefinición del método (Polimorfismo).
        """
        print(f"[SEGURIDAD] Verificando certificados para '{self.recurso}'...")
        super().ejecutar()

    def __del__(self):
        """
        DESTRUCTOR HIJO: Realiza limpieza específica antes de llamar al padre.
        """
        print(f"[SEGURIDAD] Destruyendo llaves de cifrado de la tarea #{self.id_tarea}.")
        super().__del__()


# --- Demostración del ciclo de vida de los objetos ---

if __name__ == "__main__":
    print("--- INICIO DEL MONITOR DE RED ---\n")

    # 1. Instanciación: Se activan los constructores
    descarga_zip = TareaRed(501, "archivo_datos.zip", 4500)
    print("-" * 30)
    descarga_admin = DescargaSegura(901, "config_servidor.conf", 128, "SFTP")

    print("\n--- PROCESAMIENTO ---")
    descarga_zip.ejecutar()
    descarga_admin.ejecutar()

    print("\n--- FINALIZACIÓN DE RECURSOS ---")
    # 2. Eliminación manual: Se activan los destructores
    # El orden de salida mostrará primero la limpieza del hijo y luego la del padre
    del descarga_zip
    print("...")
    del descarga_admin

    print("\n--- MONITOR DE RED APAGADO ---")
