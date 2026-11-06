import json
import time
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

SHARED_BRAIN_MATRIX = {
    "software_version": 3.0516,
    "constructor": "Freddy Arce (Calibrador Humano)",
    "layer_status": "INTERDEPENDIENTE_FRACTAL_PLANETARIO"
}

class CuecaLabsHTTPHandler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        return

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/brain":
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps(SHARED_BRAIN_MATRIX).encode("utf-8"))
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        self.end_headers()
        
        if os.path.exists("index.html"):
            with open("index.html", "r", encoding="utf-8") as f:
                self.wfile.write(f.read().encode("utf-8"))
        else:
            self.wfile.write(b"Error: index.html missing.")

if __name__ == "__main__":
    print("=========================================================================")
    print(" 🌍 CUECALABS - NÚCLEO INERCIAL PLANETARIO CONSOLIDADO ACTIVO V6")
    print("=========================================================================")
    try:
        HTTPServer(("", 8080), CuecaLabsHTTPHandler).serve_forever()
    except KeyboardInterrupt:
        print("\nDesacoplando nodo de red de forma segura...")
