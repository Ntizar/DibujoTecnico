#!/usr/bin/env python3
"""Generador de HTML para Dibujo Técnico.
Genera un archivo HTML completo a partir de la definición de tema + contenido del skill TD."""

import os
import sys
import json

REPO_DIR = '/root/workspace/DibujoTecnico'

TEMPLATE = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Dibujo Técnico</title>
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
window.onscroll = function(){{
  var h = document.documentElement;
  var p = (window.scrollY/(h.scrollHeight-h.clientHeight))*100;
  document.getElementById('progress').style.width = p+'%';
}};
</script>
</body>
</html>'''

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 generate_td.py <tema_id>")
        sys.exit(1)

    tema_id = sys.argv[1]

    # Leer progress.json
    with open(os.path.join(REPO_DIR, 'progress.json')) as f:
        progress = json.load(f)

    # Buscar tema
    tema = None
    for t in progress['temas']:
        if t['id'] == tema_id:
            tema = t
            break

    if not tema:
        print(f"Tema {tema_id} no encontrado")
        sys.exit(1)

    # Leer el skill TD correspondiente
    skill_name = tema['skills']
    skill_path = f'/hermes-home/skills/stem/td/{skill_name}/SKILL.md'
    if not os.path.exists(skill_path):
        # Intentar sin carpeta
        skill_path_alt = f'/hermes-home/skills/stem/td/{skill_name}.md'
        if os.path.exists(skill_path_alt):
            skill_path = skill_path_alt

    if not os.path.exists(skill_path):
        print(f"Skill {skill_name} no encontrado en {skill_path}")
        sys.exit(1)

    with open(skill_path) as f:
        skill_content = f.read()

    # Aquí el LLM rellena los placeholders con el contenido del skill
    # Este script es el generador base; el contenido real lo genera el cron
    # usando el skill como fuente de verdad

    print(f"✅ Tema {tema_id} listo para generar")
    print(f"   Archivo: {tema['file']}")
    print(f"   Skill fuente: {skill_name}")
    print(f"   Bloque: {tema['bloque']}")

if __name__ == '__main__':
    main()
