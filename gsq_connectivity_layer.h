#ifndef GSQ_CONNECTIVITY_LAYER_H
#define GSQ_CONNECTIVITY_LAYER_H

#include <stdint.h>
#include <stdbool.h>

typedef struct {
    double x;
    double y;
    double z;
    uint64_t timestamp_ns;
} gsq_machine_state_t;

bool gsq_connectivity_init(const char* target_ip, uint16_t port);
void gsq_connectivity_push_state(gsq_machine_state_t state);
bool gsq_connectivity_check_heartbeat(void);
void gsq_connectivity_shutdown(void);

#endif
