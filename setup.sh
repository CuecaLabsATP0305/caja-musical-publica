#!/bin/bash
# Inicializador Automatizado para la Interfaz Adaptativa - Caja Musical
set -e

echo "=== [1/3] Actualizando repositorios del sistema en Termux ==="
pkg update -y && pkg upgrade -y

echo "=== [2/3] Instalando dependencias nativas de compilación ==="
pkg install -y python clang fftw libsndfile openssl

echo "=== [3/3] Configurando el entorno virtual y dependencias de Python ==="
pip install --upgrade pip
pip install numpy scipy

echo "========================================================="
echo " Entorno configurado con éxito. Listo para ejecución.    "
echo "========================================================="
