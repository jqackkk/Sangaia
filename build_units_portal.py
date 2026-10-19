#!/usr/bin/env python3
"""
Sangaia Sovereign Measurement & Standards Portal Builder
Creates units.html and sgn/units.html for the Панотерм (°Пт) and Мономер (Мн) system,
and updates weather widgets in environment portals.
"""

import os
import re

BASE_DIR = "/Users/jackdavenport/Sangaia"

def get_units_page_html(lang="en"):
    is_sgn = (lang == "sgn")
    
    title = "Sovereign Weights & Measures System (Панотерм & Мономер) - United Provinces of Sangaia" if not is_sgn else "Сувэрэно Меры & Стандартио Система (Панотерм & Мономер) - Унито Провинциа эк Сангайа"
    
    home_link = "index.html" if not is_sgn else "index.html"
    switch_link = "sgn/units.html" if not is_sgn else "../units.html"
    switch_label = "Сангаиан (SGN)" if not is_sgn else "ENGLISH (EN)"
    logo_src = "media/nav_logo.png" if not is_sgn else "../media/nav_logo.png"
    logo_fallback = "nav_logo.png"
    id_link = "id.html" if not is_sgn else "id.html"
    services_link = "services.html" if not is_sgn else "services.html"
    
    # UI Text
    ui = {
        "home": "Home" if not is_sgn else "Домо",
        "units": "Units & Standards" if not is_sgn else "Меры & Стандартио",
        "services": "All Ministries" if not is_sgn else "Холо Министро",
        "departments": "Departments" if not is_sgn else "Дэпартамэнто",
        "sangaia_id": "Sangaia ID" if not is_sgn else "Сангайа ИД",
        "hero_badge": "National Bureau of Standards • Sovereign Metric & Thermal Directive" if not is_sgn else "Национало Бюро эк Стандартио • Сувэрэно Мэтрико & Тэрмало Дирэктиво",
        "hero_title": "The Sangaian Measurement System" if not is_sgn else "Сангайа Меры & Стандартио Система",
        "hero_sub": "A harmonious synthesis of human-scaled dimensions and clean decimal computation. Featuring the Панотерм (°Пт) temperature scale and the Мономер (Мн) universal base-10 distance family." if not is_sgn else "Хармонико синтезо эк хумано-пропорцио инкаи дэцимало калкулатио. Сувэрэно Панотерм (°Пт) тэрмало скала инкаи Мономер (Мн) универсало дистанциа фасилита.",
        "pill_temp": "🌡️ Temperature (°Пт)" if not is_sgn else "🌡️ Тэмпература (°Пт)",
        "pill_dist": "📏 Distance (Мономер)" if not is_sgn else "📏 Дистанциа (Мономер)",
        "pill_temp_calc": "🧮 Temperature Converter" if not is_sgn else "🧮 Тэмпература Калкулаторо",
        "pill_dist_calc": "📐 Distance Converter" if not is_sgn else "📐 Дистанциа Калкулаторо",
        "pill_sweet_spot": "✨ The Mathematical Sweet Spot" if not is_sgn else "✨ Матэматико Балансо",
    }
    
    return f"""<!DOCTYPE html>
<html lang="{ 'cu' if is_sgn else 'en' }">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        /* --- SANGAIA FRUTIGER AERO & SKEUOMORPHIC STYLES --- */
        :root {{
            --primary: #0284c7;
            --primary-dark: #0369a1;
            --primary-deep: #0c4a6e;
            --primary-light: #38bdf8;
            --primary-pale: #f0f9ff;
            --primary-border: #bae6fd;
            --accent-green: #10b981;
            --accent-gold: #f59e0b;
            --text-dark: #0f172a;
            --text-muted: #475569;
            --card-bg: rgba(255, 255, 255, 0.94);
            --shadow-gloss: 0 4px 20px rgba(0,0,0,0.08), inset 0 1px 0 rgba(255,255,255,0.9);
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}

        body {{
            background: #f0fdf4 radial-gradient(circle at 50% 0%, #ffffff 0%, #e0f2fe 100%) no-repeat fixed;
            min-height: 100vh;
            width: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-family: 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
            color: var(--text-dark);
            line-height: 1.6;
            -webkit-font-smoothing: antialiased;
        }}

        .main-container {{
            width: 100%;
            margin: 0;
            padding: 0;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }}

        /* --- GLOBAL METAL HEADER --- */
        #globalheader {{
            display: flex;
            align-items: center;
            position: relative;
            width: 100%;
            height: 38px;
            background: linear-gradient(to bottom, #5e5e5e 0%, #3e3e3e 50%, #2d2d2d 51%, #1f1f1f 100%);
            border-top: 1px solid #222;
            border-bottom: 1px solid #000;
            box-shadow: inset 0 1px 0 rgba(255,255,255,0.15), 0 2px 4px rgba(0,0,0,0.2);
            font-size: 11px;
            z-index: 100;
        }}

        #globalnav {{
            flex-grow: 1;
            margin: 0;
            padding: 0;
            list-style: none;
            display: flex;
            justify-content: center;
            height: 100%;
        }}

        #globalnav li {{ position: relative; height: 100%; display: flex; align-items: center; }}
        #globalnav li::after {{
            content: ""; position: absolute; right: 0; width: 1px; height: 100%;
            background: linear-gradient(to bottom, #333, #111); box-shadow: 1px 0 0 rgba(255,255,255,0.08);
        }}
        #globalnav li:first-child::before {{
            content: ""; position: absolute; left: 0; width: 1px; height: 100%;
            background: linear-gradient(to bottom, #333, #111); box-shadow: 1px 0 0 rgba(255,255,255,0.08);
        }}

        #globalnav li a {{
            display: block; color: #e8e8e8; text-decoration: none; text-shadow: 0 -1px 0 rgba(0,0,0,0.8);
            font-weight: bold; padding: 0 14px; line-height: 38px;
            transition: all 0.2s ease;
            white-space: nowrap;
        }}

        #globalnav li a:hover {{
            color: #fff;
            background: linear-gradient(rgba(255,255,255,0.08), rgba(255,255,255,0));
            text-shadow: 0 0 8px rgba(255, 255, 255, 0.8), 0 -1px 0 rgba(0,0,0,0.8);
        }}

        #globalnav li a.active {{
            color: #fff;
            background: rgba(0,0,0,0.3);
            box-shadow: inset 0 2px 5px rgba(0,0,0,0.4);
            border-bottom: 2px solid var(--primary-light);
        }}

        /* --- SKEUOMORPHIC BUTTONS --- */
        .sangaia-btn {{
            font-size: 0.88rem;
            font-family: inherit;
            height: 2.3em;
            padding: 0 1.2em;
            border-radius: 5px;
            position: relative;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            transition: all 0.2s ease;
            border: 1px solid #94a3b8;
            background: linear-gradient(to bottom, #ffffff 0%, #f1f5f9 45%, #e2e8f0 100%);
            box-shadow: 0 1px 3px rgba(0,0,0,0.1), inset 0 1px 0 rgba(255,255,255,0.9);
            color: #0f172a;
            font-weight: bold;
        }}

        .sangaia-btn:hover {{
            background: linear-gradient(to bottom, #ffffff 0%, #f8fafc 45%, #cbd5e1 100%);
            box-shadow: 0 2px 6px rgba(15, 23, 42, 0.15), inset 0 1px 0 #ffffff;
            transform: translateY(-1px);
        }}

        .btn-cyan {{
            background: linear-gradient(to bottom, #38bdf8 0%, #0284c7 60%, #0369a1 100%);
            border: 1px solid #0c4a6e;
            color: #ffffff !important;
            text-shadow: 0 -1px 1px rgba(0,0,0,0.4);
            box-shadow: 0 2px 5px rgba(2, 132, 199, 0.25), inset 0 1px 0 rgba(255,255,255,0.4);
        }}

        .btn-cyan:hover {{
            background: linear-gradient(to bottom, #7dd3fc 0%, #0ea5e9 40%, #0284c7 100%);
            box-shadow: 0 4px 10px rgba(2, 132, 199, 0.35);
        }}

        /* --- CONTENT WRAPPER --- */
        .content-wrapper {{
            max-width: 1200px;
            width: 100%;
            margin: 0 auto;
            padding: 24px 20px 60px 20px;
            display: flex;
            flex-direction: column;
            gap: 32px;
        }}

        /* --- HERO BANNER --- */
        .hero-banner {{
            background: linear-gradient(135deg, #0c4a6e 0%, #0284c7 50%, #0d9488 100%);
            border: 1px solid #7dd3fc;
            border-radius: 12px;
            padding: 36px 32px;
            position: relative;
            overflow: hidden;
            color: #ffffff;
            box-shadow: 0 10px 30px rgba(12, 74, 110, 0.25), inset 0 1px 0 rgba(255,255,255,0.4);
        }}

        .hero-banner::before {{
            content: "";
            position: absolute;
            top: 0; left: 0; right: 0; height: 50%;
            background: linear-gradient(to bottom, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 100%);
            pointer-events: none;
        }}

        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 4px 12px;
            background: rgba(255, 255, 255, 0.15);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: bold;
            letter-spacing: 0.8px;
            text-transform: uppercase;
            margin-bottom: 12px;
            backdrop-filter: blur(4px);
        }}

        .hero-title {{
            font-size: 2.3rem;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: 8px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.3);
        }}

        .hero-sub {{
            font-size: 1.05rem;
            color: rgba(255, 255, 255, 0.92);
            max-width: 880px;
            margin-bottom: 24px;
            text-shadow: 0 1px 2px rgba(0,0,0,0.2);
        }}

        .jump-pills-row {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .jump-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 7px 15px;
            border-radius: 20px;
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid #cbd5e1;
            font-size: 0.82rem;
            font-weight: bold;
            color: var(--primary-deep);
            text-decoration: none;
            box-shadow: 0 1px 3px rgba(0,0,0,0.06);
            transition: all 0.2s ease;
            cursor: pointer;
        }}

        .jump-pill:hover {{
            background: #ffffff;
            transform: translateY(-1px);
            box-shadow: 0 3px 8px rgba(0,0,0,0.12);
        }}

        /* --- SKEUOMORPHIC PANEL --- */
        .glass-panel {{
            background: var(--card-bg);
            border: 1px solid #cbd5e1;
            border-radius: 12px;
            padding: 30px;
            box-shadow: var(--shadow-gloss);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            display: flex;
            flex-direction: column;
            gap: 22px;
            position: relative;
        }}

        .panel-header {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            border-bottom: 2px solid var(--primary-pale);
            padding-bottom: 16px;
        }}

        .panel-title {{
            font-size: 1.6rem;
            font-weight: 800;
            color: var(--primary-deep);
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .panel-desc {{
            font-size: 0.95rem;
            color: var(--text-muted);
        }}

        /* --- FORMULA CALLOUT CARDS --- */
        .formula-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
        }}

        .formula-card {{
            background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
            border: 1px solid #e2e8f0;
            border-left: 4px solid var(--primary);
            border-radius: 8px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.03);
        }}

        .formula-header {{
            font-size: 0.78rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.6px;
            color: var(--primary-dark);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .formula-math {{
            font-family: 'Courier New', monospace;
            font-size: 1.25rem;
            font-weight: bold;
            color: var(--primary-deep);
            background: #f0f9ff;
            padding: 6px 12px;
            border-radius: 4px;
            border: 1px solid #bae6fd;
            display: inline-block;
        }}

        .formula-rule {{
            font-size: 0.88rem;
            color: var(--text-dark);
            line-height: 1.5;
        }}

        /* --- INTERACTIVE CONVERTER WIDGET --- */
        .converter-widget {{
            background: linear-gradient(135deg, #f8fafc 0%, #f0f9ff 100%);
            border: 1px solid #bae6fd;
            border-radius: 10px;
            padding: 24px;
            display: flex;
            flex-direction: column;
            gap: 20px;
            box-shadow: inset 0 1px 0 #ffffff, 0 4px 12px rgba(2, 132, 199, 0.08);
        }}

        .inputs-row {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 16px;
        }}

        .input-card {{
            background: #ffffff;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.04);
            transition: all 0.2s ease;
        }}

        .input-card:focus-within {{
            border-color: var(--primary);
            box-shadow: 0 0 0 3px var(--primary-pale);
        }}

        .input-label {{
            font-size: 0.82rem;
            font-weight: bold;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: flex;
            justify-content: space-between;
        }}

        .input-val {{
            font-size: 1.7rem;
            font-weight: 800;
            color: var(--primary-deep);
            border: none;
            outline: none;
            width: 100%;
            background: transparent;
            font-family: inherit;
        }}

        .mental-math-box {{
            background: #ffffff;
            border-left: 4px solid var(--accent-green);
            border-top: 1px solid #e2e8f0;
            border-right: 1px solid #e2e8f0;
            border-bottom: 1px solid #e2e8f0;
            border-radius: 6px;
            padding: 14px 18px;
            font-size: 0.88rem;
            color: var(--text-dark);
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        /* --- SKEUOMORPHIC DATA TABLE --- */
        .standards-table-wrap {{
            overflow-x: auto;
            border-radius: 8px;
            border: 1px solid #cbd5e1;
            box-shadow: 0 2px 6px rgba(0,0,0,0.04);
        }}

        .standards-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
            text-align: left;
            background: #ffffff;
        }}

        .standards-table th {{
            background: linear-gradient(to bottom, #f1f5f9 0%, #e2e8f0 100%);
            color: var(--text-dark);
            font-weight: 800;
            padding: 12px 16px;
            border-bottom: 1px solid #cbd5e1;
            white-space: nowrap;
        }}

        .standards-table td {{
            padding: 14px 16px;
            border-bottom: 1px solid #f1f5f9;
            color: var(--text-dark);
            vertical-align: middle;
        }}

        .standards-table tr:hover td {{
            background: #f8fafc;
        }}

        .badge-unit {{
            display: inline-block;
            font-weight: 800;
            font-family: 'Courier New', monospace;
            background: #f0f9ff;
            color: #0369a1;
            border: 1px solid #bae6fd;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.9rem;
        }}

        .ref-pill {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #ecfdf5;
            color: #065f46;
            border: 1px solid #a7f3d0;
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.82rem;
            font-weight: bold;
        }}

        /* --- FOOTER --- */
        .page-footer {{
            width: 100%;
            background: linear-gradient(to bottom, #1e293b 0%, #0f172a 100%);
            color: #94a3b8;
            padding: 32px 20px;
            border-top: 1px solid #334155;
            font-size: 0.85rem;
            text-align: center;
            margin-top: 40px;
        }}

        @media (max-width: 768px) {{
            .hero-title {{ font-size: 1.7rem; }}
            .panel-title {{ font-size: 1.35rem; }}
            .inputs-row {{ grid-template-columns: 1fr; }}
            .content-wrapper {{ padding: 16px 12px 40px 12px; }}
            .glass-panel {{ padding: 20px 16px; }}
        }}
    </style>
</head>
<body>

<div class="main-container">

    <!-- GLOBAL METAL HEADER -->
    <nav id="globalheader">
        <div style="position: absolute; left: 15px; display: flex; align-items: center; height: 100%;">
            <a href="https://sangaia.org/index.html">
                <img src="{logo_src}" onerror="this.onerror=null; this.src='{logo_fallback}';" style="height: 22px; width: auto;" alt="Sangaia Logo">
            </a>
        </div>
        <div style="position: absolute; right: 15px; display: flex; align-items: center; gap: 12px; height: 100%; z-index: 100;">
            <div id="auth-widget">
                <a href="{id_link}" style="color: #bbb; text-decoration: none; font-size: 11px; font-weight: bold; letter-spacing: 0.5px; padding: 3px 8px; border: 1px solid #444; border-radius: 4px; background: linear-gradient(to bottom, #555, #333); box-shadow: 0 1px 2px rgba(0,0,0,0.3); transition: all 0.2s ease;">{ui['sangaia_id']}</a>
            </div>
            <a href="{switch_link}" style="color: #bbb; text-decoration: none; font-size: 11px; font-weight: bold; letter-spacing: 0.5px; padding: 3px 8px; border: 1px solid #444; border-radius: 4px; background: linear-gradient(to bottom, #555, #333); box-shadow: 0 1px 2px rgba(0,0,0,0.3); transition: all 0.2s ease;">{switch_label}</a>
        </div>
        <ul id="globalnav">
            <li><a href="{home_link}">{ui['home']}</a></li>
            <li><a href="units.html" class="active">{ui['units']}</a></li>
            <li><a href="services.html">{ui['services']}</a></li>
            <li><a href="{id_link}">{ui['sangaia_id']}</a></li>
        </ul>
    </nav>

    <div class="content-wrapper">

        <!-- HERO BANNER -->
        <header class="hero-banner" id="overview">
            <span class="hero-badge">🏛️ {ui['hero_badge']}</span>
            <h1 class="hero-title">{ui['hero_title']}</h1>
            <p class="hero-sub">{ui['hero_sub']}</p>
            <div class="jump-pills-row">
                <a href="#temperature" class="jump-pill">{ui['pill_temp']}</a>
                <a href="#temp-converter" class="jump-pill">{ui['pill_temp_calc']}</a>
                <a href="#monomer-distance" class="jump-pill">{ui['pill_dist']}</a>
                <a href="#dist-converter" class="jump-pill">{ui['pill_dist_calc']}</a>
                <a href="#sweet-spot" class="jump-pill">{ui['pill_sweet_spot']}</a>
            </div>
        </header>

        <!-- SECTION 1: TEMPERATURE SYSTEM (ПАНОТЕРМ) -->
        <section class="glass-panel" id="temperature">
            <div class="panel-header">
                <h2 class="panel-title">🌡️ { 'The Panotherm (°Пт) Thermal Scale' if not is_sgn else 'Панотерм (°Пт) Сувэрэно Тэрмало Скала' }</h2>
                <p class="panel-desc">{ 'Official statutory temperature scale of Sangaia. Harmonized directly with both Celsius and Fahrenheit through single-digit mental operations.' if not is_sgn else 'Официало статуторо тэмпература скала эк Сангайа. Дирэкто гармонисадо куно Целсиус инкаи Фаренхаит виа уно-дигито ментало оператио.' }</p>
            </div>

            <!-- Governing Formulas -->
            <div class="formula-grid">
                <div class="formula-card">
                    <span class="formula-header">📐 { 'Celsius Definition' if not is_sgn else 'Целсиус Дэфинитио' }</span>
                    <div class="formula-math">°Пт = 0.9 × °C</div>
                    <p class="formula-rule"><strong>{ 'Mental Rule' if not is_sgn else 'Ментало Руло' }:</strong> { 'Subtract 10% from the Celsius temperature (e.g. 30°C - 3 = 27°Пт).' if not is_sgn else 'Субтракто 10% эк Целсиус тэмпература (наприм. 30°C - 3 = 27°Пт).' }</p>
                </div>
                <div class="formula-card">
                    <span class="formula-header">📐 { 'Fahrenheit Definition' if not is_sgn else 'Фаренхаит Дэфинитио' }</span>
                    <div class="formula-math">°Пт = 0.5 × (°F - 32)</div>
                    <p class="formula-rule"><strong>{ 'Mental Rule' if not is_sgn else 'Ментало Руло' }:</strong> { 'Drop 32, then cut the remainder in half (e.g. 86°F - 32 = 54 ÷ 2 = 27°Пт).' if not is_sgn else 'Дропо 32, постя дивидо ин дуо (наприм. 86°F - 32 = 54 ÷ 2 = 27°Пт).' }</p>
                </div>
                <div class="formula-card">
                    <span class="formula-header">🔄 { 'Reverse to Fahrenheit' if not is_sgn else 'Рэвэрсо ад Фаренхаит' }</span>
                    <div class="formula-math">°F = (2 × °Пт) + 32</div>
                    <p class="formula-rule"><strong>{ 'Mental Rule' if not is_sgn else 'Ментало Руло' }:</strong> { 'Double the Panotherms, then add 32 (e.g. 9°Пт → 18 + 32 = 50°F; 27°Пт → 54 + 32 = 86°F).' if not is_sgn else 'Дубло Панотерм, постя аддо 32 (наприм. 9°Пт → 18 + 32 = 50°F; 27°Пт → 54 + 32 = 86°F).' }</p>
                </div>
                <div class="formula-card">
                    <span class="formula-header">🔄 { 'Reverse to Celsius' if not is_sgn else 'Рэвэрсо ад Целсиус' }</span>
                    <div class="formula-math">°C = (°Пт ÷ 9) × 10</div>
                    <p class="formula-rule"><strong>{ 'Mental Rule' if not is_sgn else 'Ментало Руло' }:</strong> { 'Divide by 9, then multiply by 10 (e.g. 18°Пт → 2 × 10 = 20°C; 27°Пт → 3 × 10 = 30°C).' if not is_sgn else 'Дивидо виа 9, постя мултиплико виа 10 (наприм. 18°Пт → 2 × 10 = 20°C).' }</p>
                </div>
            </div>

            <!-- Key Milestones -->
            <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; padding: 20px;">
                <h3 style="font-size: 1.05rem; font-weight: bold; color: var(--primary-deep); margin-bottom: 12px;">🌟 { 'Key Human Reference Temperatures in Panotherms' if not is_sgn else 'Примаро Хумано Тэрмало Пункто ин Панотерм' }</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; text-align: center;">
                    <div style="background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 6px; padding: 12px;">
                        <div style="font-size: 1.4rem; font-weight: 800; color: #0284c7;">0°Пт</div>
                        <div style="font-size: 0.8rem; font-weight: bold; color: #475569;">{ 'Freezing Water' if not is_sgn else 'Гласио Пункто' }</div>
                        <div style="font-size: 0.75rem; color: #64748b;">0°C / 32°F</div>
                    </div>
                    <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 12px;">
                        <div style="font-size: 1.4rem; font-weight: 800; color: #16a34a;">18°Пт</div>
                        <div style="font-size: 0.8rem; font-weight: bold; color: #475569;">{ 'Room Comfort' if not is_sgn else 'Комфорто Кабина' }</div>
                        <div style="font-size: 0.75rem; color: #64748b;">20°C / 68°F</div>
                    </div>
                    <div style="background: #fefce8; border: 1px solid #fef08a; border-radius: 6px; padding: 12px;">
                        <div style="font-size: 1.4rem; font-weight: 800; color: #ca8a04;">27°Пт</div>
                        <div style="font-size: 0.8rem; font-weight: bold; color: #475569;">{ 'Warm Summer Day' if not is_sgn else 'Вэрано Калоро' }</div>
                        <div style="font-size: 0.75rem; color: #64748b;">30°C / 86°F</div>
                    </div>
                    <div style="background: #fef2f2; border: 1px solid #fecaca; border-radius: 6px; padding: 12px;">
                        <div style="font-size: 1.4rem; font-weight: 800; color: #dc2626;">33.3°Пт</div>
                        <div style="font-size: 0.8rem; font-weight: bold; color: #475569;">{ 'Human Body Core' if not is_sgn else 'Корпо Температура' }</div>
                        <div style="font-size: 0.75rem; color: #64748b;">37°C / 98.6°F</div>
                    </div>
                </div>
            </div>

            <!-- INTERACTIVE TEMPERATURE CONVERTER -->
            <div class="converter-widget" id="temp-converter">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: var(--primary-deep);">🧮 { 'Interactive Panotherm / Metric / Imperial Converter' if not is_sgn else 'Интерактиво Панотерм / Мэтрико / Империало Калкулаторо' }</h3>
                    <span style="font-size: 0.8rem; background: #e0f2fe; color: #0369a1; padding: 3px 10px; border-radius: 12px; font-weight: bold;">LIVE BIDIRECTIONAL</span>
                </div>

                <div class="inputs-row">
                    <div class="input-card">
                        <div class="input-label">
                            <span>{ 'Panotherm' if not is_sgn else 'Панотерм' }</span>
                            <span style="color:var(--primary); font-weight:800;">°Пт</span>
                        </div>
                        <input type="number" class="input-val" id="input-temp-pt" value="27" step="0.5">
                    </div>
                    <div class="input-card">
                        <div class="input-label">
                            <span>{ 'Celsius' if not is_sgn else 'Целсиус' }</span>
                            <span style="color:#059669; font-weight:800;">°C</span>
                        </div>
                        <input type="number" class="input-val" id="input-temp-c" value="30" step="0.5">
                    </div>
                    <div class="input-card">
                        <div class="input-label">
                            <span>{ 'Fahrenheit' if not is_sgn else 'Фаренхаит' }</span>
                            <span style="color:#d97706; font-weight:800;">°F</span>
                        </div>
                        <input type="number" class="input-val" id="input-temp-f" value="86" step="1">
                    </div>
                </div>

                <!-- Slider -->
                <div style="display:flex; flex-direction:column; gap:6px;">
                    <div style="display:flex; justify-content:space-between; font-size:0.75rem; color:#64748b; font-weight:bold;">
                        <span>-36°Пт (-40°C / -40°F)</span>
                        <span>0°Пт (Freezing)</span>
                        <span>18°Пт (Room)</span>
                        <span>27°Пт (Summer)</span>
                        <span>54°Пт (60°C / 140°F)</span>
                    </div>
                    <input type="range" id="temp-slider" min="-36" max="54" value="27" step="0.5" style="width:100%; cursor:pointer;">
                </div>

                <!-- Dynamic Mental Math Breakdown Box -->
                <div class="mental-math-box" id="temp-mental-box">
                    <strong>💡 { 'How to compute this instantly in your head:' if not is_sgn else 'Комо калкулато ин мэнтало рапидо:' }</strong>
                    <div id="temp-mental-steps">{ 'From 86°F: Drop 32 (54), cut in half → 27°Пт. From 30°C: Subtract 10% (-3) → 27°Пт.' if not is_sgn else 'Эк 86°F: Дропо 32 (54), дивидо виа 2 → 27°Пт. Эк 30°C: Субтракто 10% (-3) → 27°Пт.' }</div>
                </div>
            </div>
        </section>

        <!-- SECTION 2: UNIVERSAL DISTANCE SYSTEM (МОНОМЕР) -->
        <section class="glass-panel" id="monomer-distance">
            <div class="panel-header">
                <h2 class="panel-title">📏 { 'The Universal Monomer (Мн) Distance Family' if not is_sgn else 'Мономер (Мн) Универсало Дистанциа Фасилита' }</h2>
                <p class="panel-desc">{ 'Derived from the Slavic-Cyrillic root Мер (Mer — "measure/dimension") and Greek Mono- (single/one). Designed with pure base-10 metric scaling, while its units perfectly track imperial visual benchmarks.' if not is_sgn else 'Оригино эк Слав-Кирилико корен Мер (Мэра) инкаи Греко Моно- (уно). Плэно базо-10 мэтрико структура куно натурало хумано пропорцио.' }</p>
            </div>

            <!-- Mathematical Sweet Spot -->
            <div style="background: linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 100%); border: 1px solid #a7f3d0; border-radius: 8px; padding: 22px; display:flex; flex-direction:column; gap:10px;" id="sweet-spot">
                <div style="display:flex; align-items:center; gap:8px;">
                    <span style="font-size:1.4rem;">✨</span>
                    <h3 style="font-size:1.2rem; font-weight:800; color:#065f46;">{ 'The Mathematical Sweet Spot: 1 Monomer = Exactly 2.5 Centimeters' if not is_sgn else 'Матэматико Балансо: 1 Мономер = Ексакто 2.5 Сантимэтра' }</h3>
                </div>
                <p style="font-size:0.95rem; color:#047857; line-height:1.6;">
                    { 'By defining 1 Monomer (1 Мн) as exactly 2.5 cm, we achieve a unit that is 98.4% identical to an international inch (2.54 cm). All awkward imperial fractions (like multiplying by 12 or 5,280) are replaced by clean base-10 decimal multiples, while maintaining perfect human visual reference points!' if not is_sgn else 'Дэфинито эк 1 Мономер (1 Мн) комо 2.5 см гармонисо 98.4% куно инч (2.54 см). Холо компликадо импэриало матэматика (виа 12 вэл 5,280) рэнэвадо виа чисте базо-10 мэтрико!' }
                </p>
                <div style="display:flex; gap:16px; flex-wrap:wrap; margin-top:6px;">
                    <div class="ref-pill">🔟 10 Мономер = 1 Декамер (Replaces Foot)</div>
                    <div class="ref-pill">📐 30 Мономер = 1 Тридека (Replaces Yard)</div>
                    <div class="ref-pill">🎸 40 Мономер = 1 Квадродека (Replaces Meter)</div>
                    <div class="ref-pill">🚶 60,000 Мономер = 1 Киломер (Replaces Mile)</div>
                </div>
            </div>

            <!-- Comparative Standards Table -->
            <div class="standards-table-wrap">
                <table class="standards-table">
                    <thead>
                        <tr>
                            <th>{ 'Metric / Imperial Unit' if not is_sgn else 'Мэтрико / Импэриало' }</th>
                            <th>{ 'Exact Conversion' if not is_sgn else 'Ексакто Конвэрсио' }</th>
                            <th>{ 'Cyrillic Unit Name' if not is_sgn else 'Кирилико Номэ' }</th>
                            <th>{ 'Symbol' if not is_sgn else 'Символо' }</th>
                            <th>{ 'Monomer Value' if not is_sgn else 'Мономер Валорэ' }</th>
                            <th>{ 'Visual Size Reference' if not is_sgn else 'Хумано Пропорцио' }</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>1 Centimeter</strong> (1 cm)</td>
                            <td>0.4 Мн (1 cm = 0.4 Мн)</td>
                            <td>Децимн (Decimn)</td>
                            <td><span class="badge-unit">дмн</span></td>
                            <td>0.4 Мн</td>
                            <td><span class="ref-pill">💅 Width of a fingernail</span></td>
                        </tr>
                        <tr>
                            <td><strong>1 Inch</strong> (1 in = 2.54 cm)</td>
                            <td>1.016 Мн (≈ 1:1)</td>
                            <td>Мономер (Monomer)</td>
                            <td><span class="badge-unit">Мн</span></td>
                            <td>1.0 Мн (2.5 cm)</td>
                            <td><span class="ref-pill">👍 Knuckle of a thumb</span></td>
                        </tr>
                        <tr>
                            <td><strong>1 Foot</strong> (1 ft = 12 in)</td>
                            <td>12.19 Мн (≈ 10 Мн)</td>
                            <td>Декамер (Dekamer)</td>
                            <td><span class="badge-unit">Дмн</span></td>
                            <td>10 Мн (25 cm)</td>
                            <td><span class="ref-pill">🦶 Length of a human foot</span></td>
                        </tr>
                        <tr>
                            <td><strong>1 Yard</strong> (1 yd = 3 ft)</td>
                            <td>36.57 Мн (≈ 30 Мн)</td>
                            <td>Тридека (Trideka)</td>
                            <td><span class="badge-unit">3Дмн</span></td>
                            <td>30 Мн (75 cm)</td>
                            <td><span class="ref-pill">🚶 One large stride</span></td>
                        </tr>
                        <tr>
                            <td><strong>1 Meter</strong> (1 m = 100 cm)</td>
                            <td>40 Мн (Exact)</td>
                            <td>Квадродека (Kvadrodeka)</td>
                            <td><span class="badge-unit">4Дмн</span></td>
                            <td>40 Мн (100 cm)</td>
                            <td><span class="ref-pill">🎸 Guitar length</span></td>
                        </tr>
                        <tr>
                            <td><strong>1 Mile</strong> (1 mi = 5,280 ft)</td>
                            <td>63,360 Мн (≈ 60,000 Мн)</td>
                            <td>Киломер (Kilomer)</td>
                            <td><span class="badge-unit">Кмн</span></td>
                            <td>60,000 Мн (1.5 km)</td>
                            <td><span class="ref-pill">⏱️ 15-minute brisk walk</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>

            <!-- INTERACTIVE DISTANCE CONVERTER -->
            <div class="converter-widget" id="dist-converter">
                <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
                    <h3 style="font-size: 1.15rem; font-weight: 800; color: var(--primary-deep);">📐 { 'Interactive Universal Distance & Length Converter' if not is_sgn else 'Интерактиво Универсало Дистанциа Калкулаторо' }</h3>
                    <span style="font-size: 0.8rem; background: #e0f2fe; color: #0369a1; padding: 3px 10px; border-radius: 12px; font-weight: bold;">BASE-10 SCALED</span>
                </div>

                <div style="display:grid; grid-template-columns: 2fr 1fr; gap:16px;">
                    <div class="input-card">
                        <div class="input-label">
                            <span>{ 'Input Value' if not is_sgn else 'Инпут Валорэ' }</span>
                        </div>
                        <input type="number" class="input-val" id="dist-input-val" value="10" step="any">
                    </div>
                    <div class="input-card">
                        <div class="input-label">
                            <span>{ 'Unit' if not is_sgn else 'Унито' }</span>
                        </div>
                        <select class="input-val" id="dist-input-unit" style="font-size:1.1rem; cursor:pointer;">
                            <optgroup label="Sangaian System (Cyrillic)">
                                <option value="mn" selected>Мономер (Мн - 2.5 cm)</option>
                                <option value="dmn">Декамер (Дмн - 10 Мн / 25 cm)</option>
                                <option value="trideka">Тридека (3Дмн - 30 Мн / 75 cm)</option>
                                <option value="kvadrodeka">Квадродека (4Дмн - 40 Мн / 1 m)</option>
                                <option value="kmn">Киломер (Кмн - 60,000 Мн / 1.5 km)</option>
                                <option value="decimn">Децимн (дмн - 0.4 Мн / 1 cm)</option>
                            </optgroup>
                            <optgroup label="Metric System">
                                <option value="cm">Centimeters (cm)</option>
                                <option value="m">Meters (m)</option>
                                <option value="km">Kilometers (km)</option>
                            </optgroup>
                            <optgroup label="Imperial System">
                                <option value="in">Inches (in)</option>
                                <option value="ft">Feet (ft)</option>
                                <option value="yd">Yards (yd)</option>
                                <option value="mi">Miles (mi)</option>
                            </optgroup>
                        </select>
                    </div>
                </div>

                <!-- Results Output Grid -->
                <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap:12px;" id="dist-results-grid">
                    <!-- Populated dynamically via JS -->
                </div>

                <!-- Dynamic Mental Shortcut Tip -->
                <div class="mental-math-box" id="dist-mental-box">
                    <strong>💡 { 'Effortless Mental Math Shortcut:' if not is_sgn else 'Ментало Рапидо Схорткут:' }</strong>
                    <div id="dist-mental-tip">{ 'Monomers to Centimeters: Multiply by 2.5 (10 Мн × 2.5 = 25 cm). Dekamer to Feet: 1:1 human foot scale.' if not is_sgn else 'Мономер ад Сантимэтра: Мултиплико виа 2.5. Киломер ад Майл: Дивидо виа 6.' }</div>
                </div>
            </div>
        </section>

    </div>

    <!-- SKEUOMORPHIC FOOTER -->
    <footer class="page-footer">
        <p>{ 'Official Weights & Measures Standards Directorate • United Provinces of Sangaia' if not is_sgn else 'Официало Меры & Стандартио Директорио • Унито Провинциа эк Сангайа' }</p>
        <p style="font-size:0.75rem; color:#64748b; margin-top:4px;">{ 'All standards cryptographically registered under the Aretocratic Seal. Base-10 Sovereign Metric Directive.' if not is_sgn else 'Холо стандартио криптографико записадо суб Арэтократико Сигило.' }</p>
    </footer>

</div>

<script>
document.addEventListener('DOMContentLoaded', () => {{
    // --- 1. TEMPERATURE CONVERTER ENGINE ---
    const inPt = document.getElementById('input-temp-pt');
    const inC = document.getElementById('input-temp-c');
    const inF = document.getElementById('input-temp-f');
    const slider = document.getElementById('temp-slider');
    const tempMentalSteps = document.getElementById('temp-mental-steps');

    function updateFromC(c, source) {{
        const pt = c * 0.9;
        const f = c * 1.8 + 32;

        if (source !== 'pt') inPt.value = (Math.round(pt * 10) / 10).toFixed(1).replace('.0', '');
        if (source !== 'c') inC.value = (Math.round(c * 10) / 10).toFixed(1).replace('.0', '');
        if (source !== 'f') inF.value = (Math.round(f * 10) / 10).toFixed(1).replace('.0', '');
        if (source !== 'slider') slider.value = pt;

        // Mental math explanation
        const ptRound = Math.round(pt);
        const fRound = Math.round(f);
        const cRound = Math.round(c);
        
        const isSgn = "{ '1' if is_sgn else '0' }" === "1";
        if (isSgn) {{
            tempMentalSteps.innerHTML = `• <strong>Эк Фаренхаит (${{fRound}}°F)</strong>: Дропо 32 (${{fRound - 32}}), дивидо виа 2 → <strong>${{ptRound}}°Пт</strong>.<br>• <strong>Эк Целсиус (${{cRound}}°C)</strong>: Субтракто 10% (-${{(cRound * 0.1).toFixed(1)}}) → <strong>${{ptRound}}°Пт</strong>.`;
        }} else {{
            tempMentalSteps.innerHTML = `• <strong>From Fahrenheit (${{fRound}}°F)</strong>: Drop 32 (${{fRound - 32}}), then cut in half → <strong>${{ptRound}}°Пт</strong>.<br>• <strong>From Celsius (${{cRound}}°C)</strong>: Subtract 10% (-${{(cRound * 0.1).toFixed(1)}}) → <strong>${{ptRound}}°Пт</strong>.`;
        }}
    }}

    inPt.addEventListener('input', () => {{
        const pt = parseFloat(inPt.value);
        if (!isNaN(pt)) updateFromC(pt / 0.9, 'pt');
    }});

    inC.addEventListener('input', () => {{
        const c = parseFloat(inC.value);
        if (!isNaN(c)) updateFromC(c, 'c');
    }});

    inF.addEventListener('input', () => {{
        const f = parseFloat(inF.value);
        if (!isNaN(f)) updateFromC((f - 32) / 1.8, 'f');
    }});

    slider.addEventListener('input', () => {{
        const pt = parseFloat(slider.value);
        if (!isNaN(pt)) updateFromC(pt / 0.9, 'slider');
    }});

    // Initialize with 27°Пт
    updateFromC(30, 'init');

    // --- 2. DISTANCE CONVERTER ENGINE ---
    const distVal = document.getElementById('dist-input-val');
    const distUnit = document.getElementById('dist-input-unit');
    const distGrid = document.getElementById('dist-results-grid');
    const distMentalTip = document.getElementById('dist-mental-tip');

    // Conversion factor to Monomers (Мн)
    const toMonomer = {{
        'mn': 1.0,
        'decimn': 0.4,
        'dmn': 10.0,
        'trideka': 30.0,
        'kvadrodeka': 40.0,
        'kmn': 60000.0,
        'cm': 0.4,        // 1 cm = 0.4 Мн (since 1 Мн = 2.5 cm)
        'm': 40.0,        // 1 m = 100 cm = 40 Мн
        'km': 40000.0,    // 1 km = 1000 m = 40,000 Мн
        'in': 1.016,      // 1 in = 2.54 cm = 1.016 Мн
        'ft': 12.192,     // 1 ft = 30.48 cm = 12.192 Мн
        'yd': 36.576,     // 1 yd = 91.44 cm = 36.576 Мн
        'mi': 64373.76    // 1 mi = 1.609344 km = 64,373.76 Мн
    }};

    function updateDistance() {{
        const val = parseFloat(distVal.value) || 0;
        const unit = distUnit.value;
        const totalMn = val * (toMonomer[unit] || 1.0);

        // Derive all units
        const decimn = totalMn / 0.4;
        const mn = totalMn;
        const dmn = totalMn / 10.0;
        const trideka = totalMn / 30.0;
        const kvadrodeka = totalMn / 40.0;
        const kmn = totalMn / 60000.0;
        
        const cm = totalMn * 2.5;
        const m = cm / 100.0;
        const km = m / 1000.0;
        const inches = cm / 2.54;
        const feet = inches / 12.0;
        const yards = feet / 3.0;
        const miles = feet / 5280.0;

        const isSgn = "{ '1' if is_sgn else '0' }" === "1";

        function fmt(n) {{
            if (n === 0) return '0';
            if (Math.abs(n) >= 1000) return n.toLocaleString('en-US', {{ maximumFractionDigits: 2 }});
            if (Math.abs(n) >= 1) return (Math.round(n * 1000) / 1000).toString();
            return (Math.round(n * 10000) / 10000).toString();
        }}

        distGrid.innerHTML = `
            <div style="background:#ffffff; border:1px solid #bae6fd; border-radius:6px; padding:12px; display:flex; flex-direction:column;">
                <span style="font-size:0.75rem; color:#0369a1; font-weight:bold;">МОНОМЕР (Мн)</span>
                <span style="font-size:1.35rem; font-weight:800; color:#0c4a6e;">${{fmt(mn)}} Мн</span>
                <span style="font-size:0.72rem; color:#64748b;">👍 Thumb knuckle (~1 in)</span>
            </div>
            <div style="background:#ffffff; border:1px solid #bae6fd; border-radius:6px; padding:12px; display:flex; flex-direction:column;">
                <span style="font-size:0.75rem; color:#0369a1; font-weight:bold;">ДЕКАМЕР (Дмн)</span>
                <span style="font-size:1.35rem; font-weight:800; color:#0c4a6e;">${{fmt(dmn)}} Дмн</span>
                <span style="font-size:0.72rem; color:#64748b;">🦶 Human foot (~1 ft)</span>
            </div>
            <div style="background:#ffffff; border:1px solid #bae6fd; border-radius:6px; padding:12px; display:flex; flex-direction:column;">
                <span style="font-size:0.75rem; color:#0369a1; font-weight:bold;">ТРИДЕКА (3Дмн)</span>
                <span style="font-size:1.35rem; font-weight:800; color:#0c4a6e;">${{fmt(trideka)}} 3Дмн</span>
                <span style="font-size:0.72rem; color:#64748b;">🚶 Stride (~1 yard)</span>
            </div>
            <div style="background:#ffffff; border:1px solid #bae6fd; border-radius:6px; padding:12px; display:flex; flex-direction:column;">
                <span style="font-size:0.75rem; color:#0369a1; font-weight:bold;">КВАДРОДЕКА (4Дмн)</span>
                <span style="font-size:1.35rem; font-weight:800; color:#0c4a6e;">${{fmt(kvadrodeka)}} 4Дмн</span>
                <span style="font-size:0.72rem; color:#64748b;">🎸 Exactly 1.0 Meter</span>
            </div>
            <div style="background:#ffffff; border:1px solid #bae6fd; border-radius:6px; padding:12px; display:flex; flex-direction:column;">
                <span style="font-size:0.75rem; color:#0369a1; font-weight:bold;">КИЛОМЕР (Кмн)</span>
                <span style="font-size:1.35rem; font-weight:800; color:#0c4a6e;">${{fmt(kmn)}} Кмн</span>
                <span style="font-size:0.72rem; color:#64748b;">🚶 15-min walk (~1 mi)</span>
            </div>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px; padding:12px; display:flex; flex-direction:column;">
                <span style="font-size:0.75rem; color:#475569; font-weight:bold;">METRIC EQUIVALENT</span>
                <span style="font-size:1.15rem; font-weight:bold; color:#1e293b;">${{fmt(cm)}} cm / ${{fmt(m)}} m</span>
                <span style="font-size:0.72rem; color:#64748b;">${{fmt(km)}} km</span>
            </div>
            <div style="background:#f8fafc; border:1px solid #cbd5e1; border-radius:6px; padding:12px; display:flex; flex-direction:column;">
                <span style="font-size:0.75rem; color:#475569; font-weight:bold;">IMPERIAL EQUIVALENT</span>
                <span style="font-size:1.15rem; font-weight:bold; color:#1e293b;">${{fmt(feet)}} ft / ${{fmt(inches)}} in</span>
                <span style="font-size:0.72rem; color:#64748b;">${{fmt(miles)}} miles</span>
            </div>
        `;

        if (isSgn) {{
            distMentalTip.innerHTML = `• <strong>Мономер ад Сантимэтра</strong>: Мултиплико виа 2.5 (${{fmt(mn)}} Мн × 2.5 = <strong>${{fmt(cm)}} cm</strong>).<br>• <strong>Киломер ад Майл</strong>: Дропо 3 нули инкаи дивидо виа 6 (${{fmt(kmn * 60000)}} Мн → ${{fmt(kmn * 60)}} ÷ 6 = <strong>${{fmt(kmn * 10)}} mi</strong>).`;
        }} else {{
            distMentalTip.innerHTML = `• <strong>Monomers to Centimeters</strong>: Multiply by 2.5 (${{fmt(mn)}} Мн × 2.5 = <strong>${{fmt(cm)}} cm</strong>).<br>• <strong>Kilomers to Miles</strong>: Drop last three zeros and divide by 6 (e.g. 60,000 Мн → 60 ÷ 6 = <strong>1.0 mile</strong>).`;
        }}
    }}

    distVal.addEventListener('input', updateDistance);
    distUnit.addEventListener('change', updateDistance);
    updateDistance();
}});
</script>

</body>
</html>
"""

def build_all():
    # 1. Write units.html in root
    en_html = get_units_page_html(lang="en")
    with open(os.path.join(BASE_DIR, "units.html"), "w", encoding="utf-8") as f:
        f.write(en_html)
    print("Wrote: units.html")

    # 2. Write sgn/units.html in root
    sgn_html = get_units_page_html(lang="sgn")
    os.makedirs(os.path.join(BASE_DIR, "sgn"), exist_ok=True)
    with open(os.path.join(BASE_DIR, "sgn", "units.html"), "w", encoding="utf-8") as f:
        f.write(sgn_html)
    print("Wrote: sgn/units.html")

if __name__ == "__main__":
    build_all()

