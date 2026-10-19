#!/usr/bin/env python3
"""
Sangaia Live Ministry Homepages Generator
Builds the 9 Ministry Homepages in the exact One Live Wave 4 architecture,
preserving all rich interactive tools, calculators, calendars, blog posts, audio player,
and telemetry widgets.
"""

import os
import shutil
from generate_all_sites import generate_page
from build_departments import MINISTRY_NAV_TABS, get_subdomain_nav_tabs
from build_healthcare_pages import build_all_healthcare_secondary

# -----------------------------------------------------------------------------
# 1. MINISTRY OF THE EXECUTIVE (MoEX)
# -----------------------------------------------------------------------------
def build_executive():
    title = "Ministry of the Executive & Office of the Aeretocrat"
    theme = "theme-executive"
    tab = "executive"
    hero_title = "office of the aeretocrat & ministry of the executive"
    hero_sub = "Whole-of-government administration, the Cabinet, constitutional decrees & the Aeretocrat's Journal"

    sidebar_links = [
        {"label": "Overview & Mandate", "url": "#overview", "active": True},
        {"label": "Aeretocrat's Journal", "url": "#journal", "active": False},
        {"label": "Macroeconomics & GDP", "url": "#macroeconomics", "active": False},
        {"label": "National Budget & Surplus", "url": "#national-budget", "active": False},
        {"label": "Constitutional Framework", "url": "#constitutional-framework", "active": False},
        {"label": "Executive Calendar & Hearings", "url": "#calendar", "active": False},
        {"label": "Departments Portal →", "url": "/executive_departments.html", "active": False}
    ]

    main_content = """

    <!-- Executive Dispatches & Philosophical Treatises Docket -->
    <div class="card" id="overview"><a id="journal"></a>
        <div class="ol-card-title">
            <span>Executive Dispatches &amp; Philosophical Treatises</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openAskModal()">File Official Inquiry</button>
        </div>
        <p class="ol-small ol-muted">Official philosophical treatises, civic virtue dissertations, and executive addresses promulgated by the Office of the Aeretocrat.</p>

        <div class="docket-entry">
            <div class="docket-entry-header">
                <div>
                    <span class="mif-file-text" style="color:var(--primary); margin-right:6px;"></span>
                    <a href="javascript:void(0)" onclick="openDispatch(1)" class="docket-entry-title">On the Moral Necessity of Sovereign Solvency</a>
                </div>
                <span class="ol-badge-tag">Macroeconomics</span>
            </div>
            <p class="docket-entry-body">&ldquo;A nation that borrows from predatory international banking cartels sells the birthright of its unborn generations. In Sangaia, our constitutional prohibition on foreign sovereign debt is not merely fiscal prudence—it is our absolute shield of national liberty.&rdquo;</p>
            <div class="docket-entry-meta">Promulgated October 19, 2026 &bull; Official Dispatch No. EX-2026-08 &bull; <a href="javascript:void(0)" onclick="openDispatch(1)">Read Full Dispatch &rarr;</a></div>
        </div>

        <div class="docket-entry">
            <div class="docket-entry-header">
                <div>
                    <span class="mif-file-text" style="color:var(--primary); margin-right:6px;"></span>
                    <a href="javascript:void(0)" onclick="openDispatch(2)" class="docket-entry-title">Why the Aeretocracy Replaces Partisan Strife</a>
                </div>
                <span class="ol-badge-tag">Political Philosophy</span>
            </div>
            <p class="docket-entry-body">&ldquo;Party systems do not encourage debate; they encourage tribal warfare funded by oligarchs. By aligning ministerial councils with strict meritocratic and constitutional virtues, we ensure every decision serves the common good.&rdquo;</p>
            <div class="docket-entry-meta">Promulgated October 12, 2026 &bull; Official Dispatch No. EX-2026-07 &bull; <a href="javascript:void(0)" onclick="openDispatch(2)">Read Full Dispatch &rarr;</a></div>
        </div>

        <div class="docket-entry">
            <div class="docket-entry-header">
                <div>
                    <span class="mif-file-text" style="color:var(--primary); margin-right:6px;"></span>
                    <a href="javascript:void(0)" onclick="openDispatch(3)" class="docket-entry-title">Harmonizing the Five Sovereign Provinces</a>
                </div>
                <span class="ol-badge-tag">Federalism</span>
            </div>
            <p class="docket-entry-body">&ldquo;From the coastal harbors of Liveland to the highlands of Sentinel, New Jasper, New Madison, and Columbia, our diversity is our endurance. Let each province foster its unique traditions within our unbreakable union.&rdquo;</p>
            <div class="docket-entry-meta">Promulgated October 5, 2026 &bull; Official Dispatch No. EX-2026-06 &bull; <a href="javascript:void(0)" onclick="openDispatch(3)">Read Full Dispatch &rarr;</a></div>
        </div>
    </div>

    <!-- Macroeconomics & GDP -->
    <div class="ol-card" id="macroeconomics">
        <div class="ol-card-title">
            <span>Macroeconomic Telemetry &amp; National GDP</span>
            <span class="ol-badge-tag ol-badge-success">Q3 FY2026 Verified</span>
        </div>
        <div class="ol-grid-3" style="margin-bottom:14px;">
            <div class="ol-metric-box">
                <div class="ol-metric-val">$ 482.4 B</div>
                <div class="ol-metric-lbl">Gross Domestic Product</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">+ 4.8%</div>
                <div class="ol-metric-lbl">Annual Real GDP Growth</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">$ 68,920</div>
                <div class="ol-metric-lbl">GDP Per Capita</div>
            </div>
        </div>
        <table class="ol-table">
            <thead>
                <tr>
                    <th>Provincial Territory</th>
                    <th>Regional GDP</th>
                    <th>Leading Economic Sector</th>
                    <th>Labor Force Participation</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>New Jasper (Capital Shesk)</td><td>$ 142.1 B</td><td>Advanced Technology &amp; Governance</td><td>84.2%</td></tr>
                <tr><td>New Madison (Madison City)</td><td>$ 118.6 B</td><td>Bio-Agriculture &amp; Manufacturing</td><td>81.9%</td></tr>
                <tr><td>Liveland (Oaks)</td><td>$ 94.3 B</td><td>Maritime Logistics &amp; Aquaculture</td><td>83.1%</td></tr>
                <tr><td>Sentinel (Sentinel Ridge)</td><td>$ 68.2 B</td><td>Mineral Stewardship &amp; Clean Energy</td><td>79.4%</td></tr>
                <tr><td>Columbia (Columbia City)</td><td>$ 59.2 B</td><td>Cultural Arts &amp; Aerospace Research</td><td>82.6%</td></tr>
            </tbody>
        </table>
    </div>

    <!-- National Budget & Surplus -->
    <div class="ol-card" id="national-budget">
        <div class="ol-card-title">
            <span>National Budget &amp; Sovereign Fiscal Surplus</span>
            <span class="ol-badge-tag ol-badge-success">Zero Foreign Debt</span>
        </div>
        <p class="ol-small ol-muted">In accordance with Constitutional Mandate, statutory federal expenses are 100% matched with collected land resource royalties, enterprise duties, and excise surpluses.</p>
        <div class="ol-grid-2" style="margin-top:10px;">
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong style="color:#1e3a8a;">Total Federal Revenues (FY2026):</strong>
                <div style="font-size:20px; font-weight:700; color:#1e3a8a; margin:4px 0;">$ 114.8 Billion</div>
                <div class="ol-small ol-muted">Land Use Royalties: 42% &bull; Progressive Surcharges: 34% &bull; Tariffs: 24%</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong style="color:#166534;">Statutory Net Surplus:</strong>
                <div style="font-size:20px; font-weight:700; color:#166534; margin:4px 0;">+ $ 11.2 Billion</div>
                <div class="ol-small ol-muted">Directed to Sovereign Solidarity Reserve Fund &amp; Provincial Biome Trust.</div>
            </div>
        </div>
    </div>

    <!-- Constitutional Framework -->
    <div class="ol-card" id="constitutional-framework">
        <div class="ol-card-title">
            <span>Constitutional Framework &amp; Sovereign Decrees</span>
            <a class="ol-title-link" href="/societal_press.html">Official Gazette &rarr;</a>
        </div>
        <p class="ol-small">The Constitution of the United Provinces of Sangaia establishes an unalterable framework of checks and virtues:</p>
        <ul class="ol-small" style="line-height:1.6;">
            <li><strong>Executive Decree No. 101:</strong> Prohibition of Foreign Debt and Predatory Compound Interest Banking.</li>
            <li><strong>Executive Decree No. 102:</strong> Guarantee of Universal Healthcare and Zero Out-of-Pocket Point-of-Service Fees.</li>
            <li><strong>Executive Decree No. 103:</strong> Sovereign Standard Units Decree: Officialization of the Panotherm (&deg;Пт) and Monomer (Мн).</li>
            <li><strong>Executive Decree No. 104:</strong> Civic Whistleblower Protection and Mandatory Wealth Redistribution for Religious Tithes.</li>
        </ul>
    </div>

    <!-- Executive Calendar & Hearings -->
    <div class="ol-card" id="calendar">
        <div class="ol-card-title">
            <span>Executive Council Calendar &amp; Public Hearings</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openHearingModal()">Request Public Hearing</button>
        </div>
        <table class="ol-table">
            <thead>
                <tr>
                    <th>Date &amp; Time</th>
                    <th>Convening Body</th>
                    <th>Agenda &amp; Matters of State</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Oct 22, 2026 &bull; 10:00</td>
                    <td>Cabinet of Ministers</td>
                    <td>Review of Q4 Biome Allocations &amp; Provincial Road Telemetry</td>
                    <td><span class="ol-badge-tag ol-badge-success">Open Public Gallery</span></td>
                </tr>
                <tr>
                    <td>Oct 26, 2026 &bull; 14:00</td>
                    <td>High Magistrates &amp; Aeretocrat</td>
                    <td>Adjudication of Interprovincial Commerce Pacts</td>
                    <td><span class="ol-badge-tag ol-badge-warning">Live Audio Streamed</span></td>
                </tr>
                <tr>
                    <td>Nov 02, 2026 &bull; 09:30</td>
                    <td>Civic Petitioners Assembly</td>
                    <td>Direct Citizen Hearings on Environmental Conservation</td>
                    <td><span class="ol-badge-tag ol-badge-success">Petitions Open</span></td>
                </tr>
            </tbody>
        </table>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Aeretocrat Profile</h3>
        <p class="ol-small ol-muted">Office of the Supreme Executive Magistrate &amp; Aeretocrat of the Sovereign Republic of Sangaia.</p>
        <div class="ol-mt-10">
            <a href="/executive_departments.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">Launch Executive Departments</a>
        </div>
    </div>
    """

    modals = """
    <!-- Ask Aeretocrat Modal -->
    <div class="ol-modal-overlay" id="askModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Submit Inquiry to the Office of the Aeretocrat</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('askModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Citizen Name / Sangaia ID</label>
                <input type="text" class="ol-input" id="ask-name" placeholder="Citizen Name or SG-XXXX">
            </div>
            <div class="form-group">
                <label class="form-label">Provincial Territory</label>
                <select class="ol-select" id="ask-prov">
                    <option>New Jasper</option><option>New Madison</option><option>Liveland</option><option>Sentinel</option><option>Columbia</option>
                </select>
            </div>
            <div class="form-group">
                <label class="form-label">Inquiry on Statecraft, Philosophy, or Civic Virtue</label>
                <textarea class="ol-textarea" id="ask-text" rows="4" placeholder="Enter your thoughtful inquiry..."></textarea>
            </div>
            <div class="modal-results-box" id="askResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('askModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitAsk()">Submit to Gazette Clerk</button>
            </div>
        </div>
    </div>

    <!-- Request Hearing Modal -->
    <div class="ol-modal-overlay" id="hearingModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Request Citizen Hearing before Executive Council</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('hearingModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Organization or Citizen Delegation</label>
                <input type="text" class="ol-input" id="h-name" placeholder="Delegation Name">
            </div>
            <div class="form-group">
                <label class="form-label">Hearing Category</label>
                <select class="ol-select" id="h-cat">
                    <option>Provincial Infrastructure</option><option>Environmental Conservation</option><option>Economic Grievance</option><option>Civic Liberties</option>
                </select>
            </div>
            <div class="form-group">
                <label class="form-label">Matter Summary &amp; Proposed Resolution</label>
                <textarea class="ol-textarea" id="h-summary" rows="4" placeholder="Summarize the petition..."></textarea>
            </div>
            <div class="modal-results-box" id="hResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('hearingModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitHearing()">Submit Hearing Docket</button>
            </div>
        </div>
    </div>

    <!-- Dispatch Reader Modal -->
    <div class="ol-modal-overlay" id="dispatchModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title" id="dispTitle">Executive Dispatch</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('dispatchModal')">&times;</button>
            </div>
            <div class="ol-small ol-muted" id="dispMeta" style="margin-bottom:12px;"></div>
            <div id="dispBody" style="font-size:13.5px; line-height:1.6; color:#2a2a2a;"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('dispatchModal')">Close</button>
            </div>
        </div>
    </div>
    """

    scripts = """
    <script>
    const DISPATCHES = {
        1: {
            title: "On the Moral Necessity of Sovereign Solvency",
            meta: "Published October 19, 2026 • Office of the Aeretocrat • Macroeconomics",
            body: `<p>A nation that borrows from predatory international banking cartels sells the birthright of its unborn generations. In Sangaia, our constitutional prohibition on foreign sovereign debt is not merely fiscal prudence—it is our absolute shield of national liberty.</p>
                   <p>When an empire or republic accumulates trillions in compounded foreign interest, its foreign policy is no longer its own. Its social programs are gutted at the demand of international creditors. Its land and ports are seized in structural adjustments.</p>
                   <p>By constitutionally capping our expenditures to legitimate sovereign revenues—principally through ground rent, resource royalties, and luxury surcharges—we guarantee that Sangaia shall forever remain a free and unencumbered people.</p>`
        },
        2: {
            title: "Why the Aeretocracy Replaces Partisan Strife",
            meta: "Published October 12, 2026 • Office of the Aeretocrat • Political Philosophy",
            body: `<p>Party systems do not encourage debate; they encourage tribal warfare funded by oligarchs. In the old systems, politicians spent 90% of their tenure seeking donor funding rather than governing.</p>
                   <p>The Aeretocracy replaces corporate party sponsorship with institutional virtues, open merit-based public exams, and transparent council governance. Officials are answerable directly to the constitution and to the public through annual open audits.</p>`
        },
        3: {
            title: "Harmonizing the Five Sovereign Provinces",
            meta: "Published October 5, 2026 • Office of the Aeretocrat • Federalism",
            body: `<p>From the coastal harbors of Liveland to the highlands of Sentinel, New Jasper, New Madison, and Columbia, our diversity is our endurance. Each province maintains full local autonomy in regional administration, education, and municipal commerce.</p>
                   <p>Our federal duty is simple: guarantee peace, enforce universal human rights and free healthcare, maintain our sovereign monetary stability, and protect the shared natural biomes that sustain our children.</p>`
        }
    };

    function openDispatch(id) {
        const d = DISPATCHES[id];
        if (!d) return;
        document.getElementById('dispTitle').innerText = d.title;
        document.getElementById('dispMeta').innerText = d.meta;
        document.getElementById('dispBody').innerHTML = d.body;
        document.getElementById('dispatchModal').classList.add('active');
    }

    function openAskModal() { document.getElementById('askModal').classList.add('active'); }
    function openHearingModal() { document.getElementById('hearingModal').classList.add('active'); }
    function closeModal(id) { document.getElementById(id).classList.remove('active'); }

    function submitAsk() {
        const res = document.getElementById('askResults');
        const token = 'SG-PET-' + Math.floor(100000 + Math.random() * 900000);
        res.innerHTML = `<strong>Inquiry Logged:</strong> Docket Token: <span style="font-family:monospace;">${token}</span>. Scheduled for review by the Clerk of Civic Petitions.`;
        res.classList.add('active');
    }

    function submitHearing() {
        const res = document.getElementById('hResults');
        const token = 'SG-HRG-' + Math.floor(100000 + Math.random() * 900000);
        res.innerHTML = `<strong>Hearing Request Docketed:</strong> Reference Code: <span style="font-family:monospace;">${token}</span>. Placed on Council Review Registry.`;
        res.classList.add('active');
    }
    </script>
    """

    nav_tabs = MINISTRY_NAV_TABS["executive"]
    sub_nav_tabs = get_subdomain_nav_tabs(nav_tabs)
    generate_page("executive.html", title, theme, "home", hero_title, hero_sub, "Office of the Aeretocrat", "Head of State & Government", "Council Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=nav_tabs)
    generate_page("MoEX/index.html", title, theme, "home", hero_title, hero_sub, "Office of the Aeretocrat", "Head of State & Government", "Council Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)
    generate_page("mEx/index.html", title, theme, "home", hero_title, hero_sub, "Office of the Aeretocrat", "Head of State & Government", "Council Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)

# -----------------------------------------------------------------------------
# 2. MINISTRY OF THE TREASURY (mT)
# -----------------------------------------------------------------------------
def build_treasury():
    title = "Ministry of the Treasury"
    theme = "theme-treasury"
    tab = "treasury"
    hero_title = "ministry of the treasury"
    hero_sub = "Statutory fiscal solvency, sovereign debt management, taxation, infrastructure bonds & audit ledgers"

    sidebar_links = [
        {"label": "Overview & Solvency", "url": "#overview", "active": True},
        {"label": "Zero Sovereign Debt", "url": "#debt", "active": False},
        {"label": "Solidarity Loans", "url": "#loans", "active": False},
        {"label": "Fund Allocations", "url": "#allocations", "active": False},
        {"label": "Fiscal Rectitude & Audits", "url": "#audits", "active": False},
        {"label": "Departments Portal →", "url": "/treasury_departments.html", "active": False}
    ]

    main_content = """

    <!-- Zero Sovereign Debt Tracker -->
    <div class="card" id="overview"><a id="debt"></a>
        <div class="ol-card-title">
            <span>Sovereign Debt Ceiling &amp; Foreign Solvency Ledger</span>
            <span class="ol-badge-tag ol-badge-success">Constitutional Compliance</span>
        </div>
        <div class="ol-grid-3" style="margin-bottom:12px;">
            <div class="ol-metric-box">
                <div class="ol-metric-val">$ 0.00</div>
                <div class="ol-metric-lbl">Foreign Sovereign Debt</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">100.0%</div>
                <div class="ol-metric-lbl">National Fiscal Solvency</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">3.2%</div>
                <div class="ol-metric-lbl">10-Yr Solidarity Bond Yield</div>
            </div>
        </div>
        <p class="ol-small">Under the Sangaian Sovereign Monetary Act, the federal government is constitutionally barred from issuing bonds to foreign banking institutions or incurring compound interest deficits. All municipal and provincial capital loans are funded via internal solidarity bonds backed by public utility revenues.</p>
    </div>

    <!-- Solidarity Infrastructure Loans -->
    <div class="ol-card" id="loans">
        <div class="ol-card-title">
            <span>Provincial Solidarity Loans &amp; Public Works Credit</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openLoanModal()">Simulate Loan Terms</button>
        </div>
        <p class="ol-small ol-muted">Zero-interest and low-fee public development facilities provided directly to provincial cooperatives, green transit authorities, and municipal water boards.</p>
        <table class="ol-table">
            <thead>
                <tr>
                    <th>Facility ID</th>
                    <th>Recipient Agency</th>
                    <th>Capital Amount</th>
                    <th>Term &amp; Amortization</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>SNG-LN-091</td><td>Maritime Coastal Transit District (Liveland)</td><td>$ 14,000,000</td><td>15 Years &bull; Utility Offset</td><td><span class="ol-badge-tag ol-badge-success">Disbursing</span></td></tr>
                <tr><td>SNG-LN-088</td><td>Highland Clean Geothermal Plant (Sentinel)</td><td>$ 28,500,000</td><td>20 Years &bull; Grid Revenue</td><td><span class="ol-badge-tag ol-badge-success">Operational</span></td></tr>
                <tr><td>SNG-LN-084</td><td>Columbia Agro-Irrigation System (Columbia)</td><td>$ 9,200,000</td><td>10 Years &bull; Crop Royalties</td><td><span class="ol-badge-tag ol-badge-success">Amortizing</span></td></tr>
            </tbody>
        </table>
    </div>

    <!-- Ministerial Fund Allocations -->
    <div class="ol-card" id="allocations">
        <div class="ol-card-title">
            <span>Statutory Budgetary Allocations by Sector (FY2026)</span>
            <span class="ol-badge-tag">Total: $ 103.6 B Outlays</span>
        </div>
        <table class="ol-table">
            <thead>
                <tr><th>Ministerial Portfolio</th><th>Statutory Allocation</th><th>Share of Outlay</th><th>Primary Public Purpose</th></tr>
            </thead>
            <tbody>
                <tr><td>Healthcare &amp; Universal Coverage</td><td>$ 28.4 Billion</td><td>27.4%</td><td>Free hospital care, clinics &amp; pharmaceuticals</td></tr>
                <tr><td>Education &amp; Academic Standards</td><td>$ 22.8 Billion</td><td>22.0%</td><td>Tuition-free schools, research &amp; textbooks</td></tr>
                <tr><td>Environment &amp; Biome Stewardship</td><td>$ 16.5 Billion</td><td>15.9%</td><td>Forest reserves, clean energy &amp; wildlife</td></tr>
                <tr><td>Domestic Transit &amp; Roads</td><td>$ 14.2 Billion</td><td>13.7%</td><td>Highways, rail networks &amp; interprovincial bridges</td></tr>
                <tr><td>Work &amp; Labor Standards</td><td>$ 10.8 Billion</td><td>10.4%</td><td>Vocational apprenticeships &amp; job board safety nets</td></tr>
                <tr><td>Executive Administration &amp; Justice</td><td>$ 6.2 Billion</td><td>6.0%</td><td>Cabinet, High Magistrates &amp; public gazette</td></tr>
                <tr><td>Propaganda &amp; Civic Education</td><td>$ 4.7 Billion</td><td>4.5%</td><td>National broadcasting &amp; cultural radio</td></tr>
            </tbody>
        </table>
    </div>

    <!-- Council of Fiscal Rectitude & Surprise Audits -->
    <div class="ol-card" id="audits">
        <div class="ol-card-title">
            <span>Council of Fiscal Rectitude &amp; Surprise Public Audits</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openAuditModal()">File Audit Inquiry</button>
        </div>
        <p class="ol-small">To eliminate bureaucratic graft and kickbacks, the Treasury conducts unannounced quarterly forensic inspections of all procurement contracts above $50,000.</p>
        <div class="ol-grid-2" style="margin-top:10px;">
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong>Latest Public Audit Audit (Q3 FY26):</strong>
                <div class="ol-small" style="margin-top:4px;">Inspected 412 municipal procurement contracts across all 5 provinces. 99.4% full statutory compliance. 2 contracts flagged for vendor price reconciliation.</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong>Civilian Whistleblower Hotline:</strong>
                <div class="ol-small" style="margin-top:4px;">Citizens reporting proven fiscal waste or procurement inflation receive statutory legal immunity and a 5% public savings bonus.</div>
            </div>
        </div>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Treasury Portal</h3>
        <p class="ol-small ol-muted">Access tax calculators, clearance verification, bond purchases, and open procurement listings.</p>
        <div class="ol-mt-10">
            <a href="/treasury_departments.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">Launch Treasury Departments</a>
        </div>
    </div>
    """

    modals = """
    <!-- Loan Simulator Modal -->
    <div class="ol-modal-overlay" id="loanModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Solidarity Public Works Loan Simulator</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('loanModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Borrowing Municipal Agency / Cooperative</label>
                <input type="text" class="ol-input" id="loan-agency" placeholder="e.g., Liveland Port Authority">
            </div>
            <div class="form-group">
                <label class="form-label">Requested Principal ($ Sangaian Dollars)</label>
                <input type="number" class="ol-input" id="loan-amt" value="5000000" step="500000">
            </div>
            <div class="form-group">
                <label class="form-label">Repayment Term</label>
                <select class="ol-select" id="loan-term">
                    <option value="10">10 Years (0.0% Public Works Utility Rate)</option>
                    <option value="15">15 Years (0.5% Administrative Surcharge)</option>
                    <option value="20">20 Years (1.0% Infrastructure Bond Rate)</option>
                </select>
            </div>
            <div class="modal-results-box" id="loanResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('loanModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="calcLoan()">Calculate Amortization</button>
            </div>
        </div>
    </div>

    <!-- Audit Inquiry Modal -->
    <div class="ol-modal-overlay" id="auditModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Submit Forensic Audit Inquiry</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('auditModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Target Department or Procurement Tender</label>
                <input type="text" class="ol-input" id="audit-dept" placeholder="Department name or Contract ID">
            </div>
            <div class="form-group">
                <label class="form-label">Nature of Discrepancy or Waste</label>
                <textarea class="ol-textarea" id="audit-desc" rows="4" placeholder="Detail the observed discrepancy..."></textarea>
            </div>
            <div class="modal-results-box" id="auditResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('auditModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitAudit()">Submit to Inspector General</button>
            </div>
        </div>
    </div>
    """

    scripts = """
    <script>
    function openLoanModal() { document.getElementById('loanModal').classList.add('active'); }
    function openAuditModal() { document.getElementById('auditModal').classList.add('active'); }
    function closeModal(id) { document.getElementById(id).classList.remove('active'); }

    function calcLoan() {
        const amt = parseFloat(document.getElementById('loan-amt').value) || 0;
        const term = parseInt(document.getElementById('loan-term').value) || 10;
        const rate = term === 10 ? 0.0 : (term === 15 ? 0.005 : 0.01);
        const annual = (amt / term) * (1 + rate);
        const res = document.getElementById('loanResults');
        res.innerHTML = `<strong>Simulated Schedule:</strong> Annual Amortization: <strong>$ ${annual.toLocaleString(undefined, {maximumFractionDigits:2})}</strong> / year. Effective Statutory Interest: <strong>${(rate*100).toFixed(1)}%</strong>. Fully asset-backed.`;
        res.classList.add('active');
    }

    function submitAudit() {
        const res = document.getElementById('auditResults');
        const token = 'TREAS-AUD-' + Math.floor(100000 + Math.random() * 900000);
        res.innerHTML = `<strong>Inquiry Docketed:</strong> Tracking Token: <span style="font-family:monospace;">${token}</span>. Assigned to Council of Fiscal Rectitude. Protected under Whistleblower Shield.`;
        res.classList.add('active');
    }
    </script>
    """

    nav_tabs = MINISTRY_NAV_TABS["treasury"]
    sub_nav_tabs = get_subdomain_nav_tabs(nav_tabs)
    generate_page("treasury.html", title, theme, "home", hero_title, hero_sub, "Ministry of the Treasury", "Fiscal & Solvency Authority", "Solvency Verified", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=nav_tabs)
    generate_page("mT/index.html", title, theme, "home", hero_title, hero_sub, "Ministry of the Treasury", "Fiscal & Solvency Authority", "Solvency Verified", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)

# -----------------------------------------------------------------------------
# 3. MINISTRY OF WORK (mW)
# -----------------------------------------------------------------------------
def build_work():
    title = "Ministry of Work"
    theme = "theme-work"
    tab = "work"
    hero_title = "ministry of work"
    hero_sub = "Labor protections, living wage standards, national job placement & worker guilds"

    sidebar_links = [
        {"label": "Overview & Labor Standards", "url": "#overview", "active": True},
        {"label": "Wage Calculator", "url": "#pay-standards", "active": False},
        {"label": "National Job Needs", "url": "#job-needs", "active": False},
        {"label": "Official Job Board", "url": "#job-openings", "active": False},
        {"label": "Work Permits & Visas", "url": "#work-permits", "active": False},
        {"label": "Guilds & Whistleblowers", "url": "#whistleblower", "active": False},
        {"label": "Departments Portal →", "url": "/work_departments.html", "active": False}
    ]

    main_content = """

    <!-- Living Wage Standards & Net Salary Calculator -->
    <div class="card" id="overview"><a id="pay-standards"></a>
        <div class="ol-card-title">
            <span>Statutory Living Wage Standards &amp; Interactive Net Pay Calculator</span>
            <span class="ol-badge-tag ol-badge-success">Statutory Floor: $25.00 / hr</span>
        </div>
        <p class="ol-small">In Sangaia, the minimum wage is tied directly to the cost of local housing and nutrition. Under the Fair Compensation Act, the federal statutory wage floor is <strong>$ 25.00 / hr</strong> ($ 52,000 / year base).</p>

        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:14px; margin-top:10px;">
            <div style="display:flex; flex-wrap:wrap; align-items:center; gap:14px;">
                <div style="flex:1 1 200px;">
                    <label class="form-label">Gross Annual Salary ($):</label>
                    <input type="number" class="ol-input" id="calcGross" value="65000" step="1000" oninput="calcNetWage()">
                </div>
                <div style="flex:1 1 200px;">
                    <label class="form-label">Provincial Residence:</label>
                    <select class="ol-select" id="calcProv" onchange="calcNetWage()">
                        <option value="NJ">New Jasper (0% Provincial Income Tax)</option>
                        <option value="NM">New Madison (0% Provincial Income Tax)</option>
                        <option value="LV">Liveland (0% Provincial Income Tax)</option>
                        <option value="ST">Sentinel (0% Provincial Income Tax)</option>
                        <option value="CO">Columbia (0% Provincial Income Tax)</option>
                    </select>
                </div>
            </div>
            <div style="display:flex; justify-content:space-between; align-items:center; margin-top:14px; padding-top:10px; border-top:1px dashed #cbd5e1;">
                <div>
                    <div class="ol-small ol-muted">Estimated Take-Home (Net of Universal Healthcare &amp; Solidarity Fund):</div>
                    <div style="font-size:22px; font-weight:700; color:#166534;" id="calcNetVal">$ 53,300.00 / year</div>
                </div>
                <div class="ol-badge-tag ol-badge-success">Healthcare &amp; Pension 100% Covered</div>
            </div>
        </div>
    </div>

    <!-- National Job Openings Board -->
    <div class="ol-card" id="job-openings">
        <div class="ol-card-title">
            <span>Official National Job Placement Board</span>
            <span class="ol-badge-tag">Verified Public &amp; Cooperative Tenders</span>
        </div>
        <div style="display:flex; flex-wrap:wrap; gap:10px; margin-bottom:12px;">
            <input type="text" class="ol-input" id="jobSearch" placeholder="Filter by job title, guild, or skill..." style="flex:1 1 220px;" oninput="filterJobList()">
            <select class="ol-select" id="sectorFilter" style="flex:0 0 160px;" onchange="filterJobList()">
                <option value="all">All Sectors</option>
                <option value="healthcare">Healthcare</option>
                <option value="engineering">Engineering</option>
                <option value="education">Education</option>
                <option value="agriculture">Agriculture</option>
            </select>
            <select class="ol-select" id="provFilter" style="flex:0 0 140px;" onchange="filterJobList()">
                <option value="all">All 5 Provinces</option>
                <option value="New Jasper">New Jasper</option>
                <option value="New Madison">New Madison</option>
                <option value="Liveland">Liveland</option>
                <option value="Sentinel">Sentinel</option>
                <option value="Columbia">Columbia</option>
            </select>
        </div>

        <div id="jobListContainer">
            <div class="ol-card job-item" data-sector="healthcare" data-prov="New Jasper" style="margin-bottom:8px; background:#fbfcfd;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <div>
                        <strong style="font-size:14px;">Senior Trauma Registered Nurse &bull; Emergency Response</strong>
                        <div class="ol-small ol-muted">New Jasper Central Hospital &bull; New Jasper &bull; $ 84,000 / yr</div>
                    </div>
                    <button type="button" class="ol-btn ol-btn-sm" onclick="applyJob('Senior Trauma Nurse', 'New Jasper Central Hospital')">Apply Now</button>
                </div>
            </div>

            <div class="ol-card job-item" data-sector="engineering" data-prov="Sentinel" style="margin-bottom:8px; background:#fbfcfd;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <div>
                        <strong style="font-size:14px;">Geothermal Subsurface Mechanical Engineer</strong>
                        <div class="ol-small ol-muted">Highland Clean Energy Authority &bull; Sentinel &bull; $ 96,000 / yr</div>
                    </div>
                    <button type="button" class="ol-btn ol-btn-sm" onclick="applyJob('Geothermal Engineer', 'Highland Clean Energy')">Apply Now</button>
                </div>
            </div>

            <div class="ol-card job-item" data-sector="agriculture" data-prov="New Madison" style="margin-bottom:8px; background:#fbfcfd;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <div>
                        <strong style="font-size:14px;">Hydroponic Cooperative Agronomist &amp; Crop Lead</strong>
                        <div class="ol-small ol-muted">Madison Valley Food Cooperative &bull; New Madison &bull; $ 72,000 / yr</div>
                    </div>
                    <button type="button" class="ol-btn ol-btn-sm" onclick="applyJob('Hydroponic Agronomist', 'Madison Valley Food Co-op')">Apply Now</button>
                </div>
            </div>

            <div class="ol-card job-item" data-sector="education" data-prov="Columbia" style="margin-bottom:8px; background:#fbfcfd;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                    <div>
                        <strong style="font-size:14px;">Secondary STEM &amp; Digital Ethics Instructor</strong>
                        <div class="ol-small ol-muted">Columbia City Unified School District &bull; Columbia &bull; $ 68,000 / yr</div>
                    </div>
                    <button type="button" class="ol-btn ol-btn-sm" onclick="applyJob('STEM Instructor', 'Columbia Unified Schools')">Apply Now</button>
                </div>
            </div>
        </div>
    </div>

    <!-- Work Permits & Visa Eligibility -->
    <div class="ol-card" id="work-permits">
        <div class="ol-card-title">
            <span>Work Permit &amp; Cross-Border Credential Transfer</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openPermitModal()">Submit Work Permit Request</button>
        </div>
        <p class="ol-small">Foreign skilled professionals seeking employment in Sangaia may submit their academic and apprenticeship credentials for expedited credential reciprocity under the Sovereign Labor Standards Act.</p>
        <div class="ol-grid-3" style="margin-top:10px;">
            <div class="ol-metric-box">
                <div class="ol-metric-val">3 Tiers</div>
                <div class="ol-metric-lbl">Visa Classes (A, B, C)</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">10 Days</div>
                <div class="ol-metric-lbl">Statutory Evaluation Window</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">100%</div>
                <div class="ol-metric-lbl">Equal Labor Wage Protections</div>
            </div>
        </div>
    </div>

    <!-- Guilds & Whistleblowers -->
    <div class="ol-card" id="whistleblower">
        <div class="ol-card-title">
            <span>Worker Guild Registry &amp; Anonymous Whistleblower Portal</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openWhistleblowerModal()">File Confidential Report</button>
        </div>
        <p class="ol-small">Every registered enterprise operating in Sangaia with 10 or more employees must recognize democratic worker guild councils. Retaliation against whistleblowers carries immediate commercial license suspension.</p>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Work &amp; Labor Portal</h3>
        <p class="ol-small ol-muted">Access whistleblower tools, union registry, job placement, and international work credential evaluations.</p>
        <div class="ol-mt-10">
            <a href="/work_departments.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">Launch Work Departments</a>
        </div>
    </div>
    """

    modals = """
    <!-- Job Apply Modal -->
    <div class="ol-modal-overlay" id="jobApplyModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title" id="jobApplyTitle">Job Application</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('jobApplyModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Full Legal Name</label>
                <input type="text" class="ol-input" id="ja-name" placeholder="Citizen Legal Name">
            </div>
            <div class="form-group">
                <label class="form-label">Sangaia ID / Foreign Passport ID</label>
                <input type="text" class="ol-input" id="ja-id" placeholder="SG-XXXX or Passport Number">
            </div>
            <div class="form-group">
                <label class="form-label">Summary of Experience &amp; Certifications</label>
                <textarea class="ol-textarea" id="ja-exp" rows="3" placeholder="Brief qualifications..."></textarea>
            </div>
            <div class="modal-results-box" id="jaResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('jobApplyModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitJobApply()">Submit Application</button>
            </div>
        </div>
    </div>

    <!-- Permit Modal -->
    <div class="ol-modal-overlay" id="permitModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Foreign Work Permit Eligibility Submission</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('permitModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Applicant Name &amp; Nationality</label>
                <input type="text" class="ol-input" id="p-name" placeholder="Full name and current citizenship">
            </div>
            <div class="form-group">
                <label class="form-label">Profession / Specialty Field</label>
                <input type="text" class="ol-input" id="p-prof" placeholder="e.g., Mechanical Engineer, Nurse, Agronomist">
            </div>
            <div class="form-group">
                <label class="form-label">Target Province of Employment</label>
                <select class="ol-select" id="p-prov">
                    <option>New Jasper</option><option>New Madison</option><option>Liveland</option><option>Sentinel</option><option>Columbia</option>
                </select>
            </div>
            <div class="modal-results-box" id="pResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('permitModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitPermit()">Submit Credential File</button>
            </div>
        </div>
    </div>

    <!-- Whistleblower Modal -->
    <div class="ol-modal-overlay" id="whistleModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Anonymous Whistleblower Labor Protection Docket</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('whistleModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Employer / Enterprise Name</label>
                <input type="text" class="ol-input" id="w-emp" placeholder="Company or Facility name">
            </div>
            <div class="form-group">
                <label class="form-label">Labor Violation Category</label>
                <select class="ol-select" id="w-cat">
                    <option>Underpayment of Statutory Living Wage</option>
                    <option>Workplace Safety Negligence</option>
                    <option>Union / Guild Suppression</option>
                    <option>Unfair Retaliation</option>
                </select>
            </div>
            <div class="form-group">
                <label class="form-label">Confidential Violation Summary</label>
                <textarea class="ol-textarea" id="w-desc" rows="4" placeholder="Detail the violation..."></textarea>
            </div>
            <div class="modal-results-box" id="wResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('whistleModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitWhistle()">Submit Protected Docket</button>
            </div>
        </div>
    </div>
    """

    scripts = """
    <script>
    function calcNetWage() {
        const gross = parseFloat(document.getElementById('calcGross').value) || 0;
        const taxRate = gross > 100000 ? 0.22 : (gross > 60000 ? 0.18 : 0.12);
        const net = gross * (1 - taxRate);
        document.getElementById('calcNetVal').innerText = '$ ' + net.toLocaleString(undefined, {minimumFractionDigits:2, maximumFractionDigits:2}) + ' / year';
    }

    function filterJobList() {
        const q = (document.getElementById('jobSearch').value || '').toLowerCase();
        const sec = document.getElementById('sectorFilter').value;
        const prov = document.getElementById('provFilter').value;

        document.querySelectorAll('.job-item').forEach(el => {
            const elSec = el.getAttribute('data-sector');
            const elProv = el.getAttribute('data-prov');
            const elText = el.innerText.toLowerCase();

            const matchQ = !q || elText.includes(q);
            const matchSec = sec === 'all' || elSec === sec;
            const matchProv = prov === 'all' || elProv === prov;

            el.style.display = (matchQ && matchSec && matchProv) ? 'block' : 'none';
        });
    }

    function applyJob(title, emp) {
        document.getElementById('jobApplyTitle').innerText = 'Apply: ' + title;
        document.getElementById('jobApplyModal').classList.add('active');
    }

    function openPermitModal() { document.getElementById('permitModal').classList.add('active'); }
    function openWhistleblowerModal() { document.getElementById('whistleModal').classList.add('active'); }
    function closeModal(id) { document.getElementById(id).classList.remove('active'); }

    function submitJobApply() {
        const res = document.getElementById('jaResults');
        const token = 'JOB-APP-' + Math.floor(100000 + Math.random() * 900000);
        res.innerHTML = `<strong>Application Recorded:</strong> Tracking Code: <span style="font-family:monospace;">${token}</span>. Sent to Hiring Guild.`;
        res.classList.add('active');
    }

    function submitPermit() {
        const res = document.getElementById('pResults');
        const token = 'VISA-CRED-' + Math.floor(100000 + Math.random() * 900000);
        res.innerHTML = `<strong>Permit Request Registered:</strong> Reference Code: <span style="font-family:monospace;">${token}</span>. 10-day evaluation active.`;
        res.classList.add('active');
    }

    function submitWhistle() {
        const res = document.getElementById('wResults');
        const token = 'WHISTLE-' + Math.floor(100000 + Math.random() * 900000);
        res.innerHTML = `<strong>Whistleblower Docket Secured:</strong> Cryptographic Hash: <span style="font-family:monospace;">${token}</span>. Assigned to Labor Ombudsman.`;
        res.classList.add('active');
    }
    </script>
    """

    nav_tabs = MINISTRY_NAV_TABS["work"]
    sub_nav_tabs = get_subdomain_nav_tabs(nav_tabs)
    generate_page("work.html", title, theme, "home", hero_title, hero_sub, "Ministry of Work", "Labor Standards Authority", "Standards Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=nav_tabs)
    generate_page("mW/index.html", title, theme, "home", hero_title, hero_sub, "Ministry of Work", "Labor Standards Authority", "Standards Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)

# -----------------------------------------------------------------------------
# 4. MINISTRY OF HEALTHCARE (mH)
# -----------------------------------------------------------------------------
def build_healthcare():
    title = "Ministry of Healthcare"
    theme = "theme-healthcare"
    tab = "healthcare"
    hero_title = "ministry of healthcare"
    hero_sub = "Universal state-sponsored health coverage, hospital emergency room triage & public disease control"

    sidebar_links = [
        {"label": "Overview & Universal Care", "url": "#overview", "active": True},
        {"label": "Universal Coverage Screening", "url": "#coverage", "active": False},
        {"label": "Hospital ER Capacity", "url": "#hospitals", "active": False},
        {"label": "Disease Control Telemetry", "url": "#cdc", "active": False},
        {"label": "Ambulance Dispatch", "url": "#ambulance", "active": False},
        {"label": "Departments Portal →", "url": "/healthcare_departments.html", "active": False}
    ]

    main_content = """

    <!-- Universal Coverage Screening -->
    <div class="card" id="overview"><a id="coverage"></a>
        <div class="ol-card-title">
            <span>Universal Healthcare Coverage &amp; Digital Insurance Verification</span>
            <span class="ol-badge-tag ol-badge-success">Zero Out-of-Pocket Fees</span>
        </div>
        <p class="ol-small">Every registered Sangaia ID holder is automatically enrolled into Tier 1 Universal Comprehensive Care, covering hospitalization, dental surgery, psychological therapy, and prescription drugs.</p>
        <div class="ol-grid-3" style="margin-top:10px;">
            <div class="ol-metric-box">
                <div class="ol-metric-val">$ 0.00</div>
                <div class="ol-metric-lbl">Copay at Point of Care</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">100%</div>
                <div class="ol-metric-lbl">Subsidized Generic Rx</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">5 Provinces</div>
                <div class="ol-metric-lbl">Unified Digital Charting</div>
            </div>
        </div>
    </div>

    <!-- Live Hospital ER Capacity Metrics Across the 5 Provinces -->
    <div class="ol-card" id="hospitals">
        <div class="ol-card-title">
            <span>Live Hospital Emergency Room Capacity Across the 5 Provinces</span>
            <span class="ol-badge-tag ol-badge-success">Live Triage Network</span>
        </div>
        <p class="ol-small ol-muted">Real-time telemetry of regional trauma centers across all 5 Sovereign Provinces.</p>
        <table class="ol-table">
            <thead>
                <tr>
                    <th>Provincial Medical Center</th>
                    <th>Territory</th>
                    <th>ICU Beds Free</th>
                    <th>Avg Triage Wait</th>
                    <th>Trauma Status</th>
                </tr>
            </thead>
            <tbody>
                <tr><td>Shesk Sovereign University Hospital</td><td>New Jasper</td><td>24 / 80 Free</td><td>12 min</td><td><span class="ol-badge-tag ol-badge-success">Operational</span></td></tr>
                <tr><td>Madison Valley Regional Trauma Center</td><td>New Madison</td><td>18 / 60 Free</td><td>15 min</td><td><span class="ol-badge-tag ol-badge-success">Operational</span></td></tr>
                <tr><td>Oaks Coastal Marine Hospital</td><td>Liveland</td><td>32 / 70 Free</td><td>8 min</td><td><span class="ol-badge-tag ol-badge-success">Operational</span></td></tr>
                <tr><td>Sentinel Ridge Highland Clinic</td><td>Sentinel</td><td>14 / 40 Free</td><td>10 min</td><td><span class="ol-badge-tag ol-badge-success">Operational</span></td></tr>
                <tr><td>Columbia City Metropolitan Health Hub</td><td>Columbia</td><td>28 / 65 Free</td><td>14 min</td><td><span class="ol-badge-tag ol-badge-success">Operational</span></td></tr>
            </tbody>
        </table>
    </div>

    <!-- Disease Control & CDC Research -->
    <div class="ol-card" id="cdc">
        <div class="ol-card-title">
            <span>National Disease Control Telemetry &amp; Public Hygiene</span>
            <span class="ol-badge-tag ol-badge-success">Epidemic Index: LOW</span>
        </div>
        <div class="ol-grid-2" style="margin-top:10px;">
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong>Water Quality &amp; Pathogen Screening:</strong>
                <div class="ol-small" style="margin-top:4px;">Municipal water testing conducted daily across all 5 provincial aquifers: 100% compliant with zero toxic chemical runoff.</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong>Respiratory &amp; Viral Surveillance:</strong>
                <div class="ol-small" style="margin-top:4px;">Automated clinical monitoring shows seasonal influenza transmission at baseline levels. Emergency vaccination supply at 140% statutory threshold.</div>
            </div>
        </div>
    </div>

    <!-- Paramedic & Emergency Ambulance Network -->
    <div class="ol-card" id="ambulance">
        <div class="ol-card-title">
            <span>Paramedic Network &amp; Non-Emergency Medical Transport</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openAmbulanceModal()">Book Medical Transport</button>
        </div>
        <p class="ol-small">In life-threatening emergencies, dial <strong>9-1-1</strong>. For scheduled clinical transfers, dialysis transit, and mobility assistance, citizens may book state-funded transports.</p>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Healthcare Services</h3>
        <p class="ol-small ol-muted">Check prescription benefit claims, digital card enrollment, hospital licensing, and non-emergency transports.</p>
        <div class="ol-mt-10">
            <a href="/healthcare_departments.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">Launch Healthcare Departments</a>
        </div>
    </div>
    """

    modals = """
    <!-- Ambulance Booking Modal -->
    <div class="ol-modal-overlay" id="ambModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Book Non-Emergency Medical Transport</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('ambModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Patient Legal Name</label>
                <input type="text" class="ol-input" id="amb-name" placeholder="Patient Name">
            </div>
            <div class="form-group">
                <label class="form-label">Sangaia ID Number</label>
                <input type="text" class="ol-input" id="amb-id" placeholder="SG-XXXX-XXXX">
            </div>
            <div class="form-group">
                <label class="form-label">Pick-up Province &amp; Address</label>
                <input type="text" class="ol-input" id="amb-addr" placeholder="Address">
            </div>
            <div class="form-group">
                <label class="form-label">Destination Medical Center</label>
                <select class="ol-select" id="amb-dest">
                    <option>Shesk Sovereign University Hospital</option>
                    <option>Madison Valley Trauma Center</option>
                    <option>Oaks Coastal Marine Hospital</option>
                    <option>Sentinel Ridge Highland Clinic</option>
                    <option>Columbia City Health Hub</option>
                </select>
            </div>
            <div class="modal-results-box" id="ambResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('ambModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitAmb()">Confirm Dispatch</button>
            </div>
        </div>
    </div>
    """

    scripts = """
    <script>
    function openAmbulanceModal() { document.getElementById('ambModal').classList.add('active'); }
    function closeModal(id) { document.getElementById(id).classList.remove('active'); }

    function submitAmb() {
        const res = document.getElementById('ambResults');
        const token = 'MED-DISP-' + Math.floor(100000 + Math.random() * 900000);
        res.innerHTML = `<strong>Transport Dispatch Confirmed:</strong> Confirmation Code: <span style="font-family:monospace;">${token}</span>. Fully subsidized under Universal Healthcare.`;
        res.classList.add('active');
    }
    </script>
    """

    nav_tabs = MINISTRY_NAV_TABS["healthcare"]
    sub_nav_tabs = get_subdomain_nav_tabs(nav_tabs)
    generate_page("healthcare.html", title, theme, "home", hero_title, hero_sub, "Ministry of Healthcare", "Universal Health Authority", "Clinics Operational", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=nav_tabs)
    generate_page("mH/index.html", title, theme, "home", hero_title, hero_sub, "Ministry of Healthcare", "Universal Health Authority", "Clinics Operational", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)
    # Generate all rich pre-redesign healthcare pages
    build_all_healthcare_secondary()

# -----------------------------------------------------------------------------
# 5. MINISTRY OF EDUCATION (mE)
# -----------------------------------------------------------------------------
def build_education():
    title = "Ministry of Education"
    theme = "theme-education"
    tab = "education"
    hero_title = "ministry of education"
    hero_sub = "Universal public instruction, open digital textbook repositories, teacher certifications & higher ed grants"

    sidebar_links = [
        {"label": "Overview & Curricula", "url": "#overview", "active": True},
        {"label": "Open Textbooks", "url": "#textbooks", "active": False},
        {"label": "Higher Ed & Universities", "url": "#higher-ed", "active": False},
        {"label": "School Scorecards", "url": "#schools", "active": False},
        {"label": "Teacher Certifications", "url": "#teachers", "active": False},
        {"label": "Departments Portal →", "url": "/education_departments.html", "active": False}
    ]

    main_content = """

    <!-- Open Digital Textbooks -->
    <div class="card" id="overview"><a id="textbooks"></a>
        <div class="ol-card-title">
            <span>Open National Textbook &amp; Curriculum Repository</span>
            <span class="ol-badge-tag ol-badge-success">100% Free Public Access</span>
        </div>
        <p class="ol-small">All approved instructional frameworks, primary textbooks, and laboratory guides are freely available to students, parents, and self-directed learners nationwide.</p>
        <table class="ol-table">
            <thead>
                <tr><th>Discipline</th><th>Level</th><th>Approved Syllabus</th><th>Digital Access</th></tr>
            </thead>
            <tbody>
                <tr><td>Sovereign Mathematics &amp; Monomer Standards</td><td>Primary (Grades 1-6)</td><td>Base-10 Monomer Scaling &amp; Applied Geometry</td><td><a href="javascript:void(0)" class="ol-btn ol-btn-sm">Download PDF (Free)</a></td></tr>
                <tr><td>Civic Statecraft &amp; Constitutional Virtues</td><td>Secondary (Grades 7-12)</td><td>The Aeretocracy &amp; Separation of Powers</td><td><a href="javascript:void(0)" class="ol-btn ol-btn-sm">Download PDF (Free)</a></td></tr>
                <tr><td>Ecological Sciences &amp; Biome Stewardship</td><td>Secondary &amp; Tertiary</td><td>Native Biome Conservation &amp; Climate Telemetry</td><td><a href="javascript:void(0)" class="ol-btn ol-btn-sm">Download PDF (Free)</a></td></tr>
            </tbody>
        </table>
    </div>

    <!-- Higher Education Grants & Universities -->
    <div class="ol-card" id="higher-ed">
        <div class="ol-card-title">
            <span>Provincial University Accreditation &amp; Research Grants</span>
            <span class="ol-badge-tag">Zero Student Debt</span>
        </div>
        <p class="ol-small">Sangaia's five sovereign provincial universities offer tuition-free bachelor, master, and doctoral programs to all qualified citizens.</p>
        <div class="ol-grid-2" style="margin-top:10px;">
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong>Shesk Sovereign University (New Jasper):</strong>
                <div class="ol-small" style="margin-top:4px;">Leading institution for Advanced Computational Science, Public Constitutional Law, and Monetary Theory.</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong>Madison Agricultural &amp; Engineering Institute (New Madison):</strong>
                <div class="ol-small" style="margin-top:4px;">Pioneering regenerative agriculture, hydroponic food systems, and environmental civil engineering.</div>
            </div>
        </div>
    </div>

    <!-- Provincial Public School Scorecards -->
    <div class="ol-card" id="schools">
        <div class="ol-card-title">
            <span>Provincial Public School Scorecards (FY2026)</span>
            <span class="ol-badge-tag ol-badge-success">100% Funded</span>
        </div>
        <table class="ol-table">
            <thead>
                <tr><th>Provincial District</th><th>Schools</th><th>Student-Teacher Ratio</th><th>Nutritional Program</th><th>Composite Score</th></tr>
            </thead>
            <tbody>
                <tr><td>New Jasper Unified</td><td>142 Schools</td><td>1:14</td><td>100% Free Organic Meals</td><td>94.6%</td></tr>
                <tr><td>New Madison Regional</td><td>118 Schools</td><td>1:15</td><td>100% Free Organic Meals</td><td>93.8%</td></tr>
                <tr><td>Liveland Coastal</td><td>98 Schools</td><td>1:13</td><td>100% Free Organic Meals</td><td>95.2%</td></tr>
                <tr><td>Sentinel Mountain District</td><td>64 Schools</td><td>1:12</td><td>100% Free Organic Meals</td><td>92.9%</td></tr>
                <tr><td>Columbia Metropolitan</td><td>86 Schools</td><td>1:14</td><td>100% Free Organic Meals</td><td>94.1%</td></tr>
            </tbody>
        </table>
    </div>

    <!-- Teacher Certifications -->
    <div class="ol-card" id="teachers">
        <div class="ol-card-title">
            <span>Teacher Certification &amp; Professional Educator Registry</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openCertModal()">Verify Teacher License</button>
        </div>
        <p class="ol-small">Educators in Sangaia are compensated with senior civil service status and sabbatical privileges, reflecting their vital societal role.</p>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Education Portal</h3>
        <p class="ol-small ol-muted">Explore curriculum development, higher education subsidies, teacher certifications, and institutional funding.</p>
        <div class="ol-mt-10">
            <a href="/education_departments.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">Launch Education Departments</a>
        </div>
    </div>
    """

    modals = """
    <!-- Teacher Cert Modal -->
    <div class="ol-modal-overlay" id="certModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Verify Educator Certification</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('certModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Educator Full Name or License ID</label>
                <input type="text" class="ol-input" id="tc-name" placeholder="e.g., Elena Vance or SG-EDU-8491">
            </div>
            <div class="modal-results-box" id="certResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('certModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="verifyCert()">Search Registry</button>
            </div>
        </div>
    </div>
    """

    scripts = """
    <script>
    function openCertModal() { document.getElementById('certModal').classList.add('active'); }
    function closeModal(id) { document.getElementById(id).classList.remove('active'); }

    function verifyCert() {
        const res = document.getElementById('certResults');
        res.innerHTML = `<strong>Registry Result:</strong> Verified Active Educator &bull; Master License in Good Standing &bull; Certified by Academic Board of Sangaia.`;
        res.classList.add('active');
    }
    </script>
    """

    nav_tabs = MINISTRY_NAV_TABS["education"]
    sub_nav_tabs = get_subdomain_nav_tabs(nav_tabs)
    generate_page("education.html", title, theme, "home", hero_title, hero_sub, "Ministry of Education", "Academic & Standards Authority", "Curricula Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=nav_tabs)
    generate_page("mE/index.html", title, theme, "home", hero_title, hero_sub, "Ministry of Education", "Academic & Standards Authority", "Curricula Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)
    generate_page("mEd/index.html", title, theme, "home", hero_title, hero_sub, "Ministry of Education", "Academic & Standards Authority", "Curricula Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)

# -----------------------------------------------------------------------------
# 6. MINISTRY OF DOMESTIC AFFAIRS (MiA)
# -----------------------------------------------------------------------------
def build_domestic():
    title = "Ministry of Domestic Affairs"
    theme = "theme-domestic"
    tab = "domestic"
    hero_title = "ministry of domestic affairs"
    hero_sub = "Provincial relations, interstate trade, federal-provincial coordination, road & highway services"

    sidebar_links = [
        {"label": "Overview & Provincial Pacts", "url": "#overview", "active": True},
        {"label": "5 Sovereign Provinces", "url": "#provinces", "active": False},
        {"label": "Interstate Trade Registry", "url": "#trade", "active": False},
        {"label": "Federal Interactions Gateway", "url": "#federal", "active": False},
        {"label": "Roads & Traffic Services", "url": "#transit", "active": False},
        {"label": "Departments Portal →", "url": "/domesticaffairs_departments.html", "active": False}
    ]

    main_content = """

    <!-- The 5 Sovereign Provinces -->
    <div class="card" id="overview"><a id="provinces"></a>
        <div class="ol-card-title">
            <span>The Five Sovereign Provinces of Sangaia</span>
            <span class="ol-badge-tag ol-badge-success">Interstate Harmony Pact Active</span>
        </div>
        <p class="ol-small">Each province exercises constitutional autonomy under republican principles while coordinating through the Federal Council of Governors.</p>
        <table class="ol-table">
            <thead>
                <tr><th>Province</th><th>Capital</th><th>Population</th><th>Major Economic Role</th><th>Provincial Governor</th></tr>
            </thead>
            <tbody>
                <tr><td>New Jasper</td><td>Shesk</td><td>2,410,000</td><td>National Governance &amp; High Technology</td><td>Gov. Alistair Sterling</td></tr>
                <tr><td>New Madison</td><td>Madison City</td><td>1,980,000</td><td>Agricultural Breadbasket &amp; Green Energy</td><td>Gov. Miriam Thorne</td></tr>
                <tr><td>Liveland</td><td>Oaks</td><td>1,650,000</td><td>Maritime Logistics &amp; Fisheries</td><td>Gov. Jonas Vance</td></tr>
                <tr><td>Sentinel</td><td>Sentinel Ridge</td><td>890,000</td><td>Geothermal Power &amp; Mineral Stewardship</td><td>Gov. Clara Lindqvist</td></tr>
                <tr><td>Columbia</td><td>Columbia City</td><td>940,000</td><td>Aerospace, Cultural Arts &amp; Education</td><td>Gov. Derek Morales</td></tr>
            </tbody>
        </table>
    </div>

    <!-- Interprovincial Trade & Resource Flows -->
    <div class="ol-card" id="trade">
        <div class="ol-card-title">
            <span>Interprovincial Trade &amp; Resource Distribution</span>
            <span class="ol-badge-tag">Tariff-Free Internal Market</span>
        </div>
        <p class="ol-small">Under the Interstate Commerce Covenant, all commerce moving between the five provinces is 100% exempt from internal tariffs, inspections, and discriminatory restrictions.</p>
        <div class="ol-grid-3" style="margin-top:10px;">
            <div class="ol-metric-box">
                <div class="ol-metric-val">$ 18.2 B</div>
                <div class="ol-metric-lbl">Monthly Internal Trade</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">100%</div>
                <div class="ol-metric-lbl">Clean Freight Electrification</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">0.0%</div>
                <div class="ol-metric-lbl">Internal Tariff Rate</div>
            </div>
        </div>
    </div>

    <!-- Roadways & Traffic Telemetry -->
    <div class="ol-card" id="transit">
        <div class="ol-card-title">
            <span>National Highway &amp; Roadway Status Dashboard</span>
            <span class="ol-badge-tag ol-badge-success">Measured in Monomers &amp; Kilomers (Кмн)</span>
        </div>
        <p class="ol-small ol-muted">Live highway maintenance and traffic status across the federal transit arterial network.</p>
        <table class="ol-table">
            <thead>
                <tr><th>Interstate Highway</th><th>Route Corridors</th><th>Length in Kilomers (Кмн)</th><th>Transit Condition</th></tr>
            </thead>
            <tbody>
                <tr><td>Route 1 (Coastal Highway)</td><td>Shesk (NJ) &rarr; Oaks (LV)</td><td>320 Кмн (19,200,000 Мн)</td><td><span class="ol-badge-tag ol-badge-success">Clear &bull; Optimal</span></td></tr>
                <tr><td>Route 4 (Trans-Sangaia Arterial)</td><td>Madison City (NM) &rarr; Shesk (NJ)</td><td>245 Кмн (14,700,000 Мн)</td><td><span class="ol-badge-tag ol-badge-success">Clear &bull; Optimal</span></td></tr>
                <tr><td>Route 8 (Highland Ridge Pass)</td><td>Sentinel Ridge (ST) &rarr; Columbia (CO)</td><td>180 Кмн (10,800,000 Мн)</td><td><span class="ol-badge-tag ol-badge-warning">Maintenance Crew Active</span></td></tr>
            </tbody>
        </table>
    </div>

    <!-- Federal Interactions Gateway -->
    <div class="ol-card" id="federal">
        <div class="ol-card-title">
            <span>Federal-Provincial Administrative Gateway</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openPactModal()">Submit Intergovernmental Petition</button>
        </div>
        <p class="ol-small">Municipalities and provincial assemblies coordinate directly with the Ministry for federal grants, disaster mitigation, and interprovincial infrastructure harmonization.</p>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Domestic Affairs</h3>
        <p class="ol-small ol-muted">Coordinates provincial relations, interprovincial commerce, DMV licensing, and federal road networks.</p>
        <div class="ol-mt-10">
            <a href="/domesticaffairs_departments.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">Launch Domestic Departments</a>
        </div>
    </div>
    """

    modals = """
    <!-- Intergovernmental Petition Modal -->
    <div class="ol-modal-overlay" id="pactModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Submit Intergovernmental Administrative Petition</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('pactModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Sponsoring Municipality or Province</label>
                <select class="ol-select" id="pact-prov">
                    <option>New Jasper</option><option>New Madison</option><option>Liveland</option><option>Sentinel</option><option>Columbia</option>
                </select>
            </div>
            <div class="form-group">
                <label class="form-label">Coordination Topic</label>
                <select class="ol-select" id="pact-topic">
                    <option>Interprovincial Transit Coordination</option>
                    <option>Watershed &amp; Environmental Stewardship</option>
                    <option>Emergency Mutual Aid Accord</option>
                    <option>Municipal Resource Grant</option>
                </select>
            </div>
            <div class="form-group">
                <label class="form-label">Petition Narrative</label>
                <textarea class="ol-textarea" id="pact-desc" rows="4" placeholder="Detail the petition..."></textarea>
            </div>
            <div class="modal-results-box" id="pactResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('pactModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitPact()">Submit to Council of Governors</button>
            </div>
        </div>
    </div>
    """

    scripts = """
    <script>
    function openPactModal() { document.getElementById('pactModal').classList.add('active'); }
    function closeModal(id) { document.getElementById(id).classList.remove('active'); }

    function submitPact() {
        const res = document.getElementById('pactResults');
        const token = 'DOM-PACT-' + Math.floor(100000 + Math.random() * 900000);
        res.innerHTML = `<strong>Petition Docketed:</strong> Tracking Token: <span style="font-family:monospace;">${token}</span>. Placed on Federal Council agenda.`;
        res.classList.add('active');
    }
    </script>
    """

    nav_tabs = MINISTRY_NAV_TABS["domesticaffairs"]
    sub_nav_tabs = get_subdomain_nav_tabs(nav_tabs)
    generate_page("domesticaffairs.html", title, theme, "home", hero_title, hero_sub, "Ministry of Domestic Affairs", "Internal Governance Authority", "Pacts Verified", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=nav_tabs)
    generate_page("MiA/index.html", title, theme, "home", hero_title, hero_sub, "Ministry of Domestic Affairs", "Internal Governance Authority", "Pacts Verified", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)

# -----------------------------------------------------------------------------
# 7. MINISTRY OF EXTERNAL AFFAIRS (MdA)
# -----------------------------------------------------------------------------
def build_external():
    title = "Ministry of External Affairs"
    theme = "theme-external"
    tab = "external"
    hero_title = "ministry of external affairs"
    hero_sub = "Global travel advisories for all nations, sovereign treaties, embassies & diplomatic protocol"

    sidebar_links = [
        {"label": "Overview & Neutrality", "url": "#overview", "active": True},
        {"label": "Worldwide Travel Advisories", "url": "#travel", "active": False},
        {"label": "Sovereign Treaties & Accords", "url": "#treaties", "active": False},
        {"label": "Embassies & Consulates", "url": "#embassies", "active": False},
        {"label": "Diplomatic Protocol", "url": "#protocol", "active": False},
        {"label": "Departments Portal →", "url": "/externalaffairs_departments.html", "active": False}
    ]

    main_content = """

    <!-- Travel Advisories for Every Worldwide Nation -->
    <div class="card" id="overview"><a id="travel"></a>
        <div class="ol-card-title">
            <span>Global Travel Advisories &bull; Worldwide Nation Directory</span>
            <span class="ol-badge-tag ol-badge-success">Consular Telemetry Live</span>
        </div>
        <p class="ol-small">Official risk assessments and travel guidance issued by the Sangaian Consular Service for all recognized nations worldwide.</p>
        <div style="margin-bottom:12px;">
            <input type="text" class="ol-input" id="countrySearch" placeholder="Type country name (e.g., France, Japan, Switzerland, Canada)..." oninput="filterCountries()">
        </div>
        <div style="max-height:300px; overflow-y:auto; border:1px solid #dfe3e7; border-radius:3px;">
            <table class="ol-table" id="countryTable" style="margin:0;">
                <thead>
                    <tr><th>Nation</th><th>Advisory Tier</th><th>Sangaia Embassy Status</th><th>Entry Conditions</th></tr>
                </thead>
                <tbody>
                    <tr class="country-row"><td>Switzerland</td><td><span class="ol-badge-tag ol-badge-success">Level 1: Normal Caution</span></td><td>Bern Embassy &bull; Fully Operational</td><td>Visa-free 90 Days</td></tr>
                    <tr class="country-row"><td>Japan</td><td><span class="ol-badge-tag ol-badge-success">Level 1: Normal Caution</span></td><td>Tokyo Embassy &bull; Fully Operational</td><td>Visa-free 90 Days</td></tr>
                    <tr class="country-row"><td>Norway</td><td><span class="ol-badge-tag ol-badge-success">Level 1: Normal Caution</span></td><td>Oslo Embassy &bull; Fully Operational</td><td>Visa-free 90 Days</td></tr>
                    <tr class="country-row"><td>Canada</td><td><span class="ol-badge-tag ol-badge-success">Level 1: Normal Caution</span></td><td>Ottawa Embassy &bull; Fully Operational</td><td>Visa-free 90 Days</td></tr>
                    <tr class="country-row"><td>United Kingdom</td><td><span class="ol-badge-tag ol-badge-success">Level 1: Normal Caution</span></td><td>London Embassy &bull; Fully Operational</td><td>Visa-free 90 Days</td></tr>
                    <tr class="country-row"><td>United States</td><td><span class="ol-badge-tag ol-badge-warning">Level 2: Exercise Caution</span></td><td>Washington Embassy &bull; Operational</td><td>Electronic Visa Clearance</td></tr>
                    <tr class="country-row"><td>Germany</td><td><span class="ol-badge-tag ol-badge-success">Level 1: Normal Caution</span></td><td>Berlin Embassy &bull; Fully Operational</td><td>Visa-free 90 Days</td></tr>
                    <tr class="country-row"><td>France</td><td><span class="ol-badge-tag ol-badge-success">Level 1: Normal Caution</span></td><td>Paris Embassy &bull; Fully Operational</td><td>Visa-free 90 Days</td></tr>
                    <tr class="country-row"><td>Australia</td><td><span class="ol-badge-tag ol-badge-success">Level 1: Normal Caution</span></td><td>Canberra Embassy &bull; Fully Operational</td><td>Visa-free 90 Days</td></tr>
                    <tr class="country-row"><td>New Zealand</td><td><span class="ol-badge-tag ol-badge-success">Level 1: Normal Caution</span></td><td>Wellington Embassy &bull; Fully Operational</td><td>Visa-free 90 Days</td></tr>
                    <tr class="country-row"><td>Brazil</td><td><span class="ol-badge-tag ol-badge-warning">Level 2: Exercise Caution</span></td><td>Brasília Embassy &bull; Operational</td><td>Consular Visa Required</td></tr>
                    <tr class="country-row"><td>South Africa</td><td><span class="ol-badge-tag ol-badge-warning">Level 2: Exercise Caution</span></td><td>Pretoria Embassy &bull; Operational</td><td>Consular Visa Required</td></tr>
                    <tr class="country-row"><td>Ukraine</td><td><span class="ol-badge-tag ol-badge-danger">Level 4: Do Not Travel</span></td><td>Operations Remote / Warsaw Hub</td><td>Emergency Consular Only</td></tr>
                    <tr class="country-row"><td>Syria</td><td><span class="ol-badge-tag ol-badge-danger">Level 4: Do Not Travel</span></td><td>Operations Suspended</td><td>Strict Travel Warning</td></tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- Active & Past Sovereign Treaties -->
    <div class="ol-card" id="treaties">
        <div class="ol-card-title">
            <span>Sovereign Treaties &amp; International Accords Registry</span>
            <span class="ol-badge-tag">Ratified by Aeretocrat</span>
        </div>
        <table class="ol-table">
            <thead>
                <tr><th>Treaty Accord Title</th><th>Signatory Parties</th><th>Ratification</th><th>Scope of Accord</th></tr>
            </thead>
            <tbody>
                <tr><td>Geneva Maritime Passage Accord</td><td>Sangaia, Nordic &amp; Alpine States</td><td>Ratified 2024</td><td>Protection of commercial shipping and neutral ports</td></tr>
                <tr><td>Bilateral Clean Energy &amp; Battery Pact</td><td>Sangaia &amp; Pacific Alliance</td><td>Ratified 2025</td><td>Zero-tariff exchange of geothermal and lithium components</td></tr>
                <tr><td>Universal Diplomatic Immunity Treaty</td><td>International Red Cross &amp; Neutral Nations</td><td>Ratified 2024</td><td>Absolute protection of medical delegates and neutral attaches</td></tr>
            </tbody>
        </table>
    </div>

    <!-- Embassies & Consular Directory -->
    <div class="ol-card" id="embassies">
        <div class="ol-card-title">
            <span>Embassy &amp; Consular Availability</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openConsularModal()">Register Citizen Travel</button>
        </div>
        <p class="ol-small">Sangaia maintains 48 diplomatic missions and 112 consular posts worldwide to assist Sangaian citizens abroad with emergency passports, legal aid, and evacuation services.</p>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>External Affairs</h3>
        <p class="ol-small ol-muted">Manages diplomatic missions, international treaties, global commerce agreements, and consular services.</p>
        <div class="ol-mt-10">
            <a href="/externalaffairs_departments.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">Launch External Departments</a>
        </div>
    </div>
    """

    modals = """
    <!-- Consular Register Modal -->
    <div class="ol-modal-overlay" id="consularModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Register International Travel with Consular Service</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('consularModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Citizen Legal Name</label>
                <input type="text" class="ol-input" id="c-name" placeholder="Name as on Passport">
            </div>
            <div class="form-group">
                <label class="form-label">Sangaia Passport Number</label>
                <input type="text" class="ol-input" id="c-pass" placeholder="SG-P-XXXXXXX">
            </div>
            <div class="form-group">
                <label class="form-label">Destination Country</label>
                <input type="text" class="ol-input" id="c-dest" placeholder="e.g., Switzerland, Japan, Norway">
            </div>
            <div class="form-group">
                <label class="form-label">Dates of Travel</label>
                <input type="text" class="ol-input" id="c-dates" placeholder="Departure - Return">
            </div>
            <div class="modal-results-box" id="cResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('consularModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitConsular()">Register Travel Itinerary</button>
            </div>
        </div>
    </div>
    """

    scripts = """
    <script>
    function filterCountries() {
        const q = (document.getElementById('countrySearch').value || '').toLowerCase();
        document.querySelectorAll('.country-row').forEach(row => {
            row.style.display = row.innerText.toLowerCase().includes(q) ? '' : 'none';
        });
    }

    function openConsularModal() { document.getElementById('consularModal').classList.add('active'); }
    function closeModal(id) { document.getElementById(id).classList.remove('active'); }

    function submitConsular() {
        const res = document.getElementById('cResults');
        const token = 'CONS-REG-' + Math.floor(100000 + Math.random() * 900000);
        res.innerHTML = `<strong>Travel Registered:</strong> Itinerary Token: <span style="font-family:monospace;">${token}</span>. Nearest Embassy notified.`;
        res.classList.add('active');
    }
    </script>
    """

    nav_tabs = MINISTRY_NAV_TABS["externalaffairs"]
    sub_nav_tabs = get_subdomain_nav_tabs(nav_tabs)
    generate_page("externalaffairs.html", title, theme, "home", hero_title, hero_sub, "Ministry of External Affairs", "Foreign Service & Diplomatic Corp", "Missions Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=nav_tabs)
    generate_page("MdA/index.html", title, theme, "home", hero_title, hero_sub, "Ministry of External Affairs", "Foreign Service & Diplomatic Corp", "Missions Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)

# -----------------------------------------------------------------------------
# 8. MINISTRY OF THE ENVIRONMENT (MtE)
# -----------------------------------------------------------------------------
def build_environment():
    title = "Ministry of the Environment"
    theme = "theme-environment"
    tab = "environment"
    hero_title = "ministry of the environment"
    hero_sub = "Atmospheric telemetry (°Пт), biome funding, wildlife intervention, food availability & conservation"

    sidebar_links = [
        {"label": "Overview & Weather (°Пт)", "url": "#weather", "active": True},
        {"label": "Environmental Services", "url": "#services", "active": False},
        {"label": "Biome Funding by Province", "url": "#biome-funding", "active": False},
        {"label": "Wildlife Interventions", "url": "#wildlife", "active": False},
        {"label": "Food Security & Reserves", "url": "#food-security", "active": False},
        {"label": "Conservation & 3.4M Trees", "url": "#conservation", "active": False},
        {"label": "Departments Portal →", "url": "/environment_departments.html", "active": False}
    ]

    main_content = """

    <!-- Live Atmospheric Weather in Panotherm (°Пт) -->
    <div class="card" id="overview"><a id="weather"></a>
        <div class="ol-card-title">
            <span>Atmospheric Telemetry &bull; Standard Weather in Панотерм (&deg;Пт)</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="detectUserLocation()">Detect My Location Weather</button>
        </div>
        <p class="ol-small">Temperature reported in Sangaia's official unit: <strong>Панотерм (&deg;Пт)</strong>, where &deg;Пт = 0.9 &times; &deg;C = 0.5 &times; (&deg;F - 32).</p>

        <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:3px; padding:14px; margin-top:10px;">
            <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                <div>
                    <h3 id="currentLocTitle" style="color:#14532d; margin:0;">📍 New Jasper Central Station (Capital)</h3>
                    <div class="ol-small ol-muted">Automated Federal Atmospheric Array &bull; Live Telemetry</div>
                </div>
                <div style="display:flex; align-items:baseline; gap:8px;">
                    <span id="currentTempDisplay" style="font-size:36px; font-weight:700; color:#15803d;">20.5&deg;Пт</span>
                    <span class="ol-small ol-muted" id="tempEquiv">(22.8&deg;C / 73.0&deg;F)</span>
                </div>
            </div>

            <div class="ol-grid-3" style="margin-top:14px;">
                <div class="ol-metric-box">
                    <div class="ol-metric-val" id="weatherCond">Clear Sky</div>
                    <div class="ol-metric-lbl">Conditions</div>
                </div>
                <div class="ol-metric-box">
                    <div class="ol-metric-val">12 &deg;Пт / 24 &deg;Пт</div>
                    <div class="ol-metric-lbl">Daily Low / High</div>
                </div>
                <div class="ol-metric-box">
                    <div class="ol-metric-val">14 (Pure)</div>
                    <div class="ol-metric-lbl">Air Quality Index (AQI)</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Biome Funding Across the 5 Provinces -->
    <div class="ol-card" id="biome-funding">
        <div class="ol-card-title">
            <span>Provincial Biome Funding Allocations (FY2026)</span>
            <span class="ol-badge-tag ol-badge-success">$ 16.5 Billion Outlay</span>
        </div>
        <table class="ol-table">
            <thead>
                <tr><th>Provincial Biome</th><th>Territory</th><th>Annual Funding</th><th>Protected Habitat</th><th>Primary Target</th></tr>
            </thead>
            <tbody>
                <tr><td>Temperate Deciduous &amp; Oak Forest</td><td>New Jasper</td><td>$ 4.2 Billion</td><td>1,240,000 Hectares</td><td>Canopy Expansion &amp; River Basin Protection</td></tr>
                <tr><td>Alluvial Valley &amp; Prairie Grasslands</td><td>New Madison</td><td>$ 3.8 Billion</td><td>1,650,000 Hectares</td><td>Soil Micro-Biome &amp; Organic Pollinators</td></tr>
                <tr><td>Marine Estuary &amp; Tidal Salt Marshes</td><td>Liveland</td><td>$ 3.4 Billion</td><td>890,000 Hectares</td><td>Fishery Replenishment &amp; Coral Regeneration</td></tr>
                <tr><td>Subalpine Conifer &amp; Glacial Ridge</td><td>Sentinel</td><td>$ 2.9 Billion</td><td>2,100,000 Hectares</td><td>Glacial Water Purity &amp; Geothermal Safety</td></tr>
                <tr><td>Highland Savanna &amp; Wetlands</td><td>Columbia</td><td>$ 2.2 Billion</td><td>940,000 Hectares</td><td>Migratory Bird Corridors &amp; Wetland Buffers</td></tr>
            </tbody>
        </table>
    </div>

    <!-- Wildlife Intervention Initiatives -->
    <div class="ol-card" id="wildlife">
        <div class="ol-card-title">
            <span>Wildlife Intervention &amp; Endangered Habitat Rescue</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openWildlifeModal()">Report Injured Wildlife</button>
        </div>
        <p class="ol-small">The Department of Wildlife Protection operates 24/7 rescue stations across all 5 provinces to rehabilitate native fauna and enforce zero-poaching laws.</p>
        <div class="ol-grid-2" style="margin-top:10px;">
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong>Golden Osprey &amp; Falcon Restoration:</strong>
                <div class="ol-small" style="margin-top:4px;">1,420 breeding pairs monitored in Liveland and Sentinel. Species officially elevated from Threatened to Stable.</div>
            </div>
            <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:3px; padding:12px;">
                <strong>Sangaian River Otter Protection:</strong>
                <div class="ol-small" style="margin-top:4px;">River corridor connectivity program restored 340 km of unbroken freshwater migration routes.</div>
            </div>
        </div>
    </div>

    <!-- Food Availability & Strategic Reserves -->
    <div class="ol-card" id="food-security">
        <div class="ol-card-title">
            <span>Food Availability &amp; Strategic Grain Reserves</span>
            <span class="ol-badge-tag ol-badge-success">100% Domestic Self-Sufficiency</span>
        </div>
        <p class="ol-small">Sangaia maintains a 24-month sovereign grain and seed reserve to protect citizens against global supply chain shocks or extreme weather.</p>
        <div class="ol-grid-3" style="margin-top:10px;">
            <div class="ol-metric-box">
                <div class="ol-metric-val">24 Months</div>
                <div class="ol-metric-lbl">Strategic Grain Reserve</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">100%</div>
                <div class="ol-metric-lbl">Organic Public School Diet</div>
            </div>
            <div class="ol-metric-box">
                <div class="ol-metric-val">$ 0.00</div>
                <div class="ol-metric-lbl">Tax on Basic Staples</div>
            </div>
        </div>
    </div>

    <!-- Conservation & Native Tree Counter -->
    <div class="ol-card" id="conservation">
        <div class="ol-card-title">
            <span>Conservation Efforts &amp; Sovereign Reforestation</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openTreeModal()">Log Tree Planting</button>
        </div>
        <div style="text-align:center; padding:16px 0;">
            <div class="ol-small ol-muted">TOTAL NATIVE TREES PLANTED UNDER CITIZEN INITIATIVE:</div>
            <div style="font-size:36px; font-weight:700; color:#15803d; margin:6px 0;" id="treeCountVal">3,420,840</div>
            <div class="ol-small">Goal: 5,000,000 Trees by 2028 across all 5 Provinces</div>
        </div>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Environment Portal</h3>
        <p class="ol-small ol-muted">Permits for eco-construction, biome stewardship, wildlife intervention, and water source protection.</p>
        <div class="ol-mt-10">
            <a href="/environment_departments.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">Launch Environment Departments</a>
        </div>
    </div>
    """

    modals = """
    <!-- Wildlife Modal -->
    <div class="ol-modal-overlay" id="wildModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Report Injured or Endangered Wildlife</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('wildModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Observed Species</label>
                <input type="text" class="ol-input" id="w-species" placeholder="e.g., Golden Osprey, River Otter, Red Fox">
            </div>
            <div class="form-group">
                <label class="form-label">Province &amp; Specific Location / Trail Marker</label>
                <input type="text" class="ol-input" id="w-loc" placeholder="e.g., Sentinel Ridge Trail 4">
            </div>
            <div class="form-group">
                <label class="form-label">Condition &amp; Urgency</label>
                <textarea class="ol-textarea" id="w-desc" rows="3" placeholder="Describe injuries or hazards..."></textarea>
            </div>
            <div class="modal-results-box" id="wildResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('wildModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitWildlife()">Dispatch Wildlife Rescue</button>
            </div>
        </div>
    </div>

    <!-- Tree Modal -->
    <div class="ol-modal-overlay" id="treeModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Record Citizen Tree Planting</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('treeModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Citizen Name / Group</label>
                <input type="text" class="ol-input" id="t-name" placeholder="Name or School / Guild">
            </div>
            <div class="form-group">
                <label class="form-label">Number of Native Trees Planted</label>
                <input type="number" class="ol-input" id="t-count" value="10" min="1" max="500">
            </div>
            <div class="form-group">
                <label class="form-label">Species &amp; Province</label>
                <input type="text" class="ol-input" id="t-species" placeholder="e.g., White Oak in New Madison">
            </div>
            <div class="modal-results-box" id="treeResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('treeModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="submitTree()">Register to Reforestation Ledger</button>
            </div>
        </div>
    </div>
    """

    scripts = """
    <script>
    function detectUserLocation() {
        const title = document.getElementById('currentLocTitle');
        const temp = document.getElementById('currentTempDisplay');
        const equiv = document.getElementById('tempEquiv');
        title.innerText = '📍 Detected Location: Regional Sensor Array';
        temp.innerText = '21.0°Пт';
        equiv.innerText = '(23.3°C / 74.0°F)';
    }

    function openWildlifeModal() { document.getElementById('wildModal').classList.add('active'); }
    function openTreeModal() { document.getElementById('treeModal').classList.add('active'); }
    function closeModal(id) { document.getElementById(id).classList.remove('active'); }

    function submitWildlife() {
        const res = document.getElementById('wildResults');
        const token = 'WILD-RESC-' + Math.floor(100000 + Math.random() * 900000);
        res.innerHTML = `<strong>Ranger Unit Dispatched:</strong> Tracking Token: <span style="font-family:monospace;">${token}</span>. Nearest Wildlife Haven notified.`;
        res.classList.add('active');
    }

    function submitTree() {
        const count = parseInt(document.getElementById('t-count').value) || 10;
        const cur = 3420840;
        const updated = cur + count;
        document.getElementById('treeCountVal').innerText = updated.toLocaleString();
        const res = document.getElementById('treeResults');
        res.innerHTML = `<strong>Reforestation Confirmed:</strong> Added ${count} trees to national ledger. Total: ${updated.toLocaleString()}!`;
        res.classList.add('active');
    }
    </script>
    """

    nav_tabs = MINISTRY_NAV_TABS["environment"]
    sub_nav_tabs = get_subdomain_nav_tabs(nav_tabs)
    generate_page("environment.html", title, theme, "home", hero_title, hero_sub, "Ministry of the Environment", "Ecological Stewardship Authority", "Telemetry Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=nav_tabs)
    generate_page("MtE/index.html", title, theme, "home", hero_title, hero_sub, "Ministry of the Environment", "Ecological Stewardship Authority", "Telemetry Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)
    generate_page("mEnv/index.html", title, theme, "home", hero_title, hero_sub, "Ministry of the Environment", "Ecological Stewardship Authority", "Telemetry Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)

# -----------------------------------------------------------------------------
# 9. MINISTRY OF PROPAGANDA (mP)
# -----------------------------------------------------------------------------
def build_propaganda():
    title = "Ministry of Propaganda"
    theme = "theme-propaganda"
    tab = "propaganda"
    hero_title = "ministry of propaganda & public information"
    hero_sub = "Civic broadcasting, live streaming radio, reporter integrity standards & recognized churches"

    sidebar_links = [
        {"label": "Overview & Public Truth", "url": "#overview", "active": True},
        {"label": "National TV Channels", "url": "#tv", "active": False},
        {"label": "Live Radio Broadcasts", "url": "#radio", "active": False},
        {"label": "Reporter Accreditation", "url": "#reporters", "active": False},
        {"label": "Recognized Churches", "url": "#churches", "active": False},
        {"label": "Departments Portal →", "url": "/propaganda_departments.html", "active": False}
    ]

    main_content = """

    <!-- Live Audio Radio Player -->
    <div class="card" id="overview"><a id="radio"></a>
        <div class="ol-card-title">
            <span>Sangaia National Public Radio &bull; Live Audio Broadcast</span>
            <span class="ol-badge-tag ol-badge-success">ON AIR NOW</span>
        </div>
        <p class="ol-small">Tune in live to Sangaia National Radio 1: Civic addresses, classical orchestral performances, agricultural reports, and evening philosophical debates.</p>

        <div style="background:#fff7ed; border:1px solid #fed7aa; border-radius:3px; padding:16px; margin-top:10px;">
            <div style="display:flex; align-items:center; justify-content:space-between; flex-wrap:wrap; gap:12px;">
                <div>
                    <strong style="color:#7c2d12; font-size:15px;" id="currentTrackTitle">📻 Sangaia National Radio 1 &bull; 94.5 FM Stereo</strong>
                    <div class="ol-small ol-muted">Now Playing: "Concert for the Five Provinces" &bull; Shesk Philharmonic Orchestra</div>
                </div>
                <div style="display:flex; align-items:center; gap:8px;">
                    <button type="button" class="ol-btn ol-btn-primary" id="radioPlayBtn" onclick="toggleRadio()">▶ Listen Live</button>
                    <span class="ol-badge-tag" id="radioStatus">Buffer Ready</span>
                </div>
            </div>
            <!-- Standard simulated Web Audio synthesis for authentic radio tone -->
            <audio id="simAudio" preload="none"></audio>
        </div>
    </div>

    <!-- Sovereign TV & Educational Channels -->
    <div class="ol-card" id="tv">
        <div class="ol-card-title">
            <span>National Television &amp; Educational Broadcast Networks</span>
            <span class="ol-badge-tag">Free Over-The-Air &amp; Digital</span>
        </div>
        <table class="ol-table">
            <thead>
                <tr><th>Channel</th><th>Network Name</th><th>Programming Focus</th><th>Broadcast Availability</th></tr>
            </thead>
            <tbody>
                <tr><td>Channel 1</td><td>Sangaia State Television (SSTV)</td><td>Official State Addresses, Documentary &amp; World News</td><td>All 5 Provinces (1080p DTV)</td></tr>
                <tr><td>Channel 2</td><td>The Civic Academy (EduTV)</td><td>University Lectures, STEM Curriculum &amp; Language Lessons</td><td>All 5 Provinces (1080p DTV)</td></tr>
                <tr><td>Channel 3</td><td>Provincial Culture &amp; Arts (PCA)</td><td>Regional Theater, Folklore, Classical Symphony &amp; Poetry</td><td>All 5 Provinces (1080p DTV)</td></tr>
                <tr><td>Channel 4</td><td>Agricultural &amp; Biome Network (ABN)</td><td>Farming Techniques, Weather in &deg;Пт, Wildlife Reports</td><td>All 5 Provinces (1080p DTV)</td></tr>
            </tbody>
        </table>
    </div>

    <!-- Reporter Integrity & Accreditation Standards -->
    <div class="ol-card" id="reporters">
        <div class="ol-card-title">
            <span>Professional Journalist &amp; Reporter Accreditation Registry</span>
            <button type="button" class="ol-btn ol-btn-sm" onclick="openPressModal()">Verify Press Credential</button>
        </div>
        <p class="ol-small">Under the Truth in Journalism Accord, accredited reporters must declare all commercial sponsors, publish unedited interview transcripts upon request, and are protected from state censorship.</p>
    </div>

    <!-- Recognized Churches in Sangaia -->
    <div class="ol-card" id="churches">
        <div class="ol-card-title">
            <span>Registry of Recognized Churches &amp; Religious Societies</span>
            <span class="ol-badge-tag">Freedom of Conscience</span>
        </div>
        <p class="ol-small">Freedom of religion is constitutionally inviolable in Sangaia. Under statutory law, recognized churches must commit 85%+ of voluntary tithes directly to charity, soup kitchens, and community shelter.</p>
        <table class="ol-table">
            <thead>
                <tr><th>Religious Society / Chapel</th><th>Tradition</th><th>Headquarters</th><th>Charity Compliance</th></tr>
            </thead>
            <tbody>
                <tr><td>Chapel of St. Julian the Hospitaller</td><td>Christian Ecumenical</td><td>Shesk (New Jasper)</td><td><span class="ol-badge-tag ol-badge-success">91.4% Tithes Returned</span></td></tr>
                <tr><td>Azure Coastal Interfaith Fellowship</td><td>Interfaith Contemplative</td><td>Oaks (Liveland)</td><td><span class="ol-badge-tag ol-badge-success">88.5% Tithes Returned</span></td></tr>
                <tr><td>Highland Buddhist Peace Sanctuary</td><td>Buddhist Monastic</td><td>Sentinel Ridge (Sentinel)</td><td><span class="ol-badge-tag ol-badge-success">94.0% Tithes Returned</span></td></tr>
                <tr><td>Madison Reform Synagogue</td><td>Jewish Traditional</td><td>Madison City (New Madison)</td><td><span class="ol-badge-tag ol-badge-success">89.2% Tithes Returned</span></td></tr>
            </tbody>
        </table>
    </div>
    """

    sidebar_right = """
    <div class="ol-sidebox">
        <h3>Public Information</h3>
        <p class="ol-small ol-muted">Oversees state broadcasting networks, journalist accreditation, civic communications, and recognized religious registries.</p>
        <div class="ol-mt-10">
            <a href="/propaganda_departments.html" class="ol-btn ol-btn-primary ol-btn-sm" style="width:100%; text-align:center;">Launch Propaganda Departments</a>
        </div>
    </div>
    """

    modals = """
    <!-- Press Verify Modal -->
    <div class="ol-modal-overlay" id="pressModal">
        <div class="ol-modal-dialog">
            <div class="ol-modal-head">
                <span class="ol-modal-title">Verify Official Press Accreditation</span>
                <button type="button" class="ol-modal-close" onclick="closeModal('pressModal')">&times;</button>
            </div>
            <div class="form-group">
                <label class="form-label">Journalist Name or Press Card ID</label>
                <input type="text" class="ol-input" id="pr-name" placeholder="e.g., Marcus Vance or SG-PRESS-1049">
            </div>
            <div class="modal-results-box" id="prResults"></div>
            <div class="ol-modal-foot">
                <button type="button" class="ol-btn" onclick="closeModal('pressModal')">Cancel</button>
                <button type="button" class="ol-btn ol-btn-primary" onclick="verifyPress()">Verify Credential</button>
            </div>
        </div>
    </div>
    """

    scripts = """
    <script>
    let isPlaying = false;
    let audioCtx = null;
    let osc = null;

    function toggleRadio() {
        const btn = document.getElementById('radioPlayBtn');
        const st = document.getElementById('radioStatus');
        if (!isPlaying) {
            isPlaying = true;
            btn.innerText = '⏸ Pause Stream';
            st.innerText = 'STREAMING LIVE (94.5 FM)';
            st.className = 'ol-badge-tag ol-badge-success';

            // Generate soft atmospheric chime using Web Audio API to simulate broadcast
            try {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
                osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(440, audioCtx.currentTime); // Concert A
                gain.gain.setValueAtTime(0.04, audioCtx.currentTime);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
            } catch(e) {}
        } else {
            isPlaying = false;
            btn.innerText = '▶ Listen Live';
            st.innerText = 'Buffer Ready';
            st.className = 'ol-badge-tag';
            if (osc) {
                try { osc.stop(); } catch(e){}
            }
        }
    }

    function openPressModal() { document.getElementById('pressModal').classList.add('active'); }
    function closeModal(id) { document.getElementById(id).classList.remove('active'); }

    function verifyPress() {
        const res = document.getElementById('prResults');
        res.innerHTML = `<strong>Accreditation Status:</strong> Verified Active Foreign/Domestic Journalist &bull; Sovereign Press Shield Protected &bull; Certified by Ministry of Propaganda.`;
        res.classList.add('active');
    }
    </script>
    """

    nav_tabs = MINISTRY_NAV_TABS["propaganda"]
    sub_nav_tabs = get_subdomain_nav_tabs(nav_tabs)
    generate_page("propaganda.html", title, theme, "home", hero_title, hero_sub, "Ministry of Propaganda", "Civic Information Authority", "Broadcasts Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=nav_tabs)
    generate_page("mP/index.html", title, theme, "home", hero_title, hero_sub, "Ministry of Propaganda", "Civic Information Authority", "Broadcasts Active", sidebar_links, main_content, sidebar_right, modals, scripts, custom_nav_tabs=sub_nav_tabs)

if __name__ == "__main__":
    build_executive()
    build_treasury()
    build_work()
    build_healthcare()
    build_education()
    build_domestic()
    build_external()
    build_environment()
    build_propaganda()
    print("All 9 Ministry Homepages successfully generated in One Live Wave 4 architecture!")
