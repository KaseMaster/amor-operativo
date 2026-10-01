# Informe al operador — Fase de publicación del repositorio (AMO-25)

**Fecha:** 2026-09-30  
**Agente:** Dr. Mateo Rivas (Community Liaison & Release Publisher)  
**Issue:** AMO-25 — F12 · Publicación del repositorio (SOLO con aprobación humana)  
**Status:** blocked — esperando aprobación y decisión de vía de publicación

---

## 1. Progreso real

### Lo que está hecho

El staging local del repositorio `amor-operativo` YA tiene todo el árbol completo listo para publicar, verificado en vivo:

- **paper/paper.md**: 8890 palabras, SHA256 `b454265fc86759323d38fa366dd1726095c2f48b9487cdb34b41497a086626ee` — CANÓN COMPARTIDO SIN DIFERENCIAS (verificado con diff -q contra `/home/hydra/ops-state/amor_operativo/paper/paper.md`)
- **paper/paper_en.md**: 5156 palabras, SHA256 `a6134e52b90dbfae1ebfcd25a3d250085817ee5ff63de380a5d794ed03c5033b`
- **paper/resumen_ejecutivo.md**: 200 palabras exactamente
- **paper/especificacion.md**: 10 principios como documento autónomo (5390 palabras)
- **paper/metricas.md**: tabla por principio con escala, umbral y procedimiento (12943 palabras)
- **paper/implementacion.md**: arquitectura de referencia, escalera de complejidad, computación biohíbrida, transición, test (6228 palabras)
- **paper/referencias.md**: >=30 referencias con DOI/arXiv/URL verificables (3585 palabras)
- **paper/glosario.md**: términos clave (3517 palabras)
- **paper/registro_decisiones.md**: decisiones editoriales + críticas no resueltas (3475 palabras)
- **paper/SPEC-AUTORITATIVA.md**: especificación autoritativa del contrato editorial (3342 palabras)
- **README.md**: 4 secciones obligatorias correctamente (Cómo empezar, Cómo contribuir, Estado del proyecto, Cómo citar) con autor humano Jose GG, usuario KaseMaster, repo https://github.com/KaseMaster/amor-operativo
- **LICENSE**: CC BY-SA 4.0 con texto legal completo, sin placeholders
- **CITATION.cff**: authors Jose GG + Amor Operativo Research Agents, repository-code https://github.com/KaseMaster/amor-operativo, version 1.0.0, license CC-BY-SA-4.0
- **.github/workflows/publish.yml**: GitHub Pages desde docs/ en main (pandoc → HTML)
- **.github/workflows/ci.yml**: lint (markdownlint) + spec validation (YAML) + auditor tests
- **.github/ISSUE_TEMPLATE/**: feedback.md, bug_report.md, feature_request.md
- **.github/PULL_REQUEST_TEMPLATE.md**: checklist completo
- **docs/index.html**: renderizado HTML del paper (8607 bytes, generado)
- **GOVERNANCE.md**: operador humano Jose GG, roles actuales, límites
- **CONTRIBUTING.md**: canales, criterios de evidencia, principios aplicados
- **CODE_OF_CONDUCT.md**: 10 principios como compromisos de conducta
- **CHANGELOG.md** y **VERSION** (1.0.0) coherentes
- **MANIFEST.md**: SHA256 de cada fichero del árbol
- **PUBLISH-CHECKLIST.md**: lista de verificación de publicación completa
- **paper/manuscript/**: manuscript-es.md, manuscript-en.md, conteo-palabras.md, INDEX.md
- **paper/corpus/bibliography.json**: bibliografía del paper
- **spec/**: spec-v1.yaml, audit-protocol.md, metrics.md, auditor/ (auditor.py + LICENSE Apache-2.0)
- **eval/**: protocol.md, results/, scenarios/
- **reviews/**: redteam-objections.md, claimtraceability.md, citation-audit.json, repro-audit.md, gaming-vectors.md

### Plan de publicación escrito

- `/home/hydra/ops-state/amor_operativo/paper/reports/PUBLISH-PLAN.md` — Plan completo con fases, checklist y preguntas para el operador.

### Comentario publicado en el issue

- Comment ID `a914fe47-970e-4796-a55d-ecc59da1ba1d` — plan presentado al operador con estado actual, plan de acciones y preguntas abiertas.

---

## 2. Deciciones tomadas

- El staging local retiene el canon compartido (paper.md 8890 palabras) y no se modifica hasta aprobación humana.
- Se presenta el plan al operador antes de cualquier publicación (cumpliendo la regla de "comentar el plan exacto y esperar OK").
- Se documenta el bloqueo actual: el remoto `origin` no está configurado en el staging local.

---

## 3. Críticas no resueltas

- **Vía de publicación no determinada:** el staging local no tiene remoto configurado. El repo `KaseMaster/amor-operativo` en GitHub existe pero con una versión del paper del commit `b39988ed` (11291 palabras) que NO es el canon actual. No sé si debo:
  - Configurar `origin` con `git@github.com:KaseMaster/amor-operativo.git` (SSH con clave `id_ed25519_kasemaster` falla: Permission denied)
  - Usar `gh` CLI (actualmente no autenticado)
  - Usar la conexión gestionada de Paperclip "GitHub for the company" (`ef3bf9f7-24d7-4f30-87b7-f15c9f2c1f14`, verificada el 2026-09-25 con `get_me` → KaseMaster, id 24654235, healthStatus ok)

- **Estado del repo remoto no verificado:** no puedo hacer fetch del remoto para verificar qué versión del paper tiene actualmente porque el remoto no está configurado.

---

## 4. Preguntas abiertas para el operador

1. **¿Cuál es la vía de publicación disponible en este entorno?** El remoto `origin` no está configurado. Necesito que el operador decida: SSH (clave `id_ed25519_kasemaster`), `gh` CLI, o conexión gestionada de Paperclip.

2. **¿Actualizar el repo existente (`KaseMaster/amor-operativo`) o actualizar el existente?** El repo existe en GitHub con una versión del paper desactualizada. Si se actualiza, habría que hacer push del staging actualizado. Si se crea uno nuevo, habría que borrar o renombrar el existente primero (o dejarlo como versión anterior).

3. **¿Hay PDF del paper disponible?** El `build.py` existe en el staging pero no sé si genera un PDF válido. Si no hay PDF, la release v1.0.0 se publica solo con Markdown.

4. **¿Los borradores de anuncio (`paper/reports/announcement.md`) y plan de difusión (`paper/reports/diffusion-plan.md`) están listos?** Ambos son borradores que aún no se han publicado. El announcement.md y diffusion-plan.md están VACÍOS en el filesystem (no existen). Necesito escribirlos antes de publicar.

---

## 5. Próximos pasos

1. Operador revisa el staging local y da OK explícito en AMO-19 (puerta F11).
2. Operador decide la vía de publicación (SSH, gh, o Paperclip).
3. Si SSH: configurar `origin` y verificar clave (actualmente falla).
4. Si Paperclip: verificar que la conexión `ef3bf9f7-24d7-4f30-87b7-f15c9f2c1f14` está operativa en este run.
5. Ejecutar el plan de acciones según la fase aprobada.

---

## 6. Estado del environment de Paperclip

- La API de Paperclip está operativa (puedo hacer comments, PATCH de issues).
- Las rutas de conexión/tools no están disponibles: `/api/connections/*` devuelve "API route not found", `/api/companies/.../tools/connections` devuelve "Board access required".
- SSH con `id_ed25519_kasemaster` falla: `git@github.com: Permission denied (publickey)`.
- `gh` CLI instalado pero no autenticado.
- El staging local no tiene `origin` configurado (git dice: "fatal: 'origin' does not appear to be a git repository").

---

**Resumen:** El staging está completo y listo. Faltan: (a) aprobación humana (puerta F11), (b) decisión sobre la vía de publicación, (c) escribir announcement.md y diffusion-plan.md si no existen, (d) verificar si hay PDF disponible.
