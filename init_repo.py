#!/usr/bin/env python3
"""Inicializa el repo DibujoTecnico: INDEX.html + progress.json + README.md"""

import os
import json

REPO_DIR = '/root/workspace/DibujoTecnico'
os.makedirs(REPO_DIR, exist_ok=True)

# Bloques completos con 53 temas
BLOQUES = [
    {
        "name": "Bloque 1: Normalización",
        "icon": "📏",
        "skills": "td-normalizacion",
        "themes": [
            {"id": "b01-01", "file": "b01-01-formatos-papel.html", "title": "📄 Formatos de papel ISO 216", "desc": "A0, A1, A2, A3, A4 — relación √2"},
            {"id": "b01-02", "file": "b01-02-tipos-linea.html", "title": "📐 Tipos de línea ISO 128", "desc": "Gruesa, fina, discontinua, ejes..."},
            {"id": "b01-03", "file": "b01-03-escalas.html", "title": "🔍 Escalas ISO 5455", "desc": "Natural, ampliación, reducción"},
            {"id": "b01-04", "file": "b01-04-rotulacion.html", "title": "✍️ Rotulación UNE", "desc": "Tipos A y B, alturas, proporciones"},
            {"id": "b01-05", "file": "b01-05-cuadro-rotulacion.html", "title": "📋 Cuadro de rotulación y pie de plano", "desc": "Estructura, datos obligatorios"},
        ]
    },
    {
        "name": "Bloque 2: Proyecciones",
        "icon": "🔲",
        "skills": "td-proyecciones",
        "themes": [
            {"id": "b02-01", "file": "b02-01-proyeccion-ortogonal.html", "title": "👁️ Proyección ortogonal", "desc": "Rayos perpendiculares al plano"},
            {"id": "b02-02", "file": "b02-02-sistema-3-planos.html", "title": "📦 Sistema de 3 planos", "desc": "PV, PH, PL — abatimiento"},
            {"id": "b02-03", "file": "b02-03-vistas-principales.html", "title": "👀 Vistas principales", "desc": "Alzado, planta, perfil"},
            {"id": "b02-04", "file": "b02-04-correspondencia-vistas.html", "title": "🔗 Correspondencia entre vistas", "desc": "X, Y, Z — regla mnemotécnica"},
            {"id": "b02-05", "file": "b02-05-abatimiento-ph.html", "title": "🔄 Abatimiento del PH", "desc": "Giro 90° alrededor de LT"},
            {"id": "b02-06", "file": "b02-06-1o-3o-diedro.html", "title": "🌍 1º diedro vs 3º diedro", "desc": "Europa vs EE.UU."},
            {"id": "b02-07", "file": "b02-07-representacion-piezas.html", "title": "🔧 Representación de piezas", "desc": "Vista principal, mínimo de vistas"},
            {"id": "b02-08", "file": "b02-08-vista-auxiliar-parcial.html", "title": "🔎 Vista auxiliar y parcial", "desc": "Cara inclinada, zona de interés"},
        ]
    },
    {
        "name": "Bloque 3: Perspectivas",
        "icon": "🎨",
        "skills": "td-perspectivas",
        "themes": [
            {"id": "b03-01", "file": "b03-01-isometrica-ejes.html", "title": "📐 Perspectiva isométrica: ejes", "desc": "120° entre ejes, 30° de horizontal"},
            {"id": "b03-02", "file": "b03-02-isometrica-cubos.html", "title": "🧊 Isométrica: cubos y prismas", "desc": "Piezas prismáticas en isométrica"},
            {"id": "b03-03", "file": "b03-03-isometrica-circulos.html", "title": "⭕ Isométrica: círculos y elipses", "desc": "Método de 4 centros, ejes mayor/menor"},
            {"id": "b03-04", "file": "b03-04-caballera.html", "title": "📏 Perspectiva caballera", "desc": "45°, reducción 0.5"},
            {"id": "b03-05", "file": "b03-05-caballera-cilindros.html", "title": "🔩 Caballera: piezas con cilindros", "desc": "Círculos en YZ verdadera magnitud"},
            {"id": "b03-06", "file": "b03-06-dimetrica-monometrica.html", "title": "📊 Dimétrica y monométrica", "desc": "7°/42°, poco usadas pero necesarias"},
        ]
    },
    {
        "name": "Bloque 4: Diedrico — Punto, Recta, Plano",
        "icon": "📍",
        "skills": "td-diedrico-punto-recta-plano",
        "themes": [
            {"id": "b04-01", "file": "b04-01-puntos-cuadrantes.html", "title": "📍 Puntos y cuadrantes", "desc": "A(x,y,z) — 4 cuadrantes, 1º diedro"},
            {"id": "b04-02", "file": "b04-02-puntos-notables.html", "title": "⭐ Puntos notables", "desc": "Bisectores, sobre planos, sobre LT"},
            {"id": "b04-03", "file": "b04-03-recta-trazas.html", "title": "📏 Recta: trazas y posiciones", "desc": "Th, Tv — horizontal, frontal, de punta"},
            {"id": "b04-04", "file": "b04-04-recta-vm.html", "title": "📐 Recta: verdadera magnitud", "desc": "VM por giro y cambio de plano"},
            {"id": "b04-05", "file": "b04-05-plano-trazas.html", "title": "📐 Plano: trazas y posiciones", "desc": "α₁, α₂ — horizontal, frontal, oblicuo"},
            {"id": "b04-06", "file": "b04-06-rectas-notables-plano.html", "title": "↗️ Rectas notables del plano", "desc": "Horizontales, máxima pendiente"},
            {"id": "b04-07", "file": "b04-07-pertenencia.html", "title": "🔗 Pertenencia: punto en recta/plano", "desc": "Método de rectas contenidas"},
            {"id": "b04-08", "file": "b04-08-paralelismo.html", "title": "↔️ Paralelismo", "desc": "Recta-recta, recta-plano, plano-plano"},
            {"id": "b04-09", "file": "b04-09-perpendicularidad.html", "title": "⊥ Perpendicularidad recta-plano", "desc": "r'⊥α₂ y r⊥α₁"},
            {"id": "b04-10", "file": "b04-10-ejercicio-completo-diedrico.html", "title": "🏆 Ejercicio completo diedrico", "desc": "Punto + recta + plano — todo junto"},
        ]
    },
    {
        "name": "Bloque 5: Cortes y Secciones",
        "icon": "✂️",
        "skills": "td-cortes-secciones",
        "themes": [
            {"id": "b05-01", "file": "b05-01-corte-total.html", "title": "✂️ Corte total", "desc": "Hachuras 45°, línea de corte, flechas"},
            {"id": "b05-02", "file": "b05-02-corte-parcial-semicorte.html", "title": "🔪 Corte parcial y semicorte", "desc": "Mitad corte/mitad vista, eje simetría"},
            {"id": "b05-03", "file": "b05-03-corte-escalonado.html", "title": "🪜 Corte escalonado", "desc": "Varios planos paralelos, sin líneas de cambio"},
            {"id": "b05-04", "file": "b05-04-seccion-rotura.html", "title": "📌 Sección y rotura", "desc": "Sección fuera de vista, rotura ondulada"},
            {"id": "b05-05", "file": "b05-05-hachuras.html", "title": "📊 Hachuras y normas", "desc": "45°, separación, piezas macizas"},
            {"id": "b05-06", "file": "b05-06-ejercicio-completo-cortes.html", "title": "🏆 Ejercicio completo cortes", "desc": "Pieza con corte total + semicorte"},
        ]
    },
    {
        "name": "Bloque 6: Acotación",
        "icon": "📏",
        "skills": "td-acotacion",
        "themes": [
            {"id": "b06-01", "file": "b06-01-elementos-cota.html", "title": "📐 Elementos de la cota", "desc": "Línea de cota, auxiliar, valor, flecha"},
            {"id": "b06-02", "file": "b06-02-metodos-cadenas.html", "title": "→ Métodos: cadena y paralelo", "desc": "Acumulación tolerancias, origen común"},
            {"id": "b06-03", "file": "b06-03-simbolos.html", "title": "Φ Símbolos (Φ, R, SR, □)", "desc": "Diámetro, radio, esférico, cuadrado"},
            {"id": "b06-04", "file": "b06-04-reglas-acotacion.html", "title": "📋 Reglas de acotación", "desc": "No repetir, no omitir, funcionales"},
            {"id": "b06-05", "file": "b06-05-ejercicio-completo-acotacion.html", "title": "🏆 Ejercicio completo acotación", "desc": "Pieza cotada completa"},
        ]
    },
    {
        "name": "Bloque 7: Intersecciones y VM",
        "icon": "🔀",
        "skills": "td-intersecciones-vm",
        "themes": [
            {"id": "b07-01", "file": "b07-01-interseccion-recta-plano.html", "title": "🔀 Intersección recta-plano", "desc": "Plano de corte, método general"},
            {"id": "b07-02", "file": "b07-02-interseccion-plano-plano.html", "title": "🔀 Intersección plano-plano", "desc": "Dos planos de corte, recta de intersección"},
            {"id": "b07-03", "file": "b07-03-interseccion-recta-recta.html", "title": "✖️ Intersección recta-recta", "desc": "Puntos cruzados, horizontales/verticales"},
            {"id": "b07-04", "file": "b07-04-vm-giro.html", "title": "🔄 VM por giro", "desc": "Centro de giro, llevar a paralela"},
            {"id": "b07-05", "file": "b07-05-vm-cambio-plano.html", "title": "🔄 VM por cambio de plano", "desc": "Nueva LT paralela a la recta"},
            {"id": "b07-06", "file": "b07-06-distancias.html", "title": "📏 Distancia punto-recta y punto-plano", "desc": "Perpendicular en VM"},
        ]
    },
    {
        "name": "Bloque 8: Abatimientos",
        "icon": "🔄",
        "skills": "td-abatimientos-giros",
        "themes": [
            {"id": "b08-01", "file": "b08-01-concepto-abatimiento.html", "title": "🔄 Concepto de abatimiento", "desc": "Hacer coincidir plano con proyección"},
            {"id": "b08-02", "file": "b08-02-abatimiento-punto.html", "title": "📍 Abatimiento de punto en plano", "desc": "Horizontal del plano, perpendicular a traza"},
            {"id": "b08-03", "file": "b08-03-abatimiento-figuras.html", "title": "🔷 Abatimiento de figuras planas", "desc": "Figura abatida en VM"},
            {"id": "b08-04", "file": "b08-04-aplicaciones-abatimiento.html", "title": "🏆 Aplicaciones del abatimiento", "desc": "VM de ángulos, distancias reales"},
        ]
    },
    {
        "name": "Bloque 9: Planos de Conjunto",
        "icon": "🏗️",
        "skills": "td-planos-conjunto",
        "themes": [
            {"id": "b09-01", "file": "b09-01-plano-conjunto.html", "title": "🏗️ Plano de conjunto", "desc": "Montaje completo, vistas, cortes"},
            {"id": "b09-02", "file": "b09-02-despiece-marcas.html", "title": "🔩 Despiece y marcas", "desc": "Piezas individuales, referencias"},
            {"id": "b09-03", "file": "b09-03-vista-explosiva.html", "title": "💥 Vista explosiva y lista de piezas", "desc": "Orden de montaje, lista completa"},
        ]
    },
]

# Construir lista plana de todos los temas
TODOS_TEMAS = []
for bloque in BLOQUES:
    for tema in bloque["themes"]:
        TODOS_TEMAS.append({
            "id": tema["id"],
            "file": tema["file"],
            "title": tema["title"],
            "desc": tema["desc"],
            "bloque": bloque["name"],
            "icon": bloque["icon"],
            "skills": bloque["skills"],
            "status": "pending",
            "improvement_count": 0,
            "priority": len(TODOS_TEMAS) + 1,
        })

# 1. Crear progress.json
progress = {
    "curso": "Dibujo Técnico Completo",
    "autor": "David Antizar",
    "total_temas": len(TODOS_TEMAS),
    "temas": TODOS_TEMAS,
    "progreso_global": 0,
    "ult_actualizacion": "2026-06-10",
}

with open(os.path.join(REPO_DIR, 'progress.json'), 'w') as f:
    json.dump(progress, f, indent=2, ensure_ascii=False)

# 2. Crear INDEX.html
bloque_html = ""
for bloque in BLOQUES:
    temas_html = ""
    for tema in bloque["themes"]:
        temas_html += f'''            <div class="card">
                <h3>{tema["title"]}</h3>
                <p>{tema["desc"]}</p>
                <a href="{tema["file"]}" class="card-link">Abrir →</a>
            </div>
'''
    bloque_html += f'''
    <section class="bloque">
        <h2>{bloque["icon"]} {bloque["name"]}</h2>
        <div class="grid">
{temas_html}
        </div>
    </section>
'''

index_html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dibujo Técnico Completo — David Antizar</title>
<style>
:root{{--azul:#2563eb;--naranja:#f97316;--verde:#10b981;--rojo:#ef4444;--fondo:#fff;--texto:#1e293b;--gris:#94a3b8;--azul-claro:#eff6ff;--naranja-claro:#fff7ed;--verde-claro:#ecfdf5;--rojo-claro:#fef2f2;--pura-claro:#faf5ff;--pura:#a855f7}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:Inter,system-ui,-apple-system,sans-serif;background:linear-gradient(135deg,#f8faff 0%,#fffaf5 100%);color:var(--texto);line-height:1.7}}
.header{{background:linear-gradient(135deg,var(--azul),#1d4ed8);color:#fff;padding:3rem 1.5rem;text-align:center}}
.header h1{{font-size:2.2rem;margin-bottom:.5rem}}
.header p{{opacity:.9;font-size:1.1rem}}
.header .badge{{display:inline-block;background:rgba(255,255,255,.2);padding:.3rem 1rem;border-radius:20px;margin-top:1rem;font-size:.9rem}}
.container{{max-width:900px;margin:0 auto;padding:1.5rem}}
.bloque{{margin-bottom:3rem}}
.bloque h2{{font-size:1.4rem;color:var(--azul);margin-bottom:1rem;padding-bottom:.5rem;border-bottom:2px solid var(--azul-claro)}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:1rem}}
.card{{background:#fff;border:2px solid #e2e8f0;border-radius:12px;padding:1.2rem;transition:all .2s}}
.card:hover{{border-color:var(--azul);transform:translateY(-2px);box-shadow:0 4px 12px rgba(37,99,235,.1)}}
.card h3{{font-size:1rem;margin-bottom:.5rem;color:var(--texto)}}
.card p{{font-size:.85rem;color:var(--gris);margin-bottom:.8rem}}
.card-link{{display:inline-block;color:var(--azul);text-decoration:none;font-weight:600;font-size:.9rem}}
.card-link:hover{{text-decoration:underline}}
.stats{{display:flex;gap:1rem;margin:2rem 0;flex-wrap:wrap}}
.stat{{background:#fff;border:2px solid #e2e8f0;border-radius:12px;padding:1.2rem;text-align:center;flex:1;min-width:120px}}
.stat .num{{font-size:2rem;font-weight:800;color:var(--azul)}}
.stat .label{{font-size:.8rem;color:var(--gris)}}
.footer{{text-align:center;padding:2rem 1rem;color:var(--gris);font-size:.85rem;border-top:1px solid #e2e8f0;margin-top:2rem}}
</style>
</head>
<body>
<header class="header">
<h1>📐 Dibujo Técnico Completo</h1>
<p>Curso interactivo desde normalización hasta planos de conjunto industrial</p>
<div class="badge">{len(TODOS_TEMAS)} temas · Progresión guiada · SVG interactivo</div>
</header>
<main class="container">
<div class="stats">
    <div class="stat"><div class="num">{len(TODOS_TEMAS)}</div><div class="label">Temas</div></div>
    <div class="stat"><div class="num">{len(BLOQUES)}</div><div class="label">Bloques</div></div>
    <div class="stat"><div class="num">0/{len(TODOS_TEMAS)}</div><div class="label">Completados</div></div>
</div>

{bloque_html}

</main>
<footer class="footer">Hecho con ❤️ por David Antizar</footer>
</body>
</html>
'''

with open(os.path.join(REPO_DIR, 'INDEX.html'), 'w') as f:
    f.write(index_html)

# 3. Crear README.md
readme = f'''# 📐 Dibujo Técnico Completo

Curso interactivo de dibujo técnico desde normalización básica hasta planos de conjunto industrial.

**Autor:** David Antizar  
**Temas:** {len(TODOS_TEMAS)} HTML interactivos con SVG  
**URL:** https://ntizar.github.io/DibujoTecnico/

## 📚 Estructura

| Bloque | Tema | Temas |
|--------|------|-------|
| B01 | Normalización | 5 |
| B02 | Proyecciones | 8 |
| B03 | Perspectivas | 6 |
| B04 | Diedrico | 10 |
| B05 | Cortes y Secciones | 6 |
| B06 | Acotación | 5 |
| B07 | Intersecciones y VM | 6 |
| B08 | Abatimientos | 4 |
| B09 | Planos de Conjunto | 3 |
| **TOTAL** | | **{len(TODOS_TEMAS)}** |

## 🎯 Filosofía

1. **Ver primero, leer después** — SVG interactivo antes de teoría
2. **Interactuar siempre** — click en proyecciones, identificar líneas
3. **Progresión suave** — cada tema construye sobre el anterior
4. **Errores comunes** — cada tema incluye el error típico
5. **Casos reales** — planos reales, piezas industriales

## 🚀 Estado

- **Completados:** 0 / {len(TODOS_TEMAS)}
- **En progreso:** 0
- **Pendientes:** {len(TODOS_TEMAS)}

---

Hecho con ❤️ por David Antizar
'''

with open(os.path.join(REPO_DIR, 'README.md'), 'w') as f:
    f.write(readme)

print(f"✅ Repo inicializado: {len(TODOS_TEMAS)} temas en {len(BLOQUES)} bloques")
print(f"   progress.json: {len(TODOS_TEMAS)} temas")
print(f"   INDEX.html: navegación completa")
print(f"   README.md: documentación")
