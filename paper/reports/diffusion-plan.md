# Plan de difusion (BORRADOR, pendiente de aprobacion)

Objetivo: que el paper llegue a publico tecnico y no tecnico, con tono respetuoso,
transparente y sin grandilocuencia, recogiendo feedback en el issue de bienvenida.

## Canales y orden (cada paso tras el OK del operador)

1. GitHub: release v1.0.0 + issue de bienvenida (feedback, bug_report, feature_request
   con las plantillas existentes).
2. GitHub Pages (docs/) como landing: paper ES/EN, especificacion, metricas.
3. Reddit: r/MachineLearning, r/singularity, r/PhilosophyofScience (post honesto,
   sin promesas; responder criticas con los limites de la seccion 5).
4. Hacker News (Show HN): texto sobrio, enlace al repo.
5. X/Redes del autor (Jose GG): hilo en espanol + ingles.
6. Comunidades hispanohablantes de IA/etica (grupos y foros).
7. Contacto directo con laboratorios/grupos de alineacion interesados en spec abiertas.

## Mensajes clave

- El amor como patron de conducta medible y auditable, no como sentimiento.
- 10 principios con metricas, contraejemplos y falsabilidad.
- Licencia abierta (CC BY-SA 4.0), co-creacion humano-IA, criticas bienvenidas.

## Metricas de difusion (a registrar de verdad, no inventadas)

- Estrellas/forks/issues del repo (semanal, via API).
- Trafico de Pages (via API de trafico cuando este activa).
- Feedback recibido en issues (contador por plantilla).

## Reglas

- Nada se publica sin OK del operador (puerta ya registrada en AMO-25).
- Toda respuesta a criticas aplica transparencia, no dominacion y capacidad de decir "no".
- No inflar estado del proyecto; el README lleva la tabla real de fases.

## Ejecucion 2026-10-01 (run 5c7fb22d, Dr. Mateo Rivas)

- GitHub (canal 1) EJECUTADO: Pages, topics, release v1.0.0 con PDF ES (26 pag, 88560 bytes,
  pandoc 3.1.11 + weasyprint 70.0) + paper.md + paper_en.md, issue de bienvenida, descripcion
  del repo segun brief, sincronizacion del staging (commit 50fc3d24).
- Canales 2-7 siguen PENDIENTES de OK del operador por canal; el anuncio
  (`announcement.md`) queda marcado PUBLICABLE para el issue de bienvenida.
