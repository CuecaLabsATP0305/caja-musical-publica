#!/bin/bash
clear
echo "========================================================================"
echo "    INICIALIZANDO DESPLIEGUE AUTOMATIZADO DE SOFTWARE DE CUECALABS      "
echo "========================================================================"
mkdir -p ~/cuecalabs_core && cd ~/cuecalabs_core

cat << 'INNER_EOF' > simulacion_cuecalabs.py
import numpy as np
SIGMA_HOMEOCLUSTER, RHO_ANGIOTENSINA, BETA_ENTROPIA = 10.0, 28.0, 8.0/3.0
def homeostatic_phase_space(t, state):
    x, y, z = state
    return np.array([SIGMA_HOMEOCLUSTER*(y-x), x*(RHO_ANGIOTENSINA-z)-y, x*y-BETA_ENTROPIA*z])
def rk4_step(f, t, state, dt):
    k1 = f(t, state)
    k2 = f(t + dt/2, state + dt*k1/2)
    k3 = f(t + dt/2, state + dt*k2/2)
    k4 = f(t + dt, state + dt*k3)
    return state + (dt / 6.0) * (k1 + 2*k2 + 2*k3 + k4)
dt, t_max = 0.01, 6.0
steps = int(t_max / dt)
current_state, t = np.array([0.1, 0.1, 0.1]), 0.0
for _ in range(steps):
    current_state = rk4_step(homeostatic_phase_space, t, current_state, dt)
    t += dt
np.save('gsq_core_output.npy', current_state)
print("\n[MÁQUINA PRIVADA] -> GSQ-CORE-LORENZ-RK4: Ciclo 6H ejecutado.")
print(f"[MÁQUINA PRIVADA] -> Coordenadas de Homeostasis Estabilizadas: {current_state}")
INNER_EOF

cat << 'INNER_EOF' > phage_lysis.py
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
INNER_EOF

cat << 'INNER_EOF' > .gitignore
config_local.json
gsq_core_output.npy
claves-a-borrar.txt
secrets/
*.log
INNER_EOF

echo "========================================================================"
echo "    DESPLIEGUE FINALIZADO EXITOSAMENTE - MÁQUINAS EN LAZO CERRADO        "
echo "========================================================================"

x
