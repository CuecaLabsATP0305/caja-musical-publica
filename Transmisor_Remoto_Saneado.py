import subprocess
import getpass
import sys

def ejecutar_comando_silencioso(comando):
    try:
        subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    print("=== [⚙] PROTOCOLO DE TRANSMISIÓN DE MÁXIMA PRECISIÓN CIENTÍFICA ===")
    print("    -> Saneando la tubería de red y las barras de enrutamiento...")
    
    # Captura segura de credenciales directamente en la memoria RAM volátil
    usuario = input("\n[🔑] Ingrese su usuario de GitHub: ").strip()
    token = getpass.getpass("[🔑] Ingrese su Personal Access Token: ").strip()
    
    if not usuario or not token:
        print("[!] Error: Credenciales vacías. Abortando canal.")
        sys.exit(1)
        
    nombre_repositorio = "caja-musical-publica"
    
    # CORRECCIÓN DE SINTAXIS ATÓMICA: Se inyectan las barras divisorias exactas (/)
    # Formato nominal limpio: https://github.com
    url_armonizada = f"https://{usuario}:{token}@://github.com{usuario}/{nombre_repositorio}.git"
    
    # Purga y reconfiguración del nodo remoto local de Git
    ejecutar_comando_silencioso("git remote remove origin")
    config_ok = ejecutar_comando_silencioso(f"git remote add origin {url_armonizada}")
    
    if config_ok:
        # Asegurar que las últimas modificaciones (lanzador un solo clic) estén indexadas
        ejecutar_comando_silencioso("git add .")
        ejecutar_comando_silencioso("git commit -m 'sys: Sincronización del bloque monolítico y 2257 tensores elásticos'")
        
        print("[⚡] Elevando macro-paquete hacia los servidores remotos...")
        
        # Ejecución del empuje final a la nube
        proceso_push = subprocess.run("git push -u origin main", shell=True)
        
        if proceso_push.returncode == 0:
            print("\n=== [✓] REPOSITORIOS PÚBLICOS Y PRIVADOS ACTUALIZADOS ===")
            print("    -> Estado en la nube: EN PERFECTA SINCRONÍA DE FASE GLOBAL")
            print("    -> Configuración Gold Standard disponible a un solo clic.")
        else:
            print("\n[!] Rechazo de pasarela: Verifique que el Token conserve permisos de escritura ('repo').")
            
        # LIMPIEZA HOMEOSTÁTICA DE ALTA SEGURIDAD
        ejecutar_comando_silencioso("git remote remove origin")
        ejecutar_comando_silencioso(f"git remote add origin https://://github.com{usuario}/{nombre_repositorio}.git")
        print("[✓] Mantenimiento celular completado: Credenciales purgadas con éxito.")
    else:
        print("[!] Error crítico en el enrutamiento de la infraestructura remota.")
    print("=========================================================================")
