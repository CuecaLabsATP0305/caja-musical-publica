import http.server
import socketserver
import socket

print("=== [⚙] INICIANDO CANAL DE PROGRAMADOR HUMANO UNIFICADO ===")

# Algoritmo de Caza Dinámica de Puertos (Dynamic Port Hunting)
# Inicializa en un puerto aleatorio libre para evitar el error 'Address already in use'
def buscar_puerto_libre():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        return s.getsockname()[1]

PUERTO_QUIRAL = buscar_puerto_libre()
Handler = http.server.SimpleHTTPRequestHandler

# Configuración del servidor con reutilización de dirección activa
socketserver.TCPServer.allow_reuse_address = True

try:
    with socketserver.TCPServer(("", PUERTO_QUIRAL), Handler) as httpd:
        print("\n=========================================================")
        print(f"🚀 PORTAL DE SIMULACIÓN ETERNA CONSOLIDADO A +100 AÑOS")
        print(f"   -> Servidor Web Local Activo en el Puerto: {PUERTO_QUIRAL}")
        print("   -> Operador Autorizado: Freddy Arce")
        print(f"   -> Dirección de Acceso en Infinix: http://localhost:{PUERTO_QUIRAL}")
        print("=========================================================")
        print("[⚡] Lazo homeostático en escucha permanente... Presione Ctrl+C para salir.")
        
        # Inicia el bucle de escucha asíncrono reactivo
        httpd.serve_forever()
        
except Exception as e:
    print(f"[!] Falla en la inicialización de la infraestructura: {str(e)}")
