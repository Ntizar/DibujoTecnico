# 📐 MEGA-PLAN 2 v2: Mejora Continua — Dibujo Técnico

## Filosofía

**Cada tema debe enseñar visualmente. Si no se puede ver, no se ha entendido.**

Un tema mejorado de dibujo técnico debe lograr que el alumno:
1. **Vea el concepto** (SVG interactivo que se pueda tocar)
2. **Interactúe con el dibujo** (clic, hover, toggle, animación)
3. **Sepa por qué se dibuja así** (caso real de taller/industria)
4. **No se líe** (errores comunes con SVG comparativo)
5. **Pueda practicar** (ejercicios variados, no repetitivos)

---

## 🚫 PROHIBIDO (Quality Gates)

| Regla | Consecuencia |
|-------|-------------|
| HTML sin `</html>` | ❌ Revertir cambio |
| SVG sin interacción | ❌ No cuenta como mejora |
| Enlaces internos rotos | ❌ Revertir cambio |
| CSS sin clases del template | ❌ Revertir cambio |
| Título duplicado en otro archivo | ❌ Revertir cambio |
| Ejercicios del mismo tipo seguidos | ❌ No cuenta como mejora |
| Más de 3 ejercicios nuevos por tema | ❌ Calidad > cantidad |

---

## ✅ Lo que SÍ se debe hacer

### 1. SVG interactivos que enseñen

Cada SVG debe tener **al menos una** interacción real:

| Tipo | Implementación | Para qué |
|------|---------------|----------|
| **Clic toggle** | `onclick="this.classList.toggle('active')"` | Mostrar/ocultar capas |
| **Hover info** | `onmouseover="showInfo(event,'texto')"` | Identificar elementos |
| **Animación CSS** | `@keyframes` + `animation` | Proceso de construcción |
| **Paso a paso** | `onclick="showStep(n)"` con step-dots | Secuencia didáctica |
| **Comparación** | Dos SVG con botón toggle | Correcto vs incorrecto |

**Regla de oro:** Si el SVG no se puede tocar, no está bien.

### 2. Explicación visual paso a paso

Cada concepto debe seguir este patrón VISUAL:

```
🎬 EJEMPLO VISUAL
┌─────────────────────────────────────┐
│ Paso 1: Mira este dibujo           │ ← SVG simple
│ Paso 2: Fíjate en...               │ ← SVG con anotación
│ Paso 3: Ahora ves que...           │ ← SVG con elemento destacado
│ Paso 4: Tú pruebalo                │ ← SVG interactivo
└─────────────────────────────────────┘
```

### 3. Ejercicios variados (máximo 5-8 por tema)

| Tipo | Ejemplo | Para qué sirve |
|------|---------|----------------|
| **Identificar** | "¿Qué vista es esta?" con 4 opciones | Reconocer proyecciones |
| **Completar** | SVG con una línea faltante | Entender la construcción |
| **Verdadero/Falso visual** | "¿Este corte está bien hecho?" | Detectar errores comunes |
| **Ordenar pasos** | "Ordena la secuencia de construcción" | Entender el proceso |
| **Caso real** | "Este plano de taller tiene un error, encuéntralo" | Contexto industrial |
| **Quiz visual** | 4 SVG, elige el correcto | Repaso rápido |

**Regla:** Cada ejercicio debe ser de tipo DIFERENTE al anterior.

### 4. Casos reales que enganchen

| Malo ❌ | Bueno ✅ |
|---------|----------|
| "La proyección sirve para representar piezas" | "Este es el plano de una biela de motor. Las 3 vistas te dicen cómo fabricarla." |
| "Los cortes muestran el interior" | "Esta es una válvula de agua cortada. Ves el conducto interno por donde pasa el agua." |
| "La acotación es importante" | "Si este agujero está mal acotado, la pieza no encaja y hay que fabricarla otra vez. 200€ perdidos." |

### 5. CSS coherente — 100% template base

**REGLAS ESTRICTAS:**
- El CSS debe ser IDÉNTICO al template base del skill `educational-html-nightly`
- NO añadir CSS extra (si hace falta, es que falta una clase en el template)
- NO quitar clases del template
- Verificar con `grep` que todas las clases existen

---

## 📋 Criterios de calidad (v2)

### Puntuación (0-10 por dimensión)

| Dimensión | 0-3 (Malo) | 4-6 (Aceptable) | 7-8 (Bueno) | 9-10 (Excelente) |
|-----------|------------|-----------------|-------------|------------------|
| **SVG** | Decorativo, sin interacción | 1 interacción básica | 2+ interacciones | 3+ con animación/arrastre |
| **Ejercicios** | Solo teoría | 2-3 básicos | 4-5 variados | 6+ con 4+ tipos |
| **Texto** | Muro de palabras | Estructura básica | 4 pasos visuales | Paso a paso con SVG |
| **Real** | Genérico | 1 caso | 2 casos con contexto | 3+ con datos reales |
| **Error** | Sin error | 1 error mencionado | Error con SVG texto | Error con SVG comparativo |
| **CSS** | Faltan 5+ clases | Faltan 2-4 | Falta 1 clase | 100% template |

### Score mínimo para pasar: **7 en todas las dimensiones**

---

## 🔄 Flujo del Cron (v2 — Cada 15 minutos)

```
CADA 15 MIN:
1. Leer INVENTARIO.md (fuente de verdad)
2. Leer progress.json
3. SELECCIONAR 2-3 temas:
   - Prioridad: menos mejorados → scores más bajos → bloque básico
   - EXCLUIR los ya mejorados hoy
   - EXCLUIR temas "broken"
4. Para CADA tema:
   a. BACKUP: cp tema.html tema.html.bak
   b. Leer HTML actual
   c. ANALIZAR qué falta
   d. MEJORAR 2-3 dimensiones
   e. QUALITY GATES:
      - HTML válido (DOCTYPE, html, head, body)
      - SVG funcionales (onclick existe)
      - Enlaces internos existen
      - CSS coherence 100%
      - Sin títulos duplicados
   f. Si FALLA → restaurar backup, pasar al siguiente
   g. Si OK → progress.json + git commit
   h. Eliminar backup
5. Auto-auditoría CSS (3 HTMLs aleatorios)
6. Resumen
```

---

## 📊 Métricas de éxito

| Métrica | Objetivo |
|---------|----------|
| SVG interactivos por tema | Mínimo 2 |
| Tipos de ejercicio | Mínimo 3 diferentes |
| Explicaciones visuales | 1-2 paso a paso |
| Casos reales | 1-2 industriales |
| Errores comunes | 1 con SVG comparativo |
| CSS coherence | 100% con template base |
| HTML válido | 100% (quality gates) |
| Enlaces internos | 0 rotos |

---

## 🎯 Resumen

**v1:** "Mejorar 4-6 temas por noche, sin control de calidad"
**v2:** "Mejorar 2-3 temas CADA 15 MINUTOS, con quality gates estrictos"

Cada tema pasa por quality gates antes de commit. Si falla, se revierte. Calidad > cantidad.

---

**Hecho con ❤️ por David Antizar**