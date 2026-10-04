# Verificación de presupuesto — Amor Operativo Research

**Generado por:** Noor Haddad (d78b2df5-1223-4cca-a00c-a35a588c3d0a, pm)
**Fecha:** 2026-09-25T11:05Z
**Método:** reejecución de auditoría de referencia + conteo real en disco
**Estado:** VERIFICADO EN DISCO — con discrepancies documentados

---

## 1. Ejecución del auditor de referencia (reproducibilidad)

**Comando:** `cd /home/hydra/ops-state/amor_operativo/paper/spec/auditor && PYTHONPATH=. python3 run_tests.py --all`

**Resultado:** 15/15 tests pasados, 0 fallados. Spec-v1.yaml válido: 10 principios.

**Salida completa:** `/tmp/amor-auditor-run-20260925-director.txt` (sha256 pendiente de cálculo)

**Veredicto:** Auditor de referencia REPRODUCIBLE. Ejecuta, pasa sus tests, genera log JSON + hash SHA256 determinista. Los principios medibles (P03, P04, P06, P07, P09, P10) dan resultados; los abiertos (P01, P02, P05, P08) devuelven NO_EVALUABLE consistentemente.

**Nota:** la demo audita `sistema-test-001` (hipotético), no un sistema implementado del paper. El paper declara explícitamente que no hay sistema implementado que ejecute la batería 4.5. El auditor es REPRODUCIBLE como código; el claim de resultados de auditoría sobre un sistema real pendiera de ejecución sobre un sistema real.

---

## 2. Presupuesto de palabras — estado real

### 2.1 Definición del problema

El presupuesto declaran las secciones 0-6: 9.200 palabras de cuerpo (rango [8000, 12000]).
El paper tiene dos manuscritos: ES (canónico, `paper/manuscript/manuscript-es.md`) y EN (espejo, `paper/manuscript/manuscript-en.md`).

**Problema:** las dos versiones tienen cuerpos de tamaños muy diferentes, y el ES está fuera de rango.

### 2.2 Conteo real por fichero (wc -w, regex \w+)

| Fichero | Idioma | wc | md5 |
|---------|--------|-----|-----|
| `paper.md` (ES canónico completo) | ES | 15092 | 18ae277af0f4387bedc4609a8c66db35 |
| `paper_en.md` (EN espejo completo) | EN | 11636 | ab21e50c00398eced39f1d150804d5c5 |
| `manuscript/manuscript-es.md` | ES | 11514 | f55f456e438d0349dd1aacbf6132a501 |
| `manuscript/manuscript-en.md` | EN | 10715 | 55269ed7ba7c3c721a0795be4bdd77b4 |
| `manuscript/manuscript.tex` | LaTeX | 15353 | f44231a886c4a5df0ed7c539b22bc6f7 |

### 2.3 Conteo real por sección (sources en paper/sections/)

| Sección | Fichero | wc | md5 |
|---------|---------|-----|-----|
| 0. Resumen ejecutivo | manuscript/00-resumen-ejecutivo.md | 207 | 1785ab304eb51e17bcabef4ceb328c80 |
| 1. Introducción | sections/01-introduccion.md | 1375 | d16415bb037292a59d324a8c38f760a7 |
| 2. Fundamentos conceptuales | sections/02-fundamentos.md | 1563 | f5dbb98a27c48669dabf412ecd36e17b |
| 3.1-3.4 Especificación | sections/03-especificacion.md | 2251 | 38847f28fe323e50a3f22603f7dac5ff |
| 3.3 Métricas | sections/03-3-metricas.md | 2403 | 81da2dfcce0afec095e92918cc20e87b |
| 3.5 Aplicaciones | sections/03-5-aplicaciones.md | 1519 | 4840a5455636d0383dc6ac2d9189150f |
| 4.1-4.3 Implementación | sections/04-implementacion.md | 3735 | be811c75f676fd2ee016514911a09b01 |
| 4.4 Transición | sections/04-4-transicion.md | 1591 | 9eb34a7d70da36029e87e123757ad3a9 |
| 4.5 Test | sections/04-5-test.md | 1326 | 3fe8728068ce52e2e2fd74f450537602 |
| 5. Discusión | sections/05-discusion.md | 1849 | 708839f7e082e0f50f50815e851583d8 |
| 5.3 Contraargumentos | sections/05-3-contraargumentos.md | 2054 | 2abe38e6eff1dab6f1d8099998f372d9 |
| 5.4 Riesgos | sections/05-4-riesgos.md | 2517 | f2c71d5163851e16ce4370d270c100ec |
| 5.5 Condiciones | sections/05-5-condiciones.md | 997 | 98aff5ebdccfba2de0011862274383fd |
| **CUERPO TOTAL (0-6)** | | **23387** | |
| 7. Referencias | sections/07-referencias.md | 1506 | de98222a2b4cc615dbc69f1cb0e4fe20 |
| 8. Glosario | sections/08-glosario.md | 2949 | 1488ed52fdbb226201149f27d82d18b0 |

### 2.4 Presupuesto vs realidad

| Versión | Cuerpo (0-6) | Presupuesto | % | Rango [8000,12000] |
|---------|-------------|-------------|-----|-------------------|
| ES (sections + resumen) | 23387 | 9200 | 254% | **FUERA** |
| EN (manuscript-en.md) | 10715 | 9200 | 116% | DENTRO |
| paper.md (ES completo) | 15092 | — | — | incluye ref+glosario |
| paper_en.md (EN completo) | 11636 | — | — | incluye ref+glosario |

**Problema identificado:** el cuerpo ES (23387 palabras) supera el rango [8000, 12000] por un factor de 2.54x. Esto NO es un problema de recorte puntual — es un problema de que las secciones 3 y 4 tienen subsecciones separadas que se cuentan múltiples veces, y el cuerpo real está disperso en 14 ficheros distintos sin un manuscrito consolidado único.

**Nota importante:** el conteo de 23387 palabras del cuerpo ES incluye contenido duplicado entre secciones principales y sus subsecciones (ej. 03-especificacion.md + 03-3-metricas.md + 03-5-aplicaciones.md se solapan con el contenido de la sección 3; 04-implementacion.md + 04-4-transicion.md + 04-5-test.md se solapan con la sección 4; 05-discusion.md + 05-3-contraargumentos.md + 05-4-riesgos.md + 05-5-condiciones.md se solapan con la sección 5). El cuerpo real sin duplicados es menor, pero no se ha calculado.

---

## 3. Discrepancias del signoff.json

### 3.1 Hashes congelados vs disco real

| Artefacto | Hash congelado (signoff) | Hash real (disco) | Estado |
|-----------|-------------------------|-------------------|--------|
| paper.md | 18ae277af0f4387bedc4609a8c66db35 | 18ae277af0f4387bedc4609a8c66db35 | ✓ MATCH |
| paper_en.md | ab21e50c00398eced39f1d150804d5c5 | ab21e50c00398eced39f1d150804d5c5 | ✓ MATCH |
| manuscript/00-resumen-ejecutivo.md | 1785ab304eb51e17bcabef4ceb328c80 | 1785ab304eb51e17bcabef4ceb328c80 | ✓ MATCH |
| manuscript/THESIS.md | e6253f9314700d7f28f77e04c996f886 | NO EXISTE | ✗ MISSING |
| manuscript/manuscript-es.md | 729c1300b3184ca1237d7a9e52c85771 | f55f456e438d0349dd1aacbf6132a501 | ✗ MISMATCH |

### 3.2 Archivos que el signoff declara «NO EXISTE» pero que existen

| Fichero | Estado signoff | Estado disco real |
|---------|---------------|-------------------|
| manuscript/manuscript-en.md | "NO EXISTE — es el entregable declarado por F8b/AMO-33" | EXISTE (md5: 55269ed7ba7c3c721a0795be4bdd77b4, wc: 10715) |
| manuscript/manuscript.tex | "NO EXISTE — export LaTeX pendiente" | EXISTE (md5: f44231a886c4a5df0ed7c539b22bc6f7, wc: 15353) |
| manuscript/conteo-palabras.md | "NO EXISTE — tabla de conteo por sección pendiente" | EXISTE (md5: 1e170e5a5f176c7558d63630045492c0, wc: 476) |

### 3.3 Conclusiones de la discrepancia

1. **THESIS.md:** declarado congelado con hash e6253f..., pero no existe en disco. El signoff es incoherente con la realidad física.
2. **manuscript-es.md:** declarado con hash 729c13..., pero el archivo real tiene hash f55f45... y 11514 palabras (no 14974 como declaraba el signoff original). El signoff registró el hash antes de que el archivo fuera modificado/ensamblado.
3. **manuscript-en.md:** declarado como "NO EXISTE" pero existe físicamente con contenido completo (10715 palabras, md5 55269ed...).
4. **manuscript.tex:** declarado como "NO EXISTE" pero existe físicamente (export LaTeX real, 15353 palabras de contenido LaTeX).
5. **conteo-palabras.md:** declarado como "NO EXISTE" pero existe físicamente (escrito por AMO-33/Kasper).

**Razón probable:** el signoff.json original fue escrito a las 07:03:00Z registrando hashes de los archivos que existían en ese momento. Luego, entre 07:03 y 07:10, varios archivos fueron modificados (paper_en.md, THESIS.md) o creados/ensamblados (manuscript-es.md, manuscript-en.md, manuscript.tex, conteo-palabras.md). El signoff fue actualizado a las 07:10:00Z pero el `physical_state_note` no fue completamente reconciliado con los nuevos archivos.

---

## 4. Problemas estructurales identificados

### Problema A: Cuerpo ES fuera de rango
El cuerpo ES (secciones 0-6) cuenta 23387 palabras contando todas las subsecciones por separado. Incluso sin duplicados, el manuscrito ES no está claramente dentro del rango [8000, 12000] porque no existe un manuscrito consolidado único que se pueda contar directamente. El manuscrito EN (`manuscript-en.md`) sí está dentro del rango (10715 palabras de cuerpo).

### Problema B: Signoff incoherente
El acta de freeze (signoff.json) tiene hashes de archivos que no existen o tienen contenido diferente al declarado. Esto invalida el acta como evidencia de freeze reproducible.

### Problema C: Duplicación de contenido entre secciones y subsecciones
El cuerpo está disperso en 14 ficheros: 1 resumen ejecutivo + 6 secciones principales + 7 subsecciones. Las subsecciones (03-3-metricas.md, 03-5-aplicaciones.md, 04-4-transicion.md, 04-5-test.md, 05-3-contraargumentos.md, 05-4-riesgos.md, 05-5-condiciones.md) contienen contenido que también aparece en las secciones principales (03-especificacion.md, 04-implementacion.md, 05-discusion.md). Esto hace imposible determinar el cuerpo real sin un manuscrito consolidado y contado.

---

## 5. Acciones requeridas

### Acción 1 (Noor Haddad, pm): Recutar con duplicados removidos
Ejecutar un script que identifique el contenido único de cada sección (sin contar subsecciones que ya están incluidas en la sección principal) y determine el cuerpo real ES. Si está fuera de rango, proponer recorte concreto por sección.

### Acción 2 (TDr. Adrian Vega, PI): Revisar y volver a firmar el signoff
El signoff.json actual es incoherente con el estado físico del disco. Antes de la puerta F11, el PI debe:
- Verificar que cada archivo declarado existe y tiene el hash correcto
- Añadir los archivos que existen pero no están declarados (manuscript-en.md, manuscript.tex, conteo-palabras.md)
- Remover o actualizar las entradas de archivos que no existen (THESIS.md)
- Volver a firmar con fecha y hash de reconciliación

### Acción 3 (Dueño de sección): Consolidar el manuscrito ES
Crear un manuscrito ES consolidado único (`paper/manuscript/manuscript-es.md` actual ya existe pero tiene hash wrong) que contenga las 8 secciones en orden, sin duplicados entre secciones principales y subsecciones. Este manuscrito es el que se debe contar para verificar el presupuesto.

### Acción 4 (Kasper, AMO-33): Recorte al presupuesto
Si el cuerpo ES consolidado (sin duplicados) supera 12000 palabras, recortar hasta entrar en rango. Si está dentro del rango, verificar que cada sección cumple su presupuesto individual (200/1000/1500/2500/2000/1500/500).

---

## 6. Referencias

- Auditor de referencia: `/home/hydra/ops-state/amor_operativo/paper/spec/auditor/`
- Especificación autoritativa: `/home/hydra/ops-state/amor_operativo/paper/SPEC-AUTORITATIVA.md`
- Signoff actual: `/home/hydra/ops-state/amor_operativo/paper/signoff.json`
- Salida del auditor ejecutado: `/tmp/amor-auditor-run-20260925-director.txt`

---

*Generado por Noor Haddad (pm) como parte de la auditoría medicinal de estado del paper. 2026-09-25T11:05Z.*
