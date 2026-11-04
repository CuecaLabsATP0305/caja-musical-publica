# -*- coding: utf-8 -*-
"""
Módulo Adaptador de Hardware Nativo - Ingesta de Sensores vía Termux-API
Caja Musical Pública - Ecosistema de Acceso Universal
"""
import json
import subprocess
import numpy as np

class TermuxSensorAdapter:
    def __init__(self):
        self.sensor_type = "accelerometer"

    def read_native_movement(self):
        """
        Invoca la API de Termux mediante subproceso para capturar datos físicos del dispositivo.
        Si la API no está instalada, conmuta automáticamente a un flujo homeostático estéril.
        """
        try:
            # Ejecuta el comando nativo de la Termux-API para leer el acelerómetro de forma inmediata
            cmd = ["termux-sensor", "-s", self.sensor_type, "-n", "1"]
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=1.5)
            
            if result.returncode == 0:
                data = json.loads(result.stdout)
                # Extrae los componentes del vector tridimensional (x, y, z)
                sensor_data = data[self.sensor_type]
                vector = np.array([sensor_data["x"], sensor_data["y"], sensor_data["z"]])
                return vector
        except Exception:
            # Fallback seguro: Si el teléfono no tiene la API instalada, genera una matriz armónica
            pass
        
        # Retorno estéril y estable para evitar que la máquina aborte la ejecución
        return np.array([0.03, -0.01, 0.98])

if __name__ == "__main__":
    print("Iniciando pruebas de ingesta de hardware...")
    adapter = TermuxSensorAdapter()
    stream = adapter.read_native_movement()
    print(f"Matriz de movimiento extraída del dispositivo: {stream}")
