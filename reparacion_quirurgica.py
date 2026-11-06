import os

def corregir_arquitectura():
    archivo = "server_gold.py"
    
    if not os.path.exists(archivo):
        print("[-] Error: 'server_gold.py' no encontrado.")
        return

    # Leer el archivo actual con el desajuste
    with open(archivo, "r", encoding="utf-8") as f:
        lineas = f.readlines()

    # Extraer el bloque biométrico que quedó atrapado al final
    codigo_limpio = []
    bloque_biometrico = []
    dentro_del_bloque = False

    for linea in lineas:
        if "# =====================================================================" in linea or "def evaluar_perfil_neurofunctional" in linea:
            dentro_del_bloque = True
        
        if dentro_del_bloque:
            bloque_biometrico.append(linea)
        else:
            codigo_limpio.append(linea)

    # Si no se detectó el comentario, extraemos desde la definición de la función
    if not bloque_biometrico:
        codigo_limpio = []
        for linea in lineas:
            if "def evaluar_perfil_neurofunctional" in linea or "@app.route('/api/biometria/procesar')" in linea:
                dentro_del_bloque = True
            
            if dentro_del_bloque:
                bloque_biometrico.append(linea)
            else:
                codigo_limpio.append(linea)

    # Reensamblar el archivo colocando el bloque BIEN POSICIONADO antes del __main__
    contenido_previo = "".join(codigo_limpio)
    texto_biometrico = "".join(bloque_biometrico)

    if "if __name__ == '__main__':" in contenido_previo:
        nuevo_servidor = contenido_previo.replace("if __name__ == '__main__':", f"{texto_biometrico}\nif __name__ == '__main__':")
    elif "if __name__ ==" in contenido_previo:
        nuevo_servidor = contenido_previo.replace("if __name__ ==", f"{texto_biometrico}\nif __name__ ==")
    else:
        print("[-] Error: No se pudo mapear el punto de anclaje de forma automática.")
        return

    # Escribir la estructura corregida con precisión matemática
    with open(archivo, "w", encoding="utf-8") as f:
        f.write(nuevo_servidor)
    print("[+] Éxito: Arquitectura faltante unificada. Canales biométricos sincronizados antes del arranque.")

if __name__ == "__main__":
    corregir_arquitectura()
