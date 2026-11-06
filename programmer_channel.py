import numpy as np
import time
import sys

class CanalProgramador:
    def __init__(self):
        # Inicialización basada en los valores nominales de la consola de CuecaLabs
        self.X = 0.1000  # Ciclo Celular
        self.Y = 0.1000  # Receptores
        self.Z = 0.1000  # Entropía / Disipación Térmica
        self.paso_tiempo = 0.01

    def integrar_rk4_lorenz(self):
        """Simula la actualización fractal del espacio de fases (Atractor acoplado)."""
        # Parámetros estándar del sistema adaptativo de no-equilibrio
        sigma, rho, beta = 10.0, 28.0, 8.0/3.0
        
        # Derivadas instantáneas
        dx = sigma * (self.Y - self.X)
        dy = self.X * (rho - self.Z) - self.Y
        dz = self.X * self.Y - beta * self.Z
        
        # Actualización de estados por paso diferencial finito
        self.X += dx * self.paso_tiempo
        self.Y += dy * self.paso_tiempo
        self.Z += dz * self.paso_tiempo

    def bucle_principal(self):
        print("================================================================")
        print(" INTERFAZ DE MONITOREO DE LAZO CERRADO - CANAL DEL PROGRAMADOR ")
        print("================================================================")
        print("[ESTADO GLOBAL] : OPERACIÓN_NOMINAL")
        print("[FIRMA DIGITAL] : cuecalabs ATP 0305\n")
        
        try:
            iteracion = 0
            while True:
                self.integrar_rk4_lorenz()
                
                # Minimización determinista simulada de la energía libre (Gibbs)
                dg_total = -5.0 + (1.0 / (1.0 + np.exp(-self.Z * 0.1)))
                
                # Impresión síncrona en una sola línea para evitar saturación de la terminal
                sys.stdout.write(
                    f"\r[CICLO {iteracion:04d}] X: {self.X:+.4f} | Y: {self.Y:+.4f} | Z: {self.Z:+.4f} || dG: {dg_total:+.4f} kcal/mol"
                )
                sys.stdout.flush()
                
                iteracion += 1
                time.sleep(0.2)
                
        except KeyboardInterrupt:
            print("\n\n================================================================")
            print("[MAQUINA PRIVADA] -> Interfaz Cerrada de Forma Segura en el Borde.")
            print("================================================================")

if __name__ == "__main__":
    canal = CanalProgramador()
    canal.bucle_principal()
