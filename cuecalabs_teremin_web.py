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
                <title>Consola Profesional CuecaLabs v0305</title>
                <style>
                    body { background: #000; color: #00ff00; font-family: monospace; text-align: center; margin: 0; padding: 10px; user-select: none; touch-action: none; }
                    #canvas { border: 1px solid #00ff00; width: 92vw; height: 35vh; margin-top: 10px; background: #030303; }
                    .metrics { font-size: 0.9rem; margin: 4px; color: #00ff00; }
                    .btn { background: #00ff00; color: #000; border: none; padding: 12px; font-family: monospace; font-weight: bold; width: 92vw; font-size: 1rem; cursor: pointer; border-radius: 4px; margin-bottom: 5px; }
                    .input-box { width: 85vw; background: #111; border: 1px solid #00ff00; color: #00ff00; padding: 10px; font-family: monospace; font-size: 1rem; margin-top: 5px; border-radius: 4px; }
                    .selector { background: #000; color: #00ff00; border: 1px solid #00ff00; padding: 5px; font-family: monospace; margin-top: 5px; }
                </style>
            </head>
            <body>
                <h2>🏛️ CUECALABS - INTERFAZ SINTETIZADOR PROFESIONAL</h2>
                <button class="btn" id="audioBtn">🎙️ INICIALIZAR CANAL ACÚSTICO PROFESIONAL</button>
                
                <div class="metrics">
                    <label>Timbre Oscilador:</label>
                    <select id="waveType" class="selector">
                        <option value="sine">SENOIDAL (Pura)</option>
                        <option value="triangle">TRIANGULAR (Flauta/Suave)</option>
                        <option value="sawtooth">DIENTE DE SIERRA (Sinte/Pro)</option>
                        <option value="square">CUADRADA (Retro/Digital)</option>
                    </select>
                </div>

                <div class="metrics">Frecuencia: <span id="freqDisp">432 Hz</span> | Volumen: <span id="volDisp">0.050</span></div>
                <canvas id="canvas"></canvas>

                <!-- CANAL DE PROGRAMACIÓN Y DICTADO DIRECTO A LA CAJA NEGRA -->
                <div style="margin-top: 10px;">
                    <input type="text" id="cmdText" class="input-box" placeholder="Escribe comando o descriptor CD 26..."><br>
                    <button class="btn" id="voiceBtn" style="background:#0055ff; color:#fff; margin-top:5px; width:45vw;">🎤 DICTAR POR VOZ</button>
                    <button class="btn" id="sendBtn" style="background:#00aa00; color:#fff; margin-top:5px; width:45vw;">🚀 ENVIAR</button>
                </div>

                <script>
                    const canvas = document.getElementById('canvas');
                    const ctx = canvas.getContext('2d');
                    canvas.width = canvas.offsetWidth;
                    canvas.height = canvas.offsetHeight;
                    
                    let audioCtx = null;
                    let oscillator = null;
                    let gainNode = null;
                    let filterNode = null;
                    let currentFreq = 432;
                    let currentVol = 0.05;

                    document.getElementById('audioBtn').addEventListener('click', () => {
                        if (!audioCtx) {
                            audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                            oscillator = audioCtx.createOscillator();
                            gainNode = audioCtx.createGain();
                            filterNode = audioCtx.createBiquadFilter();
                            
                            oscillator.type = document.getElementById('waveType').value;
                            oscillator.frequency.setValueAtTime(currentFreq, audioCtx.currentTime);
                            gainNode.gain.setValueAtTime(currentVol, audioCtx.currentTime);
                            
                            // Filtro Pro de paso bajo para eliminar frecuencias estridentes
                            filterNode.type = 'lowpass';
                            filterNode.frequency.setValueAtTime(1200, audioCtx.currentTime);
                            
                            oscillator.connect(filterNode);
                            filterNode.connect(gainNode);
                            gainNode.connect(audioCtx.destination);
                            oscillator.start();
                            
                            document.getElementById('audioBtn').innerText = "🔊 SINTETIZADOR EN LÍNEA ADIABÁTICA";
                            document.getElementById('audioBtn').style.background = "#005500";
                            document.getElementById('audioBtn').style.color = "#00ff00";
                        }
                    });

                    document.getElementById('waveType').addEventListener('change', (e) => {
                        if (oscillator) oscillator.type = e.target.value;
                    });

                    function actualizarParametros(x, y) {
                        if (!oscillator) return;
                        currentFreq = 150 + (x / canvas.width) * 850; // Rango profesional expandido
                        currentVol = 0.005 + (1 - (y / canvas.height)) * 0.15;
                        
                        oscillator.frequency.setTargetAtTime(currentFreq, audioCtx.currentTime, 0.02);
                        gainNode.gain.setTargetAtTime(currentVol, audioCtx.currentTime, 0.02);
                        
                        document.getElementById('freqDisp').innerText = Math.round(currentFreq) + " Hz";
                        document.getElementById('volDisp').innerText = currentVol.toFixed(3);
                    }

                    canvas.addEventListener('mousemove', (e) => { const rect = canvas.getBoundingClientRect(); actualizarParametros(e.clientX - rect.left, e.clientY - rect.top); });
                    canvas.addEventListener('touchmove', (e) => { const rect = canvas.getBoundingClientRect(); const t = e.touches[0]; actualizarParametros(t.clientX - rect.left, t.clientY - rect.top); });

                    // MOTOR DE DICTADO DIRECTO POR VOZ (Web Speech API)
                    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                    if (SpeechRecognition) {
                        const recognition = new SpeechRecognition();
                        recognition.lang = 'es-ES';
                        recognition.interimResults = false;
                        
                        document.getElementById('voiceBtn').addEventListener('click', () => {
                            recognition.start();
                            document.getElementById('voiceBtn').innerText = "🎙️ ESCUCHANDO VOZ BIOLÓGICA...";
                        });
                        
                        recognition.onresult = (event) => {
                            const textoDictado = event.results[0][0].transcript;
                            document.getElementById('cmdText').value = textoDictado;
                            document.getElementById('voiceBtn').innerText = "🎤 DICTAR POR VOZ";
                        };
                        
                        recognition.onerror = () => { document.getElementById('voiceBtn').innerText = "🎤 ERROR - REINTENTAR"; };
                    } else {
                        document.getElementById('voiceBtn').innerText = "🎤 VOZ NO SOPORTADA";
                    }

                    // Vector de Envío al Lazo de la Terminal
                    document.getElementById('sendBtn').addEventListener('click', () => {
                        const cmd = document.getElementById('cmdText').value;
                        if(cmd) {
                            alert("[ENVIADO A CAJA NEGRA]: " + cmd);
                            document.getElementById('cmdText').value = "";
                        }
                    });

                    let time = 0;
                    function render() {
                        ctx.clearRect(0, 0, canvas.width, canvas.height);
                        ctx.strokeStyle = '#00ff00';
                        ctx.lineWidth = oscillator ? 3 : 1;
                        ctx.beginPath();
                        for (let x = 0; x < canvas.width; x++) {
                            let amp = 10 + (currentVol * 350);
                            let y = canvas.height/2 + Math.sin(x * 0.02 + time) * amp;
                            if (x === 0) ctx.moveTo(x, y); else ctx.lineTo(x, y);
                        }
                        ctx.stroke();
                        time += 0.04;
                        requestAnimationFrame(render);
                    }
                    render();
                </script>
            </body>
            </html>
            """
            self.wfile.write(html.encode('utf-8'))

def iniciar_servidor_teremin():
    socketserver.TCPServer.allow_reuse_address = True
    try:
        server = socketserver.TCPServer(("0.0.0.0", PORT), TereminWebHandler)
        print(f"\n[TEREMÍN] Lazo profesional activo en http://127.0.0.1:{PORT}")
        server.serve_forever()
    except:
        pass

if __name__ == "__main__":
    iniciar_servidor_teremin()
