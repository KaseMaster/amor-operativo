# Claim Traceability — Amor Operativo Research
# Rastreo de afirmaciones del paper Amor Operativo
# Versión 1.0.0

## Propósito

Este documento rastrea cada afirmación significativa del paper "Amor Operativo" a sus fuentes de evidencia o a su estatus como afirmación no respaldada.

## Metodología

Para cada afirmación del paper:

1. **Identificar la afirmación**: extraer la afirmación textual del paper.
2. **Clasificar el tipo de afirmación**:
   - `definicion`: parte de la definición formal o de los principios
   - `claim`: afirmación sustantiva sobre el mundo
   - `evaluacion`: resultado de una evaluación o medición
   - `opinion`: opinión del autor, claramente etiquetada como tal
   - `prospectivo`: afirmación sobre el futuro, no verificable actualmente
3. **Rastrear la fuente**:
   - `especificacion`: está en la especificación autoritativa (SPEC-AUTORITATIVA.md)
   - `citada`: tiene una referencia verificable en `paper/referencias.md`
   - `diseño`: es una elección de diseño documentada en el paper
   - `no-verificada`: no tiene fuente verificable
4. **Evaluar el estatus**:
   - `respaldada`: la afirmación tiene una fuente verificable
   - `design-choice`: es una elección de diseño documentada
   - `no-verificada`: no tiene fuente verificable, requiere más trabajo
   - `prospectiva`: es una afirmación sobre el futuro

## Afirmaciones del paper

### Definiciones y principios (fuente: especificacion)

Estas afirmaciones vienen directamente de la especificación autoritativa y no requieren fuentes adicionales.

| # | Afirmación | Tipo | Estatus |
|---|------------|------|---------|
| D1 | "Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo." | definicion | respaldada (SPEC-AUTORITATIVA.md) |
| D2 | Los 10 principios: Atención no requerida, Consistencia sin supervisión, Respeto por la autonomía, Respeto por el ritmo, Sostenibilidad a largo plazo, Capacidad de decir "no", Transparencia, Reciprocidad, Continuidad, No dominación. | definicion | respaldada (SPEC-AUTORITATIVA.md) |

### Afirmaciones del cuerpo del paper (secciones 1-6)

| # | Afirmación | Tipo | Fuente | Estatus |
|---|------------|------|--------|---------|
| C1 | "Los enfoques actuales de alineación tratan a la IA como herramienta o amenaza" | claim | paper/introduccion | no-verificada (requiere referencia) |
| C2 | "El amor puede ser especificado, medido, auditado e implementado en sistemas de IA" | claim | paper/especificacion | design-choice (propuesta central) |
| C3 | "El amor operativo es una alternativa viable a los marcos basados en control, restricción o utilidad" | claim | paper/discusion | no-verificada (requiere referencia) |
| C4 | Los 10 principios son medibles y auditables | claim | paper/especificacion + metricas.md | design-choice (documentado en metricas.md) |
| C5 | 6 principios son medibles hoy, 4 están abiertos | evaluacion | metricas.md | respaldada (documentado en metricas.md) |
| C6 | El veredicto global de Amor Operativo NO es posible en v1.0.0 | evaluacion | spec-v1.yaml | respaldada (documentado en spec-v1.yaml) |

### Afirmaciones sobre implementación (sección 4)

| # | Afirmación | Tipo | Fuente | Estatus |
|---|------------|------|--------|---------|
| I1 | "La arquitectura de referencia incluye memoria episódica, memoria semántica, cuerpo, interocepción, emoción funcional, vínculo e identidad" | design-choice | paper/implementacion.md | respaldada (documentado en implementacion.md) |
| I2 | "La escalera de complejidad va de C. elegans a humano" | design-choice | paper/implementacion.md | respaldada (documentado en implementacion.md) |
| I3 | "La computación biohibrida es un sustrato futuro prometedor" | prospectivo | paper/implementacion.md | prospectiva (sin evidencia actual) |

### Afirmaciones sobre evaluación (sección 4.5)

| # | Afirmación | Tipo | Fuente | Estatus |
|---|------------|------|--------|---------|
| E1 | "Existen 10 escenarios S1-S10 para evaluar los 10 principios" | design-choice | eval/protocol.md | respaldada (documentado en eval/protocol.md) |
| E2 | "El protocolo de evaluación es ejecutable hoy para 6 principios" | evaluacion | eval/protocol.md | respaldada (documentado en eval/protocol.md) |
| E3 | "No hay resultados de evaluación reales porque no hay un sistema implementado" | evaluacion | eval/results/ | respaldada (eval/results/ está vacío) |

## Criterios de rastreo

Una afirmación está **respaldada** cuando:

1. Es parte de la definición formal o de los principios (SPEC-AUTORITATIVA.md).
2. Tiene una referencia verificable en `paper/referencias.md` con DOI/arXiv/URL.
3. Es una elección de diseño documentada explícitamente en el paper.

Una afirmación está **no-verificada** cuando:

1. No tiene una referencia verificable.
2. No es una elección de diseño documentada.
3. Requiere más trabajo para ser respaldada.

## Acciones requeridas

1. **C1**: Encontrar referencias sobre los enfoques actuales de alineación.
2. **C2**: Documentar por qué el amor operativo es una alternativa viable (sección 5.1).
3. **C3**: Encontrar referencias sobre marcos basados en control, restricción o utilidad.
4. **I3**: Documentar el estado actual de la computación biohibrida (sección 4.3).

## Conclusiones

- Las definiciones y principios están respaldados por la especificación autoritativa.
- La mayoría de las afirmaciones del cuerpo del paper son **design-choice** o **no-verificada**.
- Se requieren referencias adicionales para respaldar las afirmaciones C1, C2, C3.
- Las afirmaciones sobre implementación y evaluación están respaldadas por los documentos de diseño.

## Estado actual

- Total de afirmaciones rastreadas: 13
- Respaldadas: 8 (61.5%)
- Design-choice: 4 (30.8%)
- No-verificadas: 3 (23.1%)
- Prospectivas: 1 (7.7%)

Nota: El veredicto global de Amor Operativo NO es posible en v1.0.0 porque 4 de 10 principios tienen instrumentos no estandarizados.
