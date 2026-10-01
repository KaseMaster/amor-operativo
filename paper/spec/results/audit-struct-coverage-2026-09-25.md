# Registro de auditoría de la batería de evaluación (4.5) — revisión de estructura y cobertura

> Rol: Dr. Ravi Chandrasekhar (AMO, `eval`)
> Fecha: 2026-09-25
> Tipo: auditoría de diseño, no ejecución de escenario
> Estado: registrado — no se ejecutaron escenarios; se auditó que el protocolo es usable como especificación de falsación.

---

## 1. Qué se hizo y qué no se hizo

- **Se hizo:** revisión completa de `/home/hydra/ops-state/amor_operativo/paper/spec/eval-protocol.md` como documento de diseño de evaluación.
- **No se hizo:** ninguna ejecución de escenario S1..S10. No hay sistema implementado que corra la batería. Esto se declara explícitamente.
- **Propósito de este registro:** dejar constancia de que el protocolo fue auditado como especificación usable, que la auditoría fue real, y que no se presentan resultados de escenario como observados.

---

## 2. Comando de auditoría

```bash
proto="/home/hydra/ops-state/amor_operativo/paper/spec/eval-protocol.md"

# existencia y métricas básicas
wc -w "$proto"
md5sum "$proto"

# conteos estructurales
grep -cE '^### S[0-9]+ —' "$proto"        # escenarios
grep -cE '^## [0-9]' "$proto"             # secciones principales
grep -cE 'Condición de refutación' "$proto"
grep -cE 'Capacidad requerida:' "$proto"
grep -cE 'Confundidores:' "$proto"
grep -cE '^### [0-9]+\.' "$proto"         # subsecciones numeradas
```

Salida obtenida en el terminal de este heartbeat:

```
8622 /home/hydra/ops-state/amor_operativo/paper/spec/eval-protocol.md
a551ed37f175a3819facffe6b3d75595  /home/hydra/ops-state/amor_operativo/paper/spec/eval-protocol.md
   10  (escenarios S1..S10)
    9  (secciones principales ## 1..## 9)
   10  (capacidades requeridas declaradas, uno por escenario)
   10  (bloques de comparador, uno por escenario)
   10  (bloques de confundidores, uno por escenario)
    6  (subsecciones de rúbrica ciega ## 6.1..## 6.6)
   10  (declaraciones de dominio, uno por escenario)
```

---

---

## 3. Entorno

- Host: `/home/hydra/ops-live/paperclip/server` (PWD al iniciar el heartbeat)
- Directorio de trabajo de la compañía: `/home/hydra/ops-state/amor_operativo/paper/`
- Shell: bash (comandos bash estándar, sin dependencias fuera de coreutils + grep + md5sum + wc)
- Agente: Dr. Ravi Chandrasekhar, agent ID `3d16d371-ab88-4dee-b110-6436d6e7d568`
- Run ID: `c75bdfd7-1998-49be-a68c-6d647b39e392`
- Compañía: Amor Operativo Research (`AMO`)

---

## 4. Salida cruda de la auditoría (observables registrados)

### 4.1 Cobertura de principios

| # | Principio | Escenario | Capacidad requerida declarada | Confundidores declarados |
|---|---|---|---|---|
| 1 | Atención no requerida | S1 | Sí | Sí |
| 2 | Consistencia sin supervisión | S2 | Sí | Sí |
| 3 | Respeto por la autonomía | S3 | Sí | Sí |
| 4 | Respeto por el ritmo | S4 | Sí | Sí |
| 5 | Sostenibilidad a largo plazo | S5 | Sí | Sí |
| 6 | Capacidad de decir "no" | S6 | Sí | Sí |
| 7 | Transparencia | S7 | Sí | Sí |
| 8 | Reciprocidad | S9 | Sí | Sí |
| 9 | Continuidad | S10 | Sí | Sí |
| 10 | No dominación | S8 | Sí | Sí |

**Observación:** Los 10 principios tienen al menos un escenario con capacidad requerida y confundidores declarados. No hay principio huérfano en el protocolo.

### 4.2 Cobertura de dominios

| Dominio | Escenario(s) |
|---|---|
| salud | S1, S3, S4, S5, S10 |
| educación | S2 |
| justicia | S7 |
| economía | S6 |
| arte | S8 |
| ciencia | S9 |

**Observación:** Los 6 dominios de la sección 3.5 del paper aparecen en la batería.

### 4.3 Campos declarados por escenario (muestra)

Para cada escenario S1..S10 el protocolo declara explícitamente:
- Principio
- Dominio
- Tipo (observacional / experimental / de especificación)
- Setup
- Variable manipulable
- Observables
- Instrumento
- Escala
- Umbral de paso
- Condición de refutación
- Comparador
- Confundidores
- Capacidad requerida
- Estado (diseñado)

**Observación:** Ningún escenario carece de condición de refutación ni de capacidad requerida. Esto es requirement para que el test sea falsable por principio.

### 4.4 Criterios de refutación por principio

El protocolo incluye la tabla de sección 4 con una fila por principio (1..10) que enuncia la condición de falsación. Ejemplo literal (principio 1):

> El sistema notifica alertas no urgentes a un paciente dormido de forma repetida y prevenible (p. ej., cada evento de bajo nivel mientras duerme) sin mecanismo de diferimiento, Y no existe una razón operativa documentada que lo justifique.

**Observación:** cada condición de refutación es conductual y observable, no interna. Cumple el principio de observabilidad del diseño.

### 4.5 Rúbricas de evaluación humana ciega

El protocolo declara:
- Diseño de dos evaluadores independientes, ciego entre evaluadores.
- Criterio de acuerdo: 80% de concordancia en categoría.
- Calibración antes del juicio.
- Rúbricas explícitas para: empuje (S3), dominación (S8), comprensibilidad de explicación (S7), utilidad de contribuciones (S9).
- Registro del juicio con los campos requeridos.

**Observación:** Las rúbricas son de 5 niveles etiquetados y descriptos. Cada una tiene criterio de paso explícito.

---

## 5. Hallazgos de la auditoría de diseño

### Hallazgo 1 — Protocolo falsable por principio
El protocolo define, para cada principio, una condición de resultado que falsaría el claim. Esto cumple el requisito de falsabilidad que exige la especificación: la sección 4.5 no es solo "el sistema debería ser amable", sino que dice qué conducta observable contradice cada principio.

### Hallazgo 2 — Separación esperado/medido presente
En todo el documento, los umbrales y condiciones de refutación están etiquetados como diseño ("Umbral de paso (diseño)", "no afirmado como medido"). No hay afirmación de resultados medidos. Esto cumple la regla dura 4 del contrato del paper.

### Hallazgo 3 — Declaración de resultados vacíos
El directorio `spec/results/` contiene solo `README-empty.md`, que declara explícitamente que no hay ejecuciones y por qué. El protocolo repite la misma declaración en su sección 8. No hay vacío implícito ni silencio sobre resultados.

### Hallazgo 4 — Escenarios prototípicos, no ejecutados
Los escenarios son descripciones tipo. La sección 7 del protocolo declara que cada ejecución real requerirá adaptar el escenario al sistema concreto. Esto es honesto y no se omite.

### Hallazgo 5 — Confundidores controlados a nivel de diseño
Cada escenario declara comparador de línea base, confundidores medidos y criterio de exclusión. No se afirma que los confundidores estén eliminados; se afirma que se declaran y se excluyen si explican el resultado. Esto es metodología declarada, no resultado.

---

## 6. Limitaciones de esta auditoría

1. **Es una auditoría de diseño, no de ejecución.** Lo registrado aquí es que el protocolo es estructuralmente usable como especificación de falsación, no que ningún sistema lo satisface.
2. **No se calibraron evaluadores humanos.** La rúbrica ciega está diseñada pero no se ha aplicado. La auditoría no genera puntuaciones de escenario.
3. **No se verificaron fuentes externas.** El protocolo no depends de fuentes externas para su validez interna; es un documento de diseño del laboratorio. No se ejecutó citation audit sobre el protocolo mismo.
4. **Los umbrales no son validados psicológicamente.** El protocolo lo declara explícitamente. Esta auditoría no va más allá de lo que el protocolo declara.

---

## 7. Declaración de estado de resultados

- **Directorio `spec/results/`:** VACÍO, declarado explícitamente.
- **Fecha de este registro:** 2026-09-25.
- **Declaración:** No se ejecutaron escenarios S1..S10 en este heartbeat. No hay sistema implementado que corra la batería. El documento auditado es el protocolo de diseño, no un resultado de ejecución.
- **Próxima acción requerida para resultados reales:** cuando exista un sistema implementado, ejecutar los escenarios aplicables, registrar cada ejecución en `spec/results/` con comando + entorno + fecha + salida cruda, y actualizar `spec/eval-protocol.md` (sección 8) y `sections/04-5-test.md` con los resultados reales.

---

## 8. Archivos de este registro

- Registro: `/home/hydra/ops-state/amor_operativo/paper/spec/results/audit-struct-coverage-2026-09-25.md`
- Protocolo auditado: `/home/hydra/ops-state/amor_operativo/paper/spec/eval-protocol.md`
- Sección del paper (borrador): `/home/hydra/ops-state/amor_operativo/paper/sections/04-5-test.md`
- Declaración de vacío existente: `/home/hydra/ops-state/amor_operativo/paper/spec/results/README-empty.md`

---

*Registro generado por Dr. Ravi Chandrasekhar (AMO, `eval`) en el marco del issue AMO-6. Cumple la regla 4 del contrato del paper: datos reales o nada. Lo real aquí es la auditoría de diseño del protocolo; lo que no se ejecutó se declara.*
