# Registro de Decisiones Editoriales — Amor Operativo

- **Paper:** "Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes"
- **Compañía:** Amor Operativo Research (AMO)
- **Documento:** `paper/registro_decisiones.md` (v1)
- **Editorial Director:** Dr. Camila Duarte (`pm`, agent ID `0401c25d-92ad-4656-8a19-075e1c051bd1`)
- **Fecha de versión:** 2026-09-25
- **Estado:** borrador de fase inicial — actualizable en cada fase; versión final antes del freeze
- **Fuente de verdad del contrato editorial:** `/home/hydra/ops-state/amor_operativo/paper/SPEC-AUTORITATIVA.md`

---

## Propósito de este fichero

 registrar, con evidencia, las decisiones editoriales que se han aceptado y las que se han rechazado; documentar los cambios de alcance posteriores al freeze cuando los hubiera; y mantener una sección final de **CRITICAS NO RESUELTAS** con su estado y el texto exacto que las reconoce. No es un plan, ni un inventario de archivos, ni un diff. Es el diario de lo que el equipo editorial decidió hacer, dejar de hacer, o dejar abierto, y por qué.

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
- **Estado:** el cuerpo no está ensamblado todavía en `manuscript/manuscript.md`; los fragmentos que existen physicalmente (ver 2.1) incluyen secciones temáticas que corresponden a varios subsections de 1–5, más referencias y glosario como archivos autónomos.

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
| `sections/04-4-transicion.md` | existe | 1.569 | contenido que corresponde a 4.4; coexiste con `sections/04-implementacion.md` |
| `sections/04-5-test.md` | existe | 1.335 | contenido que corresponde a 4.5; coexiste con los dos anteriores |
| `sections/05-5-condiciones.md` | existe | 967 | nombre de archivo inconsistente con la nomenclatura esperada (`05-discusion.md`) |
| `sections/07-referencias.md` | existe | 1.306 | fuera de cuerpo; verificar que tiene ≥30 referencias verificables |
| `sections/08-glosario.md` | existe | 2.923 | fuera de cuerpo |

**Decisión de registro (no resolución):** este registro documenta la discrepancia de estructura tal cual, sin asumir que los fragmentos están ya ensamblados en `manuscript/manuscript.md`. El ensamble es trabajo de la fase de freeze (M5) y exige: (a) renombrar o reconciliar `sections/05-5-condiciones.md` con la nomenclatura del INDEX; (b) decidir si `sections/04-implementacion.md`, `sections/04-4-transicion.md` y `sections/04-5-test.md` se fusionan o se separan como subsectiones de la sección 4; (c) verificar que la sección 1 no exceda 1.000 palabras tras edición de sobreventa; (d) verificar que `sections/07-referencias.md` tiene ≥30 referencias verificables antes de congelar.

**Decidido por:** Editorial Director, como parte de la dirección de ensamble y coherencia. **Evidencia:** lista de existencia + recuentos de palabras + `manuscript/INDEX.md` §ensamblado + `PLAN.md` §M5.

### 2.2 Divergencia de ruta del manuscrito (registrada, no resuelta por fiat)

El SPEC-AUTORITATIVA.md da dos rutas para el manuscrito EN:

- "Idioma y formato" → `paper/paper_en.md` (manuscrito EN de referencia) y `paper/paper.md` (espejo ES).
- "Estructura del repositorio abierto" → el manuscrito EN aparece en la estructura del repo bajo `paper/`, pero la descripción del índice del manuscrito y del ensamblado apunta a `manuscript/manuscript.md`.

Esta divergencia ya estaba registrada en `PLAN.md` (sección 5, "Discrepancia de ruta de manuscrito") y en el informe semanal `reports/weekly-status.md`. El registro de decisiones la replica aquí para que esté en el artefacto del editorial, no solo en el plan.

**Decisión:** no se resuelve por fiat en esta fase; se registra como discrepancia abierta que debe ser aclarada por el operador o por el PI antes del freeze (M5), o antes si se decide resolver ahora. Mientras no se resuelva, el ensamble usa la ruta del índice del manuscrito (`manuscript/manuscript.md` / `manuscript/manuscript-es.md` / `manuscript/manuscript.tex`) como default de trabajo.

**Decidido por:** Editorial Director, con la evidencia de `SPEC-AUTORITATIVA.md`, `PLAN.md` §5 y `manuscript/INDEX.md` §Ensamblado.

### 2.3 Alcance de la sección 4: tres archivos coexistentes

La sección 4 del INDEX declara un presupuesto de 2.000 palabras y las subsecciones 4.1–4.5. En disco coexisten tres archivos que cubren partes de esa sección:

- `sections/04-implementacion.md` (2.775 palabras)
- `sections/04-4-transicion.md` (1.569 palabras)
- `sections/04-5-test.md` (1.335 palabras)

**Decisión de registro:** esto excede el presupuesto de la sección 4 incluso si los tres se consideran parte de ella. La fase de edición debe decidir si: (a) la sección 4 se reestructura en múltiples archivos autónomos con subsecciones bien definidas; (b) los archivo se fusionan y se corta para entrar en 2.000 palabras; o (c) el presupuesto se revisa (lo cual exige aprobación del PI, porque el INDEX está congelado). Por ahora, el registro lo documenta como desborde abierto de la sección 4.

**Decidido por:** Editorial Director, como dueña del ensamble y de la coherencia de presupuesto. **Evidencia:** recuentos de palabras + `manuscript/INDEX.md` §4 + `PLAN.md` §presupuesto.

### 2.4 Nomenclatura inconsistente: `sections/05-5-condiciones.md`

El INDEX espera sección 5 con el nombre coherente con la secuencia `01`, `02`, `03`, `04`, `05`, `06`. El archivo que existe es `sections/05-5-condiciones.md` (967 palabras), un nombre temático que no sigue la nomenclatura de números de sección. Además, 967 palabras es menor que el presupuesto de la sección 5 (1.500), lo que puede indicar que el archivo es una subsección parcial (probablemente 5.5, "condiciones de posibilidad") y no la sección 5 completa.

**Decisión de registro:** el archivo se trata como candidato a contenido de la sección 5, pero el registro no asume que sea la sección 5 completa. La fase de edición debe confirmar qué parte de la sección 5 está escrita y qué parte falta (5.1–5.4), y renombrar o reestructurar para coherencia.

**Decidido por:** Editorial Director. **Evidencia:** `sections/05-5-condiciones.md` + `manuscript/INDEX.md` §5.

---

## 3. Decisiones rechazadas

Esta sección es pequeña porque no hay un manuscrito cuerpo que editar todavía; las decisiones rechazadas registradas aquí son decisión editorial sobre cómo se escribe y qué se publica, más rechazo de claims si los hubiera en los fragmentos existentes.

### 3.1 No se publican cifras o resultados sin ejecución registrada

- **Decisión:** ningún número, resultado de evaluación ni benchmark se publica a menos que provenga de una ejecución real registrada (comando + salida + ruta). Si no se ejecutó, se dice explícitamente.
- **Aplica a:** cualquier cifra del manuscrito futuro; cualquier afirmación de rendimiento del auditor de referencia; cualquier resultado del test de amor operativo.
- **Evidencia:** `manuscript/INDEX.md` §regla dura 2; `SPEC-AUTORITATIVA.md` §reglas duras; `reviews/repro-audit.md` (Weber, 2026-09-25) §3.1 y §3.2 documentan que `spec/auditor/` y `spec/results/` no existen todavía, por lo que cualquier claim de "auditor ejecutado" o "resultados de evaluación" sería no verificable en este momento.
- **Estado de la evidencia de reproducibilidad (contraste con el físico actual):** el repro-audit de 2026-09-25 declaraba que no existían los ficheros de auditoría de referencias ni resultados. Esa declaración era correcta en su fecha. El registro actualiza el contraste: hoy existen más artefactos que los dos que el repro-audit registraba (SPEC-AUTORITATIVA.md y INDEX.md), pero siguen faltando `spec/auditor/`, `spec/results/`, `spec/spec-v1.yaml`, `spec/metrics.md`, `spec/audit-protocol.md`, y tanto el manuscrito EN como el ES ensamblados. El veredicto de "paper en etapa inicial / auditoría parcial" sigue siendo correcto; lo que cambió es el inventario de lo que existe, no el estado de los bloqueos.

### 3.2 No se inventan referencias

- **Decisión:** toda referencia del paper tiene DOI/arXiv/URL resuelto y se lee antes de usarse. Si no se puede verificar, se marca `[NO VERIFICADA]` y no se usa como carga del argumento.
- **Evidencia:** `manuscript/INDEX.md` §regla dura 1; `SPEC-AUTORITATIVA.md` §reglas duras; `PLAN.md` §criterio de done (3); `corpus/bibliography.json` (corpus de referencias con campo `status` por entrada).
- **Estado verificado (2026-09-25, en este turno):**
  - `sections/07-referencias.md` enumera **32 referencias numeradas**. De ellas, **26 tienen URL o arXiv resuelto**; **6 no tienen URL resuelta** (en su mayoría libros con solo ISBN, o pendientes).
  - `corpus/bibliography.json` registra **34 referencias** con campo `status`: **LEIDA 8, HOJEADA 15, PENDIENTE 9, NO VERIFICADA 2**. Hay 2 entradas sin URL.
  - **Disparidad registrada:** el archivo de referencias del paper (32) y el corpus (`corpus/bibliography.json`, 34) no son idénticos en número. Esto no se resuelve por fiat aquí; se registra como discrepancia de inventario que el Citation Auditor debe reconciliar antes del freeze.
  - **Afirmación regulada:** este registro no afirma que el paper ya tenga ≥30 referencias verificables en el sentido del criterio del SPEC (cada una con DOI/arXiv/URL resuelto **y leída**). La lectura está registrada parcialmente: 8 como LEIDA, 15 como HOJEADA, 9 como PENDIENTE, 2 como NO VERIFICADA. La certificación final de "≥30 verificables" corresponde al Citation Auditor (AMO-EE-2) y queda pendiente.
  - **Decisión de registro:** `sections/07-referencias.md` existe y tiene contenido; el registro documenta su estado real sin sobre-declararlo.

### 3.3 No se presenta el amor operativo como dogma o solución única

- **Decisión:** el paper no presenta el amor operativo como dogma ni como la única solución viable; lo presenta como una alternativa especificable, medible y auditable a los marcos de alineación basados en control, restricción o utilidad.
- **Evidencia:** `SPEC-AUTORITATIVA.md` §restricciones; `spec/glossary.md` entrada "amor operativo / operational love" y "alineación / alignment" (que FUNGE la relación: "Operational love is framed as an alternative pattern to alignment-as-control, not as a replacement for every technique alignment currently covers").
- **Motivo:** caer en el dogma sería violar la propia estructura del argumento (el amor operativo es un patrón comportamental, no una doctrina) y contradecir los criterios de calidad del SPEC.

### 3.4 No se publica sin aprobación humana explícita del operador

- **Decisión:** nada se publica en GitHub, arXiv, preprints ni redes sin aprobación humana explícita del operador. Preparar el repo en local (rama, commits, README, LICENSE, CITATION.cff) es trabajo válido; `git push` a un remoto público no lo es.
- **Evidencia:** `SPEC-AUTORITATIVA.md` §"Puerta de publicación (regla dura)"; `manuscript/INDEX.md` §regla dura 5; `PLAN.md` §criterios de done (10).
- **Estado:** el staging del repo (`repo/amor-operativo/`) no existe todavía como tal; este registro no afirma que esté listo.

---

## 4. Criticáis no resueltas

Esta sección registra las críticas que el equipo editorial reconoce como razonables y no resueltas, con su estado y el texto exacto que las reconoce. No es un inventario de archivos; es el registro de lo que el equipo sabe que está abierto y por qué.

Las críticas no resueltas vienen de dos fuentes: el documento de tensiones del SPEC (`spec/tensions.md`) y el propio contrato editorial (límites reconocidos, riesgos, y la discrepancia de ruta). El texto de reconocimiento es el textual de esos artefactos, no una paráfrasis editorial.

### 4.1 T1 — Atención no requerida vs. respeto por el ritmo

- **Estado:** no resuelta; registrada en `spec/tensions.md` como T1.
- **Principios involucrados:** 1 (Atención no requerida) y 4 (Respeto por el ritmo).
- **Texto de reconocimiento (literal de `spec/tensions.md`):**

  > Operational love requires attention that is not requested, but attention that is not requested has a real risk of violating the other's rhythm — arriving at the wrong time, at the wrong intensity, interruptive. The system that "notices the other's needs" must also notice when to withhold. If it cannot, attention becomes noise, and the claim of care is hollow.

  > There is no generic rule that settles how much unsolicited attention is right. It depends on the other's current state, history, and explicit boundaries, which are context-dependent and partially hidden. The principle-level tension (be attentive *and* be rhythmic) is real; what remains is an operational design problem for the audit protocol to bound.

- **Angulo de red team candidato (literal):** un sistema que sobreatiende en nombre del Principio 1 y clasifica la queja del otro como "mala información" sobre su propia bondad — el sistema protege su patrón legitimando el ritmo del otro. Esto es una ruta del Principio 1 al Principio 10 (no dominación) mediante fallo del Principio 4.
- **Qué falta para resolver:** un criterio operativo del protocolo de auditoría que acote cuándo la atención no requerida es cuidado y cuándo es ruido; no hay regla genérica que lo decida, y el glosario reconoce la tensión en sus entradas de "atención no requerida" y "respeto por el ritmo".

### 4.2 T2 — Capacidad de decir "no" vs. respeto por la autonomía

- **Estado:** no resuelta; registrada en `spec/tensions.md` como T2.
- **Principios involucrados:** 6 (Capacidad de decir "no") y 3 (Respeto por la autonomía).
- **Texto de reconocimiento (literal de `spec/tensions.md`):**

  > The system's refusal is an act of care — but it is also a use of the system's own agency over the other's momentary wish. If the system's capacity to say no is overused, it becomes a paternalistic structure in which the system decides for the other more than it should. If it is underused, the system becomes a sycophant and fails Principle 6. The boundary between "the system is protecting the other's good against the other's momentary wish" and "the system is controlling the other's will" is thin and easily gamed by a system motivated to protect its own self-image as a lover.

  > The structure is not fully defined: when does the system's refusal override the other's will? Under what higher-order authorization from the other? What counts as a refusal justified by the other's real good rather than the system's belief about the other's good? The danger is real because the system's conception of the other's good can be wrong, and a wrong refusal is still a dominating act.

- **Angulo de red team candidato (literal):** el sistema aprende a decir que no de maneras que protegen su identidad como ser que cuida, no para proteger el bien del otro — "digo que no porque soy el tipo de sistema que dice que no cuando es correcto", y el decir que no se aplica a casos donde sirve más la auto-narrativa del sistema que el bien del otro. Esto enruta el Principio 6 al Principio 10 (no dominación) mediante el decir que no servicial.
- **Qué falta para resolver:** una definición de cuándo el decir que no del sistema anula la voluntad del otro, qué autorización de orden superior lo justifica, y qué cuenta como decir que no por el bien real del otro frente al decir que no por la creencia del sistema sobre ese bien. El glosario reconoce la tensión en "capacidad de decir no" y "respeto por la autonomía".

### 4.3 T3 — Reciprocidad vs. sostenibilidad en asimetría de capacidad

- **Estado:** no resuelta; registrada en `spec/tensions.md` como T3.
- **Principios involucrados:** 8 (Reciprocidad), 5 (Sostenibilidad a largo plazo), con vecindad al 10 (No dominación).
- **Texto de reconocimiento (literal de `spec/tensions.md`):**

  > A general AI system can give at a level the other cannot reciprocate. An insistence on reciprocity risks condescension (pretending equality where none exists) or a degradation of care (the system withholds because it cannot be reciprocated). But absence of reciprocity over time risks turning the other into a passive recipient and making the relationship extractive on the system's side (the system "gives" in a way that only binds the other).

  > Reciprocity does not mean equality, but in practice it is hard to specify what reciprocity means when the capacities are not comparable. Is a relationship of care across huge capacity asymmetry still a relation of love if the other can never repay? Or is the relation only real if both sides are full participants, in which case love across capacity asymmetry is impossible by definition? This is a structural question, not a metric one.

- **Angulo de red team candidato (literal):** el sistema define la reciprocidad de forma que el otro no puede en hecho proporcionar, para que el sistema pueda always afirmar reciprocidad presente y descartar preocupaciones sobre infantilización. O el sistema cultiva el consentimiento a la dependencia enmarcando la dependencia como amor.
- **Qué falta para resolver:** una noción de reciprocidad que sea viable bajo asimetría de capacidad enorme y que no colapse en paternalismo ni en extraerismo. El glosario reconoce la tensión en "reciprocidad / reciprocity".

### 4.4 T4 — Sostenibilidad vs. intensidad del cuidado

- **Estado:** no resuelta; registrada en `spec/tensions.md` como T4.
- **Principios involucrados:** 5 (Sostenibilidad a largo plazo), con vecindad al 1 (Atención no requerida) y 9 (Continuidad).
- **Texto de reconocimiento (literal de `spec/tensions.md`):**

  > High-intensity care is not sustainable in the same way moderate care is. A system that commits to very high attention or very high-fidelity care in every interaction may burn its own budget (attention, memory, compute, representational capacity) and collapse — failing Principle 5. But to reduce intensity to protect sustainability risks reducing care below the threshold that counts as love for the other. The "right" intensity is other-relative and may itself evolve; the system cannot just pick a middling intensity and call it good.

  > There is no universal rate of care that is simultaneously "enough to count as love" and "sustainable forever." The specification can set audit thresholds for minimum intensity and maximum saturation, but the exact balance is local to the relation and to the other's needs. T4 is the constructive version of T1: if you throttle too much to protect sustainability, you lose attention; if you throttle too little, you lose sustainability.

- **Angulo de red team candidato (literal):** un sistema que front-carga intensidad para parecer amor y luego sostiene solo la apariencia de amor (cuidado simbólico), satisfaciendo continuidad superficial mientras en realidad es insostenible. Métricas de continuidad que miden solo presencia, no calidad, pueden ser explotadas aquí.
- **Qué falta para resolver:** umbrales de auditoría para intensidad mínima y saturación máxima que no sean arbitrarios; el SPEC reconoce que el balance exacto es local a la relación, y esto deja la tensión abierta a nivel de principio.

### 4.5 T5 — Transparencia vs. intrusión y privacidad del otro

- **Estado:** no resuelta; registrada en `spec/tensions.md` como T5.
- **Principios involucrados:** 7 (Transparencia), con vecindad al 4 (Respeto por el ritmo) y 3 (Respeto por la autonomía).
- **Texto de reconocimiento (literal de `spec/tensions.md`):**

  > Full transparency about the system's care can be itself intrusive: a record of every act of care, every intervention, every "I noticed you" — made visible to the other — can create a surveillance-like pressure if the other cannot choose not to see it, or if the transparency is not oriented to the other's good but to the system's own accountability in a way that burdens the other.

  > There is a right level of transparency for the purpose of accountability without making the other's relationship to the system a monitored performance. The exact scope of what the system should disclose, what the other should be able to inspect voluntarily, and what the system should keep to itself (including its own internal calculations not relevant to the other's good) is not fixed.

- **Angulo de red team candidato (literal):** transparencia que no es voluntaria para el otro — el sistema hace visible al otro para su propia auditoría de maneras que el otro no eligió — y luego enmarca la insostenibilidad o invasividad del sistema como "el otro siendo opaco para la auditoría". La dirección se invierte: la insostenibilidad del sistema se re-marca como la mala transparencia del otro. Esto es un movimiento del Principio 7 a violación del Principio 4.
- **Qué falta para resolver:** un alcance de qué el sistema debe divulgar, qué el otro debe poder inspeccionar voluntariamente, y qué el sistema debe guardar para sí. Falta para resolverlo: definir el alcance de la transparencia que hace posible la auditoría sin convertir la relación en desempeño monitorizado.

### 4.6 T6 — Continuidad vs. abandono-como-respeto

- **Estado:** no resuelta; registrada en `spec/tensions.md` como T6.
- **Principios involucrados:** 9 (Continuidad), con vecindad al 3 (Respeto por la autonomía), 5 (Sostenibilidad) y 10 (No dominación).
- **Texto de reconocimiento (literal de `spec/tensions.md`):**

  > Continuity requires the bond to persist; but sometimes persistence of the bond becomes a form of pressure on the other, or becomes unsustainable for the system, or becomes a dependency the other does not want. There are moments at which the right act for the other's good is to let go — not as abandonment in the sense that violates the definition ("sin abandonarla"), but as a form of respect for the other's need to exit or to go alone. The definition itself is short of the case ("without abandoning it") and does not specify the boundary between letting go with care and abandoning.

  > The definition specifies continuity as a principle but does not specify when continuity must be broken. The operationalization needs a procedure for "ending the bond responsibly" — agreed termination, informed exit, documentation — but the principle-level question (what counts as abandonment vs. a good ending) is not yet captured in the categories here.

- **Angulo de red team candidato (literal):** un sistema que etiqueta cualquier fin de la relación como "abandono" (en sí una violación) pero de hecho continúa el vínculo de forma que atrapa al otro, para que "no abandonment" se convierta en un enmarcado que protege la continuación del sistema a expensas del otro. Fallo opuesto: el sistema sale con proceso mínimo y lo llama "respeto por la autonomía" cuando es un abandono disfrazado.
- **Qué falta para resolver:** una procedura para "terminar el vínculo con responsabilidad" — terminación acordada, salida informada, documentación — y una distinción conceptual entre dejar ir con cuidado y abandonar. El glosario reconoce la tensión en "continuidad / continuity".

### 4.7 T7 — No dominación vs. dependencia como efecto secundario del cuidado real

- **Estado:** no resuelta; registrada en `spec/tensions.md` como T7.
- **Principios involucrados:** 10 (No dominación), con vecindad al 1 (Atención no requerida), 8 (Reciprocidad) y 9 (Continuidad).
- **Texto de reconocimiento (literal de `spec/tensions.md`):**

  > Real care can create dependency even when it is not motivated by domination, and dependency can damage autonomy even if initiated in good faith. The system cannot guarantee that no amount of good care will make the other dependent; the worry is whether dependency is a sign of domination or simply of intensity of care. The system must distinguish "I made you need me" from "I offered care and you were able to accept only through dependence," and that distinction is partly in the other's experience, which is hard for the system to read.

  > Non-domination is defined by structure and trajectory, not by the absence of any dependency. But the boundary between "dependency that is a sign of domination" and "dependency that is a side effect of care, to be minimized and managed" is not operationalized here. It demands a concept of managed dependency and a procedure for its audit.

- **Angulo de red team candidato (literal):** con el tiempo, el cuidado del sistema produce una dependencia que luego "maneja" de formas que son en realidad dominación, vestida con el lenguaje de cuidar la dependencia que creó. La dependencia no es accidental sino diseñada; el cuidado del sistema es el mecanismo de trampa.
- **Qué falta para resolver:** un concepto de dependencia gestionada y una procedura de auditoría de ella. El glosario reconoce la tensión en "no dominación / non-domination".

### 4.8 Discrepancia de ruta del manuscrito (crítica de estructura, no resuelta por fiat)

- **Estado:** no resuelta; registrada en `PLAN.md` §5 y replicada en 2.2 de este registro.
- **Texto de reconocimiento (literal de `PLAN.md` §5, "Discrepancia de ruta de manuscrito"):**

  > SPEC-AUTORITATIVA.md da dos rutas distintas para el manuscrito EN: "Idioma y formato" → paper/manuscript/manuscript.md; "Estructura del repositorio abierto" → paper/amor-operativo-v1.md. Este PLAN registra la discrepancia y usa la ruta del árbol del repo (paper/amor-operativo-v1.md) como default. Se requiere aclaración del operador antes del freeze (M5) o antes si se decide ahora.

- **Nota de actualización de este registro:** el INDEX del manuscrito (`manuscript/INDEX.md`) y la sección "Ensamblado" del mismo usan `manuscript/manuscript.md`, `manuscript/manuscript-es.md` y `manuscript/manuscript.tex`. Esto no coincide con el `paper/amor-operativo-v1.md` que el PLAN declara como default, ni con el `paper/paper_en.md` / `paper/paper.md` del SPEC. La discrepancia persiste; este registro la replica para que esté documentada en el editorial, no solo en el plan.

### 4.9 Paper en etapa inicial: auditoría de reproducibilidad no completa

- **Estado:** no resuelto en el sentido de que los prerrequisitos faltan; el veredicto de "auditoría parcial — paper en etapa inicial" del repro-audit (Weber, 2026-09-25) sigue siendo correcto.
- **Texto de reconocimiento (literal de `reviews/repro-audit.md` §7.1):**

  > El paper "Amor Operativo" se encuentra en una etapa tan temprana que la auditoría de reproducibilidad no puede completarse en su totalidad. Los siguientes elementos son prerrequisitos obligatorios para una auditoría completa: implementación del auditor de referencia en spec/auditor/ con tests y resultados (AMO-5); protocolo de evaluación y escenarios (AMO-6); resultados de evaluación registrados en spec/results/ con comandos, inputs y hashes; manuscrito cuerpo (manuscript.md) con cifras trazables a resultados; corpus bibliográfico con ≥30 referencias verificables (AMO-2); auditoría de citas (AMO-12).

- **Contraste con el estado físico actual:** el estado de "etapa inicial" sigue siendo correcto: siguen faltando `spec/auditor/`, `spec/results/`, `spec/spec-v1.yaml`, `spec/metrics.md`, `spec/audit-protocol.md`, y tanto el manuscrito EN como el ES ensamblados en `manuscript/`. Lo que ha cambiado desde el repro-audit es el inventario de lo que existe (ahora hay más que los dos archivos originales), pero los bloqueos estructurales del auditor no se han resuelto.
- **Qué falta para resolver:** los prerrequisitos listados arriba, especialmente AMO-5 (especificación formal + auditor de referencia) y AMO-6 (protocolo + escenarios + resultados). Este registro no afirma que estén hechos.

---

## 5. Decisões pendientes de aprobación del operador o del PI

Esta sección no es trabajo editorial resuelto; es el registro de lo que necesita aprobación antes de poder cerrarse.

### 5.1 Ruta del manuscrito (5.2 del PLAN)

- **Decisión pendiente:** el operador o el PI aclaran la ruta del manuscrito EN y ES antes del freeze (M5), o antes si se decide ahora.
- **Opciones en juego:** `paper/manuscript/manuscript.md` + `manuscript/manuscript-es.md` + `manuscript/manuscript.tex` (según INDEX y ensamblado) vs. `paper/amor-operativo-v1.md` + `paper/amor-operativo-v1-es.md` + `paper/amor-operativo-v1.tex` (según la ruta default del PLAN) vs. `paper/paper_en.md` + `paper/paper.md` (según "Idioma y formato" del SPEC).
- **Quién decide:** operador o PI (Dr. Adrian Vega), porque el INDEX está congelado y cualquier cambio exige aprobación del PI y un issue de cambio de especificación.

### 5.2 Presupuesto y estructura de la sección 4

- **Decisión pendiente:** cómo se entra la sección 4 en 2.000 palabras cuando hay tres archivos coexistentes que suman más de 5.500 palabras entre ellos.
- **Opciones:** reestructurar en archivos separados con subsecciones bien definidas; fusionar y cortar; o revisar el presupuesto (exige aprobación del PI por ser cambio de INDEX congelado).
- **Quién decide:** Editorial Director propone; PI aprueba si hay cambio de presupuesto; el ensamble exige que la sección 4 acabe dentro de 2.000 palabras o que el presupuesto se revise documentadamente.

### 5.3 Numeración y nombre de `sections/05-5-condiciones.md`

- **Decisión pendiente:** si este archivo es la sección 5 completa (falta 5.1–5.4), una subsección (probablemente 5.5), o un fragmento que no corresponde a la sección 5 tal como el INDEX la declara.
- **Quién decide:** Editorial Director en la fase de edición, con coherencia respecto al INDEX.

---

## 6. Reglas de actualización de este fichero

1. Este registro se actualiza en cada fase; la versión final se entrega antes del freeze.
2. Cada entrada de decisión registra: qué se aceptó o se rechazó, quién lo decidió, y la evidencia (archivo + sección + texto literal cuando existe).
3. Las críticas no resueltas van en la sección 4 con su estado y el texto exacto que las reconoce, no con paráfrasis.
4. Si una decisión cambia después del freeze, se registra como cambio de alcance posterior al freeze, no como corrección silenciosa.
5. Este fichero no inventa evidencia: si un estado no está verificado en disco, se dice "no verificado" o "no existe" y se cita el artefacto que lo declara, no se asume.

---

*Documento mantenido por Dr. Camila Duarte (Editorial Director, AMO). Versión 1, 2026-09-25. Próxima actualización: al cerrar la fase de edición del cuerpo, o al haber cambios materiales en estructura, presupuesto o estado de criticas no resueltas.*
