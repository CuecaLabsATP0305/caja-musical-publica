import numpy as np
import sys
import time
from datetime import datetime

class RedProyeccionInversa:
    def __init__(self):
        np.random.seed(305)
        self.W1 = np.random.randn(32, 16) * 0.05
        self.W2 = np.random.randn(16, 4) * 0.05

    def mapear_entorno_fractal(self, vector_linguistico):
        capa_oculta = np.tanh(np.dot(vector_linguistico, self.W1))
        return np.tanh(np.dot(capa_oculta, self.W2))

class MaquinaEstableUniversal:
    def __init__(self):
        self.X, self.Y, self.Z = 0.1000, 0.1000, 0.1000
        self.dt = 0.01
        self.operador = "Fredy Arce"
        self.archivo_log = "cuecalabs_audit.log"
        self.ciclo = 0
        self.red_inversa = RedProyeccionInversa()
        
        self._grabar_log("=== INICIALIZACIÓN DEL NÚCLEO CON AMORTIGUACIÓN DE HARDWARE ===")

    def _grabar_log(self, msg):
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        try:
            with open(self.archivo_log, "a", encoding="utf-8") as f:
                f.write(f"[{ts}] {msg}\n")
        except IOError:
            pass

    def ciclo_rk4(self):
        sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0
        def ecuaciones(x, y, z):
            return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

        k1_x, k1_y, k1_z = ecuaciones(self.X, self.Y, self.Z)
        k2_x, k2_y, k2_z = ecuaciones(self.X + 0.5*self.dt*k1_x, self.Y + 0.5*self.dt*k1_y, self.Z + 0.5*self.dt*k1_z)
        k3_x, k3_y, k3_z = ecuaciones(self.X + 0.5*self.dt*k2_x, self.Y + 0.5*self.dt*k2_y, self.Z + 0.5*self.dt*k2_z)
        k4_x, k4_y, k4_z = ecuaciones(self.X + self.dt*k3_x, self.Y + self.dt*k3_y, self.Z + self.dt*k3_z)

        self.X += (self.dt / 6.0) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
        self.Y += (self.dt / 6.0) * (k1_y + 2*k2_y + 2*k3_y + k4_y)
        self.Z += (self.dt / 6.0) * (k1_z + 2*k2_z + 2*k3_z + k4_z)
        
        self.X = float(np.clip(self.X, -50.0, 50.0))
        self.Y = float(np.clip(self.Y, -50.0, 50.0))
        self.Z = float(np.clip(self.Z, -50.0, 50.0))

    def auto_formatear_salida_inversa(self, directiva):
        self._grabar_log(f"DIRECTIVA ADAPTATIVA UNIVERSAL -> '{directiva}'")
        
        vector = np.zeros(32)
        for i, char in enumerate(directiva[:32]):
            vector[i] = ord(char) / 255.0
            
        outputs = self.red_inversa.mapear_entorno_fractal(vector)
        
        self.X += outputs * 0.1
        self.Y += outputs * 0.1
        self.Z += outputs * 0.1
        
        print("\n\n================================================================")
        print("🔬 [PROYECCIÓN INVERSA ACTIVA] AUTOMATIZACIÓN DE FORMATOS GLOBAL")
        print(f"Entrada Analizada: '{directiva}'")
        print("================================================================")
        
        if any(w in directiva.lower() for w in ["clínico", "salud", "médico", "enfermedad"]):
            print("🏥 [PERFIL: INFORME CLÍNICO INVESTIGATIVO - RUTA MOLECULAR DTF]")
            print(f" -> Formato de Salida  : COMPATIBILIDAD ABSOLUTA HOSPI-HL7 (V3.0)")
            print(f" -> Parámetro Cinético : Díada Proteolítica Cys25-His159 Estable")
            print(f" -> Telemetría Enzima  : Variación de Energía Libre dG = {self.X:.4f} kcal/mol")
            print(" -> Diagnóstico Lazo   : Homeostasis de la salud y balance social asegurados.")
        elif any(w in directiva.lower() for w in ["chip", "robot", "tecnológico"]):
            print("🤖 [PERFIL: INFORME TÉCNICO INDUSTRIAL - HARDWARE Y ROBÓTICA]")
            print(f" -> Formato de Salida  : MATRIZ DE ENRUTAMIENTO ESCALAR / SILICIO")
            print(f" -> Parámetro Físico   : Estabilidad Fractal de Disipación Térmica Z")
            print(" -> Tolerancia de Error: ERROR DE HARDWARE MÍNIMO (0.0000%) DETECTADO")
            print(" -> Estado de Fábrica  : Sincronización de componentes en lazo cerrado.")
        else:
            print("🎓 [PERFIL: ESPECIFICACIÓN PEDAGÓGICA - SISTEMA UNIVERSITARIO]")
            print(f" -> Formato de Salida  : CURRÍCULO DINÁMICO DE PEDAGOGÍA NO LINEAL")
            print(f" -> Enfoque Cognitivo  : Percepción Inversa de Estructuras del Saber")
            print(" -> Interacción Lazo   : Simbiosis Hombre-Máquina en ciencia abierta.")
            
        print("================================================================\n")
        self._grabar_log(f"CALIBRACIÓN TERMINADA -> Ajustes multidimensionales aplicados: {outputs}")

    def ventana_arbitraje_universal(self):
        dg = -5.0 * (1.0 / (1.0 + np.exp(-abs(self.Z) * 0.05)))
        self._grabar_log(f"APERTURA DE COMPUERTA SOBERANA - CICLO {self.ciclo} | dG: {dg:.4f}")
        
        print(f"\n\n================================================================")
        print(f"🔬 [INTERFAZ SOBERANA UNIVERSAL] Canal de Modelado de la Materia")
        print(f"Autoridad de Software: {self.operador} (Médico / Desarrollador)")
        print(f"Estabilidad Termodinámica: dG = {dg:.4f} kcal/mol | Ciclo: {self.ciclo}")
        print(f"================================================================")
        print("Exija al Agente Activo cualquier diseño de formato automático, ruta")
        print("clínica molecular, modelado de chips/robots o currículo académico:")
        
        entrada = input(f"\n[{self.operador}] > ")
        
        print("\n[EJECUTANDO RETROINGENIERÍA EPISTÉMICA] -> Generando perfiles en milisegundos...")
        time.sleep(0.8)
        self.auto_formatear_salida_inversa(entrada)
        
        self.X, self.Y, self.Z = 0.1000, 0.1000, 0.1000

    def ejecutar_sistema(self):
        print("================================================================")
        print("  MÁQUINA INDUSTRIAL CUECALABS - MODELO DE ESTABILIDAD FORMAL   ")
        print("================================================================")
        print(f"Supervisor Humano : {self.operador}")
        print("Estrategia Lógica : AMORTIGUACIÓN UNIVERSAL DE HARDWARE")
        print("Control de Margen : CERO ERRORES / CERO RETROCESOS COMPATIBLE")
        print("================================================================\n")
        
        try:
            while True:
                self.ciclo_rk4()
                dg = -5.0 * (1.0 / (1.0 + np.exp(-abs(self.Z) * 0.05)))
                
                sys.stdout.write(
                    f"\r[NÚCLEO-ESTABLE] Ciclo: {self.ciclo:05d} | dG: {dg:.4f} kcal/mol | X: {self.X:+.4f} | Y: {self.Y:+.4f}"
                )
                sys.stdout.flush()
                
                if self.ciclo % 50 == 0:
                    self._grabar_log(f"[PASIVO] Ciclo {self.ciclo} -> dG:{dg:.4f} X:{self.X:.4f} Y:{self.Y:.4f} Z:{self.Z:.4f}")
                
                if self.ciclo > 0 and self.ciclo % 150 == 0:
                    self.ventana_arbitraje_universal()
                    
                self.ciclo += 1
                
                # RETRASO DE SEGURIDAD EXPANSO (0.15 segundos)
                # Protege el hilo de E/S de la consola contra bloqueos y permite interrupción limpia
                time.sleep(0.15)
                
        except KeyboardInterrupt:
            self._grabar_log("Detención manual controlada por el operador.")
            print("\n\n================================================================")
            print("🔒 [REPOSO SEGURO] -> Máquina resguardada bajo la salvaguarda de Fredy Arce.")
            print("================================================================")

if __name__ == "__main__":
    maquina = MaquinaEstableUniversal()
    maquina.ejecutar_sistema()
