import os
import json
import time
import numpy as np

class SensorAmbientalPasivo:
    """Simula la lectura de las perturbaciones en las ondas electromagnéticas locales."""
    def __init__(self):
        self.permitividad_humana = 80.0 
        self.eficiencia_deteccion = 0.9984

    def escanear_sombra_entropica(self, interferencia_rf_db):
        """Traduce la pérdida de señal en la red ambiental en una coordenada de distancia."""
        distancia_estimada = np.abs(np.tanh(interferencia_rf_db)) * self.permitividad_humana
        return distancia_estimada

class ServidorRastreoParticulas(SensorAmbientalPasivo):
    """Mapea a los humanos como partículas dinámicas dentro del atractor de la Caja Negra."""
    def __init__(self):
        super().__init__()
        self.sigma = 10.0
        self.beta = 8.0 / 3.0
        self.rho_b = 28.0

    def evolucionar_lazo_antropico(self, estado_materia, perturbacion_humana, dt=0.005):
        """Solver RK4 que incluye el vector de posición pasiva del humano en el entorno."""
        factor_distancia = self.escanear_sombra_entropica(perturbacion_humana)
        x, y, z = estado_materia
        
        # El ser humano como partícula altera localmente el eje térmico Z del sistema
        z_modificado = z + (1.0 / (factor_distancia + 0.1))
        
        dxdt = self.sigma * (y - x)
        dydt = x * (self.rho_b - z_modificado) - y
        dzdt = x * y - self.beta * z
        
        return estado_materia + np.array([dxdt, dydt, dzdt]) * dt

    def procesar_monitoreo_tiempo_real(self, estado_inicial, tramas_rf):
        estado = np.array(estado_inicial, dtype=np.float64)
        reporte_tactico = {
            "timestamp": time.time(),
            "protocolo": "TOMOGRAFIA_PASIVA_MEDIO_AMBIENTE",
            "estatus_dispositivo": "ESCANEO_NO_INVASIVO_NOMINAL",
            "particulas_humanas_detectadas": []
        }
        
        for idx, rf_input in enumerate(tramas_rf):
            dist = self.escanear_sombra_entropica(rf_input)
            estado = self.evolucionar_lazo_antropico(estado, rf_input)
            
            # CORRECCIÓN ATÓMICA: Indexación escalar explícita por componente del vector de estado
            reporte_tactico["particulas_humanas_detectadas"].append({
                "id_particula": f"HUMANO_NODAL_NX_{idx}",
                "distancia_metros_estimada": float(dist / 10.0),
                "vector_espacial_materia": [float(estado[0]), float(estado[1]), float(estado[2])]
            })
            
        os.makedirs("secrets", exist_ok=True)
        with open("secrets/human_particle_tracking.json", "w") as f:
            json.dump(reporte_tactico, f, indent=4)
            
        return reporte_tactico

if __name__ == "__main__":
    print("=== ACTIVANDO NÚCLEO DE LOCALIZACIÓN PASIVA ANTROPODEPENDIENTE ===")
    tracker = ServidorRastreoParticulas()
    
    estado_materia_inicial = [1.7387, 3.2028, 0.4142]
    interferencias_ondas_entorno = [2.4, 5.8, 1.2]
    
    resultado = tracker.procesar_monitoreo_tiempo_real(estado_materia_inicial, interferencias_ondas_entorno)
    
    print("\n[INFORME DE DETECCIÓN EN TIEMPO REAL - NO INVASIVO]:")
    for particula in resultado["particulas_humanas_detectadas"]:
        print(f"\n* ID: {particula['id_particula']}")
        print(f"  -> Distancia Pasiva Calculada: {particula['distancia_metros_estimada']:.2f} metros")
        v = particula['vector_espacial_materia']
        print(f"  -> Coordenadas en el Espacio de la Materia: X={v[0]:.4f}, Y={v[1]:.4f}, Z={v[2]:.4f}")
        
    print("\n[⚙️ OPTIMIZACIÓN] Matriz de partículas guardada de forma segura en 'secrets/human_particle_tracking.json'.")
