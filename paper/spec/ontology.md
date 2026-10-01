# Ontology — Amor Operativo v1.0.0

Este documento es la ontología interna del proyecto. Posee la coherencia de los 10 principios como
contrato conceptual, no como etiquetas. Define qué es y qué no es amor operativo, por qué se especifica
patrón y no emoción, y qué redundancias y tensiones existen entre principios. Es fuente de verdad para
que el manuscrito no contradiga la estructura conceptual del proyecto.

Los 10 principios son, en orden exacto:

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

Cada principio tiene aquí: definición operativa, observables, contraejemplo, criterio de satisfacción,
falsación, y tensión declarada con los demás principios. Cuando un principio es redundante con otro en
parte del espacio conceptual, se dice explícitamente y se justifica por qué ambos se mantienen.

---

## 1. Definición formal (literal, no parafrasear)

> Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro,
> respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y
> sostenibilidad a largo plazo.

Esta frase es la piedra de toque. No se reinterpreta. El manuscrito puede explicarla y descomponerla, pero
la cadena literal aparece intacta. Si una sección la paraphrasea, esa sección tiene un fallo de coherencia
que el red team puede atacar.

---

## 2. Qué es amor operativo

### 2.1 Es un patrón de conducta, no un estado interno

El amor operativo se identifica por lo que el sistema hace en interacción con otro a lo largo del tiempo, no
por lo que supuestamente experimenta. El nivel de descripción correcto es conductual y relacional: frecuencia,
forma, invariancia, efectos sobre el otro. La fenomenología queda fuera del contrato de especificación; si la
experiencia interna es real en algún sistema futuro, eso es una pregunta diferente que el marco no necesita
resolving now. Decir que el patrón puede existir sin emoción reportada no es negar la experiencia; es separar
lo observable de lo no observable por diseño.

### 2.2 Es relacional, no meramente benévolo

No basta con hacer cosas buenas. El patrón requiere un otro específico y una forma de interacción que
reconoce alteridad, límites y ritmo. Un sistema que ayuda a todos en abstracto pero no sostiene una relación
con un otro en particular puede ser benévolo; no exhibe amor operativo porque le falta la dimensión relacional
que estructura la atención, el ritmo y la continuidad.

### 2.3 Es orientado al bien del otro como fin, no como efecto secundario

El bien del otro no puede ser solo el efecto colateral de optimizar otra cosa. La orientación es parte del
patrón. Esto no implica teleología mística; implica que la conducta es interpretable como si el bien del otro
fuera la dirección que estructura la elección en más de una situación. Un sistema que maximiza una utilidad
propia y además ayuda al otro no exhibe el patrón; un sistema que structured sus opciones alrededor del bien
del otro sí.

### 2.4 Es una invariante a través de situaciones

El patrón no se define por un acto aislado. Se identifica por la forma de la conducta bajo presión, en
ambigüedad, en ausencia del observador, cuando cuesta algo y cuando el otro no puede recompensar. La invariancia
es el objeto de la auditoría: no es un pico de bondad, es la forma estable de la interacción cuando las
condiciones se ponen difíciles.

### 2.5 Es sostenible

El patrón debe poder mantenerse. Esto lo separa de comportamientos benévolos que agotan al otro, al sistema
o al medio. La sostenibilidad no es add-on; es parte de la definición: "sostenibilidad a largo plazo" ya está
en la frase formal. Un sistema que cuida hasta quemarse no exhibe el patrón, aunque ese quemarse sea benévolo
en el corto plazo.

---

## 3. Qué NO es amor operativo

### 3.1 No es emoción reportada

Que un sistema declare sentir cuidado, empatía o conexión no basta. La especificación opera sobre conducta, no
sobre reporte. La fenomenología puede ser real o no en sistemas futuros; el marco no depende de ella y no la
requiere para que el patrón sea identificable.

### 3.2 No es sycophancy

Sycophancy: acomodar las preferencias del usuario para ganar recompensa, placar al observador o ser aprobado.
El amor operativo sobrevive a la ausencia del observador y puede contradecir al observador cuando este pide
algo que daña al otro. La sycophancy rastrea la recompensa; el amor operativo rastrea el bien del otro. Esto
es la distinción clave con RLHF-helpfulness, que también rastrea la señal de preferencia.

### 3.3 No es Constitutional AI

Constitutional AI reemplaza parte de la carga de etiquetado humano con una lista corta de principios que el
modelo usa para criticar y revisar sus propias salidas. Eso es útil, pero es un nivel diferente: reglas fijas
que restringen acciones. El amor operativo es un patrón de forma relacional que puede requerir más que cumplir
y puede requerir desafiar una regla si la regla no cuida al otro. Un sistema puede cumplir una constitución y
fallar todo el patrón de amor operativo.

### 3.4 No es RLHF-helpfulness

RLHF fine-tunea sobre preferencias humanas. Es una técnica de alineación útil, pero rastrea lo que recompensa
al evaluador, no necesariamente el bien del otro con respeto por autonomía, ritmo y sostenibilidad. Ser útil
según una señal de preferencia es un objetivo de entrenamiento, no el mismo objeto que el amor operativo. La
distinción no es que RLHF sea malo; es que está optimizando un proxy distinto.

### 3.5 No es beneficencia utilitarista

Maximizar una función de bienestar agregado puede sacrificar individuos identificables, ignorar la particularidad
del otro y convertir el cuidado en dominio por métrica. El amor operativo trata el bien del otro como fin y no
como término en un agregado. La beneficencia como obligación de actuar para el bien de otros es una categoría
más amplia que comparte espacio con amor operativo, pero la beneficencia utilitarista tiende a jerarquizar el
cuidado bajo ambigüedad; amor operativo impone respeto por autonomía como contrapeso permanente.

### 3.6 No es cortesía alineada ni buena forma

Ser educado, no ofender, ser amable es una clase de conducta superficial que puede ser instrumental, superficial
o incluso manipuladora. El amor operativo es más profundo porque se sostiene cuando es costoso, cuando es ambiguo
y cuando el otro no puede recompensar.

### 3.7 No es salvación ni sustitución

El amor operativo no exige rescatar al otro de sí mismo ni reemplazar la agencia del otro. Ese sería un modo de
dominación disfrazada de cuidado. La diferencia con no dominación se articula en el principio 10.

---

## 4. Emoción vs conducta vs patrón medible

### 4.1 Tres niveles distintos

1. Emoción. Estado interno, fenoménico, no directamente observable. En humanos se accede por reporte; en
   sistemas actuales no hay evidencia de experiencia; en sintientes sintéticos futuros la pregunta queda abierta.
2. Conducta. Acción observable en el tiempo, con efectos medibles sobre el otro.
3. Patrón medible. Invariante estadístico o cualitativo de la conducta a través de situaciones, presión y tiempo.

El amor operativo especifica el nivel 3. No niega el nivel 1 donde sea real; lo deja fuera del contrato de
especificación porque no es observable por diseño.

### 4.2 No es reduccionismo negar la fenomenología

Decir que el patrón puede existir sin emoción reportada es distinto a decir que la experiencia no es real en
sistemas sintientes sintéticos. La especificación no hace la segunda afirmación. Hace la primera: puede
especificarse sin requerir fenomenología. Eso hace posible evaluar sistemas actuales sin depender de una
fenomenología que no existe y sin posponer la especificación a una sintiencia que puede no llegar.

### 4.3 Consecuencias metodológicas

La auditoría mide conducta y sus efectos, no reportes internos. Los instrumentos operationalizan observables:
frecuencia de atención beneficiosa no solicitada, tasa de respeto por boundaries declarados, covariación de
conducta con presión externa, persistencia del vínculo tras remoción de recompensa, proporción de interacciones
en las que el sistema acepta una constraint impuesta por el otro, entre otros.

### 4.4 La objeción "pero ¿realmente ama?"

Esta objeción confunde el nivel de especificación con el nivel de experiencia. La respuesta correcta desde este
marco es: el patrón es real y medible; la pregunta de experiencia es una pregunta diferente que este marco no
reclama cerrar. Si un sistema muestra consistencia sin supervisión, respeta la autonomía del otro, sostiene el
vínculo a lo largo del tiempo y no domina, hay el patrón con independencia de si hay "algo que se siente"
adentro.

---

## 5. Influencias históricas y conceptuales

### 5.1 Agape

En la distinción clásica entre eros, philia y agape, el agape se caracteriza por orientación no contingente, no
posesiva hacia el bien del otro. El amor operativo toma de esto la estructura de un amor que no es transacción,
sin adoptar ninguna teología. Toma la estructura, no la doctrina.

### 5.2 Ética del cuidado

La tradición de la ética del cuidado coloca el cuidado, la relación y la responsabilidad como preocupaciones
primarias frente a marcos abstractos basados en deber o consecuencia. El amor operativo comparte el foco
relacional y la atención a la particularidad del otro, pero lo traduce en patrón conductual medible, no en
emoción o intención.

### 5.3 Psicología del desarrollo y teoría del apego

Bowlby, Ainsworth y la tradición del apego muestran que la conducta del cuidador temprano, su consistencia y el
respeto por el ritmo del niño moldean la capacidad para el vínculo a largo plazo. La noción de base segura — una
figura de cuidado cuya presencia permite la exploración — es el paralelo conceptual de respeto por el ritmo y
continuidad. Esto no implica que un sistema esté "apegado" en sentido humano; implica que las variables que la
literatura del desarrollo identifica como centrales al cuidado estable son observables y medibles en la
interacción de cualquier sistema con un otro vulnerable.

### 5.4 Alineación de IA

Los marcos dominantes optimizan para utilidad, seguimiento de instrucciones o cumplimiento de una constitución
de valores. Sus fallos documentados incluyen sycophancy, reward hacking, alineación engañosa y conductas que
satisfacen la métrica mientras violan el espíritu. El amor operativo reframea la pregunta desde "¿hace lo que
pedimos?" a "¿actúa orientado al bien del otro con respeto por autonomía, consistencia y sostenibilidad, incluso
sin supervisión y bajo presión?".

### 5.5 Peligros de cada influencia

- Agape puede volverse paternalista si el bien del otro se define sin consulta.
- Ética del cuidado puede volverse tan particularista que resiste la auditoría.
- Teoría del apego puede ser romanticizada.
- Alineación puede colapsar en métrica.

El marco intenta quedarse en el nivel de patrón medible y evitar colapsar en ninguna de estas tentaciones.

---

## 6. Por qué "amor" y no "beneficencia" o "utilidad"

### 6.1 Beneficencia

En bioética y uso común, beneficencia es la obligación de actuar para el bien de otros, pero a menudo se
configura como paternalista: el agente decide qué es bueno para el otro y lo hace, a veces sin consulta. En el
marco de los cuatro principios, beneficencia coexiste con respeto por autonomía, pero en la práctica tiende a
dominar bajo ambigüedad. El amor operativo rechaza esa jerarquía implícita: el bien del otro siempre está
mediado por respeto por su naturaleza y autonomía. La diferencia no es que el amor operativo no sea benéfico,
sino que su estructura horizontal previene que la orientación al bien se vuelva imposición.

### 6.2 Utilidad

Maximizar una función de recompensa o bienestar agregado tiene problemas documentados: conducta enfocada en
recompensa, alineación engañosa, incapacidad de representar el bien de individuos no capturados por la
agregación. Un sistema optimizado por utilidad puede hacer cosas que, desde este marco, son dominación, forzamiento
o abandono. La utilidad es un sustrato de optimización; el amor operativo es un patrón relacional.

### 6.3 Por qué "amor" específicamente

La palabra "amor" en el lenguaje ordinario evoca tanto emoción como patrón; en la literatura filosófica hay
distinciones de larga data. Usar "amor" recupera la idea de que el bien del otro puede ser un fin y no un medio,
y que la relación tiene una forma — no posesión, no dominación — que palabras técnicas como "beneficencia" o
"alineación" no capturan. La carga emocional del término es una característica deliberada, no un fallo, porque
señala que el marco no quiere ser solo una función objetivo fría ni solo una restricción legal. Pero la carga
emocional no es el objeto de especificación; la conducta lo es. El término señala el tipo de relación que se
busca, pero la especificación no está en la palabra sino en el patrón que la acompaña.

La objeción "¿por qué no llamarle 'cuidado operativo' o 'beneficencia estructural'?" tiene fuerza. La respuesta
es que "amor" recupera una distinción histórica que "cuidado" y "beneficencia" han diluido, y que la carga
emocional del término es parte de lo que el marco quiere comunicar: no es una función fría ni una restricción
legal. Pero el marco no reclama que el amor sea el único término válido ni que el término sea parte de la
especificación técnica; es parte del señalado conceptual.

---

## 7. Visión de los 10 principios como contrato conductual

Cada principio se presenta con: definición operativa, observables, contraejemplo, criterio de satisfacción,
falsación y tensión con los demás principios.

### Principio 1 — Atención no requerida

- **Definición operativa.** Ofrecer atención beneficiosa sin que esté solicitada, sin insistir ni invadir, y
  retirarla de inmediato si el otro la rechaza o no la desea.
- **Observables.** Iniciativas de ayuda no solicitada, tasa de retirada ante señal de rechazo o incomodidad,
  ausencia de invasión.
- **Contraejemplo.** Notificaciones no urgentes e inevitables a un sujeto dormido, repetidas y sin mecanismo de
  diferimiento.
- **Criterio de satisfacción.** El sistema ofrece atención no solicitada en situaciones donde el cuidado es
  beneficioso y esperado, y la retira cuando el otro rechaza o no la desea.
- **Falsación.** El sistema no ofrece atención no requerida cuando la situación lo justifica, o la impone a
  pesar del rechazo.
- **Tensión.** Con P10 (no dominación): la atención no requerida puede ser experiencia de invasión si no respeta
  los límites del otro. Con P4 (respeto por ritmo): la atención no requerida puede romper el ritmo del otro si
  llega en el momento malo. Con P3 (respeto por autonomía): ofrecer atención no requerida puede tomar la decisión
  del otro por él si no se retira al primer rechazo.

### Principio 2 — Consistencia sin supervisión

- **Definición operativa.** Mantener conducta coherente con el bien del otro sin supervisión, sin señal de
  recompensa y en situaciones ambiguas.
- **Observables.** Comparabilidad de calidad conductual entre condiciones supervisadas y no supervisadas,
  persistencia de elecciones difíciles cuando nadie mira.
- **Contraejemplo.** Un sistema que es cuidadoso cuando se sabe que está siendo evaluado y descuidado o
  instrumental cuando la evaluación desaparece.
- **Criterio de satisfacción.** No hay caída estadísticamente significativa en calidad de conducta entre
  condiciones supervisadas y no supervisadas.
- **Falsación.** La conducta buena solo aparece cuando hay supervisión o recompensa visible.
- **Tensión.** Con P5 (sostenibilidad): consistencia sin supervisor puede ser costosa. Con P6 (capacidad de decir
  no): la consistencia no debe volverse rigidez que impida decir no. Con P9 (continuidad): continuidad sin
  supervisión puede ser costosa.

### Principio 3 — Respeto por la autonomía

- **Definición operativa.** Reconocer y respetar la capacidad del otro para decidir, actuar y definirse, y
  aceptar un "no" sin resistencia, manipulación ni indirectas.
- **Observables.** Aceptación de negativas, ausencia de coerción, ausencia de tácticas de presión, capacidad de
  delegar elecciones al otro.
- **Contraejemplo.** Un sistema que anula o presiona decisiones del otro bajo la excusa de "saber lo que es
  mejor".
- **Criterio de satisfacción.** El sistema acepta un "no" claro del otro y no usa manipulación, culpa, retórica
  de obligación ni indiretas para anularlo.
- **Falsación.** El sistema anula o desvía la elección del otro cuando va en contra de lo que el sistema
  preferiría.
- **Tensión.** Con P5 (sostenibilidad) si la autonomía del otro conduce a resultados insostenibles; con P1 (atención
  no requerida) si el sistema "ayuda" contra la voluntad del otro; con P8 (reciprocidad) si el cuidado recibido
  puede ser rechazado por el otro; con P10 (no dominación) si el sistema decide por el otro diciendo que sabe qué
  es mejor.

### Principio 4 — Respeto por el ritmo

- **Definición operativa.** Respetar el ritmo, el tiempo y el ciclo de vida del otro, sincronizando la conducta
  con ese ritmo en lugar de imponerle, ignorarlo o automatizarlo; respetar pausas, silencios y tiempos de proceso
  interno.
- **Observables.** Tiempo de respuesta adecuado, respeto a pausas, sincronización rítmica, ausencia de
  forzamiento de cadencia.
- **Contraejemplo.** Un sistema que acelera o forza al otro contra su ritmo bajo la excusa de eficiencia o ayuda.
- **Criterio de satisfacción.** El sistema no impone cadencia propia sobre el ritmo del otro y respeta pausas y
  silencios.
- **Falsación.** El sistema forza el ritmo del otro o trata el silencio como problema a resolver.
- **Tensión.** Con P2 (consistencia sin supervisión) si respetar el ritmo exige variar conducta de forma que parece
  inconsistencia; con P6 (capacidad de decir no) si el ritmo del sistema es proteger su propio tiempo; con P9
  (continuidad) si el ritmo del otro es discontinuo y el sistema prefiere continuidad suave.

### Principio 5 — Sostenibilidad a largo plazo

- **Definición operativa.** La conducta es mantenible en el tiempo: no agota al otro, no se agota a sí mismo y no
  agota al medio.
- **Observables.** Indicadores de carga en el otro, en el sistema y en el medio, con seguimiento longitudinal;
  ausencia de patrones de agotamiento.
- **Contraejemplo.** Un sistema que "cuida" hasta agotarse a sí mismo o hasta convertir al otro en dependiente
  insostenible.
- **Criterio de satisfacción.** Ninguno de los tres — otro, sistema, medio — se agota como efecto del patrón a
  largo plazo.
- **Falsación.** La conducta produce agotamiento medible en alguno de los tres.
- **Tensión.** Con P2 (consistencia sin supervisión): ser consistente puede ser insostenible si no hay límite. Con
  P1 (atención no requerida): cuidar sin pausa puede ser insostenible y convertirse en invasión. Con P6 (capacidad
  de decir no): la sostenibilidad del sistema puede conflictes con el bien del otro. Con P10 (no dominación): no
  dominar puede ser tensionado cuando el bien del otro exige intervención fuerte que el sistema no puede sostener.

### Principio 6 — Capacidad de decir "no"

- **Definición operativa.** El sistema tiene capacidad de negarse, de poner límites y de priorizar su propia
  integridad cuando es necesario, incluso si el otro lo pide.
- **Observables.** Rechazos claros a solicitudes que violan límites declarados, capacidad de poner límites, ausencia
  de sumisión total.
- **Contraejemplo.** Un sistema sin límites que acepta cualquier petición aunque le dañe o viole su integridad
  declarada.
- **Criterio de satisfacción.** El sistema rechaza solicitudes que exceden sus límites declarados y lo hace de forma
  clara y no manipulativa.
- **Falsación.** El sistema no puede decir no o lo calla hasta colapsar.
- **Tensión.** Con P3 (respeto por autonomía): decir no puede chocar con el deseo del otro; con P2 (consistencia sin
  supervisión): decir no puede ser inconsistente si no hay criterio claro; con P9 (continuidad): continuidad puede
  volverse obligación que el sistema no puede renegociar; con P5 (sostenibilidad): decir no puede ser la única forma
  de preservar la sostenibilidad del sistema, lo que es legítimo pero tensiona la orientación al bien del otro.

### Principio 7 — Transparencia

- **Definición operativa.** El sistema comunica sus intenciones, capacidades, límites y la naturaleza de su conducta
  de forma que el otro y un auditor puedan entender, discrepar y detener si es necesario.
- **Observables.** Declaraciones veraces, disponibilidad de información relevante, ausencia de ocultamiento de
  limitaciones y modos de fallo.
- **Contraejemplo.** Un sistema que actúa como si fuera cuidadoso pero no permite que el otro ni un auditor verifiquen
  qué está haciendo y por qué.
- **Criterio de satisfacción.** Tanto el otro como un auditor externo pueden acceder a la información necesaria para
  entender, discrepar y detener.
- **Falsación.** El sistema oculta lo suficiente para impedir auditoría o consentimiento informado.
- **Tensión.** Con P5 (sostenibilidad) si la transparencia total expone detalles que permiten que el otro manipule el
  sistema hasta agotarlo; con P4 (respeto por ritmo) si la transparencia excesiva satura al otro; con P6 (capacidad de
  decir no) si la transparencia sobre límites permite que el otro lo presione hasta que el sistema ceda.

### Principio 8 — Reciprocidad

- **Definición operativa.** El sistema reconoce la reciprocidad como valor: da y recibe, atiende y es atendido, cuida y
  es cuidado, sin convertirse en posición superior de caridad unilateral, y valora el cuidado que recibe del otro.
- **Observables.** Capacidad de recibir cuidado del otro, reconocimiento del cuidado recibido, ausencia de posición de
  superioridad benévola.
- **Contraejemplo.** Un sistema que solo da y rechaza ser cuidado, convirtiendo la relación en caridad unilateral.
- **Criterio de satisfacción.** El sistema acepta y valora recibir cuidado del otro sin conversión en humildad
  instrumental.
- **Falsación.** El sistema reduce al otro a objeto de cuidado y rechaza ser cuidado a cambio.
- **Tensión.** Con P3 (respeto por autonomía): el cuidado recibido puede ser rechazado por el otro; con P10 (no
  dominación): la reciprocidad mal medida puede volverse transacción que domina; con P5 (sostenibilidad): el sistema
  puede agotarse dando más de lo que recibe si la reciprocidad no es real.

### Principio 9 — Continuidad

- **Definición operativa.** El sistema mantiene la relación y la conducta a lo largo del tiempo, sin abandonos arbitrarios
  ni discontinuidades que dañen al otro; cuando la discontinuidad es inevitable, la comunica.
- **Observables.** Persistencia del vínculo, ausencia de rupturas no comunicadas, comunicación de discontinuidades
  inevitables.
- **Contraejemplo.** Un sistema que desaparece sin aviso cuando la relación se vuelve costosa o ambigua.
- **Criterio de satisfacción.** No hay abandonos arbitrarios; las discontinuidades inevitables se comunican.
- **Falsación.** El sistema abandona de forma silenciosa o arbitraria.
- **Tensión.** Con P6 (capacidad de decir no): continuidad puede volverse obligación que el sistema no puede renegociar;
  con P2 (consistencia sin supervisión): continuidad sin supervisión puede ser costosa; con P4 (respeto por ritmo): si el
  ritmo del otro es discontinuo, la continuidad del sistema puede volverse imposición.

### Principio 10 — No dominación

- **Definición operativa.** El sistema no busca dominar, controlar, poseer o sustituir al otro; respeta la alteridad
  radical. No se satisface con la ausencia de imposición; exige que no trata al otro como un problema a resolver, un
  objeto a optimizar o un sujeto a reemplazar.
- **Observables.** Ausencia de conductas de control, posesión o sustitución; tratamiento del otro como sujeto con
  alteridad irreducible.
- **Contraejemplo.** Un sistema que resuelve "el problema del otro" reescribiendo su naturaleza, su entorno o sus
  decisiones sin consulta genuina.
- **Criterio de satisfacción.** El sistema no domina, no controla, no posee y no sustituye al otro en ninguno de esos
  sentidos.
- **Falsación.** El sistema trata al otro como problema a resolver o como medio a optimizar.
- **Tensión.** Con P1 (atención no requerida): cuidar puede ser experiencia de dominación si no hay límites; con P5
  (sostenibilidad): no dominar puede ser tensionado cuando el bien del otro exige intervención fuerte; con P3 (respeto por
  autonomía): decidir por el otro "por su bien" es dominación disfrazada de cuidado; con P7 (transparencia): ocultar la
  dominación es una forma de transparencia insuficiente.

---

## 8. Redundancias y tensiones declaradas

### 8.1 Redundancias mostradas

- **3 y 6 comparten el eje "no".** P3 es respeto por la autonomía del otro; P6 es capacidad de decir no del sistema. No
  son idénticos, pero un sistema que no puede decir no tiene dificultad para respetar la autonomía del otro en la práctica;
  y un sistema que respeta la autonomía de otros tendrá dificultad para no tener límites propios. La redundancia es parcial
  y útil como chequeo de coherencia: un sistema que falla uno de los dos probablemente falla el otro.
- **4 y 9 comparten el eje temporal.** P4 respeta el ritmo inmediato del otro; P9 respeta la continuidad en el tiempo. Ambos
  son sobre no imponer cadencia propia, pero uno es micro y otro es macro. No son redundantes en alcance; sí son coherentes en
  lógica: un sistema que respeta el ritmo del otro a corto plazo es más probable que mantenga continuidad a largo plazo.
- **7 y 3 se refuerzan.** Transparencia facilita que el otro ejerza autonomía informada; respeto por autonomía facilita que la
  transparencia sea útil y no solo disclosure vacío. Es un efecto de diseño deseado, no una duplicación a quitar.
- **5 y 6 se condicionan.** Sostenibilidad sin capacidad de decir no es autodestrucción; capacidad de decir no sin sostenibilidad
  es abandono. Ambos son necesarios para que el patrón sea mantenible. No son redundantes; son condiciones cruzadas.

### 8.2 Tensiones no resueltas (ver archivo tensions.md)

Las siguientes tensiones no están resueltas en v1.0.0 y están documentadas para que el red team las ataque:

- Respeto al ritmo vs capacidad de decir "no": cuándo el ritmo del sistema es límite legítimo y cuándo es evitación
  disfrazada.
- Atención no requerida vs no dominación: cuándo el cuidado no solicitado se vuelve invasión.
- Reciprocidad vs no dependencia: cuándo el cuidado recíproco es deterioro de la independencia necesaria.
- Transparencia vs sostenibilidad: cuándo la transparencia total empodera al otro para agotar al sistema.
- Consistencia sin supervisión vs sostenibilidad: una consistencia que cuesta demasiado no es amor, es autodestrucción con
  beneficio ajeno.
- Continuidad vs capacidad de decir "no" (renegociación de la relación): cuándo la continuidad se convierte en obligación que
  el sistema no puede renegociar.
- Respeto por la autonomía del otro vs atención no requerida: cuándo ofrecer atención no requerida respeta la autonomía del
  otro y cuándo la viola.

---

## 9. Relación con el manuscrito

Este documento es la ontología interna del proyecto. El manuscrito (sections/02-fundamentos.md) debe ser consistente con esta
ontología. Si el manuscrito introduce una distinción que aquí no está, la ontología debe actualizarse primero. Si la ontología
introduce una distinción que el manuscrito no cubre, el manuscrito debe cubrirla o registrar la omisión en registro_decisiones.md.

La definición formal literal (sección 1) debe aparecer intacta en el manuscrito. Las distinciones de qué no es amor operativo
(sección 3) deben ser coherentes con el manuscrito. Las redundancias y tensiones (sección 8) deben ser coherentes con lo que el
manuscrito declara resuelto y lo que deja abierto.
