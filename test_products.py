import urllib.request
import json
import time

# Rectificación del Hostname Local y el Puerto Basal de Red
url = "http://127.0.0.1:8080"

def enviar_peticion(nombre_prueba, payload):
    print(f"\n=== Ejecutando Prueba: {nombre_prueba} ===")
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            print(f"Respuesta del Servidor: {json.dumps(res_data, indent=2)}")
    except Exception as e:
        print(f"Error en la conexión: {e}")

# 1. Validación de la Caja Musical Científica (Canal de Pedagogía Universal)
peticion_musical = {
    "rol": "UNIVERSAL_PEDAGOGY",
    "escala_social": "COMUNIDAD_LOCAL",
    "prompt": "Consulta automatizada para el cierre de brechas cognitivas en escuela rural."
}
enviar_peticion("PRODUCTO 1: CAJA MUSICAL CIENTÍFICA", peticion_musical)

time.sleep(1)

# 2. Validación de la Caja Negra Industrial (Canal Comercial de Alta Tecnología)
peticion_industrial = {
    "rol": "INDUSTRIAL_COMMERCE",
    "escala_social": "MACRO_ESTATAL",
    "cliente": "Consorcio Industrial Global",
    "prompt": "Solicitud automatizada de optimización de redes energéticas fractales mediante corrientes naturales."
}
enviar_peticion("PRODUCTO 2: CAJA NEGRA INDUSTRIAL", peticion_industrial)
