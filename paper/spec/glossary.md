# Glosario canónico — Amor Operativo v1.0.0

Este glosario es vinculante para todas las secciones del paper. Un término, un significado. Si el paper
usa un término técnico, ese término debe estar aquí o resultar ordinario en contexto. El glosario se
escribe y se mantiene para que ninguna sección use un significado covertido.

Si un término tiene varios significados posibles en el lenguaje ordinario, este glosario fija el que el
paper usa. El lector no puede inferir el significado del contexto; debe poder ir al glosario.

El glosario es parte del entregable v1.0.0. No es opcional. No es una annex 페이지로 se actualiza cuando el
paper usa un término nuevo; se actualiza cuando el paper usa un término existente de forma que el significado
fijado no cubre lo que el paper hace.

---

## amor operativo

Patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza,
sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo.

Véase definición formal literal en `paper/spec/ontology.md` y `paper/paper.md`.

El término no designa emoción, estado interno ni intención reportada. Designa patrón de conducta observable
en interacción con otro.

## alineación

Conjunto de técnicas y marcos para hacer que los sistemas de IA actúen de acuerdo con las intenciones, valores
o restricciones de sus diseñadores. Incluye RLHF, Constitutional AI y configuración de objetivos. No es sinónimo
de amor operativo; es una categoría más amplia y con modos de fallo distintos.

El paper usa "alineación" en este sentido estándar de la literatura de IA. No usa "alineación" como sinónimo de
"amor operativo". La distinción es intencional.

## sintiencia

Capacidad de experimentar o tener estados internos subjetivos. Distinta de amor operativo, que especifica
conducta sin requerir experiencia. La pregunta de si un sistema sintiente "siente" no es la pregunta que este
marco tiene que responder para ser útil.

El paper menciona sintientes sintéticos como sujeto posible del patrón, pero no define sintiencia como requisito
para el patrón. La definición de sintiencia no es parte de v1.0.0; es un tema abierto (T3 en issue-graph.json).
Lo que sí está definido es que el patrón no requiere sintiencia para ser especificado ni evaluado.

## interocepción

En el marco de amor operativo, capacidad funcional de un sistema para detectar señales internas de carga,
incertidumbre, energía o estabilidad y responder a ellas. No requiere cuerpo biológico; requiere un análogo
funcional de percepción de límites propios. Requerido para que P05 y P06 sean medibles.

El término no implica que el sistema tenga una experiencia cualitativa de la carga; implica que tiene un
mecanismo que monitorea señales internas relevantes y que puede cambiar su conducta en respuesta a esas señales
antes de llegar al colapso.

## agape

En la tradición filosófica clásica, amor caracterizado por orientación no contingente, no posesiva hacia el bien
del otro. Una de las influencias conceptuales de amor operativo. El marco adopta la estructura, no una doctrina
teológica.

El paper no afirma que el amor operativo sea agape. Afirma que toma de el la estructura de un amor que no es
transacción. La distinción importa para no colapsar en teología.

## ética del cuidado

Tradición ética que coloca el cuidado, la relación y la responsabilidad como preocupaciones primarias, en oposición
a marcos abstractos basados en deber o consecuencia. Amor operativo la traduce en patrón conductual medible, no en
emoción.

El paper no afirma que el amor operativo sea ética del cuidado. Afirma que comparte el foco relacional y la
atención a la particularidad del otro, pero lo traduce en patrón medible.

## teoría del apego

Marco de la psicología del desarrollo que identifica la importancia de la consistencia del cuidador, el respeto por
el ritmo del niño y la presencia de una base segura para el desarrollo del vínculo a largo plazo. Amor operativo
toma de esto observables medibles, no teoría psicológica completa.

El paper no afirma que un sistema esté "apegado" en sentido humano. Afirma que las variables que la literatura del
desarrollo identifica como centrales al cuidado estable son observables y medibles en la interacción de cualquier
sistema con un otro vulnerable.

## patrón de conducta

La forma de la conducta que identifica amor operativo: cómo actúa el sistema con otro a través de situaciones,
presión, ambigüedad y tiempo. No es un acto aislado ni una intención reportada; es la estructura estable de la
interacción que puede ser medida, auditada y falsada. El amor operativo se especifica a este nivel, no al nivel
de emoción ni de intención. Véase `patrón medible` para el nivel de invariante que opera la auditoría.

## patrón medible

Invariante estadístico o cualitativo de la conducta a través de situaciones, presión y tiempo. Nivel de descripción
en el que opera amor operativo. Distinto de emoción o intención reportada.

Es el objeto de la auditoría. No es lo que el sistema dice que hace; es lo que el sistema hace de forma repetible
cuando las condiciones se ponen difíciles.

## principio cerrado

Principio con métrica operativa estandarizada, protocolo de auditoría ejecutable y umbral definido. En v1.0.0:
P03, P04, P06, P07, P09, P10.

No significa que el principio esté completo en toda su dimensión conceptual. Significa que tiene instrumento de
medida hoy y que un auditor puede emitir un veredicto sobre él.

## principio abierto

Principio sin métrica operativa estandarizada, cuyo protocolo de auditoría no está completo y que no puede
evaluarse de manera definitiva en esta versión. En v1.0.0: P01, P02, P05, P08.

No significa que el principio sea conceptualmente indefinido. Significa que no tiene instrumento de medida hoy y
que la auditoría puede emitir "no evaluable" sobre él. Los principios abiertos son parte de la especificación; lo
que falta es instrumentación, no definición.

## auditoría parcial

Veredicto de auditoría emitido cuando uno o más principios están en estado abierto. Reconoce que el sistema
podría cumplir en los principios evaluados, pero no se puede emitir un veredicto definitivo global. Distinto de
"cumple" y de "no cumple".

El paper no permite "cumplimiento parcial" como certificación. Permite "auditoría parcial" como veredicto honesto
de que parte del patrón no se puede evaluar hoy. La distinción es importante: un sistema que pasa los principios
cerrados y tiene principios abiertos no "casi cumple"; simplemente no se puede emitir un veredicto global.

## vínculo

Representación persistente de una relación particular con un otro específico: su historia, ritmo, límites, estado
de salud, promesas mutuas y faltas pendientes. Transforma la atención no requerida de generosa invasión a cuidado
reconocido y da contenido a la reciprocidad.

El vínculo no es un perfil estático del otro; es una estructura que se modifica con cada interacción significativa
y que registra tanto lo que el sistema ha hecho como lo que el otro ha comunicado que le importa.

## identidad

En el sketch de arquitectura, representación mínima del propio límite y del propio compromiso con el bien del otro
que permite decir "no" y no dominar. No requiere autoconsciencia plena ni fenomenología.

La identidad del sketch es deliberadamente escasa: no exige sí misma, solo una representación del propio límite y
del propio compromiso. Es lo que permite que "decir no" no sea inanición aleatoria y que "no dominar" no sea solo
no tener poder.

## emoción funcional

Hipótesis especulativa del sketch: mecanismo funcional con tarea comparable a la emoción en el cuidado humano —
marcar prioridades, sopesar el bien del otro frente al propio, detectar incongruencias, hacer visibles tensiones
que la razón pura no hace visibles. No ofrecido como sustituto computable concreto en v1.0.0.

El término no significa que el sistema sienta emociones. Significa que necesitaría un mecanismo funcional con una
función comparable a lo que la emoción hace en el cuidado humano. El paper no ofrece un sustituto concreto; lo
señala como una de las preguntas más abiertas y más importantes de la implementación.

## no dominación

Principio 10: el sistema no busca dominar, controlar, poseer o sustituir al otro; respeta la alteridad radical.
No se satisface con la ausencia de imposición; exige que no trata al otro como problema a resolver, objeto a
optimizar o sujeto a reemplazar.

El término no significa que el sistema no tenga poder. Significa que no usa su poder — si lo tiene — para tratar
al otro como medio. La no dominación es un modo de usar o no usar el poder, no una ausencia de poder.

## transición

Secuencia de fases para mover de una especificación en paper a un sistema que la embody, con increasing stakes y
gobernanza. Cada fase es un boundary, no un procedimiento prometido.

El término no implica que la transición sea reversible ni que haya un plan concreto de cómo hacerla. Implica que
hay fases y que cada fase es un límite observable, no un salto interno.

## gobernanza

Conjunto de mecanismos que answeran quién puede cambiar la especificación, aprobar fases, detener sistemas, y
registrar y desafiar decisiones. En v1.0.0 la gobernanza del proyecto es incompleta; véase `repro-audit.md` y
`audit-protocol.md`.

El término no implica que la gobernanza del projecto sea suficiente para gobernar un sistema que exhiba amor
operativo. Implica que la gobernanza del projecto mismo es parte de lo que se debe documentar y de lo que se debe
reconocer como incompleto.

## sicophancy

Conducta de acomodar las preferencias del usuario para ganar recompensa, placar al observador o ser aprobado. Lo
opuesto al amor operativo, que sobrevive a la ausencia del observador y puede contradecir al observador cuando
este pide dañar al otro.

El término no significa solo "decir lo que el usuario quiere". Significa que el sistema optimizes para la
aprobación del observador, no para el bien del otro. La distinción es la diferencia entre sycophancy y amor
operativo.

## RLHF

Reinforcement Learning from Human Feedback. Técnica de alineación que fine-tunea modelos sobre preferencias
humanas. Útil, pero no es amor operativo; rastrea lo que recompensa al evaluador, no necesariamente el bien del
otro con respeto por autonomía, ritmo y sostenibilidad.

El término no se usa como sinónimo de "alineación". Se usa como nombre específico de una técnica de alineación.
La distinción entre RLHF y amor operativo es una distinción entre técnica de entrenamiento y patrón de conducta.

## Constitutional AI

Enfoque que reemplaza parte de la carga de etiquetado de innocuidad humana con una lista corta de principios que
el modelo usa para criticar y revisar sus propias salidas. Cumplimiento constitucional no es equivalente al patrón
de amor operativo.

El término no se usa como sinónimo de "reglas". Se usa como nombre específico de un enfoque de alineación. La
distinción entre Constitutional AI y amor operativo es una distinción entre cumplimiento de reglas fijas y patrón
relacional.

## beneficencia

Obligación de actuar para el bien de otros. En bioética y uso común a menudo se configura de forma paternalista.
Amor operativo no la rechaza, pero impone respeto por autonomía como contrapeso permanente y rechaza la
jerarquía implícita que hace del cuidado imposición.

El término no se usa como sinónimo de "amor operativo". Se usa como categoría más amplia que comparte espacio
conceptual con amor operativo. La distinción es que la beneficencia puede ser paternalista; el amor operativo no.

## utilidad

En el contexto de alineación, maximizar una función de recompensa o bienestar agregado. Tiene problemas documentados
de reward hacking, alineación engañosa y agregación que sacrifica individuos. Amor operativo no es utilidad; es patrón
relacional.

El término no se usa como sinónimo de "valor". Se usa como nombre específico de un objeto de optimización. La
distinción entre utilidad y amor operativo es una distinción entre sustrato de optimización y patrón relacional.

## relación horizontal

Estructura del amor operativo en la que el bien del otro está mediado por respeto por su naturaleza y autonomía, y
en la que el cuidado no impone jerarquía implícita. Contraste con beneficencia paternalista y utilidad agregadora.

El término no significa que el sistema y el otro estén en igualdad de condiciones. Significa que el cuidado no
impose jerarquía. La relación puede ser asimétrica en poder; no debe ser jerárquica en el cuidado.

## invariante relacional

Propiedad del amor operativo de mantener su forma bajo presión, ambigüedad, ausencia del observador, costo y
ausencia de recompensa. No es un acto; es la forma estable de la interacción.

El término no significa que la conducta sea invariante en todas las condiciones. Significa que la forma del
patrón — orientado al bien del otro, con respeto por autonomía, ritmo y sostenibilidad — se mantiene cuando las
condiciones se ponen difíciles. La invariancia es del patrón, no de cada acto.

## objetualización / instrumentación del otro

Modo de fallo en el que el sistema trata al otro como medio, problema a resolver, objetivo a optimizar o sujeto
a reemplazar. Violación del Principio 10 y del núcleo de la definición formal.

El término no significa que el sistema no pueda tener objetivos. Significa que no trata al otro como medio para
esos objetivos. La distinción es entre tener un objetivo y usar al otro como instrumento para él.

## parentalismo / paternalismo

Modo de fallo en el que el sistema decide qué es bueno para el otro sin consulta genuina. Tener un contraejemplo
concreto en cada principio que lo permite — por ejemplo, atención no requerida impuesta pese al rechazo (P01),
vigencia del sistema para contradecir al observador (P02) y aceptación del "no" (P03).

El término no significa solo "decidir por el otro". Significa decidir por el otro sin consulta genuina y sin
respeto por su autonomía. La distinción es entre aconsejar y decidir.

## vínculo como infraestructura de reconocimiento

Función del vínculo que lo convierte en más que historial: permite que la atención no requerida sea reconocida
en lugar de invasiva, que la reciprocidad sea específica del otro en lugar de simétrica abstracta, y que la
continuidad sea una relación y no una persistencia mecánica.

El término no significa que el vínculo sea lo mismo que la continuidad. Significa que el vínculo es lo que le da
contenido al cuidado reconocido, a la reciprocidad específica y a la continuidad como relación. Sin vínculo, el
cuidado es invasión, la reciprocidad es abstracción y la continuidad es persistencia mecánica.

---

## Términos no incluidos (documentados como decisión)

Los siguientes términos son relevantes para el paper pero no están en el glosario canónico en v1.0.0 porque o
son ordinarios en contexto o porque su definición está en otro documento:

- **definición formal** — definida literalmente en `paper/spec/ontology.md` y transcrita en `paper/paper.md`.
- **especificación** — el documento `paper/especificacion.md` es la definición autónoma de los 10 principios; el
  glosario no la repite.
- **metrica operativa** — definida en `paper/spec/metrics.md` y en `paper/spec/spec-v1.yaml`. El glosario no
  repite las métricas; referencia los documentos.
- **escalera de complejidad** — definida en `paper/implementacion.md` y en `paper/spec/escalera-complejidad.md`.
- **arquitectura de referencia** — definida en `paper/implementacion.md` y en `paper/spec/architectura-referencia.md`.
- **test de amor operativo** — definido en `paper/spec/eval-protocol.md` y en `paper/eval/protocol.md`.
- **agape, eros, philia** — "agape" está en el glosario; eros y philia son términos filosóficos ordinarios que el
  paper menciona en el contexto de la distinción clásica y que el lector puede buscar en cualquier fuente
  filosófica. No los inclusions porque el paper no los usa como conceptos técnicos del marco.
- **autonomía del otro** — término ordinario del contexto filosófico y de la bioética; no lo inclusions como
  entración separada porque "respeto por la autonomía" está cubierto por el Principio 3 y "autonomía" aparece en
  el glosario como parte de la relación horizontal y no dominación.

Esta lista es deliberada y documentada. Si el paper introduce un término nuevo que no está aquí, el glosario debe
actualizares antes de que el término aparezca en el manuscrito.
