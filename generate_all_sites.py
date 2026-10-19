#!/usr/bin/env python3
"""
Master Sangaia Live Site Generator
Renders pages following the user's exact One Live template architecture:
1. Zero design discrepancies across all sites.
2. Segoe WP typography ('Segoe WP', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif).
3. MetroUI Icons (https://cdn.metroui.org.ua/4.5.12/icons.css) with mif-... classes.
4. Ministerial accent colors via CSS variables and theme classes.
5. All 5 provinces: New Jasper, New Madison, Liveland, Sentinel, Columbia.
6. Sangaian currency '$', temperature '°Пт', distance 'Мн'.
7. Sangaian Cyrillic translations omitted for now as requested.
8. Core CSS embedded directly in <style> to prevent unstyled/vertical rendering due to caching.
9. No personal face images anywhere on the site.
10. No social media features (no status fields, no trending tags, no telemetry widgets).
"""

import os
import re

CSS_PATH = os.path.join(os.path.dirname(__file__), "css", "sangaia-live.css")
with open(CSS_PATH, "r", encoding="utf-8") as _f:
    MASTER_EMBEDDED_CSS = _f.read()

THEME_MINISTRY_MAP = {
    "theme-executive": ("ministry of the executive", "executive.html"),
    "theme-treasury": ("ministry of the treasury", "treasury.html"),
    "theme-work": ("ministry of work", "work.html"),
    "theme-healthcare": ("ministry of healthcare", "healthcare.html"),
    "theme-education": ("ministry of education", "education.html"),
    "theme-domestic": ("ministry of domestic affairs", "domesticaffairs.html"),
    "theme-external": ("ministry of external affairs", "externalaffairs.html"),
    "theme-environment": ("ministry of the environment", "environment.html"),
    "theme-propaganda": ("ministry of propaganda", "propaganda.html"),
}
MINISTRY_SUBDIRS = {"MoEX", "mEx", "mT", "mW", "mH", "mEd", "mE", "MdA", "MiA", "MtE", "mEnv", "mP"}

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
    extra_scripts="",
    custom_nav_tabs=None,
    sidebar_info_html=None,
    brand_text=None,
    brand_url=None
):
    norm_filename = filename.replace("\\", "/")
    parts = norm_filename.split("/")

    if brand_text is None:
        if theme_class in THEME_MINISTRY_MAP:
            brand_text = THEME_MINISTRY_MAP[theme_class][0]
        else:
            brand_text = "sangaia live"

    if brand_url is None:
        if theme_class in THEME_MINISTRY_MAP:
            root_page = THEME_MINISTRY_MAP[theme_class][1]
            if len(parts) == 2 and parts[0] in MINISTRY_SUBDIRS:
                brand_url = "index.html"
            else:
                brand_url = f"/{root_page}"
        else:
            brand_url = "/index.html"

    if custom_nav_tabs:
        nav_tabs = custom_nav_tabs
    else:
        nav_tabs = [
            ("home", "home", "/index.html"),
            ("overview", "overview", "/index.html#overview"),
            ("provinces", "5 provinces", "/index.html#showcase"),
            ("aeretocracy", "the aeretocracy", "/index.html#aeretocracy"),
            ("ministries", "9 ministries", "/index.html#ministries"),
            ("services", "services", "/services.html"),
            ("units", "units (мн • °пт)", "/index.html#units"),
        ]

    subnav_html = ""
    for tab_id, tab_label, tab_url in nav_tabs:
        cur_class = ' class="active"' if tab_id == active_tab else ''
        subnav_html += f'    <a href="{tab_url}"{cur_class}>{tab_label}</a>\n'

    sidebar_nav_html = ""
    if sidebar_nav_links:
        links_rendered = ""
        for item in sidebar_nav_links:
            label = item.get("label", "")
            url = item.get("url", "#")
            sel_class = ' class="active"' if item.get("active") else ''
            icon = item.get("icon", "mif-chevron-right")
            links_rendered += f'<li><a href="{url}"{sel_class}><span class="{icon}"></span> {label}</a></li>\n'

        sidebar_nav_html = f"""
      <div class="card">
        <h3>{sidebar_title or 'directory & navigation'}</h3>
        <p style="color: var(--text-muted); font-size: 12px; margin-bottom: 8px;">{sidebar_subtitle or 'official portals'}</p>
        <ul class="sidebar-nav-list">
          {links_rendered}
        </ul>
      </div>
"""

    if sidebar_info_html is None:
        sidebar_info_html = """
      <div class="card" style="font-size: 12px; line-height: 1.6;">
        <h3 style="color: var(--text-main); margin-bottom: 6px;">official government seal</h3>
        <p style="color: var(--text-muted); margin-bottom: 8px;">united provinces of sangaia &bull; sovereign constitutional gateway</p>
        <div style="display: flex; flex-direction: column; gap: 4px; color: var(--text-muted);">
          <div><strong style="color: var(--text-main);">jurisdiction:</strong> 5 provinces (new jasper, new madison, liveland, sentinel, columbia)</div>
          <div><strong style="color: var(--text-main);">currency:</strong> $ (sangaian dollar)</div>
          <div><strong style="color: var(--text-main);">standards:</strong> панотерм (°пт) &bull; мономер (мн)</div>
          <div><strong style="color: var(--text-main);">classification:</strong> verified official portal</div>
        </div>
      </div>
"""

    page_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} :: Sangaia Live</title>
  <link href="https://cdn.metroui.org.ua/4.5.12/icons.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
  <style>
{MASTER_EMBEDDED_CSS}
  </style>
  <link rel="stylesheet" href="/css/sangaia-live.css?v=20261019_v5">
  <script src="/js/sangaia-live.js" defer></script>
</head>
<body class="{theme_class}">

  <!-- Top Hero Header -->
  <header class="hero-header">
    <div class="top-bar">
      <div class="brand">
        <a href="{brand_url}"><span class="mif-windows"></span> {brand_text}</a>
      </div>
      <div class="top-right">
        <form class="search-box" action="/services.html" method="get">
          <input type="text" name="q" placeholder="search services, laws &amp; gazette" />
          <button type="submit" aria-label="Search"><span class="mif-search"></span></button>
        </form>
        <div class="user-profile-menu" id="userProfileMenu">
          <img src="/images/default-wl.png" alt="Avatar" width="28" height="28" style="width:28px; height:28px; border-radius:2px; object-fit:contain; background:#ffffff;" />
          <span>jqackkk</span>
          <span class="mif-arrow-drop-down" style="font-size: 14px;"></span>
          <div class="user-dropdown">
            <div class="user-dropdown-header">citizen: sg-2026-f1e8</div>
            <a href="/id.html"><span class="mif-profile"></span> sangaia id card</a>
            <a href="/citizenship.html"><span class="mif-checkmark"></span> citizenship status</a>
            <a href="/index.html#units"><span class="mif-compass"></span> units &amp; measures</a>
            <a href="/dashboard.html"><span class="mif-chart-bars"></span> sovereign registry</a>
            <div style="border-top:1px solid #e1dfdd; margin:4px 0;"></div>
            <a href="/index.html"><span class="mif-home"></span> federal home</a>
          </div>
        </div>
      </div>
    </div>
    <div class="hero-content">
      <h1>{hero_title}</h1>
      <p>{hero_sub}</p>
    </div>
  </header>

  <!-- Navigation Bar -->
  <nav class="subnav">
{subnav_html}  </nav>

  <!-- Content Grid -->
  <main class="main-wrapper">
    <!-- Left Column: Primary Content -->
    <div class="left-col">
{main_content_html}
    </div>

    <!-- Right Column: Official Sidebar Widgets -->
    <aside class="sidebar">
{sidebar_nav_html}
{sidebar_info_html}
{sidebar_right_extra_html}
    </aside>
  </main>

{modal_dialog_html}
{extra_scripts}
</body>
</html>
"""
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else ".", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(page_html)

if __name__ == "__main__":
    print("generate_all_sites module updated without social widgets.")
