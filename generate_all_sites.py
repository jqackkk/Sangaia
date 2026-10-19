#!/usr/bin/env python3
"""
Comprehensive Sangaia Live Site Generator
Generates all pages in the Sangaia repository following the One Live Wave 4 architecture.
Strictly adheres to:
1. Zero design discrepancies across all sites.
2. Segoe WP typography.
3. Ministerial accent colors via CSS variables and theme classes.
4. Preserving all rich content, interactive tools, calculators, telemetry, and forms.
5. All 5 provinces: New Jasper, New Madison, Liveland, Sentinel, Columbia.
6. Sangaian currency '$', temperature '°Пт', distance 'Мн'.
7. Sangaian Cyrillic translations omitted for now as requested.
"""

import os
import re
import json

def generate_page(
    filename,
    title,
    theme_class,
    active_tab,
    hero_title,
    hero_sub,
    sidebar_title,
    sidebar_subtitle,
    sidebar_status,
    sidebar_nav_links,
    main_content_html,
    sidebar_right_extra_html="",
    modal_dialog_html="",
    extra_scripts=""
):
    nav_tabs = [
        ("home", "Home", "/index.html"),
        ("executive", "Executive", "/executive.html"),
        ("treasury", "Treasury", "/treasury.html"),
        ("work", "Work", "/work.html"),
        ("healthcare", "Healthcare", "/healthcare.html"),
        ("education", "Education", "/education.html"),
        ("domestic", "Domestic", "/domesticaffairs.html"),
        ("external", "External", "/externalaffairs.html"),
        ("environment", "Environment", "/environment.html"),
        ("propaganda", "Propaganda", "/propaganda.html"),
        ("services", "Services", "/services.html"),
        ("units", "Units (Мн • °Пт)", "/units.html"),
    ]

    tabs_html = ""
    for tab_id, tab_label, tab_url in nav_tabs:
        cur_class = ' class="ol-current"' if tab_id == active_tab else ''
        tabs_html += f'<li{cur_class}><a href="{tab_url}">{tab_label}</a></li>\n            '

    sidenav_items_html = ""
    for item in sidebar_nav_links:
        label = item.get("label")
        url = item.get("url")
        sel_class = ' class="sel"' if item.get("active") else ''
        sidenav_items_html += f'<li><a href="{url}"{sel_class}>{label}</a></li>\n'

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} :: Sangaia Live</title>
    <link rel="stylesheet" href="/css/sangaia-live.css">
    <script src="/js/sangaia-live.js" defer></script>
</head>
<body class="{theme_class}">

<!-- Top Live Mast Banner -->
<div class="wl-mast">
    <div class="ol-container wl-mast-inner">
        <div class="ol-header-top">
            <div class="ol-logo">
                <a href="/index.html" aria-label="Sangaia Live Sovereign Portal">
                    <svg viewBox="0 0 90 90" width="22" height="22" fill="currentColor">
                        <rect x="0" y="0" width="41" height="41" rx="2"/>
                        <rect x="49" y="0" width="41" height="41" rx="2"/>
                        <rect x="0" y="49" width="41" height="41" rx="2"/>
                        <rect x="49" y="49" width="41" height="41" rx="2"/>
                    </svg>
                    <span><b>Sangaia</b> Live</span>
                </a>
            </div>
            <div class="ol-header-tools">
                <form class="ol-search" id="headerSearchForm" action="/services.html" method="get">
                    <input type="text" id="headerSearch" name="q" placeholder="Search government &amp; services" aria-label="Search">
                    <button type="submit" class="ol-search-bing" aria-label="Search">&#x1F50E;</button>
                </form>
                
                <a class="ol-icon-btn" href="/services.html" title="Notifications">
                    <svg width="16" height="16" viewBox="0 0 16 16"><path fill="currentColor" d="M8 1.5c-2.4 0-4 1.9-4 4.2v3L2.7 11c-.3.4 0 1 .5 1h9.6c.5 0 .8-.6.5-1L12 8.7v-3c0-2.3-1.6-4.2-4-4.2zm0 13c1 0 1.8-.7 2-1.5H6c.2.8 1 1.5 2 1.5z"/></svg>
                    <span class="ol-badge">3</span>
                </a>
                <a class="ol-icon-btn" href="/services.html" title="Citizen Messages">
                    <svg width="16" height="16" viewBox="0 0 16 16"><path fill="currentColor" d="M2 3h12c.6 0 1 .4 1 1v7c0 .6-.4 1-1 1H9l-3.4 2.6c-.4.3-.9 0-.9-.5V12H2c-.6 0-1-.4-1-1V4c0-.6.4-1 1-1z"/></svg>
                    <span class="ol-badge">1</span>
                </a>
                <div class="ol-me">
                    <div class="ol-me-chip" id="meChip">
                        <span class="ol-avatar sm">
                            <img src="/images/1.jpeg" alt="Citizen Profile">
                            <span class="ol-presence-dot"></span>
                        </span>
                        <span class="ol-me-name">Jqackkk</span>
                        <span class="ol-me-caret">&#9660;</span>
                    </div>
                    <div class="ol-me-menu" id="meMenu" style="display:none; position:absolute; right:0; top:36px; background:#fff; border:1px solid #dfe3e7; border-radius:3px; box-shadow:0 2px 8px rgba(0,0,0,0.15); width:180px; z-index:1000; padding:6px 0;">
                        <div style="padding:4px 12px; font-size:11px; font-weight:700; color:#64748b; text-transform:uppercase;">Citizen ID: SG-2026-F1E8</div>
                        <a href="/id.html" style="display:block; padding:5px 12px; color:#2a2a2a; font-size:13px;">Sangaia ID Card</a>
                        <a href="/citizenship.html" style="display:block; padding:5px 12px; color:#2a2a2a; font-size:13px;">Citizenship Status</a>
                        <a href="/units.html" style="display:block; padding:5px 12px; color:#2a2a2a; font-size:13px;">Units &amp; Measures</a>
                        <div style="border-top:1px solid #edf0f3; margin:4px 0;"></div>
                        <a href="/index.html" style="display:block; padding:5px 12px; color:#2a2a2a; font-size:13px;">Federal Home</a>
                    </div>
                </div>
            </div>
        </div>

        <div class="ol-band">
            <div class="ol-band-inner">
                <h1>{hero_title}</h1>
                <p class="ol-band-sub">{hero_sub}</p>
            </div>
        </div>
    </div>
</div>

<!-- Main Top Nav Tabs (One Live Bar) -->
<div class="wl-tabs">
    <div class="ol-container wl-tabs-inner">
        <ul class="ol-nav" id="primaryNav">
            {tabs_html}
        </ul>
    </div>
</div>

<!-- Main Content Grid -->
<div class="ol-container ol-main">
    <div class="ol-with-sidebar">
        <!-- Left Sidebar Navigation -->
        <div class="ol-sidebar-nav">
            <div class="ol-card ol-profile-card" style="text-align: center;">
                <span class="ol-avatar lg">
                    <img src="/images/1.jpeg" alt="Emblem">
                    <span class="ol-presence-dot"></span>
                </span>
                <div class="ol-mt-10">
                    <strong>{sidebar_title}</strong><br>
                    <span class="ol-muted ol-small">{sidebar_subtitle}</span><br>
                    <span class="ol-small" style="color:var(--ol-accent); font-weight:600;">{sidebar_status}</span>
                </div>
            </div>

            <span class="ol-sidenav-label">Portal Navigation</span>
            <ul class="ol-sidenav">
                {sidenav_items_html}
            </ul>

            <span class="ol-sidenav-label">Federal Network</span>
            <ul class="ol-sidenav">
                <li><a href="/index.html">Federal Home</a></li>
                <li><a href="/services.html">All Services</a></li>
                <li><a href="/units.html">Units (Мн &bull; &deg;Пт)</a></li>
                <li><a href="/societal_press.html">Societal Press</a></li>
            </ul>
        </div>

        <!-- Center Content -->
        <div class="ol-content">
            {main_content_html}
        </div>

        <!-- Right Sidebar (Telemetry & Quick Actions) -->
        <div class="ol-sidebar">
            <div class="ol-note">Official Government of the Sovereign Republic of Sangaia. All administrative systems active.</div>

            <div class="ol-sidebox">
                <h3>Sovereign Telemetry</h3>
                <div style="font-size:12.5px; line-height:1.6;">
                    <div><strong>Currency:</strong> Sangaian Dollar ($)</div>
                    <div><strong>Standard Temp:</strong> 22.5&deg;Пт (25&deg;C / 77&deg;F)</div>
                    <div><strong>Standard Metric:</strong> 1 Мн = 2.5 cm</div>
                    <div><strong>Active Provinces:</strong> 5 Territories</div>
                </div>
            </div>

            <div class="ol-sidebox">
                <h3>Provincial Weather (&deg;Пт)</h3>
                <table class="ol-table" style="font-size:12px; margin:0;">
                    <tr><td>New Jasper</td><td style="text-align:right;"><strong>20.5&deg;Пт</strong> (Sunny)</td></tr>
                    <tr><td>New Madison</td><td style="text-align:right;"><strong>22.0&deg;Пт</strong> (Clear)</td></tr>
                    <tr><td>Liveland</td><td style="text-align:right;"><strong>19.8&deg;Пт</strong> (Breezy)</td></tr>
                    <tr><td>Sentinel</td><td style="text-align:right;"><strong>16.2&deg;Пт</strong> (Cool)</td></tr>
                    <tr><td>Columbia</td><td style="text-align:right;"><strong>23.4&deg;Пт</strong> (Mild)</td></tr>
                </table>
            </div>

            {sidebar_right_extra_html}
        </div>
    </div>
</div>

{modal_dialog_html}

<!-- Floating Citizen Dock -->
<div class="ol-dock">
    <button type="button" class="ol-dock-tab" id="olDockMessages">
        <svg width="15" height="15" viewBox="0 0 16 16"><path fill="currentColor" d="M2 3h12c.6 0 1 .4 1 1v7c0 .6-.4 1-1 1H9l-3.4 2.6c-.4.3-.9 0-.9-.5V12H2c-.6 0-1-.4-1-1V4c0-.6.4-1 1-1z"/></svg>
        <span>Live Citizen Support</span>
    </button>
    <div class="ol-dock-list" id="olDockList">
        <div class="ol-dock-list-head">
            <span>Sangaia Citizen Assistance</span>
            <a href="javascript:void(0)" id="olDockListClose" style="color:#64748b; font-size:16px;">&times;</a>
        </div>
        <div class="ol-dock-list-body">
            <a class="ol-dock-item" href="/services.html"><strong>Online Inquiries:</strong> File petition or request</a>
            <a class="ol-dock-item" href="/units.html"><strong>Unit Calculations:</strong> Monomer &amp; Panotherm</a>
            <a class="ol-dock-item" href="/citizenship.html"><strong>Citizenship Registry:</strong> Check docket status</a>
            <a class="ol-dock-item" href="/id.html"><strong>Sangaia ID:</strong> Digital identity card</a>
        </div>
    </div>
</div>

<!-- Footer -->
<div class="ol-footer">
    <div class="ol-container ol-footer-inner">
        <p class="ol-footer-copy">&copy; 2026 Sovereign Republic of Sangaia. One Live Wave 4 Infrastructure.</p>
        <ul class="ol-footer-links">
            <li><a href="/index.html">Home</a></li>
            <li><a href="/government.html">Government Structure</a></li>
            <li><a href="/services.html">Services</a></li>
            <li><a href="/societal_press.html">Gazette</a></li>
            <li><a href="/units.html">Units System</a></li>
            <li><a href="/about.html">About Sangaia</a></li>
        </ul>
    </div>
</div>

{extra_scripts}

</body>
</html>
"""
    # Write file
    os.makedirs(os.path.dirname(os.path.abspath(filename)), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(page_html)
    print(f"Generated {filename}")

print("Page generation core ready.")
