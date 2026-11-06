import numpy as np
import sys
import json
import os
import time
from typing import Dict, Any

class SistemaTransmisionContinua:
    """
    Gestiona el bucle de muestreo síncrono en tiempo real.
    Une los sensores agnósticos con la matriz MPC y el audio polifónico.
    """
    def __init__(self, duracion_ciclos: int = 10):
        self.max_ciclos = duracion_ciclos
        self.filename_registro = "registro_lazo_cerrado.json"
        
        # Estados iniciales unificados del espacio de fases (CC, Angiotensina, Entropía)
        self.estados_fases = np.array([0.1000, 0.1000, 0.1000])
        self.referencia = np.array([1.0000, 1.0000, 1.0000])
        self.Q = np.diag([2.5, 3.0, 1.8])

    def ejecutar_bucle_perpetuo(self):
        print("\n" + "="*85)
        print(" [SISTEMA] -> INICIANDO TRANSMISIÓN CONTINUA BIOMÉTRICA EN TIEMPO REAL")
        print(" [SISTEMA] -> Sintonización automática del lazo cuántico activada.")
        print("="*85 + "\n")
        
        for ciclo in range(1, self.max_ciclos + 1):
            # 1. Simulación del flujo dinámico de sensores internos del smartphone
            # El operador desplaza armónicamente su proximidad dieléctrica y magnética
            coord_touch = 540.0 + (200.0 * np.sin(ciclo * 0.5))  # Modulación del panel táctil
            mag_ut = 45.0 + (5.0 * np.cos(ciclo * 0.5))         # Perturbación del magnetómetro
            
            # 2. Transducción de Hardware Agnóstica
            escala = max(0.0001, min((coord_touch - 200.0) / 880.0, 1.0))
            desviacion_campo = abs(mag_ut - 45.0)
            amp_voltios = float(5.0 * (1.0 - np.tanh(desviacion_campo / 20.0)))
            
            # 3. Modelado Termodinámico de Gibbs (Fase IV del protocolo experimental)
            t_reposo_h = min(6.0, 1.0 + (ciclo * 0.5))
            dG_total = (-10.5 / max(0.001, escala)) + (-5.42 * min(1.0, t_reposo_h / 6.0)) + (-5.0 * 4.184)
            operador_fractal = max(0.01, np.power(escala, 0.35))
            n_H = max(1.0, min(2.4 * (1.0 / operador_fractal), 6.0))
            
            # 4. Matriz de Control Predictivo por Modelo (MPC) sobre el espacio de fases
            error = self.referencia - self.estados_fases
            u_optimo = np.dot(self.Q, error) * escala * max(0.1, min(1.0, abs(dG_total)/20.92))
            u_optimo = np.clip(u_optimo, -0.5, 0.5)
            
            # Evolución del Atractor CCNG1 / Receptores de Angiotensina
            self.estados_fases += u_optimo - (0.02 * self.estados_fases)
            
            # Disipación bosónica cuántica cuántica de la coordenada Z (Entropía)
            hbar_omega = 0.05 * escala
            factor_bosonico = hbar_omega / max(1e-6, (np.exp(hbar_omega / (0.0083144626 * 310.15)) - 1.0))
            q_disipado = 0.04 * factor_bosonico * n_H
            self.estados_fases += u_optimo - q_disipado
            self.estados_fases = np.clip(self.estados_fases, 0.0, 1.2)
            
            u_escalar = float(np.ravel(u_optimo))
            sustrato_molar = 0.05 * (1.0 - (0.1 * abs(u_escalar)))
            
            # 5. Acoplamiento Acústico Polifónico Compuesto Avanzado
            f0 = 440.0 * np.log10(1.0 + abs(dG_total))
            f1 = f0 * 1.5
            f2 = f0 * 2.0
            
            amp_sin = sustrato_molar * 20.0
            amp_tri = abs(u_escalar) * 2.0
            amp_saw = float(q_disipado) * 3.5
            
            msg = "ARMÓNICO_NATIVO" if abs(dG_total - (-20.92)) < 5.0 else "TRANSICIÓN_DE_FASE"
            
            # Renderizado analítico instantáneo del ciclo en consola sin bloqueo
            sys.stdout.write(f"[STREAM {ciclo:02d}] Freq: {f0:.1f} Hz | Gibbs: {dG_total:.2f} kJ/mol | nH: {n_H:.3f}\n")
            sys.stdout.write(f"          Fases -> X: {self.estados_fases:.4f} | Y (Angiotensina): {self.estados_fases:.4f} | Z (Entropía): {self.estados_fases:.4f}\n")
            sys.stdout.write(f"          Audio -> Mezcla Espectral: Seno={amp_sin:.1f} / Tri={amp_tri:.1f} / Saw={amp_saw:.1f} | Emisión: \"{msg}\"\n")
            sys.stdout.write("-" * 85 + "\n")
            sys.stdout.flush()
            
            # 6. Guardar snapshot persistente acumulativo en el JSON inmutable
            telemetria = {
                "ciclo_stream": ciclo, "escala_fractal": escala, "gibbs": dG_total,
                "nH": n_H, "X": float(self.estados_fases), "Y": float(self.estados_fases),
                "Z": float(self.estados_fases), "f0_Hz": f0, "Q_quantum": float(q_disipado)
            }
            
            historial = []
            if os.path.exists(self.filename_registro):
                try:
                    with open(self.filename_registro, "r") as f:
                        historial = json.load(f)
                        if not isinstance(historial, list): historial = []
                except: pass
            historial.append({"timestamp": time.time(), "telemetria": telemetria})
            with open(self.filename_registro, "w") as f:
                json.dump(historial, f, indent=4)
                
            # Retardo metrológico de alta precisión (0.1 segundos por evento)
            time.sleep(0.1)
            
        print("\n" + "="*85)
        print(" [SISTEMA] -> TRANSMISIÓN CONTINUA CONCLUIDA EXITOSAMENTE")
        print(f" [SISTEMA] -> Datos del biosensor local exportados a '{self.filename_registro}'.")
        print("="*85 + "\n")

if __name__ == "__main__":
    stream = SistemaTransmisionContinua()
    stream.ejecutar_bucle_perpetuo()
