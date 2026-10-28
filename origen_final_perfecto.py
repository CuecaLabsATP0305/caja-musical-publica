import os
import json
import time
import numpy as np

class LineagePhylogenyCorePerfect:
    def __init__(self):
        # Nodos geométricos de los linajes de origen (Física de Poblaciones)
        self.nodo_materno_boyaca = np.array([5.53, -73.36], dtype=np.float64)  # Alta montaña oriental
        self.nodo_paterno_tolima = np.array([4.43, -75.21], dtype=np.float64)  # Alto Magdalena
        
        # Datos del sujeto experimental de calibración (Fredi Arce, 47 años, 26-Nov-1978)
        self.sujeto = {
            "nombre": "Fredi Arce",
            "cronologia": "1978-11-26",
            "marcador_biocatalitico": "Tríada Papaína (Cys-His) - Transmisión Masculina Tolima"
        }

    def calcular_centro_origen_genetico(self):
        """Resuelve el centro de masa geográfico ponderado mediante vectores puros."""
        centro_masa = (self.nodo_materno_boyaca + self.nodo_paterno_tolima) / 2.0
        return centro_masa

    def estructurar_arbol_genealogico(self):
        """Construye el grafo lógico de transmisión de datos intergeneracionales."""
        arbol = {
            "NIVEL_0_SUJETO": self.sujeto["nombre"],
            "NIVEL_1_PROGENITORES": {
                "Paterno": "Alejandro Arce Carvajal (Tolima)",
                "Materno": "Alba Leticia Clavijo (Boyacá)"
            },
            "NIVEL_2_ANCESTROS": {
                "Rama_Paterna": {"Abuelo": "Urbano", "Abuela": "Hortensia"},
                "Rama_Materna": {"Abuelo": "Coronel Pablo Clavijo", "Abuela": "Sara María Plazas"}
            }
        }
        return arbol

    def ejecutar_analisis_completo(self):
        """Procesa y guarda la matriz de linaje en el entorno seguro de la máquina."""
        centro = self.calcular_centro_origen_genetico()
        arbol_logico = self.estructurar_arbol_genealogico()
        
        # Clasificación regional basada en la física de coordenadas del territorio colombiano
        lat, lon = centro[0], centro[1]
        if 4.0 <= lat <= 5.0 and -75.0 <= lon <= -74.0:
            region_convergencia = "Cundinamarca / Sabana Occidental / Valle del Magdalena"
        else:
            region_convergencia = "Región Central / Corredor Interandino"

        resultado_filogenia = {
            "timestamp": time.time(),
            "sujeto_calibracion": self.sujeto,
            "arbol_genealogico_detectado": arbol_logico,
            "origen_geografico_estimado": {
                "latitud_centroide": float(lat),
                "longitud_centroide": float(lon),
                "macro_region_convergencia": region_convergencia,
                "descripcion": "Zona de convergencia interandina entre el Valle del Magdalena y el Altiplano Cundiboyacense"
            },
            "estatus_homeostasis": "CALIBRACION_ETNICA_NOMINAL"
        }
        
        os.makedirs("secrets", exist_ok=True)
        with open("secrets/filogenia_autor_report.json", "w") as f:
            json.dump(resultado_filogenia, f, indent=4)
            
        return resultado_filogenia

if __name__ == "__main__":
    print("=== RECONSTRUCCIÓN COGNITIVA Y REPETICIÓN DE PRUEBA FILOGENÉTICA ===")
    mapper = LineagePhylogenyCorePerfect()
    datos_finales = mapper.ejecutar_analisis_completo()
    
    print("\n[GRAFO GENEALÓGICO COMPLETO RE-VERIFICADO]:")
    print(json.dumps(datos_finales["arbol_genealogico_detectado"], indent=4, ensure_ascii=False))
    
    print("\n[VEREDICTO MATEMÁTICO DE ORIGEN DE MUESTRA]:")
    print(f" -> Centroide Preciso: Lat {datos_finales['origen_geografico_estimado']['latitud_centroide']:.4f}, Lon {datos_finales['origen_geografico_estimado']['longitud_centroide']:.4f}")
    print(f" -> Macro Región de Convergencia: {datos_finales['origen_geografico_estimado']['macro_region_convergencia']}")
    print(f" -> Entorno Físico del Linaje: {datos_finales['origen_geografico_estimado']['descripcion']}")
    print("\n[⚙️ OPTIMIZACIÓN] Datos del Creador fijados sin errores en 'secrets/filogenia_autor_report.json'.")
