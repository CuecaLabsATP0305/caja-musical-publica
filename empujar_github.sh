#!/bin/bash
echo "========================================================================="
echo " 🌍 CUECALABS - DEPLOY REMOTO CRIPTOGRÁFICO A GITHUB"
echo "========================================================================="
echo "[1/2] Reconfigurando el nodo de origen al repositorio oficial público..."
git remote remove origin 2>/dev/null
git remote add origin https://github.com

echo "[2/2] Configurando persistencia de credenciales en el búfer local..."
git config --global credential.helper store

echo "========================================================================="
echo " 👉 INSTRUCCIÓN DE INTRODUCCIÓN:"
echo " 1. Ejecute manualmente el comando: git push origin main"
echo " 2. Cuando solicite 'Username', escriba: CuecaLabsATP0305"
echo " 3. Cuando solicite 'Password', PEGUE su Token de Acceso Personal (PAT)."
echo "========================================================================="
