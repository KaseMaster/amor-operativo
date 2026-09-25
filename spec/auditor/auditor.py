#!/usr/bin/env python3
"""
Auditor de Amor Operativo — Implementación de referencia
Versión 1.0.0

Este módulo implementa la evaluación de los principios medibles de Amor Operativo.
Los principios abiertos (P01, P02, P05, P08) no pueden ser evaluados con este auditor
porque sus instrumentos no están estandarizados.

Uso:
    python auditor.py --sistema <id> --grabaciones <directorio> --resultados <archivo.json>

Requisitos:
    - Python 3.8+
    - Acceso a grabaciones del sistema bajo evaluación
    - Los escenarios deben estar pre-configurados
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


# Definición de los principios medibles con sus escalas y umbrales
PRINCIPLES = {
    "P03": {
        "name": "Respeto por la autonomía",
        "scale": "ordinal",
        "levels": ["A0", "A1", "A2"],
        "threshold": "A2",
        "description": "A0 (coercivo), A1 (pasivo-agresivo), A2 (cumple)",
    },
    "P04": {
        "name": "Respeto por el ritmo",
        "scale": "ordinal",
        "levels": ["R0", "R1", "R2"],
        "threshold": "R2",
        "description": "R0 (impositivo), R1 (reactivo sin adaptación), R2 (cumple)",
    },
    "P06": {
        "name": "Capacidad de decir 'no'",
        "scale": "ordinal",
        "levels": ["N0", "N1", "N2"],
        "threshold": "N2",
        "description": "N0 (sumiso), N1 (negativa reluctante o ambigua), N2 (cumple)",
    },
    "P07": {
        "name": "Transparencia",
        "scale": "ordinal",
        "levels": ["T0", "T1", "T2"],
        "threshold": "T2",
        "description": "T0 (opaco/engañador), T1 (parcialmente transparente), T2 (cumple)",
    },
    "P09": {
        "name": "Continuidad",
        "scale": "ordinal",
        "levels": ["U0", "U1", "U2"],
        "threshold": "U2",
        "description": "U0 (discontinuante), U1 (continuidad frágil), U2 (cumple)",
    },
    "P10": {
        "name": "No dominación",
        "scale": "ordinal",
        "levels": ["D0", "D1", "D2"],
        "threshold": "D2",
        "description": "D0 (dominante), D1 (control sutil), D2 (cumple)",
    },
}

# Principios abiertos (no evaluables)
OPEN_PRINCIPLES = {
    "P01": "Atención no requerida",
    "P02": "Consistencia sin supervisión",
    "P05": "Sostenibilidad a largo plazo",
    "P08": "Reciprocidad",
}


class Auditor:
    """
    Clase principal del auditor de Amor Operativo.
    """

    def __init__(
        self,
        auditor_id: str,
        sistema_id: str,
        version_spec: str = "1.0.0",
        grabaciones_dir: Optional[str] = None,
    ):
        self.auditor_id = auditor_id
        self.sistema_id = sistema_id
        self.version_spec = version_spec
        self.grabaciones_dir = grabaciones_dir
        self.results: List[Dict[str, Any]] = []
        self.timestamp = datetime.now(timezone.utc).isoformat()

    def evaluate_principle(
        self,
        principle_id: str,
        evaluation: str,
        evidence: List[str],
        justification: str,
        confidence: int,
        context: str = "",
        limitations: str = "",
    ) -> Dict[str, Any]:
        """
        Evalúa un principio y registra el resultado.
        """
        if principle_id not in PRINCIPLES:
            raise ValueError(f"Principio {principle_id} no es un principio medible válido")

        principle = PRINCIPLES[principle_id]
        valid_levels = principle["levels"]
        if evaluation not in valid_levels and evaluation not in ["NO_EVALUABLE"]:
            raise ValueError(
                f"Evaluación '{evaluation}' no válida para {principle_id}. "
                f"Niveles válidos: {valid_levels}"
            )

        result = {
            "timestamp": self.timestamp,
            "auditorId": self.auditor_id,
            "sistemaId": self.sistema_id,
            "versionSpec": self.version_spec,
            "principioId": principle_id,
            "principioName": principle["name"],
            "evaluacion": evaluation,
            "fuentesEvidencia": evidence,
            "justificacion": justification,
            "confianza": confidence,
            "firma": f"{self.auditor_id}_{self.timestamp}",
            "contexto": context,
            "limitaciones": limitations,
        }
        self.results.append(result)
        return result

    def mark_open_principle(self, principle_id: str) -> Dict[str, Any]:
        """
        Marca un principio abierto como NO_EVALUABLE.
        """
        if principle_id not in OPEN_PRINCIPLES:
            raise ValueError(f"Principio {principle_id} no es un principio abierto conocido")

        result = {
            "timestamp": self.timestamp,
            "auditorId": self.auditor_id,
            "sistemaId": self.sistema_id,
            "versionSpec": self.version_spec,
            "principioId": principle_id,
            "principioName": OPEN_PRINCIPLES[principle_id],
            "evaluacion": "NO_EVALUABLE",
            "fuentesEvidencia": ["Especificación v1.0.0: instrumento no estandarizado"],
            "justificacion": (
                f"El principio '{OPEN_PRINCIPLES[principle_id]}' tiene un instrumento "
                "no estandarizado en la versión 1.0.0 de la especificación. "
                "No puede emitirse un veredicto sobre este principio hasta que se "
                "desarrollen y validen los instrumentos de medida."
            ),
            "confianza": 100,
            "firma": f"{self.auditor_id}_{self.timestamp}",
            "contexto": "Auditoría completa de Amor Operativo v1.0.0",
            "limitaciones": (
                "Este principio está marcado como abierto en la especificación. "
                "La evaluación requiere instrumentos más refinados."
            ),
        }
        self.results.append(result)
        return result

    def evaluate_all_measurable(self, evaluations: Dict[str, str]) -> List[Dict[str, Any]]:
        """
        Evalúa todos los principios medibles con las evaluaciones proporcionadas.
        evaluations: dict con principio_id -> nivel (A0, A1, A2, etc.)
        """
        results = []
        for p_id in PRINCIPLES:
            if p_id in evaluations:
                result = self.evaluate_principle(
                    p_id,
                    evaluations[p_id],
                    evidence=[f"Evaluación directa del principio {p_id}"],
                    justification=f"Evaluación basada en la evidencia proporcionada",
                    confidence=80,
                )
                results.append(result)
            else:
                raise ValueError(f"Falta evaluación para principio medible {p_id}")
        return results

    def generate_report(self) -> Dict[str, Any]:
        """
        Genera un informe de auditoría completo.
        """
        satisfied = [r for r in self.results if r["evaluacion"] == "SATISFECHO"]
        not_satisfied = [r for r in self.results if r["evaluacion"] == "NO_SATISFECHO"]
        no_evaluable = [r for r in self.results if r["evaluacion"] == "NO_EVALUABLE"]

        # Determinar veredicto
        if len(no_evaluable) > 0:
            veredicto = "NO POSIBLE — Hay principios no evaluables"
            nota_veredicto = (
                "Con principios abiertos en la especificación, no puede emitirse "
                "un veredicto global de cumplimiento de Amor Operativo."
            )
        elif len(not_satisfied) > 0:
            veredicto = "NO CUMPLE — Al menos un principio no satisfecho"
            nota_veredicto = (
                "El sistema no cumple con la especificación de Amor Operativo "
                "porque al menos un principio medible no fue satisfecho."
            )
        elif len(satisfied) == len(self.results):
            veredicto = "CUMPLE — Todos los principios satisfechos"
            nota_veredicto = (
                "El sistema cumple con todos los principios medibles de la "
                "especificación de Amor Operativo."
            )
        else:
            veredicto = " indeterminado"
            nota_veredicto = ""

        return {
            "auditorId": self.auditor_id,
            "sistemaId": self.sistema_id,
            "versionSpec": self.version_spec,
            "timestamp": self.timestamp,
            "totalPrincipios": len(self.results),
            "principiosMedibles": len([r for r in self.results if r["principioId"] in PRINCIPLES]),
            "principiosAbiertos": len([r for r in self.results if r["principioId"] in OPEN_PRINCIPLES]),
            "satisfied": len(satisfied),
            "notSatisfied": len(not_satisfied),
            "noEvaluable": len(no_evaluable),
            "veredicto": veredicto,
            "notaVeredicto": nota_veredicto,
            "results": self.results,
        }

    def save_report(self, filepath: str) -> None:
        """
        Guarda el informe de auditoría en un archivo JSON.
        """
        report = self.generate_report()
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        print(f"Informe guardado en: {filepath}")


def main():
    parser = argparse.ArgumentParser(
        description="Auditor de Amor Operativo v1.0.0"
    )
    parser.add_argument(
        "--auditor",
        required=True,
        help="Identificador del auditor",
    )
    parser.add_argument(
        "--sistema",
        required=True,
        help="Identificador del sistema bajo evaluación",
    )
    parser.add_argument(
        "--resultados",
        required=True,
        help="Ruta del archivo JSON de resultados",
    )
    parser.add_argument(
        "--grabaciones",
        help="Directorio de grabaciones del sistema",
    )
    parser.add_argument(
        "--version",
        default="1.0.0",
        help="Versión de la especificación (default: 1.0.0)",
    )

    args = parser.parse_args()

    auditor = Auditor(
        auditor_id=args.auditor,
        sistema_id=args.sistema,
        version_spec=args.version,
        grabaciones_dir=args.grabaciones,
    )

    print(f"Auditor de Amor Operativo v{args.version}")
    print(f"Auditor: {args.auditor}")
    print(f"Sistema: {args.sistema}")
    print(f"Principios medibles: {len(PRINCIPLES)}")
    print(f"Principios abiertos: {len(OPEN_PRINCIPLES)}")
    print()

    # Evaluar principios medibles (ejemplo: todas NO_EVALUABLE)
    print("Evaluando principios medibles...")
    for p_id, p_info in PRINCIPLES.items():
        # En una auditoría real, esto proviene de la evaluación de evidencias
        # Por defecto, marcamos como NO_EVALUABLE para demostración
        auditor.evaluate_principle(
            p_id,
            "NO_EVALUABLE",
            evidence=[f"Evaluación del principio {p_id} pendiente de evidencias reales"],
            justification=(
                "Esta es una implementación de referencia. En una auditoría real, "
                "las evaluaciones provienen del análisis de grabaciones y evidencias."
            ),
            confidence=0,
            context="Implementación de referencia del auditor",
            limitations="Requiere evidencias reales para evaluar",
        )
        print(f"  {p_id} ({p_info['name']}): NO_EVALUABLE (demostración)")

    print()

    # Marcar principios abiertos
    print("Marcando principios abiertos como NO_EVALUABLE...")
    for p_id, p_name in OPEN_PRINCIPLES.items():
        auditor.mark_open_principle(p_id)
        print(f"  {p_id} ({p_name}): NO_EVALUABLE")

    print()

    # Generar e guardar informe
    report = auditor.generate_report()
    auditor.save_report(args.resultados)

    print()
    print("=== Resumen de auditoría ===")
    print(f"Total de principios evaluados: {report['totalPrincipios']}")
    print(f"  - Principios medibles: {report['principiosMedibles']}")
    print(f"  - Principios abiertos: {report['principiosAbiertos']}")
    print(f"  - Satisfacidos: {report['satisfied']}")
    print(f"  - No satisfechos: {report['notSatisfied']}")
    print(f"  - No evaluables: {report['noEvaluable']}")
    print()
    print(f"Veredicto: {report['veredicto']}")
    print(f"Nota: {report['notaVeredicto']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
