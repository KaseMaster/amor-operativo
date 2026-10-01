# Publish checklist — Amor Operativo

Esta lista es el puente entre el staging local y la publicación real. No se publica nada en GitHub
hasta aprobación humana explícita del operador.

## 1. Pre-publicación — revisión interna

- [ ] README tiene las cuatro secciones obligatorias: cómo empezar, cómo contribuir, estado del
  proyecto, cómo citar.
- [ ] README incluye la tesis central y los 10 principios con sus nombres exactos.
- [ ] LICENSE es CC BY-SA 4.0 con texto legal completo, sin placeholders.
- [ ] LICENSE incluye Apache-2.0 para `spec/auditor/`.
- [ ] CITATION.cff replica autor humano Jose GG y repo KaseMaster/amor-operativo.
- [ ] CONTRIBUTING.md tiene canales, criterios de evidencia y enlaces a las tres plantillas de issue
  y al PR template.
- [ ] CODE_OF_CONDUCT.md está basado en los 10 principios.
- [ ] GOVERNANCE.md describe operador humano, roles actuales y límites.
- [ ] CHANGELOG.md y VERSION están presentes y coherentes con v1.0.0.
- [ ] Plantillas de issue: feedback, bug_report, feature_request.
- [ ] Plantilla de PR con checklist.
- [ ] `paper/SPEC-AUTORITATIVA.md` es el contrato editorial real, no un artefacto de tarea.
- [ ] `spec/auditor/LICENSE` es Apache-2.0.

## 2. CI — validación

- [ ] ci.yml lints markdown y valida spec-v1.yaml y los tests del auditor.
- [ ] publish.yml genera HTML desde markdown y publica en GitHub Pages desde docs/ en push a main.
- [ ] Los ficheros del paper usados por los workflows están en su lugar y son los esperados.

## 3. Contenido del paper

- [ ] paper/paper.md es la versión canónica en español.
- [ ] paper/paper_en.md es el espejo en inglés.
- [ ] paper/resumen_ejecutivo.md: ~200 palabras.
- [ ] paper/especificacion.md: 10 principios como documento autónomo.
- [ ] paper/metricas.md: tabla por principio con escala, umbral y procedimiento.
- [ ] paper/implementacion.md: arquitectura de referencia, escalera de complejidad, computación
  biohibrida, transición, test.
- [ ] paper/referencias.md: ≥30 verificables (DOI/arXiv/URL leídos), cero inventadas.
- [ ] paper/glosario.md: términos clave.
- [ ] paper/registro_decisiones.md: decisiones editoriales + críticas no resueltas.

## 4. Aprobación humana (puerta F11)

- [ ] El operador humano Jose GG revisa el staging local y da OK explícito.
- [ ] Tras el OK, se ejecuta publicación con las herramientas de GitHub disponibles, sin push manual
  prematuro.

## 5. Publicación real (post-OK)

- [ ] Repositorio GitHub: KaseMaster/amor-operativo, público, con descripción, topics y README.
- [ ] GitHub Pages desde docs/ en main.
- [ ] Release v1.0.0: paper en Markdown + PDF si está disponible.
- [ ] Verificación post-publicación: ficheros accesibles, README correcto, CITATION.cff legible,
  workflows activos.

## 6. Post-publicación

- [ ] Informar al operador con estado real, no inflado.
- [ ] Dejar registro de lo publicado y de los próximos pendientes.

---

