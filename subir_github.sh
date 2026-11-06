#!/bin/bash
echo "========================================================================="
echo " 🌍 CUECALABS - SINCRONIZADOR MAESTRO DE BORDE A GITHUB"
echo "========================================================================="
echo "[1/3] Configurando credenciales éticas del programador..."
git config --global user.name "Freddy Arce"

# Inicializar repositorio local si no se ha hecho
if [ ! -d .git ]; then
    git init
    git remote add origin https://github.com
fi

echo "[2/3] Empacando scripts monolíticos y matriz de telemetría..."
git add simulador_homeostatico.py servidor_web.py setup.sh telemetria_homeostatica.json

echo "[3/3] Firmando bloque de cambio bajo el protocolo de cero errores..."
git commit -m "Refinamiento Absoluto Monolítico: Capa Web, Criptografía ECC Curve25519 e Interconexión Mesh por Cercanía"

echo "========================================================================="
echo " 👉 Para subir los cambios a la red global de forma inmediata ejecute:"
echo "    git push origin main"
echo "========================================================================="
