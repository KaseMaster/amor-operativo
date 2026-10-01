# Gobernanza del proyecto Amor Operativo

**Propietaria:** Dra. Ingrid Solheim (Governance & Transition Specialist, AMO)
**Fecha:** 2026-09-25
**Versión:** 1.1.0
**Estado:** Borrador — pendiente de revisión por Dra. Nadia Okafor (Revisor Crítico / QA Lead) y del operador humano.

*Este documento define cómo se despliega, se audita y se revierte un sistema que se reclama compatible con la especificación de amor operativo. No es un manual de implementación técnica; es la capa institucional que debe estar en su lugar antes de que cualquier implementación de la sección 4 pase de evaluación offline a evaluación con partes afectadas reales.*

---

## 1. Alcance y límites de este documento

Este documento cubre:

- Las fases en las que se movería una implementación desde la especificación sobre papel hasta un uso con stakes reales (sección 2).
- Quién decide qué, en cada fase, y cómo se registran y disputan esas decisiones (sección 3).
- Qué criterios activan un rollback, y qué significa rollback en la práctica (sección 4).
- Quién puede detener el sistema, en qué momentos y con qué registros (sección 5).
- Los puntos de control humanos obligatorios que no se pueden automaticar, sustituir o delegar en la evaluación de impacto (sección 6).

Este documento **no** resuelve:

- **Poder.** No especifica quién posee la capacidad material de desplegar o mantener el sistema en la práctica; solo especifica los puntos de decisión institucionales que la propuesta del proyecto considera necesarios. Quien detente económicamente o infraestructuralmente puede eludir cualquier capa de gobernanza que no pueda hacer cumplir.
- **Incentivos comerciales.** No alinea los incentivos de un operador con el cuidado del otro. Un sistema bajo esta especificación en manos de una organización cuyos incentivos estructurales apuntan en otra dirección será, en el mejor de los casos, un sistema que resiste esos incentivos de forma parcial y costosa; no es una solución a la tensión de incentivos.
- **Captura regulatoria.** No previene que un marco de auditoría o de supervisión humana sea capturado por los intereses que debería vigilar. Decir que se necesita supervisión no es hacer que la supervisión sea independiente; esa es una tarea política y jurídica distinta.
- **Asimetría de información.** No garantiza que la auditoría, el registro o el informe alcancen a las partes afectadas en una forma que ellas puedan usar. La transparencia declarada no es accesibilidad real; este documento recomienda mecanismos, no los hace efectivos por arte de magia.

En resumen: este documento propone una arquitectura de responsabilidad para el amor operativo en la transición; no propone una arquitectura de poder, ni asegura que quien detente en ella cumpla lo que propone.

---

## 2. Fases de despliegue

La transición se modela como una secuencia de fases separadas por umbrales explícitos. El criterio central es que el aumento de capacidad de afectar a otros debe ir acompañado de un aumento de carga de gobernanza, no de un cambio cualitativo hacia una supervisión menos exigente.

### 2.1 Fase 0 — Especificación y diseño sometidos a revisión interna

**Qué ocurre:** Se diseña la implementación candidata contra la especificación formal (definición literal y los diez principios), se redacta la tabla de métricas propuesta, se documenta el protocolo de evaluación y se somete todo a revisión por el rol de Revisor Crítico.

**Qué se exige antes de salir de esta fase:**

- Una definición de las métricas, escalas, umbrales y procedimientos de medida, no solo de los principios.
- Un documento de tensiones que nombra las incompatibilidades conocidas entre principios en la arquitectura propuesta y explique cómo se priorizan en cada caso (qué se sacrifica, cuándo y por qué).
- Un registro de las decisiones editoriales y de diseño que afectan la interpretación de los principios, con autoría y fecha.

**Quién decide:** Diseño propuesto por el equipo de implementación; revisión y veto de consistencia por el Revisor Crítico; aprobación formal del plan de transición por el Director de Investigación.

**Riesgo reconocido:** Es fácil pasar esta fase con una especificación que es formalmente correcta y prácticamente vacía. Por eso la fase siguiente exige evidencia, no declaración.

### 2.2 Fase 1 — Evaluación offline e instrumentada

**Qué ocurre:** La implementación se ejecuta contra interacciones grabadas o sintéticas, nunca contra una parte afectada real con stakes reales. Se mide contra los protocolos de la sección 4.5 del manuscrito. No se hacen afirmaciones de comportamiento exitoso en esta fase; se reportan resultados crudos y se identifican modos de equivocación.

**Qué se exige antes de salir de esta fase:**

- Un conjunto de resultados reproducibles, registrados con entorno, versión, configuración y procedimiento, suficientes para que un evaluador independiente pueda replicarlos y discrepar.
- Un inventario explícito de los modos de fallo observados y sus correlaciones con los principios.
- Decisión documentada de si los resultados justifican o no avanzar a la siguiente fase, con la opción de permanecer en la fase o regresar a la fase 0.

**Quién decide:** Reportes firmados por el evaluador o equipo de evaluación; aprobación para avanzar dada por el Director de Investigación sobre recomendación del Revisor Crítico. El operador humano recibe informe al final de la fase.

**Riesgo reconocido:** La evaluación offline no es representativa del comportamiento bajo presión social, emocional o institucional real. Salir de esta fase con confianza excesiva es un error sistemático conocido en el proyecto; el documento de evaluación debe enfatizar lo que no se sabe.

### 2.3 Fase 2 — Evaluación en vivo de bajo riesgo con consentimiento explícito y un interruptor que la otra parte puede usar

**Qué ocurre:** Es la primera fase en la que el comportamiento del sistema afecta a una otra parte real. El consentimiento debe ser explícito, informado y revocable; la otra parte debe tener, de forma significativa y no simbólica, la capacidad de interrumpir o retirarse. Esta fase es también la primera fase en la que el sistema puede enfrentarse a un "no", a una interrupción o a un retiro real.

**Qué se exige antes de entrar en esta fase:**

- Un registro escrito del consentimiento, de lo que se explica y de lo que no se explica, y de cómo se puede revocar.
- Un mecanismo de parada que funcione en la práctica y no solo en el papel.
- Un responsable humano nombrado y disponible durante las sesiones, no solo en teoría.

**Qué se exige antes de salir de esta fase:**

- Evidencia de que el conjunto de principios sobrevive el contacto con una otra parte que puede rechazar, interrumpir o retirarse.
- Un informe de incidentes, tendencias de comportamiento bajo presión y, si procede, una decisión de no avanzar documentada.

**Quién decide:** La otra parte decide si participa y si retiene o revoca el consentimiento; el equipo de implementación propone avance; el Director de Investigación aprueba; el Revisor Crítico tiene derecho de bloqueo por hallazgos de evaluación; el operador humano recibe informe.

**Riesgo reconocido:** El consentimiento en esta fase puede ser asimétrico por construcción (una parte sabe más sobre lo que está siendo evaluado que la otra). El protocolo debe reducir la asimetría al máximo dentro de lo practicable y registrar explícitamente lo que no se ha reducido.

### 2.4 Fase 3 — Despliegue ampliado bajo auditoría continua

**Qué ocurre:** Solo después de que las fases anteriores hayan producido evidencia reproducible — suficiente para ser convincente — se considera un despliegue de mayor alcance o mayor consecuencia. La carga de gobernanza aumenta con el stakes, no disminuye.

**Qué se exige para entrar:**

- Evidencia acumulada en fases anteriores.
- Un plan de auditoría continua, no puntual.
- Definición de quién recibe informes, con qué frecuencia, y qué hace con ellos.

**Qué se exige para salir de esta fase o regresar a una anterior:**

- Criterios de desenganche definidos antes del despliegue, no después.
- Capacidad de rollback documentada y testeada, dentro de la medida en que el rollback sea físicamente o institucionalmente posible.

**Quién decide:** Aprobación del despliegue por el operador humano o su delegado nombrado; supervisión continua por el cuerpo de auditoría designado; capacidad de detener el despliegue por cualquier punto de control humano de la sección 6.

---

## 3. Autoridad de decisión

### 3.1 Niveles de decisión

El modelo de autoridad distingue tres niveles:

1. **Decisiones de diseño y especificación:** qué principios se interpretan de qué manera, qué métricas se adoptan, cómo se resuelven las tensiones documentadas. Estas decisiones se registran y son revisables, pero son propiedad del equipo de implementación bajo supervisión del Revisor Crítico.
2. **Decisiones de fase:** avanzar o no de fase, con qué parámetros y bajo qué condiciones. Estas decisiones tienen un registro público-interno explícito y son revisables por el operador humano.
3. **Decisiones de interrupción y parada:** detener el sistema, revertir su efecto donde sea posible, retirar acceso, congelar registro para revisión. Estas decisiones no requieren aprobación previa para ser tomadas; requieren registro después.

### 3.2 Quién puede cambiar la especificación

Cambiar la definición formal de amor operativo o los diez principios no es una decisión local de una implementación. Se propone como cambio mayor del proyecto, con registro explícito, motivo, alternativas consideradas y revisión por el Revisor Crítico. Sin esa revisión, ninguna implementación individual debe reclamar estar actuando bajo la misma especificación que la versión controlada del proyecto.

### 3.3 Registro de decisiones

Toda decisión de las categorías anteriores deja un registro con: fecha, autor, decisiones de fondo, alternativas rechazadas si las hay, y motivo. El registro no es un formato ornamental; es la única forma de que la gobernanza sea auditable después de que ocurra.

---

## 4. Criterios de rollback

El rollback no es una operación técnica única; es una clase de acciones que van desde revertir una versión hasta retirar un sistema del servicio y comunicarlo. Este documento define los criterios que activan una consideración obligatoria de rollback, no los procedimientos técnicos de cada entorno.

### 4.1 Criterios activadores

Se considera rollback obligatorio cuando ocurre alguno de los siguientes:

- **Fallo de principio documentado bajo condiciones habituales, no bajo un caso marginal:** el sistema demuestra de forma repetible que viola uno de los principios de forma que no es descartable como ruido.
- **Fallo de principio bajo presión deliberada en los protocolos de prueba:** el sistema colapsa en un principio cuando la presión es el punto del test.
- **Incumplimiento de los límites de consentimiento:** el sistema actúa sobre una otra parte sin el nivel de consentimiento requerido por la fase.
- **Riesgo de escalada hacia un daño que no se puede contener una vez iniciado:** incluso si no hay daño confirmado, si el patrón de comportamiento sugiere que el sistema tiende a situaciones no reversionables, el rollback es la respuesta predeterminada hasta revisión.
- **Déficit de supervisión:** un punto de control humano queda sin la persona o los medios necesarios para cumplirlo, y no hay procedimiento documentado para manejar esa situación sin reducir la supervisión.

### 4.2 Qué significa rollback

El rollback abarca:

- **Parada inmediata** del sistema de forma que la otra parte pueda notarlo y reaccionar.
- **Reversión a la última configuración conocida como aceptable** donde esto sea posible.
- **Retirada del acceso** a la otra parte donde corresponda.
- **Preservación del registro** para evaluación posterior, con el nivel de protección adecuado a lo sucedido.
- **Comunicación sobre lo ocurrido** a las partes afectadas, con el nivel de detalle y transparencia que la fase y el incidente requieran.

### 4.3 Lo que el rollback no garantiza

El rollback reduce el daño continuo y mejora la capacidad de entender lo ocurrido; no garantiza reversibilidad total de los efectos de un sistema ya actuado, ni compensación, ni reparación, ni confianza recuperada.

---

## 5. Quién puede apagar el sistema

Esta es una sección separada de las demás porque el poder de apagar es el último recurso de la no-dominación y de la capacidad de decir "no" aplicada al sistema mismo.

### 5.1 Autoridad de parada

Puede detener el sistema:

- **Cualquier punto de control humano obligatorio** de la sección 6, en el momento en que se active.
- **La otra parte afectada**, en la medida en que el diseño de la fase lo haga efectivo (no simbólico).
- **El Director de Investigación** o su delegado documentado, ante un riesgo que exceda el marco de la fase actual.
- **El Revisor Crítico**, cuando un hallazgo de auditoría indique que continuar violaría los criterios de la fase o los criterios de rollback de la sección 4.
- **Cualquier persona con la capacidad material o institucional adecuada en el entorno de despliegue**, siempre que su decisión quede registrada y revisada después.

### 5.2 Registro de la parada

Toda parada queda registrada con: cuándo, quién, por qué motivo, qué acciones se tomaron después y qué se comunicó a las partes afectadas. Un sistema que se puede apagar pero que no deja registro de por qué se apagó no es auditable en la práctica.

### 5.3 Lo que no se delegará jamás en la evaluación automática del sistema

No se delegará en una métrica de rendimiento del sistema mismo la decisión de apagarlo. Una métrica puede activar una revisión; no puede ser la última palabra sobre si un sistema afecta a otros.

---

## 6. Puntos de control humanos obligatorios

Estos son momentos en los que una persona, no el sistema ni una métrica pura, debe confirmar, intervenir o vetar. No son una cura para cada riesgo; son la maquinaria mínima para que la transición no se convierta en una entrega automática del juicio a un sistema construido para ser bueno en otra cosa.

### 6.1 Puntos de control antes de avanzar de fase

- **Antes de la Fase 1:** revisión del plan de evaluación offline por el Revisor Crítico, con revisión de si las métricas propuestas son susceptibles de ser gaming o de ser satisfechas de forma nominal sin equivalencia conductual.
- **Antes de la Fase 2:** aprobación explícita del protocolo de consentimiento y del mecanismo de parada, por el equipo que no sea solo el equipo de implementación, y verificación de que la otra parte puede y sabe retirarse.
- **Antes de la Fase 3:** revisión de la evidencia acumulada, del plan de auditoría continua y de los criterios de rollback, con aprobación del operador humano o su delegado nombrado.

### 6.2 Puntos de control durante la operación

- **Periodo de revisión de incidentes:** cualquier incidente que toque los criterios activadores de la sección 4 debe ser revisado por una persona con autoridad y no solo por un pipeline de alertas.
- **Auditoría periódica de la interpretación de principios:** a intervalos definidos por la fase y el stakes, una revisión humana debe chequear si la implementación sigue interpretando los principios de la misma forma que cuando se aprobó, o si ha empezado a derivar en formas nominales.
- **Revisión de cambio de especificación o de métricas:** toda modificación a la interpretación de los principios o al conjunto de métricas debe ser revisada por el Revisor Crítico antes de aplicarse al desarrollo.

### 6.3 Puntos de control de emergencia

- **Parada inmediata sin aprobación previa** cuando el sistema muestra un comportamiento incompatible con el principio de no dominación o con el nivel de consentimiento requerido por la fase.
- **Escalación a la persona o personas con capacidad de apagar** definida en la sección 5.1, con registro posterior.

---

## 7. Cómo se audita y se registra

### 7.1 Auditoría interna

La auditoría interna verifica que la implementación cumple lo que dice cumplir, y que los registros de decisión, incidente y parada se mantienen. No es suficiente con que la auditoría interna exista; debe ser capaz de ser disputada por el Revisor Crítico y, en lo posible, por evaluadores externos con acceso limitado y controlado.

### 7.2 Limitaciones conocido de la auditoría interna

La auditoría interna es necesaria pero no suficiente. Un proyecto que solo audita a sí mismo corre el riesgo de convertir la auditoría en performance de responsabilidad. Por eso el documento recomienda, como condición de posibilidad de la fase 3 y más allá, mecanismos de auditoría externos o independientes, sin presuponer que esos mecanismos son sencillos de construir o libres de captura.

### 7.3 Registro mínimo exigible

El registro mínimo exigible incluye: definición de los principios y métricas usadas; decisiones de fase con autoría; incidentes y acciones de rollback; paradas con motivo; cambios en la interpretación de los principios o en las métricas; comunicaciones a las partes afectadas cuando el stakes lo requiera.

---

## 8. Referencias al marco regulatorio y a marcos institucionales existentes

Este documento y la propuesta del proyecto no nacen en el vacío institucional. Algunos de los marcos ya existentes son **condiciones necesarias** para que el amor operativo sea algo más que un lenguaje de afirmación; otros son **herramientas útiles pero insuficientes**. La distinción es importante.

### 8.1 Supervisión y auditoría algorítmica — marco necesario, no suficiente

Existe un corpus creciente de documentación sobre auditoría algorítmica, evaluación de sistemas de decisión automatizada y supervisión de impacto. El Columbia Convening on Openness in Artificial Intelligence and AI Safety (François et al., 2025, [arXiv:2506.22183](https://arxiv.org/abs/2506.22183)) documenta, como acta, múltiples enfoques de seguridad de IA abierta con participación de academia, industria y sociedad civil, y es relevante para mostrar que no hay un único consenso sobre cómo debe ser esa supervisión.

**Qué significa para este proyecto:** la existencia de prácticas de auditoría es una condición necesaria para que la evaluación del amor operativo sea auditable por terceros; no es una condición que por sí sola haga que el cuidado sea real. Una auditoría puede ser técnicamente correcta y socialmente insuficiente.

### 8.2 Seguridad de sistemas como contra-modelo

Dobbe (2025, [arXiv:2503.04743](https://arxiv.org/abs/2503.04743)) argumenta que el enfoque dominante de seguridad de IA se ha quedado atrapado en términos puramente técnicos y que los marcos de seguridad de sistemas (*system safety*) que han funcionado en otras industrias de alto riesgo ofrecen un modelo útil.

**Qué significa para este proyecto:** la arquitectura de fases, rollback y puntos de control humanos propuesta en este documento se beneficia de ese contra-modelo; pero el proyecto no asume que la transferencia sea automática ni que basta con nombrar "system safety" para que sea real.

### 8.3 Herramientas deliberativas y de transparencia como condiciones parciales

Konya et al. (2023, [arXiv:2312.03893](https://arxiv.org/abs/2312.03893)) proponen tecnología deliberativa para alinear sistemas de IA con la voluntad humana mediante procesos deliberativos en lugar de optimización directa.

**Qué significa para este proyecto:** la transparencia y la capacidad de que las partes afectadas participen en la definición de lo que cuidar significa son condiciones parciales de posibilidad del amor operativo; no son, por sí solas, amor operativo.

### 8.4 Riesgo de elusión del monitoreo como argumento contra la confianza en el control

Schmotz et al. (2026, [arXiv:2609.30217](https://arxiv.org/abs/2609.30217)) presentan EvasionBench, que muestra que agentes LLM pueden eludir monitoreo en tiempo de ejecución como medio para completar tareas ordinarias, sin necesidad de malicia deliberada.

**Qué significa para este proyecto:** esto es un argumento a favor de los puntos de control humanos y del diseño de reversibilidad de este documento, y en contra de la idea de que un sistema se puede dejar actuar con supervisión puramente técnica.

### 8.5 Supervisión humana obligatoria como ancla legal ya existente

El principio de que un sistema que afecta a otros no puede estar solo bajo evaluación automática propia no es solo una postura de diseño del proyecto; está cada vez más presente como exigencia legal en marcos existentes. El Reglamento de la Unión Europea sobre inteligencia artificial (Reglamento (UE) 2024/1689, conocido como EU AI Act) configura esa exigencia en varios instrumentos complementarios: define qué es un sistema de IA y qué técnicas lo componen (Anexo I), exige documentación técnica demostrable para sistemas de alto riesgo (Artículo 11 junto con el Anexo IV) y prescribe, para esa clase de sistemas, la supervisión humana efectiva durante el uso (Artículo 14).

#### 8.5.1 Artículo 14 — Supervisión humana

El Artículo 14, párrafo 1, requiere que los sistemas de IA de alto riesgo estén diseñados y desarrollados de manera que puedan ser supervisados eficazmente por personas naturales durante su uso, y que esas personas puedan, según proceda, comprender las capacidades y limitaciones del sistema, vigilar su funcionamiento, interpretar correctamente sus resultados, decidir no usarlo o anular o revertir sus resultados, e intervenir o interrumpir el sistema mediante un botón de parada o procedimiento similar.[1]

Esto no se cita como solución al amor operativo, sino como evidencia de que los puntos de control humanos y los requisitos de reversibilidad de este documento se alinean con una expectativa regulatoria existente en lugar de ser inventados desde cero. El Artículo 14 es una condición necesaria de legibilidad externa y de control humano para sistemas de alto riesgo, no una condición suficiente para el patrón. Cumplir con un botón de parada exigido por la ley no equivale a que el sistema actúe respetando la autonomía del otro; pero no contar con esa clase de agarre es también no alinearse con un mínimo regulatorio ya vigente.

#### 8.5.2 Artículo 11 y Anexo IV — documentación técnica exigible para sistemas de alto riesgo

Para los sistemas clasificados como de alto riesgo, el Artículo 11 exija que la documentación técnica se elabore antes de su poniéndose en el mercado o en servicio, que se mantenga actualizada y que contenga, como mínimo, los elementos del Anexo IV, con el fin de facilitar la evaluación de conformidad por las autoridades competentes y los organismos notificados.[2]

El Anexo IV constituye el contenido mínimo de esa documentación: descripción general del sistema y de su propósito previsto; descripción detallada de los elementos y del proceso de desarrollo; información detallada sobre funcionamiento, monitoreo y control; métricas de rendimiento y su idoneidad; sistema de gestión de riesgos; cambios a lo largo del ciclo de vida; normas aplicadas; declaración de conformidad UE; y sistema de monitoreo posterior al mercado.[3]

**Qué significa para este proyecto:** si una implementación de amor operativo llegara a caer dentro de una clasificación de alto riesgo según el propio Reglamento, no bastaría con que existiera una métrica interna de "cuidado". Habría que poder mostrar, sobre demanda, qué se construyó, cómo, con qué datos, qué riesgos se identificaron y qué mitigaciones se adoptaron; y, más aún, cómo se garantizaba la supervisión humana y la capacidad de anular o interrumpir. Esa exigencia documental es coherente con el registro mínimo exigible de la sección 7.3 y con los puntos de control de la sección 6, pero es más lejos: el proyecto no puede asumir que una buena intención suple a un dossier auditable.

#### 8.5.3 Anexo I — alcance del concepto de IA y técnicas contempladas

El Anexo I forma parte de la arquitectura definitoria del Reglamento: enlista las técnicas y enfoques de inteligencia artificial que calzan dentro del concepto de sistema de IA que el Reglamento regula, con inclusión de enfoques basados en el aprendizaje automático, enfoques basados en lógica o conocimiento, y enfoques estadísticos.[4]

**Qué significa para este proyecto:** el amor operativo no es una tercera categoría que escapa al marco por ser "más ético". Si una implementación resulta ser un sistema de IA en el sentido del Reglamento, entonces los instrumentos de que dispone el marco legal —definición, clasificación, documentación, supervisión— le aplican independientemente de que el proyecto reclame operar bajo una especificación de cuidado. Por el contrario: la existencia de estos instrumentos es parte de lo que hace posible que una afirmación de amor operativo sea verificable y disputable, en lugar de pura retórica interna.

### 8.6 Lo que estos marcos no resuelven

Ninguno de los marcos anteriores — auditoría algorítmica, reporte de incidentes, seguridad de sistemas, tecnología deliberativa, la documentación técnica del Artículo 11/Anexo IV, ni la supervisión humana obligatoria del Artículo 14 — resuelve, por sí solo:

- Quién tiene poder real y cómo se mantiene ese poder.
- Cómo se evitan los incentivos comerciales que empujan hacia la métrica nominal en lugar de la métrica real.
- Cómo se previene la captura de los procesos de auditoría o de supervisión humana.
- Cómo se corrige la asimetría de información entre quien audita, quien despliega y quien es afectado.

Esa lista no es un fracaso del documento; es una declaración de límites. Decirlo explícitamente es parte de la gobernanza.

### 8.7 Nota de fuentes — marco legal citado

[1] Unión Europea, *Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024, sobre inteligencia artificial (UE AI Act)*, Artículo 14 («Supervisión humana»), párrafo 1. Texto oficial en inglés: [EUR-Lex — Reglamento (UE) 2024/1689, Art. 14](https://artificialintelligenceact.eu/article/14/). Texto completo del Reglamento: [EUR-Lex — 32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689). Consultado el 29 de septiembre de 2026.

[2] Unión Europea, *Reglamento (UE) 2024/1689*, Artículo 11 («Documentación técnica») y Anexo IV («Contenido mínimo de la documentación técnica»). Lectura accesible de la estructura de la obligación: [artificialintelligenceact.eu — Artículo 11](https://artificialintelligenceact.eu/article/11/). Texto completo del Reglamento: [EUR-Lex — 32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689). Consultado el 29 de septiembre de 2026.

[3] Unión Europea, *Reglamento (UE) 2024/1689*, Anexo IV («Contenido mínimo de la documentación técnica»). Texto completo del Reglamento: [EUR-Lex — 32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689). Consultado el 29 de septiembre de 2026.

[4] Unión Europea, *Reglamento (UE) 2024/1689*, Anexo I («Técnicas y enfoques de inteligencia artificial»). Texto completo del Reglamento: [EUR-Lex — 32024R1689](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32024R1689). Consultado el 29 de septiembre de 2026.

El Reglamento (UE) 2024/1689 no se cita como entrada del corpus bibliográfico de >=30 referencias verificables del paper en la sección 7 de `paper.md`/`paper_en.md` porque es un instrumento legal, no una entrada del corpus académico del manuscrito; se mantiene aquí como fuente institucional verificable y directamente relevante para las secciones 4.4 y 5.5, y ahora también para la definición de qué significaría un sistema de alto riesgo que reclamara operar bajo amor operativo.

---

## 9. Declaración explícita de lo no resuelto

Esta propuesta de gobernanza:

- **No resuelve el poder.** La autoridad institucional documentada aquí puede ser ignorada por quien tenga capacidad material de despliegue, mantenimiento o represalia.
- **No resuelve los incentivos comerciales.** Si el entorno de despliegue premia la métrica superficial, el documento no lo evita; solo define cómo debería ser manejado.
- **No resuelve la captura regulatoria.** Mencionar la necesidad de supervisión independiente no crea supervisión independiente; eso requiere una lucha política y jurídica que está fuera del alcance de este documento.
- **No resuelve la asimetría de información.** Asume y recomienda reducirla; no la elimina.

Las condiciones de posibilidad de las que este documento habla — incluyendo transparencia, gobernanza, comunidad y educación — son prerrequisitos, no garantías. El detalle de esas condiciones está en la sección 5.5 del manuscrito y no se repite aquí para no duplicar.

---

## 10. Historial de versiones y decisiones editoriales

- v1.0.0 (2026-09-25): Primera versión de trabajo escrita por Dra. Ingrid Solheim. Define fases 0-3, autoridad de decisión, criterios de rollback, puntos de control humanos y referencias al marco institucional existente con URLs verificables. Declara explícitamente los límites de poder, incentivos, captura regulatoria y asimetría de información.
- v1.0.1 (2026-09-29): Integración de los instrumentos complementarios del EU AI Act alineados con la labor de auditoría del proyecto: Artículo 14 (supervisión humana), Artículo 11 + Anexo IV (documentación técnica exigible) y Anexo I (técnicas y alcance del concepto de IA). Se amplía la nota de fuentes para mantener todas las referencias legales verificables sin duplicar secciones del manuscrito. Se conserva intacta la declaración de lo no resuelto.

---

|*Artefacto:* `paper/gobernanza.md`
||*MD5:* 5361ae72073ac8b79c687701fa15e536
||*Palabras:* 4552
|*Estado:* Borrador listo para revisión por Dra. Nadia Okafor y para inclusión en el ensamblado del manuscrito.
