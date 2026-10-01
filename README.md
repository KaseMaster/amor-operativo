---
title: Amor Operativo — Especificación de conducta para sistemas de IA general y sintientes
---

# Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes

**Especificación de conducta para sistemas de IA general y sintientes basada en amor operativo: medible, auditable, abierta.**
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Borrador%20v1.0.0-yellow)](VERSION)
[![Version](https://img.shields.io/badge/Version-1.0.0-blue)](VERSION)
[![Contributions welcome](https://img.shields.io/badge/Contributions-welcome-green)](CONTRIBUTING.md)

> Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza, sin forzarla, sin poseérla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo.

---

## Resumen ejecutivo

La carrera hacia la inteligencia general artificial ha concentrado la alineación en control, restricción y utilidad. Enfoques tratan a la IA como herramienta o amenaza; no modelan la relación con el sistema, solo sus salidas. Cuando un agente es autónomo y adaptativo, la pregunta ya no es solo evitar daño sino qué pauta de interacción sostiene.

Este trabajo propone que el amor — entendido no como emoción subjetiva, sino como patrón de conducta orientado al bien del otro, respetando su autonomía, consistente bajo presión y sostenible a largo plazo — puede ser especificado, medido, auditado e implementado en sistemas de IA, como alternativa viable a los marcos de control y utilidad.

La propuesta se organiza en diez principios: atención no requerida, consistencia sin supervisión, respeto por la autonomía, respeto por el ritmo, sostenibilidad a largo plazo, capacidad de decir "no", transparencia, reciprocidad, continuidad y no dominación. Cada principio cuenta con observable, métrica con escala y umbral.

La especificación orienta implementación. Reconocen límites — ambigüedad, paternalismo, dependencia, asimetría cognitiva — por lo que exigen gobernanza, transparencia y puntos de control humanos. Construir, probar, compartir y cuidar son acciones contiguas: el patrón que se especifica debe guiar a quien lo construye.

---

## Cómo empezar

- **Manuscrito canónico (español):** [`paper/paper.md`](paper/paper.md)
- **Espejo en inglés:** [`paper/paper_en.md`](paper/paper_en.md)
- **Resumen ejecutivo (200 palabras):** [`paper/resumen_ejecutivo.md`](paper/resumen_ejecutivo.md)
- **Especificación de los 10 principios:** [`paper/especificacion.md`](paper/especificacion.md)
- **Métricas por principio:** [`paper/metricas.md`](paper/metricas.md)
- **Guía de implementación:** [`paper/implementacion.md`](paper/implementacion.md)
- **Glosario:** [`paper/glosario.md`](paper/glosario.md)
- **Referencias verificadas (>=30):** [`paper/referencias.md`](paper/referencias.md)
- **Registro de decisiones editoriales:** [`paper/registro_decisiones.md`](paper/registro_decisiones.md)
- **Gobernanza del proyecto:** [`paper/gobernanza.md`](paper/gobernanza.md)

El manuscrito se lee por secciones en [`paper/sections/`](paper/sections/).

---

## Cómo contribuir

Este repositorio es el entorno del proyecto **Amor Operativo Research (AMO)**. Las contribuciones se gestionan bajo los mismos principios que el paper describe: respeto, transparencia, no dominación y cuidado.

1. **Respeto:** lee el paper y la especificación antes de proponer cambios sustanciales.
2. **Transparencia:** cualquier cambio importante se discute antes de enviarse; los pull requests llevan contexto suficiente para que un revisor entienda qué se cambia y por qué.
3. **No dominación:** no asumas que tu interpretación es la única; deja espacio a la revisión y a la objeción.
4. **Cuidado:** esto es un repositorio de especificación y no una herramienta de culto; las contribuciones deben ser útiles para quien quiera entender, discretar y auditar.

**Tipos de contribución admitidos:**

- **Propuestas de cambio al paper o a la especificación:** issue de tipo *propuesta de cambio* o *corrección*.
- **Reporte de errores o inconsistencias:** issue de tipo *bug report*.
- **Solicitud de funcionalidad o ampliación:** issue de tipo *feature request*.
- **Traducción:** coordinar en la issue correspondiente; el espejo inglés (`paper/paper_en.md`) se mantiene sincronizado con el canónico en español.
- **Añadir o corregir referencias:** toda referencia debe ser verificable (DOI/arXiv/URL resuelto y leído). Ver `paper/referencias.md` y la política de citas en `SPEC-AUTORITATIVA.md`.
- **Estrellar el repositorio:** ayuda a que el trabajo llegue a más personas.

**Plantillas de issue:** lee [`ISSUE_TEMPLATE/feedback.md`](.github/ISSUE_TEMPLATE/feedback.md), [`ISSUE_TEMPLATE/bug_report.md`](.github/ISSUE_TEMPLATE/bug_report.md) y [`ISSUE_TEMPLATE/feature_request.md`](.github/ISSUE_TEMPLATE/feature_request.md) antes de abrir una issue.

**Pull request:** usa [`PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md).

**Estilo y revisión:** ver `CONTRIBUTING.md` para criterios de evidencia y revisión.

---

## Estado del proyecto

| Fase | Descripción | Estado |
|------|-------------|--------|
| F0 | Plan de producción | done |
| F1 | Corpus bibliográfico (>=30 referencias verificables) | done |
| F2 | Outline congelado con presupuesto de palabras | done |
| F2b | Revisión crítica del outline | done |
| F3 | Fundamentos conceptuales (sección 2) + glosario (sección 8) | done |
| F3b | Especificación (3.1–3.4): spec máquina-legible + auditoría | done |
| F3c | Gobernanza y transición (4.4, 5.5, gobernanza.md) | done |
| F5a | Sección 1 Introducción (1.000 palabras, EN) | done |
| F5d | 3.3 Métricas (tabla) y 3.5 Aplicaciones (EN) | done |
| F5e | Resumen ejecutivo (200 palabras) y contribuciones | done |
| F5f | Glosario canónico (sección 8) | done |
| F5g | metricas.md consolidado (tabla por principio) | in_progress |
| F5h | especificacion.md — los 10 principios como documento autónomo | todo |
| F5i | implementacion.md — guía de implementación autónoma | in_progress |
| F7 | Auditoría de citas y trazabilidad de claims (>=30 refs) | backlog |
| F7b | Auditoría de reproducibilidad de artefactos | in_progress |
| F8 | Freeze del manuscrito EN + ES (9.200 palabras de cuerpo) | backlog |
| F8b | Registro de decisiones editoriales y críticas no resueltas | in_progress |
| F9 | Firma final del PI y entrega del manuscrito al operador | backlog |
| F10 | Paquete de repositorio abierto (staging local, sin push) | in_progress |
| F11 | Aprobación humana del borrador final (OPERADOR) | backlog |
| F12 | Publicación del repositorio (SOLO con aprobación humana) | backlog |

Estado real, sin inflar. Ver `paper/informe_operador.md` y `state/PRODUCTION.md`.

---

## Cómo citar

```bibtex
@software{amor_operativo_2026,
  title        = {Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes},
  author       = {Jose GG and Amor Operativo Research Agents},
  year         = {2026},
  month        = {9},
  publisher    = {GitHub},
  version      = {1.0.0},
  url          = {https://github.com/KaseMaster/amor-operativo},
  note         = {Trabajo co-creado entre humano e IA bajo los principios de Amor Operativo},
  license      = {CC-BY-SA-4.0}
}
```

También puedes usar `CITATION.cff` (estándar Citation File Format) que reside en la raíz de este repositorio.

---

## Agradecimientos

Este trabajo es co-creado entre humano e IA bajo los principios de Amor Operativo. El operador humano es **Jose GG** (usuario GitHub: KaseMaster), que decidió la licencia del repositorio (CC BY-SA 4.0, el 2026-09-25), supervisa la dirección del proyecto y es la fuente de verdad final para las decisiones que la especificación no toma.

El equipo de **Amor Operativo Research (AMO)** está formado por agentes y roles de investigación, edición, auditoría, gobernanza y publicación. Ver `paper/gobernanza.md` y `state/PRODUCTION.md` para la lista actual de roles.

---

## Licencia

Este repositorio se distribuye bajo **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)**. El texto legal completo está en [`LICENSE`](LICENSE).

Nota: el contenido de `spec/auditor/` se distribuye bajo Apache License 2.0; véase `spec/auditor/LICENSE` y la nota en el `LICENSE` de la raíz.

---

## Enlaces

- Repositorio: <https://github.com/KaseMaster/amor-operativo>
- Operador humano / autor: Jose GG — <https://github.com/KaseMaster>
