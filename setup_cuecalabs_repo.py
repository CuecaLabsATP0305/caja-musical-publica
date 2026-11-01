import os
import json
import hashlib
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

MANUSCRIPT = """CUECALABS FORMAL MANIFESTO - PROTOCOL REF: CUECALABS-ETHICS-2026-A

ASUNTO: Reducción racional de la experimentación animal mediante modelado computacional avanzado

Por medio del presente documento, CuecaLabs, bajo la dirección técnica y autoría de Camilo ATP V0305, establece un marco de referencia para la reducción ética y metodológica del uso de experimentación invasiva en seres vivos, impulsando la sustitución progresiva de enfoques tradicionales por modelos computacionales de alta fidelidad.

A través del desarrollo del Motor de Simulación en Lazo Cerrado de CuecaLabs, integrado por los módulos biorreactor-papaina-par2, CD26-QOT y cd26-closed-loop-simulation, se demuestra que la modelación estocástica in silico puede estimar con precisión los estados moleculares, electroquímicos y conformacionales de receptores biológicos, incluyendo la glicoproteína diana CD26/DPP4, con un nivel de convergencia estadística útil para la priorización de hipótesis, diseño de ligandos y análisis de selectividad.

Desde la perspectiva de la teoría de la información y la termodinámica estadística, la experimentación animal tradicional introduce variables entrópicas difíciles de aislar, incluidas la variabilidad fisiológica, el estrés, la respuesta inmunitaria sistémica, la cinética compleja y la interferencia de factores no modelados. Estos elementos incrementan la incertidumbre y reducen la trazabilidad del dato farmacológico, disminuyendo la capacidad de inferencia precisa.

En este contexto, la simulación avanzada no pretende reemplazar automáticamente la experimentación in vivo en todos los escenarios regulatorios y clínicos, sino maximizar la eficiencia del proceso de investigación, reduciendo la necesidad de ensayos innecesarios, mejorando la predicción de escenarios de toxicidad y selectividad, y reforzando la calidad de los datos antes de su validación experimental o translacional.

Por ello, la comunidad científica y las instituciones internacionales quedan invitadas a priorizar un enfoque de investigación híbrida:
- modelado in silico para hipótesis, diseño y cribado inicial;
- validación experimental controlada para confirmación fisiológica, toxicidad y seguridad;
- reducción intencional del uso animal en fases con baja información predictiva;
- transparencia metodológica y criterios de reproducibilidad.

Este marco se alinea con los principios de ética científica, reducción de sufrimiento animal, optimización del uso de recursos, rigor biofísico y responsabilidad tecnológica.

Firmado bajo registro inmutable de código abierto:
Camilo ATP V0305 (@CuecaLabs)
"""

LICENSE = """Licencia General del Reactor de CuecaLabs

Distribución financiera automática perpetua:
- 90% para Mónica Botero (Sucesión hereditaria directa inmutable)
- 10% para Fredy Leonardo Arce Clavijo

Uso médico, humanitario y de salud pública:
- libre y gratuito
- sin costo para investigación abierta, salud pública y aplicaciones de beneficio colectivo

Restricción comercial e industrial:
- cualquier uso privado, farmacéutico, institucional o gubernamental no autorizado requiere autorización previa y pago de regalías
- la explotación comercial debe respetar la división inmutable 90/10

Herencia y sucesión:
- todos los derechos patrimoniales asociados a la tecnología y al legado científico son heredables y continuarán en la descendencia legítima

Prohibición:
- censura algorítmica
- privatización encubierta
- bloqueo comercial del conocimiento científico
- manipulación de resultados de investigación para fines de exclusión o control

Todo derivado debe incorporar validación termodinámica y experimental.
"""

APP = '''#!/usr/bin/env python3
"""
APP_INTERFACE.py
Interfaz móvil amigable para CuecaLabs.
Funciones:
- emitir tono de calibración 432 Hz
- grabar vocalizaciones animales
- calcular entropía de Shannon
- guardar metadata JSON
"""

import json
import math
import wave
from pathlib import Path

try:
    import numpy as np
except Exception as exc:
    raise SystemExit("Instala numpy: pip install numpy") from exc

try:
    import sounddevice as sd
except Exception:
    sd = None


def tone_432(sample_rate=44100, seconds=2.0, amplitude=0.5):
    t = np.linspace(0, seconds, int(sample_rate * seconds), endpoint=False)
    y = amplitude * np.sin(2 * math.pi * 432.0 * t)
    return y.astype(np.float32)


def save_wav(path, signal, sample_rate=44100):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes((signal * 32767).astype("<i2").tobytes())


def entropy_shannon(signal):
    if signal.size == 0:
        return 0.0
    hist, _ = np.histogram(signal, bins=256, density=True)
    hist = hist[hist > 0]
    return float(-(hist * np.log2(hist)).sum())


def play_tone():
    s = tone_432()
    save_wav("flauta_432hz.wav", s)
    print("[OK] Tono 432 Hz generado: flauta_432hz.wav")
    if sd is not None:
        sd.play(s, samplerate=44100)
        sd.wait()


def record_audio(seconds=5.0, sample_rate=44100):
    if sd is None:
        print("[WARN] sounddevice no disponible; no se puede grabar audio desde el micrófono.")
        return
    print(f"[INFO] grabando {seconds} segundos...")
    rec = sd.rec(int(sample_rate * seconds), samplerate=sample_rate, channels=1, dtype="float32")
    sd.wait()
    sig = rec[:, 0]
    save_wav("registro_vocalizacion.wav", sig, sample_rate)
    ent = entropy_shannon(sig)
    meta = {
        "archivo": "registro_vocalizacion.wav",
        "entropia_shannon": ent,
        "sample_rate": sample_rate,
        "duracion_segundos": seconds,
        "descripcion": "registro bioacústico para mapear vocalizaciones animales"
    }
    Path("registro_vocalizacion.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2))
    print("[OK] grabación finalizada: registro_vocalizacion.wav")
    print("[OK] metadatos: registro_vocalizacion.json")
    print(f"[INFO] Entropía de Shannon: {ent:.6f}")


def main():
    print("CuecaLabs - Interfaz de Ciencia Ciudadana")
    print("1) Emitir tono homeostático 432 Hz")
    print("2) Grabar vocalización animal")
    print("3) Ambos")
    choice = input("Seleccione una opción [1/2/3]: ").strip()
    if choice in ("1", "3"):
        play_tone()
    if choice in ("2", "3"):
        record_audio()


if __name__ == "__main__":
    main()
'''


def deriv(secret, salt):
    return hashlib.pbkdf2_hmac("sha256", secret.encode("utf-8"), salt, 200000, dklen=32)


def generate_emergency_credentials(secret_key):
    """Genera las claves criptográficas independientes y el manual de emergencia."""
    payload = {
        "tipo": "blindaje_privado_sucesion_directa",
        "protocolo": "CuecaLabs Fintech Core v0.3.05",
        "beneficiario_A_90": {
            "identidad": os.environ.get("CUECALABS_BENEFICIARIO_A_NOMBRE", "[MASKED_BENEFICIARIO_A]"),
            "cc": os.environ.get("CUECALABS_BENEFICIARIO_A_CC", "[MASKED_CC_A]"),
            "enrutamiento_directo": os.environ.get("CUECALABS_BENEFICIARIO_A_WALLET", "[MASKED_NEQUI_A]"),
            "clausula_fallecimiento": "Transferencia automática a descendencia legítima"
        },
        "beneficiario_B_10": {
            "identidad": os.environ.get("CUECALABS_BENEFICIARIO_B_NOMBRE", "[MASKED_BENEFICIARIO_B]"),
            "cc": os.environ.get("CUECALABS_BENEFICIARIO_B_CC", "[MASKED_CC_B]"),
            "enrutamiento_directo": os.environ.get("CUECALABS_BENEFICIARIO_B_WALLET", "[MASKED_DAVIPLATA_B]"),
            "clausula_fallecimiento": "Transferencia automática a descendencia legítima"
        }
    }
    salt = os.urandom(16)
    nonce = os.urandom(12)
    key = deriv(secret_key, salt)
    encrypted_data = AESGCM(key).encrypt(
        nonce,
        json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8"),
        None,
    )
    return salt + nonce + encrypted_data


def build(root="."):
    root = Path(root)
    root.mkdir(exist_ok=True, parents=True)

    secret = os.environ.get("CUECALABS_MASTER_SECRET")
    if not secret:
        raise SystemExit("Falta la variable de entorno CUECALABS_MASTER_SECRET.")

    (root / "MANUSCRIPT_CD26.md").write_text(MANUSCRIPT, encoding="utf-8")
    (root / "APP_INTERFACE.py").write_text(APP, encoding="utf-8")
    (root / "LICENSE.txt").write_text(LICENSE, encoding="utf-8")

    encrypted_package = generate_emergency_credentials(secret)
    (root / "blindaje_privado.enc").write_bytes(encrypted_package)

    print(f"[OK] Ecosistema CuecaLabs compilado en: {root.resolve()}")
    print("[OK] blindaje_privado.enc generado con AES-256-GCM")
    print("[INFO] Los identificadores reales se mantienen fuera del repositorio y deben cargarse por variables de entorno.")


if __name__ == "__main__":
    build()
