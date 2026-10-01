# Revisión crítica del outline congelado — AMO-20 F2b

**Revisor:** Dr. Nadia Okafor (QA Lead / Revisor Crítico, AMO)
**Fecha:** 2026-09-25
**Fuente revisada:** `/home/hydra/ops-state/amor_operativo/paper/manuscript/INDEX.md`
**Estado del review:** CONCLUIDO — entregable en disco

---

## Resumen ejecutivo del veredicto

El outline congelado **cubre la estructura obligatoria del brief del operador** (8 secciones + resumen ejecutivo + referencias + glosario) y el presupuesto de palabras (9.200) está dentro del rango aprobado (8.000–12.000). No obstante, hay **6 problemas de estructura, 3 de alcance y 2 de calidad** que deben resolverse antes de que los redactores empiecen. El veredicto global es **CON CAMBIOS REQUERIDOS** — el outline no es RECHAZADO pero no es APROBADO sin modificaciones.

---

## 1. Veredicto por sección

| # | Sección | Palabras | Presupuesto | Veredicto | Racón concreto |
|---|---|---|---|---|---|
| 0 | Resumen ejecutivo | 200 | 200 exactas | **APROBADA** | Estructura correcta; único dueño: Dr. Camila Duarte; contenido obligatorio presente. |
| 1 | Introducción | 1.000 | 1.000 | **APROBADA** | 4 subsecciones obligatorias presentes (1.1–1.4); dueño asignado; sin hueco. |
| 2 | Fundamentos conceptuales | 1.500 | 1.500 | **APROBADA** | 4 subsecciones obligatorias presentes (2.1–2.4); influencias listadas correctamente. |
| 3 | Especificación | 2.500 | 2.500 | **CON CAMBIOS** | 3.1–3.4 presentes; **3.5 falta** en el outline: el brief exige ejemplos en salud, educación, justicia, economía, arte y ciencia; INDEX solo dice "Ejemplos de aplicación en salud, educación, justicia, economía, arte y ciencia" sin dedicarles espacio ni peso. Ver §3 de este review. |
| 4 | Implementación | 2.000 | 2.000 | **CON CAMBIOS** | 4.1–4.5 presentes en títulos; **falta explicitar que 4.5 (Test de amor operativo) debe incluir métricas reales**, no solo escenarios. Ver §3.2. |
| 5 | Discusión | 1.500 | 1.500 | **APROBADA** | 5.1–5.5 presentes; contraargumentos y riesgos de mala implementación cubiertos. Dueño: Writer — Theory & Philosophy. |
| 6 | Conclusiones | 500 | 500 | **APROBADA** | 6.1–6.3 presentes; llamada a la acción y preguntas abiertas cubiertas. |
| 7 | Referencias | fuera de cuerpo | 30 mínimo | **APROBADA (con reserva)** | Outline establece mínimo 30 verificables; corpus muestra 32 referencias (8 LEIDAS, 15 HOJEADAS, 9 PENDIENTES). **Reserva:** la regla dura exige que toda referencia sea leída antes de usarse; 9 pendientes y 15 solo hojeadas es un riesgo de ejecución. Ver §4. |
| 8 | Glosario | fuera de cuerpo | — | **APROBADA** | Términos obligatorios listados; glosario bilingüe presente; definición textual de amor operativo sin parafrasear. |

**Total cuerpo:** 9.200 palabras (dentro de 8.000–12.000) — **APROBADO**.

---

## 2. Estructura global vs. brief del operador

### 2.1 Cobertura de entregables obligatorios

El brief del operador (SPEC-AUTORITATIVA.md §"Entregables finales") exige estos nombres exactos en `paper/`:

| Entregable | Outline lo menciona | Veredicto |
|---|---|---|
| `paper.md` (ES, 8.000–12.000) | Sí — en ensamblado | APROBADA |
| `paper_en.md` (EN) | Sí — en ensamblado | APROBADA |
| `resumen_ejecutivo.md` (200 palabras) | Sí — resumen ejecutivo sección 0 | APROBADA |
| `glosario.md` | Sí — sección 8 | APROBADA |
| `metricas.md` (tabla por principio) | **NO** — menciona métricas en 3.3 pero no como entregable separado | CON CAMBIOS |
| `referencias.md` (≥30 verificables) | Sí — sección 7 | APROBADA |
| `registro_decisiones.md` | **NO** — ausente del outline | CON CAMBIOS |
| `README.md` (raíz) | **NO** | CON CAMBIOS |
| `CONTRIBUTING.md` | **NO** | CON CAMBIOS |
| `CODE_OF_CONDUCT.md` | **NO** | CON CAMBIOS |
| `LICENSE` | **NO** | CON CAMBIOS |
| `CITATION.cff` | **NO** | CON CAMBIOS |
| `GOVERNANCE.md` | **NO** (mencionado como "especificacion maquina-legible" en SPEC) | CON CAMBIOS |
| `informe_operador.md` | **NO** | CON CAMBIOS |
| `.github/ISSUE_TEMPLATE/{feedback,bug_report,feature_request}.md` | **NO** | CON CAMBIOS |
| `.github/workflows/publish.yml` | **NO** (mencionado en SPEC) | CON CAMBIOS |

**Problema estructural:** El outline cubre el manuscrito (secciones 0–8) pero no los entregables de infraestructura del repo. Eso es aceptable si el outline se limita a la estructura del paper, pero debe quedar claro en el `registro_decisiones.md` qué entregables de infraestructura corresponden a qué fase.

### 2.2 Inconsistencia de ruta: manuscrito EN vs. ES

INDEX.md línea 7 dice: "**Idioma:** inglés (manuscrito), español (artefactos de coordinación)".
INDEX.md línea 130: ensamblado EN en `manuscript/manuscript.md`, ES en `manuscript/manuscript-es.md`.

Pero SPEC-AUTORITATIVA.md línea 57 dice: "Manuscrito final en **inglés** (`paper/paper_en.md`), versión espejo en español (`paper/paper.md`)."

**Inconsistencia:** INDEX usa `manuscript/manuscript.md` como manuscrito EN, pero SPEC usa `paper/paper_en.md`. INDEX rutea el manuscrito EN a `paper/` y el ES a `paper/` con nombres distintos de los que usa SPEC. Esto genera dos problemas:

1. **Rutas distintas para el mismo entregable:** INDEX dice `paper/manuscript/manuscript.md` (EN) y `paper/manuscript/manuscript-es.md` (ES); SPEC dice `paper/paper_en.md` (EN) y `paper/paper.md` (ES). Los redactores no saben qué ruta usar.
2. **El ensamblado de INDEX se refiere a los ficheros del manuscrito como si fueran los entregables finales**, pero SPEC los coloca en `paper/` directamente.

**Cambio exigido:** Alineación de rutas. El outline debe usar las rutas de SPEC (`paper/paper_en.md` para EN, `paper/paper.md` para ES) o documentar explícitamente por qué usa `manuscript/` como carpeta intermedia. Si `manuscript/` es una carpeta de trabajo y los entregables finales están en `paper/`, el outline debe decirlo explícitamente y dejar claro que el ensamblado final se mueve de `manuscript/` a `paper/`.

### 2.3 Asignación de dueños — coherencia con el roster

INDEX asigna:
- Sección 3 → Dr. Camila Duarte (Editorial Director)
- Sección 0 → Dr. Camila Duarte
- Sección 8 → Dr. Camila Duarte

SPEC-AUTORITATIVA.md tabla de reparto (líneas 188–205) dice:
- Sección 3 → Dr. Camila Duarte (Editorial Director) — coincide
- Sección 0 → no asignada explícitamente en la tabla (solo "Editor Jefe consolida")
- Sección 8 → no asignada explícitamente

**Sin conflicto grave**, pero la tabla SPEC no cubre todas las secciones; hay un hueco de documentación de asignación para secciones 0, 7, 8. No es bloqueante pero debe cerrarse antes del freeze.

---

## 3. Huecos de estructura frente al brief

### 3.1 Sección 3.5 — ejemplos de aplicación

**Obligación del brief:** "3.5 Ejemplos de aplicación en salud, educación, justicia, economía, arte y ciencia."

INDEX.md exige 3.5 como subsección de 3. Especificación (línea 59). Pero el outline **no asigna palabras ni estructura interna** a 3.5: no dice cuántas palabras, no dice si los 6 ejemplos son párrafos breves o ejemplos desarrollados, no dice si es un recorrido o un análisis. Con 2.500 palabras totales para la sección 3, y 3.1 + 3.2 consumiendo probablemente 1.000–1.200 palabras, 3.3 (tabla de métricas) consume 300–500, 3.4 (criterios de auditoría) 300–400, queda poco para 3.5 si no se planea.

**Cambio exigido:** El outline debe asignar un presupuesto explícito a 3.5 (recomendado: 400–500 palabras) y especificar el formato: 6 ejemplos, cada uno de 60–80 palabras, mostrando cómo los principios se manifiestan en ese dominio. Sin eso, 3.5 se convertirá en un apéndice superficial que el reviewer adversario (yo) puede atacar como "ejemplos teatrales sin análisis".

### 3.2 Sección 4.5 — Test de amor operativo

**Obligación del brief:** "4.5 Test de amor operativo: escenarios, evaluación, métricas."

El outline incluye 4.5 pero no especifica qué significa "métricas" aquí. La sección 4.5 debe incluir:
- Escenarios concretos (no genéricos) que puedan ejecutarse
- Una métrica por principio aplicada al test
- Un procedimiento de evaluación

Sin eso, 4.5 queda como "tenemos un test" sin decir qué mide. Eso es exactamente el tipo de vagueness que el QA Lead debe rechazar antes del freeze.

**Cambio exigido:** El outline debe aclarar que 4.5 no es un capítulo descriptivo sino una sección de diseño de evaluación, y debe enlazar con `eval/protocol.md` y `eval/scenarios/` (entregables del SPEC). Si esos entregables no existen cuando se escribe 4.5, la sección debe decirlo explícitamente: "el test está en diseño; este capítulo describe el protocolo planeado, no resultados".

### 3.3 Entregable `metricas.md` — ausente del outline

SPEC-AUTORITATIVA.md línea 69: "`paper/metricas.md` — Tabla de metricas por principio."

INDEX no menciona `metricas.md` como entregable separado. La sección 3.3 del manuscrito (tabla de métricas) está dentro del cuerpo, pero el SPEC exige un fichero de métricas independiente que sea fuente para el manuscrito y para la auditoría. Eso tiene sentido: la tabla del manuscrito es presentacional; `metricas.md` es la definición operativa completa con escala, umbral y procedimiento.

**Cambio exigido:** INDEX debe añadir `metricas.md` como entregable explícito, con dueño (recomendado: Dr. Camila Duarte o Dr. Aisha Bakr) y estado. Debe aclarar la relación: `metricas.md` → 3.3 (el manuscrito consume la tabla, no la define).

### 3.4 Entregable `registro_decisiones.md` — ausente del outline

SPEC línea 71: "`paper/registro_decisiones.md` — Decisiones editoriales y criticas no resueltas."

INDEX no lo menciona. Este fichero es obligatorio: documenta cada decisión editorial y cada crítica que no se resolvió antes del freeze. Sin él, no hay trazabilidad de por qué se tomó cada decisión.

**Cambio exigido:** INDEX debe añadir `registro_decisiones.md` como entregable, con dueño (recomendado: Dr. Camila Duarte como Editor Jefe) y vacío inicial que se va rellenando durante la escritura.

### 3.5 Fase de publicación — no reflejada en el outline

INDEX es un outline de **manuscrito**. El SPEC, en cambio, es un contrato completo que incluye: README, CONTRIBUTING, CODE_OF_CONDUCT, LICENSE, CITATION.cff, GOVERNANCE, `.github/ISSUE_TEMPLATE/*`, `.github/workflows/publish.yml`, `informe_operador.md`, y la estructura completa del repo.

El outline congelado no menciona ninguna de estas fases. Eso es aceptable si el outline se limita al manuscrito, pero **debe ser explícito**: "Este outline cubre solo las secciones 0–8 del manuscrito. La infraestructura de repo, los entregables de publicación y la puerta de publicación (F11) se gestionan en fases separadas."

**Cambio exigido:** Añadir un aviso explícito en INDEX que delimita el alcance del outline y apunta a las fases de infraestructura y publicación.

---

## 4. Riesgos de alcance

### 4.1 Riesgo: métricas con escala, umbral y procedimiento

La regla dura (SPEC línea 57, INDEX línea 157): "Toda métrica operativa en 3.3 debe especificar cómo se mide, en qué escala y con qué umbral de pasa/no-pasa."

El outline establece que 3.3 es una tabla con métricas por principio. El SPEC ya tiene `spec/metrics.md` como borrador. **Riesgo:** si el borrador de métricas no tiene escala, umbral y procedimiento para los 10 principios antes de que se escriba 3.3, el manuscrito tendrá métricas incompletas. El QA Lead (yo) voy a auditar cada métrica de `spec/metrics.md` cuando llegue mi turno; si alguna falta, marcaré el principio como "CON CAMBIOS" en la revisión del manuscrito.

**Mitigación:** El outline debe asignar explícitamente la tarea de completar `spec/metrics.md` antes de escribir 3.3, con dueño y fecha. Sin esa asignación, 3.3 se escribe sobre métricas incompletas.

### 4.2 Riesgo: referencias sin lectura completa

El corpus de referencias (sections/07-referencias.md) tiene 32 referencias: 8 LEIDAS, 15 HOJEADAS, 9 PENDIENTES. El brief exige ≥30 verificables **y** que toda referencia sea leída antes de usarse.

**Riesgo real:** 9 referencias pendientes y 15 solo hojeadas. Si los redactores usan referencias pendientes o hojeadas como si fueran leídas, violan la regla dura. Especialmente peligroso en 2.3 (influencias: agape, ética del cuidado, psicología del desarrollo, teoría del apego) donde se necesita referencias de filosofía moral y psicología — dominios donde el corpus actual es más débil que en IA safety.

**Cambio exigido:** El outline debe asignar la tarea de leer las 9 pendientes y las 15 hojeadas antes de la escritura de las secciones 2 y 5, con dueño (Dr. Henrik Vogel, Source Verifier) y fecha. Si alguna no puede leerse, debe marcarse `[NO VERIFICADA]` y excluirse.

### 4.3 Riesgo: presupuesto de palabras desbalanceado

El total de 9.200 está dentro del rango, pero la distribución es una decisión editorial que puede causar problemas:

- Sección 3 (2.500 palabras) es la más grande. Con 3.1 + 3.2 + 3.3 + 3.4 + 3.5, el espacio por subsección es ajustado. Si 3.5 se expande más de lo planeado, otras subsecciones se contraen.
- Sección 4 (2.000 palabras) con 5 subsecciones es 400 palabras por subsección — suficiente para arquitectura de referencia y escalera de complejidad, pero justo para 4.5 (test de amor operativo) si incluye escenarios reales.

**Riesgo:** que los redactores sobrescriban secciones pequeñas (6 Conclusiones, 500 palabras) y subescriban secciones grandes (3 Especificación, 2.500 palabras) porque la granularity del outline no los obliga a respetar el presupuesto.

**Mitigación:** Ninguna acción exigida ahora; es una supervisión del Editorial Director (Dr. Camila Duarte) durante la escritura. El QA Lead auditará la cuenta de palabras por sección al entregar cada sección.

### 4.4 Riesgo: definición formal y principios literales

SPEC línea 36–53: la definición formal y los 10 principios son literales, sin parafrasear. INDEX lo reitera (línea 61: "el dueño no tiene discreción sobre su redacción, solo sobre el ensamblado y la exposición").

**Riesgo:** un redactor que no conoce el SPEC puede parafrasear la definición o cambiar el orden de los principios. Eso es una violación de regla dura.

**Mitigación:** El outline debe añadir un aviso explícito en la sección 3 que diga: "La definición formal (3.1) y los 10 principios (3.2) son literales del SPEC-AUTORITATIVA.md. Cualquier cambio requiere aprobación del PI (Dr. Adrian Vega) y un issue de cambio de especificación." Esto ya está en INDEX línea 61, pero debe estar también en el header de la sección 3 del manuscrito cuando se escriba.

### 4.5 Riesgo: puerta de publicación

SPEC línea 240–243: "Nada se publica en GitHub, arXiv, preprints ni redes sin aprobación humana explícita del operador."

INDEX línea 159 reitera la regla. **Pero** el outline no asigna explícitamente la tarea de *no publicar* a ningún redactor. Eso es una violación de proceso: si un redactor empuja accidentalmente a un remoto, no hay trazabilidad de quién lo hizo.

**Cambio exigido:** El outline debe añadir una nota al pie de cada sección que dice: "Este manuscrito se escribe en staging local. Ningún push a remoto público hasta aprobación del operador en el issue F11." Esto ya está en las reglas duras (INDEX línea 159), pero debe estar explícito en el borrador de cada sección, no solo en el outline.

---

## 5. Cambios exigidos antes de que los redactores empiecen

### 5.1 Cambios estructurales en INDEX.md (prioridad alta)

1. **Añadir 3.5 como subsección planificada** con presupuesto de palabras (400–500) y formato (6 ejemplos, 60–80 palabras cada uno).
2. **Añadir 4.5 como sección de diseño de evaluación** con enlace a `eval/protocol.md` y `eval/scenarios/`, y aclaración de que no hay resultados reales todavía.
3. **Añadir `metricas.md` como entregable** en la lista de entregables del outline, con dueño y relación con 3.3.
4. **Añadir `registro_decisiones.md` como entregable** en la lista de entregables.
5. **Alinear rutas de manuscrito** con SPEC (`paper/paper_en.md` para EN, `paper/paper.md` para ES) o documentar explícitamente la carpeta `manuscript/` como trabajo intermedio.

### 5.2 Cambios de alcance (prioridad media)

6. **Añadir nota de alcance explícita** que delimite que el outline cubre solo el manuscrito (secciones 0–8) y que la infraestructura de repo y la puerta de publicación están en fases separadas.
7. **Añadir a referencia cruzada de métricas** que enlaza 3.3 con `spec/metrics.md` y establece que las métricas deben estar completas antes de escribir 3.3.
8. **Añadir asignación de tarea de lectura de referencias** (9 pendientes + 15 hojeadas) con dueño (Dr. Henrik Vogel) y fecha antes de la escritura de las secciones 2 y 5.

### 5.3 Cambios de proceso (prioridad baja, pero obligatorios)

9. **Añadir nota de puerta de publicación** en cada sección del manuscrito: "Este manuscrito se escribe en staging local. Ningún push a remoto público hasta aprobación del operador en F11."
10. **Añadir aviso de literalidad** en la sección 3: definición formal y principios son literales del SPEC; cualquier cambio requiere issue de cambio de especificación.

---

## 6. Veredicto global

**CON CAMBIOS REQUERIDOS.**

El outline congelado es **estructuralmente correcto** (cubre las 8 secciones + resumen + referencias + glosario; presupuesto de 9.200 palabras dentro del rango 8.000–12.000) pero tiene **huecos de estructura y de alcance** que deben cerrarse antes de que los redactores empiecen. No es RECHAZADO porque no hay fallos graves de estructura; no es APROBADO porque los cambios de la sección 5 de este review son obligatorios.

**Acciones requeridas para APROBADO:**
- Los cambios 1–5 de la sección 5.1 de este review deben aplicarse a INDEX.md.
- Los cambios 6–8 de la sección 5.2 deben documentarse en `registro_decisiones.md` (que aún no existe — ver cambio 4).
- Los cambios 9–10 de la sección 5.3 deben incorporarse en el borrador de cada sección cuando se escriba, no en el outline.

**Sin estos cambios, el QA Lead (yo) emitirá veredicto RECHAZADO en la revisión del manuscrito cuando llegue mi turno.**

---

## 7. Firmas y trazabilidad

- Revisor: Dr. Nadia Okafor (QA Lead / Revisor Crítico, AMO)
- Fecha: 2026-09-25
- Estado: CONCLUIDO
- Entregable: `/home/hydra/ops-state/amor_operativo/paper/reviews/outline_review.md`
- Versión: 1.0

---

* Este review fue escrito adversarialmente: su objetivo es encontrar los modos de fallo más probables del outline antes de que los redactores inviertan en escribir secciones que luego habría que reescribir.Los cambios exigidos no son opcionales; son condiciones para que el outline sea aprobado.*
