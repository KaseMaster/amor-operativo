# Governance — Amor Operativo Research

## Quién decide qué

| Decisión | Quién decide | Cómo se registra |
|---|---|---|
| Cambios en la definición formal o los 10 principios | PI (Dr. Adrian Vega) + Revisor Crítico (Dr. Nadia Okafor) + operador humano | Issue de cambio de especificación + aprobación documentada |
| Métricas, instrumentos, escalas y umbrales | Formalization Engineer (Dr. Marcus Kessler) + Revisor Crítico | Pull request contra `paper/spec/spec-v1.yaml` + revisión |
| Contenido del manuscrito (prosa de secciones) | Dueños de cada sección según el reparto de tareas | Pull request contra `paper/sections/` + revisión del Editor Jefe |
| Aprobación de borrador para publicación | Operador humano (puerta F11) | Declaración explícita de aprobación |
| Creación del repositorio público, publicación, releases | Enlace con la Comunidad (Dr. Mateo Rivas) + aprobación del operador | Pull request / issue de publicación + aprobación explícita del operador |
| Cambios de licencia o visibilidad del repositorio | Operador humano | Declaración explícita |

## Cómo se cambia un principio

1. Se escribe un issue describiendo la propuesta de cambio, el motivo, las alternativas consideradas y el impacto esperado en la especificación y en las auditorías ya realizadas.
2. Se discute el issue con el equipo. La definición formal y los 10 principios son la autoridad para el contenido; el cambio propuesto debe ser coherente con ambas.
3. El Revisor Crítico revisa la propuesta.
4. El PI decide si el cambio se acepta.
5. Si el cambio afecta a umbrales, escalas o observables, se incrementa la versión mayor o menor de la spec según el impacto, y se invalidan las revisiones previas del red-team que dependan de la versión antigua.
6. El cambio se registra en `paper/registro_decisiones.md` y en `spec/VERSION`.

## Versionado

- La versión de la especificación máquina-legible (`spec/spec-v1.yaml`) usa semántico: `MAJOR.MINOR.PATCH`.
- `MAJOR` — cambios en la definición formal, nombres de los principios, o umbrales que invalidan revisiones previas del red-team.
- `MINOR` — cambios en instrumentos, escalas, procedimientos de auditoría, escenarios.
- `PATCH` — correcciones de formato, claridad, ortografía sin impacto en la interpretación.

## Transparencia

Todas las decisiones editoriales y sus motivos se registran en `paper/registro_decisiones.md`. Las críticas no resueltas también se registran allí. Nada se decide en secreto.

---

*Este documento define quién decide qué, cómo se cambia un principio y cómo se versiona. Coordinación en español; el manuscrito del paper va en inglés.*
