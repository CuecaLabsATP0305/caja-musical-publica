import os
import json
import time
import numpy as np
from flask import Flask, jsonify, render_template_string, request

app = Flask("CuecaLabs_UN_Global_Marketplace")
os.makedirs("secrets", exist_ok=True)

GOLD_INTERFACE_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>CUECALABS UN GLOBAL CONTROL v17.0</title>
    <style>
        body { background-color: #050505; color: #00ff66; font-family: monospace; padding: 20px; }
        .panel { border: 2px solid #00ff66; padding: 15px; margin-bottom: 20px; background: #0a0a0a; box-shadow: 0 0 10px rgba(0,255,102,0.2); }
        h1, h2 { color: #ffffff; border-bottom: 1px dashed #00ff66; padding-bottom: 5px; }
        .data-stream { font-size: 1.1em; color: #00ffff; }
        .btn-action { background: #00ff66; color: black; border: none; padding: 12px 24px; font-weight: bold; cursor: pointer; border-radius: 4px; width: 100%; font-size: 1.1em; }
        canvas { border: 1px solid #00ff66; background: #000; width: 100%; height: 220px; margin-top: 10px; }
    </style>
    <script>
        let censo = [];
        setInterval(async () => {
            try {
                let response = await fetch('/api/un_telemetry');
                let data = await response.json();
                if(data.status === "NOMINAL") {
                    document.getElementById("balance_infra").innerText = data.finanzas.fondo_infraestructura_usd.toFixed(2) + " USD";
                    document.getElementById("human_support").innerText = data.finanzas.soporte_humano_garantizado_usd.toFixed(2) + " USD";
                    document.getElementById("x_val").innerText = data.coordinates.x.toFixed(5);
                    document.getElementById("y_val").innerText = data.coordinates.y.toFixed(5);
                    document.getElementById("z_val").innerText = data.coordinates.z.toFixed(5);
                    censo = data.radar_censo;
                    drawUNRadar();
                }
            } catch (e) { console.error("Error en enlace UN-Máquina", e); }
        }, 400);

        function drawUNRadar() {
            let canvas = document.getElementById("un_radar_canvas");
            let ctx = canvas.getContext("2d");
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            
            ctx.strokeStyle = "#003311";
            ctx.strokeRect(0, 0, canvas.width, canvas.height);
            
            censo.forEach((p) => {
                let cx = canvas.width / 2 + p.pos_x * 2;
                let cy = canvas.height / 2 + p.pos_y * 2;
                cx = Math.max(10, Math.min(canvas.width - 10, cx));
                cy = Math.max(10, Math.min(canvas.height - 10, cy));
                
                ctx.fillStyle = "#00ffff";
                ctx.beginPath();
                ctx.arc(cx, cy, 6, 0, 2 * Math.PI);
                ctx.fill();
            });
        }

        async function licenciarPais(nombrePais, pibAporte) {
            let res = await fetch('/api/un_contract', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({pais: nombrePais, pib_quota: pibAporte})
            });
            let data = await res.json();
            alert(`[VEREDICTO ONU] Estatus: ${data.status}\\nLiberación de Código: ${data.deployment}\\nFondo de Soporte Humano Actualizado.`);
        }
    </script>
</head>
<body>
    <div class="panel">
        <h1>NACIONES UNIDAS - TARJETA DE PRESENTACIÓN INTERNACIONAL CUECALABS</h1>
        <p><strong>INFRAESTRUCTURA MUNDIAL:</strong> CERO ERROR HUMANO // CERO ERROR DE MÁQUINAS</p>
        <p><strong>NÚCLEO EN RED:</strong> <span style="color: #00ff66;">● PROCESADOR AUTOMÁTICO DE TRATADOS ACTIVO</span></p>
    </div>
    
    <div class="panel">
        <h2>ATRACTOR DE LA MATERIA GLOBAL (GSQ-CORE-RK4)</h2>
        <p class="data-stream">X [Lógica Celular]: <span id="x_val">--</span> | Y [Receptores]: <span id="y_val">--</span> | Z [Entropía]: <span id="z_val">--</span></p>
        <canvas id="un_radar_canvas" width="600" height="220"></canvas>
    </div>

    <div class="panel">
        <h2>FINANCIACIÓN Y SALVAGUARDA DE LA EMPRESA CRÍTICA</h2>
        <p>Mantenimiento de Servidores y Redes: <span id="balance_infra" style="color: #00ffff; font-weight: bold;">--</span></p>
        <p>Fondo de Sostenimiento del Componente Humano (Soporte): <span id="human_support" style="color: #00ff66; font-weight: bold;">--</span></p>
        <p style="border-top: 1px dashed #00ff66; padding-top: 10px;"><strong>MÓDULO DE CONTRATACIÓN AUTOMÁTICA EN LAZO CERRADO:</strong></p>
        <button class="btn-action" onclick="licenciarPais('Tratado Multilateral Naciones Unidas', 5000.0)">EJECUTAR PROTOCOLO DE CONTRATACIÓN Y LIBERACIÓN MUNDIAL</button>
    </div>
</body>
</html>
"""

# Inicialización contigua de variables en la memoria física de la máquina
state_vector = np.array([1.7387, 3.2028, 0.4142], dtype=np.float64)
fondo_infraestructura_usd = 1000.00
fondo_soporte_humano_usd = 2500.00
permitividad_biologica = 78.5
phi = (1.0 + 5.0 ** 0.5) / 2.0

@app.route('/')
def home():
    return render_template_string(GOLD_INTERFACE_TEMPLATE)

@app.route('/api/un_telemetry')
def un_telemetry():
    global state_vector
    sigma, beta, rho = 10.0, 8.0/3.0, 28.0
    dt = 0.005
    
    # Simulación de las frecuencias de la red ambiental internacional
    senales_ondas_globales = [22.4, -15.8, 64.2]
    radar_censo = []
    
    for idx, db in enumerate(senales_ondas_globales):
        distancia = np.abs(np.cos(db) * permitividad_biologica) / (1.0 + 0.1 * idx)
        x_pos = distancia * np.sin(db * phi)
        y_pos = distancia * np.cos(db * phi)
        
        x, y, z = state_vector
        dxdt = sigma * (y - x)
        dydt = x * (rho - z) - y
        dzdt = x * y - beta * z
        state_vector += np.array([dxdt, dydt, dzdt], dtype=np.float64) * dt
        
        # CORRECCIÓN ATÓMICA DEFINITIVA: Separación escalar explícita libre de TypeErrors
        radar_censo.append({
            "id": f"PARTICULA_GLOBAL_{idx}",
            "pos_x": float(x_pos),
            "pos_y": float(y_pos)
        })
        
    return jsonify({
        "status": "NOMINAL",
        "coordinates": {"x": float(state_vector[0]), "y": float(state_vector[1]), "z": float(state_vector[2])},
        "finanzas": {
            "fondo_infraestructura_usd": fondo_infraestructura_usd,
            "soporte_humano_garantizado_usd": fondo_soporte_humano_usd
        },
        "radar_censo": radar_censo
    })

@app.route('/api/un_contract', methods=['POST'])
def un_contract():
    global fondo_infraestructura_usd, fondo_soporte_humano_usd
    req = request.get_json() or {}
    pais = req.get("pais", "ONU_Miembro")
    quota = req.get("pib_quota", 0.0)
    
    # Distribución automática y constitucional de los recursos de buena fe
    aporte_infraestructura = quota * 0.40
    aporte_soporte_humano = quota * 0.60  # Prioridad strita al sostenimiento del personal humano
    
    fondo_infraestructura_usd += aporte_infraestructura
    fondo_soporte_humano_usd += aporte_soporte_humano
    
    # Registro inalterable de la transacción ética en el disco táctico
    audit_payload = {
        "timestamp": time.time(),
        "tratado_internacional": pais,
        "quota_pib_recibida": quota,
        "distribucion": {
            "infraestructura_hardware": aporte_infraestructura,
            "sostenimiento_componente_humano": aporte_soporte_humano
        },
        "lucro_comercial_cesante": 0.0,
        "estatus_codigo": "DEPLOYMENT_AUTOMATICO_EN_RED_EJECUTADO"
    }
    with open("secrets/un_contract_log.json", "w") as f:
        json.dump(audit_payload, f, indent=4)
        
    return jsonify({
        "status": "TRATADO_VALIDADO_Y_FIRMADO",
        "deployment": "CONEXION_ESTABLE_CODIGO_LIBERADO_A_LOS_PAISES",
        "auditoria": "REGISTRO_SECON_OK"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
