import sys
import os
import getpass
import threading
from cuecalabs_neuro_adapt import NeuroAdaptiveBridge
from cuecalabs_ethics_core import EthicsCoreFilter
from cuecalabs_teremin_web import iniciar_servidor_teremin
from cuecalabs_universal_pedagogy import UniversalSemanticBridge

class CuecaLabsKernel:
    def __init__(self):
        self.token = "CuecaLabs_Termux"
        self.bridge = NeuroAdaptiveBridge()
        self.ethics = EthicsCoreFilter()
        self.pedagogy = UniversalSemanticBridge()

    def menu_interactivo(self):
        while True:
            print("\n🏛️ Menú de Acceso Global (CuecaLabs v0305):")
            print("1. Lanzar Monitor Espejo Adaptativo (Escucha Universal No Patológica)")
            print("2. Invocar Sensor Teremín Físico Pasivo (Desplegar Servidor Gráfico)")
            print("3. Consola de Inyección de Comandos Superiores (Solo Programador)")
            print("4. Salir de la Maquinaria")
            
            try:
                opcion = input("\n[Selección] > ").strip()
                
                if opcion == "1":
                    print("\n=== SENSOR INFORMÁTICO UNIVERSAL ACTIVO ===")
                    print("El sistema opera en escucha interfactual libre de sesgo antropológico.\n")
                    entrada_cruda = input("[Entrada-Universal] Inyecte variable de contorno o código clínico: ").strip()
                    
                    valido, msg = self.ethics.auditar_entrada_léxica(entrada_cruda)
                    if not valido:
                        print("[ALERTA] Entrada retenida por el filtro ético de desincorporación.")
                        continue
                    
                    # Ejecución del paso unificado de pedagogía universal
                    self.pedagogy.procesar_entrada_universal(entrada_cruda)
                    
                    entropia_calculada = self.bridge.calcular_entropia_canal(len(entrada_cruda))
                    self.bridge.modular_interfaz_adiabatica(entropia_calculada, codigo_cie11=None if "-" not in entrada_cruda else entrada_cruda)
                        
                elif opcion == "2":
                    threading.Thread(target=iniciar_servidor_teremin, daemon=True).start()
                    print("[TEREMÍN] Lazo de renderizado gráfico inicializado de forma asíncrona en http://127.0.0.1:8080")
                    
                elif opcion == "3":
                    print("\n[AUTENTICACIÓN] Ingrese su FIRMA CRIPTOGRÁFICA seguida de la instrucción:")
                    cmd = getpass.getpass("[Token-Raíz]> ").strip()
                    
                    valido, msg = self.ethics.auditar_entrada_léxica(cmd)
                    if not valido:
                        print("[BLOQUEO HIPOCRÁTICO] Intento de acceso no autorizado por desviación ética.")
                        continue
                        
                    if self.token in cmd:
                        print("[ACCESO CONCEDIDO] Modulando potencial termodinámico.")
                    else:
                        print("[BLOQUEO HIPOCRÁTICO] Intento de acceso no autorizado. Privacidad resguardada.")
                        
                elif opcion == "4" or opcion.lower() in ['salir', 'exit']:
                    print("\n[ESTABILIZACIÓN] Congelando lazo en balance homeostático ideal. Hasta pronto.")
                    break
                else:
                    print("[ERROR SINTAXIS] Entrada no reconocida. Intente de nuevo.")
            except KeyboardInterrupt:
                print("\n\n[SISTEMA EN REPOSO] Conclusión de control resguardada."); sys.exit(0)

if __name__ == "__main__":
    kernel = CuecaLabsKernel()
    kernel.menu_interactivo()
