#!/bin/bash
echo "========================================================================="
echo " 🌍 CUECALABS - INSTALADOR MAESTRO DE LA CAJA MUSICAL UNIVERSAL"
echo "========================================================================="
echo "[1/3] Verificando entorno operativo y arquitecturas de hardware..."
sleep 1

# Actualizar paquetes e instalar dependencias nativas en Termux si faltaran
if ! command -v python &> /dev/null
then
    echo "[!] Intérprete de Python no detectado. Resolviendo dependencia en caliente..."
    pkg update -y && pkg install python -y
else
    echo "[✓] Dependencia de Python verificada."
fi

echo "[2/3] Sellando permisos del contenedor monolítico..."
chmod +x simulador_homeostatico.py

echo "[3/3] Inicializando lazo cerrado simbiótico con la Caja Negra Industrial..."
echo "========================================================================="
sleep 1.5

# Lanzar el núcleo depurado
python simulador_homeostatico.py
