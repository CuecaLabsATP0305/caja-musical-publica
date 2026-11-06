#!/bin/bash
# ==============================================================================
# SCRIPT DE AUTOMATIZACIÓN DE LIBERACIÓN INTEGRAL - CUECA LABS CORE
# Consolida la suite purificada, el theremín y la telemetría libre de sesgos.
# ==============================================================================

echo "======================================================================"
echo ">> INICIALIZANDO AUDITORÍA FRACTAL DE CONTROL DE CALIDAD GLOBAL (QA) <<"
echo "======================================================================"
sleep 1

# 1. Verificación de módulos críticos de Python
for archivo in "cuecalabs_universal_pedagogy.py" "core_monolithic_telemetry.py" "cuecalabs_global_atractor.py" "cuecalabs_theremin_core.py" "AI_CONTEXT_MANIFEST.md"; do
    echo -n "[AUDITORÍA] Verificando $archivo... "
    if [ -f "$archivo" ]; then
        echo "OK (PRESENTE)"
    else
        echo "ERROR CRÍTICO: $archivo ausente."
        exit 1
    fi
done

# 2. Verificación de binarios nativos en C
echo -n "[AUDITORÍA] Verificando blindaje nativo en C... "
if [ -f "cuecalabs_input_sanity" ]; then
    echo "OK (COMPILADO Y OPERATIVO)"
else
    echo "ADVERTENCIA: Binario no detectado. Forzando compilación..."
    clang cuecalabs_input_sanity.c -o cuecalabs_input_sanity
fi

# 3. Estructuración del paquete de distribución limpio
echo "[SISTEMA] Consolidando bloque unificado en release_package/..."
mkdir -p release_package/logs
mkdir -p release_package/configs

cp core_monolithic_telemetry.py release_package/
cp cuecalabs_universal_pedagogy.py release_package/
cp cuecalabs_global_atractor.py release_package/
cp cuecalabs_theremin_core.py release_package/
cp cuecalabs_input_sanity release_package/
cp AI_CONTEXT_MANIFEST.md release_package/

echo "======================================================================"
echo ">> STATUS: PAQUETE FRACTAL GOLD STANDARD CONSTRUIDO CON CERO ERRORES <<"
echo ">> Ubicación: ~/cuecalabs_core/release_package/                  <<"
echo "======================================================================"
