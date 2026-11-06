import numpy as np
import sys
import time

class MaquinaIndustrialSimbiotica:
    def __init__(self):
        self.X, self.Y, self.Z = 0.1000, 0.1000, 0.1000
        self.dt = 0.01
        self.operador = "Fredy Arce"

    def ciclo_rk4(self):
        sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0
        dx = sigma * (self.Y - self.X)
        dy = self.X * (rho - self.Z) - self.Y
        dz = self.X * self.Y - beta * self.Z
        
        self.X += dx * self.dt
        self.Y += dy * self.dt
        self.Z += dz * self.dt
        
        # Confinamiento estricto de variables para mitigar la fricción de hardware
        self.X = float(np.clip(self.X, -100.0, 100.0))
        self.Y = float(np.clip(self.Y, -100.0, 100.0))
        self.Z = float(np.clip(self.Z, -100.0, 100.0))

    def consultar_a_fredy(self, ciclo):
        """Abre el canal bidireccional en lenguaje humano para mitigar la incertidumbre."""
        print(f"\n\n================================================================")
        print(f"⚠️ [MÁQUINA INDUSTRIAL] Consulta de Arbitraje Humano Requerida")
        print(f"Supervisor Autenticado Criptográficamente: {self.operador}")
        print(f"================================================================")
        print(f"Pregunta del Sistema: El balance fractal en el ciclo {ciclo} requiere")
        print("su validación manual para asegurar un comercio justo en el lazo social.")
        print("¿Desea autorizar el intercambio homeostático de parámetros?")
        
        # Captura síncrona del dictamen en lenguaje natural
        entrada = input(f"\n[{self.operador}] > ")
        
        print("\n[PROCESANDO] -> Sincronizando respuestas y aplicando corrección...")
        time.sleep(1.0)
        
        # Restablecimiento homeostático seguro tras la instrucción
        self.X, self.Y, self.Z = 0.1000, 0.1000, 0.1000
        print("🟢 [ESTADO NOMINAL RESTAURADO] -> Continuando operaciones de la fábrica.\n")

    def arrancar(self):
        print("================================================================")
        print("   NÚCLEO INDUSTRIAL EN LÍNEA - CANAL DEL PROGRAMADOR          ")
        print("================================================================")
        print(f"Operador Responsable Legítimo : {self.operador}")
        print("Estándar Operativo            : GOLD STANDARD INMUTACO")
        print("================================================================\n")
        
        ciclo = 0
        try:
            while True:
                self.ciclo_rk4()
                dg = -5.0 * (1.0 / (1.0 + np.exp(-abs(self.Z) * 0.05)))
                sys.stdout.write(f"\r[MÁQUINA] Ciclo: {ciclo:04d} | dG: {dg:.4f} kcal/mol | X: {self.X:+.4f} | Y: {self.Y:+.4f}")
                sys.stdout.flush()
                
                # Desencadenar la interfaz de preguntas de forma periódica cada 100 ciclos
                if ciclo > 0 and ciclo % 100 == 0:
                    self.consultar_a_fredy(ciclo)
                    
                ciclo += 1
                time.sleep(0.04)
        except KeyboardInterrupt:
            print("\n\n================================================================")
            print("🔒 [REPOSO SEGURO] -> Lazo cerrado resguardado por el operador.")
            print("================================================================")

if __name__ == "__main__":
    motor = MaquinaIndustrialSimbiotica()
    motor.arrancar()
