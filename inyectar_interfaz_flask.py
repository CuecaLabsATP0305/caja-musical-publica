import os

def inyectar_dashboard():
    archivo_target = "server_gold.py"
    
    if not os.path.exists(archivo_target):
        print("[-] Error: 'server_gold.py' no encontrado.")
        return

    with open(archivo_target, "r", encoding="utf-8") as f:
        codigo_original = f.read()

    # Nueva interfaz interactiva táctil avanzada integrada
    dashboard_html = """
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>NACIONES UNIDAS - CUECALABS MAESTRO</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body { background: #070a13; color: #f8fafc; font-family: -apple-system, BlinkMacSystemFont, sans-serif; padding: 15px; margin: 0; }
            .card { background: linear-gradient(145deg, #0f172a, #1e293b); padding: 20px; border-radius: 20px; border: 2px solid #10b981; max-width: 600px; margin: 10px auto; box-shadow: 0 8px 16px rgba(0,0,0,0.5); }
            h2, h3 { color: #34d399; margin-top: 0; }
            .metric { background: #0f172a; padding: 12px; border-radius: 10px; margin: 10px 0; border-left: 4px solid #10b981; font-family: monospace; }
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 15px; }
            button { background: #10b981; color: #0f172a; border: none; padding: 12px; border-radius: 10px; font-weight: bold; font-size: 14px; cursor: pointer; }
            button.pause { background: #f59e0b; }
            button.calib { background: #3b82f6; color: white; }
            button.export { background: #64748b; color: white; }
            input[type=range] { width: 100%; accent-color: #10b981; }
        </style>
    </head>
    <body>
        <div class="card">
            <h2>NACIONES UNIDAS - TARJETA DE PRESENTACIÓN CUECALABS</h2>
            <div style="color:#10b981; font-size:12px; font-weight:bold; margin-bottom:15px;">NÚCLEO EN RED: PROCESADOR AUTOMÁTICO ACTIVO</div>
            
            <h3>ATRACTOR DE LA MATERIA GLOBAL (GSQ-CORE-RK4)</h3>
            <div class="metric">X [Lógica Celular]: -7.08935 | Y [Receptores]: -8.61232 | Z [Entropía]: 22.90802</div>
            
            <hr style="border-color:#334155; margin:20px 0;">
            <h3>🎛️ PANEL OPERATIVO MAESTRO TÁCTIL</h3>
            
            <div style="margin-bottom: 15px;">
                <label style="color:#94a3b8; font-size:14px;">Frecuencia del Teremín: <span id="val-freq" style="color:#34d399;">695.39 Hz</span></label>
                <input type="range" min="100" max="1500" value="695" oninput="document.getElementById('val-freq').innerText = this.value + '.00 Hz'">
            </div>

            <div style="margin-bottom: 15px;">
                <label style="color:#94a3b8; font-size:14px;">Energía de Estabilización (ΔG): <span id="val-energy" style="color:#34d399;">-5.0 kcal</span></label>
                <input type="range" min="-20" max="20" value="-5" oninput="document.getElementById('val-energy').innerText = this.value + '.0 kcal'">
            </div>

            <div class="grid">
                <button onclick="alert('Iniciando Core...')">▶ INICIAR CORE</button>
                <button class="pause" onclick="alert('Lazo en Pausa.')">▌▌ PAUSA</button>
                <button class="calib" onclick="alert('Recalibración completada. Margen de error: 0.0')">🔄 CALIBRAR RK4</button>
                <button class="export" onclick="alert('Reporte Clínico Guardado.')">💾 EXPORTAR LOG</button>
            </div>
        </div>
    </body>
    </html>
    '''
    """

    # Buscar la función que retorna la página de inicio (habitualmente la ruta raíz '/')
    if "def index():" in codigo_original:
        # Buscamos la línea de retorno de esa función y la reemplazamos de forma precisa
        partes = codigo_original.split("def index():")
        subpartes = partes[1].split("return", 1)
        # Reensamblamos inyectando nuestro panel directamente en el flujo de ejecución de Flask
        resto_codigo = subpartes[1].split("'''", 2)
        
        if len(resto_codigo) >= 3:
            nuevo_codigo = partes[0] + "def index():" + subpartes[0] + dashboard_html + resto_codigo[2]
        else:
            nuevo_codigo = partes[0] + "def index():" + subpartes[0] + dashboard_html
            
        with open(archivo_target, "w", encoding="utf-8") as f:
            f.write(nuevo_codigo)
        print("[+] Éxito: Interfaz táctil unificada inyectada directamente en el backend de Flask.")
    else:
        print("[-] Error: No se localizó la función 'def index():' dentro de server_gold.py.")

if __name__ == "__main__":
    inyectar_dashboard()
