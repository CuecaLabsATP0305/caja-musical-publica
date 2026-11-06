import os

def aplicar_parche_limpio():
    archivo_target = "server_gold.py"
    
    if not os.path.exists(archivo_target):
        print("[-] Error: 'server_gold.py' no encontrado.")
        return

    with open(archivo_target, "r", encoding="utf-8") as f:
        codigo = f.read()

    # Módulo biométrico adaptativo nativo corregido y limpio
    bloque_biometrico = """
# =====================================================================
# MODULACIÓN BIOMÉTRICA AUTÓNOMA - SISTEMA ADAPTATIVO V0305
# =====================================================================
from flask import request, jsonify

def evaluar_perfil_neurofunctional(frecuencia_hz):
    if 600.00 <= frecuencia_hz <= 700.00:
        return {
            "canal": "Ingeniería/Ciencia",
            "modo_seguro": False,
            "precision_digitos": 25,
            "mensaje": "[CUECALABS CORE] Acceso autorizado al programador humano."
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

    # Inyección precisa justo después de que la instancia 'app' esté completamente construida
    if "app = Flask(__name__)" in codigo:
        nuevo_codigo = codigo.replace("app = Flask(__name__)", f"app = Flask(__name__)\n{bloque_biometrico}")
    elif "app = Flask" in codigo:
        nuevo_codigo = codigo.replace("app = Flask", f"app = Flask\n{bloque_biometrico}")
    else:
        # Si no encuentra el patrón, lo inyecta de forma segura al final de las importaciones
        nuevo_codigo = codigo + "\n" + bloque_biometrico

    with open(archivo_target, "w", encoding="utf-8") as f:
        f.write(nuevo_codigo)
    print("[+] Éxito: Modulación biométrica posicionada correctamente en el ciclo de Flask.")

if __name__ == "__main__":
    aplicar_parche_limpio()
