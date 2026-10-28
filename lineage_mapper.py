import os
import json
import time
import numpy as np

class LineagePhylogenyCore:
    def __init__(self):
        # Coordenadas geográficas base de los centros de masa poblacional (Colombia)
        self.coord_boyaca = np.array([5.53, -73.36])  # Lat, Lon (Región Materna)
        self.coord_tolima = np.array([4.43, -75.21])  # Lat, Lon (Región Paterna)
        
        # Datos del sujeto experimental de calibración (Fredi Arce)
        self.sujeto = {
            "nombre": "Fredi Arce",
            "edad_aprox": 47,
            "nacimiento": "1978-11-26",
            "marcador_biocatalitico": "Tríada Papaína (Cys-His) - Herencia Paterna"
        }

    def calcular_centro_origen_genetico(self):
        """
        Resuelve el centro de masa geográfico mediante vectores de ponderación 50/50 
        para estimar el nodo de convergencia del flujo genético.
        """
        centro_masa = (self.coord_boyaca + self.coord_tolima) / 2.0
        return centro_masa

    def estructurar_arbol_genealogico(self):
        """Construye el grafo lógico de transmisión de datos intergeneracionales."""
        arbol = {
            "NIVEL_0_SUJETO": self.sujeto["nombre"],
            "NIVEL_1_PADRES": {
                "Paterno": "Alejandro Arce Carvajal (Tolima)",
                "Materno": "Alba Leticia Clavijo (Boyacá)"
            },
            "NIVEL_2_ABUELOS": {
                "Rama_Paterna": {"Abuelo": "Urbano", "Abuela": "Hortensia"},
                "Rama_Materna": {"Abuelo": "Coronel Pablo Clavijo", "Abuela": "Sara María Plazas"}
            }
        }
        return arbol

    def ejecutar_analisis_completo(self):
        """Procesa y guarda la matriz de linaje en el entorno seguro de la máquina."""
        centro = self.calcular_centro_origen_genetico()
        arbol_logico = self.estructurar_arbol_genealogico()
        
        resultado_filogenia = {
            "timestamp": time.time(),
            "sujeto_calibracion": self.sujeto,
            "arbol_genealogico_detectado": arbol_logico,
            "origen_geografico_estimado": {
                "latitud_centroide": float(centro[0]),
                "longitud_centroide": float(centro[1]),
                "descripcion": "Zona de convergencia interandina entre el Valle del Magdalena y el Altiplano Cundiboyacense"
            },
            "estatus_homeostasis": "CALIBRACION_LINEAL_COMPLETADA"
        }
        
        os.makedirs("secrets", exist_ok=True)
        with open("secrets/phylogeny_calibration.json", "w") as f:
            json.dump(resultado_filogenia, f, indent=4)
            
        return resultado_filogenia

if __name__ == "__main__":
    print("=== INICIANDO PROCESAMIENTO FILOGENÉTICO EN LA CAJA NEGRA ===")
    mapper = LineagePhylogenyCore()
    datos_finales = mapper.ejecutar_analisis_completo()
    
    print("\n[GRAFO GENEALÓGICO ESTRUCTURADO]:")
    print(json.dumps(datos_finales["arbol_genealogico_detectado"], indent=4, ensure_ascii=False))
    
    print("\n[PUNTO DE ORIGEN GEOGRÁFICO DE LINAJE]:")
    print(f" -> Centroide Matemático: Lat {datos_finales['origen_geografico_estimado']['latitud_centroide']:.4f}, Lon {datos_finales['origen_geografico_estimado']['longitud_centroide']:.4f}")
    print(f" -> Entorno Físico: {datos_finales['origen_geografico_estimado']['descripcion']}")
    print("\n[CALIDAD] Datos de linaje humano indexados permanentemente en 'secrets/phylogeny_calibration.json'.")
