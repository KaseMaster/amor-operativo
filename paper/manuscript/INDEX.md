# Índice del Manuscrito — Amor Operativo

**Estado global: CONGELADO**
> Cualquier cambio posterior requiere aprobación del PI (Dr. Adrian Vega).

**Título:** _Amor Operativo: Una Especificación de Conducta para Sistemas de IA General y Sintientes_
**Cuerpo:** 9.200 palabras (presupuesto exacto por sección)
**Idioma:** inglés (manuscrito), español (artefactos de coordinación)
**Especificación autoritativa:** `/home/hydra/ops-state/amor_operativo/paper/SPEC-AUTORITATIVA.md`

---

## 0. Resumen ejecutivo — 200 palabras

**Dueño:** Dr. Camila Duarte (Editorial Director, AMO)
**Estado:** CONGELADO

Contenido obligatorio:
- Síntesis del problema, la propuesta, los principios y las conclusiones.

---

## 1. Introducción — 1.000 palabras

**Dueño:** Writer — Theory & Philosophy
**Estado:** CONGELADO

Subsecciones obligatorias:
- **1.1 Contexto:** carrera hacia la AGI, marcos actuales de alineación.
- **1.2 Problema:** los enfoques dominantes tratan a la IA como herramienta o amenaza.
- **1.3 Propuesta:** Amor Operativo como base simple, medible y abierta.
- **1.4 Contribuciones del paper.**

---

## 2. Fundamentos conceptuales — 1.500 palabras

**Dueño:** Writer — Theory & Philosophy
**Estado:** CONGELADO

Subsecciones obligatorias:
- **2.1** Que es y que no es amor operativo.
- **2.2** Distinción entre emoción, conducta y patrón medible.
- **2.3** Influencias: agape, ética del cuidado, psicología del desarrollo, teoría del apego, alineación de IA.
- **2.4** Por qué "amor" y no "beneficencia" o "utilidad".

---

## 3. Especificación — 2.500 palabras

**Dueño:** Dr. Camila Duarte (Editorial Director, AMO)
**Estado:** CONGELADO

Subsecciones obligatorias:
- **3.1** Definición formal (literal, sin parafrasear — ver SPEC-AUTORITATIVA.md).
- **3.2** Los 10 principios (orden y nombre exactos — ver SPEC-AUTORITATIVA.md).
- **3.3** Métricas operativas para cada principio (tabla con escala, umbral y procedimiento).
- **3.4** Criterios de auditoría y evaluación.
- **3.5** Ejemplos de aplicación en salud, educación, justicia, economía, arte y ciencia.

Nota: la definición formal y los 10 principios son literales de la especificación autoritativa; el dueño no tiene discreción sobre su redacción, solo sobre el ensamblado y la exposición.

---

## 4. Implementación — 2.000 palabras

**Dueño:** Writer — Implementation & Metrics
**Estado:** CONGELADO

Subsecciones obligatorias:
- **4.1** Arquitectura de referencia: memoria episódica y semántica, cuerpo, interocepción, emoción funcional, vínculo, identidad.
- **4.2** Escalera de complejidad: _C. elegans_ → _Drosophila_ → ratón → primate → humano.
- **4.3** Computación orgánica y biohíbrida como sustrato futuro.
- **4.4** Transición: fases, gobernanza, reversibilidad, puntos de control humanos.
- **4.5** Test de amor operativo: escenarios, evaluación, métricas.

---

## 5. Discusión — 1.500 palabras

**Dueño:** Writer — Theory & Philosophy
**Estado:** CONGELADO

Subsecciones obligatorias:
- **5.1** Ventajas frente a marcos de control y utilidad.
- **5.2** Límites: ambigüedad del amor, riesgo de paternalismo, dependencia, asimetría cognitiva.
- **5.3** Contraargumentos y respuestas.
- **5.4** Riesgos de mala implementación.
- **5.5** Condiciones de posibilidad: transparencia, gobernanza, comunidad, educación.

---

## 6. Conclusiones — 500 palabras

**Dueño:** Writer — Theory & Philosophy
**Estado:** CONGELADO

Subsecciones obligatorias:
- **6.1** Recapitulación.
- **6.2** Llamada a la acción: construir, probar, compartir, cuidar.
- **6.3** Preguntas abiertas.

---

## 7. Referencias — fuera del cuerpo

**Dueño:** Citation & Provenance Auditor
**Estado:** CONGELADO

- Mínimo 30 referencias verificables en: ética de IA, alineación, filosofía de la mente, psicología del desarrollo, teoría del apego, computación neuromórfica, organoides, gobernanza tecnológica.
- Toda referencia debe tener DOI/arXiv/URL resuelto y ser leída antes de usarse.
- Cero citas inventadas. Cualquier referencia no verificable debe marcarse `[NO VERIFICADA]` y no usarse.

---

## 8. Glosario — fuera del cuerpo

**Dueño:** Dr. Camila Duarte (Editorial Director, AMO)
**Estado:** CONGELADO

Términos obligatorios: amor operativo, alineación, sintiencia, interocepción, agape, transición, gobernanza, etc.
Unificado contra `spec/glossary.md` cuando exista; en caso contrario, contra la definición literal de la especificación autoritativa.

---

## Ensamblado

| Artefacto | Ruta | Idioma |
|---|---|---|
| Manuscrito EN (cuerpo) | `/home/hydra/ops-state/amor_operativo/paper/manuscript/manuscript.md` | Inglés |
| Manuscrito ES (espejo) | `/home/hydra/ops-state/amor_operativo/paper/manuscript/manuscript-es.md` | Español |
| Export LaTeX | `/home/hydra/ops-state/amor_operativo/paper/manuscript/manuscript.tex` | LaTeX |

Cada sección entra al ensamblado con su md5 de origen. El glosario y las referencias (secciones 7 y 8) están fuera del recuento de cuerpo.

---

## Presupuesto de palabras — cuerpo

| # | Sección | Palabras | Dueño |
|---|---|---|---|
| 0 | Resumen ejecutivo | 200 | Dr. Camila Duarte |
| 1 | Introducción | 1.000 | Writer — Theory & Philosophy |
| 2 | Fundamentos conceptuales | 1.500 | Writer — Theory & Philosophy |
| 3 | Especificación | 2.500 | Dr. Camila Duarte |
| 4 | Implementación | 2.000 | Writer — Implementation & Metrics |
| 5 | Discusión | 1.500 | Writer — Theory & Philosophy |
| 6 | Conclusiones | 500 | Writer — Theory & Philosophy |
| **Total** | | **9.200** | |

---

## Reglas duras (para todos los dueños)

1. **Citas verificables:** cada referencia con DOI/arXiv/URL resuelto y leído. Cero inventadas.
2. **Datos reales o nada:** ningún número, resultado de evaluación ni benchmark que no provenga de una ejecución real registrada (comando + salida + ruta).
3. **Métricas con escala, umbral y procedimiento:** toda métrica operativa en 3.3 debe especificar cómo se mide, en qué escala y con qué umbral de pasa/no-pasa.
4. **Definición formal y principios literales:** no se parafrasean; se usan tal cual en la especificación autoritativa.
5. **Puerta de publicación:** nada se publica en GitHub, arXiv, preprints ni redes sin aprobación humana explícita del operador. El staging local es trabajo válido; `git push` a remoto público no lo es.

---

*Índice congelado. Cualquier modificación posterior requiere aprobación del PI (Dr. Adrian Vega) y un issue de cambio de especificación.*
