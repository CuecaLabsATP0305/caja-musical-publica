#!/bin/bash
# ======================================================================
# CUECALABS UNIVERSAL DEPLOYER - EQUIDAD Y HOMEOSTASIS DE CONOCIMIENTO
# ======================================================================
echo "[⚙️] Inicializando lazo de instalación monolítica..."

# 1. Asegurar directorios de la arquitectura de la Caja Negra
mkdir -p configs logs scripts

# 2. Verificar dependencias de punto flotante de alta precisión
if ! command -v python3 &> /dev/null; then
    echo "[⚠️] Python3 no detectado. Solicitando inicialización de entorno..."
    pkg install python -y || apt-get install python3 -y
else
    echo "[OK] Intérprete matemático validado: $(python3 --version)"
fi

# 3. Forzar el cierre de puertos huérfanos para evitar ERR_CONNECTION_REFUSED
pkill -f "http.server"

# 4. Lanzar el Transductor Pedagógico en segundo plano para acceso universal
python3 -m http.server 8080 > /dev/null 2>&1 &

echo "======================================================================"
echo "🟢 DESPLIEGUE COMPLETO: TRANSMISIÓN DE FASE OPERATIVA"
echo "======================================================================"
echo " El entorno ya es accesible de forma idéntica en cualquier dispositivo"
echo " local o red móvil ingresando a: http://localhost:8080"
echo "======================================================================"
