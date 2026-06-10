#!/usr/bin/env python3
"""Generador masivo de temas de Dibujo Técnico que faltan."""

import os
import json

repo = '/root/workspace/DibujoTecnico'

# Temas que faltan
temas_faltantes = [
    {'id': 'b04-05', 'title': '↔️ Paralelismo y perpendicularidad', 'subtitle': 'Dibujo Técnico — Sistema Diédrico',
     'icon': '↔️', 'teoria': 'Dos rectas son paralelas si sus proyecciones son paralelas. Una recta es perpendicular a un plano si es perpendicular a dos rectas del plano (horizontal y frontal).',
     'ejemplos': [
         'Rectas paralelas: r\' ∥ s\' y r ∥ s',
         'Recta ⊥ plano: r\' ⊥ α₂ y r ⊥ α₁',
         'Dos planos paralelos: α₁ ∥ β₁ y α₂ ∥ β₂'
     ],
     'ejercicios': [
         ('¿Cuántas condiciones necesita una recta para ser perpendicular a un plano?', ['1', '2', '3', '4'], '1', '2'),
         ('¿Cómo se representan rectas paralelas en diédrico?', ['Solo en alzado', 'Solo en planta', 'En ambas proyecciones', 'No se pueden representar'], '3', 'En ambas proyecciones'),
         ('Un plano paralelo a otro tiene sus trazas...', ['Perpendiculares', 'Paralelas', 'Oblicuas', 'No tiene trazas'], '2', 'Paralelas'),
         ('Verdadero o Falso — r\' ⊥ α₂ y r ⊥ α₁ implica r ⊥ α', ['Verdadero', 'Falso'], '0', 'Verdadero'),
         ('¿Cuántas proyecciones tienen las rectas paralelas?', ['1', '2', '3', '4'], '1', '2'),
     ]},
    {'id': 'b04-06', 'title': '📏 Verdadera magnitud de rectas', 'subtitle': 'Dibujo Técnico — Sistema Diédrico',
     'icon': '📏', 'teoria': 'Una recta está en verdadera magnitud (VM) cuando es paralela al plano de proyección. Las rectas horizontales tienen VM en planta, las frontales en alzado, y las oblicuas se obtienen por cambio de plano o giro.',
     'ejemplos': [
         'Recta horizontal: VM en planta (r)',
         'Recta frontal: VM en alzado (r\')',
         'Recta oblicua: VM por cambio de plano'
     ],
     'ejercicios': [
         ('¿Cuándo está una recta en VM?', ['Cuando es horizontal', 'Cuando es frontal', 'Cuando es paralela al plano de proyección', 'Nunca'], '2', 'Cuando es paralela al plano de proyección'),
         ('Una recta horizontal tiene VM en...', ['Alzado', 'Planta', 'Perfil', 'No tiene VM'], '1', 'Planta'),
         ('¿Qué método se usa para obtener VM de una recta oblicua?', ['Corte', 'Cambio de plano o giro', 'Abatimiento', 'Perspectiva'], '1', 'Cambio de plano o giro'),
         ('Verdadero o Falso — Una recta frontal tiene VM en alzado', ['Verdadero', 'Falso'], '0', 'Verdadero'),
         ('¿Cuántas proyecciones se necesitan para ver la VM?', ['1', '2', '3', '4'], '0', '1'),
     ]},
    {'id': 'b04-07', 'title': '🔄 Cambio de plano', 'subtitle': 'Dibujo Técnico — Sistema Diédrico',
     'icon': '🔄', 'teoria': 'El cambio de plano consiste en sustituir uno de los planos de proyección por uno nuevo paralelo o perpendicular a la elemento geométrico. Permite obtener VM, verdaderas formas, y simplificar problemas.',
     'ejemplos': [
         '1er cambio: plano vertical nuevo ∥ a r → r\' en VM',
         '2do cambio: plano horizontal nuevo ⊥ a r\' → r en punto',
         'Cambio de plano para obtener VM de un segmento'
     ],
     'ejercicios': [
         ('¿Cuántos planos se cambian en un cambio de plano?', ['0', '1', '2', '3'], '1', '1'),
         ('El nuevo plano debe ser...', ['Paralelo al elemento', 'Perpendicular al elemento', 'Paralelo o perpendicular al elemento', 'En cualquier posición'], '2', 'Paralelo o perpendicular al elemento'),
         ('¿Cuántos cambios se necesitan para ver una recta como punto?', ['1', '2', '3', '4'], '1', '2'),
         ('Verdadero o Falso — El cambio de plano modifica la pieza', ['Verdadero', 'Falso'], '1', 'Falso'),
         ('¿Qué se obtiene con un cambio de plano?', ['VM o verdaderas formas', 'Solo cortes', 'Solo secciones', 'Solo perspectivas'], '0', 'VM o verdaderas formas'),
     ]},
    {'id': 'b04-08', 'title': '🔁 Giro de rectas y planos', 'subtitle': 'Dibujo Técnico — Sistema Diédrico',
     'icon': '🔁', 'teoria': 'El giro consiste en rotar un elemento geométrico alrededor de un eje perpendicular a un plano de proyección. Permite llevar rectas a posiciones particulares (horizontal, frontal) y obtener VM.',
     'ejemplos': [
         'Giro alrededor de eje vertical: r\' describe arco, r se desplaza horizontalmente',
         'Giro alrededor de eje frontal: r describe arco, r\' se desplaza horizontalmente',
         'Giro para llevar recta oblicua a frontal'
     ],
     'ejercicios': [
         ('¿Cuántas posiciones tiene un punto al girar alrededor de eje vertical?', ['1 en alzado, 1 en planta', 'Arco en alzado, horizontal en planta', 'Horizontal en alzado, arco en planta', 'Dos arcos'], '1', 'Arco en alzado, horizontal en planta'),
         ('El eje de giro debe ser...', ['Perpendicular a un plano de proyección', 'Paralelo a la LT', 'Oblicuo a los planos', 'En cualquier posición'], '0', 'Perpendicular a un plano de proyección'),
         ('¿Qué se logra con el giro?', ['VM del elemento', 'Solo cortes', 'Solo secciones', 'Solo perspectivas'], '0', 'VM del elemento'),
         ('Verdadero o Falso — El giro modifica las cotas del elemento', ['Verdadero', 'Falso'], '1', 'Falso'),
         ('¿Cuántos giros se necesitan para ver una recta como punto?', ['1', '2', '3', '4'], '1', '2'),
     ]},
    {'id': 'b04-09', 'title': '📋 Resumen del diedrico básico', 'subtitle': 'Dibujo Técnico — Sistema Diédrico',
     'icon': '📋', 'teoria': 'Resumen completo del diedrico básico: punto, recta, plano, pertenencia, paralelismo, perpendicularidad, VM, cambio de plano y giro. Todo lo necesario para resolver problemas del diédrico.',
     'ejemplos': [
         'Punto: A\' (alzado) + A (planta)',
         'Recta: r\' (alzado) + r (planta) + Th + Tv',
         'Plano: α₁ (traza horizontal) + α₂ (traza vertical)'
     ],
     'ejercicios': [
         ('¿Cuántos elementos básicos tiene el diédrico?', ['2', '3', '4', '5'], '1', '3'),
         ('¿Qué representa α₁?', ['Traza vertical', 'Traza horizontal', 'Línea de tierra', 'Horizontal del plano'], '1', 'Traza horizontal'),
         ('¿Cuántas proyecciones tiene un punto?', ['1', '2', '3', '4'], '1', '2'),
         ('Verdadero o Falso — La recta se representa con 2 proyecciones', ['Verdadero', 'Falso'], '0', 'Verdadero'),
         ('¿Qué se usa para obtener VM de una recta oblicua?', ['Giro o cambio de plano', 'Solo giro', 'Solo cambio de plano', 'Ninguno'], '0', 'Giro o cambio de plano'),
     ]},
    {'id': 'b04-10', 'title': '🎯 Ejercicios finales del diedrico', 'subtitle': 'Dibujo Técnico — Sistema Diédrico',
     'icon': '🎯', 'teoria': 'Ejercicios finales que combinan todos los conceptos del diedrico básico: pertenencia, paralelismo, perpendicularidad, VM, cambio de plano y giro en problemas integrados.',
     'ejemplos': [
         'Ejercicio 1: Determinar si punto P pertenece a plano α',
         'Ejercicio 2: Obtener VM de segmento AB por cambio de plano',
         'Ejercicio 3: Representar recta r perpendicular a plano α'
     ],
     'ejercicios': [
         ('¿Cuántos ejercicios finales hay?', ['3', '5', '7', '10'], '2', '7'),
         ('¿Qué concepto NO se incluye en los ejercicios finales?', ['Pertenencia', 'Paralelismo', 'Perspectiva isométrica', 'Perpendicularidad'], '2', 'Perspectiva isométrica'),
         ('Los ejercicios finales combinan...', ['Un solo concepto', 'Dos conceptos', 'Todos los conceptos', 'Ninguno'], '2', 'Todos los conceptos'),
         ('Verdadero o Falso — Los ejercicios finales son opcionales', ['Verdadero', 'Falso'], '1', 'Falso'),
         ('¿Qué se necesita para resolver los ejercicios finales?', ['Solo punto', 'Punto y recta', 'Punto, recta y plano', 'Solo plano'], '2', 'Punto, recta y plano'),
     ]},
]

def generar_html(tema):
    """Generar HTML para un tema."""
    # Generar ejercicios HTML
    ejercicios_html = ''
    for i, ejer in enumerate(tema['ejercicios'], 1):
        pregunta, opciones, correcta_idx, correcta_texto = ejer
        opciones_html = ''
        for j, opt in enumerate(opciones):
            onclick = f"checkAnswer(this, {j == correcta_idx})"
            opciones_html += f'<button class="quiz-btn" onclick="{onclick}">{opt}</button>\n'
        
        ejercicios_html += f'''
<div class="exercise">
<p>📐 Ejercicio {i}: {pregunta}</p>
<div class="quiz-options">
{opciones_html}
</div>
<p class="feedback"></p>
</div>
'''
    
    # Generar ejemplos HTML
    ejemplos_html = ''
    for ejemplo in tema['ejemplos']:
        ejemplos_html += f'<div class="box box-ejemplo"><strong>🔍 Ejemplo</strong>{ejemplo}</div>\n'
    
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{tema['title']} — {tema['subtitle']}</title>
<style>
:root{{--azul:#2563eb;--naranja:#f97316;--verde:#10b981;--rojo:#ef4444;--fondo:#fff;--texto:#1e293b;--gris:#94a3b8;--azul-claro:#eff6ff;--naranja-claro:#fff7ed;--verde-claro:#ecfdf5;--rojo-claro:#fef2f2;--pura-claro:#faf5ff;--pura:#a855f7}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:Inter,system-ui,-apple-system,sans-serif;background:linear-gradient(135deg,#f8faff 0%,#fffaf5 100%);color:var(--texto);line-height:1.7}}
.header{{background:linear-gradient(135deg,var(--azul),#1d4ed8);color:#fff;padding:2rem 1.5rem;text-align:center}}
.header h1{{font-size:1.8rem;margin-bottom:.5rem}}
.header p{{opacity:.9;font-size:1rem}}
.progress-bar{{height:4px;background:rgba(255,255,255,.3);border-radius:2px;margin-top:1rem;overflow:hidden}}
.progress-fill{{height:100%;background:#fff;border-radius:2px;width:0%;transition:width .3s}}
.container{{max-width:900px;margin:0 auto;padding:1.5rem}}
.chapter{{margin-bottom:2.5rem}}
.chapter-title{{font-size:1.4rem;color:var(--azul);margin-bottom:1rem;padding-bottom:.5rem;border-bottom:2px solid var(--azul-claro)}}
.box{{padding:1rem 1.2rem;border-radius:10px;margin:1rem 0;border-left:4px solid;box-shadow:0 1px 3px rgba(0,0,0,.04)}}
.box-teoria{{background:var(--azul-claro);border-color:var(--azul)}}
.box-ejemplo{{background:var(--naranja-claro);border-color:var(--naranja)}}
.box-error{{background:var(--rojo-claro);border-color:var(--rojo)}}
.box-idea{{background:var(--pura-claro);border-color:var(--pura)}}
.box-success{{background:var(--verde-claro);border-color:var(--verde)}}
.box strong{{display:block;margin-bottom:.3rem}}
.svg-container{{background:#f8fafc;border-radius:12px;padding:1.5rem;margin:1.5rem 0;text-align:center;border:2px solid #e2e8f0}}
.svg-container svg{{max-width:100%;height:auto}}
.svg-container svg text{{font-family:Inter,system-ui,sans-serif}}
.interactive{{background:#f1f5f9;border-radius:12px;padding:1.5rem;margin:1.5rem 0}}
.interactive h3{{color:var(--azul);margin-bottom:1rem;font-size:1.1rem}}
.interactive button{{background:var(--azul);color:#fff;border:none;padding:.5rem 1.2rem;border-radius:6px;cursor:pointer;font-size:.95rem;margin:.3rem}}
.interactive button:hover{{background:#1d4ed8}}
.result{{margin-top:.8rem;padding:.8rem;border-radius:6px;font-weight:600;min-height:2rem}}
.result.ok{{background:var(--verde-claro);color:#065f46}}
.result.fail{{background:var(--rojo-claro);color:#991b1b}}
.exercises{{margin:1.5rem 0}}
.exercise{{background:#f1f5f9;border-radius:8px;padding:1rem;margin:.8rem 0}}
.exercise p{{font-weight:600;margin-bottom:.5rem}}
.quiz-options{{display:flex;gap:.5rem;flex-wrap:wrap;margin:1rem 0}}
.quiz-btn{{padding:.6rem 1.5rem;border-radius:8px;border:2px solid var(--azul);background:#fff;font-size:1.1rem;font-weight:600;cursor:pointer;transition:all .2s}}
.quiz-btn:hover{{background:var(--azul-claro)}}
.quiz-btn.correct{{background:var(--verde);color:#fff;border-color:var(--verde)}}
.quiz-btn.wrong{{background:var(--rojo);color:#fff;border-color:var(--rojo)}}
.summary{{background:var(--azul-claro);border-radius:12px;padding:1.5rem;margin:2rem 0}}
.summary h3{{color:var(--azul);margin-bottom:.8rem}}
.summary ul{{list-style:none;padding:0}}
.summary li{{padding:.3rem 0;padding-left:1.5rem;position:relative}}
.summary li::before{{content:"✓";color:var(--verde);font-weight:bold;position:absolute;left:0}}
.nav{{display:flex;justify-content:space-between;margin:2rem 0;padding:1rem 0;border-top:1px solid #e2e8f0;border-bottom:1px solid #e2e8f0}}
.nav a{{color:var(--azul);text-decoration:none;font-weight:600;padding:.5rem 1rem;border-radius:6px}}
.nav a:hover{{background:var(--azul-claro)}}
.nav .disabled{{color:var(--gris);cursor:default;pointer-events:none}}
.footer{{text-align:center;padding:2rem 1rem;color:var(--gris);font-size:.85rem;border-top:1px solid #e2e8f0;margin-top:2rem}}
</style>
</head>
<body>
<header class="header">
<h1>{tema['title']}</h1>
<p>{tema['subtitle']}</p>
<div class="progress-bar"><div class="progress-fill" id="progress"></div></div>
</header>
<main class="container">

<section class="chapter">
<h2 class="chapter-title">🎯 ¿Qué vamos a aprender?</h2>
<div class="box box-idea">
<strong>💡 Idea clave</strong>
{tema['teoria']}
</div>
<p>En esta sesión aprenderás a:</p>
<ul style="margin:.8rem 0 1rem 1.5rem">
<li>Aplicar los conceptos del diedrico básico</li>
<li>Resolver problemas de pertenencia</li>
<li>Obtener verdaderas magnitudes</li>
<li>Usar cambio de plano y giro</li>
</ul>
</section>

<section class="chapter">
<h2 class="chapter-title">1️⃣ Conceptos principales</h2>
<div class="box box-teoria">
<strong>📖 Teoría</strong>
{tema['teoria']}
</div>
{ejemplos_html}
</section>

<section class="chapter">
<h2 class="chapter-title">📝 Ejercicios</h2>
<div class="exercises">
{ejercicios_html}
</div>
</section>

<div class="box box-error">
<strong>⚠️ Error clásico</strong>
No confundir las proyecciones. A' (con apóstrofo) es el ALZADO → arriba de la LT. A (sin apóstrofo) es la PLANTA → debajo de la LT.
</div>

<div class="box box-idea">
<strong>🔗 Conexión</strong>
Este tema construye sobre los anteriores y prepara para los siguientes. ¡Cada concepto se apoya en los anteriores!
</div>

<div class="summary">
<h3>📋 Resumen de lo aprendido</h3>
<ul>
<li>Conceptos clave del diedrico básico</li>
<li>Pertenencia, paralelismo, perpendicularidad</li>
<li>VM, cambio de plano, giro</li>
<li>Aplicación práctica en ejercicios integrados</li>
<li>¡Ya dominas el diedrico básico! 🎉</li>
</ul>
</div>

<div class="nav">
<a href="b04-03-plano-diedrico.html">← Anterior</a>
<a href="b05-01-cortes.html">Siguiente →</a>
</div>

</main>
<footer class="footer">Hecho con ❤️ por David Antizar</footer>
<script>
function checkAnswer(btn, correct) {{
  var parent = btn.parentElement;
  parent.querySelectorAll('button').forEach(function(b) {{
    b.disabled = true; b.classList.remove('correct','wrong');
  }});
  btn.classList.add(correct ? 'correct' : 'wrong');
  var feedback = parent.nextElementSibling;
  if(feedback && feedback.classList.contains('feedback')) {{
    if(correct) {{
      feedback.textContent = '✅ ¡Correcto! ¡Muy bien!';
      feedback.className = 'feedback correct';
    }} else {{
      feedback.textContent = '❌ ¡Intenta de nuevo!';
      feedback.className = 'feedback incorrect';
      setTimeout(function() {{
        parent.querySelectorAll('button').forEach(function(b) {{
          b.disabled = false; b.classList.remove('correct','wrong');
        }});
        feedback.textContent = '';
        feedback.className = 'feedback';
      }}, 1500);
    }}
  }}
}}

window.onscroll = function(){{
  var h = document.documentElement;
  var p = (window.scrollY/(h.scrollHeight-h.clientHeight))*100;
  document.getElementById('progress').style.width = p+'%';
}};
</script>
</body>
</html>
'''
    return html

# Generar todos los temas
for tema in temas_faltantes:
    html = generar_html(tema)
    filepath = os.path.join(repo, tema['id'].replace('b', 'b') + '-' + tema['id'].split('-')[1] + '.html')
    
    # Ajustar nombre de archivo
    num = tema['id'].split('-')[1]
    filename = f"b{tema['id'].split('-')[0][1:]}-{num}-{tema['title'].lower().replace('🔗', 'pertenencia').replace('↔️', 'paralelismo').replace('📏', 'vm').replace('🔄', 'cambio-plano').replace('🔁', 'giro').replace('📋', 'resumen-diedrico').replace('🎯', 'ejercicios-finales')}.html"
    
    # Usar nombre simple
    filename = f"b{tema['id'].split('-')[0][1:]}-{num}-{tema['title'].split(': ')[-1].lower().replace('🔗', 'pertenencia').replace('↔️', 'paralelismo').replace('📏', 'vm').replace('🔄', 'cambio-plano').replace('🔁', 'giro').replace('📋', 'resumen').replace('🎯', 'ejercicios')}.html"
    
    # Simplificar más
    filename = f"b{tema['id'].split('-')[0][1:]}-{num}-{tema['title'].split('—')[0].strip().split(': ')[-1].strip().lower().replace('🔗', 'pertenencia').replace('↔️', 'paralelismo').replace('📏', 'vm').replace('🔄', 'cambio-plano').replace('🔁', 'giro').replace('📋', 'resumen').replace('🎯', 'ejercicios')}.html"
    
    # Nombre final simple
    filename = f"b{tema['id'].split('-')[0][1:]}-{num}-{tema['title'].split('—')[0].strip().replace('🔗', 'pertenencia').replace('↔️', 'paralelismo').replace('📏', 'vm').replace('🔄', 'cambio-plano').replace('🔁', 'giro').replace('📋', 'resumen').replace('🎯', 'ejercicios').replace(' ', '-').lower()}.html"
    
    # Limpiar nombre
    filename = ''.join(c if c.isalnum() or c in '-_' else '' for c in filename)
    filename = filename[:50] + '.html'
    
    # Si ya existe, saltar
    if os.path.exists(os.path.join(repo, filename)):
        print(f"⏭️  Saltando {filename} (ya existe)")
        continue
    
    with open(os.path.join(repo, filename), 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ Generado: {filename}")

print(f"\n🎉 Total generados: {len(temas_faltantes)}")
