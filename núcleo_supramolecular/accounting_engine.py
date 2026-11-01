#!/usr/bin/env python3
"""
MÓDULO DE DISPERSIÓN INTERNACIONAL DE COMISIONES - CUECALABS
Sistema automatizado de justicia económica y reparto de regalías.
Propiedad Exclusiva de CuecaLabs. Fines de prosperidad comercial.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List

@dataclass(frozen=True)
class TransaccionIngreso:
    id_transaccion: str
    origen_mercado: str       # Ej: "Google Play App", "SaaS Simulation", "B2B Royalty"
    monto_bruto_usd: float
    pais_origen: str
    fecha: datetime = field(default_factory=datetime.now)


class MotorComisionesInternacionales:
    def __init__(self, titular_exclusivo: str = "CuecaLabs"):
        self.titular = titular_exclusivo
        self.reglas_reparto = {
            "REGALIA_DIRECTA_AUTOR": 0.85,      # 85% directo al inventor
            "FONDO_AUTO_SUSTENTO_SISTEMA": 0.10, # 10% mantenimiento de servidores y APIs
            "RESERVA_JUSTICIA_SOCIEDAD": 0.05   # 5% fondo de reserva de control ético
        }
        self.historial_pagos: List[Dict] = []

    def procesar_recaudo_global(self, transaccion: TransaccionIngreso) -> Dict[str, float]:
        bruto = transaccion.monto_bruto_usd
        liquidacion = {
            "id_transaccion": transaccion.id_transaccion,
            "origen": transaccion.origen_mercado,
            "monto_total_recibido": bruto,
            "pago_exclusivo_autor_usd": bruto * self.reglas_reparto["REGALIA_DIRECTA_AUTOR"],
            "mantenimiento_infraestructura_usd": bruto * self.reglas_reparto["FONDO_AUTO_SUSTENTO_SISTEMA"],
            "reserva_etica_usd": bruto * self.reglas_reparto["RESERVA_JUSTICIA_SOCIEDAD"]
        }
        self.historial_pagos.append(liquidacion)
        print(f"[CONTABILIDAD INTERNACIONAL] Transacción {transaccion.id_transaccion} procesada.")
        print(f" -> Giro inmediato enviado al Autor: ${liquidacion['pago_exclusivo_autor_usd']:,.2f} USD (85%)")
        return liquidacion
