# -*- coding: utf-8 -*-
"""
Modulo de Calibracion Adaptativa y Filtrado de Ruido Estocastico
Caja Musical Publica - Ecosistema de Acceso Universal
"""
import numpy as np

class ThereminCalibrator:
    def __init__(self, window_size=10):
        self.window_size = window_size
        self.buffer = []
        self.baseline = 0.0

    def calibrate_environment(self, sample_data):
        """Establece el umbral homeostatico del entorno fisico."""
        if len(sample_data) == 0:
            self.baseline = 1.0
        else:
            self.baseline = float(np.mean(sample_data))
        return self.baseline

    def filter_signal(self, raw_value):
        """Aplica un filtro de suavizado para eliminar el ruido de la señal."""
        self.buffer.append(raw_value)
        if len(self.buffer) > self.window_size:
            self.buffer.pop(0)
        
        # Retorna la media mitigando fluctuaciones abruptas
        return float(np.mean(self.buffer))

if __name__ == "__main__":
    print("Instanciando calibrador adaptativo...")
    calibrator = ThereminCalibrator()
    print("Filtro operativo con precision matematica.")
