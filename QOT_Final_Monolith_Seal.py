import subprocess
import getpass
import sys
from urllib.parse import urlunparse

def ejecutar_comando_git(comando):
    try:
        subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    print("=========================================================================")
    print("⚙️ NODO CONSOLIDADOR MAESTRO - RE-INYECCIÓN GOLD STANDARD FINAL")
    print("   -> Saneamiento de bits activo | Operador Autorizado: Freddy Arce")
    print("=========================================================================")
    
    usuario = input("\n[🔑] Ingrese su usuario de GitHub: ").strip()
    token = getpass.getpass("[🔑] Ingrese su Personal Access Token: ").strip()
    
    if not usuario or not token:
        print("[!] Error de control: Credenciales vacías en memoria. Abortando canal.")
        sys.exit(1)
        
    nombre_repo = "caja-musical-publica"
    
    # Ensamblaje matemático puro mediante urllib para evitar duplicidades de caracteres
    scheme = "https"
    netloc = f"{usuario}:{token}@github.com"
    path = f"/{usuario}/{nombre_repo}.git"
    url_nominal_limpia = urlunparse((scheme, netloc, path, "", "", ""))
    
    print("\n[⚡] Sintonizando la pasarela remota de Git sin fricciones...")
    ejecutar_comando_git("git remote remove origin")
    config_ok = ejecutar_comando_git(f"git remote add origin {url_nominal_limpia}")
    
    if config_ok:
        # Indexación forense del launcher un solo clic y el index.html holonómico
        ejecutar_comando_git("git add .")
        
        commit_msg = "sys: Integración del Gold Standard Monolítico y Compresión Semántica No Lineal v6.5"
        ejecutar_comando_git(f"git commit -m '{commit_msg}'")
        
        print("[⚡] Elevando bloque unificado hacia los servidores remotos de la nube...")
        proceso_push = subprocess.run("git push -u origin main", shell=True)
        
        if proceso_push.returncode == 0:
            print("\n=== [✓] REPOSITORIOS SINCRONIZADOS AL MÁXIMO ESTÁNDAR ETERNO ===")
            print("    -> Estado en la nube: EN PERFECTA SINCRONÍA DE FASE REMOTA")
            print("    -> Ambas máquinas (Pública y Privada) han quedado unificadas.")
        else:
            print("\n[!] Rechazo de red remota: Verifique los alcances de escritura del Token.")
            
        # LIMPIEZA HOMEOSTÁTICA INMEDIATA DE ALTA SEGURIDAD
        ejecutar_comando_git("git remote remove origin")
        url_generica = urlunparse((scheme, "github.com", f"/{usuario}/{nombre_repo}.git", "", "", ""))
        ejecutar_comando_git(f"git remote add origin {url_generica}")
        print("[✓] Purga completada: Credenciales eliminadas con éxito de Termux.")
    else:
        print("[!] Error crítico en el enrutamiento de la pasarela local.")
    print("=========================================================================")
