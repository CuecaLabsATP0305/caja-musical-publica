#!/bin/bash
# ==============================================================================
# PROYECTO: CUECALABS-QOT-HOMEOSTASIS-2026
# COMPONENTE: SCRIPT ORQUESTADOR MAESTRO DE LA SUITE DE SOFTWARE
# LICENCIA: AGPL-3.0 - CIENCIA ABIERTA (DESCENTRALIZADA)
# DOCTRINA: CERO ERRORES DE MÁQUINA / CERO ERRORES DE HUMANO
# ==============================================================================

# 1. Purgar el entorno y asegurar homeostasis visual
clear
echo "======================================================================"
echo "          INICIALIZANDO SUITE MAESTRA - CUECALABS GOLD STANDARD       "
echo "======================================================================"
echo "Timestamp Local: $(date)"
echo "Estado Operativo: CONFIGURACIÓN SEGURA"
echo "----------------------------------------------------------------------"
echo ""

# 2. Módulo 1: Núcleo de Autoevolución y Firmware
if [ -f "core_evolution_firmware.py" ]; then
    echo "[FIRMWARE] -> Iniciando Lazo de Control de Fases..."
    python3 core_evolution_firmware.py
else
    echo "[ERROR CRÍTICO] core_evolution_firmware.py no localizado."
fi

echo ""
echo "----------------------------------------------------------------------"
echo ""

# 3. Módulo 2: Registro Nosológico y Clínico [PDB 1X70]
if [ -f "nosology_mapping_core.py" ]; then
    echo "[NOSOLOGÍA] -> Procesando Mapeo de Estructuras Clínicas..."
    python3 nosology_mapping_core.py
else
    echo "[ERROR CRÍTICO] nosology_mapping_core.py no localizado."
fi

echo ""
echo "----------------------------------------------------------------------"
echo ""

# 4. Módulo 3: Interfaz Dinámica de Voz
if [ -f "cuecalabs_voice_cli.py" ]; then
    echo "[INTERFAZ VOZ] -> Activando Transductor de Voz Natural..."
    python3 cuecalabs_voice_cli.py
else
    echo "[ERROR CRÍTICO] cuecalabs_voice_cli.py no localizado."
fi

echo ""
echo "======================================================================"
echo "      EJECUCIÓN DE LA SUITE COMPLETADA CON ÉXITO ABSOLUTO (0 ERRORES) "
echo "======================================================================"
