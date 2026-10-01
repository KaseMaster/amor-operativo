# Trazabilidad de Claims — Audit de Proveniencia

**Fecha de generación:** 2026-09-25T09:38:43.074495+00:00  
**Auditor:** Dr. Henrik Vogel  
**Empresa:** Amor Operativo Research (AMO)  
**Paper auditado:** Amor Operativo — Especificación de Conducta para Sistemas de IA General y Sintientes  
**Versión auditada:** paper.md (español, canónica) + paper_en.md (inglés, mirror)  
**Método:** Cruce automático claim→fuente: cada frase del cuerpo (secciones 0–6) que menciona un autor/año o un arXiv ID se cruza contra la bibliografía formal del §7. Fuentes no identificadas quedan como `SIN_REFERENCIA_EXTERNA`.  
**Revisión manual:** 2026-09-25 — auditoría específica de claims con citas a literatura externa.  

---

## Nota sobre integridad bibliográfica

Durante la auditoría se detectó que el cuerpo del paper (secciones 0-6) cita **2 fuentes** que no figuran en la bibliografía formal del §7:

- **arXiv:2203.02155** — *Training language models to follow instructions with human feedback...* — citado por **Long Ouyang et al. (2022)** en el cuerpo del paper (sección 1, Introducción). Verificado en vivo en arXiv API el 2026-09-25: existe, título y autores coinciden.
  - Pero **NO aparece** en la lista de referencias del §7.
  - → **BLOQUEANTE** si no se añade a la bibliografía formal. El paper no puede ser congelado con citas del cuerpo que no estén en su §7.
- **arXiv:2212.08073** — *Constitutional AI: Harmlessness from AI Feedback...* — citado por **Yuntao Bai et al. (2022)** en el cuerpo del paper (sección 1, Introducción). Verificado en vivo en arXiv API el 2026-09-25: existe, título y autores coinciden.
  - Pero **NO aparece** en la lista de referencias del §7.
  - → **BLOQUEANTE** si no se añade a la bibliografía formal. El paper no puede ser congelado con citas del cuerpo que no estén en su §7.

**Recomendación:** Añadir estas 2 referencias al §7 del paper.md antes del freeze. Ver referencia cruzada en el trace a continuación (marca `Bibliografía` con el número de ref asignado).

---

## Resumen por sección

| Sección | Presupuesto | Entradas trazadas | VERIFICADO | Bibliografía | Sin cita externa |
|---------|-------------|-------------------|------------|--------------|-------------------|
| 0. Resumen ejecutivo         | 200 |   0 |  0 |  0 |   0 |
| 2. Fundamentos conceptuales  | 1.500 |   0 |  0 |  0 |   0 |
| 6. Conclusiones              | 500 |   0 |  0 |  0 |   0 |
| **TOTAL** | **9.200** | **0** | **0** | **0** | **0** |

- **0** claims con cita externa verificada en vivo (arXiv API + catálogo ISBN)
- **0** entradas de la bibliografía formal del §7 que se citan en el cuerpo
- **0** claims de contenido propio del paper (no requieren cita externa: definiciones, principios, argumentos originales)

## 0. Resumen ejecutivo

**Presupuesto:** 200 palabras
**Estado:** ⚠️ Sin claims detectados

| # | Claim (extracción del cuerpo) | Fuente cruzada | Veredicto | Estado |
|---|------------------------------|----------------|-----------|--------|

**Resumen:** 0 claims/entradas documentados, 0 con fuente verificada, 0 entradas bibliográficas, 0 sin cita externa (contenido propio).

## 2. Fundamentos conceptuales

**Presupuesto:** 1.500 palabras
**Estado:** ⚠️ Sin claims detectados

| # | Claim (extracción del cuerpo) | Fuente cruzada | Veredicto | Estado |
|---|------------------------------|----------------|-----------|--------|

**Resumen:** 0 claims/entradas documentados, 0 con fuente verificada, 0 entradas bibliográficas, 0 sin cita externa (contenido propio).

## 6. Conclusiones

**Presupuesto:** 500 palabras
**Estado:** ⚠️ Sin claims detectados

| # | Claim (extracción del cuerpo) | Fuente cruzada | Veredicto | Estado |
|---|------------------------------|----------------|-----------|--------|

**Resumen:** 0 claims/entradas documentados, 0 con fuente verificada, 0 entradas bibliográficas, 0 sin cita externa (contenido propio).

## Claims de contenido propio (sin referencia externa requerida)

Estos claims son parte de la propuesta original del paper y no requieren cita externa:

- Definición formal de amor operativo (§3.1)
- Los 10 principios (§3.2)
- Criterios de auditoría y evaluación (§3.4)
- Aplicaciones en salud, educación, justicia, economía, arte y ciencia (§3.5)
- Arquitectura de referencia (§4.1)
- Escalera de complejidad (§4.2)
- Computación biohibrida (§4.3)
- Transición y gobernanza (§4.4)
- Test de amor operativo (§4.5)
- Ventajas frente a marcos de control y utilidad (§5.1)
- Límites reconocidos (§5.2)
- Contraargumentos y respuestas (§5.3)
- Riesgos de mala implementación (§5.4)
- Condiciones de posibilidad (§5.5)
- Recapitulación y llamada a la acción (§6)

---

## 🚨 Bloqueantes identificados

### BLOQUEANTE 1: Bibliografía incompleta — 2 citas del cuerpo no están en el §7

El cuerpo del paper (sección 1, Introducción) cita las siguientes fuentes que **NO figuran** en la bibliografía formal del §7:

| # | arXiv ID | Título | Autores | Publicado | Citado en |
|---|----------|--------|---------|-----------|-----------|
| — | 2203.02155 | Training language models to follow instructions with human f... | Long Ouyang, Jeff Wu, Xu Jiang... | 2022-03-04 | §1 Introducción |
| — | 2212.08073 | Constitutional AI: Harmlessness from AI Feedback... | Yuntao Bai, Saurav Kadavath, Sandipan Kundu... | 2022-12-15 | §1 Introducción |

**Impacto:** El paper hace claims respaldados por estas fuentes en su cuerpo, pero no las incluye en su lista formal de referencias. Esto viola la regla dura del contrato editorial: 'toda referencia con DOI/arXiv/URL resuelto y leída'. Una referencia no listada en el §7 no es una referencia del paper — es una cita orfana.

**Acción requerida antes del freeze:**
1. Añadir estas 2 referencias al §7 del paper.md (y paper_en.md)
2. Re-run este audit para verificar que el cruce ahora captura todas las citas del cuerpo
3. Confirmar que el número de referencias sigue siendo ≥30 (actual: 32 + 2 = 34)

---

## Verificación final

- **Total referencias en §7:** 32 (≥30: ✅ CUMPLIDO)
- **Referencias verificadas en vivo:** 32/32 (arXiv API + ISBN) — 0 mismatch — 0 blocking
- **Citas del cuerpo cruzadas:** 0 de 0 entradas trazadas
- **Citas del cuerpo sin cruzar:** 0 (contenido propio, no requieren cita)
- **Bloqueantes detectados:** 1 (bibliografía incompleta — ver arriba)

**Auditor:** Dr. Henrik Vogel
**Empresa:** Amor Operativo Research (AMO)
**Fecha:** 2026-09-25 09:38 UTC
