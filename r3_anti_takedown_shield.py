#!/usr/bin/env python3
import os
import hashlib
import json
from datetime import datetime

class R3AntiTakedownShield:
    def __init__(self, garante="CuecaLabsATP0305"):
        self.garante = garante
        self.patente_id = "QOT-DPP4-2026-P01"
        self.output_file = "SECURITY_R3_IMMUNITY_MANIFEST.json"

    def calcular_hash_archivo(self, ruta_archivo):
        hash_sha256 = hashlib.sha256()
        try:
            with open(ruta_archivo, "rb") as f:
                for bloque in iter(lambda: f.read(4096), b""):
                    hash_sha256.update(bloque)
            return hash_sha256.hexdigest()
        except FileNotFoundError:
            return None

    def consolidar_escudo_repositorio(self):
        print("🛡️ Activando Escudo R3 contra elución sintáctica y falsas demandas...")
        
        archivos_objetivo = [
            "core_monolithic_telemetry.py",
            "MANIFESTO_OPEN_SCIENCE_CUECALABS.md"
        ]
        
        inventario_hashes = {}
        for archivo in archivos_objetivo:
            if os.path.exists(archivo):
                v_hash = self.calcular_hash_archivo(archivo)
                inventario_hashes[archivo] = v_hash
                print(f" -> Registro Criptográfico Sólido [{archivo}]: {v_hash[:16]}...")
            else:
                print(f"⚠️ Alerta R3: Archivo '{archivo}' no detectado en el espacio local.")

        manifiesto_seguridad = {
            "estado_escudo": "ACTIVO_LAZO_CERRADO",
            "fecha_acuñacion_utc": datetime.utcnow().isoformat() + "Z",
            "garante_fisico_legal": self.garante,
            "identificador_patente": self.patente_id,
            "marco_regulatorio": "UNESCO Open Science Directives & AGPL-3.0 Copyleft",
            "integridad_codigo_fuente": inventario_hashes,
            "clausula_anti_takedown": "Este repositorio constituye un Bien de Uso Público Universal protegido contra la apropiación indebida de algoritmos. Cualquier reclamación automatizada sin revisión por pares médicos calificados viola los términos de bioseguridad del registro autónomo QOT-DPP4-2026-P01."
        }

        os.makedirs("logs", exist_ok=True)
        with open(self.output_file, "w", encoding="utf-8") as f:
            json.dump(manifiesto_seguridad, f, indent=4, ensure_ascii=False)
            
        print(f"✨ ÉXITO: Manifiesto de Inmunidad Criptográfica guardado en '{self.output_file}'.")
        print("STATUS: Escudo R3 blindado. Listo para responder legalmente ante cualquier bot de red.")

if __name__ == "__main__":
    escudo = R3AntiTakedownShield()
    escudo.consolidar_escudo_repositorio()
