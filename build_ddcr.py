#!/usr/bin/env python3
"""
DDCR (Department of Disease Control & Research) Portal Generator
Builds the DDCR pages in the exact One Live Wave 4 architecture:
- mH/ddcr/index.html
- mH/ddcr/health_topics.html
- mH/ddcr/outbreaks.html
- mH/ddcr/search.html
- mH/ddcr/article.html
"""

import os
from generate_all_sites import generate_page

DDCR_DIR = "mH/ddcr"

def build_ddcr_index():
    main_content = """
    <div class="card">
        <h2>Department of Disease Control &amp; Research</h2>
        <p>The DDCR serves as Sangaia's primary sovereign defense against infectious diseases, epidemic threats, and public health emergencies. Through proactive containment, genomic tracking, and clinical research, we safeguard the health of all five provinces.</p>
    </div>

    <div class="card">
        <h2>Pioneering Medical Solutions &bull; Provincial Health Defense</h2>
        <p>Our research laboratories and polyclinic networks coordinate directly with provincial health authorities to deploy real-time epidemiology, emergency vaccine stockpiles, and updated clinical protocols.</p>
        <div style="display:flex; flex-wrap:wrap; gap:10px; margin-top:14px;">
            <a href="/mH/ddcr/health_topics.html" class="btn btn-primary"><span class="mif-medkit"></span> Explore Health Topics (A-Z)</a>
            <a href="/mH/ddcr/search.html" class="btn btn-secondary"><span class="mif-search"></span> Search Research Database</a>
            <a href="/mH/ddcr/outbreaks.html" class="btn btn-outline"><span class="mif-warning"></span> Active Outbreaks &amp; Protocols</a>
        </div>
    </div>

    <div class="card">
        <h3>Active Pathogen Surveillance &bull; 5 Provinces</h3>
        <div class="telemetry-grid">
            <div class="metric-box">
                <div class="metric-val">Tier 1</div>
                <div class="metric-lbl">Alert Status</div>
            </div>
            <div class="metric-box">
                <div class="metric-val">0.02%</div>
                <div class="metric-lbl">Outpatient Influx</div>
            </div>
            <div class="metric-box">
                <div class="metric-val">100%</div>
                <div class="metric-lbl">Antiviral Reserves</div>
            </div>
            <div class="metric-box">
                <div class="metric-val">18</div>
                <div class="metric-lbl">Genomic Labs</div>
            </div>
        </div>
    </div>
    """

    sidebar_extra = """
    <div class="card" style="background:#fef2f2; border-color:#fecaca;">
        <h3 style="color:#b91c1c;"><span class="mif-bell"></span> Medical Emergency</h3>
        <p style="font-size:12px; color:#7f1d1d; margin-bottom:10px;">For acute trauma, dispatch emergency response via sovereign hotline 9-1-1 or visit your regional hospital.</p>
        <a href="/healthcare.html#hospitals" class="btn btn-primary btn-sm" style="width:100%; text-align:center;">Find Nearest Hospital</a>
    </div>

    <div class="card">
        <h3>DDCR Direct Navigation</h3>
        <ul class="sidebar-nav-list">
            <li><a href="/mH/ddcr/index.html" class="active"><span class="mif-home"></span> DDCR Home</a></li>
            <li><a href="/mH/ddcr/health_topics.html"><span class="mif-folder"></span> Health Topics (A-Z)</a></li>
            <li><a href="/mH/ddcr/outbreaks.html"><span class="mif-warning"></span> Active Outbreaks</a></li>
            <li><a href="/mH/ddcr/search.html"><span class="mif-search"></span> Research Search</a></li>
            <li><a href="/healthcare.html"><span class="mif-chevron-left"></span> Ministry of Healthcare</a></li>
        </ul>
    </div>
    """

    generate_page(
        filename=os.path.join(DDCR_DIR, "index.html"),
        title="Department of Disease Control & Research (DDCR)",
        theme_class="theme-healthcare",
        active_tab="healthcare",
        hero_title="Department of Disease Control & Research (DDCR)",
        hero_sub="National Epidemiological Surveillance, Pathogen Monitoring & Clinical Research",
        sidebar_title="Ministry of Healthcare",
        sidebar_subtitle="DDCR Directorate",
        sidebar_status="Active Surveillance",
        sidebar_nav_links=[],
        main_content_html=main_content,
        sidebar_right_extra_html=sidebar_extra
    )

def build_ddcr_topics():
    main_content = """
    <div class="card">
        <h2>Health Topics Directory &bull; Comprehensive Clinical A-Z</h2>
        <p class="ol-small ol-muted">Authoritative clinical summaries, symptomatic triage, diagnostic criteria, and sovereign treatment guidance vetted by the Sangaia Medical Board.</p>
        
        <div style="margin: 12px 0;">
            <input type="text" id="topic-search-input" class="form-input" placeholder="Search disease, condition, or pathogen (e.g., Influenza, COVID-19, Mpox)...">
        </div>

        <div id="alphabet-bar" style="display: flex; flex-wrap: wrap; gap: 4px; margin: 12px 0;">
            <button type="button" class="tool-btn alphabet-link active" data-letter="all">ALL</button>
        </div>

        <div style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom:14px;">
            <button type="button" class="btn btn-outline btn-sm cat-filter active" data-cat="all">All Conditions</button>
            <button type="button" class="btn btn-outline btn-sm cat-filter" data-cat="Infectious">Infectious</button>
            <button type="button" class="btn btn-outline btn-sm cat-filter" data-cat="Respiratory">Respiratory</button>
            <button type="button" class="btn btn-outline btn-sm cat-filter" data-cat="Cardiovascular">Cardiovascular</button>
            <button type="button" class="btn btn-outline btn-sm cat-filter" data-cat="Neurological">Neurological</button>
        </div>

        <div id="topics-list" style="display: flex; flex-direction: column; gap: 10px;">
            <!-- Populated via diseases.js -->
        </div>
    </div>
    """

    sidebar_extra = """
    <div class="card">
        <h3>DDCR Navigation</h3>
        <ul class="sidebar-nav-list">
            <li><a href="/mH/ddcr/index.html"><span class="mif-home"></span> DDCR Home</a></li>
            <li><a href="/mH/ddcr/health_topics.html" class="active"><span class="mif-folder"></span> Health Topics (A-Z)</a></li>
            <li><a href="/mH/ddcr/outbreaks.html"><span class="mif-warning"></span> Active Outbreaks</a></li>
            <li><a href="/mH/ddcr/search.html"><span class="mif-search"></span> Research Search</a></li>
            <li><a href="/healthcare.html"><span class="mif-chevron-left"></span> Ministry of Healthcare</a></li>
        </ul>
    </div>
    """

    extra_scripts = """
    <script src="/mH/ddcr/data/diseases.js"></script>
    <script>
    document.addEventListener('DOMContentLoaded', () => {
        let activeCategory = 'all';
        let activeLetter = 'all';
        let searchQuery = '';

        const bar = document.getElementById('alphabet-bar');
        const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");
        alphabet.forEach(letter => {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'tool-btn alphabet-link';
            btn.textContent = letter;
            btn.dataset.letter = letter;
            btn.onclick = () => {
                document.querySelectorAll('.alphabet-link').forEach(el => el.classList.remove('active'));
                btn.classList.add('active');
                activeLetter = letter;
                renderTopics();
            };
            bar.appendChild(btn);
        });

        const allBtn = bar.querySelector('[data-letter="all"]');
        if (allBtn) {
            allBtn.onclick = () => {
                document.querySelectorAll('.alphabet-link').forEach(el => el.classList.remove('active'));
                allBtn.classList.add('active');
                activeLetter = 'all';
                renderTopics();
            };
        }

        document.querySelectorAll('.cat-filter').forEach(btn => {
            btn.onclick = () => {
                document.querySelectorAll('.cat-filter').forEach(el => el.classList.remove('active'));
                btn.classList.add('active');
                activeCategory = btn.dataset.cat;
                renderTopics();
            };
        });

        const searchInput = document.getElementById('topic-search-input');
        if (searchInput) {
            searchInput.oninput = (e) => {
                searchQuery = e.target.value.toLowerCase().trim();
                renderTopics();
            };
        }

        function renderTopics() {
            const list = document.getElementById('topics-list');
            if (!list || !window.DDCR_DISEASES) return;
            list.innerHTML = '';

            const filtered = window.DDCR_DISEASES.filter(d => {
                const matchCat = (activeCategory === 'all') || (d.category === activeCategory);
                const matchLet = (activeLetter === 'all') || (d.name.toUpperCase().startsWith(activeLetter));
                const matchQ = (!searchQuery) || (d.name.toLowerCase().includes(searchQuery) || (d.overview || '').toLowerCase().includes(searchQuery));
                return matchCat && matchLet && matchQ;
            });

            if (filtered.length === 0) {
                list.innerHTML = '<div style="padding:16px; color:#666; text-align:center;">No matching medical conditions found.</div>';
                return;
            }

            filtered.forEach(d => {
                const item = document.createElement('div');
                item.className = 'card';
                item.style.marginBottom = '8px';
                item.style.padding = '12px';
                item.innerHTML = `
                    <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                        <div>
                            <h3 style="margin:0 0 4px 0;"><a href="/mH/ddcr/article.html?topic=${encodeURIComponent(d.id)}">${d.name}</a></h3>
                            <span class="badge badge-primary">${d.category || 'General'}</span>
                        </div>
                        <a href="/mH/ddcr/article.html?topic=${encodeURIComponent(d.id)}" class="btn btn-sm btn-outline">Read Clinical Protocol &rarr;</a>
                    </div>
                    <p style="font-size:12px; color:#555; margin-top:8px; line-height:1.4;">${(d.overview || '').substring(0, 180)}...</p>
                `;
                list.appendChild(item);
            });
        }

        renderTopics();
    });
    </script>
    """

    generate_page(
        filename=os.path.join(DDCR_DIR, "health_topics.html"),
        title="Health Topics (A-Z) - DDCR",
        theme_class="theme-healthcare",
        active_tab="healthcare",
        hero_title="DDCR Health Topics & Pathogens Directory",
        hero_sub="Comprehensive Disease Registry, Clinical Protocols & Evidence-Based Guidelines",
        sidebar_title="Ministry of Healthcare",
        sidebar_subtitle="DDCR Directorate",
        sidebar_status="Active Surveillance",
        sidebar_nav_links=[],
        main_content_html=main_content,
        sidebar_right_extra_html=sidebar_extra,
        extra_scripts=extra_scripts
    )

def build_ddcr_outbreaks():
    main_content = """
    <div class="card" style="border-left: 4px solid var(--primary);">
        <h2>Active Outbreaks &amp; Epidemiological Alerts</h2>
        <p>The Department of Disease Control &amp; Research (DDCR) tracks provincial and international infectious disease trends, issuing quarantine protocols and clinical guidance across all 5 provinces.</p>
        
        <div style="background: #fef2f2; border: 1px solid #fecaca; padding: 14px; border-radius: 2px; margin-top: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                <div>
                    <span class="badge badge-danger">Status: Elevated Regional Alert</span>
                    <h3 style="margin: 6px 0 4px 0; color: #b91c1c;">Seasonal Influenza (Type A - H1N1 / H3N2)</h3>
                    <p style="font-size: 11.5px; color: #666; margin-bottom: 6px;"><strong>Regions:</strong> Northern &amp; Maritime Provinces &bull; <strong>Mandate:</strong> Polyclinic Flu Immunization</p>
                </div>
                <a href="/mH/ddcr/article.html?topic=influenza" class="btn btn-primary btn-sm">View Protocol &rarr;</a>
            </div>
            <p style="font-size: 12.5px; margin: 0; line-height: 1.45;">Increased seasonal outpatient presentations. All citizens aged 6 months and older are advised to receive their quadrivalent influenza vaccination at local provincial health clinics.</p>
        </div>

        <div style="background: #f0f9ff; border: 1px solid #bae6fd; padding: 14px; border-radius: 2px; margin-top: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                <div>
                    <span class="badge badge-primary">Status: Continuous Genomic Tracking</span>
                    <h3 style="margin: 6px 0 4px 0; color: #0284c7;">COVID-19 (JN.1 / KP.2 Subvariants)</h3>
                    <p style="font-size: 11.5px; color: #666; margin-bottom: 6px;"><strong>Regions:</strong> Nationwide Urban Centers &bull; <strong>Mandate:</strong> Wastewater Surveillance &amp; Paxlovid Access</p>
                </div>
                <a href="/mH/ddcr/article.html?topic=covid-19" class="btn btn-primary btn-sm">View Protocol &rarr;</a>
            </div>
            <p style="font-size: 12.5px; margin: 0; line-height: 1.45;">Wastewater surveillance indicates steady low-level viral activity. Provincial hospitals maintain free 5-day oral antiviral courses (Paxlovid) for high-risk citizens and seniors.</p>
        </div>

        <div style="background: #fffbeb; border: 1px solid #fde68a; padding: 14px; border-radius: 2px; margin-top: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                <div>
                    <span class="badge badge-warning">Status: International Clade I / IIb Watch</span>
                    <h3 style="margin: 6px 0 4px 0; color: #b45309;">Mpox / Monkeypox (Clade I &amp; Clade II)</h3>
                    <p style="font-size: 11.5px; color: #666; margin-bottom: 6px;"><strong>Regions:</strong> Port Entry Screenings &bull; <strong>Mandate:</strong> Rapid PCR &amp; Ring Vaccination</p>
                </div>
                <a href="/mH/ddcr/article.html?topic=mpox" class="btn btn-primary btn-sm">View Protocol &rarr;</a>
            </div>
            <p style="font-size: 12.5px; margin: 0; line-height: 1.45;">Active surveillance for international travelers arriving from regions with Clade I transmission. JYNNEOS ring-vaccination and tecovirimat stockpiles positioned at provincial centers.</p>
        </div>

        <div style="background: #f0fdf4; border: 1px solid #bbf7d0; padding: 14px; border-radius: 2px; margin-top: 14px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 10px;">
                <div>
                    <span class="badge badge-success">Status: Agricultural &amp; Wildlife Biosecurity</span>
                    <h3 style="margin: 6px 0 4px 0; color: #15803d;">Avian Influenza (HPAI H5N1 Clade 2.3.4.4b)</h3>
                    <p style="font-size: 11.5px; color: #666; margin-bottom: 6px;"><strong>Regions:</strong> Rural Agricultural Districts &bull; <strong>Mandate:</strong> PPE &amp; Dairy Pasteurized Standards</p>
                </div>
                <a href="/mH/ddcr/article.html?topic=avian-flu" class="btn btn-primary btn-sm">View Protocol &rarr;</a>
            </div>
            <p style="font-size: 12.5px; margin: 0; line-height: 1.45;">Heightened biosecurity across provincial dairy herds and poultry farms. Testing of bulk milk and wastewater confirms zero mammalian spillovers into the human municipal food supply.</p>
        </div>
    </div>
    """

    sidebar_extra = """
    <div class="card">
        <h3>DDCR Navigation</h3>
        <ul class="sidebar-nav-list">
            <li><a href="/mH/ddcr/index.html"><span class="mif-home"></span> DDCR Home</a></li>
            <li><a href="/mH/ddcr/health_topics.html"><span class="mif-folder"></span> Health Topics (A-Z)</a></li>
            <li><a href="/mH/ddcr/outbreaks.html" class="active"><span class="mif-warning"></span> Active Outbreaks</a></li>
            <li><a href="/mH/ddcr/search.html"><span class="mif-search"></span> Research Search</a></li>
            <li><a href="/healthcare.html"><span class="mif-chevron-left"></span> Ministry of Healthcare</a></li>
        </ul>
    </div>
    """

    generate_page(
        filename=os.path.join(DDCR_DIR, "outbreaks.html"),
        title="Active Outbreaks & Protocols - DDCR",
        theme_class="theme-healthcare",
        active_tab="healthcare",
        hero_title="Active Epidemiological Outbreaks",
        hero_sub="National Quarantine Guidance, Vaccine Allocations & Clinical Protocols",
        sidebar_title="Ministry of Healthcare",
        sidebar_subtitle="DDCR Directorate",
        sidebar_status="Active Surveillance",
        sidebar_nav_links=[],
        main_content_html=main_content,
        sidebar_right_extra_html=sidebar_extra
    )

def build_ddcr_search():
    main_content = """
    <div class="card">
        <h2>Medical Literature &amp; PubMed PMC Research Database</h2>
        <p class="ol-small ol-muted">Search authoritative scientific literature, clinical trials, and epidemiological studies compiled by Sangaia's national medical researchers.</p>

        <div style="margin: 12px 0;">
            <input type="text" id="search-box" class="form-input" placeholder="Search research papers by keyword, pathogen, or author...">
        </div>

        <div style="display:flex; flex-wrap:wrap; gap:6px; margin-bottom:14px;">
            <button type="button" class="btn btn-outline btn-sm tab-btn active" data-tab="all">All Literature</button>
            <button type="button" class="btn btn-outline btn-sm tab-btn" data-tab="vaccines">Vaccines &amp; Immunology</button>
            <button type="button" class="btn btn-outline btn-sm tab-btn" data-tab="therapeutics">Therapeutics</button>
            <button type="button" class="btn btn-outline btn-sm tab-btn" data-tab="genomics">Genomics &amp; Variants</button>
        </div>

        <div id="results" style="display:flex; flex-direction:column; gap:10px;">
            <!-- Populated via diseases.js -->
        </div>
    </div>
    """

    sidebar_extra = """
    <div class="card">
        <h3>DDCR Navigation</h3>
        <ul class="sidebar-nav-list">
            <li><a href="/mH/ddcr/index.html"><span class="mif-home"></span> DDCR Home</a></li>
            <li><a href="/mH/ddcr/health_topics.html"><span class="mif-folder"></span> Health Topics (A-Z)</a></li>
            <li><a href="/mH/ddcr/outbreaks.html"><span class="mif-warning"></span> Active Outbreaks</a></li>
            <li><a href="/mH/ddcr/search.html" class="active"><span class="mif-search"></span> Research Search</a></li>
            <li><a href="/healthcare.html"><span class="mif-chevron-left"></span> Ministry of Healthcare</a></li>
        </ul>
    </div>
    """

    extra_scripts = """
    <script src="/mH/ddcr/data/diseases.js"></script>
    <script>
    document.addEventListener('DOMContentLoaded', () => {
        const searchBox = document.getElementById('search-box');
        const resultsBox = document.getElementById('results');
        let activeTab = 'all';

        function getAllStudies() {
            if (!window.DDCR_DISEASES) return [];
            const studies = [];
            window.DDCR_DISEASES.forEach(d => {
                (d.research_papers || []).forEach(p => {
                    studies.push({
                        ...p,
                        disease_name: d.name,
                        disease_id: d.id
                    });
                });
            });
            return studies;
        }

        function renderResults() {
            const all = getAllStudies();
            const q = (searchBox ? searchBox.value.toLowerCase().trim() : '');
            
            const filtered = all.filter(s => {
                const text = (s.title + ' ' + (s.authors || '') + ' ' + (s.journal || '') + ' ' + (s.disease_name || '')).toLowerCase();
                const matchQ = !q || text.includes(q);
                let matchTab = true;
                if (activeTab === 'vaccines') matchTab = text.includes('vaccin') || text.includes('immun');
                else if (activeTab === 'therapeutics') matchTab = text.includes('therap') || text.includes('treatment') || text.includes('antiviral');
                else if (activeTab === 'genomics') matchTab = text.includes('genom') || text.includes('variant') || text.includes('clade') || text.includes('mutat');
                return matchQ && matchTab;
            });

            resultsBox.innerHTML = '';
            if (filtered.length === 0) {
                resultsBox.innerHTML = '<div style="padding:16px; color:#666; text-align:center;">No research papers match your query.</div>';
                return;
            }

            filtered.slice(0, 30).forEach(s => {
                const card = document.createElement('div');
                card.className = 'card';
                card.style.marginBottom = '8px';
                card.style.padding = '12px';
                card.innerHTML = `
                    <h4 style="margin:0 0 4px 0;"><a href="${s.url}" target="_blank" rel="noopener">${s.title}</a></h4>
                    <div style="font-size:11.5px; color:#666; margin-bottom:6px;">
                        <strong>${s.authors || 'Research Group'}</strong> &bull; <em>${s.journal || 'PubMed Central'}</em> (${s.year || '2026'})
                    </div>
                    <div style="display:flex; justify-content:space-between; align-items:center;">
                        <span class="badge badge-neutral">${s.disease_name}</span>
                        <a href="${s.url}" target="_blank" rel="noopener" class="btn btn-outline btn-sm">View Study on PMC &rarr;</a>
                    </div>
                `;
                resultsBox.appendChild(card);
            });
        }

        if (searchBox) searchBox.oninput = renderResults;

        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.onclick = () => {
                document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
                btn.classList.add('active');
                activeTab = btn.dataset.tab;
                renderResults();
            };
        });

        renderResults();
    });
    </script>
    """

    generate_page(
        filename=os.path.join(DDCR_DIR, "search.html"),
        title="Medical Research Database - DDCR",
        theme_class="theme-healthcare",
        active_tab="healthcare",
        hero_title="DDCR Scientific Literature Database",
        hero_sub="Search Peer-Reviewed Infectious Disease Literature & National Clinical Trials",
        sidebar_title="Ministry of Healthcare",
        sidebar_subtitle="DDCR Directorate",
        sidebar_status="Active Surveillance",
        sidebar_nav_links=[],
        main_content_html=main_content,
        sidebar_right_extra_html=sidebar_extra,
        extra_scripts=extra_scripts
    )

def build_ddcr_article():
    main_content = """
    <div class="card" id="article-container">
        <h2 id="article-title">Clinical Protocol</h2>
        <div id="article-content">Loading medical dossier...</div>
    </div>
    """

    sidebar_extra = """
    <div class="card">
        <h3>DDCR Navigation</h3>
        <ul class="sidebar-nav-list">
            <li><a href="/mH/ddcr/index.html"><span class="mif-home"></span> DDCR Home</a></li>
            <li><a href="/mH/ddcr/health_topics.html"><span class="mif-folder"></span> Health Topics (A-Z)</a></li>
            <li><a href="/mH/ddcr/outbreaks.html"><span class="mif-warning"></span> Active Outbreaks</a></li>
            <li><a href="/mH/ddcr/search.html"><span class="mif-search"></span> Research Search</a></li>
            <li><a href="/healthcare.html"><span class="mif-chevron-left"></span> Ministry of Healthcare</a></li>
        </ul>
    </div>
    """

    extra_scripts = """
    <script src="/mH/ddcr/data/diseases.js"></script>
    <script>
    document.addEventListener('DOMContentLoaded', () => {
        const urlParams = new URLSearchParams(window.location.search);
        const topicId = urlParams.get('topic') || 'covid-19';

        const diseases = window.DDCR_DISEASES || [];
        const disease = diseases.find(d => d.id === topicId) || diseases[0];

        const titleEl = document.getElementById('article-title');
        const contEl = document.getElementById('article-content');

        if (disease) {
            titleEl.textContent = disease.name;
            contEl.innerHTML = `
                <div style="margin-bottom:14px;">
                    <span class="badge badge-primary">${disease.category || 'General'}</span>
                    <span class="badge badge-success" style="margin-left:6px;">National Standard Protocol</span>
                </div>
                <h3>Clinical Overview</h3>
                <p style="font-size:13px; line-height:1.5;">${disease.overview || 'Standard disease overview.'}</p>
                
                <h3 style="margin-top:16px;">Symptomatic Profile</h3>
                <p style="font-size:13px; line-height:1.5;">${disease.symptoms || 'Common clinical symptoms recorded.'}</p>

                <h3 style="margin-top:16px;">Statutory Treatment &amp; Containment Guidelines</h3>
                <p style="font-size:13px; line-height:1.5;">${disease.treatment || 'Approved antiviral and supportive therapies.'}</p>

                <h3 style="margin-top:16px;">Associated Peer-Reviewed Literature</h3>
                <div style="margin-top:8px;">
                    ${(disease.research_papers || []).slice(0, 5).map(p => `
                        <div class="card" style="padding:10px; margin-bottom:8px;">
                            <strong>${p.title}</strong><br>
                            <span style="font-size:11.5px; color:#666;">${p.authors} &bull; <em>${p.journal}</em></span><br>
                            <a href="${p.url}" target="_blank" rel="noopener" style="font-size:12px;">Read Study &rarr;</a>
                        </div>
                    `).join('') || '<p style="color:#666;">No attached studies.</p>'}
                </div>
            `;
        } else {
            contEl.innerHTML = '<p>Disease record not found.</p>';
        }
    });
    </script>
    """

    generate_page(
        filename=os.path.join(DDCR_DIR, "article.html"),
        title="Clinical Protocol - DDCR",
        theme_class="theme-healthcare",
        active_tab="healthcare",
        hero_title="DDCR Clinical Protocol & Treatment Directive",
        hero_sub="National Disease Guideline & Scientific Evidence",
        sidebar_title="Ministry of Healthcare",
        sidebar_subtitle="DDCR Directorate",
        sidebar_status="Active Surveillance",
        sidebar_nav_links=[],
        main_content_html=main_content,
        sidebar_right_extra_html=sidebar_extra,
        extra_scripts=extra_scripts
    )

def build_article_press():
    article_path = "articles/state_of_provinces.html"
    main_content = """
    <div class="card">
        <h2>Provincial Review: Half-Year Address</h2>
        <p style="color:var(--text-muted); font-size:12px; margin-bottom:12px;"><strong>By The Ministry of the Executive</strong> &bull; July 3rd, 2026 &bull; Sangaia Gazette</p>
        
        <p><strong>HORNET'S POINT (NM)</strong> — The Sangaian government, on Friday, announced sweeping administrative reforms and economic expansions as part of their half-year provincial address, pointing to a capped tax rate and projected job growth ahead of the upcoming Revolution Day holiday.</p>

        <h3 style="margin-top:16px;">The Economy</h3>
        <p>The legislative and infrastructural changes span several critical sectors, including education, healthcare, and national defense. Government officials described the initiative as a coordinated effort to establish a more seamless administrative experience for citizens across all provinces, though details on the specific funding mechanisms for these broad projects remain limited. The half-year review represents the most comprehensive administrative overhaul the region has seen in recent years, as leaders attempt to modernize public facilities and update curriculum standards in regional schools.</p>

        <p>Sangaia's Ministry of the Treasury reported that the tax rate for residents across all provinces has not exceeded 2 percent. Officials said the low rate is designed to ensure that citizens retain a greater portion of their earnings. In addition to the tax cap, the ministry announced an expansion of employment opportunities within both the public sector and external markets. According to treasury projections, the job market is expected to add approximately 20 new applicants per week through the end of the year.</p>

        <h3 style="margin-top:16px;">Upcoming Civic Events</h3>
        <p>The midyear address comes on the eve of Sangaia's annual Revolution Day festival, scheduled for July 4. The national holiday honors global independence movements and celebrates nations that have historically seceded from former governing bodies. This year's festivities are designed to facilitate direct engagement between community members and provincial leaders. Regional directors are expected to hold town-hall-style forums throughout the holiday weekend to discuss localized infrastructure needs.</p>

        <h3 style="margin-top:16px;">A Note on Citizenship</h3>
        <p>In observance of the public holiday, Sangaia's citizenship office will suspend physical operations on Saturday. Although processing will temporarily pause, authorities noted that applicants can continue to monitor their documentation status online. Regular administrative services are scheduled to resume Monday morning.</p>
    </div>
    """

    sidebar_extra = """
    <div class="card">
        <h3>Gazette Links</h3>
        <ul class="sidebar-nav-list">
            <li><a href="/societal_press.html"><span class="mif-chevron-left"></span> Return to Societal Press</a></li>
            <li><a href="/executive.html"><span class="mif-library"></span> Executive Journal</a></li>
            <li><a href="/index.html"><span class="mif-home"></span> Federal Home</a></li>
        </ul>
    </div>
    """

    generate_page(
        filename=article_path,
        title="Provincial Review: Half-Year Address :: Sangaia Live",
        theme_class="theme-executive",
        active_tab="executive",
        hero_title="Sovereign State Gazette & Dispatches",
        hero_sub="Official Half-Year Address & Provincial Review &bull; Office of the Aeretocrat",
        sidebar_title="Ministry of the Executive",
        sidebar_subtitle="Executive Gazette",
        sidebar_status="Official Release",
        sidebar_nav_links=[],
        main_content_html=main_content,
        sidebar_right_extra_html=sidebar_extra
    )

if __name__ == "__main__":
    build_ddcr_index()
    build_ddcr_topics()
    build_ddcr_outbreaks()
    build_ddcr_search()
    build_ddcr_article()
    build_article_press()
    print("All DDCR and Gazette article pages successfully rebuilt in One Live architecture!")

