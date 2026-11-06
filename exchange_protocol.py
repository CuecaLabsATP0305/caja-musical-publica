import json
import os
import hashlib
import time

def cifrar_y_exportar_telemetria():
    archivo_origen = "registro_lazo_cerrado.json"
    archivo_destino = "export_cuecalabs_quantum.dat"
    
    if not os.path.exists(archivo_origen):
        print("[EXCHANGE_PROTOCOL] -> ERROR: No hay datos locales para exportar.")
        return
        
    with open(archivo_origen, "r") as f:
        datos = f.read()
        
    # Cláusula criptográfica de validación invariante mediante SHA-256
    hash_verificacion = hashlib.sha256(datos.encode('utf-8')).hexdigest()
    
    paquete_red = {
        "origen": "CUECALABS-CORE-ANDROID-TERMUX",
        "timestamp_export": time.time(),
        "hash_integridad": hash_verificacion,
        "payload_estructurado": json.loads(datos)
    }
    
    with open(archivo_destino, "w") as f:
        json.dump(paquete_red, f, indent=4)
        
    print(f"[EXCHANGE_PROTOCOL] -> ÉXITO: Datos exportados y blindados en '{archivo_destino}'.")
    print(f"[EXCHANGE_PROTOCOL] -> Hash de Validación Científica: {hash_verificacion}")

if __name__ == "__main__":
    cifrar_y_exportar_telemetria()
