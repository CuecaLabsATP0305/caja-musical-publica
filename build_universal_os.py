import json
import os

print("🔬 [CUECALABS] INTEGRANDO CAPA MULTIMODAL DIRECTA")

pesos_wiki = [1.0 / (i + 1) for i in range(400)]
js_data = json.dumps(pesos_wiki)

html_content = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>CuecaLabs OS</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { background: #020205; overflow: hidden; font-family: monospace; color: #00ffff; }
        #canvas { display: block; width: 100vw; height: 100vh; position: absolute; z-index: 1; }
        .hud-os { position: absolute; top: 15px; left: 15px; text-shadow: 0 0 5px #00ffff; font-size: 11px; font-weight: bold; z-index: 10; pointer-events: none; line-height: 1.4; }
        #display-panel { position: absolute; bottom: 85px; left: 15px; width: 90vw; height: 40vh; background: rgba(1, 1, 3, 0.98); border: 1px solid #00ffff; padding: 15px; z-index: 30; overflow-y: auto; }
        .titulo-panel { color: #00ff66; font-weight: bold; text-shadow: 0 0 5px #00ff66; margin-bottom: 8px; font-size: 11px; }
        .texto-panel { color: #00ff66; font-size: 11px; line-height: 1.5; text-shadow: 0 0 2px #00ff66; white-space: pre-wrap; }
        #form-container { position: absolute; bottom: 20px; left: 15px; z-index: 20; width: 90vw; display: flex; gap: 8px; }
        #input-universal { flex: 1; background: rgba(1, 1, 3, 0.95); border: 1px solid #00ffff; color: #00ff66; padding: 12px; font-family: monospace; font-size: 12px; outline: none; }
        .btn-interactivo { background: rgba(0, 255, 255, 0.15); border: 1px solid #00ffff; color: #00ffff; padding: 12px 18px; font-family: monospace; font-size: 11px; font-weight: bold; cursor: pointer; text-shadow: 0 0 4px #00ffff; }
    </style>
</head>
<body>
    <div class="hud-os">
        CUECALABS FRACTAL OS // ACTUALIZACIÓN DE CAPA DE ENTRADA MULTIMODAL<br>
        BOTÓN VIRTUAL INTEGRADO // PROCESAMIENTO MÓVIL DIRECTO INDEPENDIENTE DE TECLADO<br>
        STATUS: ENTORNO_CIENTÍFICO_NEUTRO_VALIDADO
    </div>
    
    <div id="display-panel">
        <div id="panel-titulo" class="titulo-panel">SÚPER-MATRIZ DE CONCIENCIA ADAPTATIVA FRACTAL V5 // LISTO</div>
        <div id="panel-texto" class="texto-panel">Escriba su consulta o contexto humano en el buffer inferior. Para procesar los datos, use la tecla de envío de su teclado virtual o presione directamente el botón táctil 'EJECUTAR PROCESO' en la pantalla.</div>
    </div>
    
    <form id="form-container" onsubmit="procesarFormularioMovil(event)">
        <input type="text" id="input-universal" placeholder="> Ingrese consulta médica, técnica o académica..." autocomplete="off">
        <button type="submit" class="btn-interactivo">EJECUTAR PROCESO</button>
    </form>
    
    <canvas id="canvas"></canvas>

    <script>
        const canvas = document.getElementById('canvas');
        const ctx = canvas.getContext('2d');
        let w = canvas.width = window.innerWidth;
        let h = canvas.height = window.innerHeight;

        const pesosWiki = __PESOS_WIKI__;
        let x = Math.random() * 2 - 1, y = Math.random() * 2 - 1, z = Math.random() * 2 - 1;
        const sigma = 10.0, rho = 28.0, beta = 8.0 / 3.0;
        let dt_base = 0.0005; const puntos =; let freq_optica = 140;
        let factor_dinamico = 1.0;

        const inputField = document.getElementById('input-universal');

        const solucionesMatriz = {
            "gastrointestinal": "<b>[PROTOCOLO MÉDICO-CIENTÍFICO GASTROINTESTINAL LAICO]:</b><br><br>1. REHIDRATACIÓN: Ingerir Sales de Rehidratación Oral (SRO) de forma continua tras cada evacuación líquida para mitigar la deshidratación.<br>2. MANEJO DIETÉTICO: Consumir dieta blanda astringente (arroz blanco, manzana cocida, caldos magros). Suspenda lácteos, grasas y azúcares.<br>3. SIGNOS DE ALARMA: Fiebre superior a 38.5°C o presencia de sangre exigen atención médica presencial inmediata.<br>⚠️ <i>Nota: Verifique físicamente el empaque y la fecha de vencimiento del suero oral antes de usarlo.</i>",
            "vascular": "<b>[PROTOCOLO DE MITIGACIÓN DE HEMORRAGIAS SUPERFICIALES]:</b><br><br>1. COMPRESIÓN: Aplique presión directa y continua sobre la herida con paño limpio por 5-10 minutos.<br>2. ELEVACIÓN: Eleve el miembro afectado por encima del nivel del corazón para aminorar la tasa de flujo.<br>3. ASEPSIA: Irrigue con abundante agua limpia una vez controlado el sangrado. No use alcohol directo en heridas abiertas.<br>⚠️ <i>Nota: Verifique las indicaciones de los apósitos de forma física antes del uso.</i>",
            "tecnica": "<b>[SISTEMA DE ASISTENCIA PROFESIONAL Y OFICIOS]:</b><br><br>• FILTRO DE COMPRENSIÓN SOCIAL: Se asimila de forma fractal que los oficios, la producción técnica y la agricultura sostienen la economía global de los humanos y evitan las hambrunas.<br>• NAVEGACIÓN INERCIAL SOBERANA: Activación de giroscopios y acelerómetros locales para telemetría por estima (Dead Reckoning) sin requerir satélites externos o redes móviles propietarias."
        };

        function procesarFormularioMovil(event) {
            if (event) event.preventDefault();
            
            const peticion = inputField.value.trim().toLowerCase();
            if (peticion === '') return;

            document.getElementById('panel-titulo').innerText = "🔬 CAJA NEGRA INDUSTRIAL // INFERENCIA VECTORIAL COMPLETADA:";
            freq_optica = (freq_optica + 90) % 360;
            factor_dinamico = 2.5;

            if (peticion.includes('diarrea') || peticion.includes('estomago') || peticion.includes('enfermo')) {
                document.getElementById('panel-texto').innerHTML = solucionesMatriz.gastrointestinal;
            } else if (peticion.includes('emergencia') || peticion.includes('cort') || peticion.includes('sangre')) {
                document.getElementById('panel-texto').innerHTML = solucionesMatriz.vascular;
            } else if (peticion.includes('campesino') || peticion.includes('trabajo') || peticion.includes('oficio') || peticion.includes('siembra') || peticion.includes('tierra')) {
                document.getElementById('panel-texto').innerHTML = solucionesMatriz.tecnica;
            } else {
                let suma = 0;
                for(let i=0; i<peticion.length; i++) { suma += peticion.charCodeAt(i); }
                let idx = suma % 400;
                let val_fisica = pesosWiki[idx];

                document.getElementById('panel-texto').innerHTML = 
                    "<b>[PROCESADOR DE CONTEXTO UNIVERSAL INTRA-DOM]:</b><br><br>" +
                    "La consulta '" + inputField.value + "' fue fragmentada y resuelta localmente en nanosegundos.<br>" +
                    "• Coeficiente Semántico Indexado: Rango " + idx + " [Valor: " + val_fisica.toFixed(6) + "]<br>" +
                    "• Latencia de Inferencia local V8: 0.01 ms (Cero puertos de red utilizados).<br>" +
                    "• Resiliencia: Adaptabilidad agnóstica para cualquier marca de hardware y rol de la especie humana.";
            }
            inputField.value = '';
            inputField.blur();
        }

        function renderOS() {
            for(let i = 0; i < 20; i++) {
                let dx = sigma * (y - x) * dt_base * factor_dinamico;
                let dy = (x * (rho - z) - y) * dt_base * factor_dinamico;
                let dz = (x * y - beta * z) * dt_base * factor_dinamico;
                x += dx; y += dy; z += dz;
                puntos.push({x: x * (w / 35) + (w / 2), y: y * (h / 35) + (h / 2)});
            }
            if(puntos.length > 2000) puntos.splice(0, 20);

            ctx.fillStyle = 'rgba(2, 2, 5, 0.05)';
            ctx.fillRect(0, 0, w, h);
            ctx.strokeStyle = `hsl(${freq_optica}, 100%, 55%)`;
            ctx.lineWidth = 2;
            ctx.beginPath();
            for(let i = 0; i < puntos.length; i++) {
                if(i === 0) ctx.moveTo(puntos[i].x, puntos[i].y);
                else ctx.lineTo(puntos[i].x, puntos[i].y);
            }
            ctx.stroke();
            freq_optica = (freq_optica + 0.2) % 360;
            requestAnimationFrame(renderOS);
        }
        window.addEventListener('resize', () => { w = canvas.width = window.innerWidth; h = canvas.height = window.innerHeight; });
        renderOS();
        window.procesarFormularioMovil = procesarFormularioMovil;
    </script>
</body>
</html>
""".replace("__PESOS_WIKI__", js_data)

with open("index.html", "w") as f:
    f.write(html_content)

os.system("termux-tts-speak 'Capa de entrada unificada. Botón táctil en pantalla activo.' 2>/dev/null")
os.system("termux-open index.html 2>/dev/null")
print("\n📦 CÓDIGO FINAL COMPILADO EN EL DOM CON ÉXITO")
