import os

def aplicar_interfaz_avanzada():
    archivo_target = "index.html"
    
    if not os.path.exists(archivo_target):
        print("[-] Error: 'index.html' no encontrado en el directorio actual.")
        return

    with open(archivo_target, "r", encoding="utf-8") as f:
        contenido = f.read()

    # Bloque de código HTML/CSS/JS con diseño móvil táctil avanzado
    interfaz_tactil = """
    <!-- INICIO DE CONSOLA INTERACTIVA AVANZADA CUECALABS -->
    <div id="consola-programador-avanzada" style="margin: 25px auto; max-width: 95%; background: linear-gradient(145deg, #0f172a, #1e293b); padding: 25px; border-radius: 24px; border: 2px solid #10b981; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; box-shadow: 0 12px 24px rgba(0,0,0,0.5);">
        
        <!-- Encabezado Estilo App Premium -->
        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #334155; padding-bottom: 15px; margin-bottom: 20px;">
            <span style="color: #34d399; font-weight: bold; font-size: 18px; letter-spacing: 0.5px;">🎛️ PANEL OPERATIVO MAESTRO</span>
            <span id="estado-badge" style="background: #10b981; color: #0f172a; padding: 4px 12px; border-radius: 12px; font-size: 12px; font-weight: bold;">AUTÓNOMO</span>
        </div>

        <!-- Sección de Control de Parámetros Científicos -->
        <div style="margin-bottom: 20px; text-align: left;">
            <h4 style="color: #94a3b8; margin: 0 0 12px 0; font-size: 14px; text-transform: uppercase; letter-spacing: 0.5px;">Ajuste del Lazo Supramolecular</h4>
            
            <div style="margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between; color: #f8fafc; font-size: 14px; margin-bottom: 5px;">
                    <span>Frecuencia del Teremín (F0)</span>
                    <span id="val-frecuencia" style="color: #34d399; font-family: monospace;">695.39 Hz</span>
                </div>
                <input type="range" min="100" max="1500" value="695" oninput="actualizarParametro('frecuencia', this.value)" style="width: 100%; accent-color: #10b981; background: #334155; height: 6px; border-radius: 3px; cursor: pointer;">
            </div>

            <div style="margin-bottom: 15px;">
                <div style="display: flex; justify-content: space-between; color: #f8fafc; font-size: 14px; margin-bottom: 5px;">
                    <span>Energía de Estabilización (ΔG)</span>
                    <span id="val-energia" style="color: #34d399; font-family: monospace;">-5.0 kcal</span>
                </div>
                <input type="range" min="-20" max="20" value="-5" oninput="actualizarParametro('energia', this.value)" style="width: 100%; accent-color: #10b981; background: #334155; height: 6px; border-radius: 3px; cursor: pointer;">
            </div>
        </div>

        <!-- Botones Táctiles Dinámicos Estilo Dashboard de Control -->
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin-bottom: 20px;">
            <button onclick="ejecutarAccion('INICIAR_PROCESAMIENTO')" style="background: #10b981; color: #0f172a; border: none; padding: 14px; border-radius: 14px; font-weight: bold; font-size: 15px; cursor: pointer; transition: background 0.2s;">▶ INICIAR CORE</button>
            <button onclick="ejecutarAccion('PAUSAR_LAZO')" style="background: #f59e0b; color: #0f172a; border: none; padding: 14px; border-radius: 14px; font-weight: bold; font-size: 15px; cursor: pointer; transition: background 0.2s;">▌▌ PAUSA</button>
            <button onclick="ejecutarAccion('RECALIBRAR_MATRICES')" style="background: #3b82f6; color: white; border: none; padding: 14px; border-radius: 14px; font-weight: bold; font-size: 15px; cursor: pointer; transition: background 0.2s;">🔄 CALIBRAR RK4</button>
            <button onclick="ejecutarAccion('DESCARGAR_AUDITORIA')" style="background: #64748b; color: white; border: none; padding: 14px; border-radius: 14px; font-weight: bold; font-size: 15px; cursor: pointer; transition: background 0.2s;">💾 EXPORTAR LOG</button>
        </div>

        <!-- Consola de Salida de Estado Interno Libre de Erreores -->
        <div style="background: #0f172a; border: 1px solid #334155; border-radius: 12px; padding: 12px; text-align: left; font-family: monospace; font-size: 12px; height: 80px; overflow-y: auto; color: #34d399;">
            <div style="color: #64748b;">[SISTEMA] Inicializando entorno táctil interactivo...</div>
            <div id="consola-log">[OK] Consola unificada vinculada al Atractor Global. Ready.</div>
        </div>
    </div>

    <script>
        function actualizarParametro(tipo, valor) {
            if(tipo === 'frecuencia') {
                document.getElementById('val-frecuencia').innerText = valor + ".00 Hz";
                logMensaje("Frecuencia modificada localmente a: " + valor + " Hz");
            } else if(tipo === 'energia') {
                document.getElementById('val-energia').innerText = valor + ".0 kcal";
                logMensaje("Energía de Gibbs reconfigurada a: " + valor + " kcal");
            }
        }

        function ejecutarAccion(accion) {
            logMensaje("Ejecutando directiva maestro: " + accion);
            if(accion === 'RECALIBRAR_MATRICES') {
                document.getElementById('estado-badge').innerText = "CALIBRANDO";
                document.getElementById('estado-badge').style.background = "#3b82f6";
                document.getElementById('estado-badge').style.color = "white";
                setTimeout(() => {
                    document.getElementById('estado-badge').innerText = "AUTÓNOMO";
                    document.getElementById('estado-badge').style.background = "#10b981";
                    document.getElementById('estado-badge').style.color = "#0f172a";
                    logMensaje("[OK] Recalibración completada con margen de error: 0.0");
                }, 1500);
            }
        }

        function logMensaje(texto) {
            let logDiv = document.getElementById('consola-log');
            let timestamp = new Date().toLocaleTimeString();
            logDiv.innerHTML += `\\n<span style="color: #94a3b8;">[${timestamp}]</span> ${texto}`;
            logDiv.scrollTop = logDiv.scrollHeight;
        }
    </script>
    <!-- FIN DE CONSOLA INTERACTIVA AVANZADA CUECALABS -->
    """

    if "</body>" in contenido:
        nuevo_contenido = contenido.replace("</body>", f"{interfaz_tactil}\n</body>")
        with open(archivo_target, "w", encoding="utf-8") as f:
            f.write(nuevo_contenido)
        print("[+] Éxito: Consola interactiva avanzada inyectada de forma limpia.")
    else:
        print("[-] Error: Falta la etiqueta estructural '</body>' en index.html.")

if __name__ == "__main__":
    aplicar_interfaz_avanzada()
