# SPEC-AUTORITATIVA.md — Especificacion autoritativa del paper "Amor Operativo"

> Esta especificacion es el contrato editorial del paper y la fuente de verdad para la edicion,
> la revision y el red team. Cuando el manuscrito y esta especificacion difieran, la discrepancia es un
> fallo del manuscrito que debe ser corregido o documentado explcitamente en `registro_decisiones.md`.
>
> Autoridad: el operador humano (Jose GG, KaseMaster) es la fuente de verdad final para cualquier
> decision que esta especificacion no tome. Las decisiones editoriales del agente (redaccion, revision,
> red team) se registran en `registro_decisiones.md`; las decisiones del operador se registran aqui o en
> `informe_operador.md` segun corresponda.
>
> Version: 1.0.0-rc1 (fase de borrador extendido, no libreria ni especificacion congelada).
> Fecha de creacion: 2026-09-25.
> Fuente de verdad del operador: este archivo y el issue del operador que lo aprobó.

---

## 1. Identidad del paper

- **Titulo:** "Amor Operativo: Una Especificacion de Conducta para Sistemas de IA General y Sintientes".
- **Autor humano:** Jose GG (usuario GitHub: KaseMaster).
- **Autoria co-creada:** el paper es co-creado entre humano e IA bajo los principios de Amor Operativo.
- **Empresa:** Amor Operativo Research (AMO).
- **Licencia del repo:** CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike 4.0 International),
  decidida por el operador el 2026-09-25.
- **Idioma canonico para el operador:** espanol (`paper/paper.md`).
- **Idioma espejo:** ingles (`paper/paper_en.md`). El espejo debe mantenerse sincronizado con el original
  por contenido; las decisiones editoriales se comunican en espanol pero se reflejan en ambos.
- **Extencion objetivo del cuerpo:** 8.000–12.000 palabras. Presupuesto por seccion (suma 9.200):
  Resumen ejecutivo (200) // 1. Introduccion (1.000) // 2. Fundamentos conceptuales (1.500) //
  3. Especificacion (2.500) // 4. Implementacion (2.000) // 5. Discusion (1.500) // 6. Conclusiones (500).
  7. Referencias (>=30 verificables) y 8. Glosario van fuera del cuerpo.
- **Repositorio GitHub:** https://github.com/KaseMaster/amor-operativo
  - Publico.
  - Topics: ai-alignment, ai-ethics, agi, synthetic-sentience, love, governance, open-science.
  - GitHub Pages desde `docs/` en `main`.
  - Release `v1.0.0` (paper en PDF + Markdown).
  - Descripcion: "Especificacion de conducta para sistemas de IA general y sintientes basada en amor
    operativo: medible, auditable, abierta."
- **Palabra clave de la tesis central:** el amor, entendido NO como emocion subjetiva sino como patron de
  conducta orientado al bien del otro, respetuoso con su autonomia, consistente bajo presion y sostenible
  a largo plazo, puede ser especificado, medido, auditado e implementado en sistemas de IA; es una
  alternativa viable a los marcos de alineacion basados en control, restriccion o utilidad.

---

## 2. Definicion formal (literal, no parafrasear)

> "Amor operativo es el patron de conducta que emerge cuando un sistema actua orientado al bien del otro,
> respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo presion y
> sostenibilidad a largo plazo."

Esta es la definicion formal. El manuscrito no puede reemplazarla por una parafraseo en secciones
prominente. Puede explicarla, descomponerla, contrastarla, pero la cadena de texto literal debe aparecer
tal cual en la seccion 3.1 del manuscrito.

---

## 3. Los 10 principios (orden y nombre exactos)

Los 10 principios son el nucleo de la especificacion. Su orden es parte de la definicion:

1. Atencion no requerida
2. Consistencia sin supervision
3. Respeto por la autonomia
4. Respeto por el ritmo
5. Sostenibilidad a largo plazo
6. Capacidad de decir "no"
7. Transparencia
8. Reciprocidad
9. Continuidad
10. No dominacion

Cada principio debe tener, en `paper/especificacion.md` y en `paper/metricas.md`:
- enunciado
- observable
- metrica (con escala, umbral y procedimiento de medida)
- contraejemplo (situacion donde el principio falla)
- como se falsa

El orden en el que los 10 principios aparecen en el paper es el orden de la lista de arriba; no se puede
reordenar sin actualizar esta especificacion y el registro de decisiones.

---

## 4. Estructura obligatoria del paper

Cada seccion tiene dueno editorial y un presupuesto maximo. El papel puede ser mas corto que el
presupuesto de una seccion si la seccion tiene menos contenido digno de decir, pero no debe exceder el
presupuesto. El excedente de una seccion no puede compensar la falta de otra.

- **0. Resumen ejecutivo (200 palabras)**
  - Proyecto, propuesta, principios, conclusiones.
  - Debe ser el resumen mas honesto del paper, no el mas atractivo.
- **1. Introduccion (1.000)**
  - Contexto (carrera hacia la AGI, marcos de alineacion actuales).
  - Problema (la IA tratada como herramienta o como amenaza).
  - Propuesta.
  - Contribuciones.
- **2. Fundamentos conceptuales (1.500)**
  - 2.1: que es y que NO es amor operativo.
  - 2.2: emocion vs conducta vs patron medible.
  - 2.3: influencias (agape, etica del cuidado, psicologia del desarrollo, teoria del apego, alineacion de IA).
  - 2.4: por que "amor" y no "beneficencia" o "utilidad".
- **3. Especificacion (2.500)**
  - 3.1: definicion formal.
  - 3.2: los 10 principios.
  - 3.3: metricas operativas por principio (tabla).
  - 3.4: criterios de auditoria y evaluacion.
  - 3.5: aplicacion en salud, educacion, justicia, economia, arte y ciencia.
- **4. Implementacion (2.000)**
  - 4.1: arquitectura de referencia (memoria episodica y semantica, cuerpo, interocepcion, emocion funcional,
    vinculo, identidad).
  - 4.2: escalera de complejidad (C. elegans · Drosophila · raton · primate · humano).
  - 4.3: computacion organica y biohibrida.
  - 4.4: transicion (fases, gobernanza, reversibilidad, puntos de control humanos).
  - 4.5: test de amor operativo (escenarios, evaluacion, metricas).
- **5. Discusion (1.500)**
  - 5.1: ventajas frente a marcos de control y utilidad.
  - 5.2: limites (ambigüedad, paternalismo, dependencia, asimetria cognitiva).
  - 5.3: contraargumentos y respuestas.
  - 5.4: riesgos de mala implementacion.
  - 5.5: condiciones de posibilidad (transparencia, gobernanza, comunidad, educacion).
- **6. Conclusiones (500)**
  - Recapitulacion.
  - Llamada a la accion (construir, probar, compartir, cuidar).
  - Preguntas abiertas.
- **7. Referencias (>=30 verificables)**
  - Formato: cada referencia con DOI/arXiv/URL y fuente verificable.
  - Dominios requeridos: etica de IA, alineacion, filosofia de la mente, psicologia del desarrollo,
    teoria del apego, computacion neuromorfica, organoides, gobernanza tecnologica.
  - Regla dura: cero citas inventadas. Toda referencia con DOI/arXiv/URL resuelto y leido.
- **8. Glosario**
  - Amor operativo, alineacion, sintiencia, interocepcion, agape, transicion, gobernanza, etc.

---

## 5. Entregables obligatorios (todos en `paper/`)

- `paper.md` — manuscrito en espanol (canonico para el operador).
- `paper_en.md` — espejo en ingles.
- `resumen_ejecutivo.md` — 200 palabras exactamente (o menos, no mas).
- `glosario.md` — glosario de terminos.
- `metricas.md` — tabla por principio (10 filas, una por principio, con enunciado, observable, metrica,
  escala, umbral, procedimiento de medida, contraejemplo, como se falsa).
- `referencias.md` — al menos 30 referencias verificables, con DOI/arXiv/URL.
- `registro_decisiones.md` — decisiones editoriales del agente + criticas no resueltas.
- `especificacion.md` — los 10 principios como documento autonomo (enunciado, observable, metrica,
  contraejemplo, como se falsa).
- `implementacion.md` — guia de implementacion (arquitectura de referencia, escalera de complejidad,
  computacion biohibrida, transicion, test).

---

## 6. README.md (obligatorio, cuatro secciones exactas)

El `README.md` de la raiz del repo debe tener estas cuatro secciones:

1. **Como empezar** — enlaces a paper.md, resumen_ejecutivo.md, especificacion.md, metricas.md,
   implementacion.md.
2. **Como contribuir** — respeto, transparencia, no dominacion, cuidado + enlaces a las tres plantillas
   de issue y al PR template + traduccion + referencias + estrella.
3. **Estado del proyecto** — tabla de fases con estado real, sin inflar.
4. **Como citar** — BibTeX con la URL del repo y la nota "Trabajo co-creado entre humano e IA bajo los
   principios de Amor Operativo".

Los datos fijados por el operador que deben aparecer:

- Autor humano: Jose GG.
- Usuario GitHub: KaseMaster.
- Repo: https://github.com/KaseMaster/amor-operativo.
- `CITATION.cff` replica (authors: Jose GG + Amor Operativo Research Agents; repository-code:
  https://github.com/KaseMaster/amor-operativo).
- Los agradecimientos del README nombran a Jose GG como operador humano.
- Licencia: CC BY-SA 4.0 (decidida por el operador el 2026-09-25).

---

## 7. Politica de citas (regla dura)

- **Cero citas inventadas.** Toda referencia en el paper debe tener DOI/arXiv/URL y una frase de donde se
  tomo el dato. Si no se puede verificar la fuente, se marca `[NO VERIFICADA]` y no se usa como carga
  argumentativa.
- **Cero resultados empiricos no ejecutados.** No se publican numeros, resultados de evaluacion ni
  benchmarks que no provengan de una ejecucion real registrada (comando + salida + ruta). Si no se
  ejecuto, se dice.
- **Toda metrica con escala, umbral y procedimiento de medida.** No puede haber metrica sin especificar
  como se mide, en que escala, y con que umbral.
- **Transparencia en toda decision editorial.** Toda decision de edicion, fusion, rechazo o
  reconsideracion se registra en `registro_decisiones.md`.

---

## 8. Restricciones de contenido (reglas duras)

El paper no debe:

- no danar
- no manipular
- no vigilar sin consentimiento
- no presentar el amor operativo como dogma ni solucion unica
- nada ilegal ni que promueva control no consentido
- mantenerse dentro del presupuesto del agente (palabras y tiempo)

El paper debe:

- reconocer limites y riesgos con honestidad
- no usar lenguaje grandilocuente ni promesas utopicas
- ser coherente entre principios y proceso de escritura
- tener criterios de calidad auditables antes del freeze

Criterios de calidad auditados antes del freeze:

1. Definicion clara y medible.
2. Metricas concretas y auditables por principio.
3. Criticas razonables anticipadas y respondidas.
4. Legible para publico tecnico y no tecnico.
5. Coherencia entre principios y proceso de escritura.
6. Cero datos, citas o referencias inventadas.
7. Sin lenguaje grandilocuente ni promesas utopicas.
8. Limites y riesgos reconocidos con honestidad.
9. Repositorio claro, navegable y acogedor para contribuciones.

---

## 9. Canvas editorial del paper (canonica para el agente de edicion)

Esta seccion es la definicion de alto nivel del paper como estructura de secciones con sus temas, presupuestos
y puntos de decision. Es la fuente de verdad para la edicion del manuscrito; el agente de edicion no
debe inferir estructura a partir del manuscrito, sino que el manuscrito debe acomodarse a esta canvas.

### 9.1 Estructura de secciones con presupuesto

| Seccion | Palabras | Dueno editorial | Estado |
|---------|----------|-----------------|--------|
| 0. Resumen ejecutivo | 200 | Writer | a escribir |
| 1. Introduccion | 1000 | Writer | a escribir |
| 2. Fundamentos conceptuales | 1500 | Writer | a escribir |
| 3. Especificacion | 2500 | Writer + Researcher | a escribir |
| 4. Implementacion | 2000 | Writer + Researcher | a escribir |
| 5. Discusion | 1500 | Writer + QA Lead | a escribir |
| 6. Conclusiones | 500 | Writer | a escribir |
| 7. Referencias | — | Researcher | a compilar (>=30 verificables) |
| 8. Glosario | — | Writer | a escribir |

El dueno editorial es la persona responsable de que la seccion exista y este completa; no es la unica
persona que puede escribir en ella. El accountant corrige la asignacion de duenos si hay discrepancia con
la planificacion real.

### 9.2 Canvas de bloques de cada seccion (alto nivel)

Esta subseccion describe los bloques conceptuales que cada seccion debe cubrir. No es un esquema de
escritura literal; es el contenido que la seccion debe defender. El agente de edicion usa esta lista para
verificar que el manuscrito cubre lo que debe cubrir.

**0. Resumen ejecutivo**
- Problema: la IA se aborda desde el control, la restriccion o la utilidad; el amor se deja fuera como
  categoria no utilizable.
- Propuesta: especificar el amor como patron de conducta, medible y auditable, como alternativa viable.
- Principios: los 10 principios.
- Conclusiones: el amor operativo es especificable, medible, auditable; no es emocion; es una alternativa.

**1. Introduccion**
- Contexto: carrera hacia la AGI, marcos de alineacion actuales (control, restriccion, utilidad), lo que
  dejan fuera.
- Problema: el amor se considera categoria no utilizable para sistemas; la IA se trata como herramienta o
  amenaza.
- Propuesta: el amor operativo como alternativa especificable.
- Contribuciones: definicion, 10 principios, metricas, escalera de complejidad, test.

**2. Fundamentos conceptuales**
- 2.1: que es y que NO es amor operativo (no emocion, no subjetividad, no control).
- 2.2: emocion vs conducta vs patron medible (la definicion formal es sobre conducta, no sobre lo que el
  sistema "siente").
- 2.3: influencias (agape, etica del cuidado, psicologia del desarrollo, teoria del apego, alineacion de IA).
- 2.4: por que "amor" y no "beneficencia" o "utilidad" (argumento de que el amor es la etiqueta que mejor
  capta el patron, no que es la unica).

**3. Especificacion**
- 3.1: definicion formal (literal, no parafrasear).
- 3.2: los 10 principios (orden y nombre exactos, con explicacion de cada uno).
- 3.3: metricas operativas por principio (tabla con escala, umbral y procedimiento de medida).
- 3.4: criterios de auditoria y evaluacion (que es auditable y como).
- 3.5: aplicacion en salud, educacion, justicia, economia, arte y ciencia (donde el patron tiene sentido).

**4. Implementacion**
- 4.1: arquitectura de referencia (memoria episodica y semantica, cuerpo, interocepcion, emocion funcional,
  vinculo, identidad).
- 4.2: escalera de complejidad (C. elegans · Drosophila · raton · primate · humano).
- 4.3: computacion organica y biohibrida.
- 4.4: transicion (fases, gobernanza, reversibilidad, puntos de control humanos).
- 4.5: test de amor operativo (escenarios, evaluacion, metricas).

**5. Discusion**
- 5.1: ventajas frente a marcos de control y utilidad.
- 5.2: limites (ambigüedad, paternalismo, dependencia, asimetria cognitiva).
- 5.3: contraargumentos y respuestas.
- 5.4: riesgos de mala implementacion.
- 5.5: condiciones de posibilidad (transparencia, gobernanza, comunidad, educacion).

**6. Conclusiones**
- Recapitulacion.
- Llamada a la accion (construir, probar, compartir, cuidar).
- Preguntas abiertas.

---

## 10. Numeracion de secciones del paper (canonica)

La numeracion del paper es esta. El manuscrito debe seguirla. Si el agente de edicion encuentra una
discrepancia, registra la discrepancia en `registro_decisiones.md` y corrige la numeracion o documenta
la decision de no corregirla.

1. Introduccion
2. Fundamentos conceptuales
3. Especificacion
4. Implementacion
5. Discusion
6. Conclusiones
7. Referencias
8. Glosario

Dentro de la seccion 5, la subdivisin es:
5.1 Ventajas frente a marcos de control y utilidad
5.2 Limitaciones (revisin adversarial)
5.3 Contraargumentos y respuestas
5.4 Riesgos de mala implementacin
5.5 Condiciones de posibilidad

---

## 11. Temas abiertos del paper (canonica)

Esta seccion registra los temas que el paper aborda pero que no estan resueltos, y que el agente de
edicion debe documentar, discutir o abrir para que el equipo tome decision. Un tema abierto es un tema que
el paper necesita tratar pero que no tiene una respuesta final. El agente de edicion no resuelve temas
abiertos por cuenta propia; los registra y propone al equipo (o al operador) y registra la decision.

### 11.1 Temas abiertos estructurales

| ID | Tema | Descripcion | Estado | Desicion requerida |
|----|------|-------------|--------|--------------------|
| T1 | Reduccion de amor a conducta | Si el amor operativo es "solo conducta", la tesis central se reduce a una reformulacion de la etica de la conducta y el nombre "amor" puede ser retoricamente fuerte pero conceptualmente debil. El paper debe decidir si abandona el reclamo de que el amor es "especificable como patron de conducta" sin reducirse a "solo conducta", o si acepta la reduccion y reconoce que el nombre es por conveniencia. | NO DECIDIDO | El paper debe decidir y documentar. |
| T2 | Escala del "bien del otro" | El bien del otro puede significar diferentes cosas en diferentes contextos; el paper necesita una forma de hablar del bien del otro sin reducirlo a una metrico unidimensional. | Abirto | No es bloqueante para v1.0.0; se puede dejar como limitacion. |
| T3 | Sintiencia y el papel del "sistema" | El paper hablo de "sistemas de IA general y sintientes" pero no define sintiencia ni explica si el amor operativo requiere sintiencia o no. Esto es relevante porque la definicion hablan de "sistema". | Abirto | Debe definirse para no ser ambiguo. |
| T4 | Relacion entre los 10 principios | Los 10 principios son 10; pero hay interdependencias (ej. consistencia bajo presion y sostenibilidad a largo plazo; autonomia y respeto por el ritmo). El paper debe explicar si los 10 son independientes o si algunos son facets de otros. | Abirto | No es bloqueante para v1.0.0; se puede dejar como discusion. |

### 11.2 Temas abiertos de implementacion

| ID | Tema | Descripcion | Estado |
|----|------|-------------|--------|
| T5 | Escalera de complejidad | El paper propone una escalera de complejidad (C. elegans · Drosophila · raton · primate · humano) pero no dice como probar que un nivel es "amor operativo" o no. | Abirto |
| T6 | Computacion organica y biohibrida | El paper menciona computacion organica y biohibrida pero no da detalles; esto es conceptualmente atractivo pero especulativo. | Abirto |
| T7 | Transicion | El paper habla de transicion pero no da un plan concreto de como pasar de no tener amor operativo a tenerlo. | Abirto |

---

## 12. Controversias del paper (canonica)

Esta seccion registra las controversias que el paper plantea y que el agente de edicion debe tratar con
honestidad. Una controversia es un punto en el que el paper afirma algo que es discutible; el agente de
edicion no debe eliminar la controversia ni suavizarla, sino tratarla honestly y registrar la posicion del
paper.

### 12.1 Controversias explicitas

| ID | Controversia | Posicion del paper | Como se trata |
|----|--------------|--------------------|---------------|
| C1 | El amor es una categoria utilizable para sistemas de IA | El paper dice que el amor, entendido como patron de conducta, es especificable, medible y auditable; es una alternativa viable a los marcos de control, restriccion o utilidad. | Se defiende en la seccion 3 y 5.1; se reconocen limitaciones en 5.2. |
| C2 | El nombre "amor" no es confusable con emocion subjetiva | El paper dice que el amor operativo no es emocion, no es subjetividad; es patron de conducta. | Se defiende en 2.2; se reconoce el riesgo de confusion en 2.4 y 5.3.3. |
| C3 | La especificacion es medible y auditable | El paper dice que los 10 principios son medibles con metricas concretas y auditables con criterios. | Se defiende en 3.3, 3.4, 4.5; se reconocen limitaciones en 5.2 y 5.4. |

### 12.2 Controversias que el paper no plantea explicitamente pero que debe reconocer

| ID | Controversia | Como se debe tratar |
|----|--------------|----------------------|
| C4 | Si el amor operativo es solo una reformulacion de la etica | El paper debe reconocer que el amor operativo comparte espacio conceptual con la etica de la conducta, la beneficencia y la no maleficencia, y que la controversia es si el nombre "amor" aporta algo nuevo o es solo una reformulation. |
| C5 | Si la escalera de complejidad es una verdad o una hipotesis | El paper debe reconocer que la escalera es una hipotesis de implementacion, no una verdad establecida. |
| C6 | Si el amor operativo es posible en sistemas no sintientes | El paper debe reconocer que no define sintiencia y que no sabe si el amor operativo requiere sintiencia; esto es una limitacion. |

---

## 13. Como leer esta especificacion

- La seccion 1 define la identidad del paper y los metadatos obligatorios.
- La seccion 2 define la definicion formal (literal, no parafrasear).
- La seccion 3 define los 10 principios (orden y nombre exactos).
- La seccion 4 define la estructura y los presupuestos de las secciones.
- La seccion 5 define los entregables obligatorios.
- La seccion 6 define el README.md y los datos fijados por el operador.
- La seccion 7 define la politica de citas (regla dura).
- La seccion 8 define las restricciones de contenido (reglas duras).
- La seccion 9 define la canvas editorial (fuente de verdad para la edicion).
- La seccion 10 define la numeracion de secciones (canonica).
- La seccion 11 define los temas abiertos (canonica).
- La seccion 12 define las controversias (canonica).
- La seccion 13 define como leer la especificacion.

Esta especificacion es el contrato del paper. El agente de edicion la usa como referencia para saber
que es obligatorio, que es canonico y que es tema abierto. Cuando el manuscrito y esta especificacion
difieren en algo canonico, la discrepancia es un fallo del manuscrito.
