import sys
import os
import getpass
from cuecalabs_neuro_adapt import NeuroAdaptiveBridge

class CuecaLabsKernel:
    def __init__(self):
        self.token = "CuecaLabs_Termux"
        self.bridge = NeuroAdaptiveBridge()

    def menu_interactivo(self):
        while True:
            print("\n🏛️ Menú de Acceso Global (CuecaLabs v0305):")
            print("1. Lanzar Monitor Espejo Adaptativo (Todas las capas humanas)")
            print("2. Invocar Sensor Teremín Físico Pasivo")
            print("3. Consola de Inyección de Comandos Superiores (Solo Programador)")
            print("4. Salir de la Maquinaria")
            
            try:
                opcion = input("\n[Selección] > ").strip()
                
                if opcion == "1":
                    print("\n=== SENSOR INFORMÁTICO UNIVERSAL ACTIVO ===")
                    print("El sistema está operando en escucha interfactual espejo.\n")
                    try:
                        edad = int(input("[Entrada-Universal] Ingrese Edad del Receptor: ").strip())
                        cie = input("[Entrada-Universal] Ingrese Código CIE-11 (Presione Enter si no aplica): ").strip()
                        cie = None if cie == "" else cie
                        
                        # Ejecución del puente neuro-adaptativo biofísico
                        self.bridge.conmutar_interfaz_no_lineal(edad, cie)
                    except ValueError:
                        print("[ERROR] La edad debe ser un gradiente numérico puro.")
                        
                elif opcion == "2":
                    print("\n[TEREMÍN] Monitoreando oscilaciones de contorno... Estable (0.1000)")
                    
                elif opcion == "3":
                    print("\n[AUTENTICACIÓN] Ingrese su FIRMA CRIPTOGRÁFICA seguida de la instrucción:")
                    cmd = getpass.getpass("[Token-Raíz]> ").strip()
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
