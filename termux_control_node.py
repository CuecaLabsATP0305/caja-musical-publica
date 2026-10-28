#!/usr/bin/env python3
import socket
import struct
import time
import sys
import signal

CORE_IP = "127.0.0.1"  
CORE_PORT = 8080
TELEMETRY_FORMAT = "<dddQ"
PACKET_SIZE = struct.calcsize(TELEMETRY_FORMAT)
running = True

def sigint_handler(sig, frame):
    global running
    print("\n[TERMUX] Interrupción manual recibida. Cerrando enlace de control...")
    running = False

signal.signal(signal.SIGINT, sigint_handler)

def run_supervisor():
    global running
    print(f"[TERMUX] Inicializando Supervisor en Puerto {CORE_PORT}...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setblocking(False)
    server_address = (CORE_IP, CORE_PORT)
    last_heartbeat_time = 0
    heartbeat_interval = 0.1
    print("[TERMUX] Enlace establecido. Enviando secuencias de Heartbeat...")
    
    try:
        while running:
            current_time = time.time()
            if current_time - last_heartbeat_time >= heartbeat_interval:
                try:
                    sock.sendto(b"HEARTBEAT", server_address)
                    last_heartbeat_time = current_time
                except Exception as e:
                    print(f"[ERROR DE ENLACE] No se pudo enviar el pulso: {e}", file=sys.stderr)
            try:
                data, _ = sock.recvfrom(512)
                if len(data) == PACKET_SIZE:
                    x, y, z, ts = struct.unpack(TELEMETRY_FORMAT, data)
                    sys.stdout.write(f"\r[TELEMETRÍA] TS: {ts} | X: {x:8.4f} | Y: {y:8.4f} | Z: {z:8.4f}")
                    sys.stdout.flush()
            except BlockingIOError:
                pass
            except Exception as e:
                print(f"\n[ERROR DE LECTURA] Corrupción de trama: {e}", file=sys.stderr)
            time.sleep(0.001)
    finally:
        sock.close()
        print("\n[TERMUX] Enlace desconectado de forma segura. Sistema de producción en Fail-Safe.")

if __name__ == "__main__":
    run_supervisor()
