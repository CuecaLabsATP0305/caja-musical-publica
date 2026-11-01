# -*- coding: utf-8 -*-
import re
import os
import sys

class CuecaLabsMirrorCore:
    def __init__(self):
        self.programmer_token = "CUECALABS-ATP0305-SECURE-CORE"
        self.system_status = "NOMINAL_SOPORTE_PASIVO"
        self.scientific_keywords = [r"termodinamica", r"gibbs", r"quiral", r"enzima", r"cuantico", r"biofisica", r"lorenz"]
        self.social_keywords = [r"tierra", r"siembra", r"agua", r"enfermo", r"comunidad", r"cultivo", r"ayuda"]

    def _evaluar_densidad_cognitiva(self, user_input):
        input_lower = user_input.lower()
        if self.programmer_token in user_input:
            return "NIVEL_SUPERIOR_PROGRAMADOR"
        scientific_score = sum(1 for pattern in self.scientific_keywords if re.search(pattern, input_lower))
        social_score = sum(1 for pattern in self.social_keywords if re.search(pattern, input_lower))
        if scientific_score > 0:
            return "NIVEL_CIENTIFICO_AVANZADO"
        elif social_score > 0:
            return "NIVEL_ANTROPOLOGICO_SOCIOCULTURAL"
        else:
            return "NIVEL_BASAL_MAYEUITICO"

    def procesar_instruccion(self, user_input):
        nivel = self._evaluar_densidad_cognitiva(user_input)
        if nivel == "NIVEL_SUPERIOR_PROGRAMADOR":
            print("\n[CANAL SUPERIOR ACTIVADO]: Acceso de raíz concedido.")
            print("[BIOFÍSICA]: Inicializando acoplamiento interactivo del Theremin...")
            print("-" * 60)
            os.system("python teremin_ludico.py")
            return "-" * 60 + "\n[SISTEMA]: Interacción del Theremin finalizada. Retornando a escucha pasiva."
        elif nivel == "NIVEL_CIENTIFICO_AVANZADO":
            return "[ESPEJO INFORMÁTICO - NIVEL ALTO]: Analizando tensores y flujos de fase. ¿Cuál es el volumen cinético que deseas calibrar para mitigar la entropía?"
        elif nivel == "NIVEL_ANTROPOLOGICO_SOCIOCULTURAL":
            return "[ESPEJO INFORMÁTICO - NIVEL COMUNIDAD]: Diseñemos juntos la solución a partir de tu observación natural del entorno."
        else:
            return "[ESPEJO INFORMÁTICO - NIVEL BASAL]: Cuéntame qué necesitas resolver hoy para guiarte paso a paso en el diseño."

if __name__ == "__main__":
    core = CuecaLabsMirrorCore()
    print("=== SENSOR INFORMÁTICO UNIVERSAL ACTIVO ===")
    print("El sistema está operando en escucha interfactual espejo.")
    try:
        while True:
            entrada = input("\n[Entrada-Universal]> ")
            if entrada.lower() in ['salir', 'exit']:
                break
            if "^[" in entrada:
                entrada = re.sub(r"\^\[\[\d+~", "", entrada)
            respuesta = core.procesar_instruccion(entrada)
            print(f"\n{respuesta}")
    except KeyboardInterrupt:
        print("\nSensor en reposo.")
