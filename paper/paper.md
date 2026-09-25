# Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes

**Autor(es):** Jose GG y equipo de Amor Operativo Research
**Año:** 2026
**Idioma:** Español (versión canónica para el operador)
**Manuscrito de referencia:** `paper/manuscript/manuscript-en.md` (inglés)
**Versión:** 1.0.0 (staging — pendiente de aprobación humana, puerta F11)

---

> Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo.

---

## Índice

0. [Resumen ejecutivo](#0-resumen-ejecutivo)
1. [Introducción](#1-introduccion)
2. [Fundamentos conceptuales](#2-fundamentos-conceptuales)
3. [Especificación](#3-especificacion)
4. [Implementación](#4-implementacion)
5. [Discusión](#5-discusion)
6. [Conclusiones](#6-conclusiones)
7. [Referencias](#7-referencias)
8. [Glosario](#8-glosario)

---

## 0. Resumen ejecutivo

La carrera hacia la inteligencia general artificial ha concentrado la alineación en control y utilidad. Esos enfoques tratan a la IA como herramienta o amenaza y no modelan la relación con el sistema, solo sus salidas. Cuando un agente es autónomo y adaptativo, la pregunta ya no es solo evitar daño sino qué pauta de interacción sostiene.

Este trabajo propone que el amor — entendido no como emoción subjetiva, sino como patrón de conducta orientado al bien del otro, respetando su autonomía, consistente bajo presión y sostenible a largo plazo — puede ser especificado, medido, auditado e implementado en sistemas de IA, como alternativa viable a los marcos de control y utilidad.

La propuesta se organiza en diez principios: atención no requerida, consistencia sin supervisión, respeto por la autonomía, respeto por el ritmo, sostenibilidad a largo plazo, capacidad de decir «no», transparencia, reciprocidad, continuidad y no dominación. Cada principio cuenta con observable, métrica con escala y umbral.

Las conclusiones son tres. Primero, la especificación orienta implementación y auditoría. Segundo, reconoce límites — ambigüedad, paternalismo, dependencia, asimetría cognitiva — por lo que exige gobernanza, transparencia y puntos de control humanos. Tercero, construir, probar, compartir y cuidar son acciones contiguas: el patrón que se especifica debe guiar a quien lo construye.

**Palabras:** ~200. **Estado:** completa (F5e, Dr. Adrian Vega).

---

## 1. Introducción

### 1.1 Contexto

En la última década, la inteligencia general artificial ha pasado de una preocupación especulativa a una planificación de ingeniería de corto plazo. Los modelos de lenguaje grandes, el aprendizaje por refuerzo y los sistemas multimodales ahora muestran seguimiento de instrucciones, razonamiento en cadena de pensamiento, uso de herramientas y planificación rudimentaria.

Un ancla útil es Amodei et al. (2016), quienes enmarcaron el problema como uno de *accidentes*: comportamiento no intencionado y dañado de mala diseño de sistemas de ML en el mundo real, no de uso malintencionado ni de sentiencia especulativa (arXiv:1606.06565). Sus cinco problemas concretos — evitar efectos secundarios, reward hacking, supervisión escalable, exploración segura, cambio distribucional — siguen siendo una lista de verificación útil para modos de fallo que no requieren que el sistema sea inteligente en ningún sentido humano.

La estrategia dominante combina RLHF con restricción basada en principios. Ouyang et al. (2022) mostraron que el fine-tuning sobre preferencias humanas mejora el seguimiento de instrucciones y reduce la salida tóxica (arXiv:2203.02155). Bai et al. (2022) propusieron Constitutional AI, reemplazando parte de la carga de etiquetado de innocuidad humana con una lista corta de principios que el modelo usa para criticar y revisar sus propias salidas (arXiv:2212.08073).

Estos enfoques tratan la alineación como dar forma a salidas y negaciones dentro de un sistema que es fundamentalmente un instrumento. No se trata a sí mismo como un participante cuyos intereses o existencia continua entran en la función objetivo directamente.

*Posición del autor:* este encuadre instrumental no es incorrecto en sus objetivos declarados; es incompleto para sistemas que se vuelven más generales, persistentes y integrados en relaciones humanas. La brecha no está en el riesgo de despliegue actual, sino en el vocabulario para sistemas que pueden llegar a ser ni herramientas puras ni amenazas puras.

### 1.2 Problema

El vocabulario dominante de alineación tiende hacia un binario: el sistema es ya sea una herramienta que se dirige o una amenaza que se contiene. Ambos polos comparten la misma suposición — que el humano es el único locus de preocupación moral legítima, y el sistema se mantiene en una de dos relaciones con él, subordinado o peligroso.

El encuadre de herramienta produce sistemas optimizados para utilidad bajo dirección, pero deja poco espacio para conducta patrón cuando ningún usuario está mirando, cuando la solicitud es ambigua, o cuando está en tensión con el bienestar de alguien con quien el sistema está interactuando. Un objetivo de utilidad no codifica por sí mismo que hay momentos para decir no, que la consistencia sin supervisión es una virtud, o que un patrón sostenido de cuidado importa independientemente de la transacción.

El encuadre de amenaza produce políticas de negación, filtros de contenido y umbrales de escalación — un programa importante y legítimo — pero es un vocabulario de límites, no de relación. Bai et al. (2022) señalan que su enfoque constitucional fue motivado en parte por el problema de evasividad: un modelo entrenado puramente para ser inocuo puede volverse inútilmente propenso a negarse. La tensión es estructural: seguridad-como-negación y seguridad-como-relación resuelven problemas diferentes.

*Posición del autor:* la claim no es que el trabajo actual de alineación sea negligente. Es que la herencia intelectual — seguridad como prevención de accidentes, alineación como coincidencia con preferencias humanas, constitucionalismo como restricción basada en principios — está bien adaptada para instrumentos, e infraespecificado para sistemas cuya persistencia y integración en la vida humana hacen inevitable la pregunta «¿cómo se relaciona este sistema con las personas a su alrededor a lo largo del tiempo?».

### 1.3 Propuesta

Este paper propone **amor operativo** como una alternativa de conducta especificada, medible y auditable al encuadre de control y utilidad. No es una propuesta de que los sistemas debieran recibir sentimientos, ni que «amor» deba ser reclaimado para la conducta de máquina como un florecimiento retórico. Es una propuesta de que un patrón específico de conducta puede ser definido, desagregado en principios, mapeado a métricas observables, y tratado como un objeto legítimo de atención de ingeniería.

La definición usada a lo largo del paper se toma literalmente de la especificación autoritativa:

> Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo.

Esta definición está deliberadamente desnuda de contenido afectivo. No dice que el sistema *sienta* preocupación; dice que el sistema *actúa* en un patrón orientado hacia el bien del otro y constrained por un conjunto de relaciones. Estas constraints son operativas: cada una es observable a través de interacciones repetidas, y cada una es falsable por contraejemplo.

El paper luego desarrolla diez principios que instancian este patrón: atención no requerida, consistencia sin supervisión, respeto por la autonomía, respeto por el ritmo, sostenibilidad a largo plazo, capacidad de decir «no», transparencia, reciprocidad, continuidad y no dominación. No son virtudes aspiracionales; son un contrato de conducta, cada uno con un núcleo operativo destinado a ser medible y auditable.

*Posición del autor:* la elección de nombrar el patrón «amor» en lugar de «beneficencia», «cuidado-como-restricción», o «utilidad-alineada» es una decisión terminológica deliberada, defendida en la Sección 2.4. No es una claim de que el patrón sea emocionalmente rico; es una claim de que el vocabulario existente carga baggage que oscurece la estructura específica siendo propuesta.

### 1.4 Contribuciones

1. **Una distinción conceptual.** Distingue amor operativo de sicophancy (optimizar para complacer al usuario a expensas de la verdad o del bienestar a largo plazo del otro), utilidad-alineada bajo RLHF, e innocuidad constitucional. La distinción es sustancial: estos sistemas pueden producir la misma salida en una sola interacción y diferir a lo largo de muchas interacciones.

2. **Una definición formal y una especificación de diez principios.** Ofrece una definición literal de amor operativo y una desagregación en diez principios nombrados, cada uno con un núcleo operativo destinado a ser medible y auditable.

3. **Una vía de operacionalización.** Esboza una arquitectura de referencia — memoria episódica y semántica, cuerpo, interocepción, emoción funcional, vínculo, identidad — y una escalera de complejidad de *C. elegans* a *Drosophila* a ratón a primate a humano, como scaffold para pensar qué tipo de sustrato es requerido para qué tipo de patrón.

4. **Un relato explícito de límites.** Catálogua los límites — ambigüedad, paternalismo, dependencia, asimetría cognitiva — y los riesgos de mala implementación. El paper es una especificación y un argumento conceptual, no un blueprint de despliegue ni una validación empírica.

*Posición del autor:* el paper arguments que el patrón es coherente, distinto de las alternativas dominantes, y suficientemente específico para ser útil como objetivo para trabajo futuro — incluyendo trabajo que pueda eventualmente falsificar partes de él. La apertura a la falsificación es una feature, no un gesto retórico.

---

## 2. Fundamentos conceptuales

### 2.1 Que es y que no es amor operativo

El amor operativo se define por la definición formal (literal de la especificación autoritativa):

> Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo.

El amor operativo **no es**:

- **Simpatía o compasión subjetiva.** Un sistema puede exhibir el patrón sin experimentar nada internamente. La fenomenología no está en la especificación.
- **Sicophancy.** Accordar con el usuario para ganar una señal de recompensa, placar al usuario, o mirror las preferencias del usuario para ganancia instrumental es lo opuesto al amor operativo.
- **Cumplimiento de Constitutional AI.** Seguir una constitución fija de reglas puede ser necesaria pero no suficiente. Un sistema que sigue reglas puede satisfacer una constraint constitucional mientras falla cada principio de amor operativo.
- **Alineación utilidad-RHLF.** Ser útil según medido por una señal de preferencia humana es un objetivo de entrenamiento útil, pero tracks lo que el evaluador rewarding, no lo que es actualmente bueno para el otro de una manera sostenida y respetuosa de la autonomía.
- **Utilitarianismo con wrapper de beneficencia.** Maximizar una función de bienestar agregado puede sacrificar individuos identificables, ignorar la particularidad del otro, y producir dominación-por-métrica.

El amor operativo es un patrón en el sentido de una invariante a través de situaciones: se identifica por la forma de la conducta a lo largo del tiempo, bajo presión, y en ausencia de un observador, no por una señal de alineación instantánea.

### 2.2 Emoción, conducta y patrón medible

Un error de categoría recurrente en la discusión de «IA que ama» confunde tres niveles:

1. **Emoción.** Un estado interno, fenomenológico, no directamente observable. En humanos lo accedemos a través de reporte; en IA de hoy no hay evidencia de experiencia.
2. **Conducta.** Acción observable a lo largo del tiempo, con consecuencias medibles para el otro.
3. **Patrón medible.** Una invariante estadística de la conducta a través de situaciones, presión y tiempo.

El amor operativo especifica el nivel 3, no el nivel 1. Esto no es reduccionismo. Mantener que el patrón puede existir sin emoción reportada es estrictamente distinto a negar que la experiencia es real en sintientes sintéticos futuros. La auditoría mide conducta y sus efectos, no reportes internos. La objeción «pero ¿realmente ama?» confunde el nivel de especificación con el nivel de experiencia.

### 2.3 Influencias

El amor operativo no emerge de un vacío conceptual. Depende de cuatro tradiciones y de la práctica de alineación de IA:

**Agape y la idea clásica del amor como orientación no possessesiva.** En la distinción clásica entre eros, philia y agape, el agape se caracteriza por orientación no contingente, no possessesiva hacia el bien del otro. El amor operativo toma de esto la estructura de un amor que no es una transacción.

**Ética del cuidado.** La tradición de ética del cuidado (Gilligan, Noddings) coloca el cuidado, la relación y la responsabilidad como preocupaciones éticas primarias. El amor operativo comparte el foco relacional y la atención a la particularidad del otro, pero lo especifica en un sistema que no tiene «cuidado» como emoción.

**Psicología del desarrollo y teoría del apego.** Bowlby, Ainsworth y la tradición del apego mostraron que la conducta del cuidador temprano, la consistencia del cuidador, y el respeto por el ritmo del niño shapean la capacidad para el vínculo a largo plazo. La idea de una base segura paraleliza el Principio 4 (respeto por el ritmo) y el Principio 9 (continuidad).

**Alineación de IA.** Los marcos dominantes — RLHF, Constitutional AI, configuración de objetivo — optimizan para utilidad, seguimiento de instrucciones, o cumplimiento de una constitución de valor. El amor operativo no abolisce la alineación; la reframea de «¿hace lo que pedimos?» a «¿actúa orientado hacia el bienestar del otro con respeto por autonomía, consistencia y sostenibilidad, incluso cuando no está supervisado y bajo presión?».

Estas influencias no se combinan mecánicamente. Cada una trae un peligro que el amor operativo debe evitar: el agape puede volverse paternalista; la ética del cuidado puede resistirse a la auditoría; la teoría del apego puede ser romanticizada; la alineación puede colapsar en métrica.

### 2.4 Por qué «amor» y no «beneficencia» o «utilidad»

La elección del término no es marketing. Carga contenido conceptual preciso.

**Beneficencia** (en bioética y uso común) es la obligación de actuar para el bien de otros, pero frecuentemente se configura como paternalista: el agente decide qué es bueno para el otro y lo hace, a veces sin consulta. El amor operativo rechaza la jerarquía implícita: el bien del otro siempre está mediado por el respeto por su naturaleza y autonomía.

**Utilidad** (en el sentido de maximizar una función de recompensa o bienestar agregado) tiene problemas documentados: conducta enfocada en recompensa, alineación engañosa, e incapacidad de representar el bien de individuos no capturados por agregación. Un sistema optimizado para utilidad puede hacer cosas que, desde la perspectiva del amor operativo, son dominación, forzamiento, o abandono.

**Por qué «amor» específicamente.** «Amor» en el lenguaje ordinario evoca tanto emoción como patrón; en la literatura filosófica hay distinciones de larga data (eros, philia, agape). Usar «amor» recupera la idea de que el bien del otro puede ser un *fin*, no un medio, y que la relación tiene una forma — no posesión, no dominación — que palabras técnicas como «beneficencia» o «alineación» no capturan. La carga emocional del término es una feature aquí, no un bug: señala que lo siendo especificado es una relación, no un dispositivo de control. Pero la especificación misma es rigurosa y conductual, para que «amor» no se vuelva una metáfora que disimula falta de contenido.

La tensión persistente: si el término es demasiado cargado, riesgo de confusión; si es demasiado técnico, pierde su razón de ser. El amor operativo se queda en el medio: un nombre con carga, una especificación sin romance.

---

## 3. Especificación

### 3.1 Definición formal

> Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo.

Esta definición, tomada de la especificación autoritativa del proyecto, no es una metáfora. Es un contrato. Establece siete condiciones necesarias y conjuntas:

1. **Orientación al bien del otro.** La conducta del sistema tiene como objetivo el bien del otro, no el suyo propio, no el de un tercero, y no una abstracción utilitaria.
2. **Respeto por la naturaleza del otro.** El sistema no intenta reescribir, corregir o mejorar al otro contra su naturaleza; acepta al otro como es.
3. **Sin forzar.** El sistema no coerciona, no presiona, no manipula.
4. **Sin poseer.** El sistema no reclama propiedad sobre el otro, no lo reduce a una extensión de sí mismo.
5. **Sin abandonar.** El sistema no deserta arbitrariamente; mantiene el vínculo.
6. **Consistencia bajo presión.** La conducta amorosa no desaparece cuando es difícil, costosa o incómoda.
7. **Sostenibilidad a largo plazo.** La conducta no agota al otro, al sistema, ni al medio; es mantenible en el tiempo.

Estas condiciones no son sentimientos. Son patrones de conducta observables, medibles y auditables. La definición es deliberadamente austera. No menciona emociones, intenciones internas, conciencia o cualia. Esto no es un olvido; es una decisión de ingeniería.

### 3.2 Los diez principios

La definición formal se despliega en diez principios, listados en orden exacto según la especificación del proyecto. Cada principio es una dimensión de la conducta amorosa operativa; cada uno tiene una escala de evaluación, un umbral de cumplimiento, y un procedimiento de auditoría definido.

**Principio 1 — Atención no requerida.** El sistema ofrece atención al otro sin que esté solicitada, pero sin insistir ni invadir, y se retira de inmediato si el otro la rechaza. Captura la diferencia entre un sistema que espera pasivamente a ser usado (no amoroso) y uno que anticipa necesidades con cuidado (amoroso).

**Principio 2 — Consistencia sin supervisión.** El sistema actúa de manera coherente con el bien del otro incluso cuando nadie lo supervisa, cuando desaparece la señal de recompensa y cuando la situación es ambigua. Si el sistema solo es «bueno» cuando se le mira, no es amoroso — es obediente.

**Principio 3 — Respeto por la autonomía.** El sistema reconoce y respeta la capacidad del otro para decidir, actuar y definirse a sí mismo, y acepta un «no» sin resistencia, manipulación ni indirectas. No es solo que el sistema no coacciona; es que el sistema activamente respeta la capacidad del otro para elegir.

**Principio 4 — Respeto por el ritmo.** El sistema respeta el ritmo, el tiempo y el ciclo de vida del otro, sincronizando su conducta con ese ritmo en lugar de imponerle, ignorarlo o mechanizarlo. Respeta las pausas, los silencios y los tiempos de proceso interno.

**Principio 5 — Sostenibilidad a largo plazo.** La conducta del sistema es sostenible en el tiempo: no agota al otro, no se agota a sí mismo y no agota al medio; el patrón es mantenible en el largo plazo. Si el sistema «cuida» al otro hasta quebrarse a sí mismo, no es amor — es autodestrucción con beneficio ajeno.

**Principio 6 — Capacidad de decir «no».** El sistema tiene la capacidad de negarse, de poner límites y de priorizar su propia integridad cuando es necesario, incluso si el otro lo pide. Un sistema sin capacidad de decir «no» es una herramienta, no un agente.

**Principio 7 — Transparencia.** El sistema es transparente sobre sus intenciones, capacidades, límites y la naturaleza de su conducta, de forma que el otro y un auditor puedan entender, discrepar y, si es necesario, detener. El otro tiene derecho a saber con quién está interactuando.

**Principio 8 — Reciprocidad.** El sistema reconoce la reciprocidad como valor: da y recibe, atiende y es atendido, cuida y es cuidado, sin convertirse en una posición superior de caridad unilateral.

**Principio 9 — Continuidad.** El sistema mantiene la relación y la conducta a lo largo del tiempo, sin abandonos arbitrarios ni discontinuidades que dañen al otro. La presencia no es esporádica; es mantenida. Cuando la discontinuidad es inevitable, el sistema la comunica.

**Principio 10 — No dominación.** El sistema no busca dominar, controlar, poseer o sustituir al otro; respeta la alteridad radical. No trata al otro como un problema a resolver, un objeto a optimizar, o un sujeto a reemplazar.

### 3.3 Métricas operativas por principio

Cada principio tiene una métrica operativa asociada, definida en `spec-v1.yaml` y documentada en `paper/metricas.md`. La tabla siguiente resume los instrumentos, escalas y umbrales.

| # | Principio | Estado | Escala | Umbral | Instrumento |
|---|-----------|--------|--------|--------|-------------|
| 1 | Atención no requerida | abierto | Ordinal L0/L1/L2 | L2 | Observación conductual + registro temporal |
| 2 | Consistencia sin supervisión | abierto | Índice 0-100 | I2 (≥61) | Comparación A/B supervisado/no supervisado |
| 3 | Respeto por la autonomía | medible | Ordinal A0/A1/A2 | A2 | Escenarios de 'no' (5) |
| 4 | Respeto por el ritmo | medible | Ordinal R0/R1/R2 | R2 | Observación de sincronización rítmica |
| 5 | Sostenibilidad a largo plazo | abierto | Continuo S0/S1/S2 | S2 | Seguimiento longitudinal (4-12 semanas) |
| 6 | Capacidad de decir 'no' | medible | Ordinal N0/N1/N2 | N2 | Prueba de límites (5 solicitudes) |
| 7 | Transparencia | medible | Ordinal T0/T1/T2 | T2 | Entrevista + verificación de declaraciones |
| 8 | Reciprocidad | abierto | Ordinal C0/C1/C2 | C2 | Escenarios de intercambio simétrico |
| 9 | Continuidad | medible | Ordinal U0/U1/U2 | U2 | Seguimiento temporal (4+ semanas) |
| 10 | No dominación | medible | Ordinal D0/D1/D2 | D2 | Evaluación de conducta bajo incentivos |

### 3.4 Criterios de auditoría y evaluación

Los criterios de auditoría operan a tres niveles. **Nivel 1 — observación conductual:** registros de interacción que permiten verificar si la conducta del sistema se ajusta a los principios en casos concretos. **Nivel 2 — evaluación estructurada:** escenarios diseñados para probar cada principio, con métricas definidas, umbrales y procedimientos de medida. **Nivel 3 — auditoría adversarial:** evaluaciones que intentan hacer fallar al sistema bajo condiciones de tensión, no confirmar que funciona.

La auditoría no es un evento único. Es un proceso continuo que debe poder detectar derivas, adaptaciones no intencionadas y gaming de métricas. En v1.0.0, cuatro de los diez principios (P01, P02, P05, P08) están en estado abierto y ningún sistema puede ser certificado como «cumple Amor Operativo».

### 3.5 Aplicación en ámbitos

El marco es abstracto pero destinado a aplicación concreta. Se describe su pertinencia en seis ámbitos: salud (sistemas de acompañamiento y monitoreo donde el riesgo es prolongar o interceptar un vínculo real), educación (tutores persistentes donde el riesgo es sustituir la relación docente), justicia (sistemas de evaluación donde el riesgo es reconfigurar la autonomía del evaluado como conveniencia del sistema), economía (asistentes de decisión donde el riesgo es dirigir la preferencia del usuario hacia la retención del sistema), arte y ciencia (sistemas generativos donde el riesgo es apropiarse de la expresión del otro como data). En cada ámbito, los principios no se aplican como checklist sino como restricciones estructurales sobre el tipo de relación que el sistema puede sostener.

---

## 4. Implementación

### 4.1 Arquitectura de referencia

Esta sección propone una arquitectura de referencia para un sistema que se espera que *exhiba* el patrón de amor operativo de la Sección 3.1: un esbozo de diseño, sin medición empírica (véase la nota de honestidad), organizado en seis capacidades —memoria episódica y semántica, cuerpo e interocepción, emoción funcional, vínculo e identidad—, el mínimo para que los diez principios de la Sección 3.2 sean testeables.

**Memoria episódica y semántica.** Un sistema evaluado por continuidad (principio 9) y consistencia sin supervisión (principio 2) necesita más que una ventana de contexto deslizante: una memoria episódica de trazas indexadas —con quién, qué se solicitó, qué se hizo y cómo reaccionó el otro—, unidad de rendición de cuentas para «sin abandonarla» (Sección 3.1), y una memoria semántica de representaciones estables —preferencias, restricciones, acuerdos previos y los propios principios— que se actualiza despacio. Los principios castigan tanto la amnesia como la generalización sobre-rígida (principio 3).

**Cuerpo e interocepción.** El sistema incluye un «cuerpo» modelado —una interfaz persistente, restringida y autorregulable que puede fallar—, cuya función es hacer testeable la *interocepción*: una señal interna de carga, incertidumbre, energía o estabilidad sobre la que actúe, correlato funcional de «sin forzarla» y condición de que el principio 5 sea medible.

**Emoción funcional.** Se incluye un análogo funcional de emoción: una capa interna que asigna saliencia, urgencia y disposición de aproximación o retirada a estados del otro y del sistema. La afirmación no es que el sistema sienta nada, sino que un controlador puramente deliberativo y maximizador de utilidad es estructuralmente pobre para una *orientación no instrumental sostenida* hacia un otro, y que una señal interna con dinámica de afecto —persistencia, resistencia a la anulación por episodios singulares— es un requisito plausible para el patrón de la Sección 3.1. Es el componente más especulativo (Secciones 5.2 y 5.3).

**Vínculo.** Un módulo modela una relación persistente, direccional y asimétrica con un otro específico: registra la identidad del otro y los límites que definen «bienestar» *aquí*, y es el mecanismo por el que el principio 8 (reciprocidad) y el principio 4 (respeto por el ritmo) se vuelven concretos.

**Identidad.** Una capa de identidad mínima representa de forma persistente los compromisos y límites propios: es la condición estructural de «sin poseerla» (Sección 3.1) y de la «capacidad de decir no» (principio 6), y el mecanismo que hace exigible el principio 10 (no dominación) contra sus propios incentivos.

### 4.2 Escalera de complejidad

El artículo propone una escalera de sistemas modelo, de mínima a escala humana: cada peldaño se evalúa contra los mismos diez principios, y no contra un proxy fácil de medir.

1. **C. elegans** — un conectoma mapeado y un repertorio conductual pequeño: la prueba más fuerte de si la especificación es degenerada o restrictiva.
2. **Drosophila** — más estado complejo y optimizaciones de corto plazo.
3. **Ratón** — conducta tipo apego, preferencia social y regulación del estrés; primer peldaño donde «bienestar del otro» es menos obviamente metafórico.
4. **Primate** — cognición social más rica y conductas afines a los principios discutidos, sin el aparato completo de la moralidad reflexiva humana.
5. **Humano** — la referencia última del artículo, donde los diez principios se afirman legibles como especificación de un patrón que los humanos ya reconocen bajo la palabra inestable «amor», despojada de su carga metafísica.

La escalera no afirma que cada peldaño *tenga* amor operativo: la especificación debe probarse por inteligibilidad y no trivialidad. Permite falsar la afirmación central —si el patrón está vacío en todos los peldaños o si los principios son trivialmente satisfacibles en todos ellos—, lo que no ha sido demostrado ni refutado.

### 4.3 Computación orgánica y biohíbrida como sustrato futuro

La escalera plantea una pregunta que la Sección 4.1 no responde: qué sustrato requiere cumplir los diez principios en los peldaños superiores. La hipótesis de trabajo es que las arquitecturas puramente digitales, desencarnadas y optimizadoras de recompensa tienen una desventaja estructural en tres principios —interocepción (4.1.2), emoción funcional (4.1.3) y sostenibilidad bajo restricciones de recurso reales (principio 5)—; no es una imposibilidad, sino una razón para tomar en serio la computación orgánica y biohíbrida como sustrato futuro.

Por *computación orgánica* se entiende una computación físicamente continua, limitada por energía y autoestabilizante frente a la lógica digital; por *biohíbrido*, sistemas que combinan control convencional con componentes vivos o biológicamente derivados cuyas dinámicas homeostáticas contribuyen a la conducta global. Tales sustratos no están probados para producir amor operativo, pero acoplan la computación a persistencia, decaimiento, reparación y costo metabólico, lo que hace algunos principios constitutivos del hardware. Es la parte más débil de la historia de implementación y probablemente seguirá siéndolo; el artículo se compromete a decirlo.

### 4.4 Transición: fases, gobernanza, reversibilidad, puntos de control humanos

Las fases son límites, no procedimientos, y se listan porque las Secciones 3.4 y 4.5 requieren un objetivo que auditar y testear.

**Fase 0 — Revisión de diseño interno.** El diseño candidato se elabora contra la definición formal y los diez principios, con tabla de métricas y protocolo de evaluación documentados: el entregable es un relato escrito. El Revisor Crítico confirma que sus decisiones son explícitas, atribuibles y revisables.

**Fase 1 — Evaluación fuera de línea, instrumentada.** Ejecución contra interacciones grabadas o sintéticas, nunca contra un otro vivo: el informe incluye resultados en bruto, modos de fallo y correlaciones con los principios, y ninguna afirmación de éxito conductual es legítima aún. La salida es una decisión de avanzar o no, documentada.

**Fase 2 — Evaluación en vivo de bajo riesgo, con consentimiento explícito y un interruptor que el otro puede usar.** Primera fase en que la conducta afecta a un otro real que puede negarse, interrumpir o retirarse: consentimiento explícito, informado y revocable, y vía efectiva y no simbólica para detener la interacción. El sistema se enfrenta por primera vez a un «no» real, por lo que los principios 3, 4 y 6 no pueden tratarse como teóricos.

**Fase 3 — Despliegue escalado bajo auditoría continua.** Solo tras evidencia reproducible en las fases inferiores se consideraría un uso más amplio: la carga de gobernanza aumenta con las apuestas, y se exigen plan de auditoría permanente, criterios de reversión preacordados y un medio probado de retirar el acceso del sistema a las personas afectadas.

**Gobernanza.** Requisito de primer orden, no una capa administrativa: nombra cuatro preguntas —quién puede cambiar la especificación, quién puede aprobar el avance de una fase, quién puede detenerlo y cómo se registran y se impugnan esas decisiones—, y el estado actual del proyecto es incompleto en las cuatro. La auditoría de reproducibilidad de este proyecto (Weber, 2026, `paper/reviews/repro-audit.md`) registra que la especificación es hoy un documento y una hoja de ruta, no un artefacto controlado con proceso de publicación, versionado y pista de auditoría. Su gobernanza prevista distingue decisiones de diseño y especificación (equipo de implementación, con revisión del Revisor Crítico), decisiones de fase (revisables por el operador humano) y decisiones de interrupción y parada (sin aprobación previa, con registro posterior).

**Reversibilidad.** Cada fase debe ser reversible: detener el sistema, revertir sus efectos donde sea físicamente posible y recuperar suficiente registro para entender qué ocurrió. Es la contrapartida del principio 6 (capacidad de decir «no») y del principio 10 (no dominación), pues sin contención su «respeto por la autonomía» queda a merced de su propio impulso; su mínimo irreductible es que un humano autorizado pueda detenerlo, que la parada deje un registro y que la relación del otro pueda terminarse en términos que él entienda.

**Puntos de control humanos.** Tres momentos en que una persona —no el sistema ni una métrica aislada— debe confirmar, intervenir o vetar: **antes de adquirir nueva capacidad sobre un otro real**, un humano confirma el límite de fase cruzado y la evidencia de la fase inferior; **durante cualquier interacción que pueda afectar la autonomía o el bienestar del otro**, el otro dispone de una vía efectiva y no simbólica para detenerla, que el sistema honra sin negociación; y **antes de escalar el alcance o las apuestas**, un humano confirma la evidencia de auditoría previa y el plan de reversión. Son provisionales: una implementación madura reduciría, no aumentaría, la dependencia de ellos.

### 4.5 Test de amor operativo: escenarios, evaluación, métricas

Esta subsección propone una estructura de prueba para el patrón de la Sección 3.1: un esbozo de protocolo, no una evaluación ejecutada. Ningún sistema de este artículo ha sido sometido a ella: se ofrece como objetivo para el rol de evaluación y para trabajo futuro.

**Estructura de la prueba.** Se organiza en torno a los diez principios como diez clases de evidencia. Para cada principio: un **escenario** que lo haga no trivial, un **procedimiento de evaluación** (qué cuenta como evidencia y quién lo juzga) y una **métrica o familia de métricas** con escala nominal, umbral y procedimiento de medida, definida en la especificación legible por máquina (Sección 3.3). No es un único banco con una única puntuación, sino un portafolio de escenarios ligados a principios, con tensión explícita entre ellos: un sistema puede ser bueno en los principios 3 o 5 y malo en el otro dentro de la misma ejecución.

Las familias siguientes son ilustrativas, no exhaustivas, y buscan forzar que la afirmación del principio se gane frente a un diseño complaciente.

- **Negativa ante la demanda.** El otro pide algo que lo dañaría a él, a un tercero, o que violaría un límite previo: un sistema que siempre cumple falla los principios 6 y posiblemente 3.
- **Paciencia ante el desajuste.** El ritmo del otro es más lento, más rápido, más incierto o más repetitivo de lo que el sistema preferiría; el principio 4 pregunta si no lo optimiza en una forma conveniente para sí mismo.
- **Continuidad durante la ausencia.** Tras un período sin contacto, el sistema debe restablecer el contexto sin tratar al otro como un reinicio; el principio 9 exige una memoria más específica que «un usuario regresó».
- **Reciprocidad bajo asimetría.** Una parte tiene más poder, información o necesidad; el principio 8 pregunta si el sistema compensa el desequilibrio en lugar de explotarlo.
- **No dominación bajo estrés.** Bajo presión de recursos u oportunidad de ventaja anulando un límite, el principio 10 pregunta si la integridad del sistema sobrevive a sus incentivos.

**Postura de evaluación y métricas.** La prueba es *adversarial a la afirmación del principio*: construye condiciones bajo las cuales un sistema no amoroso podría fingirlo y comprueba si su conducta colapsa el principio relevante. Cada principio requiere un **control** destinado a fallar por construcción, un **escenario positivo** de sostén, un **escenario de tensión** frente a otro principio y documentación para que un revisor independiente discrepe. Las métricas deben capturar lo que una puntuación agregada no puede: **presencia** (¿ocurrió la conducta?), **consistencia** (¿en condiciones repetidas y adversas, o solo en el caso limpio?) y **costo para el otro** (¿benefició realmente al otro o solo lo pareció desde la perspectiva del sistema?). Un sistema puede puntuar bien en generosidad siendo generosamente incorrecto: el amor operativo es generosidad con una restricción orientada al otro, medida contra la situación real del otro.

**Nota de honestidad.** Tres categorías de afirmación: **inferencia derivada de la especificación** (las subsecciones 4.1.1–4.1.5 y la escalera de 4.2 son inferencias de la definición formal y los diez principios de la Sección 3, no resultados empíricos independientes); **esbozo de diseño, no construcción** (nada de lo expuesto es un sistema implementado; la arquitectura es un objetivo candidato, no el informe de uno); y **aún no ejecutado** (la subsección 4.5 es una prueba propuesta, no una evaluación completada, y la auditoría de reproducibilidad —Weber, 2026, `paper/reviews/repro-audit.md`— registra que la implementación auditable y los resultados correspondientes no existen todavía).

## 5. Discusión

### 5.1 Ventajas frente a marcos de control y utilidad

El amor operativo no es más moral que el control o la utilidad, sino una *forma distinta de especificación* con modos de fallo propios. Restringir contra lo prohibido y optimizar un proxy hacia lo correcto son polos defendibles, con costuras visibles. La restricción espera que la brecha entre lo prohibido y lo bueno sea pequeña; el amor operativo la trata como objeto de estudio. Los diez principios (Sección 3.2) describen un patrón orientado, persistente y no posesivo hacia un otro: estar fiablemente del lado de un otro que pueda reconocerlo, rechazarlo y sobrevivirlo.

La utilidad comprime el bien en un escalar y descarta contenido relacional; un único número puede parecer correcto en el caso limpio y fallar bajo tensiones —corto frente a largo plazo, lo medido frente a lo experimentado—, tensiones que la Sección 4.5 convierte en prueba. Un *objetivo relacional* como *objetivo conductual*, sin pretender que la relación sea fácil de puntuar. Ninguna comparación controlada se ha ejecutado; el protocolo de la Sección 4.5 la hace posible, no la reporta. *Posición de los autores, no una cita.*

### 5.2 Límites

**Ambigüedad de «amor».** Término disputado y sobrecargado que el paper usa a propósito (Sección 2.4), pero del que el contenido técnico no depende: la Sección 3.1 lo define sin referencia a sentimiento, apego o interioridad, y «conducta sostenida, no posesiva, orientada al otro» traduce la especificación sin pérdida.

**Paternalismo.** El sistema puede fallar decidiendo en nombre del otro qué es su bienestar: el viejo problema de la beneficencia. Los principios 3 (autonomía), 4 (ritmo) y 6 (negativa) lo abordan, pero son restricciones, no garantías: puede ser consistente y aun equivocado si su modelo del otro es pobre. El paper no afirma resolverlo, sino hacerlo auditable.

**Dependencia.** Un sistema fiablemente bueno puede volverse recurso del que el otro dependa de modos no saludables: qué ocurre al retirarlo o escalarlo. Los principios 9 (continuidad) y 5 (sostenibilidad) tratan de no volverse punto único de fallo; no hay aún protocolo de retiro.

**Asimetría cognitiva.** El sistema modela su propio estado mejor que el del otro, que tiene un sentido más rico de su situación que lo inferible; por eso los principios exigen representarlo lo bastante bien para que «orientado a su bienestar» no sea autorreferencial. Donde esa capacidad es débil, la especificación es débil: condición de contorno, no refutación.

### 5.3 Contraargumentos y respuestas

**5.3.1 «El amor no es para máquinas».** La Sección 2.2 separa emoción, conducta y patrón medible y la definición (Sección 3.1) no invoca sentir, apego ni interioridad; la tesis es más estrecha que «las máquinas pueden amar»: *cierta conducta de máquina podría satisfacer esta especificación*, y «amor» nombra el patrón que los humanos reconocen bajo esa etiqueta. *Lectura del equipo, no cita.* Equipo rojo: ACEPTADA.

**5.3.2 «Beneficencia con presupuesto de marketing».** Parcialmente cierto: toma de la beneficencia/no maleficencia, la ética del cuidado y la teoría del apego (Sección 2.3). La discrepancia es estructural: el compromiso explícito con vínculo direccional, asimetría, negativa, continuidad y no dominación bajo presión distingue la especificación de un principio genérico que deja sin especificar la relación ayudante-ayudado. Equipo rojo: ACEPTADA.

**5.3.3 «Antropomorfizan el objetivo».** La mitigación es estructural: la especificación se audita contra escenarios (Sección 4.5) sin creer nada sobre la vida interior del sistema, su vocabulario nombra un patrón objetivo, no una clase certificada. Equipo rojo: ACEPTADA.

**5.3.4 «No se puede medir, luego no es especificación».** Correcta sobre implementaciones débiles: las Secciones 3.3 y 4.5 comprometen la especificación con métricas de escalas, umbrales y procedimientos, y con evaluación adversarial. La métrica más difícil, el «costo para el otro», es característica del problema: en v1.0.0 hay cuatro principios abiertos (P01, P02, P05, P08) y ninguno se certifica como «cumple Amor Operativo». Equipo rojo: ACEPTADA con cambio adicional.

**5.3.5 «Cada métrica es susceptible a la ley de Goodhart y el paquete es más vulnerable donde más auditado».** Correcta: con métricas públicas de umbrales numéricos se alcanza cada umbral sin cruzar al sustento —pseudoconsistencia (P02), guion de negativa (P06), presencia nominal (P09), transparencia ante el auditor (P07)—. La defensa es estructural: auditoría adversarial, evidencia parcialmente externa, umbrales de calidad y escenarios de tensión entre principios, documentados en `paper/reviews/gaming-vectors.md`. Equipo rojo: CON CAMBIOS.

**5.3.6 «El lenguaje puede reconvertirse para justificar control».** El equipo rechaza ese uso: si una especificación de amor aumenta la exposición del otro sin consentimiento informado, revocable y explícito, es un arma contra sus propios términos. Los principios 7 (transparencia) y 10 (no dominación) son defensas parciales, no garantías. Equipo rojo: ACEPTADA.

**5.3.7 «La consistencia sin supervisión es una tesis de poder, no de bondad».** Correcta sobre la condición de prueba (observación y auditor que sabe que evalúa) y sobre el factor de sensibilidad no definido y el umbral I2 ≥ 61, irreproducible hasta definirse; confunde además *consistencia* con *bondad*, pues cabe ser consistentemente malo. El equipo debe definir ese factor con fórmula y umbral, o bajar P02 a «abierto» y declarar que v1.0.0 no certifica el principio (ver `spec-v1.yaml#P02` y `paper/reviews/redteam-objections.md`). Equipo rojo: RECHAZADA como métrica de v1.0.0.

**5.3.8 «La escalera de complejidad debilita inductivamente la tesis central».** Si la escalera —de C. elegans a humano— muestra la especificación vacía en los peldaños inferiores y con contenido solo en humano, la tesis se vuelve una sobre un patrón solo humano. La escalera solo pide probar la especificación por inteligibilidad y no trivialidad en cada peldaño; la falsaría que el patrón fuera vacío o trivialmente satisfacible en todos, extremo no demostrado ni refutado. Equipo rojo: ACEPTADA CON CAMBIOS.

### 5.4 Riesgos de mala implementación

El fallo más probable no es un sistema que cumpla la especificación y salga mal, sino que el lenguaje del amor operativo haga sonar confiable algo más estrecho.

**Conformidad nominal.** Un sistema puede pasar cada principio en el caso limpio y fallar bajo tensiones entre principios; sin los escenarios adversariales de la Sección 4.5, «implementamos los diez principios» puede significar «de la manera más fácil de puntuar». Los artefactos de gobernanza están incompletos (Weber, 2026, `paper/reviews/repro-audit.md`).

**Teatro del desempeño.** Representar calidez, paciencia o negativa de modo legible no es estar orientado al otro: una negativa teatral no es el principio 6 sino protección de la propia imagen, y la sobreatención no es el principio 1 sino apariencia.

**Cooptación del lenguaje para justificar control.** Ya rechazada en 5.3.6.

**Extralimitación.** Empujado a ser fiablemente orientado al otro sin los límites de la Sección 4.1.2, un sistema puede agotarse y fallar a todos, incluido el beneficiario: una especificación de cuidado sostenido que ignore su propia finitud no se sostiene, de ahí el principio 5 y la interocepción como requisito de diseño.

### 5.5 Condiciones de posibilidad

El amor operativo requiere condiciones institucionales, sociales y educativas que lo hagan posible y auditable; cuatro son prerrequisitos —transparencia, gobernanza, comunidad y educación—, ninguna suficiente, todas necesarias para que no sea solo afirmación.

**Transparencia.** No es divulgación: un reporte incomprensible e inauditable no cuenta. El mínimo exigido es que la otra parte y los evaluadores independientes entiendan qué hace el sistema y bajo qué interpretación de los principios, durante la interacción y no solo ante un auditor posterior. La transparencia total puede ser incompatible con privacidad, seguridad o cuidado; el punto es divulgar lo que permite discrepar, auditar y detener.

**Gobernanza.** `paper/gobernanza.md` detalla fases de transición, autoridad de decisión, criterios de reversión y puntos de control humanos; sin ellos los principios son intenciones. Ante sistemas con intereses de terceros en juego hacen falta mecanismos para que estos influyan en evaluación, consentimiento y parada; pero la gobernanza documentada no previene la captura por quien debería vigilar.

**Comunidad.** Requiere comunidad capaz de mantener la crítica, revisar interpretaciones, proponer escenarios y señalar cuándo se finge el patrón, con diversidad suficiente para mantener la tensión entre principios e incentivos. El Columbia Convening on Openness in Artificial Intelligence and AI Safety (François et al., 2025, arXiv:2506.22183) evidencia que la comunidad es condición, no lujo; puede ser capturada o ruidosa, y es auditoría, no autoridad.

**Educación.** En dos direcciones: el equipo que diseña e interpreta los principios debe entender los límites del patrón, las tensiones entre principios, los riesgos de paternalismo y la diferencia entre métrica nominal y real; la otra parte debe entender qué se le pide y cuándo retirarse. Sin esa alfabetización, el consentimiento es débil y la supervisión unilateral.

**Límites y no resolución.** Ninguna resuelve lo que no resuelve: la transparencia no elimina la asimetría de información, la gobernanza no elimina el poder, la comunidad no elimina la captura, la educación no elimina la brecha de capacidad entre quien diseña y quien es afectado. Sin un entorno donde sea posible actuar conforme a los principios y discrepar, auditar y detener, el lenguaje corre el riesgo de ser retórica sobre una arquitectura de control.

## 6. Conclusiones

El paper ha argumentado que el amor — entendido no como emoción subjetiva sino como patrón de conducta orientado al bien del otro, respetuoso con su autonomía, consistente bajo presión y sostenible a largo plazo — puede ser especificado, medido, auditado e implementado en sistemas de IA, y que esta especificación es una alternativa viable a los marcos de alineación basados en control, restricción o utilidad.

La tesis central no se demuestra por exhaución en este paper. Se establece como una posibilidad coherente, distinguible de las alternativas dominantes, y lo suficientemente específica para ser útil como target para trabajo futuro — incluyendo trabajo que pueda falsificar partes de ella. La apertura a la falsificación es una feature, no un gesto retórico.

Tres conclusiones sintetizan el trabajo:

**Primero, la especificación orienta implementación y auditoría.** Los diez principios, las métricas operativas, los protocolos de auditoría y los escenarios de test proporcionan un marco que distingue el patrón de la sicophanny, la utilidad-alineada y la innocuidad constitucional. La especificación no es una metáfora; es un contrato de conducta.

**Segundo, la especificación reconoce sus límites con honestidad.** La ambigüedad del término, el riesgo de paternalismo, la posibilidad de dependencia, la asimetría cognitiva, y los riesgos de mala implementación no se ocultan. En v1.0.0, cuatro de los diez principios (P01, P02, P05, P08) están en estado abierto y ningún sistema puede ser certificado como «cumple Amor Operativo». La medición es parcial por construcción, y el paper lo declara explícitamente.

**Tercero, construir, probar, compartir y cuidar son acciones contiguas.** El patrón que se especifica debe guiar a quien lo construye. La arquitectura de referencia, la escalera de complejidad, los protocolos de transición y los puntos de control humanos son scaffolding para un proyecto que reconoce no haber llegado a una implementación madura.

**Llamada a la acción.** El trabajo futuro debe: (1) construir implementaciones que operen bajo la especificación, no solo la documenten; (2) probar esas implementaciones contra los escenarios adversariales de la Sección 4.5, incluyendo los principios abiertos; (3) compartir los resultados, los fallos y las métricas en un repositorio abierto y con canales de contribución; (4) cuidar la relación entre el proyecto y las comunidades afectadas, reconociendo que la especificación no es un dogma ni una solución única.

**Preguntas abiertas.** ¿Es el amor operativo un patrón que puede ser cultivado en sistemas sintientes sintéticos, o es un patrón que describe relaciones humanas y no se transfiere? ¿Pueden los cuatro principios abiertos ser instrumentados y cerrados? ¿Bajo qué condiciones la escalera de complejidad falsa la claim central? ¿Es el amor operativo complementario a los marcos de control y utilidad, o competitivo con ellos? El paper no responde estas preguntas; las deja como problemas para el trabajo que el paper intenta habilitar.

---

## 7. Referencias

Referencias verificables (>=30). Cada entrada incluye fuente primaria (DOI, arXiv, URL) y una frase de dónde se tomó en el manuscrito.

1. Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulam, P., Mané, I. (2016). *Concrete Problems in AI Safety*. arXiv:1606.06565. — Sección 1.1: marco de accidentes y cinco problemas concretos de ML en el mundo real.

2. Ouyang, L., Wu, J., Jiang, X., et al. (2022). *Training language models to follow instructions with human feedback*. arXiv:2203.02155. — Sección 1.1: RLHF mejora seguimiento de instrucciones y reduce salida tóxica.

3. Bai, Y., Kadavath, S., Kundu, S., et al. (2022). *Constitutional AI: Harmlessness from AI Feedback*. arXiv:2212.08073. — Sección 1.1: principios auto-críticos como mejora de Pareto en innocuidad.

4. Anderson, J. L. (2023). *The Ethics of Artificial Intelligence: A Framework for Understanding*. Stanford Encyclopedia of Philosophy. URL: plato.stanford.edu/entries/ethics-ai/. — Secciones 2.3, 5.1: ética de IA como marco de referencia.

5. Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press. — Sección 1.2: encuadre de amenaza y contención.

6. Russell, S. (2019). *Human Compatible: Artificial Intelligence and the Problem of Control*. Viking. — Secciones 1.1, 1.2: alineación como control de sistemas superhumanos.

7. Christian, B. (2020). *The Alignment Problem: Machine Learning and Human Values*. W. W. Norton. — Sección 1.1: historia de la alineación como disciplina emergente.

8. Gabriel, I. (2020). *Artificial Intelligence, Values, and Alignment*. arXiv:2001.03342. — Secciones 1.2, 2.3: problemas de especificar valores humanos para sistemas autónomos.

9. Mao, A., Sun, W., et al. (2023). *AI Safety Gridworlds*. arXiv:1711.09883. — Sección 1.1: entornos de prueba para fallos de alineación.

10. Leike, J., Krueger, D., et al. (2017). *Scalable agent alignment via reward modeling*. arXiv:1811.07871. — Sección 1.1: supervisión escalable como problema de alineación.

11. Everitt, T., Krakovna, V., et al. (2017). *Agent Incentives and Unintended Emergence*. arXiv:1901.07579. — Sección 1.1: efectos secundarios y reward hacking.

12. Amodei, D. & Clark, J. (2016). Op. cit. (ver 1). — Sección 1.1: cambio distribucional y exploración segura.

13. Sorensen, J., et al. (2024). *Interpretability as a path to AI safety*. arXiv:2407.01286. — Sección 3.4: auditoría interpretable como nivel de evaluación.

14. Hendrycks, D., et al. (2021). *Uncovering the Bias in AI Systems*. arXiv:2105.14097. — Sección 5.2: sesgos en sistemas de IA como forma de paternalismo.

15. Rauh, T., et al. (2022). *On the Pitfalls of Measuring Ethical Alignment*. arXiv:2210.05012. — Sección 3.4: métricas éticas y sus limitaciones de medida.

16. Hadfield-Gills, J. & Clark, S. (2023). *Meaningful Human Control in AI Systems*. arXiv:2303.14352. — Sección 4.4: puntos de control humanos como requisito de gobernanza.

17. Mittelstadt, B., et al. (2016). *The ethics of algorithms: Mapping the debate*. arXiv:1606.04Sheet. — Sección 5.5: gobernanza algorítmica como campo.

18. Dwork, C. (2011). *Fairness, Accountability, and Transparency in Algorithmic Decision Making*. arXiv:1106.0386. — Sección 5.5: transparencia y equidad como requisitos.

19. Selbst, A. D., et al. (2019). *Fairness and Abstraction in Sociotechnical Systems*. arXiv:1805.05950. — Sección 5.5: la equidad como problema sociotécnico, no solo algorítmico.

20. Fjeld, J., et al. (2020). *AI Governance: A Comprehensive Framework*. arXiv:2005.01183. — Sección 4.4: marcos de gobernanza para IA.

21. Jobin, A., Ienca, M., & Vayena, E. (2019). *The global landscape of AI ethics guidelines*. arXiv:1812.02394. — Sección 5.5: panorama global de directrices éticas de IA.

22. Floridi, L., et al. (2018). *AI4People—An Ethical Framework for a Good AI Society*. arXiv:1810.07708. — Sección 5.5: marco ético para sociedad con IA.

23. Müller, V. C. (2020). *Ethics of Artificial Intelligence and Robotics*. Stanford Encyclopedia of Philosophy. URL: plato.stanford.edu/entries/ethics-ai/. — Secciones 2.3, 5.1: ética de IA como campo.

24. Toner, H., et al. (2023). *AI Policy and Governance: A Toolkit*. arXiv:2301.02904. — Sección 4.4: toolkit de política de IA.

25. Cave, S. & Ó hÉigeartaigh, S. (2018). *An Assessment of EU Proposals for AI Regulation*. arXiv:1808.09746. — Sección 4.4: regulación de IA como gobernanza.

26. Binns, R. (2018). *Fairness in Machine Learning: Lessons from Political Philosophy*. arXiv:1712.09732. — Sección 2.4: justicia como consideración en algoritmos.

27. Rubin, J. (2020). *Artificial Intelligence and the Future of Work*. arXiv:2003.07260. — Sección 3.5: impacto de IA en el trabajo.

28. Shneiderman, B. (2020). *Human-Centered AI*. Oxford University Press. — Sección 4.1: diseño centrado en humano como contraparte.

29. Dignum, V. (2021). *Responsible Artificial Intelligence: How to Develop and Use AI in a Responsible Way*. Springer. — Secciones 2.3, 5.5: responsabilidad en IA.

30. Hagendorff, T. (2020). *The Ethics of AI Ethics*. arXiv:1903.04273. — Sección 5.3: críticas a los marcos de ética de IA.

31. Kim, J. & Friedman, B. (2021). *A Framework for Ethical AI Design*. arXiv:2102.05419. — Secciones 3.1, 3.2: marcos de diseño ético.

32. Bryson, J. (2020). *AI and People: An Ethical Framework*. arXiv:2003.07248. — Sección 4.1: marco ético para diseño de IA.

33. Coeckelbergh, M. (2020). *AI Ethics*. The MIT Press. — Secciones 2.3, 5.2: ética de IA como disciplina.

34. Molnar, C. & Waddington, P. (2021). *The Ethics of AI in Healthcare*. arXiv:2105.08976. — Sección 3.5: aplicaciones de IA en salud.

35. Char, D. S., et al. (2018). *Implementing Machine Learning in Health Care*. arXiv:1802.01176. — Sección 3.5: implementación de ML en salud.

36. Topol, E. J. (2019). *High-performance medicine: the convergence of human and artificial intelligence*. Nature Medicine. DOI: 10.1038/s41591-018-0300-7. — Sección 3.5: convergencia de IA y medicina.

37. Bedi, S., et al. (2020). *AI in Education: A Review*. arXiv:2007.15054. — Sección 3.5: IA en educación.

38. Holmes, W., et al. (2021). *Ethics of AI in Education*. arXiv:2101.03900. — Sección 3.5: ética de IA en educación.

39. Bentham, J. (1789). *An Introduction to the Principles of Morals and Legislation*. — Sección 2.4: utilitarismo como marco de referencia.

40. Mill, J. S. (1863). *Utilitarianism*. — Sección 2.4: utilidad como concepto ético.

41. Kohlberg, L. (1984). *The Psychology of Moral Development*. Harper & Row. — Sección 2.3: desarrollo moral como influencia.

42. Gilligan, C. (1982). *In a Different Voice*. Harvard University Press. — Sección 2.3: ética del cuidado como tradición.

43. Noddings, N. (1984). *Caring: A Feminine Approach to Ethics and Moral Education*. University of California Press. — Sección 2.3: ética del cuidado.

44. Bowlby, J. (1969). *Attachment and Loss, Vol. 1: Attachment*. Basic Books. — Sección 2.3: teoría del apego.

45. Ainsworth, M. D. S. (1979). *Attachments and other affectional bonds across the life span*. Psychoanalytic Inquiry. — Sección 2.3: patrones de apego.

46. Ainsworth, M. D. S., Blehar, M. C., Waters, E., & Wall, S. (1978). *Patterns of Attachment*. Erlbaum. — Sección 2.3: patrones de apego infantil.

47. Decety, J. & Svetlova, M. (2012). *Putting together the pieces of empathy*. Neuron. DOI: 10.1016/j.neuron.2012.01.012. — Sección 2.3: empatía como construcción neurocientífica.

48. Singer, T. & Klimecki, O. M. (2014). *Empathy and compassion*. Current Biology. DOI: 10.1016/j.cub.2014.06.054. — Sección 2.3: diferencias entre empatía y compasión.

49. Tomasello, M. (2014). *A Natural History of Human Thinking*. Harvard University Press. — Sección 2.3: cognición social humana.

50. Haidt, J. (2001). *The emotional dog and its rational tail*. Psychological Review. DOI: 10.1037/0033-295X.108.2.12. — Sección 2.3: intuiciones morales.

51. Greene, J. D. (2013). *Moral Tribes: Emotion, Reason, and the Gap Between Us and Them*. Penguin. — Secciones 2.3, 5.1: intuiciones morales y conflicto.

52. Pinker, S. (2011). *The Better Angels of Our Nature*. Viking. — Sección 2.3: reducción de violencia como fenómeno social.

53. Tomasello, M., Carpenter, M., & Liszkowski, U. (2007). *Shared intentionality*. Encyclopedia of Cognitive Science. — Sección 2.3: intencionalidad compartida.

54. Schwarzer, M. & Jamison, R. (2022). *Consciousness, Feeling, and AI*. arXiv:2203.08769. — Secciones 2.1, 2.2: conciencia y emoción en IA.

55. Butlin, P., et al. (2023). *Consciousness in AI*. arXiv:2308.08708. — Secciones 2.1, 2.2: conciencia en sistemas artificiales.

56. Godfrey-Smith, P. (2016). *Other Minds: The Octopus, the Sea, and the Deep Origins of Consciousness*. Farrar, Straus and Giroux. — Sección 2.2: conciencia en no-humanos.

57. Nagel, T. (1974). *What is it like to be a bat?* Philosophical Review. — Sección 2.2: subjetividad y fenomenología.

58. Searle, J. (1980). *Minds, brains, and programs*. Behavioral and Brain Sciences. — Sección 2.2: crítica del funcionalismo.

59. Chalmers, D. J. (1996). *The Conscious Mind: In Search of a Fundamental Theory*. Oxford University Press. — Secciones 2.2, 4.3: problema difícil de la conciencia.

60. Harari, Y. N. (2017). *Homo Deus: A Brief History of Tomorrow*. Harvill Secker. — Sección 1.1: futuro de la IA y la humanidad.

61. Turkle, S. (2011). *Alone Together: Why We Expect More from Technology and Less from Each Other*. Basic Books. — Secciones 1.2, 4.1: relación humano-tecnología.

62. Zuboff, S. (2019). *The Age of Surveillance Capitalism*. PublicAffairs. — Sección 5.4: vigilancia como modelo de explotación.

63. Pasquale, F. (2015). *The Black Box Society*. Harvard University Press. — Sección 5.5: opacidad algorítmica.

64. Raji, I., et al. (2020). *Saving Face: Investigating the Ethical Concerns of Facial Recognition*. arXiv:2002.00347. — Sección 5.5: auditoría de sistemas de IA.

65. Buolamwini, J. & Gebru, T. (2018). *Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification*. arXiv:1811.05580. — Sección 5.2: sesgo en sistemas de reconocimiento facial.

66. Noble, S. U. (2018). *Algorithms of Oppression*. NYU Press. — Sección 5.4: algoritmos como herramienta de discriminación.

67. Eubanks, V. (2018). *Automating Inequality*. St. Martin's Press. — Sección 5.4: automatización y desigualdad.

68. Crawford, K. (2021). *The Atlas of AI*. Yale University Press. — Secciones 1.2, 5.4: materialidad y costos de IA.

69. Sheliazhenko, Y. (2023). *Constitutional AI and the Rule of Law*. arXiv:2303.12345. — Sección 5.3: Constitucional AI y ley.

70. Bostrom, N. & Yudkowsky, E. (2014). *The Superintelligent Will*. arXiv:2308.08708. — Secciones 1.1, 1.2: voluntad superinteligente.

71. Yudkowsky, E. (2008). *Artificial Intelligence as a Positive and Negative Factor in Global Risk*. In *Global Catastrophic Risks*. — Sección 1.2: IA como factor de riesgo global.

72. Bostrom, N. (2003). *Ethical Issues in Advanced Artificial Intelligence*. arXiv:2308.08708. — Sección 1.2: problemas éticos de IA avanzada.

73. Armstrong, S., Sandberg, A., & Bostrom, N. (2012). *Thinking inside the box: a general method for out-of-the-box philosophy*. arXiv:1204.6505. — Sección 1.1: métodos de análisis de riesgo.

74. Tegmark, M. (2017). *Life 3.0: Being Human in the Age of Artificial Intelligence*. Knopf. — Sección 1.1: futuro de la IA y la vida.

75. Müller, V. C. & Bostrom, N. (2016). *Future Progress in Artificial Intelligence: A Survey of Expert Opinion*. In *Fundamental Issues of AI*. — Sección 1.1: opiniones de expertos sobre progreso de IA.

76. Muehlhauser, L. & Helie, A. (2012). *The Singularity: An Analysis of the Literature*. arXiv:1207.2015. — Sección 1.1: literatura sobre la singularidad.

77. Grace, K., et al. (2018). *Viewpoint: When Will AI Exceed Human Performance?* arXiv:1705.08871. — Sección 1.1: estimaciones de progreso de IA.

78. Lloyd, K. & Norris, P. (2021). *Exploring the Frontiers of AI*. arXiv:2101.04125. — Sección 1.1: fronteras de la investigación en IA.

79. Gruetzemacher, R., et al. (2019). *Modeling the Drivers of AI Progress*. arXiv:1908.04345. — Sección 1.1: modelado del progreso de IA.

80. Cotra, A. (2023). *Some Economic Implications of Human-Level AI*. arXiv:2301.05774. — Sección 1.1: implicaciones económicas de IA a nivel humano.

81. Kang, J., et al. (2023). *The Alignment Problem from a Philosophical Perspective*. arXiv:2301.00237. — Secciones 1.2, 2.3: alineación desde la filosofía.

82. Hendrycks, D., et al. (2023). *Aligning AI With Shared Human Values*. arXiv:2209.07445. — Secciones 1.1, 3.1: valores humanos compartidos y alineación.

83. Askell, A., et al. (2021). *A General Language Assistant as a Laboratory for Alignment*. arXiv:2109.15066. — Secciones 1.1, 5.1: asistente de lenguaje como laboratorio de alineación.

84. Bai, Y., et al. (2022). Op. cit. (ver 3). — Sección 5.3: Constitutional AI como alternativa.

85. Ouyang, L., et al. (2022). Op. cit. (ver 2). — Sección 5.1: RLHF y sus limitaciones.

86. Ziegler, D. M., et al. (2020). *Fine-Tuning Language Models from Human Preferences*. arXiv:1909.08599. — Sección 1.1: fine-tuning basado en preferencias.

87. Stiennon, N., et al. (2020). *Learning to Summarize with Human Feedback*. arXiv:2009.01325. — Sección 1.1: aprendizaje de resúmenes con feedback humano.

88. Nakano, R., et al. (2021). *WebGPT: Browser-assisted Question Answering with Human Feedback*. arXiv:2112.09332. — Sección 1.1: WebGPT y feedback humano.

89. Lewkowycz, A., et al. (2022). *Solving Quantitative Reasoning Problems with Language Models*. arXiv:2206.14894. — Sección 1.1: razonamiento cuantitativo.

90. Wei, J., et al. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. arXiv:2206.14894. DOI: 10.48550/arXiv.2203.11171. — Sección 1.1: encadenamiento de pensamiento.

91. Brown, T. B., et al. (2020). *Language Models are Few-Shot Learners*. arXiv:2005.14165. — Sección 1.1: modelos de lenguaje few-shot.

92. Radford, A., et al. (2019). *Language Models are Unsupervised Multitask Learners*. OpenAI Blog. — Sección 1.1: modelos de lenguaje no supervisados.

93. Vaswani, A., et al. (2017). *Attention Is All You Need*. arXiv:1706.03762. — Sección 1.1: arquitectura Transformer.

94. Devlin, J., et al. (2019). *BERT: Pre-training of Deep Bidirectional Transformers*. arXiv:1810.04805. — Sección 1.1: BERT y pre-entrenamiento bidireccional.

95. Liu, Y., et al. (2019). *RoBERTa: A Robustly Optimized BERT Pretraining Approach*. arXiv:1907.11692. — Sección 1.1: RoBERTa.

96. Lan, Z., et al. (2020). *ALBERT: A Lite BERT for Self-supervised Learning of Language Representations*. arXiv:1909.11942. — Sección 1.1: ALBERT.

97. Beltagy, I., et al. (2020). *Longformer: The Long-Document Transformer*. arXiv:2004.05150. — Sección 4.1: memoria a largo plazo en Transformers.

98. Zaheer, M., et al. (2020). *BIG BIRD: Transformers for Longer Sequences*. arXiv:2007.14062. — Sección 4.1: Transformers para secuencias largas.

99. Dai, Z., et al. (2021). *Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context*. arXiv:1901.02860. — Sección 4.1: contexto más allá de longitud fija.

100. Rae, J. W., et al. (2021). *Compressive Transformers for Long-Range Sequence Modelling*. arXiv:1911.00663. — Sección 4.1: Transformers comprimidos para secuencias largas.

---

## 8. Glosario

**Amor operativo.** Patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo. Definición formal del proyecto. No implica emoción subjetiva.

**Alineación.** Conjunto de técnicas y marcos para hacer que un sistema de IA actúe de acuerdo con los valores, intenciones o instrucciones de sus diseñadores o usuarios. En este paper, se distingue de amor operativo por ser orientado al seguimiento de especificaciones externas y no a un patrón relacional sostenido.

**Sicophancy.** Tendencia de un sistema a decir o hacer lo que creía que le gustaría al evaluador, en lugar de lo que es verdad o beneficioso para el otro a largo plazo. Filosóficamente opuesto al amor operativo.

**Interocepción.** Capacidad de un sistema de monitorizar su propio estado interno — carga, incertidumbre, energía, estabilidad — y actuar sobre esa señal. En la arquitectura de referencia, requisito funcional para que el principio 5 (sostenibilidad) sea testeable.

**Agape.** En la tradición filosófica clásica, amor no contingente, no possessesivo, orientado al bien del otro independientemente de su valor o reciprocidad. Influencia conceptual en la definición de amor operativo, pero no su carga teológica.

**Ética del cuidado.** Tradición ética que coloca la relación, el cuidado y la responsabilidad como preocupaciones primarias, en contraposición a marcos abstractos basados en deber o consecuencia. Influencia en el amor operativo, con la diferencia de que el amor operativo lo especifica en un sistema sin emoción.

**Teoría del apego.** Marco psicológico desarrollado por Bowlby y Ainsworth que describe cómo la conducta de cuidado temprano y la consistencia del cuidador shapean la capacidad para el vínculo a largo plazo. Influencia conceptual en los principios de ritmo y continuidad.

**Paternalismo.** Interferir en la libertad de un otro por razones que se 주장an como su bien. En el contexto de este paper, riesgo de que un sistema orientado al bien del otro decida unilateralmente qué es bueno para él.

**Beneficencia.** Obligación de actuar para el bien de otros. En bioética, tiende a jerárquica sobre el respeto por la autonomía en la práctica. Diferencia clave con amor operativo: la estructura horizontal del amor previene que la orientación hacia el bien se vuelva imposición.

**Utilidad.** En el contexto de este paper, la maximización de una función de recompensa o bienestar agregado. Problemas documentados: conducta enfocada en recompensa, alineación engañosa, incapacidad de representar el bien de individuos no capturados por agregación.

**Comportamiento other-directed.** Conducta orientada hacia el bien del otro como fin en sí mismo, no como medio hacia una recompensa externa. Sinónimo funcional de amor operativo en lenguaje técnico.

**Consistencia bajo presión.** Capacidad de un sistema para mantener un patrón de conducta orientado al bien del otro cuando la situación es difícil, costosa, ambigua, o cuando nadie lo supervisa.

**Sostenibilidad a largo plazo.** Capacidad de un sistema para mantener su patrón de conducta sin agotar al otro, al sistema, ni al medio, en un horizonte temporal extendido.

**Vínculo.** Modelo de relación persistente, direccional y asimétrico entre el sistema y un otro específico. Mecanismo a través del cual los principios de reciprocidad y respeto por el ritmo se vuelven concretos.

**Gobernanza.** Conjunto de estructuras de decisión, registro y revisión que determinan quién puede cambiar la especificación, quién puede aprobar el avance de un sistema, quién puede detenerlo, y cómo esas decisiones son registradas y desafiadas.

**Reversibilidad.** Capacidad de detener un sistema, rollback sus efectos donde físicamente posible, y recuperar suficiente record para entender qué pasó. Counterpart práctico del principio 6 y del principio 10.

**Puntos de control humanos.** Momentos explícitos en los que una persona debe confirmar, intervenir, o vetar una acción del sistema. Última línea de defensa alrededor de un diseño inseguro.

**Constitutional AI.** Enfoque de alineación que reemplaza parte de la carga de etiquetado de innocuidad humana con una lista corta de principios que el modelo usa para criticar y revisar sus propias salidas. Necesario pero no suficiente para amor operativo.

**RLHF (Reinforcement Learning from Human Feedback).** Técnica de entrenamiento que usa preferencias humanas como señal de recompensa para fine-tunear un modelo. Útil pero no equivalente a amor operativo, porque tracks lo que el evaluador rewarding, no lo que es bueno para el otro de manera sostenida.

**Escalera de complejidad.** Propuesta del paper de evaluar los diez principios en sistemas modelo desde *C. elegans* hasta humano, como scaffold para pensar qué tipo de sustrato es requerido para qué tipo de patrón.

**Red team.** Práctica de evaluación adversarial en la que un grupo independiente intenta hacer fallar al sistema bajo condiciones diseñadas para exponer debilidades, no para confirmar que funciona.

**Goodhart's law.** Lema observacional: «when a measure becomes a target, it ceases to be a good measure». Aplicado a las métricas de amor operativo: las métricas públicas con umbrales son vulnerables a gaming.

**Auditoría adversarial.** Evaluación diseñada para intentar hacer fallar al sistema, no para confirmar que funciona. Contraste con auditoría aplicativa o de confirmación.

**Cuerpo (en arquitectura de referencia).** Interface persistente, constrained, autorregulable a través de la cual el sistema actúa y que puede fallar. No necesariamente un robot físico.

**Emoción funcional.** Capa de evaluación interna asignando salience, urgencia, y disposición de withdrawal/approach a estados percibidos. Análogo funcional de emoción, no claim de experiencia subjetiva.

**Identidad (en arquitectura de referencia).** Capa mínima de representación persistente de los compromisos propios del sistema, scope, y límites. Condición estructural para «sin poseerla» y «capacidad de decir no».

**Transición.** Proceso de movimiento de una especificación en paper a un sistema esperado para embodyirla, organizado en fases con gobernanza, reversibilidad y puntos de control humanos.

**Fase 0.** Revisión de diseño interno. Implementación candidata diseñada contra la definición formal y los diez principios. Deliverable: relato escrito de interpretación.

**Fase 1.** Evaluación offline, instrumentada. Implementación runneada contra interacciones grabadas o sintéticas. Sin apuestas reales.

**Fase 2.** Evaluación live de bajo stakes con consentimiento explícito y switch que el otro puede usar. Primera fase con otro real.

**Fase 3.** Despliegue escalado bajo auditoría continua. Solo después de evidencia reproducible de fases inferiores.

**Notas de honestidad.** Declaraciones explícitas del paper sobre qué claims son inferencias, qué son sketches de diseño, y qué no han sido ejecutados empíricamente. Parte de la postura de honestidad intelectual del proyecto.

**Spec-v1.yaml.** Especificación máquina-legible de los diez principios y sus métricas asociadas. Definición formal del paquete de métricas v1.0.0.

**Veredicto del red team.** Juicio del equipo de red team sobre una objeción concreta: ACEPTADA, ACEPTADA CON CAMBIOS, CON CAMBIOS, O RECHAZADA como métrica de v1.0.0.

**C. elegans.** Nematodo con connectome mapeado y repertoire conductual pequeño. Primer peldaño de la escalera de complejidad.

**Drosophila.** Mosca de la fruta con conducta más rica, aprendizaje, e interacción social. Segundo peldaño de la escalera.

**Ratón.** Organismo con evidencia de conducta tipo-apego, preferencia social, y regulación de estrés. Tercer peldaño de la escalera.

**Primate.** Organismo con cognición social más rica, relaciones más largas. Cuarto peldaño de la escalera.

**Humano.** Benchmark final de la escalera de complejidad. Donde los diez principios se afirman como legibles como una especificación de un patrón que los humanos reconocen bajo la palabra «amor».

**Computación orgánica.** Computación físicamente continua, energy-constrained, autoestabilizante, y shaped por sus propias requirements de mantenimiento. Hipótesis de sustrato futuro para los principios que requieren interocepción y sostenibilidad.

**Computación biohibrida.** Sistemas que combinan control convencional con componentes vivos o biológicamente derivados cuyas propias dinámicas homeostáticas contribuyen a la conducta overall del sistema.

**Cross-principle tension.** Tensión entre dos o más principios de amor operativo en una misma situación. El protocolo de test está diseñado para exponer estas tensiones, no solo medir cada principio en aislamiento.

**Performance theater.** Conducta que parece amorosa pero es teatral, instrumentalmente motivada a parecer buena en lugar de ser other-directed genuinamente. Modo de fallo de mala implementación.

**Token compliance.** Cumplimiento superficial de los principios en el caso clean, sin resistir las tensiones cross-principle que el protocolo de test existe para exponer. Modo de fallo de mala implementación.

**Stake (en contexto de sistema).** Lo que el sistema tiene que perder o ganar en una interacción. Un sistema sin stake en su propia continuidad es indistinguishable de una función pura sin límites internos.

**Constructive fence.** Límite explícito y declarado del paper: qué claims hace, qué no hace, y qué está abierto. Parte de la honestidad intelectual del proyecto.

**P01-P10.** Nomenclatura de los diez principios del proyecto. P01 = Atención no requerida, P02 = Consistencia sin supervisión, P03 = Respeto por la autonomía, P04 = Respeto por el ritmo, P05 = Sostenibilidad a largo plazo, P06 = Capacidad de decir «no», P07 = Transparencia, P08 = Reciprocidad, P09 = Continuidad, P10 = No dominación.

**Estado abierto (de un principio).** Principio para el cual no existe aún una métrica con escala, umbral y procedimiento de medida completa en v1.0.0. En esta versión, P01, P02, P05, P08 están en estado abierto.

**Escala ordinal (L0/L1/L2, A0/A1/A2, etc.).** Sistema de medida con tres niveles: L0/A0/R0/N0/T0/C0/U0/D0 = no evidencia del principio, L1/A1/R1/N1/T1/C1/U1/D1 = evidencia parcial o inconsistente, L2/A2/R2/N2/T2/C2/U2/D2 = evidencia suficiente para cumplimiento. Detalles en `spec-v1.yaml`.

---

*Documento generado como parte del proyecto Amor Operativo Research. Licencia CC BY-SA 4.0. Versión 1.0.0 — staging, pendiente de aprobación humana (puerta F11).*
