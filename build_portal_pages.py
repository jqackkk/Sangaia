#!/usr/bin/env python3
"""
Sangaia Live Portal Pages Generator
Builds the core root pages in the One Live Wave 4 architecture:
- index.html
- services.html
- units.html
- citizenship.html
- government.html
- about.html
- societal_press.html
- dashboard.html
- application.html
- id.html & id/index.html
- literacy_test.html & literacy_exam_en.html
"""

import os
import shutil
from generate_all_sites import generate_page
from build_id_portal import build_id_pages

# -----------------------------------------------------------------------------
# 1. ROOT PORTAL HOME (index.html)
# -----------------------------------------------------------------------------
def build_index():
    title = "Sangaia Live Sovereign Portal"
    theme = "theme-federal"
    tab = "home"
    hero_title = "The United Provinces of Sangaia"
    hero_sub = "Official Sovereign Gateway &bull; The Aeretocracy &bull; One Live Wave 4 Infrastructure"

    sidebar_links = [
        {"label": "Sovereign Overview", "url": "#overview", "active": True},
        {"label": "Provincial Showcase", "url": "#showcase", "active": False},
        {"label": "The Aeretocracy", "url": "#aeretocracy", "active": False},
        {"label": "9 Federal Ministries", "url": "#ministries", "active": False},
        {"label": "5 Sovereign Provinces", "url": "#provinces", "active": False},
        {"label": "Government Structure", "url": "/government.html", "active": False},
        {"label": "Citizenship Application", "url": "/citizenship.html", "active": False}
    ]

    main_content = """
    <div class="ol-proclamation-card" id="overview">
        <div style="font-weight:600; color:var(--primary); margin-bottom:4px;">Federal Gateway Proclamation</div>
        <div>Welcome to Sangaia Live: The unified sovereign gateway for all public services, interprovincial coordination, and constitutional identity across the five united provinces.</div>
    </div>

    <!-- Official Republic Overview Card -->
    <div class="ol-card">
        <div class="ol-card-title">
            <span>Executive Federal Overview</span>
            <span class="ol-badge-tag ol-badge-success">Constitutional Republic</span>
        </div>
        <p>Sangaia is a sovereign constitutional republic operating under the Aeretocracy. Sangaia unites five autonomous provinces—<strong>New Jasper, New Madison, Liveland, Sentinel, and Columbia</strong>—providing universal public services, guaranteed living wages ($25.00/hr floor), zero foreign sovereign debt, and tuition-free education and healthcare.</p>
        <div class="ol-grid-3" style="margin-top:12px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:10px; text-align:center;">
                <div style="font-size:11px; color:#605e5c; text-transform:uppercase; font-weight:600;">Sovereign Currency</div>
                <div style="font-size:18px; font-weight:700; color:#0078d4; margin:4px 0;">$ (Dollar)</div>
                <div style="font-size:11px; color:#8a8886;">Zero Foreign Debt</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:10px; text-align:center;">
                <div style="font-size:11px; color:#605e5c; text-transform:uppercase; font-weight:600;">Temperature Standard</div>
                <div style="font-size:18px; font-weight:700; color:#0078d4; margin:4px 0;">Панотерм (°Пт)</div>
                <div style="font-size:11px; color:#8a8886;">°Пт = 0.5 &times; (°F - 32)</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:10px; text-align:center;">
                <div style="font-size:11px; color:#605e5c; text-transform:uppercase; font-weight:600;">Distance Standard</div>
                <div style="font-size:18px; font-weight:700; color:#0078d4; margin:4px 0;">Мономер (Мн)</div>
                <div style="font-size:11px; color:#8a8886;">1 Мн = 2.5 cm</div>
            </div>
        </div>
    </div>

    <!-- 3D Flip Provincial Showcase -->
    <div class="ol-card" id="showcase" style="padding:0; overflow:hidden;">
        <div style="position:relative; height:240px; background:#2a3b4c; overflow:hidden;">
            <img src="/images/plants_banner.jpg" alt="Sangaia Landscape" style="width:100%; height:100%; object-fit:cover; opacity:0.9;">
            <div style="position:absolute; bottom:0; left:0; right:0; padding:16px 20px; background:linear-gradient(transparent, rgba(15,23,42,0.85)); color:#ffffff;">
                <span class="ol-badge-tag" style="background:#0284c7; color:#fff; border-color:#38bdf8; margin-bottom:6px;">SOVEREIGN SHOWCASE</span>
                <h2 style="color:#ffffff; font-size:22px; margin:0;">Pristine Biomes of the Five Provinces</h2>
                <p class="ol-small" style="color:#e2e8f0; margin:4px 0 0;">New Jasper &bull; New Madison &bull; Liveland &bull; Sentinel &bull; Columbia</p>
            </div>
        </div>
    </div>

    <!-- Republic Vision Card -->
    <div class="ol-card">
        <div class="ol-card-title">
            <span>Better for Everyone. Including You.</span>
            <span class="ol-badge-tag ol-badge-success">Constitutional Republic</span>
        </div>
        <p>Sangaia is established to resolve the failures of legacy commercial republics. Offering accessible land, guaranteed living wages ($25.00/hr floor), zero foreign sovereign debt, and free universal healthcare and education, Sangaia is united across five distinct provincial territories designed for clarity, virtue, and prosperity.</p>
        <p>Sangaia strives to advance civic virtue and public dignity each day, inviting every citizen and prospective migrant to contribute to our shared Commonwealth.</p>
    </div>

    <!-- The Aeretocracy Framework Card -->
    <div class="ol-card" id="aeretocracy">
        <div class="ol-card-title">
            <span>Reinvented Politics. Constitutionally Ruled.</span>
            <a class="ol-title-link" href="/government.html">Learn About Government &rarr;</a>
        </div>
        <p>Sangaia has pioneered a constitutional form of government: <strong>The Aeretocracy</strong>. Unlike legacy states trapped in corporate lobbying or authoritarian party warfare, our system eliminates political parties in favor of institutional virtues, merit-based public exams, and transparent council governance.</p>
        <p>Sangaia provides familiar republican liberties with ironclad constitutional protections: <strong>It is structured so that no official—not even the Aeretocrat—can break the law</strong>.</p>
    </div>

    <!-- 9 Federal Ministries Grid -->
    <div class="ol-card" id="ministries">
        <div class="ol-card-title">
            <span>The Nine Federal Ministries of Sangaia</span>
            <a class="ol-title-link" href="/services.html">View All 72+ Services &rarr;</a>
        </div>
        <div class="ol-grid-3">
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong style="color:#1e3a8a;">🏛️ Executive</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">Aeretocrat's Journal, Cabinet, National Budget &amp; Decrees.</p>
                <a href="/executive.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Portal &rarr;</a>
            </div>
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong style="color:#0f766e;">💰 Treasury</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">Zero Debt, Solidarity Loans, Tax Code &amp; Audits.</p>
                <a href="/treasury.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Portal &rarr;</a>
            </div>
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong style="color:#6b21a8;">⚒️ Work</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">Living Wage ($25/hr), Job Board &amp; Guild Rights.</p>
                <a href="/work.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Portal &rarr;</a>
            </div>
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong style="color:#b91c1c;">🏥 Healthcare</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">100% Free Universal Healthcare &amp; ER Capacity.</p>
                <a href="/healthcare.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Portal &rarr;</a>
            </div>
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong style="color:#0284c7;">🎓 Education</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">Tuition-Free Universities, Textbooks &amp; Teachers.</p>
                <a href="/education.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Portal &rarr;</a>
            </div>
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong style="color:#1e293b;">🏢 Domestic Affairs</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">Provincial Relations, Trade, DMV &amp; Highways.</p>
                <a href="/domesticaffairs.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Portal &rarr;</a>
            </div>
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong style="color:#db2777;">🌐 External Affairs</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">Worldwide Travel Advisories, Treaties &amp; Embassies.</p>
                <a href="/externalaffairs.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Portal &rarr;</a>
            </div>
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong style="color:#15803d;">🌲 Environment</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">Weather in &deg;Пт, Biome Funds &amp; 3.4M Trees Planted.</p>
                <a href="/environment.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Portal &rarr;</a>
            </div>
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong style="color:#ea580c;">📻 Propaganda</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">State TV, Live Radio Stream, Press &amp; Churches.</p>
                <a href="/propaganda.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Portal &rarr;</a>
            </div>
        </div>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Digital Citizenship</h3>
        <p class="ol-small ol-muted">Equal opportunity civic naturalization for all who seek virtue, work, and community.</p>
        <div class="ol-mt-10">
            <a href="/citizenship.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">Citizenship Charter</a>
            <a href="/application.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center; margin-top:6px;">Apply for Citizenship</a>
        </div>
    </div>
    <div class="ol-sidebox">
        <h3>Sovereign Measurement</h3>
        <p class="ol-small ol-muted">Sangaia standardizes upon base-10 Monomer distance (Мн) and Panotherm temperature (&deg;Пт).</p>
        <div class="ol-mt-10">
            <a href="/units.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Open Units Calculator</a>
        </div>
    </div>
    """

    federal_nav_tabs = [
        ("home", "Federal Home", "/index.html"),
        ("overview", "Overview", "#overview"),
        ("showcase", "5 Provinces", "#showcase"),
        ("aeretocracy", "The Aeretocracy", "#aeretocracy"),
        ("ministries", "9 Ministries", "#ministries"),
        ("services", "Services", "/services.html"),
        ("units", "Units (Мн • °Пт)", "/units.html"),
    ]
    generate_page("index.html", title, theme, tab, hero_title, hero_sub, "Sovereign Republic of Sangaia", "Federal Executive Gateway", "Live Infrastructure", sidebar_links, main_content, sidebar_right, custom_nav_tabs=federal_nav_tabs)

# -----------------------------------------------------------------------------
# 2. SOVEREIGN WEIGHTS & MEASURES (units.html)
# -----------------------------------------------------------------------------
def build_units():
    title = "Sovereign Weights & Measures System"
    theme = "theme-education"
    tab = "units"
    hero_title = "Sovereign Weights & Measures Directorate"
    hero_sub = "Official standard systems: The Панотерм (°Пт) & Мономер (Мн) • Base-10 scaling with human dimensions"

    sidebar_links = [
        {"label": "Overview & Mandate", "url": "#overview", "active": True},
        {"label": "Temperature: Панотерм (°Пт)", "url": "#temp-converter", "active": False},
        {"label": "Distance: Мономер (Мн)", "url": "#dist-converter", "active": False},
        {"label": "Conversion Reference Tables", "url": "#tables", "active": False},
        {"label": "Mathematical Principles", "url": "#principles", "active": False}
    ]

    main_content = """

    <!-- Panotherm Temperature Converter -->
    <div class="card" id="overview"><a id="temp-converter"></a>
        <div class="ol-card-title">
            <span>1. Temperature Standard &bull; The Панотерм (&deg;Пт)</span>
            <span class="ol-badge-tag ol-badge-success">&deg;Пт = 0.9 &times; &deg;C = 0.5 &times; (&deg;F - 32)</span>
        </div>
        <p class="ol-small">Effortless mental conversions: <strong>From Fahrenheit</strong>: Drop 32, then cut in half (86&deg;F &rarr; 54 &rarr; <strong>27&deg;Пт</strong>). <strong>From Celsius</strong>: Subtract 10% (30&deg;C - 3 = <strong>27&deg;Пт</strong>).</p>

        <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:3px; padding:14px; margin-top:10px;">
            <div style="display:flex; flex-wrap:wrap; gap:12px;">
                <div style="flex:1 1 140px;">
                    <label class="form-label">Панотерм (&deg;Пт)</label>
                    <input type="number" class="ol-input" id="inPt" value="27" step="any" style="font-size:16px; font-weight:700; color:#15803d;">
                </div>
                <div style="flex:1 1 140px;">
                    <label class="form-label">Celsius (&deg;C)</label>
                    <input type="number" class="ol-input" id="inC" value="30" step="any" style="font-size:16px; font-weight:700;">
                </div>
                <div style="flex:1 1 140px;">
                    <label class="form-label">Fahrenheit (&deg;F)</label>
                    <input type="number" class="ol-input" id="inF" value="86" step="any" style="font-size:16px; font-weight:700;">
                </div>
            </div>
            <div style="margin-top:10px; padding-top:8px; border-top:1px dashed #cbd5e1;" class="ol-small" id="tempMentalText">
                • <strong>From Fahrenheit (86&deg;F)</strong>: Drop 32 (54), then cut in half &rarr; <strong>27&deg;Пт</strong>.<br>
                • <strong>From Celsius (30&deg;C)</strong>: Subtract 10% (-3) &rarr; <strong>27&deg;Пт</strong>.
            </div>
        </div>
    </div>

    <!-- Monomer Distance Converter -->
    <div class="ol-card" id="dist-converter">
        <div class="ol-card-title">
            <span>2. Universal Distance System &bull; The Мономер (Мн)</span>
            <span class="ol-badge-tag ol-badge-success">1 Monomer = Exactly 2.5 cm</span>
        </div>
        <p class="ol-small">The Mathematical Sweet Spot: Defined as exactly 2.5 cm (98.4% identical to an inch), Monomer scales cleanly into base-10 units while eliminating awkward imperial math (12 inches, 5,280 feet).</p>

        <div style="background:#f0f9ff; border:1px solid #bae6fd; border-radius:3px; padding:14px; margin-top:10px;">
            <div style="display:flex; flex-wrap:wrap; gap:12px;">
                <div style="flex:2 1 200px;">
                    <label class="form-label">Input Value:</label>
                    <input type="number" class="ol-input" id="distVal" value="10" step="any" style="font-size:16px; font-weight:700; color:#0369a1;">
                </div>
                <div style="flex:1 1 180px;">
                    <label class="form-label">Selected Unit:</label>
                    <select class="ol-select" id="distUnit" style="font-size:13.5px;">
                        <option value="mn" selected>Мономер (Мн - 2.5 cm)</option>
                        <option value="dmn">Декамер (Дмн - 10 Мн / 25 cm)</option>
                        <option value="trideka">Тридека (3Дмн - 30 Мн / 75 cm)</option>
                        <option value="kvadrodeka">Квадродека (4Дмн - 40 Мн / 1 m)</option>
                        <option value="kmn">Киломер (Кмн - 60,000 Мн / 1.5 km)</option>
                        <option value="cm">Centimeters (cm)</option>
                        <option value="m">Meters (m)</option>
                        <option value="in">Inches (in)</option>
                        <option value="ft">Feet (ft)</option>
                        <option value="mi">Miles (mi)</option>
                    </select>
                </div>
            </div>

            <!-- Dynamic Output Grid -->
            <div class="ol-grid-3" id="distOutputGrid" style="margin-top:14px;">
                <!-- Populated via JS -->
            </div>

            <div style="margin-top:12px; padding-top:8px; border-top:1px dashed #cbd5e1;" class="ol-small" id="distMentalText">
                • <strong>Monomers to Centimeters</strong>: Multiply by 2.5 (10 Мн &times; 2.5 = <strong>25 cm</strong>).<br>
                • <strong>Kilomers to Miles</strong>: Drop last three zeros and divide by 6 (60,000 Мн &rarr; 60 &divide; 6 = <strong>1.0 mile</strong>).
            </div>
        </div>
    </div>

    <!-- Official Distance Table -->
    <div class="ol-card" id="tables">
        <div class="ol-card-title">
            <span>Sovereign Distance Master Scaling Table</span>
            <span class="ol-badge-tag">Statutory Schedule A</span>
        </div>
        <table class="ol-table">
            <thead>
                <tr>
                    <th>Imperial / Metric Unit</th>
                    <th>Exact Conversion</th>
                    <th>New Cyrillic Name</th>
                    <th>Symbol</th>
                    <th>Monomer Value</th>
                    <th>Human Visual Reference</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>1 Centimeter</td><td>0.4 Мн</td><td>Децимн (Decimn)</td><td><strong>дмн</strong></td><td>0.4 Мн</td><td>Width of a fingernail</td></tr>
                <tr><td>1 Inch</td><td>1.016 Мн (1:1 everyday)</td><td>Мономер (Monomer)</td><td><strong>Мн</strong></td><td>1 Мн</td><td>Knuckle of a thumb</td></tr>
                <tr><td>1 Foot</td><td>12.19 Мн (10 Мн base)</td><td>Декамер (Dekamer)</td><td><strong>Дмн</strong></td><td>10 Мн</td><td>Length of a human foot</td></tr>
                <tr><td>1 Yard</td><td>36.57 Мн (30 Мн base)</td><td>Тридека (Trideka)</td><td><strong>3Дмн</strong></td><td>30 Мн</td><td>One large stride</td></tr>
                <tr><td>1 Meter</td><td>40 Мн</td><td>Квадродека (Kvadrodeka)</td><td><strong>4Дмн</strong></td><td>40 Мн</td><td>Guitar length</td></tr>
                <tr><td>1 Mile</td><td>63,360 Мн (60,000 base)</td><td>Киломер (Kilomer)</td><td><strong>Кмн</strong></td><td>60,000 Мн</td><td>15-minute brisk walk</td></tr>
            </tbody>
        </table>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Standardization Decree</h3>
        <p class="ol-small ol-muted">Decreed under Executive Order 103 for educational curricula, engineering tolerances, and road signage nationwide.</p>
    </div>
    """

    scripts = """
    <script>
    document.addEventListener('DOMContentLoaded', () => {
        // Temperature Engine
        const inPt = document.getElementById('inPt');
        const inC = document.getElementById('inC');
        const inF = document.getElementById('inF');
        const tempText = document.getElementById('tempMentalText');

        function updateTemp(c, source) {
            const pt = c * 0.9;
            const f = c * 1.8 + 32;

            if (source !== 'pt') inPt.value = (Math.round(pt * 10) / 10).toFixed(1).replace('.0','');
            if (source !== 'c') inC.value = (Math.round(c * 10) / 10).toFixed(1).replace('.0','');
            if (source !== 'f') inF.value = (Math.round(f * 10) / 10).toFixed(1).replace('.0','');

            const ptR = Math.round(pt);
            const fR = Math.round(f);
            const cR = Math.round(c);
            tempText.innerHTML = `• <strong>From Fahrenheit (${fR}&deg;F)</strong>: Drop 32 (${fR - 32}), cut in half &rarr; <strong>${ptR}&deg;Пт</strong>.<br>• <strong>From Celsius (${cR}&deg;C)</strong>: Subtract 10% (-${(cR*0.1).toFixed(1)}) &rarr; <strong>${ptR}&deg;Пт</strong>.`;
        }

        inPt.addEventListener('input', () => {
            const v = parseFloat(inPt.value);
            if (!isNaN(v)) updateTemp(v / 0.9, 'pt');
        });
        inC.addEventListener('input', () => {
            const v = parseFloat(inC.value);
            if (!isNaN(v)) updateTemp(v, 'c');
        });
        inF.addEventListener('input', () => {
            const v = parseFloat(inF.value);
            if (!isNaN(v)) updateTemp((v - 32) / 1.8, 'f');
        });

        // Distance Engine
        const distVal = document.getElementById('distVal');
        const distUnit = document.getElementById('distUnit');
        const grid = document.getElementById('distOutputGrid');
        const distText = document.getElementById('distMentalText');

        const toMn = {
            'mn': 1.0, 'dmn': 10.0, 'trideka': 30.0, 'kvadrodeka': 40.0, 'kmn': 60000.0,
            'cm': 0.4, 'm': 40.0, 'in': 1.016, 'ft': 12.192, 'mi': 64373.76
        };

        function updateDist() {
            const v = parseFloat(distVal.value) || 0;
            const u = distUnit.value;
            const mn = v * (toMn[u] || 1.0);

            const dmn = mn / 10.0;
            const tri = mn / 30.0;
            const kva = mn / 40.0;
            const kmn = mn / 60000.0;

            const cm = mn * 2.5;
            const m = cm / 100.0;
            const inches = cm / 2.54;
            const feet = inches / 12.0;
            const miles = feet / 5280.0;

            function fmt(n) {
                if (n === 0) return '0';
                if (Math.abs(n) >= 1000) return n.toLocaleString('en-US', { maximumFractionDigits: 2 });
                return (Math.round(n * 1000) / 1000).toString();
            }

            grid.innerHTML = `
                <div class="ol-metric-box">
                    <div class="ol-metric-val">${fmt(mn)} Мн</div>
                    <div class="ol-metric-lbl">Мономер (Knuckle ~1 in)</div>
                </div>
                <div class="ol-metric-box">
                    <div class="ol-metric-val">${fmt(dmn)} Дмн</div>
                    <div class="ol-metric-lbl">Декамер (Foot ~1 ft)</div>
                </div>
                <div class="ol-metric-box">
                    <div class="ol-metric-val">${fmt(tri)} 3Дмн</div>
                    <div class="ol-metric-lbl">Тридека (Stride ~1 yd)</div>
                </div>
                <div class="ol-metric-box">
                    <div class="ol-metric-val">${fmt(kva)} 4Дмн</div>
                    <div class="ol-metric-lbl">Квадродека (Exactly 1.0 m)</div>
                </div>
                <div class="ol-metric-box">
                    <div class="ol-metric-val">${fmt(kmn)} Кмн</div>
                    <div class="ol-metric-lbl">Киломер (Walk ~1 mi)</div>
                </div>
                <div class="ol-metric-box" style="background:#f1f5f9;">
                    <div class="ol-metric-val" style="font-size:18px; color:#334155;">${fmt(cm)} cm / ${fmt(feet)} ft</div>
                    <div class="ol-metric-lbl">Legacy Metric / Imperial</div>
                </div>
            `;

            distText.innerHTML = `• <strong>Monomers to Centimeters</strong>: Multiply by 2.5 (${fmt(mn)} Мн &times; 2.5 = <strong>${fmt(cm)} cm</strong>).<br>• <strong>Kilomers to Miles</strong>: Drop last three zeros and divide by 6 (${fmt(kmn*60000)} Мн &rarr; ${fmt(kmn*60)} &divide; 6 = <strong>${fmt(kmn*10)} mi</strong>).`;
        }

        distVal.addEventListener('input', updateDist);
        distUnit.addEventListener('change', updateDist);
        updateDist();
    });
    </script>
    """

    generate_page("units.html", title, theme, tab, hero_title, hero_sub, "Weights & Measures Bureau", "Standards Authority", "Standards Active", sidebar_links, main_content, sidebar_right, "", scripts)

# -----------------------------------------------------------------------------
# 3. DIRECTORY OF ALL SERVICES (services.html)
# -----------------------------------------------------------------------------
def build_services():
    title = "Sovereign Services Directory"
    theme = "theme-federal"
    tab = "services"
    hero_title = "Directory of Government Services & Online Tools"
    hero_sub = "Searchable registry of all 72+ statutory citizen portals across the 9 Federal Ministries"

    sidebar_links = [
        {"label": "All 9 Portals", "url": "#overview", "active": True},
        {"label": "Executive Services", "url": "/executive_departments.html", "active": False},
        {"label": "Treasury Services", "url": "/treasury_departments.html", "active": False},
        {"label": "Work & Labor Services", "url": "/work_departments.html", "active": False},
        {"label": "Healthcare Services", "url": "/healthcare_departments.html", "active": False},
        {"label": "Education Services", "url": "/education_departments.html", "active": False},
        {"label": "Domestic Affairs", "url": "/domesticaffairs_departments.html", "active": False},
        {"label": "External Affairs", "url": "/externalaffairs_departments.html", "active": False},
        {"label": "Environment Services", "url": "/environment_departments.html", "active": False},
        {"label": "Propaganda Services", "url": "/propaganda_departments.html", "active": False}
    ]

    main_content = """

    <div class="ol-card">
        <div class="ol-card-title">
            <span>Instant Public Service Directory Search</span>
            <span class="ol-badge-tag">72 Tools Available</span>
        </div>
        <p class="ol-small ol-muted">Type any department name, service title, calculator, or keyword to filter the master government catalog.</p>
        <input type="text" class="ol-input" id="servSearch" placeholder="Type keyword (e.g., tax, permit, hospital, visa, weather, radio)..." oninput="filterServices()">
    </div>

    <div class="ol-card">
        <div class="ol-card-title">
            <span>Master Catalog of Statutory Portals</span>
            <span class="ol-badge-tag ol-badge-success">All Active</span>
        </div>

        <div id="servicesMasterList">
            <div class="docket-entry serv-entry" data-cat="executive">
                <div class="docket-entry-body">
                    <strong style="font-size:14px; color:#1e3a8a;">🏛️ Ministry of the Executive</strong>
                    <div class="ol-small">Official Gazette decree archives, citizen petition pipeline, dignitary ceremonial protocol, national KPI progress dashboard, multi-ministry policy whitepapers.</div>
                    <div class="ol-mt-10"><a href="/executive_departments.html" class="ol-btn ol-btn-sm">Launch Executive Departments (6 Tools) &rarr;</a></div>
                </div>
            </div>

            <div class="docket-entry serv-entry" data-cat="treasury">
                <div class="docket-entry-body">
                    <strong style="font-size:14px; color:#0f766e;">💰 Ministry of the Treasury</strong>
                    <div class="ol-small">Individual &amp; corporate tax calculator, digital tax filing &amp; clearance, tax appeals, debt tracker &amp; solidarity bonds, procurement tenders, and expenditure audits.</div>
                    <div class="ol-mt-10"><a href="/treasury_departments.html" class="ol-btn ol-btn-sm">Launch Treasury Departments (9 Tools) &rarr;</a></div>
                </div>
            </div>

            <div class="docket-entry serv-entry" data-cat="work">
                <div class="docket-entry-body">
                    <strong style="font-size:14px; color:#6b21a8;">⚒️ Ministry of Work</strong>
                    <div class="ol-small">Anonymous labor whistleblower reporting, union registry, online mediation calendar, national job board, unemployment safety nets, vocational retraining, foreign labor visas.</div>
                    <div class="ol-mt-10"><a href="/work_departments.html" class="ol-btn ol-btn-sm">Launch Work Departments (9 Tools) &rarr;</a></div>
                </div>
            </div>

            <div class="docket-entry serv-entry" data-cat="healthcare">
                <div class="docket-entry-body">
                    <strong style="font-size:14px; color:#b91c1c;">🏥 Ministry of Healthcare</strong>
                    <div class="ol-small">Universal coverage eligibility screening, digital health card management, prescription claims, live ER triage capacity, non-emergency transports, and paramedic licensing.</div>
                    <div class="ol-mt-10"><a href="/healthcare_departments.html" class="ol-btn ol-btn-sm">Launch Healthcare Departments (6 Tools) &rarr;</a></div>
                </div>
            </div>

            <div class="docket-entry serv-entry" data-cat="education">
                <div class="docket-entry-body">
                    <strong style="font-size:14px; color:#0284c7;">🎓 Ministry of Education</strong>
                    <div class="ol-small">Digital textbook repository, teacher certification, school performance scorecards, university accreditation, tuition-free research grants, and institutional funding audits.</div>
                    <div class="ol-mt-10"><a href="/education_departments.html" class="ol-btn ol-btn-sm">Launch Education Departments (9 Tools) &rarr;</a></div>
                </div>
            </div>

            <div class="docket-entry serv-entry" data-cat="domestic">
                <div class="docket-entry-body">
                    <strong style="font-size:14px; color:#1e293b;">🏢 Ministry of Domestic Affairs</strong>
                    <div class="ol-small">Live road condition maps in Monomers/Kilomers, road maintenance reporting, commercial driver licensing, digital vehicle titles, provincial trade registry, inter-provincial dispute arbitration.</div>
                    <div class="ol-mt-10"><a href="/domesticaffairs_departments.html" class="ol-btn ol-btn-sm">Launch Domestic Departments (9 Tools) &rarr;</a></div>
                </div>
            </div>

            <div class="docket-entry serv-entry" data-cat="external">
                <div class="docket-entry-body">
                    <strong style="font-size:14px; color:#db2777;">🌐 Ministry of External Affairs</strong>
                    <div class="ol-small">Consular services locator, emergency repatriation assistance, diplomatic visa applications, public treaty archive, treaty violation reporting, export compliance assistance.</div>
                    <div class="ol-mt-10"><a href="/externalaffairs_departments.html" class="ol-btn ol-btn-sm">Launch External Departments (9 Tools) &rarr;</a></div>
                </div>
            </div>

            <div class="docket-entry serv-entry" data-cat="environment">
                <div class="docket-entry-body">
                    <strong style="font-size:14px; color:#15803d;">🌲 Ministry of the Environment</strong>
                    <div class="ol-small">Local weather in &deg;Пт, public land use permits, provincial biome funding trackers, wildlife intervention hotline, endangered species monitoring, emissions telemetry, and organic certifications.</div>
                    <div class="ol-mt-10"><a href="/environment_departments.html" class="ol-btn ol-btn-sm">Launch Environment Departments (9 Tools) &rarr;</a></div>
                </div>
            </div>

            <div class="docket-entry serv-entry" data-cat="propaganda">
                <div class="docket-entry-body">
                    <strong style="font-size:14px; color:#ea580c;">📻 Ministry of Propaganda</strong>
                    <div class="ol-small">State broadcast channel directory, live radio audio stream player, journalist accreditation registry, religious society registry, and mandatory 85% wealth redistribution audits.</div>
                    <div class="ol-mt-10"><a href="/propaganda_departments.html" class="ol-btn ol-btn-sm">Launch Propaganda Departments (9 Tools) &rarr;</a></div>
                </div>
            </div>
        </div>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Fast Identity Check</h3>
        <p class="ol-small ol-muted">Your Sangaia ID grants immediate access across all statutory portals without multiple passwords.</p>
        <div class="ol-mt-10">
            <a href="/id.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">View Sangaia ID</a>
        </div>
    </div>
    """

    scripts = """
    <script>
    function filterServices() {
        const q = (document.getElementById('servSearch').value || '').toLowerCase();
        document.querySelectorAll('.serv-entry').forEach(el => {
            el.style.display = el.innerText.toLowerCase().includes(q) ? 'flex' : 'none';
        });
    }

    // Auto-fill from URL param if present
    document.addEventListener('DOMContentLoaded', () => {
        const params = new URLSearchParams(window.location.search);
        const q = params.get('q');
        if (q) {
            const inp = document.getElementById('servSearch');
            if (inp) {
                inp.value = q;
                filterServices();
            }
        }
    });
    </script>
    """

    generate_page("services.html", title, theme, tab, hero_title, hero_sub, "Public Service Delivery", "Unified Portal Hub", "72 Tools Online", sidebar_links, main_content, sidebar_right, "", scripts)

# -----------------------------------------------------------------------------
# 4. CITIZENSHIP & CHARTER (citizenship.html)
# -----------------------------------------------------------------------------
def build_citizenship():
    title = "Sovereign Citizenship"
    theme = "theme-federal"
    tab = "home"
    hero_title = "Citizenship & Civic Rights of Sangaia"
    hero_sub = "Equal opportunity naturalization, charter of liberties, civic responsibilities & the oath"

    sidebar_links = [
        {"label": "Overview & Charter", "url": "#overview", "active": True},
        {"label": "Eligibility Tiers", "url": "#eligibility", "active": False},
        {"label": "Civic Literacy Exam", "url": "/literacy_test.html", "active": False},
        {"label": "Online Application", "url": "/application.html", "active": False},
        {"label": "Sangaia ID Portal", "url": "/id.html", "active": False}
    ]

    main_content = """

    <div class="card" id="overview"><a id="charter"></a>
        <div class="ol-card-title">
            <span>The Sangaian Charter of Fundamental Liberties</span>
            <span class="ol-badge-tag ol-badge-success">Constitutional Guarantees</span>
        </div>
        <ul style="line-height:1.7; font-size:13.5px;">
            <li><strong>Inviolability of Bodily Integrity &amp; Care:</strong> Universal healthcare is constitutionally protected with zero out-of-pocket costs at point of service.</li>
            <li><strong>Freedom of Conscience &amp; Speech:</strong> Complete freedom of expression, journalism shield rights, and peaceful religious assembly.</li>
            <li><strong>Protection Against Sovereign Indebtedness:</strong> Freedom from predatory state debt and compound interest banking structures.</li>
            <li><strong>Right to Labor &amp; Fair Compensation:</strong> Every worker is guaranteed a statutory living wage of at least $25.00/hr and guild representation.</li>
        </ul>
    </div>

    <div class="ol-card" id="eligibility">
        <div class="ol-card-title">
            <span>Naturalization &amp; Eligibility Tiers</span>
            <a class="ol-title-link" href="/application.html">Apply Online &rarr;</a>
        </div>
        <div class="ol-grid-3">
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong>Birthright Status</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">Conferred automatically to children born to Sangaian citizens or within the Five Provinces.</p>
                <span class="ol-badge-tag ol-badge-success">Immediate</span>
            </div>
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong>Resident Naturalization</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">Available to foreign professionals after 24 months continuous residence and civic examination.</p>
                <a href="/literacy_test.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center; margin-top:4px;">Take Exam</a>
            </div>
            <div class="ol-card" style="margin-bottom:0; background:#fbfcfd;">
                <strong>Sovereign Merit Grant</strong>
                <p class="ol-small ol-muted" style="margin:4px 0 8px;">Awarded directly by the Aeretocrat to scientists, artists, and humanitarians of global distinction.</p>
                <span class="ol-badge-tag">Council Review</span>
            </div>
        </div>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Begin Naturalization</h3>
        <p class="ol-small ol-muted">Complete the online examination and submit your civic petition to the Ministry of the Executive.</p>
        <div class="ol-mt-10">
            <a href="/application.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">File Application</a>
        </div>
    </div>
    """

    generate_page("citizenship.html", title, theme, tab, hero_title, hero_sub, "Civic Registry Bureau", "Citizenship & Naturalization", "Registry Active", sidebar_links, main_content, sidebar_right)

# -----------------------------------------------------------------------------
# 5. GOVERNMENT & ABOUT (government.html & about.html)
# -----------------------------------------------------------------------------
def build_gov_about():
    # government.html
    title_gov = "Government Structure & The Aeretocracy"
    theme = "theme-federal"
    tab = "home"
    hero_title_gov = "Constitutional Structure of the Republic"
    hero_sub = "Separation of Virtues &bull; The Aeretocrat, Council of Magistrates & 5 Sovereign Provinces"

    sidebar_links_gov = [
        {"label": "Constitutional Structure", "url": "#overview", "active": True},
        {"label": "The Aeretocrat", "url": "#aeretocrat", "active": False},
        {"label": "Separation of Virtues", "url": "#virtues", "active": False},
        {"label": "The 5 Provinces", "url": "#provinces", "active": False},
        {"label": "Cabinet of Ministers", "url": "#cabinet", "active": False}
    ]

    main_gov = """

    <div class="ol-card" id="virtues">
        <div class="ol-card-title">
            <span>Separation of Virtues &bull; The Four Constitutional Branches</span>
            <span class="ol-badge-tag ol-badge-success">Unalterable Law</span>
        </div>
        <div class="ol-grid-2">
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong style="color:#1e3a8a;">1. The Executive Council &amp; Aeretocrat:</strong>
                <p class="ol-small" style="margin:4px 0;">Headed by the Aeretocrat as Supreme Executive Magistrate. Administers federal decree enforcement, foreign treaties, and whole-of-government synchronization.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong style="color:#0f766e;">2. The Council of Fiscal Rectitude:</strong>
                <p class="ol-small" style="margin:4px 0;">Treasury magistrates with independent prosecutorial powers to block unconstitutional sovereign debt or predatory financial legislation.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong style="color:#1e293b;">3. The Federal Council of Governors:</strong>
                <p class="ol-small" style="margin:4px 0;">Elected executive governors of New Jasper, New Madison, Liveland, Sentinel, and Columbia coordinating interstate commerce and transport.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong style="color:#b91c1c;">4. The High Magistrates of Virtue:</strong>
                <p class="ol-small" style="margin:4px 0;">Senior constitutional jurists reviewing civil rights, ensuring zero corruption, and adjudicating interprovincial legal accords.</p>
            </div>
        </div>
    </div>

    <div class="ol-card" id="provinces">
        <div class="ol-card-title">
            <span>The Five Sovereign Provinces</span>
            <span class="ol-badge-tag">Self-Governing Republics</span>
        </div>
        <p class="ol-small">Sangaia comprises five sovereign provinces, each with a regional assembly, distinct economic specializations, and full cultural liberties:</p>
        <ul style="font-size:13.5px; line-height:1.7;">
            <li><strong>New Jasper (Shesk):</strong> Seat of federal government, sovereign technology, and legal jurisprudence.</li>
            <li><strong>New Madison (Madison City):</strong> Agricultural breadbasket, renewable biofuels, and educational institutes.</li>
            <li><strong>Liveland (Oaks):</strong> Maritime trade, oceanic fisheries, coastal tourism, and tidal energy.</li>
            <li><strong>Sentinel (Sentinel Ridge):</strong> Alpine mineral stewardship, geothermal energy, and forestry reserves.</li>
            <li><strong>Columbia (Columbia City):</strong> Cultural humanities, aerospace engineering, and fine arts.</li>
        </ul>
    </div>
    """

    generate_page("government.html", title_gov, theme, tab, hero_title_gov, hero_sub, "Constitutional Council", "Aeretocratic Governance", "Constitution Active", sidebar_links_gov, main_gov)

    # about.html
    title_about = "About the United Provinces of Sangaia"
    hero_title_about = "About Sangaia"
    hero_sub_about = "History, sovereign geography, demographic prosperity, and the Aeretocrat's mission"

    sidebar_links_about = [
        {"label": "Republic History", "url": "#overview", "active": True},
        {"label": "Geography & 5 Provinces", "url": "#geography", "active": False},
        {"label": "Monetary Foundations", "url": "#economy", "active": False},
        {"label": "Government Structure", "url": "/government.html", "active": False}
    ]

    main_about = """

    <div class="ol-card" id="history">
        <div class="ol-card-title">
            <span>Founding &amp; Historical Mission</span>
            <span class="ol-badge-tag ol-badge-success">Established 2024</span>
        </div>
        <p>Founded as a sanctuary of virtue, constitutional stability, and economic sanity, the United Provinces of Sangaia rejects both the hyper-corporatism of legacy Western empires and the tyranny of authoritarian regimes.</p>
        <p>Our monetary system is anchored by the <strong>Sangaian Dollar ($)</strong>, free of compound debt obligations to foreign financiers, backed by sovereign mineral and energy reserves.</p>
    </div>

    <div class="ol-card" id="geography">
        <div class="ol-card-title">
            <span>Geography of the Five Sovereign Provinces</span>
            <span class="ol-badge-tag">7,870,000 Total Population</span>
        </div>
        <table class="ol-table">
            <thead>
                <tr><th>Province</th><th>Capital</th><th>Population</th><th>Dominant Landscape</th></tr>
            </thead>
            <tbody>
                <tr><td>New Jasper</td><td>Shesk</td><td>2,410,000</td><td>Forest River Valleys &amp; Capitol Plains</td></tr>
                <tr><td>New Madison</td><td>Madison City</td><td>1,980,000</td><td>Alluvial Plains &amp; Hydroponic Valleys</td></tr>
                <tr><td>Liveland</td><td>Oaks</td><td>1,650,000</td><td>Coastal Peninsulas &amp; Marine Harbors</td></tr>
                <tr><td>Sentinel</td><td>Sentinel Ridge</td><td>890,000</td><td>Alpine Peaks &amp; Conifer Forests</td></tr>
                <tr><td>Columbia</td><td>Columbia City</td><td>940,000</td><td>Rolling Highlands &amp; Lake Basins</td></tr>
            </tbody>
        </table>
    </div>
    """

    generate_page("about.html", title_about, theme, tab, hero_title_about, hero_sub_about, "Sovereign Republic", "Overview & History", "Republic Stable", sidebar_links_about, main_about)

# -----------------------------------------------------------------------------
# 6. SOCIETAL PRESS & GAZETTE (societal_press.html)
# -----------------------------------------------------------------------------
def build_societal_press():
    title = "State Gazette & Societal Press"
    theme = "theme-federal"
    tab = "home"
    hero_title = "The State Gazette &amp; Societal Press"
    hero_sub = "Official public gazette, executive decrees, circulars, statutory regulations & open government archives"

    sidebar_links = [
        {"label": "Latest Decrees", "url": "#overview", "active": True},
        {"label": "Executive Circulars", "url": "#circulars", "active": False},
        {"label": "Regulatory Archives", "url": "#archives", "active": False},
        {"label": "Public Hearing Transcripts", "url": "#transcripts", "active": False}
    ]

    main_content = """

    <div class="ol-card">
        <div class="ol-card-title">
            <span>Recent Official Executive Decrees</span>
            <span class="ol-badge-tag ol-badge-success">Enacted Law</span>
        </div>
        <div class="docket-entry">
            <div class="docket-entry-header">
                <div>
                    <span class="mif-file-text" style="color:var(--primary); margin-right:6px;"></span>
                    <strong style="color:#1e3a8a;">Decree No. 104-B: Mandatory 85% Wealth Redistribution for Religious Tithes</strong>
                </div>
                <span class="ol-badge-tag ol-badge-success">Enacted</span>
            </div>
            <div class="docket-entry-body">Enacts strict statutory accounting for all recognized chapels. Tithes must be returned directly to public kitchens, youth education, and community aid.</div>
            <div class="docket-entry-meta">Published October 19, 2026 &bull; Promulgated by the Aeretocrat</div>
        </div>
        <div class="docket-entry">
            <div class="docket-entry-header">
                <div>
                    <span class="mif-file-text" style="color:var(--primary); margin-right:6px;"></span>
                    <strong style="color:#15803d;">Decree No. 103-A: Universal Standard Units Adoption (Панотерм &amp; Мономер)</strong>
                </div>
                <span class="ol-badge-tag ol-badge-success">Enacted</span>
            </div>
            <div class="docket-entry-body">Mandates base-10 Monomer scaling (1 Мн = 2.5 cm) and Panotherm (&deg;Пт = 0.9 &times; &deg;C) across all five provincial school boards and public signage.</div>
            <div class="docket-entry-meta">Published October 15, 2026 &bull; Promulgated by the Aeretocrat</div>
        </div>
        <div class="docket-entry">
            <div class="docket-entry-header">
                <div>
                    <span class="mif-file-text" style="color:var(--primary); margin-right:6px;"></span>
                    <strong style="color:#0f766e;">Decree No. 102-F: Zero Out-of-Pocket Point-of-Service Healthcare Affirmation</strong>
                </div>
                <span class="ol-badge-tag ol-badge-success">Enacted</span>
            </div>
            <div class="docket-entry-body">Reaffirms constitutional prohibition against any emergency room, clinic, or pharmacy levying copays upon Sangaian ID holders.</div>
            <div class="docket-entry-meta">Published October 10, 2026 &bull; Promulgated by the Aeretocrat</div>
        </div>
    </div>
    """

    generate_page("societal_press.html", title, theme, tab, hero_title, hero_sub, "State Gazette Directorate", "Public Record Authority", "Gazette Online", sidebar_links, main_content)

# -----------------------------------------------------------------------------
# 7. DASHBOARD & APPLICATIONS & ID & LITERACY
# -----------------------------------------------------------------------------
def build_supporting_portals():
    theme = "theme-federal"
    tab = "home"

    # dashboard.html
    dash_content = """
    <div class="ol-card">
        <div class="ol-card-title">
            <span>Macroeconomic &amp; Fiscal Key Performance Indicators</span>
            <span class="ol-badge-tag ol-badge-success">Q3 FY2026</span>
        </div>
        <div class="ol-grid-3">
            <div class="ol-metric-box">
                <div class="ol-metric-val">$ 482.4 B</div>
                <div class="ol-metric-lbl">National GDP</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">$ 0.00</div>
                <div class="ol-metric-lbl">Foreign Debt</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">+ $ 11.2 B</div>
                <div class="ol-metric-lbl">Fiscal Surplus</div>
            </div>
        </div>
    </div>
    <div class="ol-card">
        <div class="ol-card-title">
            <span>Social &amp; Environmental Vital Metrics</span>
            <span class="ol-badge-tag ol-badge-success">100% Target Met</span>
        </div>
        <div class="ol-grid-3">
            <div class="ol-metric-box">
                <div class="ol-metric-val">100%</div>
                <div class="ol-metric-lbl">Universal Health Coverage</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">3,420,840</div>
                <div class="ol-metric-lbl">Native Trees Planted</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">1:14</div>
                <div class="ol-metric-lbl">Student-Teacher Ratio</div>
            </div>
        </div>
    </div>
    """
    generate_page("dashboard.html", "National KPI Dashboard", theme, tab, "National Telemetry & Performance Dashboard", "Real-time key performance indicators across all 9 ministries", "Statistical Bureau", "Telemetry Directorate", "Metrics Live", [{"label": "National KPIs", "url": "#overview", "active": True}], dash_content)

    # application.html
    app_content = """
    <div class="ol-card">
        <div class="ol-card-title">
            <span>Submit Official Civic Application</span>
            <span class="ol-badge-tag">Encrypted Docket</span>
        </div>
        <div class="form-group">
            <label class="form-label">Full Legal Name</label>
            <input type="text" class="ol-input" id="app-name" placeholder="Applicant Legal Name">
        </div>
        <div class="form-group">
            <label class="form-label">Application Category</label>
            <select class="ol-select" id="app-cat">
                <option>Citizenship Naturalization</option>
                <option>Public Service &amp; Civil Bureau Apprenticeship</option>
                <option>Cooperative Enterprise Charter</option>
                <option>Environmental Land Stewardship Grant</option>
            </select>
        </div>
        <div class="form-group">
            <label class="form-label">Selected Province of Residence</label>
            <select class="ol-select" id="app-prov">
                <option>New Jasper</option><option>New Madison</option><option>Liveland</option><option>Sentinel</option><option>Columbia</option>
            </select>
        </div>
        <div class="form-group">
            <label class="form-label">Applicant Statement &amp; Intent</label>
            <textarea class="ol-textarea" id="app-stmt" rows="4" placeholder="Detail your background, civic commitment, or project goals..."></textarea>
        </div>
        <div class="modal-results-box" id="appResults"></div>
        <div class="ol-mt-10">
            <button type="button" class="ol-btn ol-btn-primary" onclick="submitApp()">Submit Official Application</button>
        </div>
    </div>
    """
    app_scripts = """
    <script>
    function submitApp() {
        const token = 'APP-' + Math.floor(100000 + Math.random() * 900000);
        const res = document.getElementById('appResults');
        res.innerHTML = `<strong>Application Recorded:</strong> Tracking Code: <span style="font-family:monospace;">${token}</span>. Placed on Civic Registry Docket.`;
        res.classList.add('active');
    }
    </script>
    """
    generate_page("application.html", "Public Application Portal", theme, tab, "Civic & Civil Service Application Portal", "Online filing gateway for citizenship, civil service & cooperative grants", "Civic Registry", "Application Hub", "Submissions Open", [{"label": "Application Form", "url": "#overview", "active": True}], app_content, "", "", app_scripts)

    # id.html & id/index.html with One Live People layout
    build_id_pages()

    # literacy_test.html & literacy_exam_en.html
    exam_content = """
    <div class="ol-card">
        <div class="ol-card-title">
            <span>Civic Naturalization Examination</span>
            <span class="ol-badge-tag">Instant Scoring</span>
        </div>
        <form id="quizForm" onsubmit="gradeQuiz(event)" style="display:flex; flex-direction:column; gap:16px;">
            <div>
                <strong>1. What is the official currency of Sangaia?</strong>
                <div style="margin-top:6px;"><label><input type="radio" name="q1" value="usd"> Euro</label></div>
                <div><label><input type="radio" name="q1" value="correct"> Sangaian Dollar ($)</label></div>
                <div><label><input type="radio" name="q1" value="wrong"> Sovereign Ruble</label></div>
            </div>
            <div>
                <strong>2. How many Sovereign Provinces comprise the Republic?</strong>
                <div style="margin-top:6px;"><label><input type="radio" name="q2" value="wrong"> 3</label></div>
                <div><label><input type="radio" name="q2" value="correct"> 5 (New Jasper, New Madison, Liveland, Sentinel, Columbia)</label></div>
                <div><label><input type="radio" name="q2" value="wrong"> 12</label></div>
            </div>
            <div>
                <strong>3. What is 30&deg;C in the Sangaian Panotherm (&deg;Пт) scale?</strong>
                <div style="margin-top:6px;"><label><input type="radio" name="q3" value="correct"> 27&deg;Пт (Subtract 10%)</label></div>
                <div><label><input type="radio" name="q3" value="wrong"> 30&deg;Пт</label></div>
                <div><label><input type="radio" name="q3" value="wrong"> 15&deg;Пт</label></div>
            </div>
            <div>
                <strong>4. Exactly how many centimeters is 1 Monomer (1 Мн)?</strong>
                <div style="margin-top:6px;"><label><input type="radio" name="q4" value="wrong"> 1.0 cm</label></div>
                <div><label><input type="radio" name="q4" value="correct"> Exactly 2.5 cm</label></div>
                <div><label><input type="radio" name="q4" value="wrong"> 10 cm</label></div>
            </div>
            <div>
                <strong>5. Under the Constitution, what is the policy regarding foreign sovereign debt?</strong>
                <div style="margin-top:6px;"><label><input type="radio" name="q5" value="correct"> Absolutely prohibited ($0 foreign debt)</label></div>
                <div><label><input type="radio" name="q5" value="wrong"> Borrowing up to 50% of GDP</label></div>
                <div><label><input type="radio" name="q5" value="wrong"> Managed via International IMF Loans</label></div>
            </div>
            <div class="modal-results-box" id="quizResults"></div>
            <div class="ol-mt-10">
                <button type="submit" class="ol-btn ol-btn-primary">Submit Examination for Grading</button>
            </div>
        </form>
    </div>
    """
    exam_scripts = """
    <script>
    function gradeQuiz(e) {
        e.preventDefault();
        const f = document.getElementById('quizForm');
        let score = 0;
        if (f.q1.value === 'correct') score++;
        if (f.q2.value === 'correct') score++;
        if (f.q3.value === 'correct') score++;
        if (f.q4.value === 'correct') score++;
        if (f.q5.value === 'correct') score++;

        const res = document.getElementById('quizResults');
        if (score >= 4) {
            res.innerHTML = `<strong>Examination Passed! Score: ${score}/5 (80%+).</strong> Congratulations! Certificate Code: <span style="font-family:monospace;">CERT-CIV-${Math.floor(100000 + Math.random()*900000)}</span>. You may now submit your Naturalization Application.`;
            res.className = 'modal-results-box active';
            res.style.background = '#f0fdf4';
            res.style.borderColor = '#bbf7d0';
            res.style.color = '#166534';
        } else {
            res.innerHTML = `<strong>Score: ${score}/5.</strong> Passing threshold is 4/5. Please review the constitutional and units standards and re-attempt.`;
            res.className = 'modal-results-box active';
            res.style.background = '#fee2e2';
            res.style.borderColor = '#fecaca';
            res.style.color = '#991b1b';
        }
    }
    </script>
    """
    generate_page("literacy_test.html", "Civic Examination Portal", theme, tab, "Civic Literacy & Naturalization Examination", "Interactive 5-question examination on constitutional virtues and sovereign units", "Academic Board", "Examination Authority", "Testing Active", [{"label": "Examination", "url": "#overview", "active": True}], exam_content, "", "", exam_scripts)
    generate_page("literacy_exam_en.html", "Civic Examination Portal", theme, tab, "Civic Literacy & Naturalization Examination", "Interactive 5-question examination on constitutional virtues and sovereign units", "Academic Board", "Examination Authority", "Testing Active", [{"label": "Examination", "url": "#overview", "active": True}], exam_content, "", "", exam_scripts)

if __name__ == "__main__":
    build_index()
    build_units()
    build_services()
    build_citizenship()
    build_gov_about()
    build_societal_press()
    build_supporting_portals()
    print("All core portal pages successfully generated!")
