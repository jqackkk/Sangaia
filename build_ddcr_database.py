#!/usr/bin/env python3
"""
build_ddcr_database.py
Processes downloaded PubMed & PMC CSV databases and compiles comprehensive,
authoritative disease articles and scientific literature indices for the Sangaia
Ministry of Healthcare DDCR portal and Supabase database.
"""

import csv
import json
import os
import re

DOWNLOADS = '/Users/jackdavenport/Downloads'
COVID_CSV = os.path.join(DOWNLOADS, 'csv-COVID-19.csv')
MPOX_CSV = os.path.join(DOWNLOADS, 'csv-Monkeypo.csv')
JOURNALS_CSV = os.path.join(DOWNLOADS, 'results.csv')

def load_papers(csv_path, keywords_map, max_per_cat=10):
    categorized = {k: [] for k in keywords_map}
    seen_pmids = set()
    
    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f)
        for r in reader:
            pmid = r.get('PMID', '').strip()
            pmcid = r.get('PMCID', '').strip()
            title = r.get('Title', '').strip().strip('[]')
            authors = r.get('Authors', '').strip()
            journal = r.get('Journal/Book', '').strip()
            year = r.get('Publication Year', '').strip()
            doi = r.get('DOI', '').strip()
            
            if not (pmid and title and journal) or pmid in seen_pmids:
                continue
                
            entry = {
                'pmid': pmid,
                'pmcid': pmcid,
                'title': title,
                'authors': authors,
                'journal': journal,
                'year': year,
                'doi': doi,
                'url': f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/" if pmcid else f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            }
            
            t_low = title.lower()
            for cat, kw_list in keywords_map.items():
                if len(categorized[cat]) < max_per_cat and any(k.lower() in t_low for k in kw_list):
                    categorized[cat].append(entry)
                    seen_pmids.add(pmid)
                    break
                    
    return categorized

def load_journals(csv_path, max_journals=150):
    journals = []
    seen = set()
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for r in reader:
            title = r.get('Journal Title', '').strip()
            if not title or title in seen:
                continue
            t_low = title.lower()
            # Prioritize high impact medical & public health journals
            if any(w in t_low for w in ['health', 'medic', 'infect', 'diseas', 'virol', 'immun', 'cardio', 'diabet', 'respir', 'psych', 'neuro', 'epidemiol', 'biolog', 'pediatr']):
                journals.append({
                    'title': title,
                    'nlm_abbr': r.get('NLM Title Abbreviation (TA)', '').strip(),
                    'publisher': r.get('Publisher', '').strip(),
                    'issn': r.get('ISSN (online)', '').strip() or r.get('ISSN (print)', '').strip(),
                    'pmc_url': r.get('PMC URL', '').strip()
                })
                seen.add(title)
                if len(journals) >= max_journals:
                    break
    return journals

print("Extracting COVID-19 papers...")
covid_kw = {
    'Transmission & Airborne Dynamics': ['transmission', 'aerosol', 'airborne', 'droplet', 'spread'],
    'Vaccines & Immunogenicity': ['vaccine', 'vaccination', 'mrna', 'immunogenicity', 'antibody response', 'booster'],
    'Therapeutics & Antivirals': ['remdesivir', 'paxlovid', 'treatment', 'antiviral', 'therapeutic', 'dexamethasone'],
    'Variants & Genomic Surveillance': ['variant', 'omicron', 'delta', 'mutation', 'genomic', 'lineage'],
    'Long COVID & Post-Acute Sequelae': ['long covid', 'post-acute', 'sequelae', 'persistent', 'post-covid', 'cognitive']
}
covid_papers_by_cat = load_papers(COVID_CSV, covid_kw, 10)

print("Extracting Mpox papers...")
mpox_kw = {
    'Epidemiology & Transmission': ['transmission', 'epidemiology', 'outbreak', 'spread', 'clade', 'sexual'],
    'Clinical Presentation & Pathology': ['clinical', 'manifestation', 'presentation', 'rash', 'lesion', 'cardiovascular'],
    'Vaccines & Antivirals': ['tecovirimat', 'tpoxx', 'vaccine', 'jynneos', 'acam2000', 'antiviral', 'prevention'],
    'Diagnostics & Surveillance': ['detection', 'pcr', 'diagnostic', 'laboratory', 'genomic', 'surveillance'],
    'Public Health & Global Response': ['public health', 'global', 'strategy', 'systematic review', 'guideline']
}
mpox_papers_by_cat = load_papers(MPOX_CSV, mpox_kw, 10)

print("Extracting PMC journals...")
journals_list = load_journals(JOURNALS_CSV, 150)

# Flatten COVID and Mpox papers
covid_papers = []
for cat, plist in covid_papers_by_cat.items():
    for p in plist:
        p_copy = dict(p)
        p_copy['research_category'] = cat
        covid_papers.append(p_copy)

mpox_papers = []
for cat, plist in mpox_papers_by_cat.items():
    for p in plist:
        p_copy = dict(p)
        p_copy['research_category'] = cat
        mpox_papers.append(p_copy)

print(f"Total COVID research studies: {len(covid_papers)}")
print(f"Total Mpox research studies: {len(mpox_papers)}")
print(f"Total PMC indexed journals: {len(journals_list)}")

# Save intermediate extracted literature for inspection
with open('mH/ddcr/data/literature_cache.json', 'w', encoding='utf-8') as f:
    json.dump({
        'covid_papers': covid_papers,
        'mpox_papers': mpox_papers,
        'journals': journals_list
    }, f, indent=2)

print("Literature cache successfully generated.")
