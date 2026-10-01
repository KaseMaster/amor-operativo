---
name: Feedback
description: Comentario sobre el paper, la especificación o este repositorio (claridad, tono, criterios de evidencia).
title: "[Feedback] "
labels: ["feedback"]
body:
  - type: markdown
    attributes:
      value: "Usa este issue para retroalimentación sobre secciones, legibilidad, tono o criterios de evidencia."
  - type: dropdown
    id: seccion
    attributes:
      label: Sección
      description: "¿A qué parte del proyecto se refiere tu feedback?"
      options:
        - Resumen ejecutivo
        - Introducción
        - Fundamentos conceptuales
        - Especificación (definición formal / 10 principios)
        - Métricas
        - Implementación
        - Discusión
        - Conclusiones
        - Referencias
        - Glosario
        - Este repositorio / README / plantillas
        - Otra
    validations:
      required: true
  - type: dropdown
    id: tipo
    attributes:
      label: Tipo de feedback
      options:
        - Claridad / redacción
        - Tono / lenguaje
        - Criterio de evidencia / referencia
        - Métrica / escala / umbral
        - Estructura / organización
        - Otra
    validations:
      required: true
  - type: textarea
    id: descripcion
    attributes:
      label: Descripción
      description: "Qué observas y, si es posible, por qué te parece relevante."
    validations:
      required: true
  - type: textarea
    id: evidencia
    attributes:
      label: Evidencia
      description: "Ejemplo concreto, fragmento del texto, referencia verificada o argumento que soporte el feedback. Si no la tienes, dilo claro."
    validations:
      required: false
