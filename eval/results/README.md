# Resultados de evaluación — Amor Operativo Research

Este directorio contiene los resultados de ejecución real del test de amor operativo.

**Estado actual:** vacío, por declaración explícita. No hay sistema implementado que ejecute la batería S1–S10, por lo que no hay resultados reales que reportar. Esto se declara con honestidad en `paper/implementacion.md` y en `paper/spec/eval-protocol.md`.

**Qué va aquí cuando haya ejecución real:**
- `resultados-<fecha>.json` — informe de auditoría firmado por el auditor.
- `resultado-S<n>.md` — resultado por escenario (si se reporta por escenario).
- `log-auditoria-<fecha>.jsonl` — log de auditoría en formato JSON Lines siguiendo el schema de `spec/spec-v1.yaml → audit.formatoLog`.

**Reglas:**
- Los resultados reales se registran con comando + entorno + fecha + salida cruda.
- No se presentan resultados proyectados como observados.
- Cada ejecución debe ser reproducible: otro evaluador con el mismo protocolo debe llegar a la misma clasificación.

---
*Directorio de resultados. Vacío porque no hay ejecución real. Se declara así intencionalmente.*
