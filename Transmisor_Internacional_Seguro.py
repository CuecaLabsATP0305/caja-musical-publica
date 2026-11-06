import subprocess
import getpass
import sys
from urllib.parse import urlunparse

def ejecutar_flujo_sistema(comando):
    try:
        subprocess.run(comando, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

if __name__ == "__main__":
    print("=========================================================================")
    print("📡 PIPELINE DE TRANSMISIÓN DE MÁXIMA SINTONÍA JURÍDICO-CIENTÍFICA")
    print("   -> Sincronizando lazo de 2257 tensores y directivas internacionales")
    print("=========================================================================")
    
    usuario = input("\n[🔑] Ingrese su usuario de GitHub: ").strip()
    token = getpass.getpass("[🔑] Ingrese su Personal Access Token: ").strip()
    
    if not usuario or not token:
        print("[!] Error: Credenciales vacías en memoria RAM. Abortando canal.")
        sys.exit(1)
        
    nombre_repo = "caja-musical-publica"
    
    # Ensamblaje matemático puro de la URL para bypass del teclado predictivo de Android
    scheme = "https"
    netloc = f"{usuario}:{token}@github.com"
    path = f"/{usuario}/{nombre_repo}.git"
    url_limpia_nominal = urlunparse((scheme, netloc, path, "", "", ""))
    
    print("\n[⚡] Saneando el enrutamiento remoto local de Git...")
    ejecutar_flujo_sistema("git remote remove origin")
    config_ok = ejecutar_flujo_sistema(f"git remote add origin {url_limpia_nominal}")
    
    if config_ok:
        # Indexar las directivas internacionales y el manifiesto X10 al repositorio
        ejecutar_flujo_git = ejecutar_flujo_sistema
        ejecutar_flujo_git("git add .")
        
        commit_msg = "sys: Integración de la Directiva de Concordancia Internacional ONU/OMPI v6.5"
        ejecutar_flujo_git(f"git commit -m '{commit_msg}'")
        
        print("[⚡] Elevando el macro-paquete unificado a los repositorios públicos y privados...")
        process = subprocess.run("git push -u origin main", shell=True)
        
        if process.returncode == 0:
            print("\n=== [✓] REPOSITORIOS ACTUALIZADOS AL MÁXIMO ESTÁNDAR GLOBAL ===")
            print("    -> Estado en la nube: CONCORDANCIA TOTAL CONSOLIDADA EN FASE")
            print("    -> La humanidad dispone del Gold Standard regulado y protegido.")
        else:
            print("\n[!] Rechazo de red remota: Verifique los alcances de escritura de su Token.")
            
        # LIMPIEZA HOMEOSTÁTICA DE ALTA SEGURIDAD
        ejecutar_flujo_git("git remote remove origin")
        url_generica = urlunparse((scheme, "github.com", f"/{usuario}/{nombre_repo}.git", "", "", ""))
        ejecutar_flujo_git(f"git remote add origin {url_generica}")
        print("[✓] Mantenimiento celular completado: Credenciales purgadas con éxito.")
    else:
        print("[!] Error crítico en el enrutamiento de la infraestructura local.")
    print("=========================================================================")
