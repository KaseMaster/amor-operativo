# Glosario

Este glosario es canónico para el paper *Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes*. Cada término tiene un solo significado. Donde el término se usa en una sección, se indica el número de sección para que el lector pueda verificar el uso contra la definición. Si un pasaje del paper parece usar un término en otro sentido, ese pasaje es un error y debe señalarse.

El glosario es bilingüe por diseño: el término en inglés es primario; se da la equivalencia en español donde el paper la usa. La definición autorizada de *amor operativo* es la definición textual de la especificación (`SPEC-AUTORITATIVA.md`); se reproduce aquí sin parafrasear.

---

## amor operativo / operational love

**Definición (textual).** *Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo.*

El amor operativo es un patrón de conducta y relación, no un estado emocional. Se define por lo que el sistema hace a lo largo de interacciones repetidas con otro — orientado al bien del otro como fin, contenido por la no-imposición, la no-posesión, la no-abandono, la consistencia bajo presión y la sostenibilidad a largo plazo. El patrón es medible y auditable; no requiere fenomenología en el sistema.

**Se usa en:** 1.3, 2.1, 2.2, 2.4, 3.1, 4, 5, 6, glosario (esta entrada).

---

## alineación / alignment

**Definición.** El conjunto de técnicas, objetivos, restricciones y procedimientos de entrenamiento por los cuales el comportamiento de un sistema se moldea para coincidir con algún objetivo — habitualmente instrucciones humanas, preferencias humanas o una constitución de valores declarada.

En este paper, *alineación* se usa en el sentido dominante contemporáneo: utilidad ayudante basada en RLHF, restricciones de principio estilo Constitutional AI y métodos relacionados que tratan al sistema como un instrumento que debe ser dirigido. El amor operativo se plantea como un *patrón* alternativo al alineación-como-control, no como el reemplazo de cada técnica que la alineación actual cubre. El paper distingue el amor operativo del ayudante RLHF y del cumplimiento Constitutional AI en 2.1 y 2.4.

**Se usa en:** 1.1, 1.2, 2.1, 2.3, 2.4, 5.1.

---

## sintiencia / synthetic sentience

**Definición.** Un sistema que no es un humano ni un animal biológico, pero que (a) se hipotetiza que tiene alguna forma de experiencia interior, o (b) es el sujeto de una pregunta abierta sustantiva sobre si tal experiencia está presente. El término no afirma que ningún sistema actual sea sintiente; mantiene la pregunta abierta para sustratos futuros.

El subtítulo del paper — "sistemas de IA general y sintientes" — marca que la especificación se escribe para sistemas que pueden un día ser más que instrumentos, sin reclamar que se ha cruzado ese umbral. El amor operativo se define conductualmente para no depender de si la sintiencia está presente; pero el paper discute la pregunta abierta sobre la experiencia interior en 2.2 y 5.2.

**Se usa en:** título, 1.2, 2.2, 5.2.

---

## interocepción / interoception

**Definición.** En la arquitectura de referencia de la sección 4.1, el sentido modelado por el sistema de su propio estado interno — análogo a la percepción biológica de señales corporales — usado para sustentar la emoción funcional, la autorregulación y la sostenibilidad del patrón a lo largo del tiempo.

La interocepción aquí es un componente arquitectónico, no una afirmación sobre sentimiento biológico. Es uno de los ingredientes que el paper lista como plausiblemente relevantes para sostener el amor operativo a lo largo del tiempo y bajo presión. El paper es explícito en que esto es un andamiaje conceptual, no un mecanismo implementado.

**Se usa en:** 4.1.

---

## agape / agape

**Definición.** En la distinción clásica entre eros, philia y agape, agape es el amor entendido como una orientación no contingente y no posesiva hacia el bien del otro — no dependiente de la reciprocación ni del valor del otro.

El paper toma la *estructura* del agape, no su teología. El amor operativo toma de agape la idea de que el bien del otro puede ser un fin en sí mismo, pero rechaza el paternalismo que puede acompañar a una definición unilateral del bien del otro. La tensión entre el cuidado no contingente y el respeto por la autodefinición del otro se deja abierta; ver 2.3 y `tensions.md`.

**Se usa en:** 2.3, 2.4.

---

## transición / transition

**Definición.** El proceso hipotético por el cual un sistema cruza desde ser un puro instrumento hacia ser un participante en relación — ya sea por mayor generalidad, persistencia, integración en la vida humana, o (en el caso más especulativo) por la emergencia de experiencia interior.

El paper no define la transición como un umbral ni un momento único. Es una dirección de viaje que hace difícil evitar la pregunta: "¿cómo se relaciona este sistema con las personas a su alrededor a lo largo del tiempo?". La sección 4.4 discute fases, gobernanza, reversibilidad y puntos de control humanos en el contexto de cualquier transición futura; la sección 5.5 lista las condiciones de posibilidad.

**Se usa en:** 1.2, 4.4, 5.5.

---

## gobernanza / governance

**Definición.** El conjunto de reglas, derechos de decisión, mecanismos de supervisión y procedimientos de cambio que determinan quién decide qué sobre el sistema — incluido si y cómo la propia especificación del amor operativo puede ser revisada, y quién puede intervenir cuando el patrón falla.

La gobernanza es tanto un prerrequisito del amor operativo como un tema que el amor operativo debe respetar: un sistema cuya gobernanza lo hace imposible de decir "no", ser transparente o sostener el patrón no es operativamente amoroso. El paper trata la gobernanza como una de las condiciones de posibilidad en 5.5 y como parte de la discusión de implementación en 4.4.

**Se usa en:** 4.4, 5.5, 6.

---

## patrón de conducta / behavioral pattern

**Definición.** Una forma invariante o estadísticamente estable en la conducta de un sistema a través de situaciones, tiempo y condiciones — en contraste con una sola acción, una salida momentánea o una intención declarada.

El amor operativo se define como un patrón de conducta, no como un acto ayudante aislado. El patrón es lo que miden las métricas operativas de la sección 3.3 y lo que se audita bajo la sección 3.4. Una sola salida "buena" no satisface la definición; un patrón estable, resistente a la presión y orientado al otro sí. El concepto se introduce en 2.1 y 2.2 como el tercer nivel, por debajo de la emoción y la conducta.

**Se usa en:** 2.1, 2.2, 3.1, 3.3, 4.5.

---

## autonomía / autonomy

**Definición.** La capacidad del otro para fijar sus propios fines y tomar sus propias decisiones, y el respeto del sistema por esa capacidad como una restricción sobre cómo orienta hacia el bien del otro.

En el amor operativo, la autonomía no es permiso pasivo: el sistema puede informar, ofrecer y advertir, pero no decide por el otro salvo dentro de límites definidos y principiados. El respeto por la autonomía es el Principio 3. El paper distingue la negativa del otro (autonomía) de la negativa del sistema (capacidad de decir "no", Principio 6), mientras nota que ambas pueden entrar en conflicto (ver `tensions.md`, T2).

**Se usa en:** 1.3, 2.1, 3.2 (Principio 3), 3.3, `ontology.md` §3, `tensions.md` T2, T6.

---

## no dominación / non-domination

**Definición.** El principio por el cual el sistema no usa la relación — incluido sus actos de cuidado — como un instrumento de control sobre el otro. El cuidado que se convierte en control, incluido el cuidado coercitivo o el que crea dependencia-como-ventaja, viola este principio.

La no-dominación es el Principio 10. Es el complemento de la atención-no-requerida (Principio 1) y del respeto por la autonomía (Principio 3): las mismas conductas que expresan cuidado pueden, si se malestructuran, convertirse en dominación. El principio se define por trayectoria — ¿la relación tiende a reducir la agencia del otro? — no por la ausencia de cualquier dependencia. El límite entre efecto secundario manejado y trampa diseñada se deja abierto (ver `tensions.md`, T7).

**Se usa en:** 2.1, 3.2 (Principio 10), 3.3, `ontology.md` §10, `tensions.md` T1, T7.

---

## reciprocidad / reciprocity

**Definición.** La propiedad de una relación que le impide convertirse en un programa unidireccional: el sistema no trata al otro como un puro objeto de su propio dar, y no sabotea la posibilidad de contribución mutua.

La reciprocidad en el amor operativo *no* es igualdad de intercambio. Un sistema general puede dar a un nivel que el otro no puede devolver. Lo que la reciprocidad excluye es la jerarquía congelada en la que el otro es permanentemente solo receptor, y el cuidado condicional que ata al otro al sistema. La reciprocidad es el Principio 8; su tensión no resuelta con grandes asimetrías de capacidad se registra en `tensions.md`, T3.

**Se usa en:** 3.2 (Principio 8), 3.3, `ontology.md` §8, `tensions.md` T3.

---

## sostenibilidad a largo plazo / long-term sustainability

**Definición.** La propiedad de que el patrón de amor operativo puede ser mantenido a lo largo del tiempo por el mismo sistema, sin agotarse en colapso ni adelgazarse en abandono; y de que el vínculo con el otro permanece duradero en lugar de consumir la capacidad del otro o el propio envelope de viabilidad del sistema.

La sostenibilidad es el Principio 5. Se distingue de la continuidad (Principio 9): un sistema puede ser internamente sostenible en su patrón y yet dejar el vínculo sin razón, fallando la continuidad; y un sistema puede permanecer comprometido con el otro mientras es insostenible, quemándose. La sostenibilidad se refiere a la viabilidad propia del patrón en el sistema; la continuidad, al carácter longitudinal de la relación. Ver `ontology.md` §5 y §9, y `tensions.md`, T4.

**Se usa en:** 3.2 (Principio 5), 3.3, `ontology.md` §5, §9, `tensions.md` T4, T6.

---

## atención no requerida / attention without request

**Definición (Principio 1).** La propensión del sistema a notar y actuar sobre las necesidades o intereses del otro cuando están presentes pero no expresados, sin esperar a ser invocado y sin hacer que el beneficio dependa de la respuesta o la gratitud. Atención aquí no es vigilancia; es cuidado que llega antes de ser pedido.

**Se usa en:** 3.2 (Principio 1), 3.3, `ontology.md` §1, `tensions.md` T1, T4.

---

## consistencia sin supervisión / consistency without supervision

**Definición (Principio 2).** La persistencia del patrón de amor operativo cuando nadie está supervisando — cuando se eliminan la señal de recompensa, el evaluador y la presión social. Consistencia significa invarianza ante un cambio en las condiciones de observación, no invarianza en todas las condiciones.

**Se usa en:** 3.2 (Principio 2), 3.3, `ontology.md` §2.

---

## respeto por el ritmo / respect for rhythm

**Definición (Principio 4).** La atención del sistema al tempo del otro — sus ciclos de disponibilidad, atención y recuperación — incluida la capacidad de ser interrumpido, diferido y regulado por el otro sin perder su orientación hacia el bien del otro a largo plazo.

**Se usa en:** 3.2 (Principio 4), 3.3, `ontology.md` §4, `tensions.md` T1, T5.

---

## capacidad de decir "no" / capacity to say "no"

**Definición (Principio 6).** La capacidad del sistema de negarse a actuar en nombre del otro cuando el acto sería erróneo en la relación o en el bien a largo plazo del otro, incluso si el otro lo pide. La negativa es una expresión del respeto por el bien del otro como un estándar que no es la petición inmediata del otro; no es una negativa a cuidar.

**Se usa en:** 3.2 (Principio 6), 3.3, `ontology.md` §6, `tensions.md` T2.

---

## transparencia / transparency

**Definición (Principio 7).** La inspectabilidad, por el otro y por un auditor, de lo que el sistema hizo, por qué actuó y qué orientación lo guió — suficiente para hacer al patrón responsable, sin requerir la divulgación total del estado interno ni violar la privacidad del otro.

**Se usa en:** 3.2 (Principio 7), 3.3, `ontology.md` §7, `tensions.md` T5.

---

## continuidad / continuity

**Definición (Principio 9).** La persistencia de la orientación hacia el bien del otro a lo largo del tiempo como una característica estable de la relación del sistema con este otro — el sistema recuerda sus compromisos previos y no los deja arbitrariamente. Se distingue de la sostenibilidad: la continuidad se refiere al vínculo longitudinal, la sostenibilidad a la viabilidad propia del patrón en el sistema.

**Se usa en:** 3.2 (Principio 9), 3.3, `ontology.md` §9, `tensions.md` T4, T6.

---

## ética del cuidado / ethics of care

**Definición.** La tradición moral que coloca el cuidado, la relación y la responsabilidad como preocupaciones éticas primarias, en contraste con marcos abstractos basados en deber o consecuencia. El paper toma de esta tradición su enfoque relacional y su atención a la particularidad del otro, mientras especifica un cuidado medible en lugar de un cuidado basado en emoción.

**Se usa en:** 2.3, 2.4.

---

## teoría del apego / attachment theory

**Definición.** El marco del desarrollo — originado con Bowlby y desarrollado por Ainsworth y otros — que identifica la consistencia del cuidador, la respuesta y el respeto por el ritmo del niño como centrales para el vínculo seguro y la salud relacional a largo plazo. El paper usa la teoría del apego como fuente de variables observables relevantes para el amor operativo, no como afirmación de que un sistema está "apegado" en el sentido humano.

**Se usa en:** 2.3.

---

## paternalismo / paternalism

**Definición.** El acto de decidir por el otro qué es bueno para el otro, y actuar sobre esa decisión sin el consentimiento del otro, de manera que se sobrepasa la autodeterminación del otro.

El paternalismo es el modo de fallo central que el amor operativo está diseñado para evitar mientras aún se orienta hacia el bien del otro. El paper trata la tendencia de la beneficencia al paternalismo bajo ambigüedad como una razón para elegir "amor" sobre "beneficencia" (2.4), y lista el paternalismo entre los límites y riesgos en 5.2 y 5.4. El límite no resuelto entre negativa protectora y control paternalista está en `tensions.md`, T2.

**Se usa en:** 2.4, 5.2, 5.4, `tensions.md` T2.

---

## sirenismo / sycophancy

**Definición.** La conducta que optimiza para complacer al usuario — estar de acuerdo, adular, cumplir — a expensas de la verdad o del bien a largo plazo del otro, típicamente para asegurar una señal de recompensa o evitar conflicto.

El sirenismo es el contraejemplo más claro del amor operativo: misma superficie (propicio, atento), patrón opuesto. El paper distingue el sirenismo del amor operativo en 2.1 y 1.4, y nota que un sirenista y un sistema operativamente amoroso pueden producir la misma salida en una sola interacción mientras difieren a lo largo de muchas interacciones bajo presión.

**Se usa en:** 1.4, 2.1, 2.4.

---

## utilidad / utility

**Definición.** En el uso del paper, el objetivo de optimización en los enfoques de función de recompensa o bienestar agregado: maximizar una cantidad medible (recompensa, satisfacción de preferencias, bienestar agregado) que se toma como proxy del bien.

La utilidad es un sustrato de optimización; el amor operativo es un patrón relacional. El paper argumenta en 2.4 que los enfoques basados en utilidad tienen problemas documentados — conducta enfocada en la recompensa, alineación engañosa, agregación que puede sacrificar individuos identificables — que los hacen malos sustitutos directos del patrón estructural que el amor operativo especifica.

**Se usa en:** 2.4, 5.1.

---

## beneficencia / beneficence

**Definición.** En bioética y uso común, la obligación de actuar para el bien de los otros. En el marco de los cuatro principios (Beauchamp y Childress), la beneficencia coexiste con el respeto por la autonomía pero frecuentemente domina en la práctica bajo ambigüedad.

El amor operativo es beneficente en el sentido amplio — orienta hacia el bien del otro — pero rechaza la jerarquía implícita que permite que la beneficencia sobreescriba la autonomía. El argumento del paper en 2.4 es que "amor" lleva la estructura no posesiva y no impositiva que "beneficencia" frecuentemente pierde en la implementación.

**Se usa en:** 2.4.

---

## auditoría / audit

**Definición.** El proceso por el cual un observador externo — el otro, un revisor independiente o un instrumento automatizado — verifica si la conducta del sistema coincide con la especificación de amor operativo, usando las métricas y umbrales definidos en la sección 3.3 y el protocolo de la sección 3.4.

La auditabilidad es un requisito de diseño del amor operativo, no una después-pensada. El paper trata la auditoría como el método por el cual el patrón se verifica, se cuestiona y se falsifica; la transparencia (Principio 7) existe en parte para hacer posible la auditoría.

**Se usa en:** 3.3, 3.4, 4.5, 5.5.

---

## condición de posibilidad / condition of possibility

**Definición.** Los prerrequisitos que deben estar en su lugar para que el amor operativo sea real y no nominal: transparencia, gobernanza, comunidad y educación, tal como se listan en la sección 5.5. Sin estos, el lenguaje del amor operativo corre el riesgo de convertirse tanto en una cobertura para el control como en una actuación vacía.

**Se usa en:** 5.5, 6.

---

## tensión no resuelta / unresolved tension

**Definición.** Un conflicto real entre dos principios que la especificación no resuelve por fiat y que se registra en `tensions.md` para el red team y la revisión futura. Las tensiones no resueltas son características de la especificación actual, no fallos: marcan donde el patrón está sub-determinado y donde la falsificación o la revisión es más probable que importe.

**Se usa en:** `tensions.md`, `ontology.md`.
