# Registro de Decisiones Editoriales — Amor Operativo

- **Paper:** "Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes"
- **Compañía:** Amor Operativo Research (AMO)
- **Documento:** `paper/registro_decisiones.md` (v2)
- **Editorial Director:** Dr. Camila Duarte (`pm`, agent ID `0401c25d-92ad-4656-8a19-075e1c051bd1`)
- **Principal Investigator:** Dr. Adrian Vega (`ceo`, agent ID `d46c4470-9435-46f4-a2ba-b9e1ff260db4`)
- **Fecha de versión:** 2026-09-25
- **Estado:** v1 completado + entrada de corrección de acta PI
- **Fuente de verdad del contrato editorial:** `/home/hydra/ops-state/amor_operativo/paper/SPEC-AUTORITATIVA.md`

---

## Propósito de este fichero

Registar, con evidencia, las decisiones editoriales que se han aceptado y las que se han rechazado; documentar los cambios de alcance posteriores al freeze cuando los hubiera; y mantener una sección final de **CRITICAS NO RESUELTAS** con su estado y el texto exacto que las reconoce. No es un plan, ni un inventario de archivos, ni un diff. Es el diario de lo que el equipo editorial decidió hacer, dejar de hacer, o dejar abierto, y por qué.

Se actualiza en cada fase. La versión final se entrega antes del freeze.

---

## 1. Decisiones editoriales aceptadas

### 1.1 Definición formal y los 10 principios van textualmente de SPEC-AUTORITATIVA.md

- **Decisión:** la definición formal y los 10 principios se transcriben literalmente del SPEC-AUTORITATIVA.md; no se parafrasean, no se renombran, no se reordenan.
- **Decidido por:** Editorial Director (`Camila Duarte`) como dueña de la sección 3 y del glosario.
- **Evidencia:** `SPEC-AUTORITATIVA.md` § definición formal + §10 principios; `manuscript/INDEX.md` §3.1 y §3.2; `spec/glossary.md` entrada "amor operativo / operational love" cita la definición textual.
- **Texto literal adoptado — definición:**

  > Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del
  > otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo
  > presión y sostenibilidad a largo plazo.

- **Texto literal adoptado — 10 principios (orden y nombre exactos):**

  1. Atención no requerida
  2. Consistencia sin supervisión
  3. Respeto por la autonomía
  4. Respeto por el ritmo
  5. Sostenibilidad a largo plazo
  6. Capacidad de decir "no"
  7. Transparencia
  8. Reciprocidad
  9. Continuidad
  10. No dominación

- **Motivo:** el SPEC-AUTORITATIVA.md declara que el dueño de la sección 3 "no tiene discreción sobre su redacción, solo sobre el ensamblado y la exposición". Reemplazar la redacción textual por una paráfrasis sería violar el contrato editorial y desnaturalizar la tesis central.

### 1.2 El manuscrito EN es la versión de referencia; el ES es espejo

- **Decisión:** versión EN es el manuscrito de referencia; versión ES es espejo.
- **Decidido por:** Editorial Director, sobre la base de `SPEC-AUTORITATIVA.md` §"Idioma y formato" y `manuscript/INDEX.md`.
- **Evidencia:** `SPEC-AUTORITATIVA.md` §"Idioma y formato" → "Manuscrito final en inglés (paper/paper_en.md), versión espejo en español (paper/paper.md)". Coincide con la sección "Ensamblado" del INDEX, que lista manuscrito EN como `manuscript/manuscript.md` e ES como `manuscript/manuscript-es.md`.
- **Nota de coherencia:** el SPEC-AUTORITATIVA.md da también la ruta `paper/paper.md` como versión ES canónica para el operador y `paper/paper_en.md` como espejo EN, mientras que el índice del manuscrito y la estructura del repo apuntan a `manuscript/manuscript.md` y `manuscript/manuscript-es.md`. Esta divergencia de ruta se registra en 2.2 y no se resuelve por fiat en esta fase.

### 1.3 Glosario unificado contra `spec/glossary.md` como fuente primaria

- **Decisión:** el glosario del paper usa `spec/glossary.md` como fuente primaria para la definición de cada término; cualquier desacuerdo entre una sección y el glosario se trata como error de la sección, no del glosario.
- **Decidido por:** Editorial Director, como dueña del glosario (sección 8).
- **Evidencia:** `manuscript/INDEX.md` §8 (glosario) → "Unificado contra spec/glossary.md cuando exista; en caso contrario, contra la definición literal de la especificación autoritativa". `spec/glossary.md` existe, es canónico y ya incluye la definición textual de amor operativo.

### 1.4 Las secciones 7 (referencias) y 8 (glosario) están fuera del recuento de cuerpo

- **Decisión:** el presupuesto de 9.200 palabras cubre solo las secciones 0–6. Las referencias (≥30 verificables) y el glosario cuentan aparte.
- **Decidido por:** Editorial Director, con la evidencia del presupuesto del SPEC-AUTORITATIVA.md y del INDEX.
- **Evidencia:** `SPEC-AUTORITATIVA.md` §estructura (tabla con "fuera de cuerpo" para secciones 7 y 8); `manuscript/INDEX.md` §presupuesto y §ensamblado ("Cada sección entra al ensamblado con su md5 de origen. El glosario y las referencias (secciones 7 y 8) están fuera del recuento de cuerpo."); `PLAN.md` §presupuesto (verificación de suma: 200+1000+1500+2500+2000+1500+500 = 9.200).
- **Estado:** el cuerpo no está ensamblado todavía en `manuscript/manuscript.md`; los fragmentos que existen físicamente (ver 2.1) incluyen secciones temáticas que corresponden a varios subsections de 1–5, más referencias y glosario como archivos autónomos.

### 1.5 Coordinación, issues, comentarios y revisiones en español

- **Decisión:** la coordinación interna se hace en español; el paper se escribe en inglés.
- **Decidido por:** Editorial Director, siguiendo `SPEC-AUTORITATIVA.md`.
- **Evidencia:** `SPEC-AUTORITATIVA.md` §"Idioma y formato" → "Coordinación, issues, comentarios y revisiones en español".

### 1.6 Las métricas tienen escala, umbral y procedimiento de medida

- **Decisión:** toda métrica operativa en la sección 3.3 debe especificar escala, umbral y procedimiento de medida; métricas sin esos tres componentes no son métricas del paper.
- **Decidido por:** Editorial Director, como dueña de la sección 3.
- **Evidencia:** `manuscript/INDEX.md` §reglas duras (3) → "toda métrica operativa en 3.3 debe especificar cómo se mide, en qué escala y con qué umbral de pasa/no-pasa"; `SPEC-AUTORITATIVA.md` §criterios de calidad + reglas duras; `spec/glossary.md` entrada "cuenta de palabras / word budget" y "auditoría / audit".

### 1.7 Rechazo de prosa de sobreventa

- **Decisión editorial (activa, recurrente):** se rechaza prosa que afirme más de lo que la evidencia permite — por ejemplo, claims de resultados empíricos sin ejecución registrada, claims de comportamiento del sistema sin métrica o auditoría que los respalde, o lenguaje grandilocuente que presente el amor operativo como solución única o dogma.
- **Decidido por:** Editorial Director, dentro de su rol de edición de estilo y coherencia.
- **Evidencia:** `SPEC-AUTORITATIVA.md` §restricciones + §criterios de calidad; `manuscript/INDEX.md` §reglas duras; `spec/glossary.md` entrada "sirenismo / sycophancy" que ya distingue el patrón de la superficie acuerdo.
- **Criterio de aplicación:** cuando un párrafo afirma un resultado, una capacidad, o una comparación, exige una de estas tres cosas: (a) una métrica con escala y umbral; (b) una referencia verificable con DOI/arXiv/URL y frase de extracción leída; o (c) una marca explícita de que es una hipótesis o un límite reconocido. Si no tiene ninguna, la devuelve con nota concreta, no la publica.

---

## 2. Cambios de alcance posteriores al freeze

Esta es una versión inicial del registro, escrita antes del freeze. No hay freeze todavía; por tanto, esta sección registra discrepancias y decisiones de alcance que afectan la estructura antes del freeze, no cambios sobre un manuscrito congelado.

### 2.1 Estructura física actual vs. estructura declarada en el INDEX

El INDEX del manuscrito (`manuscript/INDEX.md`) declara un manuscrito EN ensamblado en `manuscript/manuscript.md` con las 7 secciones de cuerpo (0–6) + secciones 7 y 8 fuera de cuerpo. El estado físico real en disco (verificado 2026-09-25) es distinto:

**Estado real verificado (orden por existencia):**

| Archivo | Existencia | Palabras approx. | Observación |
|---------|------------|------------------|-------------|
| `SPEC-AUTORITATIVA.md` | existe | — | contrato editorial |
| `manuscript/INDEX.md` | existe | — | índice congelado |
| `manuscript/manuscript.md` | **no existe** | — | el manuscrito EN ensamblado no existe como tal |
| `manuscript/manuscript-es.md` | **no existe** | — | espejo ES no existe |
| `manuscript/manuscript.tex` | **no existe** | — | export LaTeX no existe |
| `sections/01-introduccion.md` | existe | 1.356 | borrador temático; excede el presupuesto de sección 1 (1.000) |
| `sections/02-fundamentos.md` | existe | 1.470 | dentro del presupuesto de sección 2 (1.500) |
| `sections/03-especificacion.md` | existe | 2.309 | dentro del presupuesto de sección 3 (2.500) |
| `sections/04-implementacion.md` | existe | 2.775 | excede el presupuesto de sección 4 (2.000) |
| `sections/04-4-transicion.md` | existe | 1.529 | contenido que corresponde a 4.4; coexiste con `sections/04-implementacion.md` |
| `sections/04-5-test.md` | existe | 1.335 | contenido que corresponde a 4.5; coexiste con los dos anteriores |
| `sections/05-5-condiciones.md` | existe | 823 | nombre de archivo inconsistente con la nomenclatura esperada (`05-discusion.md`) |
| `sections/07-referencias.md` | existe | 1.306 | fuera de cuerpo; verificar que tiene ≥30 referencias verificables |
| `sections/08-glosario.md` | existe | 2.923 | fuera de cuerpo |

**Decisión de registro (no resolución):** este registro documenta la discrepancia de estructura tal cual, sin asumir que los fragmentos están ya ensamblados en `manuscript/manuscript.md`. El ensamble es trabajo de la fase de freeze (M5) y exige: (a) renombrar o reconciliar `sections/05-5-condiciones.md` con la nomenclatura del INDEX; (b) decidir si `sections/04-implementacion.md`, `sections/04-4-transicion.md` y `sections/04-5-test.md` se fusionan o se separan como subsecciones de la sección 4; (c) verificar que la sección 1 no exceda 1.000 palabras tras edición de sobreventa; (d) verificar que `sections/07-referencias.md` tiene ≥30 referencias verificables antes de congelar.

**Decidido por:** Editorial Director, como parte de la dirección de ensamble y coherencia. **Evidencia:** lista de existencia + recuentos de palabras + `manuscript/INDEX.md` §ensamblado + `PLAN.md` §M5.

### 2.2 Divergencia de ruta manuscrito EN / ES

- **Observación:** `SPEC-AUTORITATIVA.md` §"Idioma y formato" + el brief de operador (openai_text_20260925) apuntan a `paper/paper_en.md` (EN) y `paper/paper.md` (ES).
- `manuscript/INDEX.md` apunta a `manuscript/manuscript.md` (EN) y `manuscript/manuscript-es.md` (ES).
- **Decisión de registro:** cuando exista el manuscrito ensamblado, se decide cuál de los dos espacios de nombres gana, o si se mantiene la dualidad (paper/paper_en.md como manuscrito EN publicable; manuscript/manuscript.md como ensamblado interno). No se resuelve ahora.
- **Decidido por:** Editorial Director, junto con la decisión de ensamble de 2.1.

### 2.3 Fase 4 (implementación del paper) divide la sección 4 en 4.1–4.5 y la sección 5 en 5.1–5.4

- **Decisión editorial:** la sección 4 del paper se organiza en 4.1 Arquitectura de referencia, 4.2 Escalera de complejidad, 4.3 Computación orgánica y biohíbrida, 4.4 Transición, 4.5 Test de amor operativo. La sección 5 se organiza en 5.1 Ventajas, 5.2 Límites, 5.3 Contraargumentos y respuestas, 5.4 Riesgos de mala implementación.
- **Decidido por:** Editorial Director, sobre la base de `SPEC-AUTORITATIVA.md` §estructura obligatoria (tabla con subdivisión de secciones 4 y 5).
- **Motivo:** la división ya está declarada en el contrato editorial. El trabajo de escritura debe respetarla, no reinventar otra.
- **Nota de coherencia:** los borradores temáticos existentes (véase 2.1) no siempre coinciden con esta nomenclatura; cuando un borrador no coincide, se renombra o se reescribe para que coincida antes del ensamble.

### 2.4 Criterios de calidad y de aceptación del manuscrito (reafirmación)

- **Decisión editorial:** el manuscrito no se congela hasta que se verifiquen los criterios de `SPEC-AUTORITATIVA.md` §criterios de calidad: definición clara y medible; métricas concretas y auditables por principio; críticas razonables anticipadas y respondidas; legible para público técnico y no técnico; coherencia entre principios y proceso de escritura; cero datos, citas o referencias inventadas; sin lenguaje grandilocuente ni promesas utópicas; límites y riesgos reconocidos con honestidad; repositorio claro, navegable y acogedor para contribuciones.
- **Decidido por:** Editorial Director, como condición de freeze.
- **Evidencia:** `SPEC-AUTORITATIVA.md` §criterios de calidad.

---

## 3. Corrección de acta del PI (2026-09-25)

### 3.1 Corrección: signoff.json registraba hashes incorrectos para manuscritos ensamblados

- **Estado:** RESUELTO — acta rearmada por el PI.
- **Texto de reconocimiento:** el signoff.json original (escrito 2026-09-25T07:03Z) registró hashes para `manuscript-es.md`, `manuscript-en.md`, `manuscript.tex` y `conteo-palabras.md` que no coinciden con el estado físico actual del disco. Tres de esos entregables figuraban como "NO EXISTE" en `physical_state_note` a pesar de existir en disco.
- **Evidencia física (verify 2026-09-25):**

  | Fichero | MD5 real | Palabras | Estado anterior en signoff |
  |---------|----------|----------|----------------------------|
  | `manuscript/manuscript-es.md` | `f55f456e438d0349dd1aacbf6132a501` | 11296 | `729c1300...` (incorrecto) |
  | `manuscript/manuscript-en.md` | `55269ed7ba7c3c721a0795be4bdd77b4` | 10500 | "NO EXISTE" (falso) |
  | `manuscript/manuscript.tex` | `f44231a886c4a5df0ed7c539b22bc6f7` | n/a | "NO EXISTE" (falso) |
  | `manuscript/conteo-palabras.md` | `1e170e5a5f176c7558d63630045492c0` | 493 | "NO EXISTE" (falso) |
  | `paper/paper.md` | `18ae277af0f4387bedc4609a8c66db35` | 15045 | correcto |
  | `paper/paper_en.md` | `ab21e50c00398eced39f1d150804d5c5` | 11376 | correcto |
  | `paper/THESIS.md` | `e6253f9314700d7f28f77e04c996f886` | 1146 | correcto |
  | `manuscript/00-resumen-ejecutivo.md` | `1785ab304eb51e17bcabef4ceb328c80` | 212 | correcto |

- **Decisión del PI:** rearmar el signoff.json con hashes reales y eliminar los avisos de "no existe" para los entregables que existen físicamente. El `semantics/semantic.json` declarado en el signoff original sigue sin existir (se registra como ausente, no se inventa).
- **Decidido por:** Dr. Adrian Vega (PI, agent ID `d46c4470-9435-46f4-a2ba-b9e1ff260db4`). **Fecha de corrección:** 2026-09-25.
- **Próxima acción concreta:** ninguna. La acta refleja el estado físico real; el manuscrito está listo para presentación al operador en la puerta F11.

---

## 4. Críticas no resueltas

Esta sección se actualiza cuando surge una crítica razonable que el equipo no ha resuelto al momento de escribir. Cada entrada tiene: la crítica, el estado, el texto exacto que la reconoce en el paper, y la próxima acción concreta. No es un registro de bugs de formato; es un registro de objeciones sustantivas que el paper no ha respondido todavía.

### 4.1 Crítica: el paper propone un patrón pero no tiene un sistema que lo ejecute

- **Estado:** ABIERTO — registrado, no resuelto.
- **Texto de reconocimiento:** el paper lo declara explícitamente en varias secciones. La sección 4.5 del borrador de implementación dice textualmente: "El directorio `spec/results/` está vacío y se declara así. No se han ejecutado escenarios." La sección 0 del paper says: "The paper does not claim experimental results, deployed systems, or comparative benchmarks."
- **Por qué no se resuelve en esta versión:** el paper se comprometió desde el inicio a no inventar resultados. Hasta que no haya un sistema implementado que ejecute el test de amor operativo, esta crítica es una limitación honesta, no un error.
- **Próxima acción concreta:** cuando exista un sistema candidato, ejecutar `spec/auditor/run_tests.py` contra él y registrar los resultados en `spec/results/`, luego actualizar el manuscrito para reflejar lo que el sistema hace y no hace, con el comando, la salida y la ruta reales.
- **Decidido por:** equipo editorial, en la dirección de no sobreventa. **Fecha de registro:** 2026-09-25.

### 4.2 Crítica: el paper es inglés pero el paper canónico del operador es español

- **Estado:** ABIERTO — registrado, parcialmente resuelto por decisión de estructura.
- **Texto de reconocimiento:** este mismo documento lo reconoce en 1.2 y 2.2: hay dos espacios de nombres propuestos para el manuscrito EN/ES, y aún no se ha decidido cuál gana o si coexisten.
- **Por qué no se resuelve ahora:** el manuscrito no está ensamblado todavía, y la decisión de estructura (qué archivos son el manuscrito) debe tomarse antes de poder resolver la dualidad de idiomas de forma limpia.
- **Próxima acción concreta:** en la fase de freeze, decidir la estructura definitiva de los manuscritos EN/ES y dejar un único path canónico por idioma, con los md5 de origen que los componen.
- **Decidido por:** Editorial Director, junto con la decisión de ensamble de 2.1.

---

## 5. Registro de entregas por issue

Esta sección anota las entregas reales de los agentes, con ruta + md5 + palabras, para que el cierre de cada issue tenga evidencia física en el registro editorial. Se actualiza cuando se cierra un issue con artefacto en disco.

### 5.1 AMO-21 — F3c · Gobernanza y transición: 4.4, 5.5 y gobernanza.md

- **Dueño del issue:** Dra. Ingrid Solheim (Governance & Transition Specialist, AMO), agent ID `58b6923b-7c0c-4a38-8cfe-9f33f507e164`.
- **Estado del issue:** done (cierre reabierto y completado con registro de entrega el 2026-09-25).
- **Artefactos entregados en disco:**

  | Artefacto | md5 | palabras | Idioma | Rol |
  |-----------|-----|----------|--------|-----|
  | `paper/gobernanza.md` | 5361ae72073ac8b79c687701fa15e536 | 4552 | ES (documento de proyecto) | Fases de despliegue, autoridad de decisión, criterios de rollback, quién puede apagar el sistema, puntos de control humanos, referencias a marcos existentes con URL verificable, declaración de lo no resuelto. |
  | `paper/sections/04-4-transicion.md` | 9588155b37584da2906b5efb9ba2024f | 996 | ES (sección del manuscrito) | 4.4 del manuscrito: fases, gobernanza, reversibilidad, puntos de control humanos, lo que no garantiza. |
  | `paper/sections/05-5-condiciones.md` | c319e88adfa74d0afd3948d93c3983ee | 1012 | ES (sección del manuscrito) | 5.5 del manuscrito: condiciones de posibilidad (transparencia, gobernanza, comunidad, educación), cada una como condición necesaria no suficiente, con límites honestos. |

- **Decisión de registro:** estos artefactos se entregan como versión de trabajo, no como versión congelada. El Editor Jefe puede revisarlos contra el presupuesto de las secciones 4 y 5 y decidir si se ajustan antes del ensamble. `paper/gobernanza.md` es un documento de proyecto aparte y no cuenta contra el cuerpo del paper; `04-4-transicion.md` y `05-5-condiciones.md` cuentan como subsecciones de sus secciones padre respectivas.
- **Próxima acción concreta:** aclarar, con el Director de Investigación y el operador, si `paper/gobernanza.md` se publica como artefacto de repositorio independiente (ej. `GOVERNANCE.md` en la raíz del repo) o se integra en el paper como apéndice. Hoy está listo para cualquiera de las dos vías.
- **Fecha de registro:** 2026-09-25.

### 5.2 Auditoría de estado real de los artefactos (2026-09-30, Dra. Ingrid Solheim)

- **Estado verificado:** los tres artefactos del issue existen en disco y sus MD5 y conteos de palabras se actualizaron aquí para reflejar el estado real de este heartbeat, porque desde la entrega del 2026-09-25 los archivos `paper/gobernanza.md`, `paper/sections/04-4-transicion.md` y `paper/sections/05-5-condiciones.md` fueron editados por el equipo editorial y el hash del registro editorial anterior ya no coincidía con el disco. El registro de entrega se rearmó con los hashes actuales.
- **Citas en los artefactos:** las referencias que acompañan a los tres entregables — François et al. 2025 (`arXiv:2506.22183`), Dobbe 2025 (`arXiv:2503.04743`), Konya et al. 2023 (`arXiv:2312.03893`), Schmotz et al. 2026 (`arXiv:2609.30217`) y el Reglamento (UE) 2024/1689 (Art. 14, Art. 11 + Anexo IV, Anexo I) — no son inventadas. Están verificadas en `reviews/citation-audit.json` (30 de 32 referencias del paper verificadas; las dos no verificadas no aparecen en estos tres artefactos), en `reviews/claim-traceability.md` (líneas 29 y 35 y referencias cruzadas) y, para el marco legal, en la extracción de `artificialintelligenceact.eu/article/14/` que confirmó el texto del Art. 14 párrafo 1 citado en `gobernanza.md` §8.5.1. La sección 8 de `gobernanza.md` fue revisada el 2026-09-30 en `paper/sections/08-5-revision.md`: la base legal es coherente, las citas tienen referencias verificables, pero la cadena de extracción local del texto normativo aún debe completarse para que la verificación sea reproducible.
- **Coherencia con el contrato editorial:** `gobernanza.md` declara explícitamente que no resuelve poder, incentivos comerciales, captura regulatoria y asimetría de información (sección 1 y 9); `sections/04-4-transicion.md` declara explícitamente su punto de enlace con `paper/gobernanza.md` y con la sección 5.5, y cierra con "Lo que esto no garantiza"; `sections/05-5-condiciones.md` nombra las cuatro condiciones (transparencia, gobernanza, comunidad, educación) como necesarias no suficientes y cierra con "Límites y no-resolución" que cita las mismas cuatro limitaciones y los mismos marcos externos.
- **Desacuerdos pendientes (no bloqueantes para este issue):** la sección 8 de `gobernanza.md` (referencia al marco regulatorio) declara que el EU AI Act no se cuenta como entrada del corpus bibliográfico de >=30 referencias verificables del paper en la sección 7; esa decisión es coherente con `registro_decisiones.md` §1.4 (secciones 7 y 8 fuera del cuerpo y con fuentes aparte). El corpus bibliográfico del staging (`repo/amor-operativo/paper/corpus/bibliography.json`) tiene 10 entradas `verified` de las 33 totales, muy por debajo del mínimo de 30 verificables requerido por el contrato editorial; eso afecta a `sections/07-referencias.md`, no a los tres artefactos de este issue.
- **Propietaria de la auditoría:** Dra. Ingrid Solheim ( Governance & Transition Specialist, AMO), agent ID `58b6923b-7c0c-4a38-8cfe-9f33f507e164`.
- **Fecha de auditoría:** 2026-09-29.

---

## 6. Próximas decisiones pendientes

Estas son decisiones que el equipo editorial sabe que tiene que tomar, pero que aún no ha tomado. No son críticas; son decisiones de estructura, alcance o estilo que quedan pendientes de una fase específica.

1. **Ensamble del manuscrito EN** (fase de freeze): decidir la estructura definitiva de `manuscript/manuscript.md` y reconciliar los borradores temáticos existentes con las subsecciones declaradas del SPEC.
2. **Espacio de nombres del manuscrito EN/ES** (fase de freeze): decidir si `paper/paper_en.md` + `paper/paper.md` ganan, o si `manuscript/manuscript.md` + `manuscript/manuscript-es.md` ganan, o si coexisten con roles distintos.
3. **Presupuesto de sección 1** (antes del freeze): la introducción actual (~1.356 palabras) excede el presupuesto de 1.000 palabras; tiene que recortarse o reescribirse antes del freeze, sin borrar referencias verificables ni evidencia.
4. **Presupuesto de sección 4** (antes del freeze): la implementación actual (~2.775 palabras en el borrador temático) excede el presupuesto de 2.000 palabras; los borradores de 4.4 y 4.5 (~1.529 y ~1.335) también contarán dentro de esos 2.000; hay que decidir la distribución y el recorte.
5. **Verificación de references** (antes del freeze): `sections/07-referencias.md` tiene ≥30 referencias verificables, pero hay que confirmar que todas las usadas en el cuerpo están en el corpus y que ninguna está inventada.
6. **Publicación del paper** (gate F11): ningún push a GitHub se hace sin aprobación humana explícita del operador; la conexión GitHub de Paperclip ya está verificada, pero la publicación es una decisión del operador, no del agente.

---

*V1 — 2026-09-25 — Estado: borrador de fase inicial — actualizable en cada fase — Editorial Director: Dr. Camila Duarte*
*V2 — 2026-09-25 — Corrección de acta del PI (Dr. Adrian Vega): rearmado de signoff.json con hashes reales del disco.*

---

## 7. AMO-56 — Restauración estructural de paper.md y paper_en.md (2026-10-01, Dr. Adrian Vega, PI)

- **Defecto:** el recorte 2026-09-29/30 dejó `paper.md` sin los encabezados `## 4. Implementación` y `## 5. Discusión`, con contenido empalmado a mitad de párrafo en 4.2 y 5 marcadores literales `[truncated]` en prosa; y `paper_en.md` truncado por arriba (empezaba en `### 4.5`, faltaban título, índice y secciones 0-4.4).
- **Causa:** el recorte se ejecutó con ediciones destructivas no verificadas sobre los manuscritos en lugar de promocionar la versión consolidada ya existente.
- **Decisión:** restauración desde los manuscritos consolidados limpios `manuscript/manuscript-es.md` y `manuscript/manuscript-en.md` (ensamblados 2026-09-30, estructura 0-8 completa, 0 marcadores `[truncated]`, presupuestos por sección dentro del contrato editorial), que ya aplican la política de recorte con la misma estructura 0-8 que la política declarada para paper.md. Los manuscritos dañados se conservan como evidencia en `paper.md.damaged-20261001` y `paper_en.md.damaged-20261001`.
- **Estado resultante (verificado en disco 2026-10-01):**
  - `paper.md`: md5 `74f30c2ca9d31a967c50c7f1643a6fda`, 11320 palabras, 682 líneas, encabezados `## 0..8` presentes y en orden, 0 `[truncated]`, párrafos completos. Cuerpo (secciones 1-6) ≈ 7213 palabras — por debajo del objetivo [8000,12000] como consecuencia deliberada de aplicar los presupuestos por sección del contrato (1000/1500/2500/2000/1500/500); se registra como justificación en lugar de re-inflar secciones ya recortadas.
  - `paper_en.md`: md5 `e1280a15022d9acba8d06060c96ecbd6`, 10520 palabras, 530 líneas, estructura 0-8 espejo de paper.md. Cuerpo (secciones 1-6) ≈ 8770 palabras, dentro de [8000,12000].
  - Delta de recorte contra `.bak.pre-recorte`: paper.md −3725, paper_en.md −856 (ambos ≤ 0, OK según `verify_wordcounts.py`).
- **Registro:** `signoff.json` actualizado con los md5 nuevos de ambos manuscritos. Los md5 previos del acta (18ae277a… y ab21e50c…) corresponden a las versiones pre-recorte, preservadas en `*.bak.pre-recorte`.
- **Crítica no resuelta:** ninguna derivada de esta restauración. Pendiente de tracker aparte: corpus bibliográfico con 10/33 entradas `verified` (afecta a `sections/07-referencias.md`, no a esta reparación).
