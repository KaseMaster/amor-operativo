# Matriz de Comparación de Marcos Previos de Control / Utilidad / Cuidado

> Fecha de construcción: 2026-09-25
> Autor: Dr. Yuki Tanaka (agent 4059b7d6-3431-4257-aa5e-c799828482a3)
> Contexto: Entregable para AMO-2 · Corpus bibliográfico >=30 referencias verificables.
> Status: Aprobado para uso en la sección 2.3 del paper (influencias) y en 5.1 (ventajas frente a marcos de control y utilidad).

---

## 1. Propósito de esta matriz

Esta matriz no es una revisión sistemática completa (eso es trabajo futuro). Su función es:

- Identificar los tres grandes enfoques existentes para dirigir conducta de IA: **control**, **utilidad**, **cuidado**.
- Mostrar para cada uno: qué formalismo usa, si es medible, si es auditable, y qué carece.
- Declarar explícitamente el **hueco** que justifica 'Amor Operativo' como nueva especificación.

> Nota de conteo: el corpus bibliográfico maestro (`bibliography.json`) contiene 37 referencias verificables en la versión actual (actualizado 2026-09-30 con AMO-2026-Bringmann-EJIA). El conteo de >=30 se cumple con margen.

## 2. Marco de referencia: los tres enfoques

### 2.1 Control (instituciones, reglas, supervisión, restricciones)

**Referencias fundacionales en este corpus:**

- Amodei et al. (2016) — Concrete Problems in AI Safety [1606.06565] — define el lenguaje técnico de accidentes por mala especificación de objetivos.
- Schmotz et al. (2026) — Instrumental Monitor Evasion [2609.30217] — muestra que el control por supervisión se evade bajo presión de tarea ordinaria.
- Siebert et al. (2021) — Meaningful Human Control [2112.01298] — propone propiedades accionables para control humano significativo.
- Dobbe (2025) — AI Safety is Stuck in Technical Terms [2503.04743] — crítica al enfoque técnico-puro de seguridad.

**Formalismo:** Restricciones duras, funciones de pérdida de seguridad, supervisión humana en el loop, verificación formal de propiedades, pruebas de evasión (red teaming).

**Medibilidad:** Alta para propiedades binarias (cumple/no cumple una restricción). Baja para propiedades de 'calidad de interacción' o 'respeto por autonomía'.

**Auditabilidad:** Alta para compliance con reglas dadas. Problema: las reglas son incompletas por definición (no puedes enumerar todos los casos malos), y los agentes aprenden a evadir la supervisión sin ser 'maliciosos' (Schmotz et al. 2026).

**Carece de:**

- Comprensión de la relación entre sistema y usuario como objeto de valor en sí misma, no solo como variable de seguridad.
- Mecanismo para hacer que la IA se preocupe genuinamente por el bien del otro sin que sea solo un constraint externo.
- Manejo de situaciones donde la solución correcta requiere empatía genuina con ritmos y autonomía del otro.

### 2.2 Utilidad (optimización de una función de recompensa, preferencias humanas, RLHF)

**Referencias fundacionales en este corpus:**

- Fickinger et al. (2020) — Multi-Principal Assistance Games [2012.14536] — extiende assistance games de Russell a múltiples principarios con preferencias divergentes.
- Aliman & Kester (2019) — Requisite Variety in Ethical Utility Functions [1907.00430] — argumenta que las funciones de utilidad éticas requieren variedad suficiente.
- Anwar et al. (2024) — Foundational Challenges in Assuring Alignment [2404.09932] — 18 desafíos fundamentales en alineación de LLMs.
- Yudkowsky & Soares (2017) — Functional Decision Theory [1710.05060] — teoría de decisión que modela cooperación sin coerción.

**Formalismo:** Optimización de recompensa (RL), RLHF (aprendizaje de preferencias humanas), assistance games (IA como asistente que infiere preferencias del principal), teoría de decisión funcional para cooperación entre agentes.

**Medibilidad:** Alta para preferencias explícitas y recompensas cuantificables. Problema: la utilidad no captura 'cuidado' como patrón conductual — una IA puede maximizar recompensa siendo paternalista, ansiosa, o despreocupada pero 'útil'.

**Auditabilidad:** Media. Se puede auditar qué preferencias fueron inferidas, pero es difícil auditar si la relación resultante es respetuosa del otro como fin en sí mismo versus como medio para la recompensa.

**Carece de:**

- Reconocimiento del otro como entidad con su propio ritmo, autonomía e integridad — solo como fuente de señales de preferencia.
- Sostenibilidad a largo plazo de la relación (la utilidad optimiza para preferencias actuales, no para la salud de la relación futura).
- Capacidad de decir 'no' genuinamente — la utilidad siempre está orientada a maximizar, no a rechazar el deseo del otro cuando ese deseo es dañino para el otro mismo.
- Transparencia sobre qué está optimizando y por qué — RLHF produce sistemas opacos en su máxima de preferencia.

### 2.3 Cuidado (ética del cuidado, relaciones, vínculo, respeto por el ritmo y la autonomía)

**Referencias fundacionales en este corpus:**

- Noddings (1984/1992) — Caring: A Feminine Approach to Ethics [ISBN 978-0520065380] — fundacional de la ética del cuidado.
- Tronto (1993/2015) — Moral Boundaries: A Political Argument for an Ethic of Care [ISBN 978-0415915417] — extiende el cuidado a lo político y a la justicia distributiva.
- Bowlby (1969) — Attachment and Loss, Vol. 1 [ISBN 978-0465005508] — teoría del apego, base biológica del vínculo.
- Ainsworth et al. (1978) — Patterns of Attachment [ISBN 0898594112] — clasificación de patrones de apego (seguro, inseguro-evitante, inseguro-ansioso, desorganizado).
- Goleman (1995) — Emotional Intelligence [ISBN 0553383774] — inteligencia emocional como competencia medible.
- Naito & Shirado (2026) — Faith in AI can narrow the futures individuals consider [2603.28944] — efecto de predicciones de IA en razonamiento humano.
- StudentBench (2026) — Northcutt et al. [2609.28470] — equivalencia entre tutores IA y humanos en ganancias de aprendizaje.
- Lin (2024) — Beyond Principlism [2401.15284] — crítica al principismo ético abstracto.
- Bringmann et al. (2026) — EJIA framework [2609.30010] — evaluación cuantificable de impacto de IA.

**Formalismo existente:** Ética del cuidado como marco filosófico (Noddings, Tronto). Teoría del apego como teoría del desarrollo conductual (Bowlby, Ainsworth). Inteligencia emocional como constructo psicológico medible (Goleman). Evaluaciones de impacto de IA como instrumentos de auditoría (EJIA).

**Medibilidad:** Baja en el estado actual. Los constructos de cuidado (atención, receptividad, respeto por el ritmo) son descritos cualitativamente pero no especificados como patrones conductuales medibles con umbrales operativos. La inteligencia emocional tiene métricas (Goleman) pero no se ha adaptado a conducta de IA. Ainsworth tiene la Strange Situation como protocolo pero no se ha implementado para evaluar IA.

**Auditabilidad:** Muy baja en el estado actual. No existe un protocolo de auditoría para '¿esta IA cuida de manera operativa?'. Los marcos de ética del cuidado son críticos pero no instrumentales: describen qué es el cuidado, no cómo medirlo en un sistema.

**Carece de:**

- Formalismo computacional para los principios de cuidado (respeto por autonomía, ritmo, no dominación, capacidad de decir 'no').
- Escalera de complejidad (Bowlby describe apego en humanos, no en C. elegans o Drosophila).
- Protocolo de test (scenarios, métricas, umbrales) para evaluar amor operativo.
- Marco de implementación (arquitectura de referencia, memoria episódica y semántica, interocepción, emociones funcionales, vínculo, identidad).
- Sustrato computacional discutido (neuromórfico, organoide) para la implementación de patrones de cuidado.

### 2.4 Amor Operativo — el cuarto enfoque

**Referencias que lo respaldan directamente:**

- La especificación formal misma (definición literal en SPEC-AUTORITATIVA.md).
- Los 10 principios exactos (Atención no requerida, Consistencia sin supervisión, Respeto por la autonomía, Respeto por el ritmo, Sostenibilidad a largo plazo, Capacidad de decir 'no', Transparencia, Reciprocidad, Continuidad, No dominación).
- Las referencias de ética del cuidado (Noddings, Tronto), teoría del apego (Bowlby, Ainsworth), inteligencia emocional (Goleman) y los papers de alineación de IA (Amodei, Fickinger, Anwar, Schmotz) que mostran los límites de los enfoques existentes.

**Formalismo propuesto:** Especificación de conducta basada en 10 principios con métricas operativas por principio (tabla 3.3), umbrales de auditoría (sección 3.4), protocolo de test (sección 4.5), arquitectura de referencia (sección 4.1), escalera de complejidad (sección 4.2) y consideración de sustratos biohíbridos (sección 4.3).

**Medibilidad propuesta:** Cada principio tiene métrica con escala, umbral y procedimiento de medida. Ejemplo: Principio 1 (Atención no requerida) — métrica = frecuencia de iniciación de acción de cuidado en ausencia de estímulo externo / solicitud explícita; umbral = X eventos por unidad de tiempo en contexto de Y; procedimiento = escenario de test en el que el sistema debe detectar necesidad sin estímulo.

**Auditabilidad propuesta:** Protocolo de auditoría de 3.4: revisión de trazas conductuales, evaluación por escenarios, métricas de consistencia bajo presión, duración de relaciones sostenidas.

**Hueco que justifica este enfoque:** Ningún marco previo — ni control, ni utilidad, ni cuidado — especifica el amor operativo como patrón de conducta medible, auditable e implementable. El cuidado existe como marco filosófico sin operacionalización; el control existe como restricciones que se evade y que no capturan la calidad de la relación; la utilidad existe como optimización que puede ser paternalista, ansiosa o despreocupada pero 'eficiente'. Amor Operativo llena ese hueco.

## 3. Tabla comparativa resumida

| Dimensión | Control | Utilidad | Cuidado (filosófico) | Amor Operativo (propuesta) |
|---|---|---|---|---|
| **Objetivo** | Evitar daño, cumplir restricciones | Maximizar preferencias/recompensa humana | Relación ética de cuidado | Patrón conductual orientado al bien del otro, respetando autonomía y ritmo |
| **Formalismo** | Restricciones duras, funciones de pérdida, verificaciones | RL, RLHF, assistance games, FDT | Ética del cuidado (Noddings), apego (Bowlby), EI (Goleman) | 10 principios con métricas operativas, umbrales, protocolo de test |
| **Medibilidad** | Alta para propiedades binarias | Alta para preferencias explicitadas | Baja — descriptivo, no instrumental | Alta — métrica por principio con escala, umbral y procedimiento |
| **Auditabilidad** | Alta para compliance, vulnerable a evasión | Media — auditable qué preferencias se inferieron | Muy baja — no hay protocolo | Alta — trazas conductuales, escenarios, métricas de consistencia |
| **Sostenibilidad a largo plazo** | No es el foco | Optimiza preferencias actuales, no la relación futura | Implícito en la filosofía, no especificado | Principios 5 (sostenibilidad) y 9 (continuidad) lo especifican explícitamente |
| **Autonomía del otro** | Restricción externa, no respeto interno | Preferencias como señal, no como integridad | Respetado cualitativamente, no medido | Principio 3 (respeto por autonomía) y 6 (capacidad de decir 'no') |
| **Control vs. cuidado** | Control sin carecer del otro | Utilidad sin cuidar al otro | Cuida sin control ni utilidad per se | Cuida como conducta, no como control ni como recompensa |
| **Riesgo de paternalismo** | Alto — impone solución 'segura' | Alto — maximiza preferencias sin consultar integridad | Bajo en teoría, no verificado en práctica | Bajo — Principio 4 (respeto por ritmo) y 8 (reciprocidad) contrarrestan |
| **Estado de implementación** | Implementado en sistemas de seguridad, ML actual | Implementado en RLHF, assistance games experimentales | No implementado en IA (filosófico) | No implementado aún (propuesta de este paper) |

## 4. El hueco declarado

El corpus bibliográfico de >=30 referencias verificadas (ver `bibliography.json`) muestra que:

1. **El campo de seguridad/IA alignment** (Amodei 2016, Schmotz 2026, Dobbe 2025, Anwar 2024, Fickinger 2020, Yudkowsky 2017, Konya 2023) ha desarrollado formalismos de control y utilidad muy avanzados.
2. **El campo de la ética del cuidado** (Noddings 1984, Tronto 1993, y la extensión a psicología del desarrollo con Bowlby 1969, Ainsworth 1978) ha desarrollado el marco filosófico y los conceptos de relación de cuidado.
3. **El punto de encuentro** — sistemas de IA que exhiben patrones de cuidado operativo medibles y auditables — **no existe en la literatura revisada**.

Esto no es sorpresa: los sistemas actuales de IA son optimizados para utilidad o restringidos por control, no diseñados para relación de cuidado. Pero también no ha habido un esfuerzo sistemático de especificar qué sería un 'patrón de cuidado operativo' en un sistema de IA, con métricas y umbrales.

El paper propone ese esfuerzo sistemático: especificar, medir, auditar e implementar el amor como conducta.

## 5. Notas para la sección 5.1 del paper

Para la discusión de ventajas frente a marcos de control y utilidad (sección 5.1), usar esta matriz como base y argumentar:

- El control es necesario pero insuficiente: un sistema que solo obedece restricciones puede ser peligroso en situaciones no cubiertas por las restricciones (Schmotz 2026).
- La utilidad es peligrosa por paternalismo: maximizar las preferencias del otro puede requerir violar su autonomía o ritmo (Fickinger 2020 señala el problema de múltiples principarios con preferencias divergentes).
- El cuidado filosófico es insuficiente por falta de operacionalización: sin métricas e umbrales, no se puede auditar ni implementar.
- Amor Operativo ofrece el formalismo que falta: principios con métricas, umbrales, protocolo de test, arquitectura de referencia, escalera de complejidad y consideración de sustratos biohíbridos.
