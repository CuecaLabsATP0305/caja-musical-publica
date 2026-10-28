#!/bin/bash
clear
echo "========================================================="
echo "  INICIALIZADOR DE INTERACCIÓN DINÁMICA - CUECALABS 2026 "
echo "========================================================="
echo ""

# Verificar si los archivos críticos existen en el directorio
if [ -f "core_evolution_firmware.py" ]; then
    echo "[SISTEMA] Ejecutando Núcleo de Autoevolución..."
    python3 core_evolution_firmware.py
else
    echo "[ALERTA] core_evolution_firmware.py no encontrado en este directorio."
fi

echo ""
if [ -f "nosology_mapping_core.py" ]; then
    echo "[SISTEMA] Ejecutando Módulo de Mapeo Clínico..."
    python3 nosology_mapping_core.py
else
    echo "[ALERTA] nosology_mapping_core.py no encontrado."
fi
echo ""
echo "========================================================="
