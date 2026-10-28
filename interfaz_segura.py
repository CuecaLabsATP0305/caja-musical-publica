# -*- coding: utf-8 -*-
import json, os, time
try:
    with open("secrets/gsq_core_output.json", "r") as f: coords = json.load(f)
except: coords = [0.1, 0.1, 0.1]
try:
    with open("secrets/tactical_countermeasures.json", "r") as f: counter = json.load(f)
except: counter = {"ESTADO_DE_HOMEOSTASIS": "ACTIVO"}
try:
    while True:
        os.system("clear")
        print("========================================================================")
        print("      INTERFAZ DE MONITOREO DE LAZO CERRADO - CUECALABS CORE V0305     ")
        print("========================================================================")
        print(" [ESTADO GLOBAL] : " + str(counter.get("ESTADO_DE_HOMEOSTASIS")))
        print(" [FIRMA DIGITAL] : cuecalabs ATP 0305")
        print("------------------------------------------------------------------------")
        print(" COORDENADAS DEL ESPACIO DE FASES BIOFÍSICO (GSQ-CORE-LORENZ-RK4):")
        print("   X (CCNG1 / Ciclo Celular)         :  " + f"{coords[0]:.4f}")
        print("   Y (Angiotensina / Receptores)     :  " + f"{coords[1]:.4f}")
        print("   Z (Entropía / Disipación Térmica) :  " + f"{coords[2]:.4f}")
        print("========================================================================")
        time.sleep(2)
except KeyboardInterrupt: print("\n[MAQUINA PRIVADA] -> Interfaz Cerrada.\n")
