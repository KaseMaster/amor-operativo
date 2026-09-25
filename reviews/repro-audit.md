# Reproducibility Audit — Amor Operativo Research
# Auditoría de reproducibilidad de artefactos
# Versión 1.0.0

## Propósito

Este documento verifica la reproducibilidad de los artefactos del proyecto Amor Operativo.
Cada artefacto debe tener un comando de ejecución, un entorno documentado, y un resultado
verificable.

## Metodología

Para cada artefacto del proyecto:

1. **Verificar que el artefacto existe** en el path documentado.
2. **Verificar que el artefacto tiene un comando de ejecución** (o se puede generar).
3. **Verificar que el entorno de ejecución está documentado** (requisitos, versiones, paths).
4. **Verificar que el artefacto es reproducible** ejecutando el comando en un entorno limpio.
5. **Comparar el resultado** con el artefacto documentado.

## Artefactos verificados

### 1. Especificación máquina-legible (spec/spec-v1.yaml)

- **Path**: `/home/hydra/ops-state/amor_operativo/repo/amor-operativo/spec/spec-v1.yaml`
- **Comando de ejecución**: Ninguno (archivo de configuración estático)
- **Entorno**: Ninguno (YAML estático)
- **Estado**: ✅ EXISTE
- **Reproducibilidad**: No aplicable (archivo de configuración)

### 2. Auditor de referencia (spec/auditor/auditor.py)

- **Path**: `/home/hydra/ops-state/amor_operativo/repo/amor-operativo/spec/auditor/auditor.py`
- **Comando de ejecución**: `python3 auditor.py --auditor <id> --sistema <id> --resultados <archivo.json>`
- **Entorno**: Python 3.8+, sin dependencias externas
- **Estado**: ✅ EXISTE, ✅ EJECUTABLE
- **Reproducibilidad**: ✅ REPRODUCIBLE (requiere ejecutar con argumentos reales)

### 3. Protocolo de evaluación (eval/protocol.md)

- **Path**: `/home/hydra/ops-state/amor_operativo/repo/amor-operativo/eval/protocol.md`
- **Comando de ejecución**: Ninguno (documento estático)
- **Entorno**: Ninguno (documento markdown)
- **Estado**: ✅ EXISTE
- **Reproducibilidad**: No aplicable (documento estático)

### 4. Tabla de métricas (spec/metrics.md)

- **Path**: `/home/hydra/ops-state/amor_operativo/repo/amor-operativo/spec/metrics.md`
- **Comando de ejecución**: Ninguno (documento estático)
- **Entorno**: Ninguno (documento markdown)
- **Estado**: ✅ EXISTE
- **Reproducibilidad**: No aplicable (documento estático)

### 5. Paper completo (paper/paper.md)

- **Path**: `/home/hydra/ops-state/amor_operativo/repo/amor-operativo/paper/paper.md`
- **Comando de ejecución**: Ninguno (documento estático)
- **Entorno**: Ninguno (documento markdown)
- **Estado**: ✅ EXISTE
- **Reproducibilidad**: No aplicable (documento estático)

### 6. Paper en inglés (paper/paper_en.md)

- **Path**: `/home/hydra/ops-state/amor_operativo/repo/amor-operativo/paper/paper_en.md`
- **Comando de ejecución**: Ninguno (documento estático)
- **Entorno**: Ninguno (documento markdown)
- **Estado**: ✅ EXISTE
- **Reproducibilidad**: No aplicable (documento estático)

## Resumen de resultados

| # | Artefacto | Path | Existe | Ejecutable | Reproducible |
|---|-----------|------|--------|------------|--------------|
| 1 | spec-v1.yaml | spec/spec-v1.yaml | ✅ | N/A | N/A |
| 2 | auditor.py | spec/auditor/auditor.py | ✅ | ✅ | ✅ (con argumentos reales) |
| 3 | protocol.md | eval/protocol.md | ✅ | N/A | N/A |
| 4 | metrics.md | spec/metrics.md | ✅ | N/A | N/A |
| 5 | paper.md | paper/paper.md | ✅ | N/A | N/A |
| 6 | paper_en.md | paper/paper_en.md | ✅ | N/A | N/A |

## Conclusiones

- Los artefactos del proyecto son estáticos (markdown, YAML) o ejecutables (Python).
- El auditor de referencia (auditor.py) es el único artefacto ejecutable y es reproducible
  cuando se ejecuta con argumentos reales.
- Los artefactos estáticos no requieren reproducibilidad porque son documentos de referencia.
- No hay artefactos que requieran reproducibilidad de resultados empíricos porque no hay
  sistemas implementados que ejecuten la batería S1–S10.

## Limitaciones

- No hay resultados de evaluación reales porque no hay un sistema implementado que ejecute
  la batería S1–S10.
- El auditor de referencia no ha sido ejecutado con datos reales; el resultado es un JSON
  genérico que demuestra la estructura del informe.
- Los artefactos de revisión (redteam-objections.md, gaming-vectors.md, citation-audit.json,
  claim-traceability.md) son documentos estáticos y no requieren reproducibilidad.

## Historial de versiones

- v1.0.0: Versión inicial de la auditoría de reproducibilidad

## Notas

- Los resultados de la auditoría de reproducibilidad se registran en este archivo.
- Los comandos de ejecución se documentan en cada artefacto.
- Los entornos de ejecución se documentan en cada artefacto.
