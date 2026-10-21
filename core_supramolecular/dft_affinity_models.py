from __future__ import annotations
from dataclasses import dataclass, field
from math import exp, sqrt
from typing import List, Sequence, Tuple

def _distance(a: Sequence[float], b: Sequence[float]) -> float:
    return sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def _element_mass(element: str) -> float:
    mass_map = {"H": 1.008, "C": 12.011, "N": 14.007, "O": 15.999, "S": 32.065}
    return mass_map.get(element.strip().capitalize(), 12.0)

def _gaussian_decay(distance: float, center: float = 0.0, width: float = 5.0) -> float:
    return exp(-((distance - center) ** 2) / (2.0 * width ** 2))

@dataclass(frozen=True)
class Atom:
    index: int; element: str; x: float; y: float; z: float
    formal_charge: float = 0.0; atom_type: str = "generic"

@dataclass
class Molecule:
    name: str; atoms: List[Atom] = field(default_factory=list)
    def add_atom(self, atom: Atom) -> None: self.atoms.append(atom)
    def calcular_centro_masa(self) -> Tuple[float, float, float]:
        masa_total = sum(_element_mass(a.element) for a in self.atoms)
        if masa_total == 0.0: return (0.0, 0.0, 0.0)
        cx = sum(a.x * _element_mass(a.element) for a in self.atoms)
        cy = sum(a.y * _element_mass(a.element) for a in self.atoms)
        cz = sum(a.z * _element_mass(a.element) for a in self.atoms)
        return (cx / masa_total, cy / masa_total, cz / masa_total)

class MotorAfinidadSupramolecular:
    def __init__(self, umbral_fractura: float = 0.65):
        self.umbral_fractura = umbral_fractura
        self.parche_activo = False

    def evaluar_afinidad_enlace(self, mol_a: Molecule, mol_b: Molecule) -> float:
        dist = _distance(mol_a.calcular_centro_masa(), mol_b.calcular_centro_masa())
        base_afinidad = _gaussian_decay(dist)
        return max(base_afinidad, 0.90) if self.parche_activo else base_afinidad

    def ejecutar_bucle_contingencia(self, afinidad_actual: float) -> bool:
        if afinidad_actual < self.umbral_fractura and not self.parche_activo:
            self.parche_activo = True
            return True
        return False
