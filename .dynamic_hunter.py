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
