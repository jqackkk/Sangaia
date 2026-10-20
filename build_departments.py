#!/usr/bin/env python3
"""
Sangaia Live Department & Entity Pages Generator
Uses canonical structured data from make_departments.py and generate_departments_html.py:
1. Generates the central Departments Overview page for each of the 9 Ministries.
2. Generates a DEDICATED SEPARATE PAGE for each statutory department / entity across all 9 ministries (24 total).
3. Injects all 75 interactive modal tool configurations into each department page with zero discrepancies.
4. Cleaned of all social media features (no status fields, no trending tags, no telemetry widgets).
"""

import os
import json
from make_departments import MINISTRIES
from generate_departments_html import MODAL_CONFIGS
from generate_all_sites import generate_page

MINISTRY_NAV_TABS = {
    "executive": [
        ("home", "executive home", "/executive.html"),
        ("departments", "departments", "/executive_departments.html"),
        ("journal", "aeretocrat's journal", "/executive.html#journal"),
        ("macroeconomics", "macroeconomics & gdp", "/executive.html#macroeconomics"),
        ("budget", "national budget", "/executive.html#national-budget"),
        ("constitution", "constitution & veto", "/executive.html#constitutional-framework"),
        ("calendar", "cabinet calendar", "/executive.html#calendar"),
        ("federal", "← federal portal", "/index.html"),
    ],
    "treasury": [
        ("home", "treasury home", "/treasury.html"),
        ("departments", "departments", "/treasury_departments.html"),
        ("debt-ceiling", "debt ceiling ($0)", "/treasury.html#debt-ceiling"),
        ("loans", "solidarity loans", "/treasury.html#loans"),
        ("budget", "budget ledger", "/treasury.html#fund-allocation"),
        ("electives", "electives salaries", "/treasury.html#electives"),
        ("audits", "check-ins & audits", "/treasury.html#audits"),
        ("federal", "← federal portal", "/index.html"),
    ],
    "work": [
        ("home", "work home", "/work.html"),
        ("departments", "departments", "/work_departments.html"),
        ("wages", "living wage ($25/hr)", "/work.html#wages"),
        ("needs", "labor shortages", "/work.html#needs"),
        ("jobs", "job market", "/work.html#jobs"),
        ("permits", "work permits", "/work.html#work-permits"),
        ("unions", "guild registry", "/work.html#whistleblower"),
        ("federal", "← federal portal", "/index.html"),
    ],
    "healthcare": [
        ("home", "healthcare home", "/healthcare.html"),
        ("departments", "departments", "/healthcare_departments.html"),
        ("services", "medical services", "/healthcare_services.html"),
        ("hospitals", "5-province hospitals", "/healthcare_hospitals.html"),
        ("research", "medical research", "/healthcare_research.html"),
        ("support", "patient support", "/healthcare_support.html"),
        ("ddcr", "ddcr disease control", "/mH/ddcr/index.html"),
        ("federal", "← federal portal", "/index.html"),
    ],
    "education": [
        ("home", "education home", "/education.html"),
        ("departments", "departments", "/education_departments.html"),
        ("textbooks", "open textbooks", "/education.html#textbooks"),
        ("higher-ed", "higher ed & grants", "/education.html#higher-ed"),
        ("schools", "school scorecards", "/education.html#schools"),
        ("teachers", "teacher certifications", "/education.html#teachers"),
        ("federal", "← federal portal", "/index.html"),
    ],
    "domesticaffairs": [
        ("home", "domestic home", "/domesticaffairs.html"),
        ("departments", "departments", "/domesticaffairs_departments.html"),
        ("provincial", "5-provincial relations", "/domesticaffairs.html#provincial-relations"),
        ("trade", "internal common market", "/domesticaffairs.html#provincial-trade"),
        ("accords", "federal accords", "/domesticaffairs.html#federal-interactions"),
        ("transit", "highways & dmv", "/domesticaffairs.html#traffic-roads"),
        ("federal", "← federal portal", "/index.html"),
    ],
    "externalaffairs": [
        ("home", "external home", "/externalaffairs.html"),
        ("departments", "departments", "/externalaffairs_departments.html"),
        ("travel", "travel advisories", "/externalaffairs.html#travel-advisories"),
        ("treaties", "treaties archive", "/externalaffairs.html#treaties"),
        ("embassies", "global embassies", "/externalaffairs.html#embassies"),
        ("visas", "visa services", "/externalaffairs.html#visa-services"),
        ("federal", "← federal portal", "/index.html"),
    ],
    "environment": [
        ("home", "environment home", "/environment.html"),
        ("departments", "departments", "/environment_departments.html"),
        ("services", "eco services", "/environment.html#services"),
        ("biome", "biome funding", "/environment.html#biome-funding"),
        ("wildlife", "wildlife rescue", "/environment.html#wildlife"),
        ("food", "food security", "/environment.html#food-security"),
        ("weather", "weather (°пт)", "/environment.html#weather"),
        ("conservation", "tree planting ledger", "/environment.html#conservation"),
        ("federal", "← federal portal", "/index.html"),
    ],
    "propaganda": [
        ("home", "propaganda home", "/propaganda.html"),
        ("departments", "departments", "/propaganda_departments.html"),
        ("radio", "live radio & broadcast", "/propaganda.html#live-radio"),
        ("tv", "tv & radio directory", "/propaganda.html#channels-directory"),
        ("press", "reporter qualifications", "/propaganda.html#reporter-qualifications"),
        ("churches", "religious audits", "/propaganda.html#churches-registry"),
        ("federal", "← federal portal", "/index.html"),
    ],
}

def get_subdomain_nav_tabs(tabs):
    sub_tabs = []
    for tid, tlabel, turl in tabs:
        if turl.startswith("/index.html") or turl == "/services.html" or turl == "/units.html":
            sub_tabs.append((tid, tlabel, f"https://sangaia.org{turl}"))
        elif turl.endswith("_departments.html"):
            sub_tabs.append((tid, tlabel, "departments.html"))
        elif ".html#" in turl:
            sub_tabs.append((tid, tlabel, turl[turl.find('#'):]))
        elif turl.startswith("/") and turl.endswith(".html"):
            sub_tabs.append((tid, tlabel, "index.html"))
        else:
            sub_tabs.append((tid, tlabel, turl))
    return sub_tabs

EMOJI_TO_MIF = {
    "📜": "mif-description",
    "📥": "mif-inbox",
    "🎖️": "mif-medal",
    "📈": "mif-chart-line",
    "📑": "mif-bookmarks",
    "🤝": "mif-handshake",
    "🧮": "mif-calculator2",
    "⚖️": "mif-balance-scale",
    "🛑": "mif-stop",
    "🏛️": "mif-cabinet",
    "📊": "mif-chart-bars",
    "🔍": "mif-search",
    "📋": "mif-clipboard",
    "🛡️": "mif-security",
    "📚": "mif-books",
    "💼": "mif-suitcase",
    "🪙": "mif-coins",
    "🎓": "mif-school",
    "🛂": "mif-fingerprint",
    "📞": "mif-phone",
    "💳": "mif-credit-card",
    "🏥": "mif-medkit",
    "💊": "mif-injection",
    "🚨": "mif-alarm",
    "🚐": "mif-ambulance",
    "👨‍⚕️": "mif-user-md",
    "🌲": "mif-tree",
    "📻": "mif-broadcast",
    "🌐": "mif-earth",
    "💰": "mif-coins",
    "⚒️": "mif-hammer",
    "🏢": "mif-location-city",
    "⚠️": "mif-warning",
    "🔬": "mif-microscope",
    "🕊️": "mif-earth2",
    "🌱": "mif-nature",
    "💧": "mif-water",
    "🐾": "mif-paw",
    "🚗": "mif-drive",
    "🛣️": "mif-drive-eta",
    "🚆": "mif-subway",
    "🚌": "mif-bus",
    "🛳️": "mif-ship",
    "✈️": "mif-airplane",
    "📺": "mif-tv",
    "📰": "mif-news",
    "⛪": "mif-home",
    "🔔": "mif-bell",
}

def get_mif_icon(raw_icon, size="mif-2x"):
    if raw_icon and raw_icon.startswith("mif-"):
        mif = raw_icon
    else:
        mif = EMOJI_TO_MIF.get(raw_icon.strip() if raw_icon else "", "mif-cabinet")
    return f'<span class="{mif} {size} fg-primary"></span>'

# Modal Dialog HTML Template
MODAL_DIALOG_HTML = """
<div class="ol-modal-overlay" id="interactive-modal-overlay">
    <div class="ol-modal-dialog" id="interactive-modal-window">
        <div class="ol-modal-head">
            <div style="display:flex; align-items:center; gap:8px;">
                <span id="modal-icon" class="mif-cabinet mif-lg fg-primary"></span>
                <span class="ol-modal-title" id="modal-title">interactive service</span>
            </div>
            <button type="button" class="ol-modal-close" id="modal-close-btn">&times;</button>
        </div>
        <div id="modal-dynamic-fields"></div>
        <div class="modal-results-box" id="modal-results-box"></div>
        <div class="ol-modal-foot">
            <button type="button" class="ol-btn" id="modal-cancel-btn">close</button>
            <button type="button" class="ol-btn ol-btn-primary" id="modal-action-btn">submit application</button>
        </div>
    </div>
</div>
"""

# Scripts for Interactive Modal Tools
EXTRA_SCRIPTS_TEMPLATE = """
<script>
const MODAL_CONFIGS = {modal_configs_json};
const EMOJI_MAP = {{
    "📜": "mif-description",
    "📥": "mif-inbox",
    "🎖️": "mif-medal",
    "📈": "mif-chart-line",
    "📑": "mif-bookmarks",
    "🤝": "mif-handshake",
    "🧮": "mif-calculator2",
    "⚖️": "mif-balance-scale",
    "🛑": "mif-stop",
    "🏛️": "mif-cabinet",
    "📊": "mif-chart-bars",
    "🔍": "mif-search",
    "📋": "mif-clipboard",
    "🛡️": "mif-security",
    "📚": "mif-books",
    "💼": "mif-suitcase",
    "🪙": "mif-coins",
    "🎓": "mif-school",
    "🛂": "mif-fingerprint",
    "📞": "mif-phone",
    "💳": "mif-credit-card",
    "🏥": "mif-medkit",
    "💊": "mif-injection",
    "🚨": "mif-alarm",
    "🚐": "mif-ambulance",
    "👨‍⚕️": "mif-user-md",
    "🌲": "mif-tree",
    "📻": "mif-broadcast",
    "🌐": "mif-earth",
    "💰": "mif-coins",
    "⚒️": "mif-hammer",
    "🏢": "mif-location-city",
    "⚠️": "mif-warning",
    "🔬": "mif-microscope"
}};

document.addEventListener('DOMContentLoaded', () => {{
    const modalOverlay = document.getElementById('interactive-modal-overlay');
    const modalCloseBtn = document.getElementById('modal-close-btn');
    const modalCancelBtn = document.getElementById('modal-cancel-btn');
    const modalActionBtn = document.getElementById('modal-action-btn');
    const modalIcon = document.getElementById('modal-icon');
    const modalTitle = document.getElementById('modal-title');
    const modalDynamicFields = document.getElementById('modal-dynamic-fields');
    const modalResultsBox = document.getElementById('modal-results-box');
    const searchInput = document.getElementById('dept-search-input');

    let activeModalConfig = null;
    let activeModalId = null;

    if (searchInput) {{
        searchInput.addEventListener('input', (e) => {{
            const q = e.target.value.toLowerCase().trim();
            const depts = document.querySelectorAll('.dept-container');
            depts.forEach(d => {{
                const text = d.innerText.toLowerCase();
                d.style.display = (!q || text.includes(q)) ? 'block' : 'none';
            }});
        }});
    }}

    function openModal(modalId) {{
        const cfg = MODAL_CONFIGS[modalId];
        if (!cfg) return;
        activeModalConfig = cfg;
        activeModalId = modalId;

        const mifClass = (cfg.icon && cfg.icon.startsWith('mif-')) ? cfg.icon : (EMOJI_MAP[cfg.icon] || 'mif-cabinet');
        modalIcon.className = mifClass + ' mif-lg fg-primary';
        modalIcon.innerText = '';
        modalTitle.innerText = (cfg.title_en || 'service portal').toLowerCase();
        modalResultsBox.classList.remove('active');
        modalResultsBox.innerHTML = '';
        modalActionBtn.innerText = (cfg.action_en || 'submit').toLowerCase();

        let fieldsHtml = '';
        if (cfg.fields && cfg.fields.length > 0) {{
            cfg.fields.forEach(f => {{
                fieldsHtml += `<div class="form-group" style="margin-bottom:12px;">`;
                fieldsHtml += `<label class="form-label" style="display:block; font-size:12px; font-weight:600; margin-bottom:4px;">${{f.label_en}}</label>`;
                if (f.type === 'select') {{
                    fieldsHtml += `<select class="ol-select" id="input-${{f.id}}" style="width:100%;">`;
                    (f.options_en || []).forEach(opt => {{
                        fieldsHtml += `<option value="${{opt}}">${{opt}}</option>`;
                    }});
                    fieldsHtml += `</select>`;
                }} else if (f.type === 'textarea') {{
                    fieldsHtml += `<textarea class="ol-textarea" id="input-${{f.id}}" rows="3" placeholder="${{f.placeholder_en || ''}}" style="width:100%;"></textarea>`;
                }} else {{
                    fieldsHtml += `<input type="${{f.type || 'text'}}" class="ol-input" id="input-${{f.id}}" placeholder="${{f.placeholder_en || ''}}" style="width:100%;">`;
                }}
                fieldsHtml += `</div>`;
            }});
        }} else {{
            fieldsHtml = `<p class="ol-small ol-muted">Instant cryptographic verification enabled. Click below to execute.</p>`;
        }}

        modalDynamicFields.innerHTML = fieldsHtml;
        modalOverlay.classList.add('active');
    }}

    function closeModal() {{
        modalOverlay.classList.remove('active');
    }}

    if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeModal);
    if (modalCancelBtn) modalCancelBtn.addEventListener('click', closeModal);
    modalOverlay.addEventListener('click', (e) => {{
        if (e.target === modalOverlay) closeModal();
    }});

    document.querySelectorAll('.open-modal-btn').forEach(btn => {{
        btn.addEventListener('click', () => {{
            openModal(btn.getAttribute('data-modal'));
        }});
    }});

    if (modalActionBtn) {{
        modalActionBtn.addEventListener('click', () => {{
            if (!activeModalConfig) return;
            const cfg = activeModalConfig;

            if (activeModalId === 'taxcalc') {{
                const inc = parseFloat((document.getElementById('input-income') || {{}}).value) || 0;
                const ent = (document.getElementById('input-type') || {{}}).value;
                let rate = 0.12;
                if (ent === 'corp') rate = 0.18;
                else if (ent === 'resource') rate = 0.22;
                const tax = inc * rate;
                const net = inc - tax;

                modalResultsBox.innerHTML = `
                    <div style="font-weight:700; margin-bottom:6px; color:#166534;">Statutory Tax Assessment Calculated:</div>
                    <div>Assessed Revenue Base: <strong>$ ${{inc.toLocaleString()}}</strong></div>
                    <div>Statutory Effective Rate: <strong>${{(rate * 100).toFixed(1)}}%</strong></div>
                    <div>Mandatory Sovereign Remittance: <strong>$ ${{tax.toLocaleString()}}</strong></div>
                    <div>Net Retained Capital: <strong>$ ${{net.toLocaleString()}}</strong></div>
                    <div class="ol-small ol-muted" style="margin-top:6px;">Reference Code: SNG-TAX-${{Math.floor(100000 + Math.random() * 900000)}}</div>
                `;
                modalResultsBox.classList.add('active');
                return;
            }}

            const token = (cfg.token_prefix || 'SNG-STAT') + '-' + Math.floor(100000 + Math.random() * 900000);
            let sampleHtml = '';
            if (cfg.sample_results_en && cfg.sample_results_en.length > 0) {{
                sampleHtml = '<div style=\"margin-top:8px;\"><strong>Recent Official Records:</strong><ul style=\"margin:4px 0 0 16px;\">';
                cfg.sample_results_en.slice(0, 3).forEach(s => {{
                    sampleHtml += `<li><strong>${{s.title || ''}}:</strong> ${{s.desc || s.date || ''}}</li>`;
                }});
                sampleHtml += '</ul></div>';
            }}

            modalResultsBox.innerHTML = `
                <div style="font-weight:700; margin-bottom:6px; color:#166534;">Official Sovereign Docket Generated</div>
                <div>Statutory Authorization Token: <span style="font-family:monospace; font-weight:700;">${{token}}</span></div>
                <div>Processing Authority: <strong>${{cfg.title_en || 'Federal Directorate'}}</strong></div>
                <div>Status: <span class="ol-badge-tag ol-badge-success">confirmed &bull; recorded in societal press</span></div>
                ${{sampleHtml}}
            `;
            modalResultsBox.classList.add('active');
        }});
    }}
}});
</script>
"""

def build_all_ministry_departments():
    modal_configs_json = json.dumps(MODAL_CONFIGS)
    extra_scripts = EXTRA_SCRIPTS_TEMPLATE.format(modal_configs_json=modal_configs_json)

    for mkey, m in MINISTRIES.items():
        theme_class = f"theme-{mkey}"
        ministry_title = m["ministry_en"]
        home_url = f"/{m['root_file']}"
        dept_hub_file = f"{mkey}_departments.html"

        target_dirs = m.get("target_dirs", [])
        departments = m.get("departments", [])

        nav_tabs = MINISTRY_NAV_TABS.get(mkey)
        sub_nav_tabs = get_subdomain_nav_tabs(nav_tabs) if nav_tabs else None

        # Build Sidenav links for the departments overview
        overview_sidebar_links = [
            {"label": f"← {ministry_title} Home", "url": home_url, "active": False},
            {"label": "Overview & Search", "url": "#overview", "active": True}
        ]

        # Prepare department entries
        dept_entries = []
        for d in departments:
            dept_id = d["id"]
            clean_id = dept_id.replace('-', '_')
            if mkey == "healthcare" and clean_id == "hospitals":
                clean_id = "hospitals_dept"
            dept_file = f"{mkey}_{clean_id}.html"
            short_name = d["name_en"].replace("Department of ", "").replace("Department & ", "")
            overview_sidebar_links.append({
                "label": f"Dept: {short_name}",
                "url": f"#{dept_id}",
                "active": False
            })
            dept_entries.append({
                "id": dept_id,
                "clean_id": clean_id,
                "file": dept_file,
                "title": d["name_en"],
                "short_name": short_name,
                "mandate": d["mandate_en"],
                "functions": d["functions"]
            })

        # -------------------------------------------------------------
        # 1. Build Overview Hub Page ([ministry]_departments.html)
        # -------------------------------------------------------------
        hub_cards = []
        hub_cards.append(f"""
        <div class="ol-card" id="overview">
            <div class="ol-card-title">
                <span>Find Statutory Services &amp; Dedicated Entity Portals</span>
                <span class="ol-badge-tag">{len(departments)} Entities Active</span>
            </div>
            <p class="ol-small ol-muted">Instant keyword search across statutory mandates, citizen registries, calculators, and official filing portals of the {ministry_title}.</p>
            <input type="text" class="ol-input" id="dept-search-input" placeholder="Type department name, service title, or keyword..." style="margin-top:6px;">
        </div>
        """)

        for d in dept_entries:
            func_cards = ""
            for f in d["functions"]:
                icon = f.get("icon", "🏛️")
                ftitle = f.get("title_en", "Service")
                fdesc = f.get("desc_en", "")
                modal_id = f.get("modal", "")

                func_cards += f"""
                <div class="ol-card func-item-box" style="margin-bottom:0; background:#fbfcfd; border:1px solid #dfe3e7;">
                    <div style="display:flex; align-items:flex-start; gap:12px;">
                        <div style="line-height:1;">{get_mif_icon(icon, 'mif-2x')}</div>
                        <div style="flex:1 1 auto; min-width:0;">
                            <strong style="color:#1e293b; font-size:13.5px; display:block; margin-bottom:4px;">{ftitle.lower()}</strong>
                            <p class="ol-small ol-muted" style="margin-bottom:10px; line-height:1.4;">{fdesc}</p>
                            <button type="button" class="ol-btn ol-btn-primary ol-btn-sm open-modal-btn" data-modal="{modal_id}">
                                launch service &rarr;
                            </button>
                        </div>
                    </div>
                </div>
                """

            hub_cards.append(f"""
            <div class="ol-card dept-container" id="{d['id']}">
                <div class="ol-card-title">
                    <span><span class="mif-location-city mif-lg fg-primary"></span> {d['title'].lower()}</span>
                    <a class="ol-title-link" href="/{d['file']}" style="font-weight:600;">open dedicated page &rarr;</a>
                </div>
                <div class="ol-note" style="margin-bottom:14px;">
                    <strong>constitutional mandate:</strong> {d['mandate']}
                </div>
                <div class="ol-grid-2">
                    {func_cards}
                </div>
                <div style="margin-top:12px; padding-top:10px; border-top:1px solid #e1dfdd; display:flex; justify-content:space-between; align-items:center;">
                    <span class="ol-small ol-muted">official entity id: {d['id']}</span>
                    <a href="/{d['file']}" class="ol-btn ol-btn-sm">view standalone {d['short_name'].lower()} portal &rarr;</a>
                </div>
            </div>
            """)

        hub_main_content = "\n".join(hub_cards)

        hub_sidebar_right = f"""
        <div class="ol-sidebox">
            <h3>{ministry_title}</h3>
            <p class="ol-small ol-muted">All services operate under federal statutory oversight. Applications are cryptographically authenticated via Sangaia ID.</p>
            <div style="margin-top:10px;">
                <a href="{home_url}" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Return to Ministry Portal</a>
            </div>
        </div>
        """

        # Generate root hub file
        generate_page(
            filename=dept_hub_file,
            title=f"{ministry_title} Departments",
            theme_class=theme_class,
            active_tab="departments",
            hero_title=ministry_title,
            hero_sub=f"Statutory Directorates, Executive Decrees & State Administration &bull; {ministry_title}",
            sidebar_title=ministry_title,
            sidebar_subtitle="Statutory Authority",
            sidebar_status="Directorate Active",
            sidebar_nav_links=overview_sidebar_links,
            main_content_html=hub_main_content,
            sidebar_right_extra_html=hub_sidebar_right,
            modal_dialog_html=MODAL_DIALOG_HTML,
            extra_scripts=extra_scripts,
            custom_nav_tabs=nav_tabs
        )

        # Generate subdomain mirror for hub file
        for tdir in target_dirs:
            sub_hub_path = os.path.join(tdir, "departments.html")
            generate_page(
                filename=sub_hub_path,
                title=f"{ministry_title} Departments",
                theme_class=theme_class,
                active_tab="departments",
                hero_title=ministry_title,
                hero_sub=f"Statutory Directorates, Executive Decrees & State Administration &bull; {ministry_title}",
                sidebar_title=ministry_title,
                sidebar_subtitle="Statutory Authority",
                sidebar_status="Directorate Active",
                sidebar_nav_links=overview_sidebar_links,
                main_content_html=hub_main_content,
                sidebar_right_extra_html=hub_sidebar_right,
                modal_dialog_html=MODAL_DIALOG_HTML,
                extra_scripts=extra_scripts,
                custom_nav_tabs=sub_nav_tabs
            )

        # -------------------------------------------------------------
        # 2. Build SEPARATE DEDICATED PAGES for each entity (department)
        # -------------------------------------------------------------
        for d in dept_entries:
            dept_title = d["title"]
            dept_file = d["file"]
            clean_id = d["clean_id"]

            func_cards = ""
            for f in d["functions"]:
                icon = f.get("icon", "🏛️")
                ftitle = f.get("title_en", "Service")
                fdesc = f.get("desc_en", "")
                modal_id = f.get("modal", "")

                func_cards += f"""
                <div class="ol-card func-item-box" style="margin-bottom:0; background:#fbfcfd; border:1px solid #dfe3e7; padding:16px;">
                    <div style="display:flex; align-items:flex-start; gap:14px;">
                        <div style="line-height:1;">{get_mif_icon(icon, 'mif-2x')}</div>
                        <div style="flex:1 1 auto; min-width:0;">
                            <h3 style="color:#1e293b; font-size:15px; margin-bottom:6px;">{ftitle.lower()}</h3>
                            <p class="ol-small ol-muted" style="margin-bottom:12px; line-height:1.5;">{fdesc}</p>
                            <button type="button" class="ol-btn ol-btn-primary ol-btn-sm open-modal-btn" data-modal="{modal_id}">
                                launch interactive service &rarr;
                            </button>
                        </div>
                    </div>
                </div>
                """

            sister_links = [
                {"label": f"← all {ministry_title} departments", "url": f"/{dept_hub_file}", "active": False},
                {"label": f"← {ministry_title} home", "url": home_url, "active": False},
            ]
            for s in dept_entries:
                sister_links.append({
                    "label": f"dept: {s['short_name'].lower()}",
                    "url": f"/{s['file']}",
                    "active": (s["id"] == d["id"])
                })

            dedicated_main_html = f"""
            <div class="ol-card">
                <div class="ol-card-title">
                    <span><span class="mif-location-city mif-lg fg-primary"></span> {dept_title.lower()}</span>
                    <span class="ol-badge-tag ol-badge-success">statutory authority active</span>
                </div>
                <div class="ol-note" style="margin-bottom:14px;">
                    <strong>official constitutional mandate:</strong> {d['mandate']}
                </div>
                <p class="ol-small">this department operates under sovereign jurisdiction across all 5 provinces: new jasper, new madison, liveland, sentinel, and columbia. all services are governed by statutory standards, guaranteed zero sovereign commercial debt, and integrated with sangaia id cryptographic authentication.</p>
            </div>

            <div class="ol-card">
                <div class="ol-card-title">
                    <span>Operational Functions &amp; Citizen Service Engines</span>
                    <span class="ol-badge-tag">{len(d['functions'])} Active Portals</span>
                </div>
                <p class="ol-small ol-muted" style="margin-bottom:14px;">Select any operational service below to initiate interactive forms, cryptographic dockets, and instant statutory verifications.</p>
                <div style="display:flex; flex-direction:column; gap:12px;">
                    {func_cards}
                </div>
            </div>

            <div class="ol-card" style="font-size:12.5px; line-height:1.6;">
                <div class="ol-card-title">
                    <span>Directorate Administration &amp; Public Inquiries</span>
                </div>
                <div><strong>Executive Directorate:</strong> Sovereign Administrative District, Central Capital</div>
                <div><strong>Operating Hours:</strong> Monday – Friday, 08:00 – 17:00 (State Calendar)</div>
                <div><strong>Service Level Guarantee:</strong> 10-Day Statutory Review Window for all dockets</div>
                <div><strong>Authentication Standard:</strong> Aretocratic Cryptographic Seal Verified</div>
            </div>
            """

            dedicated_sidebar_right = f"""
            <div class="ol-sidebox">
                <h3>{ministry_title}</h3>
                <p class="ol-small ol-muted">Parent ministry portal with sovereign telemetry, executive blog, and full public services catalog.</p>
                <div class="ol-mt-10">
                    <a href="{home_url}" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Open Ministry Home</a>
                    <a href="/{dept_hub_file}" class="ol-btn ol-btn-sm" style="width:100%; text-align:center; margin-top:6px;">All Departments Hub</a>
                </div>
            </div>
            """

            # Generate root separate page
            generate_page(
                filename=dept_file,
                title=f"{dept_title} :: {ministry_title}",
                theme_class=theme_class,
                active_tab="departments",
                hero_title=dept_title,
                hero_sub=f"Statutory Federal Department &bull; {ministry_title}",
                sidebar_title=dept_title,
                sidebar_subtitle="Statutory Authority",
                sidebar_status="Operational",
                sidebar_nav_links=sister_links,
                main_content_html=dedicated_main_html,
                sidebar_right_extra_html=dedicated_sidebar_right,
                modal_dialog_html=MODAL_DIALOG_HTML,
                extra_scripts=extra_scripts,
                custom_nav_tabs=nav_tabs
            )

            # Generate subdomain separate page
            for tdir in target_dirs:
                sub_dept_file = os.path.join(tdir, f"{clean_id}.html")
                sub_sister_links = [
                    {"label": f"← All {ministry_title} Departments", "url": "departments.html", "active": False},
                    {"label": f"← {ministry_title} Home", "url": "index.html", "active": False},
                ]
                for s in dept_entries:
                    sub_sister_links.append({
                        "label": f"Dept: {s['short_name']}",
                        "url": f"{s['clean_id']}.html",
                        "active": (s["id"] == d["id"])
                    })

                generate_page(
                    filename=sub_dept_file,
                    title=f"{dept_title} :: {ministry_title}",
                    theme_class=theme_class,
                    active_tab="departments",
                    hero_title=dept_title,
                    hero_sub=f"Statutory Federal Department &bull; {ministry_title}",
                    sidebar_title=dept_title,
                    sidebar_subtitle="Statutory Authority",
                    sidebar_status="Operational",
                    sidebar_nav_links=sub_sister_links,
                    main_content_html=dedicated_main_html,
                    sidebar_right_extra_html=dedicated_sidebar_right,
                    modal_dialog_html=MODAL_DIALOG_HTML,
                    extra_scripts=extra_scripts,
                    custom_nav_tabs=sub_nav_tabs
                )

    print("All 9 ministry department overview hubs and all 24 dedicated entity pages generated successfully!")

if __name__ == "__main__":
    build_all_ministry_departments()
