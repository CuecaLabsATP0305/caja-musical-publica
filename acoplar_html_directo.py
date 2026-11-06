import os

def forzar_render_local():
    archivo_target = "server_gold.py"
    
    if not os.path.exists(archivo_target):
        print("[-] Error: 'server_gold.py' no encontrado.")
        return

    # Limpiar cualquier modificación previa errónea en el servidor usando Git
    os.system("git checkout server_gold.py")

    with open(archivo_target, "r", encoding="utf-8") as f:
        codigo = f.read()

    # Función inyectable que lee el HTML físico y lo transmite por el puerto 8080
    funcion_render = """
@app.route('/')
def render_interfaz_tactil_maestro():
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"Error en el lazo de interfaz: {str(e)}"
"""

    # Inyectamos la ruta maestra justo antes del bloque __main__ para asegurar la carga
    if "if __name__" in codigo:
        nuevo_codigo = codigo.replace("if __name__", f"{funcion_render}\nif __name__")
        with open(archivo_target, "w", encoding="utf-8") as f:
            f.write(nuevo_codigo)
        print("[+] Éxito: Enrutamiento directo a index.html configurado en el backend.")
    else:
        print("[-] Error: No se encontró el punto de anclaje de ejecución.")

if __name__ == "__main__":
    forzar_render_local()
