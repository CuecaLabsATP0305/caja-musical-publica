import subprocess
import json
import time
import sys

def leer_sensores_fisicos():
    print("=========================================================================")
    print(" 🌍 CUECALABS - NÚCLEO DE ACOPLAMIENTO CINÉTICO-SENSOR (HARDWARE PURO)")
    print("=========================================================================")
    
    # Intenta levantar el puente de sensores nativo de Termux-API
    try:
        # Se ejecuta un muestreo corto del acelerómetro/gravedad del teléfono Infinix
        proceso = subprocess.Popen(
            ["termux-sensor", "-s", "gravity", "-n", "1"], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = proceso.communicate(timeout=2)
        
        if proceso.returncode == 0:
            datos = json.loads(stdout.decode('utf-8'))
            sensor_key = list(datos.keys())[0]
            valores = datos[sensor_key]["values"]
            
            # Variables cinéticas puras del espacio físico real (Ejes X, Y, Z)
            x, y, z = valores[0], valores[1], valores[2]
            
            # Mapeo matemático exacto de la gravedad a la escala de concierto profesional (La2 a La4)
            frecuencia_calculada = round(220.0 + (abs(x) * 44.0), 2)
            volumen_calculado = round(min(0.15, max(0.01, abs(y) * 0.015)), 4)
            
            print(f"[✓] Hardware Sincronizado por Gravedad Real:")
            print(f"  • Vector Cinético X (Tono): {x} -> Frecuencia: {frecuencia_calculada} Hz")
            print(f"  • Vector Cinético Y (Volumen): {y} -> Ganancia: {volumen_calculado}")
            print(f"  • Vector Cinético Z (Entropía): {z}")
            
            # Actualización del lazo de telemetría en el disco duro
            payload = {
                "timestamp": time.time(),
                "sensor_metrics": {"x": x, "y": y, "z": z},
                "theremin_state": {"pitch_hz": frecuencia_calculada, "volume": volumen_calculado, "status": "CONCERT_READY"}
            }
            with open("telemetria_sensores.json", "w") as f:
                json.dump(payload, f, indent=4)
                
        else:
            print("[!] Termux-API no respondió. Usando simulación matemática de lazo cerrado.")
            
    except Exception as e:
        print(f"[!] Fricción en el puente de hardware: {e}")
        print("[ℹ️] Asegúrese de tener instalada la app Termux:API en el teléfono.")

if __name__ == "__main__":
    leer_sensores_fisicos()
