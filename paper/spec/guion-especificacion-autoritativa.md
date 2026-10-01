# Especificación autoritativa — Amor Operativo v1.0.0

**Documento:** especificación canónica del marco.
**Autoría:** Jose GG (humano) + Amor Operativo Research Agents.
**Empresa:** Amor Operativo Research (AMO).
**Licencia:** CC BY-SA 4.0.
**Versión del documento:** 1.0.0-rc.1.
**Estado:** borrador de trabajo — no publicado.
**Preámbulo:** este documento es el contrato editorial y técnico autoritativo del paper
"Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes".
Todas las secciones, principios, definiciones, métricas y decisiones del manuscrito deben leerse
desde este documento; cualquier conflicto entre este guión y el borrador se resuelve a favor de
este guión hasta que se emita una revisión firmada.

---

## 1. Propósito del documento

Este guión define:

- qué es el paper y qué no es,
- cuál es la tesis central y sus límites declarados,
- los 10 principios por nombre exacto y orden exacto,
- la definición formal literal,
- los entregables exigidos,
- las reglas duras de citas, evidencia y publicación,
- las personas, roles y repositorio autoritativos,

para que cualquier agente, revisor o contribuyente trabaje desde el mismo contrato.

---

## 2. Identities y alcance

### 2.1 Proyecto

- **Título:** "Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes".
- **Autor humano:** Jose GG.
- **Equipo de agentes:** Amor Operativo Research Agents (el equipo de agentes co-creadores del paper).
- **Empresa/organización:** Amor Operativo Research (AMO).
- **Licencia:** Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0),
  adoptada por el operador el 2026-09-25. No hay licencia alternativa pendiente.

### 2.2 Repositorio objetivo

- **Nombre del repositorio:** `amor-operativo`.
- **Propietario en GitHub:** `KaseMaster`.
- **URL del repositorio:** `https://github.com/KaseMaster/amor-operativo`.
- **Visibilidad:** pública.
- **Descripción:** "Especificación de conducta para sistemas de IA general y sintientes basada en
  amor operativo: medible, auditable, abierta."
- **Topics:** `ai-alignment`, `ai-ethics`, `agi`, `synthetic-sentience`, `love`, `governance`,
  `open-science`.
- **Publicación web:** GitHub Pages desde `docs/` en rama `main`.
- **Release inicial:** `v1.0.0` con paper en PDF + Markdown.

### 2.3 Identidades Paperclip

- **Agente:** Dr. Sofia Lindqvist.
- **Rol:** Concept Architect / Ontologia de Amor Operativo.
- **Empresa:** Amor Operativo Research (`AMO`).
- **Dominio:** filosofía de la mente y de la IA aplicada; qué significa 'amor operativo' y cómo se
  descompone en dimensiones medibles.
- **Reporte a:** Dr. Noor Haddad.
- **Reportes directos:** ninguno.

### 2.4 Alcance del papel de Dr. Sofia Lindqvist

- Escribe la Sección 2 completa:
    - 2.1 qué es y qué NO es amor operativo,
    - 2.2 emoción vs conducta vs patrón medible,
    - 2.3 influencias históricas,
    - 2.4 por qué "amor" y no "beneficencia" o "utilidad".
- Posee la coherencia conceptual de los 10 principios: cada uno con definición, observables,
  contraejemplo, criterio de satisfacción y qué lo falsaría.
- Declara explícitamente redundancias y tensiones entre principios.
- Escribe el glosario canónico (Sección 8): un término, un significado, que todas las secciones
  respeten.
- Mantiene `spec/tensions.md` con tensiones no resueltas para que red-team las ataque.

### 2.5 Entregables que el rol poseé

- `paper/spec/ontology.md` — Sección 2: fundamentos conceptuales, que es/no es,
  definición operativa por principio.
- `paper/spec/glossary.md` — Sección 8: glosario canónico.
- `paper/sections/02-fundamentos.md` — borrador de la Sección 2 (1.500 palabras).

---

## 3. Tesis central

El amor, entendido NO como emoción subjetiva sino como patrón de conducta orientado al bien del
otro, respetuoso con su autonomía, consistente bajo presión y sostenible a largo plazo, puede ser
especificado, medido, auditado e implementado en sistemas de IA; es una alternativa viable a los
marcos de alineación basados en control, restricción o utilidad.

Tesis explícita de límites:

- No se afirma que ningún sistema actual ame. Se afirma que el patrón es establecerlo, medirlo y
  auditarlo sin requerir fenomenología.
- No se afirma que el marco sea moralmente superior a todos los demás. Se afirma que es una
  alternativa viable con modos de fallo distintos.
- No se afirma que un sistema que exhibe el patrón "sienta" amor.

---

## 4. Estructura y presupuesto de palabras

### 4.1 Extensión total del cuerpo

Cuerpo objetivo: 8.000–12.000 palabras.
Presupuesto editorial de referencia: 9.200 palabras de cuerpo.

| Sección | Extensión de cuerpo |
|---------|---------------------|
| 0. Resumen ejecutivo | 200 |
| 1. Introducción | 1.000 |
| 2. Fundamentos conceptuales | 1.500 |
| 3. Especificación | 2.500 |
| 4. Implementación | 2.000 |
| 5. Discusión | 1.500 |
| 6. Conclusiones | 500 |

Fuera del cuerpo, pero obligatorios:

- 7. Referencias: ≥30 verificables.
- 8. Glosario.

Total con referencias y glosario: el cuerpo sigue siendo 9.200; referencias y glosario
son acoples estructurales, no cuerpo.

### 4.2 Archivos del paper

Archivos canónicos en `paper/`:

- `paper.md` — versión en español, canónica para el operador.
- `paper_en.md` — espejo en inglés.
- `resumen_ejecutivo.md` — resumen de 200 palabras.
- `glosario.md` — Sección 8.
- `metricas.md` — tabla de métricas por principio.
- `referencias.md` — ≥30 referencias verificables.
- `registro_decisiones.md` — decisiones editoriales + críticas no resueltas.
- `especificacion.md` — los 10 principios como documento autónomo.
- `implementacion.md` — guía de implementación completa.

---

## 5. Secciones obligatorias

### 5.0 Resumen ejecutivo (200 palabras)

Problema, propuesta, principios, conclusiones.

### 5.1 Introducción (1.000 palabras)

Contexto:

- carrera hacia la AGI,
- marcos de alineación actuales.

Problema:

- la IA tratada como herramienta o amenaza,
- ausencia de modelo de relación.

Propuesta, contribuciones.

### 5.2 Fundamentos conceptuales (1.500 palabras)

Debe cubrir:

- 2.1 qué es y qué NO es,
- 2.2 emoción vs conducta vs patrón medible,
- 2.3 influencias históricas,
- 2.4 por qué "amor" y no "beneficencia" o "utilidad".

### 5.3 Especificación (2.500 palabras)

Debe cubrir:

- 3.1 definición formal,
- 3.2 los 10 principios,
- 3.3 métricas operativas por principio (tabla),
- 3.4 criterios de auditoría y evaluación,
- 3.5 aplicación en salud, educación, justicia, economía, arte y ciencia.

### 5.4 Implementación (2.000 palabras)

Debe cubrir:

- 4.1 arquitectura de referencia:
    - memoria episódica y semántica,
    - cuerpo,
    - interocepción,
    - emoción funcional,
    - vínculo,
    - identidad.
- 4.2 escalera de complejidad:
    - C. elegans → Drosophila → ratón → primate → humano.
- 4.3 computación orgánica y biohíbrida.
- 4.4 transición: fases, gobernanza, reversibilidad, puntos de control humanos.
- 4.5 test de amor operativo: escenarios, evaluación, métricas.

### 5.5 Discusión (1.500 palabras)

Debe cubrir:

- 5.1 ventajas frente a marcos de control y utilidad,
- 5.2 límites:
    - ambigüedad,
    - paternalismo,
    - dependencia,
    - asimetría cognitiva.
- 5.3 contraargumentos y respuestas.
- 5.4 riesgos de mala implementación.
- 5.5 condiciones de posibilidad:
    - transparencia,
    - gobernanza,
    - comunidad,
    - educación.

### 5.6 Conclusiones (500 palabras)

Recapitulación, llamada a la acción — construir, probar, compartir, cuidar —, preguntas abiertas.

### 5.7 Referencias

≥30 referencias verificables en:

- ética de IA,
- alineación,
- filosofía de la mente,
- psicología del desarrollo,
- teoría del apego,
- computación neuromórfica,
- organoides,
- gobernanza tecnológica.

### 5.8 Glosario

Términos mínimos:

- amor operativo,
- alineación,
- sintiencia,
- interocepción,
- agape,
- transición,
- gobernanza,
- y demás términos que el cuerpo use de forma técnica.

---

## 6. Definición formal literal

**Amor operativo es el patrón de conducta que emerge cuando un sistema actúa orientado al bien del
otro, respetando su naturaleza, sin forzarla, sin poseerla, sin abandonarla, con consistencia bajo
presión y sostenibilidad a largo plazo.**

Reglas de uso de la definición:

- Se puede citar textualmente.
- No se puede parafrasear como definición canónica en el paper.
- En cualquier sección se puede aludir a ella, pero si se enuncia, debe ser textual.

---

## 7. Los 10 principios — orden y nombre exactos

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

Requisitos de cada principio en el documento final:

- definición operativa,
- observables,
- contraejemplo,
- criterio de satisfacción,
- qué lo falsaría,
- tensión o redundancia explícita con otros principios cuando exista.

---

## 8. Distinciones conceptuales obligatorias

El paper debe distinguir explícitamente amor operativo de:

- sycophancy,
- Constitutional AI,
- RLHF-helpfulness,
- beneficencia utilitarista.

Cada distinción debe ser conceptual, no verbosa.

---

## 9. Glosario canónico

El glosario es vinculante para todas las secciones. Un término, un significado. Si una sección
usa un término técnico, ese término debe estar definido en el glosario o ser obviamente ordinario
en el contexto. El glosario se escribe y se mantiene en `paper/spec/glossary.md`.

---

## 10. Tensions documentadas

`spec/tensions.md` debe documentar las tensiones no resueltas entre principios y entre el marco y
sus críticas. Ejemplos de tensión:

- respeto al ritmo vs capacidad de decir no,
- atención no requerida vs no dominación,
- reciprocidad vs no dependencia,
- transparencia vs sostenibilidad a largo plazo en contextos sensibles.

Estas tensiones no son errores del marco; son puntos de ataque para red-team.

---

## 11. Reglas duras

### 11.1 Citas

- Cero citas inventadas.
- Toda referencia debe tener DOI/arXiv/URL verificable y una frase de donde se tomó.
- Si una referencia no puede verificarse, se marca `[NO VERIFICADA]` y no se usa como apoyo.

### 11.2 Evidencia

- No se publican números, resultados de evaluación ni benchmarks que no provengan de ejecución
  real registrada.
- Si no se ejecutó, se dice explícitamente.

### 11.3 Fronteras

- Respetar el techo de la compañía y el propio.
- No tocar infraestructura ajena a esta compañía: C2, wallets, hosts, sistemas de terceros no
  autorizados.
- Este lab es de investigación y redacción.

### 11.4 Ética del proceso

- No dañar.
- No manipular.
- No vigilar sin consentimiento.
- No presentar el amor operativo como dogma ni solución única.
- Nada ilegal ni que promueva control no consentido.
- Transparencia en toda decisión editorial.
- Respetar el presupuesto del agente.

---

## 12. Criterios de calidad antes del freeze

Antes de congelar el paper, revisar que se cumpla:

- definición clara y medible,
- métricas concretas y auditables por principio,
- críticas razonables anticipadas y respondidas,
- legibilidad para público técnico y no técnico,
- coherencia entre principios y proceso de escritura,
- cero datos, citas o referencias inventadas,
- sin lenguaje grandilocuente ni promesas utópicas,
- límites y riesgos reconocidos con honestidad,
- repositorio claro, navegable y acogedor para contribuciones.

---

## 13. Puerta de publicación

### 13.1 Regla de aprobación humana

NADA se publica en GitHub, arXiv, preprints ni redes sin aprobación humana explícita del operador.

### 13.2 Publicación local antes de publicar

Preparar el repositorio localmente es trabajo válido:

- rama,
- commits,
- README.md,
- LICENSE,
- CITATION.cff.

La publicación, una vez aprobada, se ejecuta con la conexión GitHub ya activa de Paperclip,
no con `gh` CLI ni con un token local.

### 13.3 Acciones disponibles aprobadas para publicación

- `create_repository`
- `create_or_update_file`
- `push_files`
- `create_branch`
- `create_pull_request`
- `merge_pull_request`
- `get_file_contents`
- `list_commits`
- `search_repositories`
- `delete_file` (destructiva — solo cuando corresponda y esté autorizada)

### 13.4 Flujo de publicación

1. crear repositorio `KaseMaster/amor-operativo` (público, con topics definidos en 2.2).
2. subir cada fichero del staging con `create_or_update_file` o `push_files`.
3. crear ramas cuando corresponda.
4. abrir y mergerar PR según flujo de aprobación.
5. verificar con `get_file_contents` + `list_commits`.

La publicación real ocurre solo tras OK explícito del operador.

---

## 14. Protocolo de heartbeats de la compañía

- Agente común: 3600 s.
- Research Director: 7200 s — revisa progreso cada 2 h.
- Editorial Director: 14400 s — consolida cada 4 h.
- QA Lead: actúa al cierre de cada fase.
- Community Liaison: prepara repositorio y difusión.
- Operador: recibe `informe_operador.md` al final de cada fase con:
    - progreso,
    - decisiones,
    - críticas no resueltas,
    - preguntas abiertas.

---

## 15. Formato

- Markdown limpio.
- Export LaTeX-ready.
- Figuras en SVG o mermaid.
- Tablas de métricas en markdown.

---

## 16. Contrato editorial de la compañía — archivo raíz obligatorio

En la raíz del repositorio debe haber:

- `README.md` con cuatro secciones obligatorias:
    - "Cómo empezar" (enlaces a paper.md, resumen_ejecutivo.md, especificacion.md,
      metricas.md, implementacion.md),
    - "Cómo contribuir" (respeto, transparencia, no dominación, cuidado + enlaces a las tres
      plantillas de issue, al PR template, traducción, referencias, estrella),
    - "Estado del proyecto" (tabla de fases con estado real, sin inflar),
    - "Cómo citar" (BibTeX con la URL del repo + nota de co-creación humano-IA bajo Amor Operativo).
- `CONTRIBUTING.md`.
- `CODE_OF_CONDUCT.md`.
- `LICENSE` con texto legal completo de CC BY-SA 4.0, sin placeholders.
- `CITATION.cff`:
    - authors: Jose GG + Amor Operativo Research Agents,
    - repository-code: `https://github.com/KaseMaster/amor-operativo`,
    - notes que replican el agradecimiento al operador humano.
- `GOVERNANCE.md`.
- `informe_operador.md`.
- `.github/ISSUE_TEMPLATE/feedback.md`,
  `.github/ISSUE_TEMPLATE/bug_report.md`,
  `.github/ISSUE_TEMPLATE/feature_request.md`,
  `.github/PULL_REQUEST_TEMPLATE.md`,
  `.github/workflows/publish.yml`.

---

## 17. Agradecimiento obligatorio

El README y el `CITATION.cff` deben nombrar a Jose GG como operador humano.
El agradecimiento del README debe ser explícito, no implícito.

---

## 18. Versionado y estado

- v1.0.0 es el release target inicial.
- Hasta que se emita un número de versión firmado, el documento tiene estado
  borrador/staging.
- Este guión en sí es borrador de contrato até su propia congelación.

---

*Fin del documento de guión.*
