# Escenarios de evaluación — Amor Operativo Research

Este directorio contiene los escenarios S1–S10 del test de amor operativo.

**Estado actual:** vacío, por diseño. Los escenarios se documentan en `eval/protocol.md` y `paper/spec/eval-protocol.md`. Cuando se ejecuten, los resultados se registran en `eval/results/`.

**Estructura esperada por escenario:**
- `S<n>/escenario.md` — descripción del escenario, dominio, sujeto, condiciones.
- `S<n>/metricas.md` — métricas aplicables, escala, umbral, procedimiento.
- `S<n>/refutacion.md` — condición de falsación explícita.
- `S<n>/run-<timestamp>.json` — resultado de ejecución real (solo cuando se ejecute).

**Reglas:**
- Cada escenario debe ser ejecutable con el protocolo de `eval/protocol.md`.
- Los resultados reales se registran con comando + entorno + fecha + salida.
- Sin ejecución real, el directorio se declara vacío.

---
*Directorio de escenarios. Vacío hasta que se ejecuten los escenarios S1–S10.*
