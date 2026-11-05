import json
import time
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class CuecaLabsHTTPHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            # Carga dinámica de la telemetría homeostática en caliente
            try:
                with open("telemetria_homeostatica.json", "r") as f:
                    data = json.load(f)
                pitch = data["theremin_concert_state"]["theremin_pitch_hz"]
                volume = data["theremin_concert_state"]["theremin_volume_gain"]
                version = data["software_version"]
                entropy = data["thermodynamic_metrics"]["entropy_absorption"]
            except Exception:
                pitch, volume, version, entropy = 440.0, 0.5, 3.0508, 1.7619

            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>CuecaLabs - Caja Musical</title>
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <style>
                    body {{ font-family: 'Courier New', monospace; background-color: #0d0d0d; color: #00ff00; padding: 20px; text-align: center; }}
                    .container {{ max-width: 600px; margin: 0 auto; border: 2px solid #00ff00; padding: 20px; box-shadow: 0 0 15px #00ff00; }}
                    .box {{ border: 1px dashed #00ff00; padding: 15px; margin-top: 20px; text-align: left; background-color: #111; }}
                    .btn {{ padding: 10px 20px; background-color: #00ff00; color: #000; border: none; font-weight: bold; cursor: pointer; margin-top: 10px; }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h2>🌍 CAJA MUSICAL UNIVERSAL</h2>
                    <p>Interfaz de Abstracción Fascinante para la Sociedad</p>
                    <hr style="border-color: #00ff00;">
                    
                    <div class="box">
                        <h3>[Estado del Theremin de Concierto]</h3>
                        <p>• Frecuencia: {pitch} Hz</p>
                        <p>• Volumen: {volume}</p>
                        <p>• Absorción de Entropía: {entropy}</p>
                        <p>• Core Software: {version}</p>
                        <button class="btn" onclick="audioConcert({pitch}, {volume})">🔊 ESCUCHAR EN NAVEGADOR</button>
                    </div>
                </div>
                <script>
                    function audioConcert(p, v) {{
                        let audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                        let osc = audioCtx.createOscillator();
                        let gain = audioCtx.createGain();
                        osc.type = 'sine';
                        osc.frequency.setValueAtTime(p, audioCtx.currentTime);
                        gain.gain.setValueAtTime(v, audioCtx.currentTime);
                        osc.connect(gain);
                        gain.connect(audioCtx.destination);
                        osc.start();
                        setTimeout(() => {{ osc.stop(); }}, 800);
                    }}
                </script>
            </body>
            </html>
            """
            self.wfile.write(html_content.encode("utf-8"))

def run_server():
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, CuecaLabsHTTPHandler)
    print("=========================================================================")
    print(" 🌍 CUECALABS - NÚCLEO WEB FASCINANTE Y DE BAJA FRICCIÓN ACTIVO")
    print("=========================================================================")
    print("  👉 Servidor de Borde levantado de forma segura.")
    print("  👉 Abra su navegador en: http://localhost:8080")
    print("=========================================================================")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
