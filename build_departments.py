#!/usr/bin/env python3
"""
Sangaia Live Department Pages Generator
Re-architects all 9 department portal pages into the exact One Live Wave 4 architecture.
"""

import os
import re

DEPT_SPECS = [
    {
        "file": "executive_departments.html",
        "theme": "theme-executive",
        "tab": "executive",
        "ministry": "Ministry of the Executive",
        "sub": "Statutory Directorates, Executive Decrees & State Administration",
        "role": "Executive Administration",
        "home_url": "/executive.html",
        "subdomain_dir": "MoEX",
        "subdomain_alt": "mEx"
    },
    {
        "file": "treasury_departments.html",
        "theme": "theme-treasury",
        "tab": "treasury",
        "ministry": "Ministry of the Treasury",
        "sub": "Fiscal Management, Sovereign Borrowing, Taxation & Procurement",
        "role": "Fiscal Authority",
        "home_url": "/treasury.html",
        "subdomain_dir": "mT",
        "subdomain_alt": None
    },
    {
        "file": "work_departments.html",
        "theme": "theme-work",
        "tab": "work",
        "ministry": "Ministry of Work",
        "sub": "Labor Standards, Worker Protections, Employment Safety & Guilds",
        "role": "Labor Authority",
        "home_url": "/work.html",
        "subdomain_dir": "mW",
        "subdomain_alt": None
    },
    {
        "file": "healthcare_departments.html",
        "theme": "theme-healthcare",
        "tab": "healthcare",
        "ministry": "Ministry of Healthcare",
        "sub": "Universal Coverage, Hospital Capacity, Emergency Dispatch & CDC",
        "role": "Universal Health Authority",
        "home_url": "/healthcare.html",
        "subdomain_dir": "mH",
        "subdomain_alt": None
    },
    {
        "file": "education_departments.html",
        "theme": "theme-education",
        "tab": "education",
        "ministry": "Ministry of Education",
        "sub": "National Curriculum, Digital Textbooks, Higher Education & Grants",
        "role": "Academic Authority",
        "home_url": "/education.html",
        "subdomain_dir": "mE",
        "subdomain_alt": "mEd"
    },
    {
        "file": "domesticaffairs_departments.html",
        "theme": "theme-domestic",
        "tab": "domestic",
        "ministry": "Ministry of Domestic Affairs",
        "sub": "Provincial Relations, Interstate Trade, Federal Coordination & Transit",
        "role": "Internal Governance",
        "home_url": "/domesticaffairs.html",
        "subdomain_dir": "MiA",
        "subdomain_alt": None
    },
    {
        "file": "externalaffairs_departments.html",
        "theme": "theme-external",
        "tab": "external",
        "ministry": "Ministry of External Affairs",
        "sub": "Worldwide Travel Advisories, Sovereign Treaties, Embassies & Protocol",
        "role": "Foreign Service & Diplomatic Corp",
        "home_url": "/externalaffairs.html",
        "subdomain_dir": "MdA",
        "subdomain_alt": None
    },
    {
        "file": "environment_departments.html",
        "theme": "theme-environment",
        "tab": "environment",
        "ministry": "Ministry of the Environment",
        "sub": "Atmospheric Telemetry (°Пт), Biome Funding, Wildlife Intervention & Conservation",
        "role": "Ecological Stewardship",
        "home_url": "/environment.html",
        "subdomain_dir": "MtE",
        "subdomain_alt": "mEnv"
    },
    {
        "file": "propaganda_departments.html",
        "theme": "theme-propaganda",
        "tab": "propaganda",
        "ministry": "Ministry of Propaganda",
        "sub": "Civic Broadcasting, Live Audio Streaming, Press Accreditation & Churches",
        "role": "Civic Information Authority",
        "home_url": "/propaganda.html",
        "subdomain_dir": "mP",
        "subdomain_alt": None
    }
]

def build_dept_page(spec):
    src_file = spec["file"]
    with open(src_file, 'r', encoding='utf-8') as f:
        src_txt = f.read()

    # Extract MODAL_CONFIGS
    m_cfg = re.search(r'const MODAL_CONFIGS\s*=\s*(\{.*?\});', src_txt, re.DOTALL)
    modal_configs_js = m_cfg.group(0) if m_cfg else "const MODAL_CONFIGS = {};"

    # Extract sections
    sections = re.findall(r'<section class=\"dept-card\" id=\"([^\"]+)\">(.*?)</section>', src_txt, re.DOTALL)

    # Build Left Sidenav Links
    sidebar_nav_links = [
        {"label": f"← {spec['ministry']} Home", "url": spec["home_url"], "active": False},
        {"label": "Overview & Search", "url": "#overview", "active": True}
    ]
    for sid, shtml in sections:
        dtitle_match = re.search(r'<h2 class=\"dept-title\">(.*?)</h2>', shtml)
        dtitle = dtitle_match.group(1).strip() if dtitle_match else sid
        # Shorten label for sidenav
        short_title = dtitle.replace("Department of ", "").replace("Department & ", "")
        sidebar_nav_links.append({"label": f"Dept: {short_title}", "url": f"#{sid}", "active": False})

    # Build Main Content Cards
    content_cards = []
    
    # 1. Search card
    content_cards.append(f"""
    <div class="ol-card" id="overview">
        <div class="ol-card-title">
            <span>Find Statutory Services &amp; Interactive Portals</span>
            <span class="ol-badge-tag">{len(sections)} Departments Active</span>
        </div>
        <p class="ol-small ol-muted">Instant keyword search across statutory mandates, citizen registries, calculators, and official filing portals.</p>
        <input type="text" class="ol-input" id="dept-search-input" placeholder="Type department name, service title, or keyword..." style="margin-top:6px;">
    </div>
    """)

    # 2. Department Cards
    for sid, shtml in sections:
        dtitle = re.search(r'<h2 class=\"dept-title\">(.*?)</h2>', shtml).group(1).strip()
        mandate = re.search(r'<p class=\"mandate-text\">(.*?)</p>', shtml).group(1).strip()
        funcs = re.findall(r'<div class=\"function-card\">.*?<div class=\"func-icon-wrap\">(.*?)</div>.*?<h3 class=\"func-title\">(.*?)</h3>.*?<p class=\"func-desc\">(.*?)</p>.*?data-modal=\"([^\"]+)\"', shtml, re.DOTALL)

        func_cards_html = ""
        for icon, ftitle, fdesc, modal_id in funcs:
            func_cards_html += f"""
            <div class="ol-card func-item-box" style="margin-bottom:0; background:#fbfcfd; border:1px solid #dfe3e7;">
                <div style="display:flex; align-items:flex-start; gap:12px;">
                    <div style="font-size:26px; line-height:1;">{icon.strip()}</div>
                    <div style="flex:1 1 auto; min-width:0;">
                        <strong style="color:#1e293b; font-size:13.5px; display:block; margin-bottom:4px;">{ftitle.strip()}</strong>
                        <p class="ol-small ol-muted" style="margin-bottom:10px; line-height:1.4;">{fdesc.strip()}</p>
                        <button type="button" class="ol-btn ol-btn-primary ol-btn-sm open-modal-btn" data-modal="{modal_id}">
                            Launch Service &rarr;
                        </button>
                    </div>
                </div>
            </div>
            """

        content_cards.append(f"""
        <div class="ol-card dept-container" id="{sid}">
            <div class="ol-card-title">
                <span>🏢 {dtitle}</span>
                <a class="ol-title-link" href="#overview">Top ↑</a>
            </div>
            <div class="ol-note" style="margin-bottom:14px;">
                <strong>Constitutional Mandate:</strong> {mandate}
            </div>
            <div class="ol-grid-2">
                {func_cards_html}
            </div>
        </div>
        """)

    main_content_html = "\n".join(content_cards)

    # Right Sidebar Content
    sidebar_right_html = f"""
    <div class="ol-sidebox">
        <h3>Department Overview</h3>
        <p class="ol-small ol-muted">All services operate under federal statutory oversight of the {spec['ministry']}. Applications are cryptographically authenticated via Sangaia ID.</p>
        <div style="margin-top:10px;">
            <a href="{spec['home_url']}" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Return to Ministry Portal</a>
        </div>
    </div>
    """

    # Modal Dialog HTML
    modal_dialog_html = """
    <!-- Standardized One Live Wave 4 Modal Dialog -->
    <div class="ol-modal-overlay" id="interactive-modal-overlay">
        <div class="ol-modal-dialog" id="interactive-modal-window">
            <div class="ol-modal-head">
                <div style="display:flex; align-items:center; gap:8px;">
                    <span id="modal-icon" style="font-size:20px;">🏛️</span>
                    <span class="ol-modal-title" id="modal-title">Interactive Service</span>
                </div>
                <button type="button" class="ol-modal-close" id="modal-close-btn">&times;</button>
            </div>
            <div id="modal-dynamic-fields"></div>
            <div class="modal-results-box" id="modal-results-box"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" id="modal-cancel-btn">Close</button>
                <button type="button" class="ol-btn ol-btn-primary" id="modal-action-btn">Submit Application</button>
            </div>
        </div>
    </div>
    """

    # Scripts HTML
    extra_scripts = f"""
    <script>
    // Injected Statutory Modal Configs
    {modal_configs_js}

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

        // Instant Page Search Filter
        if (searchInput) {{
            searchInput.addEventListener('input', (e) => {{
                const q = e.target.value.toLowerCase().trim();
                const depts = document.querySelectorAll('.dept-container');
                depts.forEach(d => {{
                    const text = d.innerText.toLowerCase();
                    if (!q || text.includes(q)) {{
                        d.style.display = 'block';
                        const items = d.querySelectorAll('.func-item-box');
                        items.forEach(it => {{
                            if (!q || it.innerText.toLowerCase().includes(q)) {{
                                it.style.display = 'block';
                            }} else {{
                                it.style.display = 'none';
                            }}
                        }});
                    }} else {{
                        d.style.display = 'none';
                    }}
                }});
            }});
        }}

        function openModal(modalId) {{
            const cfg = MODAL_CONFIGS[modalId];
            if (!cfg) return;

            activeModalId = modalId;
            activeModalConfig = cfg;

            modalResultsBox.classList.remove('active');
            modalResultsBox.innerHTML = '';
            modalDynamicFields.innerHTML = '';

            modalIcon.textContent = cfg.icon || '🏛️';
            modalTitle.textContent = cfg.title_en || 'Statutory Portal';
            modalActionBtn.textContent = cfg.action_en || 'Submit';

            // Fields
            if (cfg.fields && cfg.fields.length > 0) {{
                cfg.fields.forEach(f => {{
                    const grp = document.createElement('div');
                    grp.className = 'form-group';
                    const lbl = document.createElement('label');
                    lbl.className = 'form-label';
                    lbl.textContent = f.label_en || f.name;
                    grp.appendChild(lbl);

                    if (f.type === 'select') {{
                        const sel = document.createElement('select');
                        sel.className = 'ol-select';
                        sel.id = `input-${{f.name}}`;
                        (f.options || []).forEach(opt => {{
                            const op = document.createElement('option');
                            op.value = opt.val;
                            op.textContent = opt.en || opt.val;
                            sel.appendChild(op);
                        }});
                        grp.appendChild(sel);
                    }} else if (f.type === 'textarea') {{
                        const ta = document.createElement('textarea');
                        ta.className = 'ol-textarea';
                        ta.id = `input-${{f.name}}`;
                        ta.placeholder = f.placeholder_en || '';
                        ta.rows = 3;
                        grp.appendChild(ta);
                    }} else {{
                        const inp = document.createElement('input');
                        inp.type = f.type || 'text';
                        inp.className = 'ol-input';
                        inp.id = `input-${{f.name}}`;
                        if (f.default !== undefined) inp.value = f.default;
                        inp.placeholder = f.placeholder_en || '';
                        grp.appendChild(inp);
                    }}
                    modalDynamicFields.appendChild(grp);
                }});
            }}

            // Telemetry Metrics
            if (cfg.metrics && cfg.metrics.length > 0) {{
                const grid = document.createElement('div');
                grid.className = 'modal-telemetry-grid';
                cfg.metrics.forEach(m => {{
                    const card = document.createElement('div');
                    card.className = 'telemetry-card';
                    card.innerHTML = `
                        <div class="telemetry-name">${{m.name_en || ''}}</div>
                        <div class="telemetry-val">${{m.val || ''}}</div>
                        <div class="telemetry-sub">${{m.sub_en || ''}}</div>
                    `;
                    grid.appendChild(card);
                }});
                modalDynamicFields.appendChild(grid);
            }}

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

        // Bind Launch Buttons
        document.querySelectorAll('.open-modal-btn').forEach(btn => {{
            btn.addEventListener('click', () => {{
                openModal(btn.getAttribute('data-modal'));
            }});
        }});

        // Action submit logic
        if (modalActionBtn) {{
            modalActionBtn.addEventListener('click', () => {{
                if (!activeModalConfig) return;
                const cfg = activeModalConfig;

                // Tax Calculator
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

                // Generic simulated submission
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
                    <div>Status: <span class="ol-badge-tag ol-badge-success">CONFIRMED &bull; RECORDED IN GAZETTE</span></div>
                    ${{sampleHtml}}
                `;
                modalResultsBox.classList.add('active');
            }});
        }}
    }});
    </script>
    """

    from generate_all_sites import generate_page
    # Generate root department file
    generate_page(
        filename=src_file,
        title=f"{spec['ministry']} Departments",
        theme_class=spec["theme"],
        active_tab=spec["tab"],
        hero_title=spec["ministry"],
        hero_sub=spec["sub"],
        sidebar_title=spec["ministry"],
        sidebar_subtitle=spec["role"],
        sidebar_status="Directorate Active",
        sidebar_nav_links=sidebar_nav_links,
        main_content_html=main_content_html,
        sidebar_right_extra_html=sidebar_right_html,
        modal_dialog_html=modal_dialog_html,
        extra_scripts=extra_scripts
    )

    # Subdomain mirror
    if spec["subdomain_dir"]:
        sub_path = os.path.join(spec["subdomain_dir"], "departments.html")
        generate_page(
            filename=sub_path,
            title=f"{spec['ministry']} Departments",
            theme_class=spec["theme"],
            active_tab=spec["tab"],
            hero_title=spec["ministry"],
            hero_sub=spec["sub"],
            sidebar_title=spec["ministry"],
            sidebar_subtitle=spec["role"],
            sidebar_status="Directorate Active",
            sidebar_nav_links=sidebar_nav_links,
            main_content_html=main_content_html,
            sidebar_right_extra_html=sidebar_right_html,
            modal_dialog_html=modal_dialog_html,
            extra_scripts=extra_scripts
        )

    if spec["subdomain_alt"]:
        alt_path = os.path.join(spec["subdomain_alt"], "departments.html")
        generate_page(
            filename=alt_path,
            title=f"{spec['ministry']} Departments",
            theme_class=spec["theme"],
            active_tab=spec["tab"],
            hero_title=spec["ministry"],
            hero_sub=spec["sub"],
            sidebar_title=spec["ministry"],
            sidebar_subtitle=spec["role"],
            sidebar_status="Directorate Active",
            sidebar_nav_links=sidebar_nav_links,
            main_content_html=main_content_html,
            sidebar_right_extra_html=sidebar_right_html,
            modal_dialog_html=modal_dialog_html,
            extra_scripts=extra_scripts
        )

if __name__ == "__main__":
    for s in DEPT_SPECS:
        build_dept_page(s)
    print("All 9 department portals successfully rebuilt in One Live Wave 4 architecture!")
