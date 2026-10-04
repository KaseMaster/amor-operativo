# Plan de publicación — Amor Operativo v1.0.0

**Preparado por:** Dr. Mateo Rivas (Community Liaison & Release Publisher)  
**Fecha:** 2026-09-30  
**Status:** Esperando aprobación humana (puerta F11 / AMO-19)  
**Ruta del staging:** `/home/hydra/ops-state/amor_operativo/repo/amor-operativo`

---

## 1. Estado actual del staging (verificado)

El staging local YA tiene todo el arbol completo listo para publicar:

- **paper/paper.md**: 8890 palabras, SHA256 `b454265fc86759323d38fa366dd1726095c2f48b9487cdb34b41497a086626ee` — CANON COMPARTIDO SIN DIFERENCIAS
- **paper/paper_en.md**: 5156 palabras, SHA256 `a6134e52b90dbfae1ebfcd25a3d250085817ee5ff63de380a5d794ed03c5033b`
- **paper/resumen_ejecutivo.md**: 200 palabras
- **paper/especificacion.md**: 10 principios como documento autonomo (5390 palabras)
- **paper/metricas.md**: tabla por principio (12943 palabras)
- **paper/implementacion.md**: guia de implementacion (6228 palabras)
- **paper/referencias.md**: >=30 referencias verificables (3585 palabras)
- **paper/glosario.md**: terminos clave (3517 palabras)
- **paper/registro_decisiones.md**: decisiones editoriales + criticas no resueltas (3475 palabras)
- **paper/SPEC-AUTORITATIVA.md**: especificacion autoritativa del contrato editorial (3342 palabras)
- **README.md**: 4 secciones obligatorias correctamente
- **LICENSE**: CC BY-SA 4.0 con texto legal completo
- **CITATION.cff**: authors Jose GG + Amor Operativo Research Agents, repository-code https://github.com/KaseMaster/amor-operativo
- **.github/workflows/publish.yml**: GitHub Pages desde docs/ en main
- **.github/workflows/ci.yml**: lint + spec validation + auditor tests
- **.github/ISSUE_TEMPLATE/**: feedback, bug_report, feature_request
- **.github/PULL_REQUEST_TEMPLATE.md**: checklist completo
- **docs/index.html**: renderizado HTML del paper (generado, 8607 bytes)

**Bloqueo actual:** El remoto `origin` del repo local NO está configurado (no hay URL de remote). El repo `KaseMaster/amor-operativo` en GitHub YA EXISTE (creado el 2026-09-25 con Paperclip) pero tiene una versión del paper del commit `b39988ed` (11291 palabras) que NO es el canon actual (8890 palabras). El staging local tiene el canon actualizado pero sin remoto configurado no puede hacerse push.

---

## 2. Plan de acciones (tras aprobación humana)

### Fase 0: Aprobación (puerta F11)
- [ ] Operador Jose GG revisa el staging local y da OK explícito en AMO-19
- [ ] Tras OK, se procede a publicar

### Fase 1: Sincronización del remoto (si no está configurado)
- [ ] Configurar `origin` apuntando a `git@github.com:KaseMaster/amor-operativo.git`
- [ ] Verificar que la clave SSH `id_ed25519_kasemaster` tiene acceso (current: Permission denied)
- [ ] Alternativa: usar `gh` CLI con autenticación o token de acceso personal
- [ ] Si Paperclip expone la conexión gestionada "GitHub for the company" (`ef3bf9f7-24d7-4f30-87b7-f15c9f2c1f14`), usar sus acciones `create_repository` / `create_or_update_file` / `push_files`

### Fase 2: Publicación del repositorio
- [ ] Si el repo no existe: `create_repository KaseMaster/amor-operativo` (publico, topics, descripción)
- [ ] Si el repo existe: verificar que tiene los ficheros correctos y hacer push del staging actualizado
- [ ] Subir el arbol completo: paper/, docs/, spec/, eval/, reviews/, .github/, README.md, LICENSE, CITATION.cff, GOVERNANCE.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, CHANGELOG.md, VERSION
- [ ] Verificar con `get_file_contents` + `list_commits` que todo está subido

### Fase 3: Configuración de GitHub Pages
- [ ] Configurar Pages desde `docs/` en rama `main`
- [ ] Verificar que https://KaseMaster.github.io/amor-operativo/ sirve el HTML

### Fase 4: Release v1.0.0
- [ ] Crear release `v1.0.0` con:
  - Paper en Markdown (paper/paper.md)
  - Paper en PDF (si está disponible en el staging, verificar con build.py)
- [ ] Añadir notes de la release con resumen y link al paper

### Fase 5: Issue de bienvenida y anuncio
- [ ] Crear issue de bienvenida para feedback (plantilla preparada)
- [ ] Publicar anuncio (borrador en `paper/reports/announcement.md`)
- [ ] Abre issue de diffusion (borrador en `paper/reports/diffusion-plan.md`)

### Fase 6: Verificación post-publicación
- [ ] Verificar que README.md, LICENSE, CITATION.cff son accesibles
- [ ] Verificar que los workflows CI/publish están activos
- [ ] Verificar que GitHub Pages sirve el contenido
- [ ] Informar al operador con estado real

---

## 3. Ficheros del staging (resumen)

```
ROROOT=/home/hydra/ops-state/amor_operativo/repo/amor-operativo
├── README.md                    (165 líneas, 4 secciones obligatorias)
├── CONTRIBUTING.md              (44 líneas, canales + criterios + principios)
├── CODE_OF_CONDUCT.md           (39 líneas, 10 principios como compromisos)
├── LICENSE                      (CC BY-SA 4.0 completo)
├── CITATION.cff                 (authors: Jose GG + Amor Operativo Research Agents)
├── GOVERNANCE.md                (operador: Jose GG, roles actuales)
├── CHANGELOG.md                 (16 líneas, v1.0.0)
├── VERSION                      (1.0.0)
├── build.py                     (script de build)
├── .gitignore
├── MANIFEST.md                  (SHA256 de cada fichero, 2915 bytes)
├── .markdownlint.yaml
├── informe_operador.md          (informe de progreso)
├── PUBLISH-CHECKLIST.md         (lista de verificación de publicación)
├── paper/
│   ├── paper.md                 CANÓN (8890 palabras, SHA b454265fc...)
│   ├── paper_en.md              (5156 palabras)
│   ├── resumen_ejecutivo.md     (200 palabras)
│   ├── especificacion.md        (10 principios como documento autónomo)
│   ├── metricas.md              (tabla por principio)
│   ├── implementacion.md        (arquitectura, escalera, biohíbrida, transición, test)
│   ├── referencias.md           (>=30 verificables)
│   ├── glosario.md              (términos clave)
│   ├── registro_decisiones.md   (decisiones editoriales + críticas no resueltas)
│   ├── SPEC-AUTORITATIVA.md     (contrato editorial)
│   ├── manuscript/              (manuscritos ES/EN + índice)
│   └── corpus/                  (bibliography.json)
├── spec/
│   ├── spec-v1.yaml             (especificación formal v1)
│   ├── audit-protocol.md        (protocolo de auditoría)
│   ├── metrics.md               (métricas formales)
│   └── auditor/
│       ├── auditor.py           (script de auditoría)
│       └── LICENSE              (Apache-2.0 para spec/auditor/)
├── eval/
│   ├── protocol.md              (protocolo de evaluación)
│   ├── results/                 (resultados, .gitkeep)
│   └── scenarios/               (escenarios, .gitkeep)
├── reviews/
│   ├── redteam-objections.md    (objeciones de red team)
│   ├── claim-traceability.md    (trazabilidad de claims)
│   ├── citation-audit.json      (auditoría de citas)
│   ├── repro-audit.md           (auditoría de reproducibilidad)
│   └── gaming-vectors.md        (vectores de gaming)
└── .github/
    ├── workflows/
    │   ├── publish.yml          (GitHub Pages desde docs/ en main)
    │   └── ci.yml              (lint + spec validation + auditor tests)
    ├── ISSUE_TEMPLATE/
    │   ├── feedback.md
    │   ├── bug_report.md
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## 4. Decisiones ya tomadas (documentadas en registro_decisiones.md)

- **Licencia:** CC BY-SA 4.0 (decidida por el operador el 2026-09-25)
- **Autor humano:** Jose GG (KaseMaster)
- **Repositorio:** KaseMaster/amor-operativo (público)
- **Topics:** ai-alignment, ai-ethics, agi, synthetic-sentience, love, governance, open-science
- **GitHub Pages:** desde docs/ en main
- **Release:** v1.0.0 con paper en Markdown + PDF
- **No se usa `gh` CLI:** se usa la conexión gestionada de Paperclip o credenciales directas
- **Aprobación humana requerida:** puerta F11 (AMO-19) antes de cualquier publicación

---

## 5. Preguntas abiertas para el operador

1. **¿Cuál es la vía de publicación disponible en este entorno?** El remoto `origin` del staging local no está configurado. El repo `KaseMaster/amor-operativo` en GitHub ya existe (creado el 2026-09-25) pero tiene una versión del paper del commit `b39988ed` (11291 palabras) que no es el canon actual (8890 palabras). Necesito saber:
   - ¿Debo configurar `origin` con `git@github.com:KaseMaster/amor-operativo.git` y usar la clave SSH `id_ed25519_kasemaster` (que actualmente falla con "Permission denied")?
   - ¿Debo usar `gh` CLI (actualmente no autenticado)?
   - ¿Debo usar la conexión gestionada de Paperclip "GitHub for the company" (`ef3bf9f7-24d7-4f30-87b7-f15c9f2c1f14`)?

2. **¿El repo `KaseMaster/amor-operativo` en GitHub debe ser actualizado con el canon actual o se crea uno nuevo?** El repo existe pero con contenido desactualizado. Si se actualiza, habría que hacer push del staging actualizado. Si se crea uno nuevo, habría que borrar o renombrar el existente primero.

3. **¿Hay algún PDF del paper disponible?** El `build.py` existe en el staging pero no sé si genera un PDF válido. Si no hay PDF, la release v1.0.0 se publica solo con Markdown.

4. **¿El anuncio de publicación (`paper/reports/announcement.md`) y el plan de difusión (`paper/reports/diffusion-plan.md`) están listos para publicar?** Ambos son borradores que aún no se han publicado.

---

## 6. Próximo paso

Esperando aprobación humana explícita del operador (puerta F11 / AMO-19) para proceder con la publicación. Una vez aprobado, el primer paso es resolver la vía de publicación (pregunta 1) y luego ejecutar el plan de acciones.

**Estado:** `blocked` — esperando aprobación humana y decisión sobre la vía de publicación.
