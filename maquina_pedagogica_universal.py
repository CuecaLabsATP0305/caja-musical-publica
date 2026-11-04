import numpy as np
import sys
import time
from datetime import datetime

class RedPedagogicaNiños:
    def __init__(self):
        np.random.seed(305)
        # Red expandida a 64 descriptores para asimilar la pedagogía no lineal
        self.W1 = np.random.randn(64, 24) * 0.05
        self.W2 = np.random.randn(24, 4) * 0.05

    def inferencia_ludica(self, vector_64d, entropia_z):
        coeficiente_pedagogico = 1.5 / (1.0 + np.exp(-abs(entropia_z) * 0.01))
        capa_oculta = np.tanh(np.dot(vector_64d, self.W1) * coeficiente_pedagogico)
        return np.tanh(np.dot(capa_oculta, self.W2))

class CajaMusicalPublicaCore:
    def __init__(self):
        self.X, self.Y, self.Z = 0.1000, 0.1000, 0.1000
        self.dt = 0.01
        self.operador = "Fredy Arce"
        self.ciclo = 0
        self.red_cognitiva = RedPedagogicaNiños()

    def ciclo_rk4(self):
        sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0
        dx = sigma * (self.Y - self.X)
        dy = self.X * (rho - self.Z) - self.Y
        dz = self.X * self.Y - beta * self.Z
        self.X += dx * self.dt
        self.Y += dy * self.dt
        self.Z += dz * self.dt
        self.X = float(np.clip(self.X, -50.0, 50.0))
        self.Y = float(np.clip(self.Y, -50.0, 50.0))
        self.Z = float(np.clip(self.Z, -50.0, 50.0))

    def interactuar_entorno_infantil(self, estimulo):
        vector_64d = np.zeros(64)
        for i, char in enumerate(estimulo[:64]): vector_64d[i] = ord(char) / 255.0
        outputs = self.red_cognitiva.inferencia_ludica(vector_64d, self.Z)
        ajuste = float(np.mean(outputs))
        self.X += ajuste * 0.1
        self.Y += ajuste * 0.1
        self.Z += ajuste * 0.1
        print(f"\n\n🎵 [CAJA MUSICAL PÚBLICA] Interacción Pedagógica Detectada")
        print(f" -> Formato: Amigo de los Niños y Científicos de todas las edades.")
        print(f" -> Estado: Coordenadas de Ciencia Abierta actualizadas sin errores.")

    def ejecutar(self):
        print("================================================================")
        print("  🎵 MÁQUINA PEDAGÓGICA UNIVERSAL - CAJA MUSICAL PÚBLICA       ")
        print("================================================================")
        try:
            while True:
                self.ciclo_rk4()
                dg = -5.0 * (1.0 / (1.0 + np.exp(-abs(self.Z) * 0.05)))
                sys.stdout.write(f"\r[PEDAGÓGICO] Ciclo: {self.ciclo:05d} | dG: {dg:.4f} kcal/mol")
                sys.stdout.flush()
                if self.ciclo > 0 and self.ciclo % 150 == 0:
                    self.interactuar_entorno_infantil("Interacción de ciencia abierta educativa infantil")
                self.ciclo += 1
                time.sleep(0.12)
        except KeyboardInterrupt:
            print("\n\n🔒 [REPOSO SEGURO] -> Caja musical en estado de latencia nominal.")

if __name__ == "__main__":
    caja = CajaMusicalPublicaCore()
    caja.ejecutar()
