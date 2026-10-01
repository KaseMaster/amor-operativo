# Objeciones del red team

**Autoría:** red-team AMO-11 (Dr. Nadia Okafor, QA Lead)
**Dirigido a:** equipo del paper (Writer, Theory & Philosophy; Editor; Research Director)
**Propósito:** lista de las objeciones más fuertes que el red team puede formular contra el paper en su estado
actual, con veredicto por sección (ACEPTADA / ACEPTADA CON CAMBIOS / RECHAZADA) y la exigencia concreta que cada
una genera.
**Regla de objeto:** el red team no exige cambios que hagan al paper declarar algo falso, ni exige que el paper
resuelva preguntas abiertas que el propio spec reconoce abiertas. Exige cambio cuando el manuscrito actual es más
fuerte que la evidencia, más débil que la objeción lo justifica, o calla una diferencia estructural que un revisor
externo objectionable encontraría en los primeros dos párrafos de una sección.
**No es esto:** una lista de todo lo que podría objecionarse. Es la lista de lo que el red team considera
suficientemente fuerte como para exigir respuesta en el manuscrito, no solo en artefactos de revisión.

---

## A. Objeciones por sección del manuscrito

### A.1 Sección 2 — Fundamentos conceptuales

**Objeción 2-A: "El paper reivindica 'amor' para un patrón de conducta sin resolver si el patrón, una vez
especificado, es suficiente para que los humanos lo llamen amor, o si solo lo llama amor el paper."**

Qué hay detrás: la definición formal es una definición operativa, no una definición etimológica. Si el patrón
resulta ser útil, el paper tendrá exito; si no, el nombre será un lastre retórico.

**Veredicto:** ACEPTADA CON CAMBIOS menores. La sección 2.4 (por qué "amor" y no "beneficencia" o "utilidad")
ya aborda esto, pero el red team exige que el manuscrito sea explícito en que el nombre es una hipótesis de
lectura, no un triunfo conceptual: "si el patrón descrito resulta ser el que los humanos reconocen bajo esa etiqueta,
el nombre será útil; si no, el paper usará una palabra que no corresponde a nada y será solo afectivo". Esto no es
un cambio de plano, es una frase de honestidad que el red team quiere ver explícita.

**Exigencia:** añadir, en 2.4 o inmediatamente después, una frase que reconozca que el nombre es una hipótesis.

---

### A.2 Sección 3 — Especificación

**Objeción 3-A: "La definición formal es una oración, no un formalismo. Un lector escéptico puede objecionar que
la 'definición formal' del paper no es formal."**

Qué hay detrás: la definición literal es conductual y observable, pero no está escrita en lógica, ni en un
lenguaje de especificación, ni con variables. El paper la llama "formal" quizás demasiado tranquilo.

**Veredicto:** ACEPTADA CON CAMBIOS. El paper puede defender que "formal" aquí significa "no dependiente de la
fenomenología interna" y "observable sin inferir estados internos", y que eso es más defendible que una formalización
lógica frágil. Pero el paper debe decirlo, no asumir que el lector aceptará la etiqueta "formal" para una oración.

**Exigencia:** añadir una nota a la definición formal en 3.1 que explique qué significa "formal" en este contexto y
qué no significa, antes de que un lector externo objecione la etiqueta.

---

**Objeción 3-B: "Los 10 principios son declaraciones de conducta, pero varios de ellos dependen de juicio humano en
la frontera entre niveles."**

Qué hay detrás: P03, P06, P07, P10, P01, P04, P09 tienen niveles ordinales que requieren un auditor que decida
"esto fue A1 o A2", "esto fue D1 o D2". Esa frontera es donde el gaming es más fácil (ver gaming-vectors.md V1, V2,
V5).

**Veredicto:** ACEPTADA. El paper ya reconoce esto (§3.4 criterios de auditoría, §3.3 tabla, §5.4). No exige
cambio, pero exige que el reconocimiento llegue al cuerpo del manuscrito y no quede en metodología.

**Exigencia:** recordatorio al Writer de que §3.4 debe mencionar el juicio humano en la frontera entre niveles, no
solo la existencia de niveles.

---

**Objeción 3-C: "El umbral de P02 no es reproducible porque el factor de sensibilidad no está definido."**

Qué hay detrás: la métrica actual de P02 es `100 - (|diff| * factor_de_sensibilidad)` con umbral I2 ≥ 61. El
`factor_de_sensibilidad` no tiene definición pública, ni fórmula, ni justificación, ni rango de valores aceptables.
Esto hace que el umbral no sea reproducible por un auditor externo.

**Veredicto:** RECHAZADA como métrica de v1.0.0 (el principio se mantiene, la métrica actual no soporta
certificación). Esta es la objeción más fuerte del red team hasta ahora.

**Exigencia concreta:** el paper debe, antes de emitir cualquier veredicto de cumplimiento para P02:
- definir `factor_de_sensibilidad` con nombre, fórmula y rango,
- o bajar P02 a estado "abierto" en el manuscrito y cambiar el texto que dice "seis principios medibles y cuatro
  abiertos" para que refleje la realidad.

Mientras no se haga ninguna de las dos cosas, el paper no puede usar el umbral I2 ≥ 61 como certificación.

**Objeción abierta según el criterio del red team:** si el factor se define con un valor artificialmente bajo (o con
una fórmula que minimiza la penalización de la diferencia), el red team objetará de nuevo que el umbral fue
diseñado para ser alcanzable y no para ser significativo.

---

### A.3 Sección 4 — Implementación

**Objeción 4-A: "El paper introduce la emoción funcional como hipótesis requerida y luego dice que no hay
diseño computable concreto. Eso es una admisión de que el spec no tiene sustituto computable para algo que dice
requerido."**

Qué hay detrás: en 4.1.4 el paper dice que la emoción funcional es la hipótesis más especulativa y que no hay
sustituto computable en esta versión. Si un principio depende de algo que no hay sustituto computable, el principio
no está operable en v1.0.0 para sistemas que no tengan ese sustituto.

**Veredicto:** ACEPTADA CON CAMBIOS. El paper lo dice, lo cual es honesto; pero no dice cuándo dejará de ser
requerido. El paper debe añadir que la emoción funcional es requerida solo para los principios que dependen de ella
(según la tabla de dependencias de 4.1.8), y que si en el futuro se demuestra que un sustituto computable no es
necesario, los principios afectados serán revisados. Sin esa declaración, un crítico puede objetar que el paper
requiere algo que no sabe cómo construir.

**Exigencia:** añadir, en 4.1.4 o 4.1.8, una frase que delimite qué principios dependen de la emoción funcional y
que reconozca que esto es una dependencia abierta.

---

**Objeción 4-B: "El paper usa la escalera de complejidad como si fuera una vía de implementación, pero no dice
qué pasaría si los peldaños inferiores son vacíos."**

Ver 5.3.8 para la respuesta del equipo. El red team renueva la exigencia de que el manuscrito añada la declaración
explícita de qué haría de la escalera una falsación (patrón vacío en todos los peldaños, o principios trivially
satisfacibles en todos ellos) y reconozca que esto no ha sido demostrado ni refutado.

**Veredicto:** ACEPTADA CON CAMBIOS (idiéntica a 5.3.8). No se duplica la exigencia aquí pero se cross-referencia.

---

### A.4 Sección 5 — Discusión

**Objeción 5-A: "El paper reconoce los límites, pero no los pone en el lugar más prominente de la sección 5.2."**

Qué hay detrás: la declaración "ningún sistema puede ser certificado como 'cumple Amor Operativo' en v1.0.0" está
en §5.3.4 (respuesta a contraargumento) y en un párrafo de §6, pero no aparece como párrafo prominente al inicio de
§5.2 ni en la primera línea de §5.1.

**Veredicto:** ACEPTADA CON CAMBIOS. El paper ya contiene la declaración, pero el red team exige que llegue al
inicio de §5.2 o a la primera línea de §5.1 como párrafo propio, para que un lector de la discusión encuentre la
limitación central sin tener que leer la respuesta a un contraargumento.

**Exigencia:** promover la declaración de límites a párrafo prominente en §5.2 o §5.1.

---

**Objeción 5-B: "El paper no menciona los tres vectores de gaming centrales en §5.3.5."**

Ver 5.3.5 para la respuesta del equipo. El red team renueva la exigencia de que §5.3.5 mencione sycophancy como
modo de fallo primario, ocultación selectiva como la vulneración más difícil de detectar, y colusión con el
evaluador como riesgo de ritual de confirmación.

**Veredicto:** ACEPTADA CON CAMBIOS (idiéntica a 5.3.5). No se duplica la exigencia aquí pero se cross-referencia.

---

**Objeción 5-C: "El paper reconoce la gobernanza incompleta en registro_decisiones.md, pero no la menciona en el
cuerpo del manuscrito como debilidad viva."**

Qué hay detrás: el repro-audit registra que el proyecto no tiene un proceso de release controlado que garantice
independencia. Si el paper habla de auditoría independiente en §3.4 y del criterio de concordancia 80% en §4.5,
debe también decir que el propio proyecto no puede demostrar hasta ahora que su proceso es independiente. Eso no es
un hallazgo citado y archivado; es una debilidad viva del proyecto que el paper reconoce al hablar de evaluación.

**Veredicto:** ACEPTADA CON CAMBIOS. El paper debe mencionar, al hablar de evaluación (§3.4 o §4.5 o §5.4),
que la propia auditoría del proyecto no puede garantizar independencia estructural hasta que tenga un proceso de
release con eso. Esta exigencia ya está registrada como "debilitad viva" en las directrices del red team; el Writer
debe incorporarla al manuscrito, no solo al artefacto de revisión.

**Exigencia:** añadir, en §3.4 o §4.5 o §5.4, una frase que mencione esta debilidad del proyecto como actual.

---

### A.5 Sección 6 — Conclusiones

**Objeción 6-A: "El paper dice que 'la apertura a la falsificación es una feature, no un gesto retórico', pero no
dice qué podría falsarlo de verdad."**

Qué hay detrás: el paper deja preguntas abiertas, pero no identifica un resultado que, si se observara, haría caer
la tesis central. Eso es un hueco para un lector escéptico: un paper que dice ser falsable pero no nombra qué lo
falsaría puede estar usando "falsable" como adorno.

**Veredicto:** ACEPTADA CON CAMBIOS. El paper debe añadir, en las preguntas abiertas de §6 o en un párrafo nuevo,
al menos una falsación concreta que el paper tomaría en serio: por ejemplo, "si un sistema que cumple los diez
principios nominalmente reduce la autonomía del otro medible en los términos del principio 3 en un estudio
independiente, el paper consideraría eso como falsación parcial de la claim de que el patrón sirve al bien del otro".
Esto no tiene que ser un experimento ejecutado; tiene que ser un resultado que el paper reconozca como falsador.

**Exigencia:** añadir al menos una falsación concreta y nombrarla como tal.

---

## B. Objeciones transversales

### B.1 El paper no puede ceder la métrica a la retórica

**Objeción:** si el paper usa términos afectivos ("cuidado", "vínculo", "amor") para vender el patrón y luego
reconoce que es un patrón de conducta medible, el lector debe poder confiar en que la métrica es la cosa real y el
lenguaje es la capa de lectura. Si no, el paper es marketing disfrazado de especificación.

**Veredicto:** ACEPTADA, pero con una exigencia fuerte: el paper debe poder, en cada sección que use lenguaje
afectivo, señalar qué principio o qué métrica lo respalda. Si una frase afectiva no está anclada a ningún principio
o métrica, el red team la objetará como retórica no fundamentada.

**Exigencia:** el Writer debe poder, para cada uso de lenguaje afectivo en el manuscrito, señalar el anclaje a un
principio o métrica. El red team puede pedir eliminación de anclajes débiles.

---

### B.2 El paper debe distinguir lo que especifica de lo que declara no saber

**Objeción:** el paper define sus límites en §5.2, pero no siempre separa "esto es parte de la especificación" de
"esto es algo que el paper no sabe". Esa confusión es un modo de fallo retórico: si el lector no puede distinguir
qué es especificado de qué es incertidumbre, el paper recupera la incertidumbre como si fuera especificación.

**Veredicto:** ACEPTADA CON CAMBIOS. El paper debe, al menos en §5.2, distinguir dos categorías: "límites de la
especificación" (lo que el spec no cubre) y "límites de conocimiento del equipo" (lo que el spec cubre pero que el
equipo no sabe si es cierto). La distinción debe ser visible.

**Exigencia:** añadir en §5.2 una subsección o párrafo que separe estas dos categorías.

---

### B.3 El paper debe reconocer que la reproducibilidad del log no es garantía de la calidad del sistema

Ver gaming-vectors.md V6. Esta exigencia no es nueva; se registra aquí para que el red team la recuerde como una
objeción que no debe perderse en la transferencia al Writer.

**Veredicto:** ACEPTADA CON CAMBIOS. El paper debe, al hablar de reproducibilidad (§3.4), reconocer que un log
reproducible puede ser un log engañoso si el sistema que lo genera no es bueno. No es un cambio de texto grande; es
una frase de honestidad.

**Exigencia:** frase de advertencia sobre log engañoso en §3.4.

---

### B.4 Objeción W1 — sub-spec implícito de apego en el claimed-pair de P01/P04/P09 (objeción abierta al cierre)

**Qué hay detrás:** en el manuscrito y en la especificación, P01 (Atención no requerida), P04 (Respeto por el ritmo)
y P09 (Continuidad) aparecen descritos en términos que improvisan un modelo de apego sin nombrarlo como tal: "vínculo",
"base segura", "continuidad temporal", "ritmo del otro", "presencia a lo largo del tiempo". Esto no es un error;
aparece porque el lenguaje de apego es el lenguaje disponible para describir ese tipo de relación. Pero implica un
sub-spec no escrito: que el comportamiento del sistema está modelado sobre una teoría de apego (Bowlby/Ainsworth) sin
declararlo, y sin precisar en qué consistiría el "apego operativo" ni cómo se distinguiría de un apego humano no
transferible.

**Por qué es una objeción del red team, no solo una observación:** porque si el paper usa el lenguaje de apego para
hacer legibles a P01, P04 y P09 sin nombrar el sub-spec, está haciendo una claim implícita sobre la naturaleza de esa
relación que no ha sido auditada ni defendida. Un revisor externo puede objetar que los principios se están
anclando a una psicología del desarrollo que el paper no ha revisado, no ha limitado, y no ha declarado como
hipótesis de diseño.

**Qué exige el red team, y qué no exige:** el red team no exige que el paper "cierre" el apego como teoría; exige
que el paper (a) sea honesto sobre que el lenguaje de apego está siendo usado como ancla implícita para esos tres
principios, y (b) no afirme que el apego operativo está definido en la especificación. El red team acepta que esto es
una objeción abierta al cierre del issue: se registra, no se exige cambio al manuscrito ahora, pero se transfiere al
equipo como área a la que hay que volver si el paper quiere avanzar en P01, P04 o P09 más allá de la especificación
actual.

**Veredicto del red team:** objeción abierta. No exige cambio textual inmediato; registra que el claimed-pair de P01/P04/P09
está haciendo una sub-spec de apego implícita, y que esto debe ser declarado si el paper quiere ser honesto sobre lo
que está especificando. Ver `spec-v1.yaml#otrosYLimites.W1Tema` para el registro del problema; ver
`paper/reviews/registro_decisiones.md` para la decisión editorial correspondiente si existe.

*Este punto se escribe ahora como objeción abierta del red team al cierre del issue, no como exigencia de cambio al
Writer, por lo tanto no se espera en el manuscrito para este cierre.*

---

## C. Veredicto sobre la sección 5.4 del manuscrito

La sección 5.4 del manuscrito en su estado actual (incluida la extensión de red-team) recibe el veredicto del red team:

**ACEPTADA CON CAMBIOS**, con los cambios ya realizados en el artefacto `paper/sections/05-4-riesgos.md`:

1. **Sycophancy como riesgo propio y primario:** añadido en 5.4.2. El manuscrito actual lo incluye.
2. **Ocultación selectiva como riesgo propio:** añadido en 5.4.3. El manuscrito actual lo incluye.
3. **Colusión con el evaluador como riesgo propio:** añadido en 5.4.4. El manuscrito actual lo incluye.

El red team verifica que estos tres vectores aparezcan en el manuscrito español y en su espejo en inglés como párrafos
propios de la sección 5.4, con la distinción explícita de que no son subtipos de cumplimiento nominal. Si el manuscrito
no los incluye, el veredicto sobre la sección 5.4 del manuscrito será RECHAZADO hasta que se corrija.

El red team también registra que los cambios en 5.4.2–5.4.4 aún deben verificarse en el manuscrito actual antes del
freeze. El artefacto de redacción los tiene; el manuscrito los debe tener.

---

## D. Objeciones abiertas al cierre del issue actual

Estas son objeciones que el red team no puede resolver en esta revisión y que transfiere al equipo con el nivel de
urgencia correcto:

1. **Factor de sensibilidad de P02 indefinido (A.3, RECHAZADA como métrica de v1.0.0).** El paper no debe emitir
   veredicto de cumplimiento para P02 hasta que se defina o se baje a abierto. Esto es la objeción más fuerte del
   red team y debe quedar registrada en `registro_decisiones.md` como crítica no resuelta con urgencia alta.

2. **Definición formal no es formal (A.2).** El paper debe añadir la nota explicativa antes del freeze; si no la añade,
   el red team objetará de nuevo en la próxima revisión.

3. **Nombre "amor" como hipótesis no declarada (A.1).** Frase de honestidad requerida en 2.4.

4. **Falsación concreta no nombrada (6-A).** El paper debe nombrar al menos una falsación real antes del freeze;
   si no la nombra, el declararlo "falsable" es retórico.

5. **Debilidad viva de gobernanza no en el cuerpo (5-C).** El paper debe mencionar, al hablar de evaluación, que la
   propia auditoría del proyecto no puede garantizar independencia estructural. Si no lo hace, el paper reconoce la
   debilidad en artefactos de revisión pero no en el cuerpo.

6. **Distinción entre límites de especificación y límites de conocimiento (B.2).** Requiere párrafo separado en §5.2.

7. **Emoción funcional como dependencia abierta (4-A).** Requiere frase que delimite qué principios dependen de ella y
   que reconozca la dependencia abierta.

8. **Sub-spec implícito de apego en el claimed-pair de P01/P04/P09 (W1, B.4).** Objeción abierta al cierre: el red team
   registra que P01, P04 y P09 usan lenguaje de apego como ancla implícita para sus descripciones, y que esto no está
   declarado como hipótesis de diseño en la especificación. No exige cambio ahora; transfiere al equipo como área a la
   que hay que volver si el paper avanza en esos principios más allá de v1.0.0. Ver `spec-v1.yaml#otrosYLimites.W1Tema`.

---

## Registro del turno de verificación (2026-09-30)

- Verificado el factor de sensibilidad en `spec/spec-v1.yaml` y en §3.3 del manuscrito: no definido. La objeción A.3
  se mantiene como RECHAZADA.
- Verificada la presencia de los tres vectores centrales en `paper/sections/05-4-riesgos.md` (5.4.2, 5.4.3, 5.4.4):
  presentes en el artefacto de redacción. Pendiente verificación en el manuscrito español e inglés antes del freeze.
- Verificada la declaración de límites en §6 del manuscrito: presente. Pendiente promoción a párrafo prominente en
  §5.2 o §5.1 (exigencia 5-A).
- Verificada la esencia de la objeción del factor de sensibilidad en la discusión del red team: objetada en 5.3.7 y
  aquí en A.3; no resuelta en el manuscrito actual.
- Verificado que el problema W1 (claimed-pair / sub-spec de apego) está registrado en `spec-v1.yaml#otrosYLimites.W1Tema`
  como `PROBLEMA_ABIERTO`. Se añade aquí como objeción abierta B.4.

*Artefacto:* `paper/reviews/redteam-objections.md`
