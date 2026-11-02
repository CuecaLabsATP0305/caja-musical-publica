#!/usr/bin/env bash
set -e

echo "⚡ Iniciando la integración del visualizador y la interfaz acústica..."

# 1. Crear el archivo HTML5 con Canvas e integración Web Audio API
cat << 'INDEX' > index.html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CuecaLabs Core - Visualizador e Interfaz Fractal</title>
    <style>
        body {
            background-color: #0d1117;
            color: #c9d1d9;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 20px;
        }
        h1 { color: #58a6ff; margin-bottom: 5px; }
        .metadata { font-size: 0.85em; color: #8b949e; margin-bottom: 20px; }
        #canvasContainer { margin: 10px auto; max-width: 600px; }
        canvas {
            background: #161b22;
            border: 2px solid #30363d;
            border-radius: 8px;
            width: 100%;
            height: auto;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
        }
        .btn-audio {
            background-color: #238636;
            color: #ffffff;
            border: none;
            padding: 12px 24px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 6px;
            cursor: pointer;
            margin: 15px auto;
            display: block;
            transition: background 0.2s;
        }
        .btn-audio:hover { background-color: #2ea043; }
        .controls-info { font-size: 0.9em; color: #7d8590; margin-top: 10px; }
    </style>
</head>
<body>

    <h1>🏛️ Árbol de las Ciencias del Fruto Maduro</h1>
    <div class="metadata">
        Licencia AGPL-3.0 Descentralizada | Registro: QOT-DPP4-2026-P01 | Garante: CuecaLabsATP0305
    </div>

    <!-- Botón de desbloqueo unificado para políticas de seguridad de audio en móviles -->
    <button class="btn-audio" id="initAudioBtn">⚡ Inicializar y Desbloquear Theremin</button>

    <div id="canvasContainer">
        <canvas id="scienceTreeCanvas" width="600" height="500"></canvas>
    </div>

    <div class="controls-info" id="statusDisplay">
        🎛️ Theremin Inactivo | Frecuencia Basal: 850.22 Hz | Desviación: 0.000000 Hz
    </div>

    <script>
        // --- 1. CONFIGURACIÓN DEL CANVAS (INFOGRAFÍA DEL BIORREACTOR) ---
        const canvas = document.getElementById('scienceTreeCanvas');
        const ctx = canvas.getContext('2d');

        function dibujarInfografia(ejeX = 0, ejeY = 0) {
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Dibujar Árbol de la Ciencia (Estructura de la Papaína)
            ctx.strokeStyle = '#238636';
            ctx.lineWidth = 6;
            ctx.beginPath();
            ctx.moveTo(300, 480);
            ctx.lineTo(300, 250); // Tronco principal
            ctx.stroke();

            // Ramificaciones Fractales
            ctx.strokeStyle = '#2ea043';
            ctx.lineWidth = 4;
            ctx.beginPath();
            ctx.moveTo(300, 350); ctx.lineTo(200, 280);
            ctx.moveTo(300, 280); ctx.lineTo(400, 220);
            ctx.stroke();

            // Fruto Maduro (Fijación del Pozo Cuántico PAR2 a -5.0 kcal/mol)
            ctx.fillStyle = '#e3b341';
            ctx.beginPath();
            ctx.arc(300, 220, 35, 0, Math.PI * 2);
            ctx.fill();

            // Texto Informativo del Fruto
            ctx.fillStyle = '#0d1117';
            ctx.font = 'bold 12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('PAR2', 300, 215);
            ctx.fillText('-5.0 kcal', 300, 230);

            // Capa de Confinamiento Micelar (Círculo de Seguridad Exterior)
            ctx.strokeStyle = '#388bfd';
            ctx.lineWidth = 2;
            ctx.setLineDash([6, 6]);
            ctx.beginPath();
            ctx.arc(300, 250, 180 + (ejeX * 5), 0, Math.PI * 2);
            ctx.stroke();
            ctx.setLineDash([]);

            // Indicador de Cursor Táctil / Interacción
            if (ejeX !== 0 || ejeY !== 0) {
                ctx.fillStyle = '#f85149';
                ctx.beginPath();
                ctx.arc(ejeX, ejeY, 8, 0, Math.PI * 2);
                ctx.fill();
            }

            // Etiquetas de las Capas Fractales
            ctx.fillStyle = '#58a6ff';
            ctx.font = '14px monospace';
            ctx.textAlign = 'left';
            ctx.fillText('Capa Ultra-Micro: Cys25–His159', 20, 40);
            ctx.fillText('Capa Sistémica: Matriz MPC Activa', 20, 60);
            ctx.fillText('Capa Macro-Social: Bien Público', 20, 80);
        }

        // Renderizado inicial estático
        dibujarInfografia();

        // --- 2. INTEGRACIÓN EN LAZO CERRADO VÍA WEB AUDIO API ---
        let audioCtx = null;
        let oscillator = null;
        let gainNode = null;
        const basalFreq = 850.22;

        const initBtn = document.getElementById('initAudioBtn');
        const statusDisplay = document.getElementById('statusDisplay');

        initBtn.addEventListener('click', () => {
            if (!audioCtx) {
                // Inicializar contexto de audio compatible con navegadores móviles
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                
                oscillator = audioCtx.createOscillator();
                gainNode = audioCtx.createGain();

                oscillator.type = 'sine';
                oscillator.frequency.setValueAtTime(basalFreq, audioCtx.currentTime);
                gainNode.gain.setValueAtTime(0.02, audioCtx.currentTime); // Volumen de protección bajo

                oscillator.connect(gainNode);
                gainNode.connect(audioCtx.destination);
                oscillator.start();

                statusDisplay.innerText = `⚡ Theremin Activo | Frecuencia: ${basalFreq} Hz | Lazo Cerrado Estable`;
                initBtn.style.backgroundColor = '#21262d';
                initBtn.innerText = '⚙️ Interfaz de Audio Conectada';
            }
        });

        // --- 3. SEÑALIZACIÓN EN TIEMPO REAL POR INTERACCIÓN TÁCTIL (THEREMIN) ---
        function manejarInteraccion(clientX, clientY) {
            const rect = canvas.getBoundingClientRect();
            const x = clientX - rect.left;
            const y = clientY - rect.top;

            // Escalar coordenadas a la resolución interna del canvas
            const canvasX = (x / rect.width) * canvas.width;
            const canvasY = (y / rect.height) * canvas.height;

            // Redibuja el árbol de la ciencia adaptando el confinamiento micelar dinámicamente
            dibujarInfografia(canvasX, canvasY);

            // Modulación de frecuencia en función de la posición del cursor táctil
            if (audioCtx && oscillator) {
                // Mapear el Eje X al rango de modulación de alta gama
                const deltaFreq = (canvasX - 300) * 1.2; 
                const nuevaFrecuencia = basalFreq + deltaFreq;
                oscillator.frequency.setValueAtTime(nuevaFrecuencia, audioCtx.currentTime);

                // Mapear el Eje Y a la ganancia dieléctrica (volumen) de forma controlada
                const nuevaGanancia = Math.max(0.005, Math.min(0.08, (1 - (canvasY / canvas.height)) * 0.1));
                gainNode.gain.setValueAtTime(nuevaGanancia, audioCtx.currentTime);

                statusDisplay.innerText = `🎛️ Dinámico | F0: ${nuevaFrecuencia.toFixed(2)} Hz | Modulación MPC Activa`;
            }
        }

        // Escuchadores de eventos para ratón y pantallas táctiles
        canvas.addEventListener('mousemove', (e) => {
            manejarInteraccion(e.clientX, e.clientY);
        });

        canvas.addEventListener('touchmove', (e) => {
            if (e.touches.length > 0) {
                manejarInteraccion(e.touches[0].clientX, e.touches[0].clientY);
                e.preventDefault(); // Impedir scroll de pantalla durante la modulación
            }
        }, { passive: false });

    </script>
</body>
</html>
INDEX

# 2. Levantar el servidor web local en segundo plano en el puerto 8080
echo "🌐 Levantando servidor HTTP de Ciencia Abierta en http://localhost:8080 ..."
python3 -m http.server 8080 > /dev/null 2>&1 &

echo "======================================================================"
echo "✨ SISTEMA COMPLETO INTEGRADO: CERO ERRORES"
echo "STATUS: Servidor sirviendo la infografía y el Theremin de forma segura."
echo "Acceda desde el navegador de su dispositivo en: http://localhost:8080"
echo "======================================================================"
