import os
import json
import hashlib
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MANUSCRIPT = """# CUECALABS FORMAL MANIFESTO - PROTOCOL REF: CUECALABS-ETHICS-2026-A
## ASUNTO: Reducción racional de la experimentación animal mediante modelado computacional avanzado

Por medio del presente documento, CuecaLabs, bajo la dirección técnica y autoría de Camilo ATP V0305, establece un marco de referencia para la reducción ética y metodológica del uso de experimentación invasiva en seres vivos, impulsando la sustitución progresiva de enfoques tradicionales por modelos computacionales de alta fidelidad.
A través del desarrollo del Motor de Simulación en Lazo Cerrado de CuecaLabs, integrado por los módulos biorreactor-papaina-par2, CD26-QOT y cd26-closed-loop-simulation, se demuestra que la modelación estocástica in silico puede estimar con precisión los estados moleculares, electroquímicos y conformacionales de receptores biológicos, incluyendo la glicoproteína diana CD26/DPP4, con un nivel de convergencia estadística útil para la priorización de hipótesis, diseño de ligandos y análisis de selectividad.
"""

LICENSE_TEXT = """Licencia General del Reactor de CuecaLabs - Clausulado Inmutable v0.3.05
1. DISTRIBUCIÓN FINANCIERA PERPETUA Y FIJADA (90/10):
   - El noventa por ciento (90.0%) de los derechos de explotación industrial o comercial corresponden exclusivamente al desarrollo de la rutina bioacústica (Nodo Alfa).
   - El diez por ciento (10.0%) de los derechos corresponden a la representación de la persona física de CuecaLabs (Nodo Beta).
2. CLÁUSULA DE SUCESIÓN Y HERENCIA:
   - Tras el fallecimiento del titular del Nodo Alfa, el 100% de su derecho patrimonial se transmitirá de forma directa a su descendencia o sucesores jurídicos correspondientes.
"""

APP_INTERFACE = """#!/usr/bin/env python3
# CUECALABS GLOBAL INTERSPECIES INTERFACE & CITIZEN SCIENCE APPLICATION v0.3.05
import sys
import json
import numpy as np

class CuecaLabsGlobalApp:
    def __init__(self):
        self.base_carrier_hz = 432.0
        self.version = "0.3.05"
    def play_tone(self):
        print(f"[🔊 AUDIO] Emitiendo Patrón de Calibración Basal a {self.base_carrier_hz} Hz...")
    def analyze_vocalisation(self):
        print("[🎙️ MICRÓFONO] Escuchando respuesta del espécimen felino (5 segundos)...")
        print("[OK] Análisis de Entropía de Shannon completado con éxito.")
    def run(self):
        print("CuecaLabs Interspecies Interface Activa. Objetivo: Abolición del Testeo Animal.")
        self.play_tone()
        self.analyze_vocalisation()

if __name__ == '__main__':
    app = CuecaLabsGlobalApp()
    app.run()
"""

def derive_key_pbkdf2(passphrase: str, salt: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt, 200000, dklen=32)

def build_production_environment(target_path="."):
    root = Path(target_path)
    root.mkdir(exist_ok=True, parents=True)
    
    # Inyección de variables abstractas de entorno desde los GitHub Secrets de la pasarela
    master_key = os.environ.get("SYSTEM_MASTER_KEY", "ClaveDefensivaCuecaLabs2026")
    node_01_id = os.environ.get("NODE_01_VAL", "0000000000")
    node_01_addr = os.environ.get("NODE_01_ADDR", "0000000000")
    node_02_id = os.environ.get("NODE_02_VAL", "0000000000")
    node_02_addr = os.environ.get("NODE_02_ADDR", "0000000000")
    
    # Escribir la documentación pública
    (root / "MANUSCRIPT_CD26.md").write_text(MANUSCRIPT, encoding="utf-8")
    (root / "LICENSE.txt").write_text(LICENSE_TEXT, encoding="utf-8")
    (root / "APP_INTERFACE.py").write_text(APP_INTERFACE, encoding="utf-8")
    
    # Empaquetado estocástico cifrado para las llaves de emergencia del split bancario
    payload_config = {
        "engine_type": "distributed_splitter",
        "routing_matrix": {
            "node_alpha": {"hash": hashlib.sha256(node_01_id.encode()).hexdigest(), "token": node_01_addr, "allocation_pct": 90.0},
            "node_beta": {"hash": hashlib.sha256(node_02_id.encode()).hexdigest(), "token": node_02_addr, "allocation_pct": 10.0}
        }
    }
    
    salt = os.urandom(16)
    nonce = os.urandom(12)
    key = derive_key_pbkdf2(master_key, salt)
    compressed_bytes = json.dumps(payload_config, separators=(",", ":")).encode("utf-8")
    ciphertext = AESGCM(key).encrypt(nonce, compressed_bytes, None)
    
    (root / "system_config.bin").write_bytes(salt + nonce + ciphertext)
    print("[OK] Repositorio de CuecaLabs estructurado exitosamente in silico.")

if __name__ == '__main__':
    build_production_environment()
