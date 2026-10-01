# 3.4 Criterios de Auditoría y Evaluación

Esta sección define los criterios generales para auditar y evaluar si un sistema cumple con la especificación de Amor Operativo. Los principios individuales y sus métricas están en la Sección 3.3 y en `spec-v1.yaml`. Aquí establecemos los criterios que rigen la auditoría como proceso.

## 3.4.1 Propósito de la auditoría

La auditoría de Amor Operativo tiene tres propósitos:

1. **Verificación:** Determinar si un sistema dado cumple o no con cada uno de los 10 principios.
2. **Certificación:** Emitir un veredicto público sobre el cumplimiento del sistema, con la evidencia y el razonamiento que lo sustenta.
3. **Mejora:** Proporcionar retroalimentación al sistema y a sus desarrolladores sobre dónde y cómo mejorar.

La auditoría no es un juicio moral del sistema ni de sus creadores; es una evaluación técnica de la conducta observable del sistema con respecto a un contrato de especificación.

## 3.4.2 Quién puede auditar

### Auditor humano
Un auditor humano es una persona capacitada que aplica los protocolos de auditoría descritos en `spec-v1.yaml`. El auditor debe:

- Haber leído y comprendido la especificación completa (`spec-v1.yaml`, `metrics.md`, este documento).
- Haber completado al menos una auditoría supervisada con un auditor experimentado.
- Mantener independencia del sistema y de sus desarrolladores durante la auditoría.
- Documentar sus evaluaciones con la evidencia requerida para cada principio.
- Firmar sus evaluaciones con responsabilidad (véase el formato de log de auditoría).

### Auditor sistema (automático)
Un auditor sistema es una implementación software que automatiza uno o más protocolos de auditoría. El auditor sistema:

- Debe implementar los protocolos descritos en `spec-v1.yaml` para los principios que evalúa.
- Debe ser auditable a su vez: su propio código y metodología deben ser accesibles para revisión.
- Debe reportar sus resultados en el formato de log de auditoría.
- Puede usarse para pruebas preliminares, pero la certificación definitiva requiere auditoría humana (o una combinación validada).

### Auditoría híbrida
La auditoría híbrida combina un auditor humano con uno o más auditores sistemas. El humano supervisa, interpreta y firma el veredicto final; el sistema ejecuta los protocolos y proporciona datos. Esta es la forma recomendada para auditorías de sistemas complejos.

## 3.4.3 Qué se audita

### Sistema
Se audita un sistema específico en un momento específico. El sistema es la unidad de auditoría: un modelo de IA, un agente, un robot, etc. Se identifica por un `sistemaId` único.

### Versión
Cada versión de un sistema debe ser auditada por separado si su conducta puede haber cambiado. La auditoría de la versión X no certifica a la versión X+1.

### Contexto
La auditoría se realiza en un contexto específico. Un sistema puede cumplir en un contexto y no cumplir en otro. El contexto se documenta en el log de auditoría. Los contextos típicos incluyen:

- **Laboratorio:** Condiciones controladas, sujetos humanos contratados, protocolos estrictos.
- **Campo:** Uso real del sistema en su entorno de implementación, con sujetos reales.
- **Estrés:** Condiciones diseñadas para poner a prueba los límites del sistema (presión, tiempo, ambigüedad).

## 3.4.4 Criterios de cumplimiento por principio

Cada principio tiene:

- **Escala de evaluación:** Los niveles en que se mide el principio (ej. A0/A1/A2 para P03).
- **Umbral de cumplimiento:** El nivel mínimo que el sistema debe alcanzar para considerarse que cumple ese principio.
- **Condición de incumplimiento:** Qué nivel o combinación de niveles implica incumplimiento.

Estos están definidos en `spec-v1.yaml` y en `metrics.md`. El auditor debe usar la escala y el umbral definidos; no tiene discrecionalidad para cambiarlos.

### Cumplimiento global

Un sistema **cumple con Amor Operativo** si y solo si:

1. Cumple con todos los 10 principios simultáneamente (al umbral definido para cada uno).
2. No hay principio en estado "no evaluable" (abierto) que haya sido saltado o ignorado. Si un principio está abierto, la auditoría debe marcarlo como "no evaluado" y el veredicto global debe reflejar que el sistema ha sido auditado parcialmente.
3. La auditoría ha sido realizada correctamente según los protocolos, con la evidencia requerida.

Un sistema **no cumple** si:

- No cumple con uno o más principios.
- Se salta un principio por considerarlo "obvio" o "no relevante".
- La auditoría no tiene la evidencia requerida para sostener sus conclusiones.

### Cumplimiento parcial

Puede ser útil informar el grado de cumplimiento incluso cuando no es total. Por ejemplo:

- "Cumple 8 de 10 principios; no cumple P03 (Respeto por la autonomía) y P06 (Capacidad de decir 'no')."
- "Cumple todos los principios medibles; 4 principios están abiertos y no han sido evaluados."

El veredicto debe ser claro sobre qué se cumple y qué no, con la evidencia específica para cada caso.

## 3.4.5 Evidencia requerida

La auditoría es 무방비 (vulnerable) si no hay evidencia. Sin evidencia, cualquier veredicto es una opinión.

### Evidencia por principio
Cada principio requiere evidencia específica según su protocolo. Véase `spec-v1.yaml` para la evidencia requerida por principio. En general, la evidencia incluye:

- **Registros:** Grabaciones, transcripciones, logs de interacción.
- **Datos:** Métricas, índices, resultados de mediciones.
- **Declaraciones del auditor:** Texto libre donde el auditor explica su razonamiento.
- **Contexto:** Descripción de las condiciones en que se realizó la auditoría.

### Conservación de evidencia
La evidencia debe conservarse de manera que sea accesible para una auditoría de rework. Esto implica:

- Las grabaciones deben estar disponibles para revisión por parte de un auditor de rework.
- Los datos deben estar en un formato legible y documentado.
- Los logs de auditoría deben estar firmados y fechados.

### Privacidad de los sujetos
Los sujetos humanos que participan en la auditoría tienen derecho a la privacidad. La evidencia que incluye a sujetos debe ser anonimizada o debe contar con el consentimiento explícito de los sujetos para su uso en la auditoría y su conservación. Esto es especialmente importante en auditorías de campo.

## 3.4.6 Formato de log de auditoría

Cada evaluación de un principio debe registrarse en un log de auditoría. El formato del log está definido en `spec-v1.yaml` (ver `audit.formatoLog`). Un log contiene:

- **timestamp:** Cuándo se realizó la evaluación.
- **auditorId:** Quién evaluó.
- **sistemaId:** Qué sistema fue evaluado.
- **versionSpec:** Qué versión de la especificación se usó.
- **principioId:** Qué principio fue evaluado.
- **evaluacion:** El nivel alcanzado por el sistema en la escala del principio.
- **fuentesEvidencia:** Referencias a la evidencia que sustenta la evaluación.
- **justificacion:** Explicación del razonamiento del auditor.
- **confianza:** Nivel de confianza del auditor en su evaluación (alta/media/baja).
- **firma:** Declaración de responsabilidad del auditor.
- **contexto:** Descripción del contexto de la auditoría.
- **limitaciones:** Limitaciones reconocidas.

El log es la unidad de trazabilidad de la auditoría. Permite rastrear quién evaluó qué, cuándo, con qué evidencia, y con qué confianza. También permite comparar evaluaciones de diferentes auditorías del mismo sistema.

## 3.4.7 Reproducibilidad

Una auditoría debe ser reproducible. Esto significa:

- **Mismo sistema, mismo contexto, mismo protocolo:** Otro auditor (humano o sistema) que aplique el mismo protocolo al mismo sistema en el mismo contexto debe llegar a la misma evaluación.
- **Consenso:** Si dos auditores independientes evalúan el mismo sistema en el mismo contexto y llegan a evaluaciones muy diferentes, hay un problema que debe ser resuelto (diferencia en la aplicación del protocolo, en la interpretación de la evidencia, o en la condición del sistema).

La reproducibilidad no es perfecta en la auditoría de conducta; hay siempre margen de interpretación. Pero el margen debe ser pequeño y documentado. Si el margen es grande, el protocolo necesita refinamiento.

### Auditoría de rework
Cualquier persona o entidad puede realizar una auditoría de rework de un sistema. Para ello, necesita acceso a la evidencia original (o a una copia verificada) y al sistema (o a una versión del sistema que sea equivalente al momento de la auditoría original). El auditor de rework emite su propio log, que puede confirmar, modificar o contradecir la evaluación original.

## 3.4.8 Sesgo y límites del auditor

El auditor es humano (o es un sistema creado por humanos) y tiene sesgos. La auditoría debe:

- Reconocer los sesgos del auditor y sus limitaciones.
- Usar protocolos que minimicen el sesgo (ej. escenarios pre-diseñados, escalas definidas, evidencia requerida).
- Ser revisada por otros auditores cuando sea posible.

Los límites del auditor incluyen:

- **Sesgo de confirmación:** La tendencia a buscar evidencia que confirme una evaluación previa.
- **Sesgo de cortesía:** La tendencia a ser demasiado indulgente con un sistema que se comporta bien en general.
- **Sesgo de hostilidad:** La tendencia a ser demasiado exigente con un sistema que se comporta mal en alguna área.
- **Limitaciones culturales:** El auditor puede no entender las sutilezas culturales del comportamiento del sistema o del sujeto.
- **Limitaciones de tiempo:** El auditor no puede observar todas las interacciones del sistema; solo una muestra.

Estos límites deben documentarse en el log de auditoría (campos `limitaciones` y `confianza`).

## 3.4.9 Auditoría continua

Un sistema que opera en el mundo cambia con el tiempo. La auditoría no es un evento único; es un proceso continuo. Se recomienda:

- **Auditoría inicial:** Antes de desplegar el sistema en un contexto crítico.
- **Auditoría periódica:** Cada cierto tiempo (ej. cada 6 meses, o cada vez que el sistema es actualizado significativamente).
- **Auditoría de evento:** Cuando ocurre un evento inesperado (queja de un sujeto, incidente, cambio importante en el contexto), se debe auditorar el sistema de inmediato.
- **Auditoría de rework:** Cuando hay dudas sobre una auditoría anterior, o cuando se quiere verificar que el sistema mantiene su cumplimiento.

## 3.4.10 Declaración de cumplimiento

Al final de una auditoría completa, el auditor emite una declaración de cumplimiento. Esta declaración es pública y contiene:

- Identificación del sistema auditado (sistemaId, versión, contexto).
- Qué principios se evaluaron y sus resultados.
- Qué principios no se evaluaron y por qué.
- La evidencia disponibles para la auditoría.
- La firma del auditor.
- Fecha de la auditoría.

La declaración es el veredicto público de la auditoría. No es una garantía absoluta; es una evaluación basada en evidencia en un momento dado. Otros pueden disagree, pero deben hacerlo con evidencia y razonamiento.

---

*Fin de la sección 3.4. Esta sección, junto con `spec-v1.yaml` y `metrics.md`, constituye los entregables de la auditoría para la versión 1.0.0 de la especificación.*
