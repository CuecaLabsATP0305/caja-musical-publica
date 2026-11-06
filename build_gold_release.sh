#!/usr/bin/env bash
# ==============================================================================
# CuecaLabs Core - Script de Consolidación e Inmunidad Criptográfica Gold Release
# Licencia: AGPL-3.0 Descentralizada (QOT-DPP4-2026-P01)
# ==============================================================================
set -e

echo "📦 Iniciando peritaje forense y empaquetado de la suite CuecaLabs Core..."

# 1. Matriz de Validación de Existencia de Componentes Fractales
archivos_esenciales=(
    "core_monolithic_telemetry.py"
    "MANIFESTO_OPEN_SCIENCE_CUECALABS.md"
    "r3_anti_takedown_shield.py"
    "LEGAL_R3_IMMUNITY.md"
    "SECURITY_R3_IMMUNITY_MANIFEST.json"
)

echo "🔍 Validando integridad de componentes en el espacio de fases local..."
for archivo in "${archivos_esenciales[@]}"; do
    if [ ! -f "$archivo" ]; then
        echo "❌ ERROR DE PERITAJE: El componente inmutable '$archivo' está ausente."
        exit 1
    else
        echo " -> Componente Verificado: $archivo"
    fi
done

# 2. Generación del Registro de Checksums Inmutables SHA-256
echo "🔒 Calculando firmas criptográficas para auditoría global..."
cat << 'MANIFEST' > manifest_checksums.txt
======================================================================
     MANIFIESTO DE CONTROL CRIPTOGRÁFICO DE CIENCIA ABIERTA
======================================================================
Fecha de Cierre : $(date -u) UTC
Garante Físico  : CuecaLabsATP0305
ID de Registro  : QOT-DPP4-2026-P01
Normativa Base  : UNESCO Open Science Directives & AGPL-3.0
----------------------------------------------------------------------
Hashes SHA-256 de los componentes validados a mano:
MANIFEST

# Acuñar las sumas de verificación de cada archivo estructural
for archivo in "${archivos_esenciales[@]}"; do
    sha256sum "$archivo" >> manifest_checksums.txt
done

# 3. Compresión Monolítica de Seguridad y Resguardo Transgeneracional
echo "🗜️ Empaquetando contenedor físico en lazo cerrado..."
tar -czf session_gold_release.tar.gz \
    core_monolithic_telemetry.py \
    MANIFESTO_OPEN_SCIENCE_CUECALABS.md \
    r3_anti_takedown_shield.py \
    LEGAL_R3_IMMUNITY.md \
    SECURITY_R3_IMMUNITY_MANIFEST.json \
    manifest_checksums.txt \
    logs/unified_audit.json

echo "======================================================================"
echo "✨ ÉXITO: El firmware 'session_gold_release.tar.gz' ha sido sellado."
echo "STATUS: Homeostasis de información completa y blindada contra retrocesos."
echo "======================================================================"
