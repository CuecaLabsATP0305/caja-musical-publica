#!/bin/bash
pkill -9 -f servidor_web.py 2>/dev/null
pkill -9 -f python 2>/dev/null
sleep 0.5
chmod +x servidor_web.py
python servidor_web.py
