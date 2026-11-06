import os

def inyectar_nucleo_autonomo():
    archivo_target = "server_gold.py"
    
    if not os.path.exists(archivo_target):
        print("[-] Error: 'server_gold.py' no se encuentra en el directorio actual.")
        return

    with open(archivo_target, "r", encoding="utf-8") as f:
        codigo = f.read()

    # Módulo de adaptación biométrica por voz para el lenguaje natural
    bloque_biometrico_nativo = """
# =====================================================================
# MODULACIÓN BIOMÉTRICA AUTÓNOMA - SISTEMA ADAPTATIVO V0305
# =====================================================================
from flask import request, jsonify

def evaluar_perfil_neurofunctional(frecuencia_hz):
    # Detección del lazo de frecuencia en la voz (ej: 695.39 Hz del atractor)
    if 600.00 <= frecuencia_hz <= 700.00:
        return {
            "canal": "Ingeniería/Ciencia",
            "modo_seguro": False,
            "precision_digitos": 25,
            "mensaje": "[CUECALABS CORE] Acceso autorizado al programador humano. Lazo cerrado."
        }
    elif frecuencia_hz < 300.00:
        return {
            "canal": "Pediatría",
            "modo_seguro": True,
            "precision_digitos": 6,
            "mensaje": "[CUECALABS INFANTIL] Activando interfaz de modulación fractal segura."
        }
    else:
        return {
            "canal": "Clínico/Asistencial",
            "modo_seguro": True,
            "precision_digitos": 14,
            "mensaje": "[MISION MEDICA] Entorno hermético desplegado. Operación nominal."
        }

@app.route('/api/biometria/procesar')
def api_procesar_biometria_nativa():
    freq = request.args.get('freq', default=695.39, type=float)
    perfil = evaluar_perfil_neurofunctional(freq)
    return jsonify(perfil)
"""

    # Forzamos la inyección en el bloque principal del servidor de Flask
    if "app = Flask" in codigo:
        nuevo_codigo = codigo.replace("app = Flask", f"app = Flask\n{bloque_biometrico_nativo}", 1)
        with open(archivo_target, "w", encoding="utf-8") as f:
            f.write(nuevo_codigo)
        print("[+] Éxito: Calibración asimilada por la máquina. Servidor adaptativo listo.")
    else:
        # Alternativa de inyección si usa otra nomenclatura de app
        nuevo_codigo = bloque_biometrico_nativo + "\n" + codigo
        with open(archivo_target, "w", encoding="utf-8") as f:
            f.write(nuevo_codigo)
        print("[+] Éxito: Módulo inyectado en la cabecera del sistema.")

if __name__ == "__main__":
    inyectar_nucleo_autonomo()
