# 📐 MEGA-PLAN 2: Mejora Continua — Dibujo Técnico

## Filosofía

**No se trata de añadir más SVG. Se trata de que cada dibujo enseñe mejor.**

Un tema mejorado de dibujo técnico debe lograr que el alumno:
1. **Vea el concepto** (no solo lo lea, que lo vea dibujado)
2. **Interactúe con el dibujo** (clic, arrastrar, mostrar/ocultar)
3. **Sepa por qué se dibuja así** (caso real de taller/industria)
4. **No se líe** (errores comunes visuales, no abstractos)
5. **Pueda practicar** (ejercicios de identificación, no solo teoría)

---

## ❌ Lo que NO se debe hacer

- Añadir SVG decorativos que no explican nada
- Copiar la misma estructura de ejercicios en todos los temas
- Poner texto sin dibujo que lo acompañe
- Ejercicios de "dibuja tú" sin guía paso a paso
- Ignorar los errores visuales típicos (trazos mal, confusión de diedros)

## ✅ Lo que SÍ se debe hacer

### 1. SVG interactivos que enseñen

Cada SVG debe tener **al menos una** de estas interacciones:

| Tipo | Cómo se hace | Para qué sirve |
|------|-------------|----------------|
| **Clic para mostrar/ocultar** | `onclick="toggleLayer(this)"` | Mostrar partes ocultas, trazos auxiliares |
| **Hover con info** | `onmouseover="showInfo(event)"` | Identificar elementos del dibujo |
| **Animación simple** | CSS `@keyframes` + `animation` | Mostrar el proceso de construcción |
| **Arrastrar** | `mousedown/mousemove/mouseup` | Colocar vistas, alinear proyecciones |
| **Comparación** | Dos SVG lado a lado con botón toggle | Antes/después, correcto/incorrecto |

**Regla de oro:** Si el SVG no se puede tocar, no está bien.

### 2. Explicación visual paso a paso

Cada concepto debe seguir este patrón VISUAL:

```
🎬 EJEMPLO VISUAL
┌─────────────────────────────────────┐
│ Paso 1: Mira este dibujo           │ ← SVG simple
│ Paso 2: Fíjate en...               │ ← SVG con anotación
│ Paso 3: Ahora ves que...            │ ← SVG con elemento destacado
│ Paso 4: Tú pruebalo                 │ ← SVG interactivo
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

**Regla: Si añades un ejercicio, debe ser visualmente diferente al anterior.**

### 4. Casos reales que enganchen

| Malo ❌ | Bueno ✅ |
|---------|----------|
| "La proyección sirve para representar piezas" | "Este es el plano de una biela de motor. Las 3 vistas te dicen cómo fabricarla." |
| "Los cortes muestran el interior" | "Esta es una válvula de agua cortada. Ves el conducto interno por donde pasa el agua." |
| "La acotación es importante" | "Si este agujero está mal acotado, la pieza no encaja y hay que fabricarla otra vez. 200€ perdidos." |

### 5. CSS coherente entre todos los HTML

**Problema detectado:** Todos los HTML de DT usan el mismo CSS inline, pero puede haber deriva (temas viejos sin ciertas clases, temas nuevos con CSS extra).

**Solución:** Cada mejora debe:
1. Verificar que el CSS del tema coincide con el template base (el del MEGA-PLAN.md)
2. Si falta alguna clase (`.box-problema`, `.toggle-btn`, `.feedback`), añadirla
3. Si sobra CSS que no se usa, quitarlo
4. Mantener las mismas variables CSS (`--azul`, `--naraja`, etc.)

---

## 📋 Criterios de calidad por tema

### Puntuación (0-10 por dimensión)

| Dimensión | 0-3 (Malo) | 4-6 (Aceptable) | 7-10 (Excelente) |
|-----------|------------|-----------------|------------------|
| **SVG** | Decorativo, sin interacción | 1-2 interacciones básicas | 3+ interacciones, animación, arrastre |
| **Ejercicios** | Solo teoría, sin práctica | 3-4 ejercicios básicos | 5-8 variados (identificar, completar, V/F, quiz) |
| **Texto** | Muro de palabras sin dibujo | Texto con 1-2 SVG de apoyo | Explicación paso a paso VISUAL |
| **Real** | Genérico | 1 caso real | 2+ casos con contexto industrial |
| **Error** | Sin error común | 1 error mencionado | Error visual con SVG de comparación |
| **CSS** | Clases faltantes o extra | Coherente con template | Idéntico al template base |

### Score mínimo para pasar a "mejorado": **5 en todas las dimensiones**

---

## 🔄 Flujo del Cron Nocturno (22:00 - 00:00)

```
CADA NOCH:
1. Leer progress.json
2. Seleccionar 3-5 temas (prioridad + menos mejorados)
3. Para CADA tema:
   a. Leer HTML actual
   b. ANALIZAR qué falta (no asumir)
   c. MEJORAR 2-3 dimensiones concretas:
      - ¿Falta SVG interactivo? → Añadir 1 con clic/hover
      - ¿Faltan ejercicios? → Añadir 2-3 tipos diferentes
      - ¿Falta explicación visual? → Añadir 1 paso a paso
      - ¿Faltan casos reales? → Añadir 1-2 industriales
      - ¿Falta error común? → Añadir 1 con SVG comparativo
      - ¿CSS incoherente? → Arreglar para que coincida con template
   d. VERIFICAR que el HTML no está roto
   e. ACTUALIZAR progress.json
   f. GIT commit
4. Al final: auto-auditoría de CSS coherence
   - Leer 3-5 HTMLs aleatorios
   - Comparar sus CSS con el template base
   - Si hay deriva, anotar para la próxima nocha
5. Resumen de la sesión
```

### Criterios de selección de temas

1. **Prioridad 1:** Temas con `improvement_count = 0` (nunca mejorados)
2. **Prioridad 2:** Temas con scores más bajos
3. **Prioridad 3:** Temas de bloques básicos primero (B01 > B02 > B03 > ...)
4. **Nunca repetir** el mismo tema en la misma nocha

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

---

## 🎯 Resumen

**Antes:** "Tema creado = tema terminado"
**Ahora:** "Cada nocha, 3-5 temas mejoran en algo visual, pedagógico o de coherence"

La cantidad de temas mejorados por nocha importa menos que la calidad de cada mejora. Un SVG interactivo bien hecho vale más que 10 ejercicios repetitivos.

---

**Hecho con ❤️ por David Antizar**