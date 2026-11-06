import base64
import getpass
import subprocess

def ejecutar_paso_absoluto():
    print("=========================================================================")
    print(" 🌍 CUECALABS - NÚCLEO INTERACTIVO DE AUTENTICACIÓN MATEMÁTICA V3")
    print("=========================================================================")
    
    usuario = input("[⚙️] Escriba su usuario de GitHub (Ej: CuecaLabsATP0305): ").strip()
    token_crudo = getpass.getpass("[⚙️] Pegue su Token de Acceso Personal (PAT): ").strip()
    
    if not token_crudo:
        print("[!] Error: El token no puede ser una cadena vacía.")
        return

    print("\n[1/3] Codificando credenciales en la matriz binaria local...")
    token_bytes = token_crudo.encode('utf-8')
    token_b64 = base64.b64encode(token_bytes).decode('utf-8')
    token_decodificado = base64.b64decode(token_b64.encode('utf-8')).decode('utf-8')
    
    print("[2/3] Configurando origen remoto con URL unificada y limpia...")
    # Concatenación nativa limpia: https://github.com
    repo_url = f"https://{usuario}:{token_decodificado}@://github.com{usuario}/caja-musical-publica.git"
    
    subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
    subprocess.run(["git", "remote", "add", "origin", repo_url])
    
    print("[3/3] Sincronizando y empujando bloques monolíticos a la red global...")
    resultado = subprocess.run(["git", "push", "-u", "origin", "main"])
    
    if resultado.returncode == 0:
        print("=========================================================================")
        print(" 🎉 LAZO CERRADO CONSOLIDADO: REPOSITORIO EN VIVO EN GITHUB")
        print("=========================================================================")
    else:
        print("[!] Despliegue en 'main' rebotado. Intentando canal de respaldo 'master'...")
        subprocess.run(["git", "push", "-u", "origin", "master"])

if __name__ == "__main__":
    ejecutar_paso_absoluto()
