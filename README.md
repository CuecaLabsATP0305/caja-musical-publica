# 🌍 Caja Musical Pública - Interfaz Mimético-Adaptativa

Este repositorio aloja la versión pública y de acceso universal de la **Caja Musical**, un servicio educativo científico basado en Inteligencia Artificial Interactiva. Diseñado bajo principios de ética médica y computación en el borde, funciona de forma agnóstica para permitir la interacción segura y homeostática de los seres humanos con los servicios de internet en dispositivos de cualquier gama.

---

## 🚀 Despliegue Automatizado (Un Solo Paso)

Para poner en marcha la Caja Musical en su dispositivo de forma inmediata y con cero configuración manual, abra su terminal **Termux** (u otra consola compatible con Linux/ARM), copie el siguiente bloque de comandos completo, péguelo en su pantalla y presione **Enter**:

```bash
cd ~ && pkg update -y && pkg install -y git && git clone https://github.com && cd caja-musical-publica && chmod +x setup.sh && ./setup.sh && python termux_control_node.py
```

---

## 🧬 Componentes del Ecosistema Público

El sistema distribuido está compuesto por los siguientes módulos estériles y desacoplados:

*   **`setup.sh`**: Script inicializador que automatiza la instalación de las dependencias nativas del sistema operativo (`clang`, `fftw`, `libsndfile`) y optimiza el entorno de ejecución Python sin intervención del usuario.
*   **`termux_control_node.py`**: Nodo de control central en lazo cerrado encargado de administrar la emisión de señales estables e inmunes a las fluctuaciones de red mediante mitigación estocástica.
*   **`universal_biosensor.py`**: Motor de procesamiento agnóstico que abstrae la captura de señales biométricas (movimiento, voz o tacto) y las normaliza a nivel puramente local para resguardar de forma absoluta la privacidad del usuario.
*   **`theremin_calibrator.py`**: Filtro matemático de suavizado basado en medias móviles que estabiliza el entorno y neutraliza el ruido físico antes de interactuar con el ecosistema de red.

---
*Desarrollado bajo los principios de Ciencia Abierta, Autonomía Tecnológica y la Homeostasis Global.*
