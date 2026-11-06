import os

def aplicar_parche_al_final():
    archivo_target = "server_gold.py"
    
    if not os.path.exists(archivo_target):
        print("[-] Error: 'server_gold.py' no encontrado.")
        return

    with open(archivo_target, "r", encoding="utf-8") as f:
        codigo_original = f.read()

    # Módulo de adaptación biométrica por voz (Uso racional y ético)
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

    # Concatenamos de forma segura al final del archivo original
    nuevo_codigo = codigo_original + "\n" + bloque_biometrico

    with open(archivo_target, "w", encoding="utf-8") as f:
        f.write(nuevo_codigo)
    print("[+] Éxito: Modulación biométrica concatenada de forma segura al final del servidor.")

if __name__ == "__main__":
    aplicar_parche_al_final()
