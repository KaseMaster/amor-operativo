---
name: Bug report
description: Inconsistencia, referencia no verificada, métrica mal declarada o campo vacío en documentación obligatoria.
title: "[Bug] "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: "Usa este issue para reportar un error o inconsistencia concreta. Por favor, incluye la ubicación exacta."
  - type: input
    id: ubicacion
    attributes:
      label: Ubicación
      description: "Fichero y línea o sección afectada."
      placeholder: "paper/paper.md §3.2, o README, o metricas.md, etc."
    validations:
      required: true
  - type: textarea
    id: observacion
    attributes:
      label: Qué está mal
      description: "Descripción del problema: contradicción, referencia no verificada, campo vacío, métrica mal declarada, etc."
    validations:
      required: true
  - type: textarea
    id: evidencia
    attributes:
      label: Evidencia
      description: "Qué has revisado y por qué consideras que es un bug. Si es una referencia, indica si fue verificada o no."
    validations:
      required: true
  - type: dropdown
    id: severidad
    attributes:
      label: Severidad
      options:
        - Menor (claridad / tono)
        - Medio (inconsistencia o referencia dudosa)
        - Alto (campo obligatorio vacío o contradicción que bloquea lectura)
    validations:
      required: true
  - type: checkboxes
    id: verificado
    attributes:
      label: ¿Verificado?
      options:
        - "Sí: he revisado el fichero y el fragmento afectado."
        - "No: es un reporte inicial pendiente de revisión."
