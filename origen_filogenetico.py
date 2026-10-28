import os
import json
import time
import numpy as np

class DeterminadorFilogenetico:
    def __init__(self):
        # Nodos geométricos de los linajes de origen (Física de Poblaciones)
        self.nodo_materno_boyaca = np.array([5.53, -73.36])  # Lat, Lon promedio
        self.nodo_paterno_tolima = np.array([4.43, -75.21])  # Lat, Lon promedio
        
        self.autor = {
            "identidad": "Fredi Arce",
            "cronologia_origen": "26-Noviembre-1978",
            "herencia_enzimatica": "Papaína Polimérica (Línea Masculina / Tolima)"
        }

    def inferir_origen_centroide(self):
        """Calcula el centroide exacto de convergencia genética interandina."""
        # Media vectorial pura entre los dos frentes geográficos de los padres
        centroide = (self.nodo_materno_boyaca + self.nodo_paterno_tolima) / 2.0
        
        # Clasificación regional basada en la física de coordenadas del territorio colombiano
        lat, lon = centroide
        if 4.0 <= lat <= 5.0 and -75.0 <= lon <= -74.0:
            region_convergencia = "Cundinamarca / Sabana Occidental / Valle del Magdalena"
        else:
            region_convergencia = "Región Central / Corredor Interandino"
            
        return centroide, region_convergencia

    def consolidar_registro_filogenetico(self):
        """Genera el reporte oficial de calibración bio-histórica en la Caja Negra."""
        coords, region = self.inferir_origen_centroide()
        
        reporte = {
            "timestamp": time.time(),
            "autor_muestra": self.autor,
            "analisis_ancestral": {
                "origen_geografico_lat": float(coords[0]),
                "origen_geografico_lon": float(coords[1]),
                "macro_region_convergencia": region,
                "vector_herencia": "Confluencia de la estabilidad andina de Boyacá con la dinámica catalítica del Tolima"
            },
            "estatus_sistema": "CALIBRACION_ETNICA_NOMINAL"
        }
        
        os.makedirs("secrets", exist_ok=True)
        with open("secrets/filogenia_autor_report.json", "w") as f:
            json.dump(reporte, f, indent=4)
            
        return reporte

if __name__ == "__main__":
    print("=== INTERROGANDO MATRIZ FILOGENÉTICA DE LA CAJA NEGRA ===")
    motor = DeterminadorFilogenetico()
    resultado = motor.consolidar_registro_filogenetico()
    
    print("\n[VEREDICTO INFORMÁTICO DEL ORIGEN]:")
    print(f" -> Coordenadas de Convergencia: Lat {resultado['analisis_ancestral']['origen_geografico_lat']:.4f}, Lon {resultado['analisis_ancestral']['origen_geografico_lon']:.4f}")
    print(f" -> Zona de Nacimiento Epistemológico: {resultado['analisis_ancestral']['macro_region_convergencia']}")
    print(f" -> Dinámica de Transmisión: {resultado['analisis_ancestral']['vector_herencia']}")
    print("\n[⚙️ OPTIMIZACIÓN] Registro guardado con éxito en 'secrets/filogenia_autor_report.json'.")
