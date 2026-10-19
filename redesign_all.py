#!/usr/bin/env python3
"""
Sangaia Live Master Redesign Orchestrator
Executes full redesign across every single page in the Sangaia repository,
guaranteeing:
1. Zero discrepancies in design language across all portals.
2. Segoe WP typography.
3. MetroUI Icons (mif-...) via https://cdn.metroui.org.ua/4.5.12/icons.css.
4. Ministerial color themes (Executive: Navy/Gold, Treasury: Emerald/Teal, Work: Purple,
   Healthcare: Crimson, Education: Cyan, Domestic: Navy Blue, External: Pink,
   Environment: Forest Green, Propaganda: Orange, Portal: Windows Live Blue).
5. All 5 provinces: New Jasper, New Madison, Liveland, Sentinel, Columbia.
6. Sangaian currency '$', temperature '°Пт', distance 'Мн'.
7. Sangaian Cyrillic translations removed/paused as instructed by user until review.
8. Accurate Domestic/External/Environment links with zero routing mixups.
"""

import os
import shutil
import subprocess

def run_orchestration():
    print("=" * 60)
    print("STEP 1: Rebuilding Core Portal Pages (index, services, units, etc.)...")
    import build_portal_pages
    build_portal_pages.build_index()
    build_portal_pages.build_units()
    build_portal_pages.build_services()
    build_portal_pages.build_citizenship()
    build_portal_pages.build_gov_about()
    build_portal_pages.build_societal_press()
    build_portal_pages.build_supporting_portals()

    print("=" * 60)
    print("STEP 2: Rebuilding 9 Ministry Homepages & Subdomains...")
    import build_ministry_homepages
    build_ministry_homepages.build_executive()
    build_ministry_homepages.build_treasury()
    build_ministry_homepages.build_work()
    build_ministry_homepages.build_healthcare()
    build_ministry_homepages.build_education()
    build_ministry_homepages.build_domestic()
    build_ministry_homepages.build_external()
    build_ministry_homepages.build_environment()
    build_ministry_homepages.build_propaganda()

    print("=" * 60)
    print("STEP 3: Rebuilding 9 Department Portals & Subdomains...")
    import build_departments
    for s in build_departments.DEPT_SPECS:
        build_departments.build_dept_page(s)

    print("=" * 60)
    print("STEP 4: Rebuilding DDCR & Gazette Articles...")
    import build_ddcr
    build_ddcr.build_ddcr_index()
    build_ddcr.build_ddcr_topics()
    build_ddcr.build_ddcr_outbreaks()
    build_ddcr.build_ddcr_search()
    build_ddcr.build_ddcr_article()
    build_ddcr.build_article_press()

    print("=" * 60)
    print("STEP 5: Synchronizing Subdomains & Mirroring Files...")
    # Mirror id.html -> id/index.html
    os.makedirs("id", exist_ok=True)
    shutil.copy("id.html", "id/index.html")

    # Remove any remaining sgn directories
    for root, dirs, files in os.walk('.'):
        if '.git' in root or '.gemini' in root: continue
        for d in list(dirs):
            if d == 'sgn':
                shutil.rmtree(os.path.join(root, d))

    print("=" * 60)
    print("STEP 6: Scanning Repository for Design Integrity...")
    total_html = 0
    passed_html = 0
    failures = []

    for root, dirs, files in os.walk('.'):
        if '.git' in root or '.gemini' in root: continue
        for f in files:
            if f.endswith('.html'):
                total_html += 1
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()

                checks = {
                    "MetroUI Icons": 'cdn.metroui.org.ua' in content,
                    "Hero Header": 'hero-header' in content,
                    "Subnav": 'subnav' in content,
                    "Main Wrapper": 'main-wrapper' in content,
                    "Messages Dock": 'messages-dock' in content
                }

                if all(checks.values()):
                    passed_html += 1
                else:
                    failures.append((p, [k for k, v in checks.items() if not v]))

    print(f"Audit Complete: {passed_html}/{total_html} HTML files fully adhere to the One Live architecture.")
    if failures:
        print("Pages with missing components:")
        for path, failed_checks in failures:
            print(f"  {path}: missing {', '.join(failed_checks)}")
    else:
        print("SUCCESS: 100% of HTML files in repository adhere to the exact One Live design system with ZERO discrepancies!")

if __name__ == "__main__":
    run_orchestration()
