import http.server
import socketserver
import threading
import json
import math

PORT = 8080

class TereminWebHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Elimina el ruido de logs en la terminal Termux

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            # Interfaz adaptativa universal: no requiere conocer el modelo de teléfono
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Consola de Telemetría Teremín v0305</title>
                <style>
                    body { background: #000; color: #00ff00; font-family: monospace; text-align: center; margin: 0; padding: 20px; overflow: hidden; }
                    #canvas { border: 1px solid #00ff00; width: 90vw; height: 50vh; margin-top: 20px; }
                    .metrics { font-size: 1.2rem; margin: 10px; color: #00ff00; }
                </style>
            </head>
            <body>
                <h2>🏛️ CUECALABS CORE - SENSOR TEREMÍN FÍSICO</h2>
                <div class="metrics">Equilibrio Basal: <span id="basal">0.1000</span></div>
                <div class="metrics">Energía Libre de Gibbs: <span id="gibbs">-5.00 kcal/mol</span></div>
                <canvas id="canvas"></canvas>
                <script>
                    const canvas = document.getElementById('canvas');
                    const ctx = canvas.getContext('2d');
                    canvas.width = canvas.offsetWidth;
                    canvas.height = canvas.offsetHeight;
                    
                    let t = 0;
                    function render() {
                        ctx.clearRect(0, 0, canvas.width, canvas.height);
                        ctx.strokeStyle = '#00ff00';
                        ctx.lineWidth = 2;
                        ctx.beginPath();
                        // Simulación matemática del acoplamiento neuronal biológico/digital
                        for (let x = 0; x < canvas.width; x++) {
                            let y = canvas.height/2 + Math.sin(x * 0.01 + t) * 50 * Math.sin(t * 0.5);
                            if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
                        }
                        ctx.stroke();
                        t += 0.05;
                        requestAnimationFrame(render);
                    }
                    render();
                </script>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))

def iniciar_servidor_teremin():
    handler = TereminWebHandler
    server = socketserver.TCPServer(("0.0.0.0", PORT), handler)
    print(f"\n[TEREMÍN LOCAL] Servidor gráfico desplegado en http://127.0.0.1:{PORT}")
    server.serve_forever()

if __name__ == "__main__":
    iniciar_servidor_teremin()
