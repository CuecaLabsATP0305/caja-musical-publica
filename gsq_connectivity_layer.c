#include "gsq_connectivity_layer.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <pthread.h>
#include <time.h>

#define RING_BUFFER_SIZE 256
#define MAX_HEARTBEAT_TIMEOUT_MS 500

static int server_socket = -1;
static gsq_machine_state_t ring_buffer[RING_BUFFER_SIZE];
static volatile uint32_t head = 0;
static volatile uint32_t tail = 0;

static pthread_t telemetry_thread;
static volatile bool running = false;
static volatile uint64_t last_termux_heartbeat = 0;

static uint64_t get_time_ns(void) {
    struct timespec ts;
    clock_gettime(CLOCK_MONOTONIC, &ts);
    return (uint64_t)ts.tv_sec * 1000000000ULL + ts.tv_nsec;
}

static void* telemetry_worker(void* arg) {
    (void)arg;
    struct sockaddr_in client_addr;
    socklen_t addr_len = sizeof(client_addr);
    char rx_buffer[32];

    while (running) {
        ssize_t rx_bytes = recvfrom(server_socket, rx_buffer, sizeof(rx_buffer) - 1, MSG_DONTWAIT, 
                                    (struct sockaddr*)&client_addr, &addr_len);
        if (rx_bytes > 0) {
            rx_buffer[rx_bytes] = '\0';
            if (strcmp(rx_buffer, "HEARTBEAT") == 0) {
                last_termux_heartbeat = get_time_ns();
            }
        }

        if (tail != head) {
            uint32_t next_tail = (tail + 1) % RING_BUFFER_SIZE;
            gsq_machine_state_t state_to_send = ring_buffer[tail];
            tail = next_tail;

            sendto(server_socket, &state_to_send, sizeof(gsq_machine_state_t), MSG_DONTWAIT, 
                   (struct sockaddr*)&client_addr, addr_len);
        }
        usleep(500);
    }
    return NULL;
}

bool gsq_connectivity_init(const char* target_ip, uint16_t port) {
    server_socket = socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP);
    if (server_socket < 0) return false;

    int flags = fcntl(server_socket, F_GETFL, 0);
    fcntl(server_socket, F_SETFL, flags | O_NONBLOCK);

    struct sockaddr_in server_addr;
    memset(&server_addr, 0, sizeof(server_addr));
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(port);
    server_addr.sin_addr.s_addr = inet_addr(target_ip);

    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        close(server_socket);
        return false;
    }

    running = true;
    last_termux_heartbeat = get_time_ns();
    pthread_create(&telemetry_thread, NULL, telemetry_worker, NULL);
    return true;
}

void gsq_connectivity_push_state(gsq_machine_state_t state) {
    uint32_t next_head = (head + 1) % RING_BUFFER_SIZE;
    if (next_head != tail) {
        ring_buffer[head] = state;
        head = next_head;
    }
}

bool gsq_connectivity_check_heartbeat(void) {
    uint64_t current_time = get_time_ns();
    uint64_t diff_ms = (current_time - last_termux_heartbeat) / 1000000ULL;
    if (diff_ms > MAX_HEARTBEAT_TIMEOUT_MS) {
        return false;
    }
    return true;
}

void gsq_connectivity_shutdown(void) {
    running = false;
    pthread_join(telemetry_thread, NULL);
    if (server_socket >= 0) {
        close(server_socket);
    }
}
