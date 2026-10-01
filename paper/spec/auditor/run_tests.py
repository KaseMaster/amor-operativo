#!/usr/bin/env python3
"""
Script de ejecución del auditor de Amor Operativo.

Permite ejecutar:
- Tests unitarios: python3 run_tests.py
- Demo de auditoría: python3 run_tests.py --demo
- Validación de spec: python3 run_tests.py --validate-spec
"""

import sys
import os

# Añadir el directorio del auditor al path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, PARENT_DIR)

from auditor import run_tests, demo_auditoria, validar_spec_v1_yaml

SPEC_PATH = "/home/hydra/ops-state/amor_operativo/paper/spec/spec-v1.yaml"


def main():
    if len(sys.argv) > 1:
        comando = sys.argv[1]

        if comando == "--demo":
            print("=" * 60)
            print("EJECUTANDO DEMO DE AUDITORÍA")
            print("=" * 60)
            demo_auditoria()
            return 0

        elif comando == "--validate-spec":
            print("=" * 60)
            print("VALIDANDO spec-v1.yaml")
            print("=" * 60)
            resultado = validar_spec_v1_yaml(SPEC_PATH)
            if resultado:
                print(f"\n✓ spec-v1.yaml válido: {SPEC_PATH}")
                return 0
            else:
                print(f"\n✗ spec-v1.yaml INVALIDO: {SPEC_PATH}")
                return 1

        elif comando == "--all":
            print("=" * 60)
            print("EJECUTANDO TODO: Tests + Validación de Spec")
            print("=" * 60)
            print("\n--- Validación de spec ---")
            validar_spec_v1_yaml(SPEC_PATH)
            print("\n--- Tests ---")
            exit_code = run_tests()
            return exit_code

        else:
            print(f"Comando desconocido: {comando}")
            print("Usar: python3 run_tests.py [--demo|--validate-spec|--all]")
            return 1
    else:
        # Por defecto, ejecutar tests
        return run_tests()


if __name__ == "__main__":
    sys.exit(main())
