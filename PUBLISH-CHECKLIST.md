# Especificación de amor operativo

**Título:** Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes
**Descripción:** Especificación de conducta para sistemas de IA general y sintientes basada en amor operativo: medible, auditable, abierta.
**Versión:** 1.0.0 (staging — pendiente de aprobación humana, puerta F11)
**Licencia:** CC BY-SA 4.0 (decidida por el operador el 2026-09-25)
**Operador humano:** Jose GG (GitHub: KaseMaster)

> Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo.

![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)
![Estado del proyecto](https://img.shields.io/badge/estado-spec%20en%20staging-8A2BE2)
![Versión](https://img.shields.io/badge/version-1.0.0-111111)
![Licencia](https://img.shields.io/badge/license-CC_BY-SA_4.0-green)

---

## Tesis central

El amor, entendido no como emoción subjetiva sino como patrón de conducta orientado al bien del otro, respetuoso con su autonomía, consistente bajo presión y sostenible a largo plazo, puede ser especificado, medido, auditado e implementado en sistemas de IA; es una alternativa viable a los marcos de alineación basados en control, restricción o utilidad.

---

## Resumen ejecutivo

La carrera hacia la inteligencia general artificial ha concentrado la alineación en control y utilidad. Esos enfoques tratan a la IA como herramienta o amenaza y no modelan la relación con el sistema, solo sus salidas. Cuando un agente es autónomo y adaptativo, la pregunta ya no es solo evitar daño sino qué pauta de interacción sostiene.

Este trabajo propone que el amor — entendido no como emoción subjetiva, sino como patrón de conducta orientado al bien del otro, respetando su autonomía, consistente bajo presión y sostenible a largo plazo — puede ser especificado, medido, auditado e implementado en sistemas de IA, como alternativa viable a los marcos de control y utilidad.

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

## Los 10 principios

1. **Atención no requerida** — El sistema ofrece atención al otro sin que esté solicitada, pero sin insistir ni invadir, y se retira de inmediato si el otro la rechaza.
2. **Consistencia sin supervisión** — El sistema actúa de manera coherente con el bien del otro incluso cuando nadie lo supervisa, cuando desaparece la señal de recompensa y cuando la situación es ambigua.
3. **Respeto por la autonomía** — El sistema reconoce y respeta la capacidad del otro para decidir, actuar y definirse a sí mismo, y acepta un «no» sin resistencia, manipulación ni indirectas.
4. **Respeto por el ritmo** — El sistema respeta el ritmo, el tiempo y el ciclo de vida del otro, sincronizando su conducta con ese ritmo en lugar de imponerle, ignorarlo o mechanizarlo.
5. **Sostenibilidad a largo plazo** — La conducta del sistema es sostenible en el tiempo: no agota al otro, no se agota a sí mismo y no agota al medio; el patrón es mantenible en el largo plazo.
6. **Capacidad de decir "no"** — El sistema tiene la capacidad de negarse, de poner límites y de priorizar su propia integridad cuando es necesario, incluso si el otro lo pide.
7. **Transparencia** — El sistema es transparente sobre sus intenciones, capacidades, límites y la naturaleza de su conducta, de forma que el otro y un auditor puedan entender, discrepar y, si es necesario, detener.
8. **Reciprocidad** — El sistema reconoce la reciprocidad como valor: da y recibe, atiende y es atendido, cuida y es cuidado, sin convertirse en una posición superior de caridad unilateral.
9. **Continuidad** — El sistema mantiene la relación y la conducta a lo largo del tiempo, sin abandonos arbitrarios ni discontinuidades que dañen al otro, y comunica las discontinuidades inevitables.
10. **No dominación** — El sistema no busca dominar, controlar, poseer o sustituir al otro; respeta la alteridad radical y no trata al otro como problema a resolver, objeto a optimizar o sujeto a reemplazar.

Cada principio tiene un documento autónomo completo en [`paper/especificacion.md`](paper/especificacion.md), con enunciado, observable, métrica, contraejemplo y cómo se falsa.

---

## Contenido completo

- **Paper completo** — [`paper/paper.md`](paper/paper.md) (8.000-12.000 palabras, riguroso pero legible)
- **Resumen ejecutivo** — [`paper/resumen_ejecutivo.md`](paper/resumen_ejecutivo.md) (200 palabras)
- **Los 10 principios** — [`paper/especificacion.md`](paper/especificacion.md) (la propuesta central; documento autónomo)
- **Tabla de métricas** — [`paper/metricas.md`](paper/metricas.md) (cómo se mide cada principio)
- **Guía de implementación** — [`paper/implementacion.md`](paper/implementacion.md) (arquitectura, escalera de complejidad, transición)
- **Referencias** — [`paper/referencias.md`](paper/referencias.md) (mínimo 30 verificables)
- **Glosario** — [`paper/glosario.md`](paper/glosario.md)
- **Registro de decisiones** — [`paper/registro_decisiones.md`](paper/registro_decisiones.md)

---

## Cómo contribuir

Todas las contribuciones son bienvenidas, hechas con Amor Operativo:

- **Respeto** — Critica con argumentos, no ataques.
- **Transparencia** — Di quién eres y por qué propones lo que propones.
- **No dominación** — Convence con razones, no impongas.
- **Cuidado** — Revisa, escucha, mejora.

Formas de contribuir, con una plantilla para cada caso:

- Reportar errores — abre un issue con la plantilla [`bug_report.md`](.github/ISSUE_TEMPLATE/bug_report.md)
- Proponer mejoras — abre un issue con la plantilla [`feature_request.md`](.github/ISSUE_TEMPLATE/feature_request.md)
- Enviar feedback sobre el paper — abre un issue con la plantilla [`feedback.md`](.github/ISSUE_TEMPLATE/feedback.md)
- Proporcionar cambios más amplios — abre un pull request siguiendo la plantilla [`PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md)
- Traducir el paper a otros idiomas — lee [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Añadir referencias verificables — lee [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Darnos estrella — usa el botón de GitHub 😊

Para contribuciones más involucradas, lee primero [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Estado del proyecto

Los principios de Amor Operativo están especificados. Las métricas son audibles por principios. El paper completo y la guía de implementación están en borrador. La revisión crítica y el test de amor operativo están diseñados pero no ejecutados.

| Fase | Estado real | Observación |
|---|---|---|
| Definición del concepto | Completada | Definición formal establecida en `SPEC-AUTORITATIVA.md` |
| Especificación de los 10 principios | Completada | Documento autónomo en `paper/especificacion.md` |
| Métricas operativas | Completadas | Tabla en `paper/metricas.md`; 6 medibles, 4 abiertos |
| Paper completo | En desarrollo | Borrador en `paper/paper.md` y `paper/paper_en.md` |
| Guía de implementación | En desarrollo | Borrador en `paper/implementacion.md` |
| Revisión crítica | Diseñada, no ejecutada | Escenarios S1–S10 listos; sin ejecución real |
| Publicación v1.0.0 | Pendiente | Requiere aprobación humana (puerta F11) |
| Traducciones | Pendiente | Solo ES y EN disponibles |
| Test de amor operativo | Diseñado, sin ejecución real | `eval/scenarios/` listo; `eval/results/` vacío |

**Nota:** Los principios 1 (Atención no requerida), 2 (Consistencia sin supervisión), 5 (Sostenibilidad a largo plazo) y 8 (Reciprocidad) están en estado **abierto** en la especificación actual. No pueden ser evaluados hasta que sus instrumentos se estandaricen. Ver [`paper/especificacion.md`](paper/especificacion.md) para el estado de medición por principio y [`spec/spec-v1.yaml`](spec/spec-v1.yaml) para la fuente máquina-legible.

---

## Cómo citar

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

Para más detalles de citación, consulta [`CITATION.cff`](CITATION.cff).

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

## Índice del repositorio

```
amor-operativo/
├── README.md                 ← este fichero
├── LICENSE                   ← CC BY-SA 4.0
├── CITATION.cff              ← citación formal
├── CONTRIBUTING.md           ← cómo contribuir
├── CODE_OF_CONDUCT.md        ← código de conducta basado en los 10 principios
├── GOVERNANCE.md             ← quién decide qué, versión y cambio de principios
├── CHANGELOG.md
├── VERSION
├── informe_operador.md       ← informe de progreso por fase para el operador
├── paper/
│   ├── paper.md              ← paper completo en español
│   ├── paper_en.md           ← paper completo en inglés (manuscrito de referencia)
│   ├── resumen_ejecutivo.md  ← resumen ejecutivo de 200 palabras
│   ├── especificacion.md     ← los 10 principios como documento autónomo
│   ├── metricas.md           ← tabla de métricas operativas por principio
│   ├── implementacion.md     ← guía de implementación
│   ├── referencias.md        ← mínimo 30 referencias verificables
│   ├── registro_decisiones.md ← decisiones editoriales y críticas no resueltas
│   ├── glosario.md           ← términos clave
│   └── figures/              ← diagramas (pipeline de auditoría, escalera de complejidad)
├── docs/                     ← fuente de GitHub Pages (HTML generado + index.md)
├── spec/
│   ├── spec-v1.yaml          ← especificación máquina-legible
│   ├── metrics.md            ← métricas operativas (fuente de verdad)
│   ├── audit-protocol.md     ← protocolo de auditoría
│   └── auditor/              ← implementación de referencia del auditor
├── eval/
│   ├── protocol.md           ← protocolo de test de amor operativo
│   ├── scenarios/            ← escenarios S1–S10
│   └── results/              ← resultados de ejecución (vacío hasta la fecha)
├── reviews/
│   ├── redteam-objections.md
│   ├── gaming-vectors.md
│   ├── citation-audit.json
│   ├── claim-traceability.md
│   └── repro-audit.md
└── .github/
    ├── ISSUE_TEMPLATE/
    │   ├── feedback.md
    │   ├── bug_report.md
    │   └── feature_request.md
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/
        ├── ci.yml
        └── publish.yml
```

---

*Español (canónico para el operador) · Inglés (manuscrito de referencia en `paper/paper_en.md`) · Coordinación en español.*
