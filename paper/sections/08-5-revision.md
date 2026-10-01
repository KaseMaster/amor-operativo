# Revisión de la sección 8 de `paper/gobernanza.md`

## 1. Propósito

Esta revisión se aplica a la sección 8 de `paper/gobernanza.md` (Referencia al marco regulatorio y a marcos institucionales existentes) con el objetivo de confirmar o corregir la veracidad de sus afirmaciones sobre autoridad legal, requisitos de documentación y supervisión humana para sistemas de inteligencia artificial. Esta revisión no es opcional: el propio documento declara que esta sección justifica su propia existencia y su participación en la gobernanza del proyecto. Si la sección 8 no es verificable, la gobernanza del proyecto no tiene la base que reclama.

## 2. Criterios de revisión

Las siguientes preguntas deben responder sí o no con evidencia local o verificable:

1. ¿El Reglamento (UE) 2024/1689 existe y es aplicable a sistemas de IA que afecten a personas reales en la UE?
2. ¿El artículo 14 párrafo 1 dice lo que el documento afirma que dice?
3. ¿Los artículos 11 y Anexo IV exigen documentación técnica antes del puesto en mercado o servicio?
4. ¿El Anexo I define qué técnicas entran en el concepto de sistema de IA?
5. ¿Las referencias URL del documento resuelven a los textos esperados?
6. ¿La sección declara correctamente lo que no resuelve?

## 3. Resultado de revisión

### 3.1 Existencia y aplicabilidad del Reglamento (UE) 2024/1689

**Respuesta: Sí, verificado.** El Reglamento (UE) 2024/1689 (UE AI Act) fue publicado en el DOUE el 12 de julio de 2024 y entra en vigor de forma escalonada. Su alcance incluye sistemas de IA que afecten a personas naturales dentro del espacio de la UE, con especial atención a los sistemas de alto riesgo definidos en el Anexo III y a los requisitos de documentación y supervisión que esos sistemas deben cumplir. Esta no es una afirmación especulativa del proyecto; es un instrumento legal vigente.

**Evidencia esperada para auditoría externa:**
- Publicación oficial en el DOUE: DOUE L 2024/1689 (o referencia equivalente en EUR-Lex con el número CELEX 32024R1689).
- Entrada en la base de datos de legislación de la UE con fecha de publicación, fecha de entrada en vigor y calendario de aplicación.

**Estado del proyecto:** el documento cita la referencia legal correctamente y la diferencia entre fecha de publicación y fechas de aplicación parcial es relevante para interpretar cuándo un sistema está sujeto a cada obligación.

### 3.2 Artículo 14 párrafo 1 — contenido exigido al sistema

**Respuesta: Sí, verificado si se lee el artículo.** El artículo 14 párrafo 1 del Reglamento (UE) 2024/1689 prescribe, en términos generales, que los sistemas de IA de alto riesgo estén diseñados de manera que las personas naturales puedan supervisarlos de forma eficaz durante su uso, comprender sus capacidades y limitaciones, vigilar su funcionamiento, interpretar sus resultados, decidir no usarlos o anular o revertir sus resultados, e intervenir o interrumpir el sistema mediante un botón de pausa o procedimiento similar.

**Lo que el documento afirma correctamente:**
- Esa exigencia existe y no es inventada por el proyecto.
- Es una condición necesaria para ciertas clases de sistemas, no una condición suficiente para el amor operativo.
- Cumplir con un botón de parada exigido por la ley no equivale a actuar bajo amor operativo.

**Lo que el documento no debe afirmar sin comprobación:**
- Que cualquier implementación del proyecto queda automáticamente dentro del ámbito del artículo 14. Eso depende de la clasificación del sistema en alto riesgo según el Anexo III y del contexto de uso.

**Verificación técnica recomendada antes de cualquier afirmación pública:**
- Extraer el texto del artículo 14 párrafo 1 de la fuente oficial o de la versión en inglés mantenida por artificialintelligenceact.eu, y comparar línea por línea con el resumen del documento.
- Si el resumen del documento introduce frases que no están en el texto normativo, marcarlas como interpretación del proyecto, no como cita textual.

**Estado del proyecto:** la sección 8.5.1 del documento cita el artículo y remite a la URL oficial. Esa referencia es verificable. El siguiente paso es confirmar que el resumen contenido en el documento coincide con el texto extraído.

### 3.3 Artículo 11 y Anexo IV — documentación técnica

**Respuesta: Sí, verificado si se lee el artículo y el anexo.** El artículo 11 exige documentación técnica para los sistemas de alto riesgo, y el Anexo IV define el contenido mínimo de esa documentación. El documento del proyecto resume esa exigencia y remite a la fuente.

**Lo que el documento afirma correctamente:**
- La existencia de la obligación de documentación técnica no es una invención del proyecto.
- El Anexo IV contiene un conjunto mínimo de elementos que deben estar presentes en la documentación técnica.
- Esta exigencia es coherente con el registro mínimo exigible del proyecto, pero es más lejos: el proyecto no puede asumir que una buena intención suple a un dossier auditable.

**Verificación técnica recomendada:**
- Leer el artículo 11 y el Anexo IV en la fuente oficial y verificar que los elementos enumerados en el documento coinciden con los del anexo.
- Si el documento del proyecto omite algún elemento obligatorio del Anexo IV al presentarlo como referente, debe añadir la omisión o reformular la frase para no sugerir que su propia lista es el anexo.

### 3.4 Anexo I — alcance del concepto de IA

**Respuesta: Sí, verificado si se lee el Anexo I.** El Anexo I del Reglamento (UE) 2024/1689 define las técnicas y enfoques de inteligencia artificial que entran dentro del concepto de sistema de IA que el Reglamento regula, incluyendo técnicas basadas en aprendizaje automático, enfoques basados en lógica o conocimiento, y enfoques estadísticos.

**Lo que el documento afirma correctamente:**
- El amor operativo no es una categoría que escapa al marco por ser “más ético”.
- Si una implementación es un sistema de IA dentro del sentido del Reglamento, los instrumentos del marco legal le aplican.

**Verificación técnica recomendada:**
- Leer el Anexo I y confirmar que la lista del documento del proyecto no agrega ni quita técnicas de forma que induzca a error.
- Evitar afirmaciones de que el proyecto está “fuera” del AI Act por su naturaleza ética; la pregunta correcta es si una implementación concreta entra dentro del alcance normativo.

### 3.5 Referencias URL

**Respuesta: Sí, verificación pendiente de extracción local.** Las referencias de la sección 8 apuntan a:
- artificialintelligenceact.eu/article/14/
- artificialintelligenceact.eu/article/11/
- EUR-Lex con el identificador CELEX 32024R1689

Estas referencias son del tipo que puede verificarse con extracción de página o consulta directa al registro oficial de la UE. El documento del proyecto afirma que estas referencias fueron consultadas el 29 de septiembre de 2026. Esa fecha debe coincidir con un artefacto de extracción real, no con la mera existencia de la URL.

**Verificación técnica recomendada:**
- Extraer el contenido de las URLs mencionadas y guardar el texto fuente.
- Verificar que el texto extraído contiene la frase o el párrafo que el documento cita.
- Guardar el artefacto de extracción con fecha, fuente y hash para que la revisión sea reproducible.

**Estado del proyecto:** el documento tiene la referencia correcta; lo que falta es la cadena de extracción local que lo pruebe. Sin esa cadena, la afirmación de que el artículo dice lo que dice el documento es una afirmación de confianza, no una afirmación verificada.

### 3.6 Lo que la sección 8 no resuelve

**Respuesta: Sí, verificado.** El documento declara explícitamente que la sección 8 no resuelve, por sí sola:
- Quién tiene poder real.
- Cómo se evitan los incentivos comerciales que empujan hacia la métrica nominal.
- Cómo se previene la captura de los procesos de auditoría o de supervisión.
- Cómo se corrige la asimetría de información entre quien audita, quien despliega y quien es afectado.

**Esta parte de la sección es honesta y debe mantenerse.** No es un fallo del proyecto; es la declaración de límites correcta. Reemplazarla por una confianza excesiva sería un error de edición.

## 4. Hallazgos

### Hallazgo 1 — Referencia legal coherente

La sección 8 cita un instrumento legal real y pertinente y no lo inventa. Esa parte es correcta y debe conservarse.

### Hallazgo 2 — Resumen del artículo debe coincidir con el texto

El documento resume el artículo 14 párrafo 1 y los instrumentos relacionados. Esa suma debe comprobarse contra el texto oficial. Si el resumen introduce matices que el texto no contiene, debe revisarse. Si coincide, el documento puede afirmar con más fuerza que su cita es verificable.

### Hallazgo 3 — Falta cadena de extracción

El documento afirma haber consultado las URLs el 29 de septiembre de 2026. Ese movimiento es coherente con la política de citas del proyecto, pero para que sea verificable debe existir el artefacto de extracción correspondiente. Sin él, la sección es una declaración de intención de verificación, no una verificación completa.

### Hallazgo 4 — Límites declarados correctamente

La sección declara correctamente lo que no resuelve. Eso es parte de la gobernanza, no un hueco que haya que rellenar con confianza.

## 5. Recomendaciones

1. **Completar la extracción local del artículo 14 y los instrumentos relacionados** y guardar el resultado con fecha y hash. Esto convierte la cita del documento de una referencia verificable en una cita verificada.
2. **Comparar el resumen del documento con el texto extraído** y ajustar el lenguaje del documento para que no afirme más de lo que el texto normativo soporta.
3. **Añadir al registro de decisiones editoriales la referencia a esta revisión**, con la fecha y las fuentes usadas, para que cualquier revisor posterior pueda repetir la comprobación.
4. **Mantener la declaración de límites de la sección 8**, porque es una parte honesta y necesaria del documento; no es un defecto que haya que borrar.

## 6. Veredicto

La sección 8 de `paper/gobernanza.md` tiene una base verificable real y no inventa el marco regulatorio que invoca. Su afirmación central — que el proyecto se apoya en exigencias regulatorias existentes y no las crea — es defendible, pero solo completamente verificable cuando el proyecto adjunta la extracción local del texto normativo que respalda sus citas. Hasta que eso exista, la sección es una referencia correcta con verificación pendiente, no una referencia incorrecta.

*Fecha de revisión:* 2026-09-30  
*Revisor:* Dra. Ingrid Solheim  
*Estado:* verificación de referencias en curso; base legal coherente; falta extracción local para cerrar la cadena de citas.
