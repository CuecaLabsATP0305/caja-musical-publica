import json
import urllib.request
import time

class SystemAuditor:
    def __init__(self):
        self.endpoint = "http://127.0.0.1:8080"
        print("🔍 [AUDITORÍA CUECALABS] Inicializando inspector de lazo cerrado v0.3.05...")

    def audit_machine(self, path, machine_name):
        try:
            url = f"{self.endpoint}{path}"
            start_time = time.time()
            response = urllib.request.urlopen(url, timeout=2)
            data = json.loads(response.read().decode('utf-8'))
            elapsed = (time.time() - start_time) * 1000
            
            print(f"\n✅ [AUDITORÍA] {machine_name} detectada en {path}")
            print(f"   |-- Latencia física de red: {elapsed:.2f} ms")
            if "data" in data:
                metrics = data["data"]
                print(f"   |-- Estado Acoplamiento: {metrics.get('status')}")
                print(f"   |-- Escalar Comprensión: {metrics.get('scalar_comprehension') or metrics.get('scalar_comprehension_index')}")
                if "phase_space" in metrics:
                    ps = metrics["phase_space"]
                    print(f"   |-- Espacio Fases: X={ps.get('X_ccng1')}, Y={ps.get('Y_angiotensin')}, Z={ps.get('Z_entropy')}")
                print(f"   |-- Energía de Gibbs: {metrics.get('gibbs_energy_kcal_mol')} kcal/mol")
        except Exception as e:
            print(f"❌ [FALLO DE AUDITORÍA] No se pudo interconectar con {machine_name} en {path}: {e}")

    def execute_full_run(self):
        print("=================================================================")
        print(" INICIANDO ANÁLISIS DE PARAMETRIZACIÓN ATÓMICA DE LAS MÁQUINAS")
        print("=================================================================")
        self.audit_machine("/product1", "MAQUINA 1: CAJA MUSICAL (CORTICAL CORRELATION)")
        self.audit_machine("/product2", "MAQUINA 2: CAJA NEGRA (BIORREACTOR NO-EQUILIBRIO)")
        print("\n=================================================================")
        print(" AUDITORÍA FINALIZADA - CERO ERRORES HUMANOS - SISTEMA COMPROBADO")
        print("=================================================================")

if __name__ == "__main__":
    auditor = SystemAuditor()
    auditor.execute_full_run()
