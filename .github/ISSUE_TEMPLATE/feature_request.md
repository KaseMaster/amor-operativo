---
name: Feature request
description: Proponer un cambio en principios, métricas, aplicaciones, estructura del paper o del repo.
title: "[Feature] "
labels: ["enhancement"]
body:
  - type: dropdown
    id: ambito
    attributes:
      label: Ámbito
      options:
        - Principio o definición formal
        - Métrica / escala / umbral
        - Aplicación (salud, educación, justicia, economía, arte, ciencia)
        - Estructura del paper
        - Estructura del repo / plantillas
        - Otra
    validations:
      required: true
  - type: textarea
    id: proposicion
    attributes:
      label: Qué propones
      description: "Describe el cambio concreto que sugieres."
    validations:
      required: true
  - type: textarea
    id: motivo
    attributes:
      label: Motivo
      description: "Por qué es útil, qué problema soluciona o qué gap cubre."
    validations:
      required: true
  - type: textarea
    id: criterios
    attributes:
      label: Criterios de aceptación
      description: "Si fuera una métrica o principio nuevo, qué observable, escala, umbral y procedimiento tendría."
    validations:
      required: false
  - type: textarea
    id: contraargumentos
    attributes:
      label: Contraargumentos conocidos
      description: "Riesgos, límites o objeciones que reconoces de antemano."
    validations:
      required: false
