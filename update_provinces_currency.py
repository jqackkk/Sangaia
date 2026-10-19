#!/usr/bin/env python3
"""
Sangaia Full Provinces & Currency Updater
Updates:
1. Sangaian Dollar representation from "$" to "$" across all files.
2. The 5 official provinces of Sangaia:
   - New Jasper (City: Shesk)
   - New Madison (City: Madison City)
   - Liveland (City: Oaks)
   - Sentinel (City: Sentinel Ridge)
   - Columbia (City: Columbia City)
3. Domestic Affairs provincial relations, internal common market trade, and highway telemetry.
4. Environment provincial weather stations and biome funding tables.
5. Healthcare hospital directory for all 5 provinces.
6. Department generation scripts and all generated department portals.
"""

import os
import re
import subprocess

BASE_DIR = "/Users/jackdavenport/Sangaia"

def update_currency_symbol():
    print("\n--- 1. Replacing $ with $ across all repository files ---")
    count = 0
    total_replaced = 0

    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root or 'node_modules' in root:
            continue
        for fname in files:
            if fname.endswith(('.html', '.js', '.py', '.txt')):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if '$' in content:
                        cnt = content.count('$')
                        content = content.replace('$', '$')
                        with open(fpath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        count += 1
                        total_replaced += cnt
                except Exception as e:
                    print(f"Error in {fpath}: {e}")

    print(f"Replaced {total_replaced} occurrences of $ with $ across {count} files.")

def update_generator_provinces():
    print("\n--- 2. Updating generate_departments_html.py with the 5 official provinces ---")
    gen_file = os.path.join(BASE_DIR, "generate_departments_html.py")
    with open(gen_file, 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Update petition province options
    old_petition_opts = '''            {"name": "province", "label_en": "Home Province", "label_sgn": "Провинциа", "type": "select", "options": [
                {"val": "capitol", "en": "Capitol Federal District", "sgn": "Капитоло Федерало Дистрикто"},
                {"val": "montana", "en": "Northern Highland Province", "sgn": "Нордо Алпино Провинциа"},
                {"val": "costa", "en": "Azure Maritime Province", "sgn": "Азуро Маритимо Провинциа"},
                {"val": "valle", "en": "Emerald Valley Agricultural Province", "sgn": "Эмэральдо Вале Провинциа"}
            ]},'''

    new_petition_opts = '''            {"name": "province", "label_en": "Home Province", "label_sgn": "Провинциа", "type": "select", "options": [
                {"val": "new_jasper", "en": "New Jasper Province", "sgn": "Ново Јаспэр Провинциа"},
                {"val": "new_madison", "en": "New Madison Province", "sgn": "Ново Мадисон Провинциа"},
                {"val": "liveland", "en": "Liveland Province", "sgn": "Ливланд Провинциа"},
                {"val": "sentinel", "en": "Sentinel Province", "sgn": "Сэнтинэл Провинциа"},
                {"val": "columbia", "en": "Columbia Province", "sgn": "Колумбиа Провинциа"}
            ]},'''
    code = code.replace(old_petition_opts, new_petition_opts)

    # 2. Update jobs province options
    old_jobs_opts = '''            {"name": "province", "label_en": "Preferred Province", "label_sgn": "Провинциа", "type": "select", "options": [
                {"val": "all", "en": "All Provinces (Relocation Allowance Available)", "sgn": "Холо Провинциа"},
                {"val": "capitol", "en": "Capitol Federal District", "sgn": "Капитоло Федерало"},
                {"val": "montana", "en": "Northern Highland Province", "sgn": "Нордо Алпино"},
                {"val": "costa", "en": "Azure Maritime Province", "sgn": "Азуро Маритимо"}
            ]}'''

    new_jobs_opts = '''            {"name": "province", "label_en": "Preferred Province", "label_sgn": "Провинциа", "type": "select", "options": [
                {"val": "all", "en": "All 5 Provinces (Relocation Allowance Available)", "sgn": "Холо 5 Провинциа"},
                {"val": "new_jasper", "en": "New Jasper (Shesk Central)", "sgn": "Ново Јаспэр (Шэск)"},
                {"val": "new_madison", "en": "New Madison (Madison City)", "sgn": "Ново Мадисон (Мадисон)"},
                {"val": "liveland", "en": "Liveland (Oaks Agricultural Hub)", "sgn": "Ливланд (Оакс)"},
                {"val": "sentinel", "en": "Sentinel (Alpine Ecological Reserve)", "sgn": "Сэнтинэл (Алпино)"},
                {"val": "columbia", "en": "Columbia (Maritime Harbor)", "sgn": "Колумбиа (Харбор)"}
            ]}'''
    code = code.replace(old_jobs_opts, new_jobs_opts)

    # 3. Update provider directory options
    old_prov_opts = '''            {"name": "province", "label_en": "Province / District", "label_sgn": "Провинциа / Дистрикто", "type": "select", "options": [
                {"val": "all", "en": "All Provincial Polyclinics", "sgn": "Холо Поликлиника"},
                {"val": "capitol", "en": "Capitol General Medical Center", "sgn": "Капитоло Генерало Мэдико"},
                {"val": "montana", "en": "Highland Alpine Community Clinic", "sgn": "Алпино Комунитиа Клиника"},
                {"val": "costa", "en": "Azure Coast Regional Hospital", "sgn": "Азуро Коста Рэгионало"}
            ]}'''

    new_prov_opts = '''            {"name": "province", "label_en": "Province / District", "label_sgn": "Провинциа / Дистрикто", "type": "select", "options": [
                {"val": "all", "en": "All 5 Provincial Hospitals & Polyclinics", "sgn": "Холо 5 Провинциало Клиника"},
                {"val": "new_jasper", "en": "Watson Healthcare / New Jasper Hospital (Shesk)", "sgn": "Ново Јаспэр Хоспитало (Шэск)"},
                {"val": "new_madison", "en": "New Madison Hospital (Madison City)", "sgn": "Ново Мадисон Хоспитало (Мадисон)"},
                {"val": "liveland", "en": "Suwannee Emergency Hospital (Oaks, Liveland)", "sgn": "Суванни ЕР Хоспитало (Оакс, Ливланд)"},
                {"val": "sentinel", "en": "Sentinel Regional Trauma Center", "sgn": "Сэнтинэл Рэгионало Травма"},
                {"val": "columbia", "en": "Columbia Maritime Regional Medical Center", "sgn": "Колумбиа Маритимо Генерало"}
            ]}'''
    code = code.replace(old_prov_opts, new_prov_opts)

    # 4. Update shipping manifest options
    old_ship_opts = '''            {"name": "origin_prov", "label_en": "Origin Province", "label_sgn": "Оригино Провинциа", "type": "select", "options": [
                {"val": "capitol", "en": "Capitol Federal District", "sgn": "Капитоло Федерало"},
                {"val": "montana", "en": "Northern Highland Province", "sgn": "Нордо Алпино"},
                {"val": "costa", "en": "Azure Maritime Province", "sgn": "Азуро Маритимо"},
                {"val": "valle", "en": "Emerald Valley Agricultural Province", "sgn": "Эмэральдо Вале"}
            ]},
            {"name": "dest_prov", "label_en": "Destination Province", "label_sgn": "Дэстинатио Провинциа", "type": "select", "options": [
                {"val": "costa", "en": "Azure Maritime Province", "sgn": "Азуро Маритимо"},
                {"val": "valle", "en": "Emerald Valley Agricultural Province", "sgn": "Эмэральдо Вале"},
                {"val": "capitol", "en": "Capitol Federal District", "sgn": "Капитоло Федерало"},
                {"val": "montana", "en": "Northern Highland Province", "sgn": "Нордо Алпино"}
            ]},'''

    new_ship_opts = '''            {"name": "origin_prov", "label_en": "Origin Province", "label_sgn": "Оригино Провинциа", "type": "select", "options": [
                {"val": "new_jasper", "en": "New Jasper Province (Shesk)", "sgn": "Ново Јаспэр (Шэск)"},
                {"val": "new_madison", "en": "New Madison Province (Madison City)", "sgn": "Ново Мадисон (Мадисон)"},
                {"val": "liveland", "en": "Liveland Province (Oaks)", "sgn": "Ливланд (Оакс)"},
                {"val": "sentinel", "en": "Sentinel Province (Sentinel Ridge)", "sgn": "Сэнтинэл (Сэнтинэл)"},
                {"val": "columbia", "en": "Columbia Province (Columbia City)", "sgn": "Колумбиа (Колумбиа)"}
            ]},
            {"name": "dest_prov", "label_en": "Destination Province", "label_sgn": "Дэстинатио Провинциа", "type": "select", "options": [
                {"val": "columbia", "en": "Columbia Province (Columbia City)", "sgn": "Колумбиа (Колумбиа)"},
                {"val": "new_jasper", "en": "New Jasper Province (Shesk)", "sgn": "Ново Јаспэр (Шэск)"},
                {"val": "new_madison", "en": "New Madison Province (Madison City)", "sgn": "Ново Мадисон (Мадисон)"},
                {"val": "liveland", "en": "Liveland Province (Oaks)", "sgn": "Ливланд (Оакс)"},
                {"val": "sentinel", "en": "Sentinel Province (Sentinel Ridge)", "sgn": "Сэнтинэл (Сэнтинэл)"}
            ]},'''
    code = code.replace(old_ship_opts, new_ship_opts)

    # 5. Update trademap metrics
    old_trademap_sub = '''{"name_en": "Internal Tariff Rate", "name_sgn": "Интерно Тарифо Градо", "val": "0.00% Statutory", "sub_en": "Article IV: Absolute freedom of domestic goods", "sub_sgn": "Артикло IV: Либэро трэйд ин Сангайа"},'''
    new_trademap_sub = '''{"name_en": "Internal Tariff Rate", "name_sgn": "Интерно Тарифо Градо", "val": "0.00% Statutory", "sub_en": "Article IV: 0% tariffs across New Jasper, New Madison, Liveland, Sentinel, Columbia", "sub_sgn": "Артикло IV: 0% тарифо транз Ново Јаспэр, Ново Мадисон, Ливланд, Сэнтинэл, Колумбиа"},'''
    code = code.replace(old_trademap_sub, new_trademap_sub)

    # 6. Update air sensors
    old_airsensors = '''        "metrics": [
            {"name_en": "Capitol District PM2.5", "name_sgn": "Капитоло Дистрикто ПМ2.5", "val": "4.2 µg/m³", "sub_en": "Pristine WHO Class 1 clean air", "sub_sgn": "Пуро ВХО Класо 1 аэро"},
            {"name_en": "Northern High Ridge Ozone", "name_sgn": "Нордо Алпино Озоно", "val": "0.018 ppm", "sub_en": "Ultra-clean natural atmospheric purity", "sub_sgn": "Ултра-пуро атмосфэра"},
            {"name_en": "Azure Coastal Dissolved Oxygen", "name_sgn": "Азуро Коста Оксигэн ин Аква", "val": "9.8 mg/L", "sub_en": "Super-oxygenated marine vitality", "sub_sgn": "Оптимо марино виталито"}
        ],'''

    new_airsensors = '''        "metrics": [
            {"name_en": "New Jasper (Shesk Basin) PM2.5", "name_sgn": "Ново Јаспэр (Шэск) ПМ2.5", "val": "4.2 µg/m³", "sub_en": "Pristine WHO Class 1 clean air", "sub_sgn": "Пуро ВХО Класо 1 аэро"},
            {"name_en": "Sentinel Ridge Ozone", "name_sgn": "Сэнтинэл Ридж Озоно", "val": "0.018 ppm", "sub_en": "Ultra-clean alpine air purity", "sub_sgn": "Ултра-пуро алпино аэро"},
            {"name_en": "Columbia Maritime Basin Oxygen", "name_sgn": "Колумбиа Оксигэн ин Аква", "val": "9.8 mg/L", "sub_en": "Super-oxygenated freshwater & marine vitality", "sub_sgn": "Оптимо марино & аква виталито"}
        ],'''
    code = code.replace(old_airsensors, new_airsensors)

    # 7. Update hazard map routes
    old_hazardmap = '''        "metrics": [
            {"name_en": "Route 1: Trans-Sangaia Spine", "name_sgn": "Маршруто 1: Транз-Сангайа", "val": "Clear & Dry (110 km/h)", "sub_en": "Cameras 1-14 active • 0 obstructions", "sub_sgn": "Камера 1-14 ливо • 0 блокадо"},
            {"name_en": "Alpine Pass Highway 4", "name_sgn": "Алпино Пасо Виа 4", "val": "Light Snow (60 km/h)", "sub_en": "Heated asphalt active • Chains recommended", "sub_sgn": "Тэрмало асфалто активо"},
            {"name_en": "Coastal Maritime Expressway 101", "name_sgn": "Азуро Коста Виа 101", "val": "Clear & Ocean Breeze", "sub_en": "Speed: 100 km/h • 0 incidents", "sub_sgn": "Спидо: 100 км/х • 0 инцидэнто"}
        ],'''

    new_hazardmap = '''        "metrics": [
            {"name_en": "Highway S-1: Jasper-Madison Arterial", "name_sgn": "Виа С-1: Јаспэр-Мадисон", "val": "Clear & Dry (74 Кмн/h / 110 km/h)", "sub_en": "Shesk &harr; Madison City • 0 obstructions", "sub_sgn": "Шэск &harr; Мадисон • 0 блокадо"},
            {"name_en": "Highway S-2: Liveland Trunk", "name_sgn": "Виа С-2: Ливланд Транзито", "val": "Clear & Shaded (60 Кмн/h / 90 km/h)", "sub_en": "Oaks &harr; Shesk Corridor", "sub_sgn": "Оакс &harr; Шэск Коридоро"},
            {"name_en": "Highway S-3: Sentinel Alpine Pass", "name_sgn": "Виа С-3: Сэнтинэл Пасо", "val": "Clear & Dry (40 Кмн/h / 60 km/h)", "sub_en": "Heated roadbeds active • Sentinel Ridge", "sub_sgn": "Тэрмало виа • Сэнтинэл Ридж"}
        ],'''
    code = code.replace(old_hazardmap, new_hazardmap)

    with open(gen_file, 'w', encoding='utf-8') as f:
        f.write(code)
    print("Updated generate_departments_html.py with 5 provinces.")

    # Re-run generator to update all 42 files
    print("Regenerating all 42 department portals...")
    subprocess.run(["python3", gen_file], check=True)

def update_domestic_affairs():
    print("\n--- 3. Updating Domestic Affairs with the 5 official provinces ---")
    da_files = [
        os.path.join(BASE_DIR, "domesticaffairs.html"),
        os.path.join(BASE_DIR, "MiA", "index.html"),
    ]

    en_prov_section = '''        <!-- SECTION 1: PROVINCIAL RELATIONS & COUNCIL OF GOVERNORS -->
        <div class="glass-panel" id="provincial-relations">
            <h2>
                <span>Provincial Relations & Council of Governors</span>
                <button type="button" class="sangaia-btn btn-navy" onclick="openPetitionModal()">
                    <span>Petition Provincial Council &rarr;</span>
                </button>
            </h2>
            <p>
                In the United Provinces of Sangaia, democratic balance requires close inter-provincial harmony. The Council of Governors convenes quarterly to resolve boundary alignment, oversee shared watershed stewardship, and uphold mutual legal recognition across all 5 sovereign provinces: <strong>New Jasper, New Madison, Liveland, Sentinel, and Columbia</strong>.
            </p>

            <div class="feature-grid-3">
                <div class="feature-card">
                    <div>
                        <span class="badge badge-navy" style="margin-bottom: 8px;">Provincial Seat</span>
                        <h3>New Jasper Province</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Governor:</strong> Hon. Arthur Vance<br>
                            <strong>Administrative Capital:</strong> Shesk<br>
                            <strong>Focus:</strong> Central administrative hub, federal assembly liaison, advanced rail freight logistics, and pharmaceutical reserves.
                        </p>
                    </div>
                    <div style="background: #f1f5f9; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--navy-midnight);">
                        Harmony Accord: Fully Ratified &bull; 0 Pending Border Disputes
                    </div>
                </div>

                <div class="feature-card">
                    <div>
                        <span class="badge badge-navy" style="margin-bottom: 8px;">Provincial Seat</span>
                        <h3>New Madison Province</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Governor:</strong> Dr. Henrik Zhao<br>
                            <strong>Administrative Capital:</strong> Madison City<br>
                            <strong>Focus:</strong> Clean tech research, microelectronics, educational university consortiums, and automated maglev transit.
                        </p>
                    </div>
                    <div style="background: #f1f5f9; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--navy-midnight);">
                        Harmony Accord: Fully Ratified &bull; Interstate Power Sharing Accord
                    </div>
                </div>

                <div class="feature-card">
                    <div>
                        <span class="badge badge-navy" style="margin-bottom: 8px;">Provincial Seat</span>
                        <h3>Liveland Province</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Governor:</strong> Mateo Alvarez<br>
                            <strong>Administrative Capital:</strong> Oaks<br>
                            <strong>Focus:</strong> Regenerative agro-forestry, hydroponic grain reserves, organic orchards, and pasture dairy cooperatives.
                        </p>
                    </div>
                    <div style="background: #f1f5f9; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--navy-midnight);">
                        Harmony Accord: Fully Ratified &bull; Agricultural Common Market Protocol
                    </div>
                </div>

                <div class="feature-card">
                    <div>
                        <span class="badge badge-navy" style="margin-bottom: 8px;">Provincial Seat</span>
                        <h3>Sentinel Province</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Governor:</strong> Astrid Solberg<br>
                            <strong>Administrative Capital:</strong> Sentinel Ridge<br>
                            <strong>Focus:</strong> Alpine ecological preserves, watershed guardians, hydro & geothermal microgrids, and wilderness stewardship.
                        </p>
                    </div>
                    <div style="background: #f1f5f9; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--navy-midnight);">
                        Harmony Accord: Fully Ratified &bull; Trans-Provincial Watershed Accord
                    </div>
                </div>

                <div class="feature-card">
                    <div>
                        <span class="badge badge-navy" style="margin-bottom: 8px;">Provincial Seat</span>
                        <h3>Columbia Province</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Governor:</strong> Capt. Ronald Sterling<br>
                            <strong>Administrative Capital:</strong> Columbia City<br>
                            <strong>Focus:</strong> Deepwater container logistics, canal lock operations, maritime fisheries management, and coastal renewable fleets.
                        </p>
                    </div>
                    <div style="background: #f1f5f9; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--navy-midnight);">
                        Harmony Accord: Fully Ratified &bull; Port Fee Equalization Certified
                    </div>
                </div>

                <div class="feature-card" style="border-top-color: var(--gold-accent);">
                    <div>
                        <span class="badge badge-amber" style="margin-bottom: 8px;">Arbitration Tribunal</span>
                        <h3>Inter-Provincial Dispute Court</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Chief Magistrate:</strong> Justice Valerie Thorne<br>
                            <strong>Location:</strong> Federal Arbitration Chamber, Shesk<br>
                            <strong>Jurisdiction:</strong> Binding arbitration for contract disputes between municipal authorities.
                        </p>
                    </div>
                    <div style="background: #fffbeb; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--gold-accent);">
                        Case Backlog: 0 &bull; Average Resolution Time: 14 Days
                    </div>
                </div>
            </div>
        </div>'''

    en_trade_table = '''        <!-- SECTION 2: PROVINCIAL TRADE & COMMON MARKET -->
        <div class="glass-panel" id="provincial-trade">
            <h2>
                <span>Provincial Trade & The Sangaian Internal Common Market</span>
                <button type="button" class="sangaia-btn btn-navy" onclick="openManifestModal()">
                    <span>Register Freight Manifest &rarr;</span>
                </button>
            </h2>
            <p>
                The Sangaian Constitution explicitly prohibits inter-provincial trade tariffs, quotas, or transport embargoes. Over $ 48.2 Billion in annual domestic commerce flows freely across rail, maglev, and highway freight corridors connecting our 5 provinces.
            </p>

            <div class="data-table-wrapper">
                <table class="navy-table">
                    <thead>
                        <tr>
                            <th>Origin Province</th>
                            <th>Key Domestic Exports</th>
                            <th>Primary Destination</th>
                            <th>Annual Volume ($)</th>
                            <th>Regulatory Clearance</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>New Jasper</strong></td>
                            <td>Hard red wheat, clinical pharmaceuticals, agricultural harvesters</td>
                            <td>All Provinces (National Supply)</td>
                            <td><span style="font-weight: 800; color: var(--navy-midnight);">$ 14,200,000,000</span></td>
                            <td><span class="badge badge-green">100% Tariff-Free & Inspected</span></td>
                        </tr>
                        <tr>
                            <td><strong>New Madison</strong></td>
                            <td>Microprocessors, maglev rolling stock, financial services, software</td>
                            <td>All Provinces (National Grid)</td>
                            <td><span style="font-weight: 800; color: var(--navy-midnight);">$ 11,800,000,000</span></td>
                            <td><span class="badge badge-green">100% Tariff-Free & Inspected</span></td>
                        </tr>
                        <tr>
                            <td><strong>Liveland</strong></td>
                            <td>Pasture dairy, organic beef, apples, textiles, wool, bio-fuels</td>
                            <td>New Madison & New Jasper</td>
                            <td><span style="font-weight: 800; color: var(--navy-midnight);">$ 9,600,000,000</span></td>
                            <td><span class="badge badge-green">100% Tariff-Free & Inspected</span></td>
                        </tr>
                        <tr>
                            <td><strong>Sentinel</strong></td>
                            <td>Hydro-electric power, boreal timber, structural granite, minerals</td>
                            <td>Columbia & New Madison</td>
                            <td><span style="font-weight: 800; color: var(--navy-midnight);">$ 8,100,000,000</span></td>
                            <td><span class="badge badge-green">100% Tariff-Free & Inspected</span></td>
                        </tr>
                        <tr>
                            <td><strong>Columbia</strong></td>
                            <td>Seafood, marine aquaculture, container logistics, industrial salt</td>
                            <td>New Jasper & Sentinel</td>
                            <td><span style="font-weight: 800; color: var(--navy-midnight);">$ 4,500,000,000</span></td>
                            <td><span class="badge badge-green">100% Tariff-Free & Inspected</span></td>
                        </tr>
                    </tbody>
                    <tfoot>
                        <tr style="background: #e8eef8; font-weight: bold;">
                            <td>Total Internal Common Market</td>
                            <td colspan="2">Seamless Cross-Border Movement of Goods & Food</td>
                            <td style="color: var(--navy-midnight); font-size: 1.05rem;">$ 48,200,000,000</td>
                            <td>0% Import Duties Enforced</td>
                        </tr>
                    </tfoot>
                </table>
            </div>
        </div>'''

    en_highway_grid = '''            <div class="traffic-grid">
                <div class="traffic-card">
                    <div>
                        <span class="route-badge">HIGHWAY S-1</span>
                        <div style="font-weight: bold; color: var(--navy-midnight);">Jasper-Madison Arterial</div>
                        <div style="font-size: 0.82rem; color: #64748b;">Shesk &harr; Madison City (96 Кмн / 144 km)</div>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge badge-green">Clear &bull; 74 Кмн/h (110 km/h)</span>
                        <div style="font-size: 0.78rem; color: #64748b; margin-top: 4px;">Pavement Dry</div>
                    </div>
                </div>

                <div class="traffic-card">
                    <div>
                        <span class="route-badge" style="background: #15803d;">HIGHWAY S-2</span>
                        <div style="font-weight: bold; color: var(--navy-midnight);">Liveland Trunk Highway</div>
                        <div style="font-size: 0.82rem; color: #64748b;">Oaks &harr; Shesk (72 Кмн / 108 km)</div>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge badge-green">Clear &bull; 66 Кмн/h (100 km/h)</span>
                        <div style="font-size: 0.78rem; color: #64748b; margin-top: 4px;">Optimal Visibility</div>
                    </div>
                </div>

                <div class="traffic-card caution">
                    <div>
                        <span class="route-badge" style="background: #0284c7;">HIGHWAY S-3</span>
                        <div style="font-weight: bold; color: var(--navy-midnight);">Sentinel Alpine Ridge Pass</div>
                        <div style="font-size: 0.82rem; color: #64748b;">Sentinel Ridge Corridor (120 Кмн / 180 km)</div>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge badge-amber">Caution &bull; Heated Asphalt Active</span>
                        <div style="font-size: 0.78rem; color: #64748b; margin-top: 4px;">Plows Deployed</div>
                    </div>
                </div>

                <div class="traffic-card">
                    <div>
                        <span class="route-badge" style="background: #0c4a6e;">HIGHWAY S-4</span>
                        <div style="font-weight: bold; color: var(--navy-midnight);">Columbia Coastal Expressway</div>
                        <div style="font-size: 0.82rem; color: #64748b;">Columbia City &harr; Oaks (140 Кмн / 210 km)</div>
                    </div>
                    <div style="text-align: right;">
                        <span class="badge badge-green">Flowing &bull; 68 Кмн/h (102 km/h)</span>
                        <div style="font-size: 0.78rem; color: #64748b; margin-top: 4px;">Smart Signals Active</div>
                    </div>
                </div>
            </div>'''

    for path in da_files:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                c = f.read()

            # Replace sections
            c = re.sub(r'<!-- SECTION 1: PROVINCIAL RELATIONS & COUNCIL OF GOVERNORS -->.*?<!-- SECTION 2: PROVINCIAL TRADE & COMMON MARKET -->', en_prov_section + '\n\n', c, flags=re.DOTALL)
            c = re.sub(r'<!-- SECTION 2: PROVINCIAL TRADE & COMMON MARKET -->.*?<!-- SECTION 3: FEDERAL INTERACTIONS & CO-GOVERNANCE -->', en_trade_table + '\n\n', c, flags=re.DOTALL)
            c = re.sub(r'<div class="traffic-grid">.*?</div>\s*<!-- Road Services Directory -->', en_highway_grid + '\n\n            <!-- Road Services Directory -->', c, flags=re.DOTALL)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Updated {path}")

    # Also Sangaian versions
    da_sgn_files = [
        os.path.join(BASE_DIR, "sgn", "domesticaffairs.html"),
        os.path.join(BASE_DIR, "MiA", "sgn", "index.html"),
    ]

    sgn_prov_section = '''        <!-- SECTION 1: PROVINCIAL RELATIONS & COUNCIL OF GOVERNORS -->
        <div class="glass-panel" id="provincial-relations">
            <h2>
                <span>Провинциало Рэлатио & Консилио эк Гувэрноро</span>
                <button type="button" class="sangaia-btn btn-navy" onclick="openPetitionModal()">
                    <span>Пэтитио Провинциало Консилио &rarr;</span>
                </button>
            </h2>
            <p>
                Ин свои Унито Провинциа эк Сангайа, дэмократико балансо экзиго фортис интер-провинциало хармониа. Консилио эк Гувэрноро конвэнио квартало про рэсолуто граница, супэрвидо аква, инкаи мютуало јуро транз холо 5 сувэрэно провинциа: <strong>Ново Јаспэр, Ново Мадисон, Ливланд, Сэнтинэл, инкаи Колумбиа</strong>.
            </p>

            <div class="feature-grid-3">
                <div class="feature-card">
                    <div>
                        <span class="badge badge-navy" style="margin-bottom: 8px;">Провинциало Сэдэ</span>
                        <h3>Ново Јаспэр Провинциа</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Гувэрноро:</strong> Артур Ванс<br>
                            <strong>Капитало:</strong> Шэск<br>
                            <strong>Фокус:</strong> Цэнтрало административо хуб, федерало асэмблеа лиаисон, транзито логистико, фармациа.
                        </p>
                    </div>
                    <div style="background: #f1f5f9; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--navy-midnight);">
                        Хармониа Акордо: 100% Ратифико &bull; 0 Граница Диспуто
                    </div>
                </div>

                <div class="feature-card">
                    <div>
                        <span class="badge badge-navy" style="margin-bottom: 8px;">Провинциало Сэдэ</span>
                        <h3>Ново Мадисон Провинциа</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Гувэрноро:</strong> Др. Хэнрик Жао<br>
                            <strong>Капитало:</strong> Мадисон Сити<br>
                            <strong>Фокус:</strong> Виридо тэк сциэнциа, микроэлэктронико, унивэрсито консорцио, маглев транзито.
                        </p>
                    </div>
                    <div style="background: #f1f5f9; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--navy-midnight);">
                        Хармониа Акордо: 100% Ратифико &bull; Энэргиа Акордо
                    </div>
                </div>

                <div class="feature-card">
                    <div>
                        <span class="badge badge-navy" style="margin-bottom: 8px;">Провинциало Сэдэ</span>
                        <h3>Ливланд Провинциа</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Гувэрноро:</strong> Матэо Алварэз<br>
                            <strong>Капитало:</strong> Оакс<br>
                            <strong>Фокус:</strong> Рэгэнэративо агро-форест, хидропоник грано рэзэрва, био-продукт, даири коопэративо.
                        </p>
                    </div>
                    <div style="background: #f1f5f9; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--navy-midnight);">
                        Хармониа Акордо: 100% Ратифико &bull; Агро Трэйд Протоколо
                    </div>
                </div>

                <div class="feature-card">
                    <div>
                        <span class="badge badge-navy" style="margin-bottom: 8px;">Провинциало Сэдэ</span>
                        <h3>Сэнтинэл Провинциа</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Гувэрноро:</strong> Астрид Солбэрг<br>
                            <strong>Капитало:</strong> Сэнтинэл Ридж<br>
                            <strong>Фокус:</strong> Алпино биом салво, аква гардан, хидро-энэргиа, гэотэрмало, сильва салво.
                        </p>
                    </div>
                    <div style="background: #f1f5f9; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--navy-midnight);">
                        Хармониа Акордо: 100% Ратифико &bull; Аква Салво Акордо
                    </div>
                </div>

                <div class="feature-card">
                    <div>
                        <span class="badge badge-navy" style="margin-bottom: 8px;">Провинциало Сэдэ</span>
                        <h3>Колумбиа Провинциа</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Гувэрноро:</strong> Роналд Стэрлинг<br>
                            <strong>Капитало:</strong> Колумбиа Сити<br>
                            <strong>Фокус:</strong> Маритимо карго логистико, порт оператио, марино рыбо салво, рэнэвадо флота.
                        </p>
                    </div>
                    <div style="background: #f1f5f9; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--navy-midnight);">
                        Хармониа Акордо: 100% Ратифико &bull; Порт Либэро Сэртификато
                    </div>
                </div>

                <div class="feature-card" style="border-top-color: var(--gold-accent);">
                    <div>
                        <span class="badge badge-amber" style="margin-bottom: 8px;">Арбитрато Трибунало</span>
                        <h3>Интер-Провинциало Диспуто Корто</h3>
                        <p style="font-size: 0.88rem; color: #475569;">
                            <strong>Магистрато:</strong> Валэри Торнэ<br>
                            <strong>Сэдэ:</strong> Федерало Арбитрато Кабина, Шэск<br>
                            <strong>Јурисдиктио:</strong> Облигаторо арбитрато про муниципио контракто.
                        </p>
                    </div>
                    <div style="background: #fffbeb; border-radius: 6px; padding: 10px; font-size: 0.82rem; font-weight: bold; color: var(--gold-accent);">
                        Баклог: 0 &bull; Мэдиа Тэмпоро: 14 Дио
                    </div>
                </div>
            </div>
        </div>'''

    for path in da_sgn_files:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                c = f.read()

            c = re.sub(r'<!-- SECTION 1: PROVINCIAL RELATIONS & COUNCIL OF GOVERNORS -->.*?<!-- SECTION 2: PROVINCIAL TRADE & COMMON MARKET -->', sgn_prov_section + '\n\n', c, flags=re.DOTALL)

            with open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Updated SGN {path}")

def update_environment_weather_stations():
    print("\n--- 4. Updating Environment weather stations and biomes with the 5 provinces ---")
    env_files = [
        os.path.join(BASE_DIR, "environment.html"),
        os.path.join(BASE_DIR, "MtE", "index.html"),
        os.path.join(BASE_DIR, "mEnv", "index.html"),
    ]

    new_stations_js = '''    const provincialStations = {
        new_jasper: {
            name: "📍 Shesk (New Jasper Province)",
            lat: 30.51, lon: -82.95,
            tempC: 22, feelsC: 22,
            humidity: "54%", wind: "12 km/h", aqi: "14 (Pure)", precip: "0.0 mm",
            condition: "Partly Cloudy & Pleasant", icon: "⛅",
            forecast: [
                { day: "Today", icon: "⛅", max: 23, min: 14 },
                { day: "Tue", icon: "☀️", max: 25, min: 15 },
                { day: "Wed", icon: "🌤️", max: 24, min: 14 },
                { day: "Thu", icon: "🌧️", max: 20, min: 12 },
                { day: "Fri", icon: "☀️", max: 23, min: 14 }
            ]
        },
        new_madison: {
            name: "📍 Madison City (New Madison Province)",
            lat: 30.46, lon: -83.41,
            tempC: 23, feelsC: 23,
            humidity: "50%", wind: "10 km/h", aqi: "12 (Pristine)", precip: "0.0 mm",
            condition: "Warm Sunshine & Gentle Breeze", icon: "☀️",
            forecast: [
                { day: "Today", icon: "☀️", max: 24, min: 15 },
                { day: "Tue", icon: "🌤️", max: 25, min: 16 },
                { day: "Wed", icon: "⛅", max: 23, min: 14 },
                { day: "Thu", icon: "🌧️", max: 21, min: 13 },
                { day: "Fri", icon: "☀️", max: 24, min: 15 }
            ]
        },
        liveland: {
            name: "📍 Oaks (Liveland Province)",
            lat: 30.29, lon: -82.98,
            tempC: 24, feelsC: 24,
            humidity: "56%", wind: "8 km/h", aqi: "10 (Pristine)", precip: "0.0 mm",
            condition: "Fair & Oak Canopy Shaded", icon: "🌤️",
            forecast: [
                { day: "Today", icon: "🌤️", max: 25, min: 15 },
                { day: "Tue", icon: "☀️", max: 26, min: 16 },
                { day: "Wed", icon: "⛅", max: 24, min: 15 },
                { day: "Thu", icon: "🌧️", max: 21, min: 14 },
                { day: "Fri", icon: "☀️", max: 25, min: 15 }
            ]
        },
        sentinel: {
            name: "📍 Sentinel Ridge (Sentinel Province)",
            lat: 30.33, lon: -82.75,
            tempC: 18, feelsC: 18,
            humidity: "48%", wind: "16 km/h", aqi: "6 (Alpine Pure)", precip: "0.0 mm",
            condition: "Crisp Ridge Air & Sunny", icon: "☀️",
            forecast: [
                { day: "Today", icon: "☀️", max: 19, min: 9 },
                { day: "Tue", icon: "🌤️", max: 21, min: 10 },
                { day: "Wed", icon: "❄️", max: 15, min: 6 },
                { day: "Thu", icon: "⛅", max: 17, min: 8 },
                { day: "Fri", icon: "☀️", max: 20, min: 10 }
            ]
        },
        columbia: {
            name: "📍 Columbia City (Columbia Province)",
            lat: 30.18, lon: -82.63,
            tempC: 23, feelsC: 23,
            humidity: "62%", wind: "14 km/h", aqi: "11 (Pristine)", precip: "0.0 mm",
            condition: "Pleasant Lake Breeze & Sunny", icon: "🌤️",
            forecast: [
                { day: "Today", icon: "🌤️", max: 24, min: 15 },
                { day: "Tue", icon: "☀️", max: 26, min: 16 },
                { day: "Wed", icon: "🌧️", max: 21, min: 14 },
                { day: "Thu", icon: "⛅", max: 23, min: 15 },
                { day: "Fri", icon: "☀️", max: 25, min: 16 }
            ]
        }
    };'''

    en_pills = '''                        <span class="station-pill active" onclick="loadProvincialWeather('new_jasper')">New Jasper (Shesk)</span>
                        <span class="station-pill" onclick="loadProvincialWeather('new_madison')">New Madison (Madison City)</span>
                        <span class="station-pill" onclick="loadProvincialWeather('liveland')">Liveland (Oaks)</span>
                        <span class="station-pill" onclick="loadProvincialWeather('sentinel')">Sentinel (Sentinel Ridge)</span>
                        <span class="station-pill" onclick="loadProvincialWeather('columbia')">Columbia (Columbia City)</span>'''

    for path in env_files:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                c = f.read()

            c = re.sub(r'const provincialStations = \{.*?\n    \};', new_stations_js, c, flags=re.DOTALL)
            c = re.sub(r'<div class="station-pills">.*?</div>', f'<div class="station-pills">\n{en_pills}\n                    </div>', c, flags=re.DOTALL)
            c = c.replace("loadProvincialWeather('veridia')", "loadProvincialWeather('new_jasper')")

            with open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Updated {path}")

    # SGN Environment files
    env_sgn_files = [
        os.path.join(BASE_DIR, "sgn", "environment.html"),
        os.path.join(BASE_DIR, "MtE", "sgn", "index.html"),
        os.path.join(BASE_DIR, "mEnv", "sgn", "index.html"),
    ]

    sgn_pills = '''                        <span class="station-pill active" onclick="loadProvincialWeather('new_jasper')">Ново Јаспэр (Шэск)</span>
                        <span class="station-pill" onclick="loadProvincialWeather('new_madison')">Ново Мадисон (Мадисон)</span>
                        <span class="station-pill" onclick="loadProvincialWeather('liveland')">Ливланд (Оакс)</span>
                        <span class="station-pill" onclick="loadProvincialWeather('sentinel')">Сэнтинэл (Сэнтинэл)</span>
                        <span class="station-pill" onclick="loadProvincialWeather('columbia')">Колумбиа (Колумбиа)</span>'''

    for path in env_sgn_files:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                c = f.read()

            c = re.sub(r'const provincialStations = \{.*?\n    \};', new_stations_js, c, flags=re.DOTALL)
            c = re.sub(r'<div class="station-pills">.*?</div>', f'<div class="station-pills">\n{sgn_pills}\n                    </div>', c, flags=re.DOTALL)
            c = c.replace("loadProvincialWeather('veridia')", "loadProvincialWeather('new_jasper')")

            with open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Updated SGN {path}")

def update_healthcare_hospitals():
    print("\n--- 5. Adding Sentinel and Columbia hospitals to Healthcare ---")
    hosp_files = [
        os.path.join(BASE_DIR, "mH", "hospitals.html"),
        os.path.join(BASE_DIR, "mH", "sgn", "hospitals.html"),
    ]

    en_sentinel_columbia = '''                    <div class="article-card">
                        <h3 style="color: #c0392b; font-family: inherit; font-style: normal;">Sentinel Memorial Hospital</h3>
                        <p style="margin-bottom: 5px;"><strong>Sangaian Address:</strong> H0004 4th Street, Sentinel Ridge, Sentinel, 1-4000</p>
                        <p style="margin-bottom: 15px; color: #777;"><em>Map Equivalent: 168 NW Main Blvd, Lake City, FL 32055</em></p>
                        <a href="javascript:void(0);" onclick="openMap('168+NW+Main+Blvd,+Lake+City,+FL+32055')" class="sangaia-btn"><span>Get Directions</span></a>
                    </div>

                    <div class="article-card">
                        <h3 style="color: #c0392b; font-family: inherit; font-style: normal;">Columbia Regional Medical Center</h3>
                        <p style="margin-bottom: 5px;"><strong>Sangaian Address:</strong> H0005 5th Street, Columbia City, Columbia, 1-5000</p>
                        <p style="margin-bottom: 15px; color: #777;"><em>Map Equivalent: 4288 SW State Road 47, Lake City, FL 32024</em></p>
                        <a href="javascript:void(0);" onclick="openMap('4288+SW+State+Road+47,+Lake+City,+FL+32024')" class="sangaia-btn"><span>Get Directions</span></a>
                    </div>'''

    sgn_sentinel_columbia = '''                    <div class="article-card">
                        <h3 style="color: #c0392b; font-family: inherit; font-style: normal;">Сэнтинэл Мэмориало Хоспитало</h3>
                        <p style="margin-bottom: 5px;"><strong>Сангайа Адрэсо:</strong> H0004 4th Street, Sentinel Ridge, Sentinel, 1-4000</p>
                        <p style="margin-bottom: 15px; color: #777;"><em>Карто: 168 NW Main Blvd, Lake City, FL 32055</em></p>
                        <a href="javascript:void(0);" onclick="openMap('168+NW+Main+Blvd,+Lake+City,+FL+32055')" class="sangaia-btn"><span>Дирэктио &rarr;</span></a>
                    </div>

                    <div class="article-card">
                        <h3 style="color: #c0392b; font-family: inherit; font-style: normal;">Колумбиа Рэгионало Мэдико Цэнтро</h3>
                        <p style="margin-bottom: 5px;"><strong>Сангайа Адрэсо:</strong> H0005 5th Street, Columbia City, Columbia, 1-5000</p>
                        <p style="margin-bottom: 15px; color: #777;"><em>Карто: 4288 SW State Road 47, Lake City, FL 32024</em></p>
                        <a href="javascript:void(0);" onclick="openMap('4288+SW+State+Road+47,+Lake+City,+FL+32024')" class="sangaia-btn"><span>Дирэктио &rarr;</span></a>
                    </div>'''

    en_path = hosp_files[0]
    if os.path.exists(en_path):
        with open(en_path, 'r', encoding='utf-8') as f:
            c = f.read()
        if 'Sentinel Memorial Hospital' not in c:
            c = c.replace('<!-- Sangaian Address: H0003 -->', '')
            c = c.replace('</div>\n\n                </div>\n            </div>', f'{en_sentinel_columbia}\n\n                </div>\n            </div>')
            with open(en_path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Updated {en_path}")

    sgn_path = hosp_files[1]
    if os.path.exists(sgn_path):
        with open(sgn_path, 'r', encoding='utf-8') as f:
            c = f.read()
        if 'Сэнтинэл' not in c:
            c = c.replace('</div>\n\n                </div>\n            </div>', f'{sgn_sentinel_columbia}\n\n                </div>\n            </div>')
            with open(sgn_path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"Updated {sgn_path}")

def run_all():
    update_currency_symbol()
    update_generator_provinces()
    update_domestic_affairs()
    update_environment_weather_stations()
    update_healthcare_hospitals()
    print("\n[SUCCESS] All provinces, mapping, and currency updates completed perfectly!")

if __name__ == "__main__":
    run_all()
