#!/usr/bin/env python3
"""
Sangaia Live Healthcare Secondary Pages Generator
Restores the rich pre-redesign pages for the Ministry of Healthcare:
1. Services (services.html / healthcare_services.html) - Sangaian Health Charter & Service Catalog
2. Hospitals (hospitals.html / healthcare_hospitals.html) - 5-Province Hospital Emergency Network
3. Research (research.html / healthcare_research.html) - Biomedical Innovation & DDCR Gateway
4. Support (support.html / healthcare_support.html) - Patient Advocacy, FAQ & Emergency Hotline
"""

import os
from generate_all_sites import generate_page

HEALTHCARE_NAV_TABS = [
    ("home", "Healthcare Home", "/healthcare.html"),
    ("departments", "Departments", "/healthcare_departments.html"),
    ("services", "Medical Services", "/healthcare_services.html"),
    ("hospitals", "5-Province Hospitals", "/healthcare_hospitals.html"),
    ("research", "Medical Research", "/healthcare_research.html"),
    ("support", "Patient Support", "/healthcare_support.html"),
    ("ddcr", "DDCR Disease Control", "/mH/ddcr/index.html"),
    ("federal", "← Federal Portal", "/index.html"),
]

HEALTHCARE_NAV_TABS_SUBDOMAIN = [
    ("home", "Healthcare Home", "index.html"),
    ("departments", "Departments", "departments.html"),
    ("services", "Medical Services", "services.html"),
    ("hospitals", "5-Province Hospitals", "hospitals.html"),
    ("research", "Medical Research", "research.html"),
    ("support", "Patient Support", "support.html"),
    ("ddcr", "DDCR Disease Control", "ddcr/index.html"),
    ("federal", "← Federal Portal", "https://sangaia.org/index.html"),
]

def build_hospitals_page():
    title = "5-Province Hospital Emergency Network & Regional Medical Centers"
    theme = "theme-healthcare"
    hero_title = "Hospital Emergency Network & Regional Medical Centers"
    hero_sub = "Level 1 trauma care, acute intensive triage, and regional medical facilities across all 5 sovereign provinces"

    sidebar_links = [
        {"label": "Overview & ER Triage", "url": "#overview", "active": True},
        {"label": "Watson Healthcare (New Jasper)", "url": "#watson", "active": False},
        {"label": "New Madison Hospital (New Madison)", "url": "#madison", "active": False},
        {"label": "Suwannee Emergency (Liveland)", "url": "#suwannee", "active": False},
        {"label": "Sentinel Memorial Hospital (Sentinel)", "url": "#sentinel", "active": False},
        {"label": "Columbia Regional Center (Columbia)", "url": "#columbia", "active": False},
        {"label": "Emergency Protocols", "url": "#emergency-protocols", "active": False}
    ]

    main_content = """
    <!-- Hospital Network Overview -->
    <div class="ol-card" id="overview">
        <div class="ol-card-title">
            <span>Sangaia Integrated Hospital Network</span>
            <span class="ol-badge-tag ol-badge-success">5 Provincial Centers Active</span>
        </div>
        <p>Sangaia boasts a fully integrated network of state-of-the-art public hospitals across all five sovereign provinces. Every facility operates 24/7 acute trauma response, subsidized neonatal and pediatric wings, and emergency room care with zero out-of-pocket costs for registered citizens.</p>
        <div class="ol-grid-3" style="margin-top:12px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:10px; text-align:center;">
                <div style="font-size:11px; color:#605e5c; text-transform:uppercase; font-weight:600;">Average ER Wait Time</div>
                <div style="font-size:18px; font-weight:700; color:#b91c1c; margin:4px 0;">12 Minutes</div>
                <div style="font-size:11px; color:#8a8886;">Rapid Triage Standard</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:10px; text-align:center;">
                <div style="font-size:11px; color:#605e5c; text-transform:uppercase; font-weight:600;">Emergency Copay</div>
                <div style="font-size:18px; font-weight:700; color:#b91c1c; margin:4px 0;">$ 0.00</div>
                <div style="font-size:11px; color:#8a8886;">100% Sovereign Funded</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:10px; text-align:center;">
                <div style="font-size:11px; color:#605e5c; text-transform:uppercase; font-weight:600;">Helipad Capacity</div>
                <div style="font-size:18px; font-weight:700; color:#b91c1c; margin:4px 0;">5 / 5 Bases</div>
                <div style="font-size:11px; color:#8a8886;">Air Medevac Active</div>
            </div>
        </div>
    </div>

    <!-- Province 1: Watson Healthcare (New Jasper) -->
    <div class="ol-card" id="watson">
        <div class="ol-card-title">
            <span>Watson Healthcare &bull; Province of New Jasper</span>
            <span class="ol-badge-tag">Level 1 Trauma Center</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:6px; font-size:13px; margin:8px 0;">
            <div><strong>Sangaian Address:</strong> H0001 1st Street, Shesk, New Jasper, 1-1000</div>
            <div style="color:#605e5c;"><em>Map Reference: 506 4th St NW, Jasper, FL 32052</em></div>
            <div><strong>Key Departments:</strong> Emergency Medicine, Cardiovascular Surgery, Pediatric ICU, Orthopedics</div>
            <div><strong>ER Availability:</strong> 24/7 Triage &bull; 48 Acute Beds &bull; Immediate Trauma Team</div>
        </div>
        <div style="margin-top:10px;">
            <button type="button" class="ol-btn ol-btn-sm" onclick="alert('Routing directions to Watson Healthcare (New Jasper)...')">Get Driving Directions &rarr;</button>
        </div>
    </div>

    <!-- Province 2: New Madison Hospital (New Madison) -->
    <div class="ol-card" id="madison">
        <div class="ol-card-title">
            <span>New Madison Hospital &bull; Province of New Madison</span>
            <span class="ol-badge-tag">Regional Acute Center</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:6px; font-size:13px; margin:8px 0;">
            <div><strong>Sangaian Address:</strong> H0002 2nd Street, Madison City, New Madison, 1-2000</div>
            <div style="color:#605e5c;"><em>Map Reference: 224 NW Crane Ave, Madison, FL 32340</em></div>
            <div><strong>Key Departments:</strong> Intensive Care, Maternal Health, Emergency Pediatrics, Dialysis Unit</div>
            <div><strong>ER Availability:</strong> 24/7 Triage &bull; 36 Acute Beds &bull; Dedicated Stroke Response Unit</div>
        </div>
        <div style="margin-top:10px;">
            <button type="button" class="ol-btn ol-btn-sm" onclick="alert('Routing directions to New Madison Hospital (New Madison)...')">Get Driving Directions &rarr;</button>
        </div>
    </div>

    <!-- Province 3: Suwannee Emergency (Liveland) -->
    <div class="ol-card" id="suwannee">
        <div class="ol-card-title">
            <span>Suwannee Emergency Hospital &bull; Province of Liveland</span>
            <span class="ol-badge-tag">Rapid Response Center</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:6px; font-size:13px; margin:8px 0;">
            <div><strong>Sangaian Address:</strong> H0003 3rd Street, Oaks, Liveland, 1-3000</div>
            <div style="color:#605e5c;"><em>Map Reference: 1100 11th St SW, Live Oak, FL 32064</em></div>
            <div><strong>Key Departments:</strong> Rapid Emergency Triage, Acute Medical Care, Helipad Dispatch, Surgical Suites</div>
            <div><strong>ER Availability:</strong> 24/7 Triage &bull; 40 Acute Beds &bull; Coastal Disaster Relief Wing</div>
        </div>
        <div style="margin-top:10px;">
            <button type="button" class="ol-btn ol-btn-sm" onclick="alert('Routing directions to Suwannee Emergency (Liveland)...')">Get Driving Directions &rarr;</button>
        </div>
    </div>

    <!-- Province 4: Sentinel Memorial Hospital (Sentinel) -->
    <div class="ol-card" id="sentinel">
        <div class="ol-card-title">
            <span>Sentinel Memorial Hospital &bull; Province of Sentinel</span>
            <span class="ol-badge-tag">Neurological & Trauma Hub</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:6px; font-size:13px; margin:8px 0;">
            <div><strong>Sangaian Address:</strong> H0004 4th Street, Sentinel Ridge, Sentinel, 1-4000</div>
            <div style="color:#605e5c;"><em>Map Reference: 168 NW Main Blvd, Lake City, FL 32055</em></div>
            <div><strong>Key Departments:</strong> Specialized Neurological Wing, Orthopedic Surgery, Free Emergency Care, Burn Center</div>
            <div><strong>ER Availability:</strong> 24/7 Triage &bull; 54 Acute Beds &bull; Advanced CT / MRI Diagnostic Suite</div>
        </div>
        <div style="margin-top:10px;">
            <button type="button" class="ol-btn ol-btn-sm" onclick="alert('Routing directions to Sentinel Memorial Hospital (Sentinel)...')">Get Driving Directions &rarr;</button>
        </div>
    </div>

    <!-- Province 5: Columbia Regional Medical Center (Columbia) -->
    <div class="ol-card" id="columbia">
        <div class="ol-card-title">
            <span>Columbia Regional Medical Center &bull; Province of Columbia</span>
            <span class="ol-badge-tag">Comprehensive Medical Hub</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:6px; font-size:13px; margin:8px 0;">
            <div><strong>Sangaian Address:</strong> H0005 5th Street, Columbia City, Columbia, 1-5000</div>
            <div style="color:#605e5c;"><em>Map Reference: 4288 SW State Road 47, Lake City, FL 32024</em></div>
            <div><strong>Key Departments:</strong> Regional Oncology Center, Neonatal ICU, Sovereign Healthcare Research Hub, Toxicology</div>
            <div><strong>ER Availability:</strong> 24/7 Triage &bull; 62 Acute Beds &bull; State-Level Pandemic Isolation Wing</div>
        </div>
        <div style="margin-top:10px;">
            <button type="button" class="ol-btn ol-btn-sm" onclick="alert('Routing directions to Columbia Regional Medical Center (Columbia)...')">Get Driving Directions &rarr;</button>
        </div>
    </div>

    <!-- Emergency Protocols -->
    <div class="ol-card" id="emergency-protocols">
        <div class="ol-card-title">
            <span>Emergency Medical Transport &amp; Ambulance Dispatch</span>
            <span class="ol-badge-tag" style="background:#b91c1c; color:#fff; border-color:#991b1b;">Hotline: 9-1-1</span>
        </div>
        <p>If you or someone near you experiences chest pain, severe hemorrhage, respiratory distress, or trauma, dial <strong>9-1-1</strong> immediately. Ambulance dispatch is 100% sovereign-funded with zero out-of-pocket bills for all residents.</p>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Emergency Dispatch</h3>
        <p class="ol-small ol-muted">24/7 Sovereign Triage Dispatchers standing by across New Jasper, New Madison, Liveland, Sentinel, and Columbia.</p>
        <div class="ol-mt-10">
            <a href="tel:911" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center; background:#b91c1c; border-color:#991b1b;">Dial Emergency 9-1-1</a>
        </div>
    </div>
    <div class="ol-sidebox">
        <h3>Statutory Health Directory</h3>
        <p class="ol-small ol-muted">Explore statutory departments, health licenses, and clinical standards.</p>
        <div class="ol-mt-10">
            <a href="/healthcare_departments.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Launch Departments</a>
        </div>
    </div>
    """

    generate_page("healthcare_hospitals.html", title, theme, "hospitals", hero_title, hero_sub, "Ministry of Healthcare", "5-Province Hospital Network", "ERs Active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS)
    generate_page("mH/hospitals.html", title, theme, "hospitals", hero_title, hero_sub, "Ministry of Healthcare", "5-Province Hospital Network", "ERs Active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS_SUBDOMAIN)

def build_services_page():
    title = "Comprehensive Medical Services & The Sangaian Health Charter"
    theme = "theme-healthcare"
    hero_title = "Comprehensive Medical Services"
    hero_sub = "Guaranteed universal coverage, zero out-of-pocket fees, preventative care, and specialized surgery"

    sidebar_links = [
        {"label": "The Sangaian Health Charter", "url": "#charter", "active": True},
        {"label": "Comprehensive Care Catalog", "url": "#catalog", "active": False},
        {"label": "Prescription Drug Coverage", "url": "#pharmacy", "active": False},
        {"label": "Dental & Vision Healthcare", "url": "#dental-vision", "active": False},
        {"label": "Mental Health & Wellness", "url": "#mental-health", "active": False},
        {"label": "Zero-Cost Pricing Schedule", "url": "#pricing", "active": False}
    ]

    main_content = """
    <!-- The Sangaian Health Charter -->
    <div class="ol-card" id="charter">
        <div class="ol-card-title">
            <span>The Sangaian Health Charter</span>
            <span class="ol-badge-tag ol-badge-success">Constitutional Right</span>
        </div>
        <p>The Sangaian Health Charter establishes that healthcare is a fundamental civic entitlement, not a commodity. Under Article IV of the Sovereign Constitution, no citizen or authorized resident shall ever be turned away from medical treatment, denied medications, or driven into debt due to illness.</p>
        <div class="ol-note" style="margin-top:12px;">
            <strong>Statutory Guarantee:</strong> 100% of preventative doctor visits, emergency surgeries, hospital stays, and essential prescription medications are covered by sovereign public revenue.
        </div>
    </div>

    <!-- Comprehensive Care Catalog -->
    <div class="ol-card" id="catalog">
        <div class="ol-card-title">
            <span>Comprehensive Healthcare Services</span>
            <span class="ol-badge-tag">All Provincial Facilities</span>
        </div>
        <p>We provide a comprehensive array of medical services to ensure the health and dignity of all Sangaians:</p>
        <table class="ol-table" style="margin-top:10px;">
            <thead>
                <tr>
                    <th>Service Discipline</th>
                    <th>Covered Procedures</th>
                    <th>Provincial Availability</th>
                    <th>Citizen Cost</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Primary Care</strong></td>
                    <td>Annual physicals, chronic illness management, pediatric wellness, vaccinations</td>
                    <td>All 5 Provinces</td>
                    <td><span class="ol-badge-tag ol-badge-success">$ 0.00 (Free)</span></td>
                </tr>
                <tr>
                    <td><strong>Emergency &amp; Trauma</strong></td>
                    <td>24/7 ER triage, acute surgery, intensive care, burn care, air ambulance</td>
                    <td>All 5 Provinces</td>
                    <td><span class="ol-badge-tag ol-badge-success">$ 0.00 (Free)</span></td>
                </tr>
                <tr>
                    <td><strong>Specialty Surgery</strong></td>
                    <td>Cardiothoracic, orthopedic, neurosurgery, oncological resections</td>
                    <td>Regional Hubs</td>
                    <td><span class="ol-badge-tag ol-badge-success">$ 0.00 (Free)</span></td>
                </tr>
                <tr>
                    <td><strong>Maternal &amp; Infant</strong></td>
                    <td>Prenatal care, birthing suites, neonatal intensive care, postnatal visits</td>
                    <td>All 5 Provinces</td>
                    <td><span class="ol-badge-tag ol-badge-success">$ 0.00 (Free)</span></td>
                </tr>
                <tr>
                    <td><strong>Diagnostic Imaging</strong></td>
                    <td>MRI, CT scans, ultrasound, X-ray, digital lab bloodwork</td>
                    <td>All 5 Provinces</td>
                    <td><span class="ol-badge-tag ol-badge-success">$ 0.00 (Free)</span></td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- Prescription Drug Coverage -->
    <div class="ol-card" id="pharmacy">
        <div class="ol-card-title">
            <span>Prescription Drug Formulary &amp; Local Dispensaries</span>
            <span class="ol-badge-tag">Zero Copay</span>
        </div>
        <p>All essential maintenance medications—including insulin, cardiovascular medications, antibiotics, and inhalers—are categorized under Tier 1 of the Sovereign Formulary and dispensed at zero cost through accredited public hospital pharmacies.</p>
    </div>

    <!-- Dental & Vision -->
    <div class="ol-card" id="dental-vision">
        <div class="ol-card-title">
            <span>Dental, Vision &amp; Auditory Care</span>
            <span class="ol-badge-tag">Universal Inclusions</span>
        </div>
        <p>Unlike commercial healthcare regimes, Sangaia treats oral and visual health as inseparable from bodily wellbeing. Annual dental cleanings, cavity restorations, comprehensive eye examinations, and standard corrective lenses are fully covered.</p>
    </div>

    <!-- Mental Health & Wellness -->
    <div class="ol-card" id="mental-health">
        <div class="ol-card-title">
            <span>Mental Health, Counseling &amp; Addiction Support</span>
            <span class="ol-badge-tag">Confidential &bull; Free</span>
        </div>
        <p>Mental healthcare is accessible without referral. Citizens may book confidential therapy sessions, psychiatric consultations, or residential holistic recovery programs with complete medical privacy.</p>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Health Pricing PDF</h3>
        <p class="ol-small ol-muted">Download the official Sangaia Health Pricing Schedule detailing full universal coverage benchmarks.</p>
        <div class="ol-mt-10">
            <a href="javascript:void(0)" onclick="alert('Downloading Sangaia Health Pricing Schedule (PDF)...')" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">Download Pricing PDF</a>
        </div>
    </div>
    """

    generate_page("healthcare_services.html", title, theme, "services", hero_title, hero_sub, "Ministry of Healthcare", "Universal Health Charter", "Services Active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS)
    generate_page("mH/services.html", title, theme, "services", hero_title, hero_sub, "Ministry of Healthcare", "Universal Health Charter", "Services Active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS_SUBDOMAIN)

def build_research_page():
    title = "Medical Research, Clinical Trials & DDCR Liaison"
    theme = "theme-healthcare"
    hero_title = "Medical Research & Development Directorate"
    hero_sub = "Ethical clinical trials, open-access biomedical literature, non-commercial patents & disease surveillance"

    sidebar_links = [
        {"label": "Research & Ethics Mandate", "url": "#overview", "active": True},
        {"label": "DDCR Portal Gateway", "url": "#ddcr-gateway", "active": False},
        {"label": "Active Clinical Trials", "url": "#trials", "active": False},
        {"label": "Biomedical Standards", "url": "#standards", "active": False},
        {"label": "Provincial Labs", "url": "#labs", "active": False}
    ]

    main_content = """
    <!-- Medical Research & Development -->
    <div class="ol-card" id="overview">
        <div class="ol-card-title">
            <span>Medical Research &amp; Non-Commercial Innovation</span>
            <span class="ol-badge-tag ol-badge-success">Open Access</span>
        </div>
        <p>The Ministry of Healthcare invests heavily in the future of sovereign medicine. All medical research funded by Sangaia is held in public trust with open-source patent licenses, guaranteeing that breakthroughs in oncology, genomics, and infectious disease treatments remain globally accessible and free from monopolistic price-gouging.</p>
    </div>

    <!-- DDCR Gateway Card -->
    <div class="ol-card" id="ddcr-gateway" style="border: 2px solid #b91c1c; background: #fffdfd;">
        <div class="ol-card-title">
            <span style="color:#b91c1c; font-size:16px;">Department of Disease Control &amp; Research (DDCR)</span>
            <span class="ol-badge-tag" style="background:#b91c1c; color:#fff; border-color:#991b1b;">Sovereign CDC</span>
        </div>
        <p>Looking for specific health topics, epidemic guidelines, outbreak surveillance, or biomedical research papers? The DDCR maintains our comprehensive national repository:</p>
        <div class="ol-grid-3" style="margin-top:14px;">
            <div style="background:#ffffff; border:1px solid #fecaca; border-radius:2px; padding:12px; text-align:center;">
                <div style="font-size:22px;">📚</div>
                <strong style="display:block; margin:6px 0 4px; font-size:13px;">Health Topics (A-Z)</strong>
                <p class="ol-small ol-muted">Verified disease symptom guides and clinical treatment protocols.</p>
                <a href="/mH/ddcr/health_topics.html" class="ol-btn ol-btn-sm" style="width:100%; margin-top:8px;">Browse Topics &rarr;</a>
            </div>
            <div style="background:#ffffff; border:1px solid #fecaca; border-radius:2px; padding:12px; text-align:center;">
                <div style="font-size:22px;">⚠️</div>
                <strong style="display:block; margin:6px 0 4px; font-size:13px;">Outbreak Surveillance</strong>
                <p class="ol-small ol-muted">Real-time provincial alert levels, quarantine corridors, and containment.</p>
                <a href="/mH/ddcr/outbreaks.html" class="ol-btn ol-btn-sm" style="width:100%; margin-top:8px;">View Outbreaks &rarr;</a>
            </div>
            <div style="background:#ffffff; border:1px solid #fecaca; border-radius:2px; padding:12px; text-align:center;">
                <div style="font-size:22px;">🔬</div>
                <strong style="display:block; margin:6px 0 4px; font-size:13px;">PubMed / Literature</strong>
                <p class="ol-small ol-muted">Live search across PubMed, PMC, and sovereign biomedical papers.</p>
                <a href="/mH/ddcr/search.html" class="ol-btn ol-btn-sm" style="width:100%; margin-top:8px;">Search Literature &rarr;</a>
            </div>
        </div>
    </div>

    <!-- Active Clinical Trials -->
    <div class="ol-card" id="trials">
        <div class="ol-card-title">
            <span>Active Sovereign Clinical Trials Registry</span>
            <span class="ol-badge-tag">Ethically Monitored</span>
        </div>
        <p>All clinical trials conducted within Sangaia adhere to the Declaration of Helsinki and strict informed consent protocols. Trial participants receive full medical oversight, transparent risk disclosure, and guaranteed post-trial therapy.</p>
        <div style="display:flex; flex-direction:column; gap:8px; margin-top:10px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:10px;">
                <strong>Trial SG-2026-ONC-04: Targeted Immunotherapy in Advanced Solid Tumors</strong>
                <div class="ol-small ol-muted">Columbia Regional Medical Center &bull; Phase II &bull; Enrollment Open</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:10px;">
                <strong>Trial SG-2026-NEU-11: Neural Regeneration in Traumatic Spinal Cord Injury</strong>
                <div class="ol-small ol-muted">Sentinel Memorial Hospital &bull; Phase I/II &bull; Clinical Observation Active</div>
            </div>
        </div>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>DDCR Direct Portal</h3>
        <p class="ol-small ol-muted">Access the dedicated Disease Control & Research system for epidemic surveillance and diagnostic databases.</p>
        <div class="ol-mt-10">
            <a href="/mH/ddcr/index.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center; background:#b91c1c; border-color:#991b1b;">Open DDCR Portal</a>
        </div>
    </div>
    """

    generate_page("healthcare_research.html", title, theme, "research", hero_title, hero_sub, "Ministry of Healthcare", "Innovation & DDCR", "Laboratories Active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS)
    generate_page("mH/research.html", title, theme, "research", hero_title, hero_sub, "Ministry of Healthcare", "Innovation & DDCR", "Laboratories Active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS_SUBDOMAIN)

def build_support_page():
    title = "Patient Support, Citizen Advocacy & Healthcare FAQ"
    theme = "theme-healthcare"
    hero_title = "Patient Support & Citizen Advocacy"
    hero_sub = "24/7 medical advice hotline, patient rights, hospital navigator, and comprehensive healthcare FAQ"

    sidebar_links = [
        {"label": "Patient Support Overview", "url": "#overview", "active": True},
        {"label": "Frequently Asked Questions", "url": "#faq", "active": False},
        {"label": "Patient Rights Charter", "url": "#rights", "active": False},
        {"label": "Medical Evacuation Hotline", "url": "#hotline", "active": False},
        {"label": "Patient Ombudsman Contact", "url": "#ombudsman", "active": False}
    ]

    main_content = """
    <!-- Patient Support Overview -->
    <div class="ol-card" id="overview">
        <div class="ol-card-title">
            <span>Patient Support &amp; Healthcare Navigation</span>
            <span class="ol-badge-tag ol-badge-success">Advocacy Services Free</span>
        </div>
        <p>The Patient Support Directorate assists citizens with hospital appointments, medical record transfers between provinces, accessibility accommodations, and grievance resolution. We ensure that every patient receives compassionate, prompt, and dignified care.</p>
    </div>

    <!-- Frequently Asked Questions -->
    <div class="ol-card" id="faq">
        <div class="ol-card-title">
            <span>Frequently Asked Questions</span>
            <span class="ol-badge-tag">Sangaia Health Mandate</span>
        </div>
        <div style="display:flex; flex-direction:column; gap:12px; margin-top:8px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:#b91c1c; font-size:14px;">How do I apply for healthcare?</strong>
                <p class="ol-small" style="margin-top:4px;">All citizens are automatically eligible for universal healthcare under the Sangaian Health Mandate upon receipt of their Sangaia ID. You can present your physical or digital Sangaia ID at any provincial clinic or hospital for immediate registration.</p>
            </div>

            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:#b91c1c; font-size:14px;">What does the Sangaian Health Charter cover?</strong>
                <p class="ol-small" style="margin-top:4px;">The Charter comprehensively covers preventative checkups, emergency room care, routine surgeries, organ transplants, mental health counseling, prescription medications on the national formulary, dental restorations, and corrective eye examinations at 100% state expense.</p>
            </div>

            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:#b91c1c; font-size:14px;">How do I find a doctor or specialist?</strong>
                <p class="ol-small" style="margin-top:4px;">You may schedule an appointment directly at any public hospital in New Jasper, New Madison, Liveland, Sentinel, or Columbia. Referrals for specialized surgical disciplines are issued within 48 hours by your primary care physician.</p>
            </div>

            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:#b91c1c; font-size:14px;">What do I do in an emergency?</strong>
                <p class="ol-small" style="margin-top:4px;">For life-threatening conditions, dial <strong>9-1-1</strong> immediately. For non-life-threatening medical guidance, you can call the 24/7 Sovereign Health Nurse Line at <strong>1-800-SANGAIA-CARE</strong>.</p>
            </div>
        </div>
    </div>

    <!-- Patient Rights Charter -->
    <div class="ol-card" id="rights">
        <div class="ol-card-title">
            <span>Patient Rights &amp; Legal Guarantees</span>
            <span class="ol-badge-tag">Statutory Protection</span>
        </div>
        <p>Every individual receiving care in Sangaia is legally guaranteed:</p>
        <ul style="margin:8px 0 0 20px; font-size:13px; line-height:1.6; color:#201f1e;">
            <li>The right to informed consent, complete treatment disclosure, and dignity.</li>
            <li>Zero surprise medical bills or commercial collection harassment.</li>
            <li>Cryptographic privacy of electronic medical records under sovereign data protection laws.</li>
            <li>Free interpretation services in any recognized regional or international language.</li>
        </ul>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>24/7 Patient Helpline</h3>
        <p class="ol-small ol-muted">Speak with a registered triage nurse or patient advocate toll-free anytime.</p>
        <div class="ol-mt-10">
            <button type="button" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; background:#b91c1c; border-color:#991b1b;" onclick="alert('Connecting to 24/7 Patient Nurse Line (Toll-Free 1-800-SANGAIA-CARE)...')">Call Nurse Line</button>
        </div>
    </div>
    """

    generate_page("healthcare_support.html", title, theme, "support", hero_title, hero_sub, "Ministry of Healthcare", "Advocacy & FAQ", "Support Available", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS)
    generate_page("mH/support.html", title, theme, "support", hero_title, hero_sub, "Ministry of Healthcare", "Advocacy & FAQ", "Support Available", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS_SUBDOMAIN)

def build_all_healthcare_secondary():
    build_hospitals_page()
    build_services_page()
    build_research_page()
    build_support_page()
    print("All 4 Healthcare secondary pages successfully restored and generated in One Live architecture!")

if __name__ == "__main__":
    build_all_healthcare_secondary()
