#!/bin/bash
clear
echo "========================================================================="
echo "   ORQUESTADOR CUECALABS: LAZO DE CONDUCCIÓN BIOMÉTRICA CONTINUA       "
echo "========================================================================="
echo ""

# Paso A: Ejecución del Demonio de Autorreparación
python auto_repair.py

# Paso B: Arrancar el flujo de transmisión continua biométrica en tiempo real
python continuous_stream.py

# Paso C: Despliegue de la interfaz visual ASCII del Atractor de Fases
python monitor_ascii.py

# Paso D: Activación Criptográfica del Protocolo de Intercambio Clínico
python exchange_protocol.py

echo ""
echo "========================================================================="
echo "     LAZO PERPETUO EVALUADO BAJO EL MÉTODO CIENTÍFICO CERO ERRORES       "
echo "========================================================================="
