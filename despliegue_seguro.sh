#!/bin/bash
echo "========================================================================="
echo " 🌍 CUECALABS - NÚCLEO FRACTAL DE PRECISIÓN ABSOLUTA"
echo "========================================================================="

# 1. Configuración del Helper de Credenciales Oculto en Búfer Volátil
git config --global credential.helper cache

# 2. Inyección de la URL oficial completa del repositorio de la patente
# https://github.com
git remote remove origin 2>/dev/null
git remote add origin https://github.com

echo "[✓] Matriz de Redirección Asignada con Precisión Absoluta."
echo "========================================================================="
echo " 👉 PASO DE EMPUJE FINAL CON SEGURIDAD VISUAL:"
echo " 1. La terminal solicitará 'Username'. Escriba: CuecaLabsATP0305"
echo " 2. La terminal solicitará 'Password'. PEGUE su token (quedará oculto)."
echo "========================================================================="
sleep 0.5

# 3. Lanzamiento balanceado del push a la rama principal
git push -u origin main || git push -u origin master
