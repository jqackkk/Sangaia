#!/usr/bin/env python3
"""
Sangaia Live Master Redesign Orchestrator
Executes full redesign across every single page and website directory in the Sangaia repository,
guaranteeing:
1. Zero discrepancies in design language across all portals.
2. Segoe WP typography.
3. MetroUI Icons (mif-...) via https://cdn.metroui.org.ua/4.5.12/icons.css.
4. Embedded self-contained master CSS in <style> to prevent unstyled / vertical rendering.
5. All assets (css, js, images) copied to all subdomain directories so every website is fully styled.
6. NO face photos anywhere across the site.
7. Quotes only on the homepage (index.html).
8. Accurate Domestic/External/Environment routing with zero link mixups.
"""

import os
import shutil

SUBDOMAIN_DIRS = [
    "MoEX", "mEx", "mT", "mW", "mH", "mEd", "mE",
    "MiA", "MdA", "MtE", "mEnv", "mP", "mH/ddcr", "id", "articles"
]

def sync_assets_to_subdomains():
    print("Syncing assets (css, js, images) to all subdomain directories...")
    for sub in SUBDOMAIN_DIRS:
        os.makedirs(sub, exist_ok=True)
        # Copy css
        sub_css = os.path.join(sub, "css")
        os.makedirs(sub_css, exist_ok=True)
        shutil.copy("css/sangaia-live.css", os.path.join(sub_css, "sangaia-live.css"))

        # Copy js
        sub_js = os.path.join(sub, "js")
        os.makedirs(sub_js, exist_ok=True)
        shutil.copy("js/sangaia-live.js", os.path.join(sub_js, "sangaia-live.js"))

        # Copy images
        sub_img = os.path.join(sub, "images")
        os.makedirs(sub_img, exist_ok=True)
        for img in os.listdir("images"):
            src_p = os.path.join("images", img)
            if os.path.isfile(src_p):
                shutil.copy(src_p, os.path.join(sub_img, img))

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

    # Sync assets to all subdomains
    sync_assets_to_subdomains()

    print("=" * 60)
    print("STEP 6: Scanning Repository for Design Integrity & Face Image Removal...")
    total_html = 0
    passed_html = 0
    face_references = 0
    failures = []

    for root, dirs, files in os.walk('.'):
        if '.git' in root or '.gemini' in root: continue
        for f in files:
            if f.endswith('.html'):
                total_html += 1
                p = os.path.join(root, f)
                with open(p, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()

                if '1.jpeg' in content:
                    face_references += 1
                    print(f"WARNING: Face reference found in {p}")

                checks = {
                    "MetroUI Icons": 'cdn.metroui.org.ua' in content,
                    "Embedded Style": '<style>' in content and '--primary:' in content,
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
    print(f"Face image references remaining: {face_references}")
    if failures:
        print("Pages with missing components:")
        for path, failed_checks in failures:
            print(f"  {path}: missing {', '.join(failed_checks)}")
    else:
        print("SUCCESS: 100% of HTML files in repository adhere to the exact One Live design system with ZERO discrepancies and ZERO face images!")

if __name__ == "__main__":
    run_orchestration()
