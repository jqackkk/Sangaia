#!/usr/bin/env python3
"""
Builds all 4 secondary Healthcare pages following the user's exact One Live Card Architecture:
1. healthcare_hospitals.html (& mH/hospitals.html)
2. healthcare_services.html (& mH/services.html)
3. healthcare_research.html (& mH/research.html)
4. healthcare_support.html (& mH/support.html)

Strict Rules Enforced:
- Every section is wrapped in clean One Live <section class="card" id="...">
- Sub-elements organized into .ol-grid-2 and .ol-grid-3 bordered sub-cards
- All navigation tabs, headings, badges, and button labels strictly in lowercase
- Segoe WP typography ('Segoe WP', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif)
- No $0.00 pricing listings (universal healthcare is guaranteed by constitutional charter)
- No social media features, telemetry, or personal face images
"""

import os
from generate_all_sites import generate_page

HEALTHCARE_NAV_TABS = [
    ("home", "healthcare home", "/healthcare.html"),
    ("departments", "departments", "/healthcare_departments.html"),
    ("services", "medical services", "/healthcare_services.html"),
    ("hospitals", "5-province hospitals", "/healthcare_hospitals.html"),
    ("research", "medical research", "/healthcare_research.html"),
    ("support", "patient support", "/healthcare_support.html"),
    ("ddcr", "ddcr disease control", "/mH/ddcr/index.html"),
    ("federal", "← federal portal", "/index.html"),
]

HEALTHCARE_NAV_TABS_SUBDOMAIN = [
    ("home", "healthcare home", "index.html"),
    ("departments", "departments", "departments.html"),
    ("services", "medical services", "services.html"),
    ("hospitals", "5-province hospitals", "hospitals.html"),
    ("research", "medical research", "research.html"),
    ("support", "patient support", "support.html"),
    ("ddcr", "ddcr disease control", "ddcr/index.html"),
    ("federal", "← federal portal", "https://sangaia.org/index.html"),
]

def build_hospitals_page():
    title = "5-Province Hospital Emergency Network & Regional Medical Centers"
    theme = "theme-healthcare"
    hero_title = "hospital emergency network & regional medical centers"
    hero_sub = "level 1 trauma care, acute intensive triage, and regional medical facilities across all 5 sovereign provinces"

    sidebar_links = [
        {"label": "overview & er triage", "url": "#overview", "active": True},
        {"label": "watson healthcare (new jasper)", "url": "#watson", "active": False},
        {"label": "new madison hospital (new madison)", "url": "#madison", "active": False},
        {"label": "suwannee emergency (liveland)", "url": "#suwannee", "active": False},
        {"label": "sentinel memorial hospital (sentinel)", "url": "#sentinel", "active": False},
        {"label": "columbia regional center (columbia)", "url": "#columbia", "active": False},
        {"label": "emergency protocols", "url": "#emergency-protocols", "active": False}
    ]

    main_content = """
    <!-- Hospital Network Overview -->
    <section class="card" id="overview">
        <div class="ol-card-title">
            <span>sangaia integrated hospital network</span>
            <span class="ol-badge-tag ol-badge-success">5 provincial centers active</span>
        </div>
        <p>sangaia boasts a fully integrated network of state-of-the-art public hospitals across all five sovereign provinces. every facility operates 24/7 acute trauma response, subsidized neonatal and pediatric wings, and emergency room care with zero out-of-pocket costs for registered citizens.</p>
        <div class="ol-grid-3" style="margin-top:14px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px; text-align:center;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600;">average er wait time</div>
                <div style="font-size:18px; font-weight:700; color:#b91c1c; margin:4px 0;">12 minutes</div>
                <div style="font-size:11px; color:#8a8886;">rapid triage standard</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px; text-align:center;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600;">acute trauma beds</div>
                <div style="font-size:18px; font-weight:700; color:#b91c1c; margin:4px 0;">240+ beds</div>
                <div style="font-size:11px; color:#8a8886;">100% acute capacity</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px; text-align:center;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600;">helipad capacity</div>
                <div style="font-size:18px; font-weight:700; color:#b91c1c; margin:4px 0;">5 / 5 bases</div>
                <div style="font-size:11px; color:#8a8886;">air medevac active</div>
            </div>
        </div>
    </section>

    <!-- Province 1: Watson Healthcare (New Jasper) -->
    <section class="card" id="watson">
        <div class="ol-card-title">
            <span>watson healthcare &bull; province of new jasper</span>
            <span class="ol-badge-tag">level 1 trauma center</span>
        </div>
        <div class="ol-grid-2" style="margin-top:12px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">facility location</div>
                <div style="font-weight:600; color:var(--text-main);">H0001 1st street, shesk, new jasper, 1-1000</div>
                <div class="ol-small ol-muted" style="margin-top:2px;">map reference: 506 4th st nw, jasper, fl 32052</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">emergency readiness</div>
                <div style="font-weight:600; color:#b91c1c;">24/7 triage &bull; 48 acute beds</div>
                <div class="ol-small ol-muted" style="margin-top:2px;">immediate trauma surgical response active</div>
            </div>
        </div>
        <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px; margin-top:10px;">
            <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">specialized clinical departments</div>
            <p class="ol-small" style="margin:0;">emergency medicine, cardiovascular surgery, pediatric icu, orthopedics, burn care unit.</p>
        </div>
        <div style="margin-top:12px;">
            <button type="button" class="ol-btn ol-btn-sm" onclick="alert('routing directions to watson healthcare (new jasper)...')">get driving directions &rarr;</button>
        </div>
    </section>

    <!-- Province 2: New Madison Hospital (New Madison) -->
    <section class="card" id="madison">
        <div class="ol-card-title">
            <span>new madison hospital &bull; province of new madison</span>
            <span class="ol-badge-tag">regional acute center</span>
        </div>
        <div class="ol-grid-2" style="margin-top:12px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">facility location</div>
                <div style="font-weight:600; color:var(--text-main);">H0002 2nd street, madison city, new madison, 1-2000</div>
                <div class="ol-small ol-muted" style="margin-top:2px;">map reference: 224 nw crane ave, madison, fl 32340</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">emergency readiness</div>
                <div style="font-weight:600; color:#b91c1c;">24/7 triage &bull; 36 acute beds</div>
                <div class="ol-small ol-muted" style="margin-top:2px;">dedicated stroke &amp; cardiovascular response unit</div>
            </div>
        </div>
        <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px; margin-top:10px;">
            <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">specialized clinical departments</div>
            <p class="ol-small" style="margin:0;">intensive care, maternal health, emergency pediatrics, dialysis unit, pulmonary medicine.</p>
        </div>
        <div style="margin-top:12px;">
            <button type="button" class="ol-btn ol-btn-sm" onclick="alert('routing directions to new madison hospital (new madison)...')">get driving directions &rarr;</button>
        </div>
    </section>

    <!-- Province 3: Suwannee Emergency (Liveland) -->
    <section class="card" id="suwannee">
        <div class="ol-card-title">
            <span>suwannee emergency hospital &bull; province of liveland</span>
            <span class="ol-badge-tag">rapid response center</span>
        </div>
        <div class="ol-grid-2" style="margin-top:12px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">facility location</div>
                <div style="font-weight:600; color:var(--text-main);">H0003 3rd street, oaks, liveland, 1-3000</div>
                <div class="ol-small ol-muted" style="margin-top:2px;">map reference: 1100 11th st sw, live oak, fl 32064</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">emergency readiness</div>
                <div style="font-weight:600; color:#b91c1c;">24/7 triage &bull; 40 acute beds</div>
                <div class="ol-small ol-muted" style="margin-top:2px;">coastal disaster relief wing &amp; helipad dispatch</div>
            </div>
        </div>
        <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px; margin-top:10px;">
            <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">specialized clinical departments</div>
            <p class="ol-small" style="margin:0;">rapid emergency triage, acute medical care, helipad dispatch, surgical suites, maritime trauma.</p>
        </div>
        <div style="margin-top:12px;">
            <button type="button" class="ol-btn ol-btn-sm" onclick="alert('routing directions to suwannee emergency (liveland)...')">get driving directions &rarr;</button>
        </div>
    </section>

    <!-- Province 4: Sentinel Memorial Hospital (Sentinel) -->
    <section class="card" id="sentinel">
        <div class="ol-card-title">
            <span>sentinel memorial hospital &bull; province of sentinel</span>
            <span class="ol-badge-tag">neurological &amp; trauma hub</span>
        </div>
        <div class="ol-grid-2" style="margin-top:12px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">facility location</div>
                <div style="font-weight:600; color:var(--text-main);">H0004 4th street, sentinel ridge, sentinel, 1-4000</div>
                <div class="ol-small ol-muted" style="margin-top:2px;">map reference: 168 nw main blvd, lake city, fl 32055</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">emergency readiness</div>
                <div style="font-weight:600; color:#b91c1c;">24/7 triage &bull; 54 acute beds</div>
                <div class="ol-small ol-muted" style="margin-top:2px;">advanced ct / mri diagnostic suite &bull; highland triage</div>
            </div>
        </div>
        <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px; margin-top:10px;">
            <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">specialized clinical departments</div>
            <p class="ol-small" style="margin:0;">specialized neurological wing, orthopedic surgery, universal emergency care, burn center, hypothermia triage.</p>
        </div>
        <div style="margin-top:12px;">
            <button type="button" class="ol-btn ol-btn-sm" onclick="alert('routing directions to sentinel memorial hospital (sentinel)...')">get driving directions &rarr;</button>
        </div>
    </section>

    <!-- Province 5: Columbia Regional Medical Center (Columbia) -->
    <section class="card" id="columbia">
        <div class="ol-card-title">
            <span>columbia regional medical center &bull; province of columbia</span>
            <span class="ol-badge-tag">comprehensive medical hub</span>
        </div>
        <div class="ol-grid-2" style="margin-top:12px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">facility location</div>
                <div style="font-weight:600; color:var(--text-main);">H0005 5th street, columbia city, columbia, 1-5000</div>
                <div class="ol-small ol-muted" style="margin-top:2px;">map reference: 4288 sw state road 47, lake city, fl 32024</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">emergency readiness</div>
                <div style="font-weight:600; color:#b91c1c;">24/7 triage &bull; 62 acute beds</div>
                <div class="ol-small ol-muted" style="margin-top:2px;">state-level pandemic isolation wing &bull; advanced oncology hub</div>
            </div>
        </div>
        <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px; margin-top:10px;">
            <div style="font-size:11px; color:#605e5c; text-transform:lowercase; font-weight:600; margin-bottom:4px;">specialized clinical departments</div>
            <p class="ol-small" style="margin:0;">regional oncology center, neonatal icu, sovereign healthcare research hub, clinical toxicology, genetic medicine.</p>
        </div>
        <div style="margin-top:12px;">
            <button type="button" class="ol-btn ol-btn-sm" onclick="alert('routing directions to columbia regional medical center (columbia)...')">get driving directions &rarr;</button>
        </div>
    </section>

    <!-- Emergency Protocols -->
    <section class="card" id="emergency-protocols">
        <div class="ol-card-title">
            <span>emergency medical transport &amp; ambulance dispatch</span>
            <span class="ol-badge-tag" style="background:#b91c1c; color:#fff; border-color:#991b1b;">hotline: 9-1-1</span>
        </div>
        <div class="ol-grid-2" style="margin-top:12px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:#b91c1c; font-size:13px; display:block; margin-bottom:4px;">life-threatening emergencies</strong>
                <p class="ol-small ol-muted" style="margin:0;">for chest pain, severe hemorrhage, respiratory distress, or acute trauma, dial <strong>9-1-1</strong> immediately for rapid paramedic response.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">100% sovereign funded dispatch</strong>
                <p class="ol-small ol-muted" style="margin:0;">ground ambulances, mobile triage units, and air medevac helicopters operate with zero out-of-pocket bills for all residents.</p>
            </div>
        </div>
    </section>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>emergency dispatch</h3>
        <p class="ol-small ol-muted">24/7 sovereign triage dispatchers standing by across new jasper, new madison, liveland, sentinel, and columbia.</p>
        <div class="ol-mt-10">
            <a href="tel:911" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center; background:#b91c1c; border-color:#991b1b;">dial emergency 9-1-1</a>
        </div>
    </div>
    <div class="ol-sidebox">
        <h3>statutory health directory</h3>
        <p class="ol-small ol-muted">explore statutory departments, health licenses, and clinical standards.</p>
        <div class="ol-mt-10">
            <a href="/healthcare_departments.html" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">launch departments</a>
        </div>
    </div>
    """

    generate_page("healthcare_hospitals.html", title, theme, "hospitals", hero_title, hero_sub, "ministry of healthcare", "5-province hospital network", "ers active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS)
    generate_page("mH/hospitals.html", title, theme, "hospitals", hero_title, hero_sub, "ministry of healthcare", "5-province hospital network", "ers active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS_SUBDOMAIN)

def build_services_page():
    title = "Comprehensive Medical Services & The Sangaian Health Charter"
    theme = "theme-healthcare"
    hero_title = "comprehensive medical services"
    hero_sub = "guaranteed universal coverage, preventative care, and specialized surgery across all 5 provinces"

    sidebar_links = [
        {"label": "the sangaian health charter", "url": "#charter", "active": True},
        {"label": "comprehensive care catalog", "url": "#catalog", "active": False},
        {"label": "prescription drug coverage", "url": "#pharmacy", "active": False},
        {"label": "dental & vision healthcare", "url": "#dental-vision", "active": False},
        {"label": "mental health & wellness", "url": "#mental-health", "active": False}
    ]

    main_content = """
    <!-- The Sangaian Health Charter -->
    <section class="card" id="charter">
        <div class="ol-card-title">
            <span>the sangaian health charter</span>
            <span class="ol-badge-tag ol-badge-success">constitutional right</span>
        </div>
        <p>the sangaian health charter establishes that healthcare is a fundamental civic entitlement, not a commodity. under article iv of the sovereign constitution, no citizen or authorized resident shall ever be turned away from medical treatment, denied medications, or driven into debt due to illness.</p>
        <div class="ol-grid-2" style="margin-top:14px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">constitutional guarantee</strong>
                <p class="ol-small ol-muted" style="margin:0;">universal access to level 1 trauma surgery, acute intensive triage, and preventative wellness across all 5 sovereign provinces.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">100% public funding</strong>
                <p class="ol-small ol-muted" style="margin:0;">zero out-of-pocket medical debt, surprise bills, or private insurer denials. funded directly from sovereign public revenue.</p>
            </div>
        </div>
    </section>

    <!-- Comprehensive Care Catalog -->
    <section class="card" id="catalog">
        <div class="ol-card-title">
            <span>comprehensive healthcare services</span>
            <span class="ol-badge-tag">all provincial facilities</span>
        </div>
        <p class="ol-small ol-muted">statutory medical procedures provided at all accredited public healthcare facilities:</p>
        <table class="ol-table" style="margin-top:10px;">
            <thead>
                <tr>
                    <th>service discipline</th>
                    <th>covered procedures</th>
                    <th>provincial availability</th>
                    <th>coverage status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>primary care</strong></td>
                    <td>annual physicals, chronic illness management, pediatric wellness, vaccinations</td>
                    <td>all 5 provinces</td>
                    <td><span class="ol-badge-tag ol-badge-success">universal public coverage</span></td>
                </tr>
                <tr>
                    <td><strong>emergency &amp; trauma</strong></td>
                    <td>24/7 er triage, acute surgery, intensive care, burn care, air ambulance</td>
                    <td>all 5 provinces</td>
                    <td><span class="ol-badge-tag ol-badge-success">universal public coverage</span></td>
                </tr>
                <tr>
                    <td><strong>specialty surgery</strong></td>
                    <td>cardiothoracic, orthopedic, neurosurgery, oncological resections</td>
                    <td>regional hubs</td>
                    <td><span class="ol-badge-tag ol-badge-success">universal public coverage</span></td>
                </tr>
                <tr>
                    <td><strong>maternal &amp; infant</strong></td>
                    <td>prenatal care, birthing suites, neonatal intensive care, postnatal visits</td>
                    <td>all 5 provinces</td>
                    <td><span class="ol-badge-tag ol-badge-success">universal public coverage</span></td>
                </tr>
                <tr>
                    <td><strong>diagnostic imaging</strong></td>
                    <td>mri, ct scans, ultrasound, x-ray, digital lab bloodwork</td>
                    <td>all 5 provinces</td>
                    <td><span class="ol-badge-tag ol-badge-success">universal public coverage</span></td>
                </tr>
            </tbody>
        </table>
    </section>

    <!-- Prescription Drug Coverage -->
    <section class="card" id="pharmacy">
        <div class="ol-card-title">
            <span>prescription drug formulary &amp; local dispensaries</span>
            <span class="ol-badge-tag ol-badge-success">100% sovereign funded</span>
        </div>
        <p class="ol-small ol-muted">all essential maintenance medications are categorized under tier 1 of the sovereign formulary and dispensed without fees through accredited public hospital pharmacies.</p>
        <div class="ol-grid-2" style="margin-top:14px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">essential life-support therapeutics</strong>
                <p class="ol-small ol-muted" style="margin:0;">human biosimilar insulin (all formats), cardiovascular regulators, statins, and anti-arrhythmic agents.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">broad-spectrum anti-infectives</strong>
                <p class="ol-small ol-muted" style="margin:0;">penicillins, cephalosporins, macrolides, and antivirals available on-demand at hospital dispensaries.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">pulmonary &amp; respiratory inhalers</strong>
                <p class="ol-small ol-muted" style="margin:0;">maintenance corticosteroids, rescue bronchodilators (salbutamol), and pediatric nebulizer solutions.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">oncological &amp; autoimmune medications</strong>
                <p class="ol-small ol-muted" style="margin:0;">targeted immunotherapies, chemotherapy infusions, and rheumatological biologics fully covered.</p>
            </div>
        </div>
    </section>

    <!-- Dental & Vision -->
    <section class="card" id="dental-vision">
        <div class="ol-card-title">
            <span>dental, vision &amp; auditory care</span>
            <span class="ol-badge-tag">universal inclusions</span>
        </div>
        <p class="ol-small ol-muted">unlike commercial regimes, sangaia treats oral and sensory wellbeing as inseparable from bodily health.</p>
        <div class="ol-grid-3" style="margin-top:14px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">preventative &amp; restorative dental</strong>
                <p class="ol-small ol-muted" style="margin:0;">annual examinations, ultrasonic prophylaxis, composite restorations, and endodontic therapy.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">optometry &amp; corrective lenses</strong>
                <p class="ol-small ol-muted" style="margin:0;">comprehensive eye exams, digital retinal imaging, and standard prescription eyewear.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">audiology &amp; hearing support</strong>
                <p class="ol-small ol-muted" style="margin:0;">diagnostic hearing screenings, inner-ear consultations, and sovereign digital hearing aids.</p>
            </div>
        </div>
    </section>

    <!-- Mental Health & Wellness -->
    <section class="card" id="mental-health">
        <div class="ol-card-title">
            <span>mental health, counseling &amp; addiction support</span>
            <span class="ol-badge-tag">confidential &bull; universal</span>
        </div>
        <p class="ol-small ol-muted">mental healthcare is accessible without referral. citizens may book confidential therapy sessions, psychiatric consultations, or residential holistic recovery programs with complete medical privacy.</p>
        <div class="ol-grid-3" style="margin-top:14px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">individual &amp; family therapy</strong>
                <p class="ol-small ol-muted" style="margin:0;">confidential psychotherapy, cognitive behavioral support, and family counseling.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">24/7 crisis de-escalation</strong>
                <p class="ol-small ol-muted" style="margin:0;">specialized medical crisis teams dispatched with zero law enforcement or punitive response.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">holistic recovery programs</strong>
                <p class="ol-small ol-muted" style="margin:0;">provincial retreat centers offering addiction rehabilitation, peer mentorship, and wellness.</p>
            </div>
        </div>
    </section>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>patient health charter</h3>
        <p class="ol-small ol-muted">download the official sangaia health charter detailing universal constitutional coverage protections.</p>
        <div class="ol-mt-10">
            <a href="javascript:void(0)" onclick="alert('downloading sangaia patient health charter (.pdf)...')" class="ol-btn ol-btn-sm" style="width:100%; text-align:center;">download health charter (.pdf)</a>
        </div>
    </div>
    """

    generate_page("healthcare_services.html", title, theme, "services", hero_title, hero_sub, "ministry of healthcare", "universal health charter", "services active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS)
    generate_page("mH/services.html", title, theme, "services", hero_title, hero_sub, "ministry of healthcare", "universal health charter", "services active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS_SUBDOMAIN)

def build_research_page():
    title = "Medical Research, Clinical Trials & DDCR Liaison"
    theme = "theme-healthcare"
    hero_title = "medical research & development directorate"
    hero_sub = "ethical clinical trials, open-access biomedical literature, non-commercial patents & disease surveillance"

    sidebar_links = [
        {"label": "research & ethics mandate", "url": "#overview", "active": True},
        {"label": "ddcr portal gateway", "url": "#ddcr-gateway", "active": False},
        {"label": "active clinical trials", "url": "#trials", "active": False},
        {"label": "biomedical standards", "url": "#standards", "active": False},
        {"label": "provincial labs", "url": "#labs", "active": False}
    ]

    main_content = """
    <!-- Medical Research & Development -->
    <section class="card" id="overview">
        <div class="ol-card-title">
            <span>medical research &amp; non-commercial innovation</span>
            <span class="ol-badge-tag ol-badge-success">open access</span>
        </div>
        <p>the ministry of healthcare invests heavily in the future of sovereign medicine. all medical research funded by sangaia is held in public trust with open-source patent licenses, guaranteeing that breakthroughs in oncology, genomics, and infectious disease treatments remain globally accessible and free from monopolistic price-gouging.</p>
        <div class="ol-grid-2" style="margin-top:14px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">open patent sovereignty</strong>
                <p class="ol-small ol-muted" style="margin:0;">all government-funded research is placed directly into the public domain, preventing commercial patent lockouts.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">ethical trial mandate</strong>
                <p class="ol-small ol-muted" style="margin:0;">rigorous compliance with the declaration of helsinki, transparent safety reporting, and guaranteed lifetime patient monitoring.</p>
            </div>
        </div>
    </section>

    <!-- DDCR Gateway Card -->
    <section class="card" id="ddcr-gateway" style="border: 2px solid #b91c1c; background: #fffdfd;">
        <div class="ol-card-title">
            <span style="color:#b91c1c; font-size:15px;">department of disease control &amp; research (ddcr)</span>
            <span class="ol-badge-tag" style="background:#b91c1c; color:#fff; border-color:#991b1b;">sovereign cdc</span>
        </div>
        <p>looking for specific health topics, epidemic guidelines, outbreak surveillance, or biomedical research papers? the ddcr maintains our comprehensive national repository:</p>
        <div class="ol-grid-3" style="margin-top:14px;">
            <div style="background:#ffffff; border:1px solid #fecaca; border-radius:2px; padding:12px; text-align:center;">
                <div style="font-size:22px;">📚</div>
                <strong style="display:block; margin:6px 0 4px; font-size:13px;">health topics (a-z)</strong>
                <p class="ol-small ol-muted">verified disease symptom guides and clinical treatment protocols.</p>
                <a href="/mH/ddcr/health_topics.html" class="ol-btn ol-btn-sm" style="width:100%; margin-top:8px;">browse topics &rarr;</a>
            </div>
            <div style="background:#ffffff; border:1px solid #fecaca; border-radius:2px; padding:12px; text-align:center;">
                <div style="font-size:22px;">⚠️</div>
                <strong style="display:block; margin:6px 0 4px; font-size:13px;">outbreak surveillance</strong>
                <p class="ol-small ol-muted">real-time provincial alert levels, quarantine corridors, and containment.</p>
                <a href="/mH/ddcr/outbreaks.html" class="ol-btn ol-btn-sm" style="width:100%; margin-top:8px;">view outbreaks &rarr;</a>
            </div>
            <div style="background:#ffffff; border:1px solid #fecaca; border-radius:2px; padding:12px; text-align:center;">
                <div style="font-size:22px;">🔬</div>
                <strong style="display:block; margin:6px 0 4px; font-size:13px;">pubmed / literature</strong>
                <p class="ol-small ol-muted">live search across pubmed, pmc, and sovereign biomedical papers.</p>
                <a href="/mH/ddcr/search.html" class="ol-btn ol-btn-sm" style="width:100%; margin-top:8px;">search literature &rarr;</a>
            </div>
        </div>
    </section>

    <!-- Active Clinical Trials -->
    <section class="card" id="trials">
        <div class="ol-card-title">
            <span>active sovereign clinical trials registry</span>
            <span class="ol-badge-tag">ethically monitored</span>
        </div>
        <p class="ol-small ol-muted">all clinical trials conducted within sangaia adhere to strict informed consent protocols:</p>
        <div class="ol-grid-2" style="margin-top:14px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:14px;">
                <strong style="color:#b91c1c; font-size:13.5px; display:block; margin-bottom:4px;">trial sg-2026-onc-04: targeted solid tumor immunotherapy</strong>
                <div class="ol-small ol-muted" style="margin-bottom:6px;">columbia regional medical center &bull; phase ii &bull; enrollment active</div>
                <p class="ol-small" style="margin:0;">assessing personalized neoantigen peptide vaccines for advanced colorectal and pulmonary carcinomas.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:14px;">
                <strong style="color:#b91c1c; font-size:13.5px; display:block; margin-bottom:4px;">trial sg-2026-neu-11: neural regeneration in spinal trauma</strong>
                <div class="ol-small ol-muted" style="margin-bottom:6px;">sentinel memorial hospital &bull; phase i/ii &bull; observation active</div>
                <p class="ol-small" style="margin:0;">testing biocompatible axonal growth scaffolds paired with electrical neuro-stimulation therapies.</p>
            </div>
        </div>
    </section>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>ddcr direct portal</h3>
        <p class="ol-small ol-muted">access the dedicated disease control &amp; research system for epidemic surveillance and diagnostic databases.</p>
        <div class="ol-mt-10">
            <a href="/mH/ddcr/index.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center; background:#b91c1c; border-color:#991b1b;">open ddcr portal</a>
        </div>
    </div>
    """

    generate_page("healthcare_research.html", title, theme, "research", hero_title, hero_sub, "ministry of healthcare", "innovation & ddcr", "laboratories active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS)
    generate_page("mH/research.html", title, theme, "research", hero_title, hero_sub, "ministry of healthcare", "innovation & ddcr", "laboratories active", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS_SUBDOMAIN)

def build_support_page():
    title = "Patient Support, Citizen Advocacy & Healthcare FAQ"
    theme = "theme-healthcare"
    hero_title = "patient support & citizen advocacy"
    hero_sub = "24/7 medical advice hotline, patient rights, hospital navigator, and comprehensive healthcare faq"

    sidebar_links = [
        {"label": "patient support overview", "url": "#overview", "active": True},
        {"label": "frequently asked questions", "url": "#faq", "active": False},
        {"label": "patient rights charter", "url": "#rights", "active": False},
        {"label": "medical evacuation hotline", "url": "#hotline", "active": False},
        {"label": "patient ombudsman contact", "url": "#ombudsman", "active": False}
    ]

    main_content = """
    <!-- Patient Support Overview -->
    <section class="card" id="overview">
        <div class="ol-card-title">
            <span>patient support &amp; healthcare navigation</span>
            <span class="ol-badge-tag ol-badge-success">advocacy services free</span>
        </div>
        <p>the patient support directorate assists citizens with hospital appointments, medical record transfers between provinces, accessibility accommodations, and grievance resolution. we ensure that every patient receives compassionate, prompt, and dignified care.</p>
        <div class="ol-grid-2" style="margin-top:14px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">inter-provincial chart synchronization</strong>
                <p class="ol-small ol-muted" style="margin:0;">unified electronic health records accessible instantly across all 5 provincial medical centers.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">independent ombudsman council</strong>
                <p class="ol-small ol-muted" style="margin:0;">direct citizen advocacy for patient rights, clinical review appeals, and language accommodations.</p>
            </div>
        </div>
    </section>

    <!-- Frequently Asked Questions -->
    <section class="card" id="faq">
        <div class="ol-card-title">
            <span>frequently asked questions</span>
            <span class="ol-badge-tag">sangaia health mandate</span>
        </div>
        <div class="ol-grid-2" style="margin-top:14px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:14px;">
                <strong style="color:#b91c1c; font-size:13.5px; display:block; margin-bottom:6px;">how do i apply for healthcare?</strong>
                <p class="ol-small" style="margin:0; line-height:1.5;">all citizens are automatically eligible for universal healthcare under the sangaian health mandate upon receipt of their sangaia id. you can present your physical or digital sangaia id at any provincial clinic or hospital for immediate registration.</p>
            </div>

            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:14px;">
                <strong style="color:#b91c1c; font-size:13.5px; display:block; margin-bottom:6px;">what does the sangaian health charter cover?</strong>
                <p class="ol-small" style="margin:0; line-height:1.5;">the charter comprehensively covers preventative checkups, emergency room care, routine surgeries, organ transplants, mental health counseling, prescription medications on the national formulary, dental restorations, and corrective eye examinations at 100% state expense.</p>
            </div>

            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:14px;">
                <strong style="color:#b91c1c; font-size:13.5px; display:block; margin-bottom:6px;">how do i find a doctor or specialist?</strong>
                <p class="ol-small" style="margin:0; line-height:1.5;">you may schedule an appointment directly at any public hospital in new jasper, new madison, liveland, sentinel, or columbia. referrals for specialized surgical disciplines are issued within 48 hours by your primary care physician.</p>
            </div>

            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:14px;">
                <strong style="color:#b91c1c; font-size:13.5px; display:block; margin-bottom:6px;">what do i do in an emergency?</strong>
                <p class="ol-small" style="margin:0; line-height:1.5;">for life-threatening conditions, dial <strong>9-1-1</strong> immediately. for non-life-threatening medical guidance, you can call the 24/7 sovereign health nurse line at <strong>1-800-sangaia-care</strong>.</p>
            </div>
        </div>
    </section>

    <!-- Patient Rights Charter -->
    <section class="card" id="rights">
        <div class="ol-card-title">
            <span>patient rights &amp; legal guarantees</span>
            <span class="ol-badge-tag">statutory protection</span>
        </div>
        <p class="ol-small ol-muted">every individual receiving care in sangaia is legally guaranteed ironclad protections:</p>
        <div class="ol-grid-2" style="margin-top:14px;">
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">informed consent &amp; dignity</strong>
                <p class="ol-small ol-muted" style="margin:0;">the absolute right to full treatment disclosure, second opinions, and respectful care.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">zero out-of-pocket billing</strong>
                <p class="ol-small ol-muted" style="margin:0;">constitutional ban on surprise fees, debt collection, and commercial medical liens.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">cryptographic record privacy</strong>
                <p class="ol-small ol-muted" style="margin:0;">electronic medical charts encrypted under sovereign individual key ownership.</p>
            </div>
            <div style="background:#f8fafc; border:1px solid #e1dfdd; border-radius:2px; padding:12px;">
                <strong style="color:var(--text-main); font-size:13px; display:block; margin-bottom:4px;">free language interpretation</strong>
                <p class="ol-small ol-muted" style="margin:0;">certified multilingual medical interpreters available 24/7 in-person or via live video.</p>
            </div>
        </div>
    </section>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>24/7 patient helpline</h3>
        <p class="ol-small ol-muted">speak with a registered triage nurse or patient advocate toll-free anytime.</p>
        <div class="ol-mt-10">
            <button type="button" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; background:#b91c1c; border-color:#991b1b;" onclick="alert('connecting to 24/7 patient nurse line (toll-free 1-800-sangaia-care)...')">call nurse line</button>
        </div>
    </div>
    """

    generate_page("healthcare_support.html", title, theme, "support", hero_title, hero_sub, "ministry of healthcare", "advocacy & faq", "support available", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS)
    generate_page("mH/support.html", title, theme, "support", hero_title, hero_sub, "ministry of healthcare", "advocacy & faq", "support available", sidebar_links, main_content, sidebar_right, custom_nav_tabs=HEALTHCARE_NAV_TABS_SUBDOMAIN)

def build_all_healthcare_secondary():
    build_hospitals_page()
    build_services_page()
    build_research_page()
    build_support_page()

if __name__ == "__main__":
    print("rebuilding all 4 healthcare pages with clean one live card architecture...")
    build_all_healthcare_secondary()
    print("all 4 healthcare secondary pages successfully restored and generated in one live architecture!")
