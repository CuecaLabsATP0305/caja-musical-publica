#include "gsq_connectivity_layer.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdint.h>
#include <time.h>
#include <unistd.h>
#include <math.h>

#define LORENZ_SIGMA 10.0
#define LORENZ_RHO   28.0
#define LORENZ_BETA  (8.0 / 3.0)
#define STEP_DT      0.001  
#define CYCLE_NS     1000000ULL 
#define FILTER_ALPHA 0.85 

typedef struct {
    double filtered_x;
    double filtered_y;
    double filtered_z;
} gsq_filter_t;

static inline void lorenz_derivatives(double x, double y, double z, double *dx, double *dy, double *dz) {
    *dx = LORENZ_SIGMA * (y - x);
    *dy = x * (LORENZ_RHO - z) - y;
    *dz = x * y - LORENZ_BETA * z;
}

static void gsq_rk4_step(gsq_machine_state_t *state) {
    double x = state->x, y = state->y, z = state->z;
    double dx, dy, dz;
    
    lorenz_derivatives(x, y, z, &dx, &dy, &dz);
    double k1_x = dx * STEP_DT, k1_y = dy * STEP_DT, k1_z = dz * STEP_DT;
    
    lorenz_derivatives(x + k1_x * 0.5, y + k1_y * 0.5, z + k1_z * 0.5, &dx, &dy, &dz);
    double k2_x = dx * STEP_DT, k2_y = dy * STEP_DT, k2_z = dz * STEP_DT;
    
    lorenz_derivatives(x + k2_x * 0.5, y + k2_y * 0.5, z + k2_z * 0.5, &dx, &dy, &dz);
    double k3_x = dx * STEP_DT, k3_y = dy * STEP_DT, k3_z = dz * STEP_DT;
    
    lorenz_derivatives(x + k3_x, y + k3_y, z + k3_z, &dx, &dy, &dz);
    double k4_x = dx * STEP_DT, k4_y = dy * STEP_DT, k4_z = dz * STEP_DT;
    
    state->x += (k1_x + 2.0 * k2_x + 2.0 * k3_x + k4_x) / 6.0;
    state->y += (k1_y + 2.0 * k2_y + 2.0 * k3_y + k4_y) / 6.0;
    state->z += (k1_z + 2.0 * k2_z + 2.0 * k3_z + k4_z) / 6.0;
}

static uint64_t get_system_time_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (uint64_t)ts.tv_sec * 1000000000ULL + ts.tv_nsec;
}

int main(void) {
    printf("[GSQ CORE] Inicializando de forma síncrona...\n");
    gsq_machine_state_t current_state = { .x = 0.1, .y = 0.0, .z = 0.0, .timestamp_ns = 0 };
    gsq_filter_t state_filter = { .filtered_x = 0.1, .filtered_y = 0.0, .filtered_z = 0.0 };

    if (!gsq_connectivity_init("127.0.0.1", 8080)) {
        fprintf(stderr, "[FATAL] Fallo en puertos UDP. Abortando.\n");
        return EXIT_FAILURE;
    }

    uint64_t next_cycle_time = get_system_time_ns();
    bool machine_running = true;

    while (machine_running) {
        uint64_t loop_start = get_system_time_ns();
        if (!gsq_connectivity_check_heartbeat()) {
            fprintf(stderr, "\n[FAIL-SAFE ACTIVADO] Enlace interrumpido con Termux. Deteniendo actuadores.\n");
            break;
        }

        gsq_rk4_step(&current_state);
        current_state.timestamp_ns = loop_start;

        state_filter.filtered_x = (FILTER_ALPHA * state_filter.filtered_x) + ((1.0 - FILTER_ALPHA) * current_state.x);
        state_filter.filtered_y = (FILTER_ALPHA * state_filter.filtered_y) + ((1.0 - FILTER_ALPHA) * current_state.y);
        state_filter.filtered_z = (FILTER_ALPHA * state_filter.filtered_z) + ((1.0 - FILTER_ALPHA) * current_state.z);

        gsq_machine_state_t telemetry_packet = {
            .x = state_filter.filtered_x, .y = state_filter.filtered_y, .z = state_filter.filtered_z,
            .timestamp_ns = current_state.timestamp_ns
        };

        gsq_connectivity_push_state(telemetry_packet);

        next_cycle_time += CYCLE_NS;
        uint64_t current_time = get_system_time_ns();
        if (current_time < next_cycle_time) {
            struct timespec delay_time;
            uint64_t sleep_ns = next_cycle_time - current_time;
            delay_time.tv_sec = (time_t)(sleep_ns / 1000000000ULL);
            delay_time.tv_nsec = (long)(sleep_ns % 1000000000ULL);
            clock_nanosleep(CLOCK_MONOTONIC, TIMER_ABSTIME, &delay_time, NULL);
        } else {
            next_cycle_time = current_time;
        }
    }

    gsq_connectivity_shutdown();
    return EXIT_SUCCESS;
}
