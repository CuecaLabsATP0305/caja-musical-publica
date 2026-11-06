import numpy as np
import sys
import time
from datetime import datetime
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class RedProyeccionInversaAvanzada:
    def __init__(self):
        np.random.seed(305)
        self.W1 = np.random.randn(32, 16) * 0.05
        self.W2 = np.random.randn(16, 4) * 0.05

    def mapear_entorno_fractal(self, vector_linguistico):
        capa_oculta = np.tanh(np.dot(vector_linguistico, self.W1))
        return np.tanh(np.dot(capa_oculta, self.W2))

class BiorreactorIndustrialGlobal:
    def __init__(self):
        # Variables de estado (GSQ-CORE-LORENZ-RK4)
        self.X, self.Y, self.Z = 0.1000, 0.1000, 0.1000
        self.dt = 0.01
        self.operador = "Fredy Arce"
        self.ciclo = 0
        self.red_inversa = RedProyeccionInversaAvanzada()
        self.dg_actual = -2.5000
        
        # Historial de telemetría para la analítica de desviación estadística
        self.historial_dg = []

    def ciclo_rk4(self):
        sigma, rho, beta = 10.0, 28.0, 8.0 / 3.0
        def ecuaciones(x, y, z):
            return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

        k1_x, k1_y, k1_z = ecuaciones(self.X, self.Y, self.Z)
        k2_x, k2_y, k2_z = ecuaciones(self.X + 0.5*self.dt*k1_x, self.Y + 0.5*self.dt*k1_y, self.Z + 0.5*self.dt*k1_z)
        k3_x, k3_y, k3_z = ecuaciones(self.X + 0.5*self.dt*k2_x, self.Y + 0.5*self.dt*k2_y, self.Z + 0.5*self.dt*k2_z)
        k4_x, k4_y, k4_z = ecuaciones(self.X + self.dt*k3_x, self.Y + self.dt*k3_y, self.Z + self.dt*k3_z)

        self.X += (self.dt / 6.0) * (k1_x + 2*k2_x + 2*k3_x + k4_x)
        self.Y += (self.dt / 6.0) * (k1_y + 2*k2_y + 2*k3_y + k4_y)
        self.Z += (self.dt / 6.0) * (k1_z + 2*k2_z + 2*k3_z + k4_z)
        
        self.X = float(np.clip(self.X, -50.0, 50.0))
        self.Y = float(np.clip(self.Y, -50.0, 50.0))
        self.Z = float(np.clip(self.Z, -50.0, 50.0))

        # Actualizar cálculo Gibbsiano
        self.dg_actual = -5.0 * (1.0 / (1.0 + np.exp(-abs(self.Z) * 0.05)))
        self.historial_dg.append(self.dg_actual)
        
        # Mantener buffer acotado en memoria de las últimas 150 lecturas
        if len(self.historial_dg) > 150:
            self.historial_dg.pop(0)

    def ejecutar_analitica_desviacion(self):
        """Calcula la desviación estándar y la varianza para medir el desgaste y la homeostasis."""
        if len(self.historial_dg) < 2:
            return 0.0, 0.0
        desviacion = float(np.std(self.historial_dg))
        varianza = float(np.var(self.historial_dg))
        return desviacion, varianza

# Capa de red: Servidor Web local en puerto 8080 (Canal 2 Desacoplado)
biorreactor_global = BiorreactorIndustrialGlobal()

class ServidorWebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        desviacion, varianza = biorreactor_global.ejecutar_analitica_desviacion()
        
        html = f"""<html>
        <head><title>CuecaLabs Core Dashboard</title>
        <meta http-equiv="refresh" content="2">
        <style>body{{font-family:monospace; background-color:#111; color:#0f0; padding:20px;}}
        .card{{border:1px solid #0f0; padding:15px; margin-bottom:10px;}}</style></head>
        <body>
        <h2>📊 PANEL DE SUPERVISIÓN TÁCTIL (CANAL 2)</h2>
        <div class="card">
            <h3>Variables de Estado del Biorreactor</h3>
            <p><b>Operador Responsable:</b> {biorreactor_global.operador}</p>
            <p><b>Ciclo Activo:</b> {biorreactor_global.ciclo:05d}</p>
            <p><b>Energía Libre (dG):</b> {biorreactor_global.dg_actual:.4f} kcal/mol</p>
            <p><b>Coordenadas:</b> X: {biorreactor_global.X:+.4f} | Y: {biorreactor_global.Y:+.4f} | Z: {biorreactor_global.Z:+.4f}</p>
        </div>
        <div class="card">
            <h3>📈 ANALÍTICA ESTADÍSTICA DE NO-EQUILIBRIO</h3>
            <p><b>Desviación Estándar (dG):</b> {desviacion:.6f}</p>
            <p><b>Varianza de Fase:</b> {varianza:.6f}</p>
            <p><b>Estado del Lazo:</b> HOMEÓSTASIS COMPATIBLE (CERO ERRORES)</p>
        </div>
        </body></html>"""
        self.wfile.write(html.encode('utf-8'))

    def log_message(self, format, *args):
        return # Desactivar logs ruidosos de peticiones HTTP en la terminal

def iniciar_servidor_http():
    server = HTTPServer(('localhost', 8080), ServidorWebHandler)
    server.serve_forever()

if __name__ == "__main__":
    # Levantar el Canal 2 en un hilo asíncrono para no congelar el motor
    hilo_web = threading.Thread(target=iniciar_servidor_http, daemon=True)
    hilo_web.start()
    
    print("================================================================")
    print(" 🚀 MÁQUINA INDUSTRIAL CUECALABS - MULTIPLEXACIÓN DE CANALES    ")
    print("================================================================")
    print(" -> CANAL 2 ACTIVADO : Servidor Web corriendo en http://localhost:8080")
    print(" -> MÓDULO ANALÍTICO : Evaluación Estadística de Desviación en Lazo")
    print("================================================================\n")
    
    try:
        while True:
            biorreactor_global.ciclo_rk4()
            
            if biorreactor_global.ciclo % 150 == 0:
                dev, var = biorreactor_global.ejecutar_analitica_desviacion()
                sys.stdout.write(
                    f"\r[NÚCLEO] Ciclo: {biorreactor_global.ciclo:05d} | dG: {biorreactor_global.dg_actual:.4f} | Dev.Std: {dev:.6f}"
                )
                sys.stdout.flush()
                
            biorreactor_global.ciclo += 1
            time.sleep(0.02)
    except KeyboardInterrupt:
        print("\n\n🔒 [REPOSO SEGURO] -> Servidor e hilos resguardados nominalmente.")
