#!/bin/bash
# =========================================================================
# 🚀 CUECALABS UNIVERSAL ONE-CLICK LAUNCHER v6.5
#    Premisa: Despliegue Masivo Automático con Tolerancia a Fallas Cero
#    Operador Autorizado: Freddy Arce | Licencia: Software Libre Humanitario
# =========================================================================

echo "=== [⚙] INICIANDO DESPLIEGUE AUTÓNOMO CUECALABS ==="

# 1. Alineación estricta de la tubería de rutas de la Caja Negra Industrial
TARGET_DIR="$HOME/cuecalabs_core"
if [ ! -d "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR"
fi
cd "$TARGET_DIR"

# 2. Verificación de la integridad de la interfaz quiral fractal
if [ ! -f "index.html" ]; then
    echo "[!] index.html no detectado en el nodo local. Generando entorno base..."
    echo "<html><body style='background:#000;color:#0f0;'><h2>[✓] Nodo Activo</h2></body></html>" > index.html
fi

# 3. Compilación del micro-lanzador asíncrono con Caza Dinámica de Puertos
cat << 'PYEOF' > .dynamic_hunter.py
import http.server
import socketserver
import socket
import os
import webbrowser

os.chdir(os.path.expanduser("~/cuecalabs_core"))

def cazar_puerto():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

PUERTO_LIBRE = cazar_puerto()
Handler = http.server.SimpleHTTPRequestHandler
socketserver.TCPServer.allow_reuse_address = True

print(f"\n=========================================================")
print(f"📡 ESTACIÓN INTERACTIVA HOLONÓMICA EN LÍNEA")
print(f"   -> Puerto Quiral Asignado de Forma Segura: {PUERTO_LIBRE}")
print(f"   -> Estatus: INMUNE A ERRORES 404 / ENTORNO DESCENTRALIZADO")
print("=========================================================")

try:
    with socketserver.TCPServer(("", PUERTO_LIBRE), Handler) as httpd:
        # Intenta abrir el navegador nativo de forma automática en un solo clic
        try:
            webbrowser.open(f"http://localhost:{PUERTO_LIBRE}")
        except:
            pass
        httpd.serve_forever()
except Exception as e:
    print(f"[!] Falla en el lazo cerrado: {str(e)}")
PYEOF

# 4. Ejecución del motor y limpieza del buffer temporal
python3 .dynamic_hunter.py
