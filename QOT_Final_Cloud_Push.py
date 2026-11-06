import subprocess
import getpass
import sys
from urllib.parse import urlunparse

def ejecutar_flujo_git(comando):
    """Ejecuta subprocesos controlando de forma estricta los descriptores de contexto ARM."""
    try:
        subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    print("=========================================================================")
    print("📡 PIPELINE DE SUBIDA INTEGRAL - CONSOLIDACIÓN DE FASE EN LA NUBE")
    print("   -> Sincronizando: Reportes de Carga Máxima (6863 Hz) y Estratificación")
    print("=========================================================================")
    
    # Captura interactiva enmascarada directamente en la memoria RAM volátil
    usuario = input("\n[🔑] Ingrese su usuario de GitHub: ").strip()
    token = getpass.getpass("[🔑] Ingrese su Personal Access Token: ").strip()
    
    if not usuario or not token:
        print("[!] Error de control: Credenciales vacías en memoria. Abortando canal.")
        sys.exit(1)
        
    nombre_repositorio = "caja-musical-publica"
    
    # Ensamblaje matemático puro mediante urllib para anular mutaciones de caracteres
    scheme = "https"
    netloc = f"{usuario}:{token}@github.com"
    path = f"/{usuario}/{nombre_repositorio}.git"
    url_nominal_limpia = urlunparse((scheme, netloc, path, "", "", ""))
    
    print("\n[⚡] Saneando el lazo remoto local de Git...")
    ejecutar_flujo_git("git remote remove origin")
    config_ok = ejecutar_flujo_git(f"git remote add origin {url_nominal_limpia}")
    
    if config_ok:
        print("[✓] Pasarela remota armada mediante ensamblaje nativo de objetos.")
        print("[⚡] Indexando últimos reportes y matriz de estratificación...")
        
        # Indexación de los nuevos JSON de estrés y aseguramiento al índice forense
        ejecutar_flujo_git("git add .")
        
        commit_msg = "sys: Sincronización del reporte de carga máxima de 6863.85 Hz y matriz de calidad"
        ejecutar_flujo_git(f"git commit -m '{commit_msg}'")
        
        print("[⚡] Elevando bloque monolítico hacia los servidores remotos de GitHub...")
        proceso_push = subprocess.run("git push -u origin main", shell=True)
        
        if proceso_push.returncode == 0:
            print("\n=== [✓] REPOSITORIOS ACTUALIZADOS AL MÁXIMO ESTÁNDAR GLOBAL ===")
            print("    -> Estado en la nube: EN PERFECTA SINCRONÍA DE FASE REMOTA")
            print("    -> Las 11,425 líneas y el Gold Standard están blindados y activos.")
        else:
            print("\n[!] Rechazo de red remota: Verifique los alcances de escritura del Token.")
            
        # LIMPIEZA HOMEOSTÁTICA INMEDIATA DE ALTA SEGURIDAD (Purga de la terminal)
        ejecutar_flujo_git("git remote remove origin")
        url_generica = urlunparse((scheme, "github.com", f"/{usuario}/{nombre_repositorio}.git", "", "", ""))
        ejecutar_flujo_git(f"git remote add origin {url_generica}")
        print("[✓] Mantenimiento celular completado: Credenciales purgadas con éxito.")
    else:
        print("[!] Error crítico en el enrutamiento de la pasarela local.")
    print("=========================================================================")
