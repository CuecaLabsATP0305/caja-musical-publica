import numpy as np
import time, sys
def generate_lytic_payload():
    SIGMA_LYTIC, RHO_BURST, BETA_DECAY = 40.0, 150.0, 12.0
    state, dt = np.array([0.1, 0.1, 0.1]), 0.001
    print("[SISTEMA DEFENSA ACTIVA] -> Inicializando ciclo lítico...")
    try:
        while True:
            x, y, z = state
            state += np.array([SIGMA_LYTIC*(y-x), x*(RHO_BURST-z)-y, x*y-BETA_DECAY*z]) * dt
            sys.stdout.write(f"GSQ-CORE-MUTATION-ID-{x:0.4f}-{y:0.4f}-{z:0.4f}\n")
            sys.stdout.flush()
    except BrokenPipeError:
        print("\n[MÁQUINA PRIVADA] -> Lisis completada.")
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--activate-lytic-protocol":
        generate_lytic_payload()
    else:
        print("[MÁQUINA PRIVADA] -> Contramedida activa en modo latente.")
