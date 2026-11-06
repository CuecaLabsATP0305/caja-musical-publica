#!/bin/bash
echo "=== INICIANDO RAMPA DE AUTOMATIZACIÓN EN LAZO CERRADO ==="
echo "Ejecutando mapeo espectral secuencial..."

# Barrido de frecuencias automatizado (Frecuencia, Amplitud fija, Tiempo de reposo)
python maquina_pedagogica_universal.py 50000 1.5 1.0
sleep 0.2
python maquina_pedagogica_universal.py 120000 2.5 3.0
sleep 0.2
python maquina_pedagogica_universal.py 200000 3.5 4.5
sleep 0.2
python maquina_pedagogica_universal.py 266666.6 4.5 6.0

echo "=== RAMPA CONCLUIDA: DATOS EXPORTADOS COMPLETA E INMUTABLEMENTE ==="
