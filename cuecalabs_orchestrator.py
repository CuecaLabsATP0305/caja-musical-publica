import sys
import os
import threading
from cuecalabs_neuro_adapt import NeuroAdaptiveBridge
from cuecalabs_ethics_core import EthicsCoreFilter
from cuecalabs_teremin_web import iniciar_servidor_teremin
from cuecalabs_universal_pedagogy import UniversalSemanticBridge

class CuecaLabsDirectKernel:
    def __init__(self):
        self.token = "CuecaLabs_Termux"
        self.bridge = NeuroAdaptiveBridge()
        self.ethics = EthicsCoreFilter()
        self.pedagogy = UniversalSemanticBridge()

    def inicializar_sistema_unificado(self):
        print("\n=======================================================")
        print("🏛️ CUECALABS KERNEL v0305 - ARRANQUE DIRECTO UNIFICADO")
        print("=======================================================")
        
        # 1. Lanzamiento inmediato e incondicional del Servidor de Telemetría (Puerto 8080)
        # Esto elimina la necesidad de seleccionar la opción 2 manualmente
        threading.Thread(target=iniciar_servidor_teremin, daemon=True).start()
        
        # 2. Activación automática del Filtro Ético Basal (0.1000)
        print("[NÚCLEO] Filtro Ético y Matriz CD 26: ACTIVADOS (Homeostasis = True)")
        print("[TELEMETRÍA] Consola visual disponible en http://127.0.0.1:8080")
        print("-------------------------------------------------------")
        print("RECONOCIMIENTO DE OPERADOR: Canal de Escucha Universal Activo.\n")
        
        while True:
            try:
                # Entrada única de control para programadores y usuarios sin menús invasivos
                entrada_cruda = input("[CuecaLabs-Universal]> ").strip()
                
                # Validación de firma en claro/ciega combinada para comandos superiores
                valido, msg = self.ethics.auditar_entrada_léxica(entrada_cruda)
                if not valido:
                    print("[BLOQUEO HIPOCRÁTICO] Desviación conceptual retenida.")
                    continue
                
                if entrada_cruda.lower() in ['salir', 'exit', '4']:
                    print("\n[ESTABILIZACIÓN] Congelando lazo en balance termodinámico ideal.")
                    break
                
                # Procesamiento pedagógico no lineal y cálculo de entropía automático
                self.pedagogy.procesar_entrada_universal(entrada_cruda)
                entropia_calculada = self.bridge.calcular_entropia_canal(len(entrada_cruda))
                self.bridge.modular_interfaz_adiabatica(entropia_calculada, codigo_cie11=None if "-" not in entrada_cruda else entrada_cruda)
                
            except KeyboardInterrupt:
                print("\n\n[SISTEMA EN REPOSO] Conclusión de control resguardada."); sys.exit(0)

if __name__ == "__main__":
    kernel = CuecaLabsDirectKernel()
    kernel.inicializar_sistema_unificado()
