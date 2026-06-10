# Dibujo Técnico Completo — Mega Plan

## Visión

Curso completo de dibujo técnico interactivo: desde normalización básica hasta planos de conjunto industrial. ~53 HTML interactivos con SVG interactivo, ejercicios con feedback, progresión pedagógica guiada.

**Autor:** David Antizar
**URL destino:** `https://ntizar.github.io/DibujoTecnico/`
**Repo destino:** `Ntizar/DibujoTecnico` (crear)
**Stack:** HTML + CSS inline + SVG interactivo + KaTeX (ESO+) + JS vanilla

## Filosofía pedagógica

1. **Ver primero, leer después** — cada concepto se muestra visualmente (SVG) antes de explicar
2. **Interactuar siempre** — click en proyecciones, arrastrar vistas, identificar líneas
3. **Progresión suave** — de lo simple a lo complejo, cada tema construye sobre el anterior
4. **Errores comunes** — cada tema incluye el error típico y por qué ocurre
5. **Casos reales** — planos reales, piezas industriales, cómo se usa en la práctica

## Estructura del curso (9 bloques)

| Bloque | Tema | Temas | Archivos | Skills fuente |
|--------|------|-------|----------|---------------|
| B01 | Normalización | Formatos, líneas, escalas, rotulación | 5 | td-normalizacion |
| B02 | Proyecciones | Ortogonal, diédrico, vistas, abatimiento | 8 | td-proyecciones |
| B03 | Perspectivas | Isométrica, caballera, dimétrica, círculos | 6 | td-perspectivas |
| B04 | Diedrico Básico | Punto, recta, plano, pertenencia | 10 | td-diedrico-punto-recta-plano |
| B05 | Cortes y Secciones | Corte total, parcial, semicorte, escalonado | 6 | td-cortes-secciones |
| B06 | Acotación | Elementos, métodos, reglas, símbolos | 5 | td-acotacion |
| B07 | Intersecciones y VM | Recta-plano, plano-plano, giros, cambio de plano | 6 | td-intersecciones-vm |
| B08 | Abatimientos | Concepto, figuras, aplicaciones | 4 | td-abatimientos-giros |
| B09 | Planos de Conjunto | Montaje, despiece, lista de piezas | 3 | td-planos-conjunto |
| | **TOTAL** | | **53** | |

## Template HTML base (dibujo técnico)

Cada HTML sigue esta estructura:

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — {subtitle}</title>
<style>
:root{--azul:#2563eb;--naranja:#f97316;--verde:#10b981;--rojo:#ef4444;--fondo:#fff;--texto:#1e293b;--gris:#94a3b8;--azul-claro:#eff6ff;--naranja-claro:#fff7ed;--verde-claro:#ecfdf5;--rojo-claro:#fef2f2;--pura-claro:#faf5ff;--pura:#a855f7}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Inter,system-ui,-apple-system,sans-serif;background:linear-gradient(135deg,#f8faff 0%,#fffaf5 100%);color:var(--texto);line-height:1.7}
.header{background:linear-gradient(135deg,var(--azul),#1d4ed8);color:#fff;padding:2rem 1.5rem;text-align:center}
.header h1{font-size:1.8rem;margin-bottom:.5rem}
.header p{opacity:.9;font-size:1rem}
.progress-bar{height:4px;background:rgba(255,255,255,.3);border-radius:2px;margin-top:1rem;overflow:hidden}
.progress-fill{height:100%;background:#fff;border-radius:2px;width:0%;transition:width .3s}
.container{max-width:900px;margin:0 auto;padding:1.5rem}
.chapter{margin-bottom:2.5rem}
.chapter-title{font-size:1.4rem;color:var(--azul);margin-bottom:1rem;padding-bottom:.5rem;border-bottom:2px solid var(--azul-claro)}
.box{padding:1rem 1.2rem;border-radius:10px;margin:1rem 0;border-left:4px solid;box-shadow:0 1px 3px rgba(0,0,0,.04)}
.box-teoria{background:var(--azul-claro);border-color:var(--azul)}
.box-ejemplo{background:var(--naranja-claro);border-color:var(--naranja)}
.box-error{background:var(--rojo-claro);border-color:var(--rojo)}
.box-idea{background:var(--pura-claro);border-color:var(--pura)}
.box-success{background:var(--verde-claro);border-color:var(--verde)}
.box strong{display:block;margin-bottom:.3rem}
.svg-container{background:#f8fafc;border-radius:12px;padding:1.5rem;margin:1.5rem 0;text-align:center;border:2px solid #e2e8f0}
.svg-container svg{max-width:100%;height:auto}
.svg-container svg text{font-family:Inter,system-ui,sans-serif}
.interactive{background:#f1f5f9;border-radius:12px;padding:1.5rem;margin:1.5rem 0}
.interactive h3{color:var(--azul);margin-bottom:1rem;font-size:1.1rem}
.interactive button{background:var(--azul);color:#fff;border:none;padding:.5rem 1.2rem;border-radius:6px;cursor:pointer;font-size:.95rem;margin:.3rem}
.interactive button:hover{background:#1d4ed8}
.result{margin-top:.8rem;padding:.8rem;border-radius:6px;font-weight:600;min-height:2rem}
.result.ok{background:var(--verde-claro);color:#065f46}
.result.fail{background:var(--rojo-claro);color:#991b1b}
.exercises{margin:1.5rem 0}
.exercise{background:#f1f5f9;border-radius:8px;padding:1rem;margin:.8rem 0}
.exercise p{font-weight:600;margin-bottom:.5rem}
.quiz-options{display:flex;gap:.5rem;flex-wrap:wrap;margin:1rem 0}
.quiz-btn{padding:.6rem 1.5rem;border-radius:8px;border:2px solid var(--azul);background:#fff;font-size:1.1rem;font-weight:600;cursor:pointer;transition:all .2s}
.quiz-btn:hover{background:var(--azul-claro)}
.quiz-btn.correct{background:var(--verde);color:#fff;border-color:var(--verde)}
.quiz-btn.wrong{background:var(--rojo);color:#fff;border-color:var(--rojo)}
.summary{background:var(--azul-claro);border-radius:12px;padding:1.5rem;margin:2rem 0}
.summary h3{color:var(--azul);margin-bottom:.8rem}
.summary ul{list-style:none;padding:0}
.summary li{padding:.3rem 0;padding-left:1.5rem;position:relative}
.summary li::before{content:"✓";color:var(--verde);font-weight:bold;position:absolute;left:0}
.nav{display:flex;justify-content:space-between;margin:2rem 0;padding:1rem 0;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0}
.nav a{color:var(--azul);text-decoration:none;font-weight:600;padding:.5rem 1rem;border-radius:6px}
.nav a:hover{background:var(--azul-claro)}
.nav .disabled{color:var(--gris);cursor:default;pointer-events:none}
.footer{text-align:center;padding:2rem 1rem;color:var(--gris);font-size:.85rem;border-top:1px solid #e2e8f0;margin-top:2rem}
</style>
</head>
<body>
<header class="header">
<h1>{title}</h1>
<p>{subtitle}</p>
<div class="progress-bar"><div class="progress-fill" id="progress"></div></div>
</header>
<main class="container">
<section class="chapter">
<h2 class="chapter-title">🎯 ¿Qué vamos a aprender?</h2>
<div class="box box-idea"><strong>💡 Idea clave</strong>{key_idea}</div>
<p>En esta sesión aprenderás a:</p>
<ul style="margin:.8rem 0 1rem 1.5rem">{learning_goals}</ul>
</section>
<section class="chapter">
<h2 class="chapter-title">1️⃣ {theory_title}</h2>
<div class="box box-teoria"><strong>📖 Teoría</strong>{theory_text}</div>
<div class="box box-ejemplo"><strong>🔍 Ejemplo 1</strong>{example_1}</div>
<div class="box box-ejemplo"><strong>🔍 Ejemplo 2</strong>{example_2}</div>
<div class="box box-ejemplo"><strong>🔍 Ejemplo 3</strong>{example_3}</div>
</section>
<section class="chapter">
<h2 class="chapter-title">2️⃣ {interactive_title}</h2>
<div class="svg-container">{svg_content}</div>
<div class="interactive">
<h3>{interactive_desc}</h3>
{interactive_content}
<div class="result" id="interactiveResult"></div>
</div>
</section>
<section class="chapter">
<h2 class="chapter-title">📝 Ejercicios</h2>
<div class="exercises">{exercises_html}</div>
</section>
<div class="summary">
<h3>📋 Resumen de lo aprendido</h3>
<ul>{summary_items}</ul>
</div>
<div class="nav">
<a href="{prev_link}">← Anterior</a>
<a href="{next_link}">Siguiente →</a>
</div>
</main>
<footer class="footer">Hecho con ❤️ por David Antizar</footer>
<script>
{js_code}
window.onscroll = function(){
  var h = document.documentElement;
  var p = (window.scrollY/(h.scrollHeight-h.clientHeight))*100;
  document.getElementById('progress').style.width = p+'%';
};
</script>
</body>
</html>
```

## SVG interactivo — patrón base

Cada tema de dibujo técnico necesita SVG específico. El SVG debe:
- Usar `stroke-width` adecuado (0.5 para auxiliares, 1.5 para contornos)
- Incluir líneas de tierra (LT) con `stroke-dasharray`
- Usar colores semánticos: azul (ejes), negro (contornos), rojo (cotas), verde (ayuda)
- Ser interactivo: elementos clicables con `onclick`
- Incluir tooltips con `title` SVG

## Nomenclatura de archivos

- `b01-01-formatos-papel.html` — Bloque 1, tema 1
- `b01-02-tipos-linea.html` — Bloque 1, tema 2
- `INDEX.html` — Página principal con todos los bloques

## Criterio de "tema hecho"

1. ✅ SVG interactivo que muestre el concepto clave
2. ✅ Al menos 3 ejemplos resueltos
3. ✅ Al menos 3 ejercicios interactivos con feedback (variedad de tipos)
4. ✅ Error común explicado
5. ✅ Caso de uso real
6. ✅ Resumen final
7. ✅ Navegación Anterior/Siguiente
8. ✅ Atribución "Hecho con ❤️ por David Antizar"
9. ✅ Responsive (móvil + escritorio)
10. ✅ Intuición visual antes que texto

## Progresión pedagógica

El orden de los 53 temas es CRÍTICO: cada tema debe construir sobre el anterior.

### Bloque 1: Normalización (5 temas)
1. Formatos de papel ISO 216
2. Tipos de línea ISO 128
3. Escalas ISO 5455
4. Rotulación UNE
5. Cuadro de rotulación y pie de plano

### Bloque 2: Proyecciones (8 temas)
6. Proyección ortogonal (concepto)
7. Sistema de 3 planos (PV, PH, PL)
8. Vistas principales (alzado, planta, perfil)
9. Correspondencia entre vistas
10. Abatimiento del PH
11. 1º diedro vs 3º diedro
12. Representación de piezas simple
13. Vista auxiliar y parcial

### Bloque 3: Perspectivas (6 temas)
14. Perspectiva isométrica (ejes)
15. Isométrica: cubo y prismas
16. Isométrica: círculos y elipses
17. Perspectiva caballera
18. Caballera: piezas con cilindros
19. Dimétrica y monométrica

### Bloque 4: Diedrico (10 temas)
20. Sistema diédrico: puntos y cuadrantes
21. Puntos notables
22. Recta: trazas y posiciones
23. Recta: verdadera magnitud
24. Plano: trazas y posiciones
25. Rectas notables del plano
26. Pertenencia: punto en recta, punto en plano
27. Paralelismo: recta-recta, recta-plano, plano-plano
28. Perpendicularidad: recta-plano
29. Ejercicio completo diedrico

### Bloque 5: Cortes y Secciones (6 temas)
30. Corte total
31. Corte parcial y semicorte
32. Corte escalonado
33. Sección y rotura
34. Hachuras y normas
35. Ejercicio completo cortes

### Bloque 6: Acotación (5 temas)
36. Elementos de la cota
37. Métodos de acotación (cadena, paralelo)
38. Símbolos (Φ, R, SR)
39. Reglas de acotación
40. Ejercicio completo acotación

### Bloque 7: Intersecciones y VM (6 temas)
41. Intersección recta-plano
42. Intersección plano-plano
43. Intersección recta-recta (puntos cruzados)
44. Verdadera magnitud por giro
45. Verdadera magnitud por cambio de plano
46. Distancia punto-recta y punto-plano

### Bloque 8: Abatimientos (4 temas)
47. Concepto de abatimiento
48. Abatimiento de punto en plano
49. Abatimiento de figuras planas
50. Aplicaciones del abatimiento

### Bloque 9: Planos de Conjunto (3 temas)
51. Plano de conjunto
52. Despiece y marcas
53. Vista explosiva y lista de piezas

## Sistema de crons

### Cron 1: `td-mega-plan` (una vez)
- Crea el repo `Ntizar/DibujoTecnico`
- Genera INDEX.html
- Genera progress.json
- Genera primer cron para tema 1

### Cron 2: `td-generador` (recurring, cada 5 minutos)
- Lee progress.json → busca siguiente pending
- Lee el skill TD correspondiente
- Genera el HTML del tema con SVG interactivo
- Crea el siguiente cron para el tema siguiente
- Git commit + push
- Actualiza progress.json

### Cron 3: `td-verificador` (diario 02:00 UTC)
- Revisa todos los HTML generados
- Verifica: SVG presente, ejercicios ≥3, navegación, atribución
- Si algo falla → crea cron de corrección

## Estructura de directorios

```
DibujoTecnico/
├── INDEX.html          # Página principal
├── progress.json       # Estado de cada tema
├── b01-01-formatos-papel.html
├── b01-02-tipos-linea.html
├── ...
├── b09-03-lista-piezas.html
└── README.md
```

## Reglas de oro

1. **NUNCA borrar contenido**, solo añadir
2. **SVG interactivo siempre** — no imágenes estáticas
3. **Progresión estricta** — cada tema construye sobre el anterior
4. **Variedad de ejercicios** — quiz, completar, V/F, identificar en SVG
5. **Contenido en castellano** — TODO en español
6. **Responsive** — debe funcionar en móvil
7. **Un solo archivo HTML** — CSS y JS inline
8. **Atribución** — "Hecho con ❤️ por David Antizar"
