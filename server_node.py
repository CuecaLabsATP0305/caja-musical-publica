# -*- coding: utf-8 -*-
"""
Nodo Servidor de Escucha y Validación Homeostática
Caja Musical Pública - Ecosistema de Acceso Universal
"""
import socket

def run_server(host="127.0.0.1", port=65432):
    print(f"=== INICIANDO NODO RECEPTOR COOPERATIVO EN {host}:{port} ===")
    
    # Configuración del socket de escucha de Linux
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(" -> Canal de escucha abierto. Esperando señal de la Caja Musical...")
        
        # Lazo de recepción simple para validación
        conn, addr = server_socket.accept()
        print(f"    [CONEXIÓN ANÓNIMA DE RED] Origen detectado en: {addr}")
        
        data = conn.recv(1024).decode('utf-8')
        if data:
            print(f"    [DATO NORMALIZADO RECIBIDO]: {data}")
            
        conn.close()
        print("=== VALIDACIÓN DE LAZO CERRADO REALIZADA CON ÉXITO ===")
    except Exception as e:
        print(f" -> Fricción en el nodo servidor: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    run_server()
