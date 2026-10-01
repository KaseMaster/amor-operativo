# Contributing to Amor Operativo

Gracias por estar aquí. Este repositorio no es solo un paper y un conjunto de ficheros: es un espacio de trabajo donde se especifica, revisa y difunde una propuesta sobre conducta en sistemas de IA. Por eso, contribuir no es solo enviar cambios; es hacerlo de forma que respete a quienes leen, revisan, traducen y deciden.

## Canales

- **Retroalimentación:** plantilla de [feedback](.github/ISSUE_TEMPLATE/feedback.md) para comentarios sobre secciones, claridad, tono o criterios de evidencia.
- **Errores e inconsistencias:** plantilla de [bug report](.github/ISSUE_TEMPLATE/bug_report.md) para contradicciones, referencias no verificadas, métricas mal declaradas o campos vacíos en documentación obligatoria.
- **Nuevas propuestas:** plantilla de [feature request](.github/ISSUE_TEMPLATE/feature_request.md) para cambios en principios, métricas, aplicaciones, estructura del paper o del repo.
- **Cambios en el código del repo o del paper:** Pull Request con la plantilla de [PR](.github/PULL_REQUEST_TEMPLATE.md).

## Criterios de evidencia

Toda contribución que añade o cambia una afirmación factual debe llevar la evidencia que la soporta.

- **Referencias:** cualquier referencia incluida debe ser verificable con DOI, arXiv o URL resuelta, y debe ser leída antes de añadirse. No añadas referencias que no has revisado.
- **Métricas:** si propones una métrica, debe incluir escala, umbral y procedimiento de medida explícito, no solo un nombre o una idea.
- **Change log:** los cambios que afectan al contenido del paper o a la especificación se reflejan en el registro de decisiones del proyecto y, cuando corresponde, en CHANGELOG.md y VERSION.
- **Prosa:** el paper canónico es `paper/paper.md` en español; el espejo inglés es `paper/paper_en.md`. Las contribuciones de texto se coordinan en español.

## Estilo y calidad

- Markdown limpio y legible, con tablas y listas donde ayuden, preferible a texto denso sin estructura.
- Las secciones del paper siguen el esquema definido en la especificación autorizada del proyecto.
- Si tu contribución introduce un cambio editorial sustancial, documenta la decisión en el registro de decisiones del proyecto y, si procede, en un issue antes del PR.
- No inflés el estado del proyecto ni uses lenguaje grandilocuente; el trabajo está en borrador de especificación, no en release auditada.

## Principios aplicados a las contribuciones

Las contribuciones se esperan bajo los mismos diez principios que describe el paper: atención no requerida, consistencia sin supervisión, respeto por la autonomía, respeto por el ritmo, sostenibilidad a largo plazo, capacidad de decir "no", transparencia, reciprocidad, continuidad y no dominación.

En la práctica, eso significa: contribuir con cuidado, respetando el ritmo de revisión; siendo transparentes sobre lo que aportas y lo que no; pudiendo decir que no; y sin imponer tu dirección sobre la del operador humano ni sobre la especificación ya aprobada.

## Proceso típico

1. Abre un issue o usa una de las plantillas antes de empezar trabajo sustancial cuando el cambio no sea menor.
2. Propón el cambio y espera retroalimentación.
3. Si se alinea, implementa el cambio en el fichero correspondiente.
4. Abre un Pull Request con la plantilla, marcando lo que cambia, por qué y cómo se verifica.
5. La aprobación humana corresponde al operador humano; el repo de staging local no publica en GitHub hasta que haya un OK explícito.

## Preguntas abiertas

Si hay algo que no está claro, pregunta en un issue; no asumas. Este proyecto tiene preguntas abiertas documentadas en su propio registro y en el paper.
