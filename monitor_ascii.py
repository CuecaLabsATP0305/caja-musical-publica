import json
import os
import sys

def renderizar_atractor():
    if not os.path.exists("registro_lazo_cerrado.json"):
        print("[ERROR] Archivo de persistencia de fases no encontrado.")
        return
        
    with open("registro_lazo_cerrado.json", "r") as f:
        data = json.load(f)
    
    if not data or not isinstance(data, list):
        print("[AVISO] Registro vacío. Ejecute la rampa primero.")
        return

    # Extraer las últimas coordenadas calculadas por la matriz MPC
    ultimo_ciclo = data[-1]["telemetria"]
    x = ultimo_ciclo["estados"][0]
    y = ultimo_ciclo["estados"][1]
    z = ultimo_ciclo["estados"][2]
    
    # Crear un lienzo ASCII plano (20 filas x 50 columnas)
    ancho, alto = 50, 20
    lienzo = [[" " for _ in range(ancho)] for _ in range(alto)]
    
    # Mapear coordenadas (0.0 a 1.2) a los índices del lienzo plano
    pos_x = int((x / 1.2) * (ancho - 1))
    pos_y = int((y / 1.2) * (alto - 1))
    
    # Dibujar la referencia ideal (Punto de equilibrio homeostático de la máquina)
    ref_x = int((1.0 / 1.2) * (ancho - 1))
    ref_y = int((1.0 / 1.2) * (alto - 1))
    lienzo[alto - 1 - ref_y][ref_x] = "☼"
    
    # Marcar la posición actual calculada
    lienzo[alto - 1 - pos_y][pos_x] = "⚛"
    
    print("\n" + "░"*54)
    print(f" MONITOR DE ESPACIO DE FASES ABSOLUTO - CUECALABS UNIVERSAL")
    print("░"*54)
    for fila in lienzo:
        print("│ " + "".join(fila) + " │")
    print(" └──" + "─"*ancho + "──┘")
    print(f" Telemetría Actual -> X (Ciclo): {x:.4f} | Y (Angiotensina): {y:.4f} | Z (Entropía): {z:.4f}")
    print(f" Simbología        -> ☼ : Punto Ideal de Homeostasis | ⚛ : Coordenada Actual del Lazo")
    print(" " + "="*52 + "\n")

if __name__ == "__main__":
    renderizar_atractor()
