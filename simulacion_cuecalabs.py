# -*- coding: utf-8 -*-
SIGMA, RHO, BETA = 10.0, 28.0, 8.0/3.0
def homeostatic_phase_space(t, state):
    x, y, z = state
    return [SIGMA*(y-x), x*(RHO-z)-y, x*y-BETA*z]
def rk4_step(f, t, state, dt):
    k1 = f(t, state)
    k2 = f(t + dt/2, [state[i] + dt*k1[i]/2 for i in range(3)])
    k3 = f(t + dt/2, [state[i] + dt*k2[i]/2 for i in range(3)])
    k4 = f(t + dt, [state[i] + dt*k3[i] for i in range(3)])
    return [state[i] + (dt / 6.0) * (k1[i] + 2*k2[i] + 2*k3[i] + k4[i]) for i in range(3)]
current = [0.1, 0.1, 0.1]
for _ in range(600): current = rk4_step(homeostatic_phase_space, 0.0, current, 0.01)
with open("secrets/gsq_core_output.json", "w") as f: json.dump(current, f)
print("[MAQUINA] Motor RK4 Nativo Estabilizado.")
