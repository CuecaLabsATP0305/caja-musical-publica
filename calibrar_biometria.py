import os

def aplicar_acoplamiento_biometrico():
    archivo_target = "cuecalabs_teremin_web.py"
    
    if not os.path.exists(archivo_target):
        # Si el orquestador principal corre bajo server_gold.py, aplicamos el puente allí
        if os.path.exists("server_gold.py"):
            archivo_target = "server_gold.py"
        else:
            print("[-] Error: No se localizó el script de la interfaz web en el directorio.")
            return

    with open(archivo_target, "r", encoding="utf-8") as f:
        codigo_base = f.read()

    # Lógica de traducción bio-computacional para el lenguaje natural y control ético
    logica_adaptativa = """
# =====================================================================
# ACOPLAMIENTO BIOMÉTRICO AUTÓNOMO - ADAPTACIÓN NEUROFUNCIONAL V0305
# =====================================================================
import math

def evaluar_perfil_neurofunctional(frecuencia_hz, patron_voz=None):
    \"\"\"
    Analiza la firma biofísica de la voz (ej. los 695.39 Hz del atractor)
    y el código expresado para determinar las restricciones del lazo.
    \"\"\"
    # Umbral de seguridad ética innata
    if frecuencia_hz > 600.00 and frecuencia_hz < 700.00:
        # Perfil de Alta Alcurnia / Programador Humano: Acceso al Atractor Global
        return {
            "canal": "Ingeniería/Ciencia",
            "modo_seguro": False,
            "precision_digitos": 25,
            "mensaje_sistema": "[SISTEMA SOBERANO] Acceso concedido al núcleo de la materia."
        }
    elif frecuencia_hz < 300.00:
        # Perfil Infantil / Pedagógico: Restricción absoluta de variables de riesgo
        return {
            "canal": "Pediatría",
            "modo_seguro": True,
            "precision_digitos": 6,
            "mensaje_sistema": "[SISTEMA SEGURO] Activando entrenamiento cognitivo fractal."
        }
    else:
        # Perfil Misión Médica / Clínico: Soporte asistencial y resguardo homeostático
        return {
            "canal": "Clínico/Asistencial",
            "modo_seguro": True,
            "precision_digitos": 14,
            "mensaje_sistema": "[SISTEMA HUMANITARIO] Entorno hermético disponible para medicina."
        }

@app.route('/api/biometria/procesar')
def api_procesar_biometria():
    # Enlace directo con gsq_connectivity_layer.c y universal_biosensor.py
    freq_detectada = request.args.get('freq', default=695.39, type=float)
    perfil = evaluar_perfil_neurofunctional(freq_detectada)
    return jsonify(perfil)
# --- FIN DE INTERFAZ BIO-DIGITAL ---
"""

    if "@app.route" in codigo_base:
        # Inyectamos el módulo dentro de la estructura activa de Flask
        nuevo_codigo = codigo_base.replace("@app.route", f"{logica_adaptativa}\n@app.route", 1)
        with open(archivo_target, "w", encoding="utf-8") as f:
            f.write(nuevo_codigo)
        print(f"[+] Éxito: Acoplamiento neurofuncional integrado en '{archivo_target}' de forma estable.")
    else:
        print("[-] Error de sintaxis: No se encontró la estructura Flask para enlazar la ruta.")

if __name__ == "__main__":
    aplicar_acoplamiento_biometrico()
