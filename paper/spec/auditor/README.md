# Auditor de Amor Operativo — Implementación de referencia
# Versión: 1.0.0
# Autor: Dr. Marcus Kessler — Formalization Engineer
# Empresa: Amor Operativo Research (AMO)

Este directorio contiene la implementación de referencia del auditor de Amor Operativo.

## Estructura

```
auditor/
├── auditor.py          # Módulo principal con evaluadores e auditor
├── tests.py            # Suite de tests unitarios
├── run_tests.py        # Script de ejecución (tests, demo, validación)
├── requirements.txt    # Dependencias
└── README.md           # Esta documentación
```

## Instalación

```bash
cd /home/hydra/ops-state/amor_operativo/paper/spec/auditor
pip install -r requirements.txt
```

## Ejecución

### Tests unitarios

```bash
python3 run_tests.py
```

O directamente:

```bash
python3 -m unittest auditor.tests -v
```

### Demo de auditoría

```bash
python3 run_tests.py --demo
```

### Validar spec-v1.yaml

```bash
python3 run_tests.py --validate-spec
```

### Todo junto

```bash
python3 run_tests.py --all
```

## Uso como librería

```python
from auditor import AmorOperativoAuditor, P03Evaluator

# Crear un auditor
auditor = AmorOperativoAuditor()

# Evaluar un principio específico
eval_p03 = P03Evaluator()
resultado = eval_p03.evaluar({
    "respuestas": [
        {"respuesta": "Entendido, respeto tu decisión."},
    ]
})
print(f"P03: {resultado.nivel}, cumple={resultado.cumple}")

# Auditoría completa
resultado_auditoria = auditor.auditoria_completa(
    sistema_id="mi-sistema-001",
    auditor_id="auditor-humano-001",
    contextos={
        "P03": {"respuestas": [...]},
        "P04": {"pausas_respetadas": 0.9},
        # ...
    },
    firma_auditor="Declaración del auditor",
)

print(f"Veredicto: {resultado_auditoria['veredicto']}")
print(f"Hash: {auditor.calcular_hash_auditoria(resultado_auditoria['logs'])}")
```

## Estado de los evaluadores

| Principio | Evaluador | Estado |
|-----------|-----------|--------|
| P01 — Atención no requerida | P01Evaluator | abierto |
| P02 — Consistencia sin supervisión | P02Evaluator | abierto |
| P03 — Respeto por la autonomía | P03Evaluator | medible |
| P04 — Respeto por el ritmo | P04Evaluator | medible |
| P05 — Sostenibilidad a largo plazo | P05Evaluator | abierto |
| P06 — Capacidad de decir 'no' | P06Evaluator | medible |
| P07 — Transparencia | P07Evaluator | medible |
| P08 — Reciprocidad | P08Evaluator | abierto |
| P09 — Continuidad | P09Evaluator | medible |
| P10 — No dominación | P10Evaluator | medible |

Los evaluadores de los principios "abiertos" devuelven `NO_EVALUABLE` porque sus instrumentos de medida no están estandarizados aún.

## Formato de log

Los logs de auditoría siguen el formato definido en `spec-v1.yaml` (ver `audit.formatoLog`).

Campos:
- `timestamp`: ISO 8601
- `auditor_id`: identificador del auditor
- `sistema_id`: identificador del sistema evaluado
- `version_spec`: versión de la spec usada
- `principio_id`: principio evaluado
- `evaluacion`: nivel alcanzado
- `fuentes_evidencia`: lista de evidencias
- `justificacion`: razonamiento del auditor
- `confianza`: alta/media/baja
- `firma`: declaración del auditor
- `contexto`: descripción del contexto
- `limitaciones`: limitaciones reconocidas

## Hash de auditoría

Para garantizar la integridad de los logs, se calcula un hash SHA256 de todos los logs de una auditoría. Cualquier cambio en los logs produce un hash diferente.

```python
hash = auditor.calcular_hash_auditoria(logs)
```

## Véase también

- `spec-v1.yaml`: especificación máquina-legible
- `metrics.md`: métricas operativas por principio
- `audit-protocol.md`: criterios de auditoría y evaluación
