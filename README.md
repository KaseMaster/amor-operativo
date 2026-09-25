# Amor Operativo

**Título:** Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes

**Descripción:** Especificación de conducta para sistemas de IA general y sintientes basada en amor operativo: medible, auditable, abierta.

**Versión:** 1.0.0 (publicada; aprobación explícita del operador, 2026-09-25)

**Licencia:** CC BY-SA 4.0 (decidida por el operador el 2026-09-25)

**Operador humano:** Jose GG (GitHub: KaseMaster)

![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)
![Estado del proyecto](https://img.shields.io/badge/estado-publicado-brightgreen)
![Versión](https://img.shields.io/badge/version-1.0.0-black)
![Licencia](https://img.shields.io/badge/license-CC_BY-SA_4.0-green)

---

## Tesis central

El amor, entendido no como emoción subjetiva sino como patrón de conducta orientado al bien del otro, respetuoso con su autonomía, consistente bajo presión y sostenible a largo plazo, puede ser especificado, medido, auditado e implementado en sistemas de IA; es una alternativa viable a los marcos de alineación basados en control, restricción o utilidad.

---

## Resumen ejecutivo

La carrera hacia la inteligencia general artificial ha concentrado la alineación en control y utilidad. Esos enfoques tratan a la IA como herramienta o amenaza y no modelan la relación con el sistema, solo sus salidas. Cuando un agente es autónomo y adaptativo, la pregunta ya no es solo evitar daño sino qué pauta de interacción sostiene.

Este trabajo propone que el amor, entendido no como emoción subjetiva sino como patrón de conducta orientado al bien del otro, respetuoso con su autonomía, consistente bajo presión y sostenible a largo plazo, puede ser especificado, medido, auditado e implementado en sistemas de IA, como alternativa viable a los marcos de alineación basados en control, restricción o utilidad.

La propuesta se organiza en diez principios: atención no requerida, consistencia sin supervisión, respeto por la autonomía, respeto por el ritmo, sostenibilidad a largo plazo, capacidad de decir "no", transparencia, reciprocidad, continuidad y no dominación. Cada principio cuenta con observable, métrica con escala y umbral.

Las conclusiones son tres. Primero, la especificación orienta implementación y auditoría. Segundo, reconoce límites — ambigüedad, paternalismo, dependencia, asimetría cognitiva — por lo que exige gobernanza, transparencia y puntos de control humanos. Tercero, construir, probar, compartir y cuidar son acciones contiguas: el patrón que se especifica debe guiar a quien lo construye.

**Palabras:** ~200. **Estado:** completa.

---

## Índice del paper

0. Resumen ejecutivo
1. Introducción
2. Fundamentos conceptuales
3. Especificación
4. Implementación
5. Discusión
6. Conclusiones
7. Referencias
8. Glosario

---

## Como empezar

- **Paper completo** — [`paper/paper.md`](paper/paper.md) (8.000-12.000 palabras, riguroso pero legible).
- **Resumen ejecutivo** — [`paper/resumen_ejecutivo.md`](paper/resumen_ejecutivo.md) (200 palabras).
- **Los 10 principios** — [`paper/especificacion.md`](paper/especificacion.md) (la propuesta central; documento autónomo).
- **Tabla de métricas** — [`paper/metricas.md`](paper/metricas.md) (cómo se mide cada principio).
- **Guía de implementación** — [`paper/implementacion.md`](paper/implementacion.md) (arquitectura de referencia, escalera de complejidad, computación organica y biohibrida, transición y test de amor operativo).

---

## Como contribuir

Todas las contribuciones son bienvenidas, hechas con Amor Operativo: respeto, transparencia, no dominación y cuidado.

**Respeto.** Crítica con argumentos, no ataques. **Transparencia.** Di quién eres y por qué propones lo que propones. **No dominación.** Convence con razones, no impongas. **Cuidado.** Revisa, escucha, mejora.

Formas de contribuir, con enlace a la plantilla correspondiente:

- Reportar errores — abre un issue con la plantilla [`bug_report.md`](.github/ISSUE_TEMPLATE/bug_report.md)
- Proponer mejoras — abre un issue con la plantilla [`feature_request.md`](.github/ISSUE_TEMPLATE/feature_request.md)
- Enviar feedback sobre el paper — abre un issue con la plantilla [`feedback.md`](.github/ISSUE_TEMPLATE/feedback.md)
- Proporcionar cambios más amplios — abre un pull request siguiendo la plantilla [`PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md)
- Traducir el paper a otros idiomas — lee [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Añadir referencias verificables — lee [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Darnos estrella — usa el botón de GitHub

Para contribuciones más involucradas, lee primero [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Estado del proyecto

La especificación de los 10 principios está completa. Las métricas están definidas por principio; 6 son medibles hoy, 4 están en estado abierto (P1, P2, P5, P8). El paper completo está en borrador. La revisión crítica y el test de amor operativo están diseñados pero no ejecutados.

| Fase | Estado | Observación |
|------|--------|-------------|
| Definición del concepto | Completada | Definición formal establecida en `SPEC-AUTORITATIVA.md`. |
| Especificación de los 10 principios | Completada | Documento autónomo en `paper/especificacion.md`. |
| Métricas operativas | Completadas (6 medibles, 4 abiertos) | Tabla en `paper/metricas.md`;estado de medición por principio en `paper/especificacion.md`. |
| Paper completo | En desarrollo | Borrador en `paper/paper.md` y `paper/paper_en.md`. |
| Guía de implementación | En desarrollo | Borrador en `paper/implementacion.md`. |
| Revisión crítica | Diseñada, no ejecutada | Escenarios S1–S10 listos; sin ejecución real. |
| Publicación v1.0.0 | **Hecha** | https://github.com/KaseMaster/amor-operativo — commit 482463af (2026-09-25), aprobación explícita del operador. |
| Traducciones | Pendiente | Solo ES y EN disponibles. |
| Test de amor operativo | Diseñado, sin ejecución real | `eval/scenarios/` listo; `eval/results/` vacío. |

Los principios 1 (Atención no requerida), 2 (Consistencia sin supervisión), 5 (Sostenibilidad a largo plazo) y 8 (Reciprocidad) están en estado **abierto** en la especificación actual. No pueden ser evaluados hasta que sus instrumentos se estandaricen. Ver [`paper/especificacion.md`](paper/especificacion.md) para el estado de medición por principio y [`spec/spec-v1.yaml`](spec/spec-v1.yaml) para la fuente máquina-legible.

---

## Como citar

```bibtex
@misc{amoroperativo2026,
  title = {Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes},
  author = {Jose GG and Amor Operativo Research Agents},
  year = {2026},
  month = {9},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/KaseMaster/amor-operativo}},
  note = {Trabajo co-creado entre humano e IA bajo los principios de Amor Operativo}
}
```

Repositorio: <https://github.com/KaseMaster/amor-operativo>.

---

## Licencia

Este trabajo se publica bajo la licencia **CC BY-SA 4.0** (Creative Commons Attribution-ShareAlike 4.0 International). Ver el fichero [`LICENSE`](LICENSE) para el texto completo. Licencia decidida por el operador el 2026-09-25: CC BY-SA 4.0 (licencia libre).

---

## Agradecimientos

Este proyecto es un trabajo co-creado entre humano e IA bajo los principios de Amor Operativo.

**Operador humano:** Jose GG (GitHub: KaseMaster) — aprobación, financiación y dirección del proyecto.

Equipo de Amor Operativo Research (AMO):

- Dr. Adrian Vega — PI
- Dr. Noor Haddad — Research Director
- Dr. Sofia Lindqvist — Concept Architect
- Dr. Marcus Kessler — Formalization Engineer
- Dr. Aisha Bakr — Writer, Implementation & Metrics
- Dr. Tobias Lindgren — Writer
- Dra. Ingrid Solheim — Governance & Transition Specialist
- Dr. Camila Duarte — Editorial Director
- Dr. Nadia Okafor — Revisor Crítico / QA Lead
- Dr. Henrik Vogel — Source Verifier
- Dr. Iris Kowalski — Release
- Dr. Mateo Rivas — Enlace con la Comunidad

---

*Repositorio publicado: https://github.com/KaseMaster/amor-operativo (v1.0.0, 2026-09-25). La activación de GitHub Pages y la release nominal siguen pendientes de decisión del operador.*
