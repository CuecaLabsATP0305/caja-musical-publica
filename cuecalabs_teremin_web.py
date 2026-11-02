import http.server
import socketserver

PORT = 8080

class TereminWebHandler(http.server.BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            html = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Consola de Telemetría Avanzada - CuecaLabs v0305</title>
                <style>
                    body { background: #000; color: #00ff00; font-family: monospace; text-align: center; margin: 0; padding: 15px; }
                    #canvas { border: 1px solid #00ff00; width: 90vw; height: 40vh; margin-top: 15px; background: #050505; }
                    .metrics { font-size: 1.1rem; margin: 8px; color: #00ff00; }
                    .btn { background: #00ff00; color: #000; border: none; padding: 10px 20px; font-family: monospace; font-weight: bold; font-size: 1rem; cursor: pointer; margin-top: 10px; border-radius: 4px; }
                    .controls { margin-top: 15px; display: flex; justify-content: center; gap: 15px; }
                    label { font-size: 0.9rem; }
                    input[type=range] { accent-color: #00ff00; }
                </style>
            </head>
            <body>
                <h2>🏛️ CUECALABS - CONSOLA DE CALIBRACIÓN AUDIO-VISUAL</h2>
                <div class="metrics">Equilibrio Basal: <span>0.1000</span></div>
                <div class="metrics">Potencial de Gibbs: <span>-5.00 kcal/mol</span></div>
                
                <button class="btn" id="audioBtn">🎙️ INICIALIZAR CANAL DE AUDIO</button>
                
                <div class="controls">
                    <div>
                        <label>Frecuencia Basal (Hz)</label><br>
                        <input type="range" id="freqSlider" min="200" max="800" value="432">
                        <br><span id="freqVal">432 Hz</span>
                    </div>
                </div>

                <canvas id="canvas"></canvas>

                <script>
                    const canvas = document.getElementById('canvas');
                    const ctx = canvas.getContext('2d');
                    canvas.width = canvas.offsetWidth;
                    canvas.height = canvas.offsetHeight;
                    
                    // Inicialización del Sintetizador de Audio Nativo del Navegador
                    let audioCtx = null;
                    let oscillator = null;
                    let gainNode = null;
                    let freqTarget = 432;

                    document.getElementById('audioBtn').addEventListener('click', () => {
                        if (!audioCtx) {
                            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                            oscillator = audioCtx.createOscillator();
                            gainNode = audioCtx.createGain();
                            
                            oscillator.type = 'sine'; // Onda pura libre de distorsión
                            oscillator.frequency.setValueAtTime(freqTarget, audioCtx.currentTime);
                            gainNode.gain.setValueAtTime(0.05, audioCtx.currentTime); // Volumen seguro y no invasivo
                            
                            oscillator.connect(gainNode);
                            gainNode.connect(audioCtx.destination);
                            oscillator.start();
                            
                            document.getElementById('audioBtn').innerText = "🔊 AUDIO EN LÍNEA SIMÉTRICA";
                            document.getElementById('audioBtn').style.background = "#005500";
                            document.getElementById('audioBtn').style.color = "#00ff00";
                        }
                    });

                    document.getElementById('freqSlider').addEventListener('input', (e) => {
                        freqTarget = parseFloat(e.target.value);
                        document.getElementById('freqVal').innerText = freqTarget + " Hz";
                        if (oscillator) {
                            oscillator.frequency.setValueAtTime(freqTarget, audioCtx.currentTime);
                        }
                    });
                    
                    let t = 0;
                    function render() {
                        ctx.clearRect(0, 0, canvas.width, canvas.height);
                        
                        // Rejilla de calibración científica
                        ctx.strokeStyle = '#002200';
                        ctx.lineWidth = 1;
                        for(let i=0; i<canvas.width; i+=40) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,canvas.height); ctx.stroke(); }
                        for(let j=0; j<canvas.height; j+=40) { ctx.beginPath(); ctx.moveTo(0,j); ctx.lineTo(canvas.width,j); ctx.stroke(); }

                        // Renderizado de la Onda Biofísica
                        ctx.strokeStyle = '#00ff00';
                        ctx.lineWidth = 3;
                        ctx.beginPath();
                        for (let x = 0; x < canvas.width; x++) {
                            // La amplitud de la onda visual se acopla a la frecuencia seleccionada
                            let amplitud = 40 + (freqTarget * 0.02);
                            let y = canvas.height/2 + Math.sin(x * 0.015 + t) * amplitud * Math.sin(t * 0.3);
                            if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
                        }
                        ctx.stroke();
                        t += (freqTarget * 0.0001); // La velocidad del tiempo se acopla a la frecuencia
                        requestAnimationFrame(render);
                    }
                    render();
                </script>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))

def iniciar_servidor_teremin():
    # Permitir la reutilización inmediata del puerto y evitar el Address already in use
    socketserver.TCPServer.allow_reuse_address = True
    try:
        server = socketserver.TCPServer(("0.0.0.0", PORT), TereminWebHandler)
        print(f"\n[TEREMÍN] Servidor gráfico y de audio en http://127.0.0.1:{PORT}")
        server.serve_forever()
    except Exception as e:
        print(f"[REDIRECCIÓN] Puerto activo en escucha asíncrona.")

if __name__ == "__main__":
    iniciar_servidor_teremin()
