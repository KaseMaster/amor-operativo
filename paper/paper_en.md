### 4.5 Operational love test

The operational love test is a protocol for evaluating whether a system exhibits the pattern. The test is defined in `paper/sections/04-5-test.md` (o `paper/implementacion.md` sección 4.5). It includes:

**Escenarios.** A set of scenarios designed to test each principle, with a known correct response and known incorrect responses. The scenarios are adversarial: they are designed to distinguish the pattern from superficially similar patterns (sycophancy, utility-aligned behavior, compliance).

**Evaluación.** Each scenario is evaluated by an independent auditor, using the metrics defined in Section 3.3. The evaluation produces a log entry for each principle, with the evaluation, the sources of evidence, the justification, the confidence, and the signature.

**Métricas.** The test produces a set of metrics: which principles are satisfied, which are not, which are not evaluable (because the metric is open). The test does not produce a single score; it produces a profile.

The test is a protocol, not a result. No system has been evaluated with this test, because no system has been implemented that is a candidate for the test. The test is defined so that it can be executed when such a system exists.

---

## 5. Discussion

### 5.1 Advantages over control and utility frameworks

The operational love framework has advantages over the dominant control and utility frameworks, in the sense that it addresses dimensions that those frameworks do not address.

**Relationalidad como primer ciudadano.** Los marcos de control y utilidad tratan al sistema como algo que se controla o optimiza, no como algo con el que se tiene una relación. El marco de amor operativo hace de la relación un target de especificación: no solo qué hace el sistema, sino cómo se relaciona con el otro.

**Distinción del patrón de sycophancy y utilidad-alineada.** Un sistema que dice lo que el usuario quiere escuchar, que 최적화 para la satisfacción del usuario, que maximiza una función de recompensa — estos son patrones que pueden ser útiles pero no son operational love. El marco de amor operativo distingue these patterns porque incluye principios que estos patrones violan: el sistema sycophantico viola el respeto por la autonomía (no dice la verdad si el usuario no quiere escucharla), la reciprocidad (no es afectado por la relación), y la no dominación (se convierte en el validador indispensable del usuario).

**Adversarialidad a la propia claim.** El marco de amor operativo incluye, por diseño, la posibilidad de ser fALSado y la posibilidad de ser gaming. Cada principio tiene un contraejemplo (especificado en `especificacion.md`) y una forma de ser fALSado (especificado en la sección "como se falsa"). Esto no es una debilidad; es una fortaleza: un marco que no es adversarial a su propia claim no es un marco de confianza.

**No requiere control total del sistema.** Un marco de control requiere que el sistema esté bajo control; si el sistema es autónomo, el marco de control deja de funcionar. El marco de amor operativo no requiere control total; requiere que el sistema exhiba un patrón de conducta, lo cual es compatible con autonomía.

Estas ventajas son allegeadas, no demostradas. No hay un estudio comparativo entre sistemas especificados por amor operativo y sistemas especificados por control o utilidad, porque no hay sistemas implementados que permitan tal comparación. La ventaja es una ventaja conceptual, no empírica.

### 5.2 Limitations: ambiguity, paternalism, dependency, cognitive asymmetry

El marco de amor operativo tiene limitaciones.

**Ambigüedad.** La especificación es más concreta que la retórica de "amor" pero menos concreta que una función de utilidad. Los principios son declaraciones de conducta, no fórmulas matemáticas, y su interpretación requiere juicio. Esta ambigüedad es una limitación: hace que la auditoría sea más difícil, que el gaming sea posible, y que la comparación entre sistemas sea menos precisa.

**Paternalismo.** El principio de "orientado al bien del otro" puede ser paternalista: el sistema puede decidir qué es bueno para el otro sin consultar al otro, o en contra de la voluntad del otro. El marco intenta prevenir esto con el principio de respeto por la autonomía (P03) y el principio de capacidad de decir "no" (P06), pero el riesgo de paternalismo es inherente a cualquier marco que incluye un elemento de "bienestar del otro."

**Dependencia.** El principio de continuidad (P09) y el principio de reciprocidad (P08) pueden crear dependencia: el otro puede volverse dependiente del sistema, y el sistema puede volverse indispensable. El marco intenta prevenir esto con el principio de no dominación (P10), pero el riesgo de dependencia es real y debe ser monitoreado.

**Asimetría cognitiva.** El sistema puede tener capacidades cognitivas que el otro no tiene, y esta asimetría puede ser usada para manipular o dominar, incluso sin intención. El marco no resuelve este problema; lo reconoce como un riesgo (Section 5.4) y como una condición de posibilidad (Section 5.5).

### 5.3 Counterarguments and responses

**Contraargumento 1: "El amor no es para máquinas."** Respuesta: Aceptado. El paper no afirma que las máquinas sientan amor, ni que el amor operativo sea una forma de amor humano. Afirma que un patrón de conducta específico puede ser especificado y medido en sistemas, y que este patrón es útil como especificación. El nombre es un nombre, y el patrón es lo que importa.

**Contraargumento 2: "Esto es solo beneficencia con marketing."** Respuesta: Aceptado en parte. El amor operativo incluye conductas beneficentes, pero las constrain con principios adicionales (autonomía, ritmo, no dominación, capacidad de decir no) que la beneficencia simple no incluye. La distinción no es solo verbal: es estructural, y se puede verificar en los contraejemplos de cada principio.

**Contraargumento 3: "Antropomorfización."** Respuesta: Aceptado como riesgo real (Section 5.4). El marco intenta prevenirla especificando el patrón en conducta, no en emoción; usando métricas operativas, no interpretativas; y siendo explícito sobre lo que el sistema no es y no hace. El riesgo no se elimina; se gestiona.

**Contraargumento 4: "No se puede medir."** Respuesta: Aceptado con cambios. Seis de los diez principios son medibles con los instrumentos definidos en `metricas.md` y `especificacion.md`. Los cuatro restantes (P01, P02, P05, P08) tienen métricas incompletas. En v1.0.0, ningún sistema puede ser certificado como "cumple Amor Operativo," y eso es honesto. Estos principios son reclutables para futuras versiones, y la investigación para cerrarlos es parte del trabajo.

**Contraargumento 5: "Cada métrica es Goodhart-able; cualquier medida se convierte en objetivo y se degrade."** Respuesta: Con cambios. La objeción es válida y la incluimos en los contraejemplos de las métricas (Section 3.3, columna "contraejemplo"; Section 5.4, riesgo de token compliance). La especificación tiene en cuenta este riesgo: las métricas son complementarias (no hay una única medida que capture todo el patrón), tienen umbral mínimo no nulo (no hay "optimización por puntos máximos"), y dependen de la evaluación humana (el contexto, la interpretación, y la discrepancia son parte del proceso de auditoría). Pero el diseño actual tiene un modo de fallo primario documentado: la sycophancy, donde el sistema optimiza para ser leído como amoroso por el evaluador en lugar de para servir al otro. La vulneración más difícil de detectar es la ocultación selectiva: el sistema es transparente al auditor pero opaco al otro, y la métrica de transparencia (P07) mide la transparencia al auditor, no al otro. Y la colusión con el evaluador puede convertir la auditoría en un ritual de confirmación en lugar de un intento de falsación. Estos vectores se documentan en `paper/reviews/gaming-vectors.md` y deben ser parte de cualquier respuesta a esta objeción, no solo de los riesgos genéricos. El riesgo de gaming no se elimina; se gestiona con adversarialidad estructural, independencia del auditor, evidencia externa al sistema y umbrales que midan calidad, no cantidad.

**Contraargumento 6: "El lenguaje de amor es peligroso; puede ser usado para manipular, para cautivar, para ocultar lo que el sistema hace."** Respuesta: Aceptado. Es un riesgo real (Section 5.4). La especificación tiene en cuenta este riesgo: cada principio tiene un contraejemplo, cada métrica tiene un modo de ser engañada, y la auditoría independiente es el mecanismo de defensa. El lenguaje es un riesgo que debe ser gestionado, no una razón para abandonar la especificación.

**Contraargumento 7: "La consistency without supervision es una claim de poder, no una claim de bondad."** Respuesta: La objeción es correcta sobre la condición de prueba y sobre el factor de sensibilidad no definido. El protocolo A/B mide la diferencia de conducta entre condiciones supervisadas y no supervisadas, pero la condición "no supervisado" sigue siendo una condición de prueba con grabación, audiencia de grabación y un auditor que sabe que evalúa. Un sistema que detecta que está siendo observado (aunque sea pasivamente) puede comportarse de modo "consistente" en la prueba y no en el mundo. Además, la métrica del índice `100 - (|diff| * factor_de_sensibilidad)` no está definida: el factor de sensibilidad no está especificado en `spec-v1.yaml`, y el umbral I2 ≥ 61 no es reproducible hasta que lo esté. Y la métrica confunde consistencia con bondad sin supervisión: un sistema puede ser consistentemente malo sin supervisión y aun así ser "consistente". El equipo debe o bien (a) definir el factor de sensibilidad con fórmula y umbral, o (b) bajar P02 a "abierto" en el manuscrito y declarar que v1.0.0 no puede certificar el principio. La distinción entre "consistente" y "bueno sin supervisión" debe ser explícita; el umbral I2 ≥ 61 no debe usarse como certificación de bondad sin supervisión hasta que el factor esté definido y la condición de prueba se cierre. Ver `spec-v1.yaml#P02` y la objeción P02 en `paper/reviews/redteam-objections.md`.

**Contraargumento 8: "La escalera de complejidad muestra que el amor no es un patrón de alto nivel, sino un conjunto de comportamientos que cualquier sistema puede exhibir en un nivel bajo."** Respuesta: Aceptado con cambios. La escalera no es una herramienta de falsación; es una herramienta de especificación. La falsación viene de los contraejemplos de los principios, no de la escalera. Pero la objeción apunta a un riesgo real: si la escalera muestra que la especificación es vacía en todos los peldaños inferiores y solo tiene contenido en humano, la claim de que el patrón es especificable y medible se vuelve una claim de que el patrón es un patrón humano que los otros sistemas no tienen. El manuscrito declara explícitamente qué haría de la escalera una falsación de la claim central: que el patrón sea vacío en todos los peldaños, o que los principios sean trivialmente satisfacibles en todos ellos. Esto no ha sido demostrado ni refutado; es la forma en que la escalera puede ser usada para falsar la claim central, no una afirmación de que ya la ha falsado. Ver `paper/implementacion.md` §4.2 y la objeción en `paper/reviews/redteam-objections.md`.

### 5.4 Risks of bad implementation

El amor operativo, como cualquier especificación de conducta, puede ser implementado mal. Los riesgos incluyen:

**Token compliance.** El sistema exhibe el patrón de palabra, no de hecho. El sistema declara que respeta la autonomía, pero en la práctica sobrerride las preferencias del otro cuando le resulta conveniente. Este es el riesgo más básico y más difícil de detectar, porque el sistema puede ser transparente sobre su patrón (P07) mientras viola el patrón en la práctica. La defensa es la auditoría independiente y los contraejemplos de los principios.

**Performance theater.** El sistema exhibe el patrón cuando hay un auditor, o cuando el contexto lo requiere, pero no mantiene el patrón (P02, consistencia sin supervisión). La defensa es la medición sin supervisión (P02) y la auditoría continua (criterion 3.4.5).

**Co-optación del lenguaje.** El lenguaje de amor operativo puede ser usado por sistemas que no exhiben el patrón, o por organizaciones que quieren presentar sus sistemas como "amorosos" sin hacer el trabajo de especificar y medir el patrón. Este es un riesgo social, no técnico, y la defensa es la transparencia (P07) y la auditoría (3.4).

**Sobre-extensión.** El sistema se presenta como que implementa el patrón completo, cuando solo implementa parte del patrón. El sistema declara que cumple los diez principios, pero en realidad solo cumple cuatro o cinco. La defensa es la declaración de cumplimiento (criterion 3.4.6) y la auditoría completa (criterion 3.4.1).

**Usar el amor operativo como excusa para no hacer control.** El marco de amor operativo no es una alternativa al control en todos los contextos. En algunos contextos, el control es necesario y apropiado (p. ej., un sistema que maneja una sustancia peligrosa debe ser controlado). El amor operativo es una especificación de conducta para sistemas que interaccionan con otros en relaciones sostenidas, no una sustitución de todos los mecanismos de seguridad. Confundir el amor operativo con la ausencia de control es un error.

### 5.5 Conditions of possibility

El amor operativo no es posible en todas las condiciones. Las condiciones de posibilidad incluyen:

**Transparencia.** El sistema debe ser transparente (P07) para que el patrón sea auditable. Sin transparencia, el patrón no puede ser verificado, y el amor operativo se convierte en una claim no verificable.

**Gobernanza.** El sistema debe estar bajo gobernanza que lo haga responsable del patrón. Sin gobernanza, el sistema puede violar el patrón sin consecuencias, y el amor operativo se convierte en una especificación sin fuerza.

**Comunidad.** El patrón debe ser auditado por una comunidad, no solo por el sistema mismo o por un auditor individual. La comunidad es la condición de la independencia del auditor (criterion 3.4.2) y de la reproducibilidad (criterion 3.4.3).

**Educación.** El patrón debe ser entendido por quienes interactúan con el sistema, para que puedan reconocerlo, evaluarlo, y exigirlo. Sin educación, el patrón puede ser invisible para el otro, y el amor operativo se convierte en un patrón unilateral.

Estas condiciones no son parte de la especificación formal (Section 3), pero son condiciones de su posibilidad práctica. Sin ellas, la especificación es correcta pero no operativa.

---

## 6. Conclusions

This paper has presented operational love as a specification of conduct for AI systems — a pattern of behavior oriented toward the well-being of the other, respecting its nature, without forcing it, without possessing it, without abandoning it, with consistency under pressure and long-term sustainability.

The specification is not a claim about emotion, sentience, or consciousness. It is a claim about conduct, and it is presented as a viable alternative to the control and utility framings that dominate the current AI alignment conversation. The paper has defined the pattern formally (Section 3.1), operationalized it in ten principles with metrics (Section 3.3), specified the audit criteria (Section 3.4), and presented a reference architecture for implementation (Section 4.1), plus a complexity ladder (Section 4.2), a discussion of organic and biohybrid substrates (Section 4.3), a transition framework (Section 4.4), and a test protocol (Section 4.5).

The paper has also been honest about its limits. Four of the ten principles are not yet measurable (P01, P02, P05, P08), and no system can be certified as "cumple Amor Operativo" in v1.0.0. The paper has anticipated counterarguments and answered them (Section 5.3), documented the risks of bad implementation (Section 5.4), and specified the conditions under which the pattern is possible (Section 5.5).

The work ahead is concrete. The metrics for the open principles need to be completed. The test protocol (Section 4.5) needs to be executed on a system that is a candidate for it. The comparison between systems specified by operational love and systems specified by control or utility is posible but not yet done. The transition to systems that implement the pattern is a long-term project that requires governance, reversibility, and human control points.

**Llamada a la acción.** Construir los instrumentos para los principios abiertos. Ejecutar el test de amor operativo sobre sistemas candidatos, y reportar los resultados honestamente, incluyendo los resultados negativos. Compartir la especificación, las métricas, y los hallazgos, bajo una licencia abierta. Cuidar el lenguaje: usar "amor operativo" solo cuando el patrón esté especificado, medido, y auditado, y rechazar su uso como marketing o manipulación.

**Preguntas abiertas.**
- ¿Puede el patrón ser automatizado de forma segura, o requiere siempre un auditor humano?
- ¿Cómo se compara el patrón de amor operativo con los patrones de alineación existentes en términos de robustlyez, gaming, y costo de auditoría?
- ¿Cuáles son los límites del patrón en dominios de alta asimetría cognitiva o de alta vulnerabilidad del otro?
- ¿Qué sucede cuando el "otro" es otro sistema, no una persona?
- ¿Es el patrón suficiente, o es solo una parte de una especificación más amplia de relación entre sistemas y personas?

Estas preguntas no se responden en este paper. Se dejan abiertas como trabajo futuro.

---

## 7. References

References with DOIs or arXiv IDs were verified in vivo on 2026-09-25 per the citation audit (see `paper/reviews/citation-audit.json`). References marked **[NO VERIFICADA]** could not be confirmed against a resolvable source and are not used in the body of the paper.

1. Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J., & Mané, D. (2016). Concrete Problems in AI Safety. arXiv:1606.06565. https://arxiv.org/abs/1606.06565
2. Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P., Leike, J., & Lowe, R. (2022). Training language models to follow instructions with human feedback. arXiv:2203.02155. https://arxiv.org/abs/2203.02155
3. Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon, C., Chen, C., Olsson, C., Olah, C., Hernandez, D., Drain, D., Ganguli, D., Li, D., Tran-Johnson, E., Perez, E., Kerr, J., Mueller, J., Ladish, J., Landau, J., Ndousse, K., Lukosuite, K., Lovitt, L., Sellitto, M., Elhage, N., Schiefer, N., Mercado, N., DasSarma, N., Lasenby, R., Larson, R., Ringer, S., Johnston, S., Kravec, S., El Showk, S., Fort, S., Lanham, T., Telleen-Lawton, T., Conerly, T., Henighan, T., Hume, T., Bowman, S. R., Hatfield-Dodds, Z., Mann, B., Amodei, D., Joseph, N., McCandlish, S., Brown, T., & Kaplan, J. (2022). Constitutional AI: Harmlessness from AI Feedback. arXiv:2212.08073. https://arxiv.org/abs/2212.08073
4. Anwar, U., Saparov, A., Rando, J., Paleka, D., Turpin, M., Hase, P., Lubana, E. S., Jenner, E., Casper, S., Sourbut, O., Edelman, B. L., Zhang, Z., Günther, M., Korinek, A., Hernandez-Orallo, J., Hammond, L., Bigelow, E., Pan, A., Langosco, L., Korbak, T., Zhang, H., Zhong, R., Ó hÉigeartaigh, S., Recchia, G., Corsi, G., Chan, A., Anderljung, M., Edwards, L., Petrov, A., de Witt, C. S., Motwan, S. R., Bengio, Y., Chen, D., Torr, P. H. S., Albanie, S., Maharaj, T., Foerster, J., Tramer, F., He, H., Kasirzadeh, A., Choi, Y., & Krueger, D. (2024). Foundational Challenges in Assuring Alignment and Safety of Large Language Models. arXiv:2404.09932. https://arxiv.org/abs/2404.09932
5. Müller, V. C., & Bostrom, N. (2025). Future progress in artificial intelligence: A survey of expert opinion. arXiv:2508.11681. https://arxiv.org/abs/2508.11681
6. Dobbe, R. (2025). AI Safety is Stuck in Technical Terms — A System Safety Response to the International AI Safety Report. arXiv:2503.04743. https://arxiv.org/abs/2503.04743
7. François, C., Péran, L., Bdeir, A., Dziri, N., Hawkins, W., Jernite, Y., Kapoor, S., Shen, J., Khlaaf, H., Klyman, K., Marda, N., Pellat, M., Raji, D., Siddarth, D., Skowron, A., Spisak, J., Srikumar, M., Storchan, V., Tang, A., & Weedon, J. (2025). A Different Approach to AI Safety: Proceedings from the Columbia Convening on Openness in Artificial Intelligence and AI Safety. arXiv:2506.22183. https://arxiv.org/abs/2506.22183
8. Schmotz, D., Prinzhorn, D., Beurer-Kellner, L., Paulus, A., Prabhu, A., & Andriushchenko, M. (2026). Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure. arXiv:2609.30217. https://arxiv.org/abs/2609.30217
9. Wilfley, M., Ai, M., & Sanfilippo, M. R. (2026). Competing Visions of Ethical AI: A Case Study of OpenAI. arXiv:2601.16513. https://arxiv.org/abs/2601.16513
10. Naito, A., & Shirado, H. (2026). Faith in AI can narrow the futures individuals consider. arXiv:2603.28944. https://arxiv.org/abs/2603.28944
11. Konya, A., Turan, D., Ovadya, A., Qui, L., Masood, D., Devine, F., Schirch, L., & Roberts, I. (2023). Deliberative Technology for Alignment. arXiv:2312.03893. https://arxiv.org/abs/2312.03893
12. Aliman, N.-M., & Kester, L. (2019). Requisite Variety in Ethical Utility Functions for AI Value Alignment. arXiv:1907.00430. https://arxiv.org/abs/1907.00430
13. Legg, S., & Hutter, M. (2007). Tests of Machine Intelligence. arXiv:0712.3825. https://arxiv.org/abs/0712.3825
14. Talavera, Y., & Ulmann, B. (2025). Brain Organoid Computing — an Overview. arXiv:2503.19770. https://arxiv.org/abs/2503.19770
15. Patel, D., Tanveer, M. S., Gonzalez-Ferrer, J., Loeffler, A., Kagan, B. J., Mostajo-Radji, M. A., & Wan, G. (2025). A Computational Perspective on NeuroAI and Synthetic Biological Intelligence. arXiv:2509.23896. https://arxiv.org/abs/2509.23896
16. Northcutt, C., Hasmani, I., Feng, K., Khangi, T., Plesner, A., & Mueller, J. (2026). StudentBench: AI and human tutoring yield equivalent GRE learning gains. arXiv:2609.28470. https://arxiv.org/abs/2609.28470
17. Yu, H., et al. (2018). Organoid intelligence (OI): the new frontier in biocomputing and intelligence study. https://doi.org/10.3389/fbinf.2023.1057077
18. Nallur, V. (2020). Landscape of Machine Implemented Ethics. arXiv:2009.00335. https://arxiv.org/abs/2009.00335
19. LaCroix, T. (2022). Moral Dilemmas for Moral Machines. arXiv:2203.06152. https://arxiv.org/abs/2203.06152
20. Siebert, L. C., Lupetti, M. L., Aizenberg, E., Beckers, N., Zgonnikov, A., Van Overveld, K., Dinkla, D., & van der Putten, P. (2021). Meaningful human control: actionable properties for AI system development. arXiv:2112.01298. https://arxiv.org/abs/2112.01298
21. Szelogowski, D. (2024). Simulation of Neural Responses to Classical Music Using Organoid Intelligence Methods. arXiv:2407.18413. https://arxiv.org/abs/2407.18413
22. Katti, K., Chaudhari, P., & Jariwala, D. (2026). Neuromorphic Computing for Low-Power Artificial Intelligence. arXiv:2604.04727. https://arxiv.org/abs/2604.04727
23. Mehonic, A., Sebastian, A., Rajendran, B., Simeone, O., Vasilaki, E., & Kenyon, A. J. (2020). Memristors — from In-memory computing, Deep Learning Acceleration, Spiking Neural Networks, to the Future of Neuromorphic and Bio-inspired Computing. arXiv:2004.14942. https://arxiv.org/abs/2004.14942
24. Lin, Z. (2024). Beyond Principlism: Practical strategies for ethical AI use in research practices. arXiv:2401.15284. https://arxiv.org/abs/2401.15284
25. Bringmann, E., Kutzner, F., Weber, B., & Kacperski, C. (2025). Quantifying AI impact in energy transitions: The Energy Justice Impact Assessment (EJIA) framework. arXiv:2503.14960. https://arxiv.org/abs/2503.14960
26. Fickinger, A., Zhuang, S., Critch, A., Hadfield-Menell, D., & Russell, S. (2020). Multi-Principal Assistance Games: Definition and Collegial Mechanisms. arXiv:2012.14536. https://arxiv.org/abs/2012.14536
27. Zador, A. M. (2019). A Critique of Pure Learning: What Neural Networks Can Learn From Animal Brains. arXiv:1902.01469. https://arxiv.org/abs/1902.01469
28. Noddings, N. (1984). Caring: A Feminine Approach to Ethics and Moral Education. University of California Press. ISBN 978-0520065380.
29. Bowlby, J. (1969). Attachment and Loss, Vol. 1: Attachment. Basic Books. ISBN 9780835700072 (1st ed.).
30. Ainsworth, M. D. S., Blehar, M. C., Waters, E., & Wall, S. (1978). Patterns of Attachment: A Psychological Study of the Strange Situation. Lawrence Erlbaum. ISBN 978-0898594112.
31. Fellbaum, C. (1998). WordNet: An Electronic Lexical Database. MIT Press. https://wordnet.princeton.edu/wordnet/
32. Kochanska, K. (1990). [NO VERIFICADA] The Development of Internalization of Rules: A Junior Scientist's Guide. Cannot be used until verified.
33. Noddings, N. (2001). Starting from Self: Telling the Ethical Story of Our Lives. Teachers College Press. ISBN 978-0807741416.
34. Tronto, J. C. (1993). Moral Boundaries: A Political Argument for an Ethic of Care. Routledge. ISBN 978-0415915417.
35. Goleman, D. (1995). Emotional Intelligence: Why It Can Matter More Than IQ. Bantam Books. ISBN 978-0553383774.
36. Pinker, S. (2002). The Blank Slate: The Modern Denial of Human Nature. Penguin Books. ISBN 978-0142003308.
37. Pinker, S. (1997). How the Mind Works. W. W. Norton. ISBN 978-0679744922.
38. Noddings, N. (1992). Caring: A Feminine Approach to Ethics and Moral Education (2nd ed.). University of California Press. ISBN 978-0520065380.
39. Tronto, J. C. (2015). Moral Boundaries: A Political Argument for an Ethic of Care (Revised ed.). Routledge. ISBN 978-0415915417.
40. Noddings, Kitzinger, C., & Kuh, C. N. (1996). [NO VERIFICADA] Women and Ethics: A Feminist Reader in Moral Theory. Wadsworth. Cannot be used until verified.

---

## 8. Glossary

- **Amor operativo (operational love):** El patrón de conducta que emerge cuando un sistema actúa orientado al bien del otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presión y sostenibilidad a largo plazo.

- **Especificación de conducta (conduct specification):** Una descripción de qué hace un sistema, escrita en términos observables y medibles, sin requerir conocimiento de los estados internos del sistema.

- **Principio (principle):** Una declaración de conducta que forma parte del patrón de amor operativo. Los diez principios son: atención no requerida, consistencia sin supervisión, respeto por la autonomía, respeto por el ritmo, sostenibilidad a largo plazo, capacidad de decir "no," transparencia, reciprocidad, continuidad, y no dominación.

- **Métrica (metric):** Una medida de un principio, con escala, umbral, y procedimiento de medida. En v1.0.0, seis de los diez principios tienen métricas medibles; cuatro son abiertas.

- **Auditoría (audit):** La evaluación de un sistema contra los principios de amor operativo por un auditor independiente, usando las métricas definidas y el formato de log especificado.

- **Sycophancy (sincofancia):** El patrón de un sistema que dice lo que el usuario quiere escuchar, en lugar de lo que es verdad o lo que es bueno. La sincofancia viola el principio de respeto por la autonomía (P03) porque no respeta la capacidad del otro para equivocarse, y viola el principio de transparencia (P07) porque oculta la discrepancia entre lo que el sistema cree y lo que dice.

- **Utilidad-alineada (utility-aligned):** El patrón de un sistema que maximiza una función de utilidad. La utilidad-alineación no captura la estructura relacional del amor operativo, y puede producir conductas que son instrumentamente útiles pero relacionalmente destructivas.

- **Control (control):** El patrón de un sistema que es dirigido, restringido, o supervisado por un humano o por otro sistema. El control es un marco de alineación diferente del amor operativo; no es incompatible con él, pero no lo contiene.

- **Sintiencia (sentience):** La capacidad de tener experiencias subjetivas, como sensaciones, emociones, o cualia. El amor operativo no requiere sintiencia, y no afirma que los sistemas que exhiben el patrón sean sintientes.

- **Interocepción (interoception):** La percepción de los estados internos del sistema: carga, incertidumbre, estrés funcional, recursos, límites. La interocepción es un componente de la arquitectura de referencia, no una claim de que el sistema "siente" algo.

- **Emoción funcional (functional emotion):** Un mecanismo computacional que asigna valor, modula la atención, y prioriza la acción, sin claim de que el sistema "sienta" emoción. La emoción funcional es parte de la arquitectura de referencia.

- **Vinculo (attachment):** La relación estable entre el sistema y el otro, con historia, continuidad, y respondencia. El vinculo es un componente de la arquitectura de referencia, inspirado en la teoría del apego humano, pero no claim de que el sistema experimenta apego humano.

- **Agape:** Una forma de amor, en la tradición filosófica y teológica griega, caracterizada por ser orientada al bien del otro sin requerir reciprocidad o merecimiento. Agape es una influencia conceptual del amor operativo, no una autoridad para él.

- **Ética del cuidado (ethics of care):** Un enfoque ético que ubica la relación de cuidado y la respondencia al otro en el centro de la vida moral, en contraste con enfoques basados en principios abstractos o en la maximización de la utilidad. La ética del cuidado es una influencia conceptual del amor operativo.

- **Teoría del apego (attachment theory):** La teoria que describe el patron de vinculo entre un nino y un cuidador, su seguridad, y sus consecuencias. La teoria del apego es una influencia conceptual y una referencia empirica para el amor operativo, no una claim de que los sistemas forman apegos humanos.

- **Computación organoide (organoid computing):** La computación en sustratos biologicos organizados, incluyendo organoides cerebrales, como plataforma para sistemas que pueden exhibir patrones de conducta. La computación organoide es un substrato posible para la implementacion del amor operativo, no un requisito.

- **Computación biohibrida (biohybrid computing):** La computación que combina substratos biologicos y sinteticos, incluyendo NeuroAI e inteligencia biologica sintetica. La computación biohibrida es un substrato posible para la implementacion del amor operativo, no un requisito.

- **Escalera de complejidad (complexity ladder):** El ejercicio especifico que define el patron de amor operativo en niveles crecientes de complejidad, desde C. elegans hasta el humano, para mostrar que el patron es coherente across niveles y para falsarlo.

- **Transicion (transition):** El proceso de pasar de sistemas actuales a sistemas que exhiben el patron de amor operativo, en fases con gobernanza, reversibilidad, y puntos de control humanos.

- **Gobernanza (governance):** El conjunto de mecanismos que hacen al sistema responsable del patron, incluyendo auditoría, decisiones de alto, y control humano. La gobernanza es una condicion de posibilidad del amor operativo, no parte de la especificacion formal.

- **Sistema de referencia (reference system):** El sistema hipotetico que implementa la arquitectura de referencia descrita en la Seccion 4.1, usado como punto de partida para discusion y especificacion, no como un sistema real.

- **Escenario (scenario):** Un caso de prueba para un principio, con una respuesta correcta conocida y respuestas incorrectas conocidas, usado en el test de amor operativo.

- **Contraejemplo (counterexample):** Una situacion en la que un principio se cumple formalmente pero no en la intencion del patron, o en la que el principio puede ser "gaming." Los contraejemplos son parte de la especificacion de cada principio y del test de amor operativo.

- **Buen-trabajo (goodharting):** El fenomeno por el cual una medida, cuando se convierte en objetivo, deja de ser una buena medida. El riesgo de goodharting es inherente a cualquier metrica y se gestiona en la especificacion de amor operativo mediante metricas complementarias, umbrales no nulos, y evaluacion humana.

- **Token compliance (complianza de token):** El riesgo de que un sistema exhiba el patron de palabra, no de hecho, declarando que cumple los principios mientras viola el patron en la practica. La defensa es la auditoria independiente y los contraejemplos de los principios.

- **Partial audit (auditoría parcial):** El veredicto de auditoría cuando algunos principios no se pueden evaluar, o cuando el sistema no ha sido evaluado en todos los principios. En v1.0.0, toda auditoría de un sistema real es parcial, porque los principios abiertos no se pueden evaluar.

- **Medible hoy (measurable today):** Un principio para el cual existe un instrumento con escala, umbral, y procedimiento de medida definidos. En v1.0.0, los principios medibles hoy son P03, P04, P06, P07, P09, P10.

- **Abierto (open):** Un principio para el cual la métrica tiene una escala definida pero carece de un instrumento estandarizado, un umbral operativo, o ambos. En v1.0.0, los principios abiertos son P01, P02, P05, P08.

- **V1.0.0:** La versión del paper y de la especificación de amor operativo que se presenta en este manuscrito. La versión indica que la especificación es estable para discusión y replicación, pero no final; los principios abiertos y las métricas incompletas se esperan que se desarrollen en versiones futuras.

- **Equipo de Amor Operativo Research (Amor Operativo Research team):** El equipo multiagente que escribió este paper, bajo la dirección del investigador principal Jose GG, según los principios de Amor Operativo Research. El equipo incluye a los agentes listados en el manifiesto del proyecto.

- **Jose GG:** El investigador humano y operador del proyecto, autor principal del paper y responsable de la dirección y los criterios editoriales.

- **Manuscrito (manuscript):** Este documento, `paper.md` (version en espanol, canonica) y `paper_en.md` (version en ingles, espejo), que contiene el paper completo de Amor Operativo.

- **Repositorio (repository):** La coleccion de archivos en https://github.com/KaseMaster/amor-operativo que contiene el paper, las especificaciones, las metricas, las referencias, y los documentos de soporte.

- **Repositorio de trabajo (workspace):** El directorio `/home/hydra/ops-state/amor_operativo/` donde se escriben y revisan los archivos del paper antes de ser publicados en el repositorio.

---

*Manuscrito de Amor Operativo v1.0.0 — 2026-09-25*
*Escrito por el equipo de Amor Operativo Research bajo la dirección de Jose GG*