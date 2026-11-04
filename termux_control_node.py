# -*- coding: utf-8 -*-
"""
Nodo de Control en Lazo Cerrado - Capa de Red Real Asíncrona (Sockets)
Caja Musical Pública - Ecosistema de Acceso Universal
"""
import time
import random
import socket
from universal_biosensor import UniversalBiosensor

class TermuxControlNode:
    def __init__(self, host="127.0.0.1", port=65432):
        self.biosensor = UniversalBiosensor()
        self.max_retries = 4
        self.host = host
        self.port = port

    def emit_homeostatic_signal(self, telemetria_abstracta):
        """
        Transmite la señal purificada a través de un socketTCP real utilizando
        un mecanismo de recuperación exponencial ante denegaciones de servicio.
        """
        base_delay = 1.0
        payload = f"{telemetria_abstracta:.4f}".encode('utf-8')
        
        for attempt in range(self.max_retries):
            # Instanciación de socket de flujo de datos (TCP/IP)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(2.0)
            
            try:
                # Intento de conexión al nodo de red distribuido
                client_socket.connect((self.host, self.port))
                client_socket.sendall(payload)
                print(f"    [REAL-NET] Sincronización exitosa en el intento {attempt + 1}.")
                client_socket.close()
                return True
            except (socket.timeout, socket.error):
                # Mitigación del ruido del canal mediante retraso estocástico
                sleep_time = (base_delay ** attempt) + random.uniform(0.1, 0.3)
                print(f"    [NET-FRICCIÓN] Nodo remoto inaccesible. Reintento {attempt + 1}/{self.max_retries}. Esperando {sleep_time:.2f}s...")
                client_socket.close()
                time.sleep(sleep_time)
                
        return False

    def run_production_cycle(self):
        """Ciclo continuo de procesamiento biométrico y envío a la red."""
        print("=== MÁQUINA OPERATIVA: EMISOR DE RED EN LAZO CERRADO REAL ===")
        try:
            import numpy as np
            mock_stream = np.random.uniform(-1.0, 1.0, 4)
        except ImportError:
            mock_stream = [0.15, -0.32, 0.88]
            
        signal = self.biosensor.process_sensor_stream(mock_stream)
        print(f" -> Señal local procesada por el Biosensor: {signal:.4f}")
        
        # Ejecuta la prueba de transmisión real
        success = self.emit_homeostatic_signal(signal)
        print(f"=== ESTADO FINAL DE LA TRANSFERENCIA: {success} ===")

if __name__ == "__main__":
    node = TermuxControlNode()
    node.run_production_cycle()
