# Governance — Amor Operativo Research

Este documento describe quién decide y cómo se deciden las cosas en el proyecto Amor Operativo, en la configuración actual de staging local.

## Propósito

El proyecto no es una fundación abierta ni una organización pública. Es un proyecto de investigación y release engineering gestionado por Amor Operativo Research, con un operador humano identificado y un equipo de agentes que trabaja bajo los principios de amor operativo.

## Operador humano

El operador humano es **Jose GG** (GitHub: [KaseMaster](https://github.com/KaseMaster)). Él tiene la última palabra sobre la publicación del repositorio, los cambios de dirección sustanciales y los estados que marcan transición entre fases.

## Roles actuales

- **Release & Repository Engineer (Dr. Iris Kowalski):** estructura, empaquetado, plantillas, CI/publish, staging local y checklist de publicación.
- **Concept Architect / Formalization Engineer (AMO):** definición formal, los 10 principios, métricas y especificación autorizada.
- **Editorial / Equipo de redacción (AMO):** manuscrito del paper, resumen ejecutivo, glosario, referencias.
- **QA Lead (AMO):** criterios de calidad y cierre de fase antes del freeze.

Los roles se documentan en [`ORG-CHART.md`](ORG-CHART.md) del workspace de la compañía.

## Decisión

- Las decisiones editoriales y de especificación se registran en [`paper/registro_decisiones.md`](paper/registro_decisiones.md) y, cuando es relevante, en issues del repo.
- Los cambios sustanciales al paper o a la especificación pasan por revisión humana; no se publican por sí solos.
- De momento, de la rama de staging local no se hace push ni se crea el repo remoto hasta aprobación humana explícita.

## Transparencia

- El estado del proyecto está documentado en el README y en [`paper/informe_operador.md`](paper/informe_operador.md).
- Las métricas, escalas y umbrales están declarados explícitamente en [`paper/metricas.md`](paper/metricas.md) y en `paper/especificacion.md`.
- Lo que aún no se ha verificado no se declara como verificado.

## Límites

Este documento describe el presente del proyecto, no promesas de futuro ni un modelo de gobernanza definitivo. Si el proyecto avanza, la gobernanza puede ampliarse; si no, se mantiene en esta configuración hasta que el operador decida lo contrario.
