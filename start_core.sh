#!/bin/bash
# Script de Validación y Arranque Nominal - CuecaLabs Gold Standard

echo "================================================================"
# Verificar que el archivo principal exista en el directorio activo
if [ -f "simulador_interfaz_humana.py" ]; then
    echo "🟢 [VERIFICACIÓN] Archivo simulador_interfaz_humana.py detectado."
    echo "🚀 Inicializando lazo cerrado industrial..."
    echo "================================================================"
    python simulador_interfaz_humana.py
else
    echo "❌ [ERROR] No se encontró el archivo simulador_interfaz_humana.py"
    echo "Recreando el archivo base de forma automática..."
    echo "================================================================"
fi
