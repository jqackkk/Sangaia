#!/usr/bin/env python3
"""
Sangaia Departments Portal Generator
Generates responsive, Frutiger Aero / Skeuomorphic Department portals for all 9 Ministries
in both English and Sangaian Cyrillic, with 75 fully interactive functional modal tools.
"""

import os
import re
import json
from make_departments import MINISTRIES

BASE_DIR = "/Users/jackdavenport/Sangaia"

# UI Translations
UI_STRINGS = {
    "en": {
        "title_suffix": "United Provinces of Sangaia",
        "home": "Home",
        "departments": "Departments",
        "services": "All Ministries",
        "sangaia_id": "Sangaia ID",
        "lang_switch": "Сангаиан (SGN)",
        "hero_badge": "Official Federal Departments & Executive Agencies",
        "hero_sub": "Statutory directorates, operational branches, and public service delivery engines of sovereign Sangaia.",
        "search_placeholder": "Search departments, services, mandates, or tools...",
        "filter_all": "All Departments",
        "dept_badge": "Statutory Federal Department",
        "mandate_label": "Official Constitutional & Statutory Mandate",
        "functions_label": "Operational Functions & Interactive Citizen Portals",
        "close": "Close",
        "submit": "Submit Application",
        "cancel": "Cancel",
        "verified_badge": "CRYPTOGRAPHICALLY VERIFIED • SANGAIA SOVEREIGN LEDGER",
        "token_label": "Verification Docket ID",
        "timestamp_label": "Timestamp",
        "status_label": "Status",
        "active_status": "PROCESSED & RECORDED",
        "download_receipt": "Download Sovereign Receipt",
        "print_receipt": "Print Official Docket",
        "footer_text": "Official Portal of the United Provinces of Sangaia • Government Information Gateway • Zero-Debt Sovereign Republic",
        "footer_sub": "All rights reserved. Digital decrees and records cryptographically signed under the Aretocratic Seal."
    },
    "sgn": {
        "title_suffix": "Унито Провинциа эк Сангайа",
        "home": "Домо",
        "departments": "Дэпартамэнто",
        "services": "Холо Министро",
        "sangaia_id": "Сангайа ИД",
        "lang_switch": "ENGLISH (EN)",
        "hero_badge": "Официало Федерало Дэпартамэнто & Эксэкуто Агэнциа",
        "hero_sub": "Конституционало директорио, оперативо рамо, инкаи публико сэрвицо макино эк сувэрэно Сангайа.",
        "search_placeholder": "Скэро дэпартамэнто, сэрвицо, мандато, вэл инструмэнто...",
        "filter_all": "Холо Дэпартамэнто",
        "dept_badge": "Конституционало Федерало Дэпарто",
        "mandate_label": "Официало Конституционало & Статуторо Мандато",
        "functions_label": "Оперативо Функцио & Интерактиво Цивикано Портало",
        "close": "Клаудо",
        "submit": "Субмито Апликатио",
        "cancel": "Канцэло",
        "verified_badge": "КРИПТОГРАФИКО ВЭРИФИКАДО • САНГАЙА СУВЭРЭНО ЛЕДЖЕР",
        "token_label": "Вэрификатио Докэто ИД",
        "timestamp_label": "Тэмпоро-Нота",
        "status_label": "Статуто",
        "active_status": "ПРОЦЕСАДО & ЗАПИСАДО",
        "download_receipt": "Дэскарго Сувэрэно Рэцэпто",
        "print_receipt": "Импримо Официало Докэто",
        "footer_text": "Официало Портало эк Унито Провинциа эк Сангайа • Информатио Гаранто • Син-Дэбито Сувэрэно Рэпублика",
        "footer_sub": "Холо јуро рэзэрвадо. Дигитало дэкрито криптографико сигнадо суб Арэтократико Сигило."
    }
}

# Detailed Interactive Modal Configurations for all 75 functions
MODAL_CONFIGS = {
    # EXECUTIVE
    "gazette": {
        "type": "search",
        "icon": "📜",
        "title_en": "Executive Orders & Decrees Societal Press Archive",
        "title_sgn": "Эксэкуто Дэкрито & Ордо Официало Социетало Прэсс Архиво",
        "fields": [
            {"name": "query", "label_en": "Keyword / Decree Reference", "label_sgn": "Ключо-слово / Дэкрито Номэро", "type": "text", "placeholder_en": "e.g., zero-debt, biome, education, cabinet", "placeholder_sgn": "наприм., син-дэбито, биом, эдукатио"},
            {"name": "category", "label_en": "Jurisdiction Category", "label_sgn": "Јурисдиктио Катэгорио", "type": "select", "options": [
                {"val": "all", "en": "All Societal Press Classifications", "sgn": "Холо Социетало Прэсс Катэгорио"},
                {"val": "aretocratic", "en": "Aretocratic Proclamations (Veto / Constitutional)", "sgn": "Арэтократико Прокламатио"},
                {"val": "cabinet", "en": "Cabinet Directives & Ministerial Mandates", "sgn": "Кабино Дирэктиво"},
                {"val": "emergency", "en": "Sovereign Emergency Preparedness Orders", "sgn": "Сувэрэно Сургэнциа Ордо"}
            ]}
        ],
        "action_en": "Query Societal Press Archive",
        "action_sgn": "Скэро Социетало Прэсс Архиво",
        "sample_results_en": [
            {"ref": "DEC-2026-088", "date": "14 Oct 2026", "title": "Aretocratic Veto on Discretionary Deficit Instruments", "desc": "Reaffirming the constitutional ceiling of 0% sovereign fiscal debt across all ministerial ledgers."},
            {"ref": "DEC-2026-071", "date": "02 Oct 2026", "title": "Statutory Expansion of Biome Corridor Protection Zones", "desc": "Allocating 24,000 additional hectares of alpine rain-forest to protected state biome status."},
            {"ref": "DEC-2026-049", "date": "18 Sep 2026", "title": "Mandatory 85%+ Community Redistribution for Spiritual Constructs", "desc": "Enforcing civic wealth return audits on all registered religious institutions."}
        ],
        "sample_results_sgn": [
            {"ref": "DEC-2026-088", "date": "14 Окт 2026", "title": "Арэтократико Вэто супра Дэфицито Инструмэнто", "desc": "Рэ-афирмадо конституционало цэлинг эк 0% сувэрэно дэбито транз холо министро."},
            {"ref": "DEC-2026-071", "date": "02 Окт 2026", "title": "Статуторо Экспансио эк Биом Коридоро Зона", "desc": "Алокатио эк 24,000 гектаро алпино сильва ад протэктадо биом статуто."},
            {"ref": "DEC-2026-049", "date": "18 Сэп 2026", "title": "Облигаторо 85%+ Комунитиа Рэдивидо про Рэлигио", "desc": "Фортис цивикано рико рэдивидо аудито транз холо экклэсиа."}
        ]
    },
    "petition": {
        "type": "form",
        "icon": "📥",
        "title_en": "Citizen Petition & Grievance Pipeline",
        "title_sgn": "Цивикано Пэтитио & Грава Канало",
        "fields": [
            {"name": "citizen_id", "label_en": "Citizen Sangaia ID", "label_sgn": "Цивикано Сангайа ИД", "type": "text", "placeholder_en": "e.g., SNG-88942-A", "placeholder_sgn": "наприм., SNG-88942-A"},
            {"name": "province", "label_en": "Home Province", "label_sgn": "Провинциа", "type": "select", "options": [
                {"val": "new_jasper", "en": "New Jasper Province", "sgn": "Ново Јаспэр Провинциа"},
                {"val": "new_madison", "en": "New Madison Province", "sgn": "Ново Мадисон Провинциа"},
                {"val": "liveland", "en": "Liveland Province", "sgn": "Ливланд Провинциа"},
                {"val": "sentinel", "en": "Sentinel Province", "sgn": "Сэнтинэл Провинциа"},
                {"val": "columbia", "en": "Columbia Province", "sgn": "Колумбиа Провинциа"}
            ]},
            {"name": "subject", "label_en": "Petition Subject", "label_sgn": "Пэтитио Тэма", "type": "text", "placeholder_en": "Brief title of proposal or grievance", "placeholder_sgn": "Титуло эк пропоситио"},
            {"name": "details", "label_en": "Detailed Petition & Statutory Rationale", "label_sgn": "Дэталадо Пэтитио & Ратио", "type": "textarea", "placeholder_en": "State the constitutional, ethical, or communal justification for action...", "placeholder_sgn": "Скрибо конституционало ратио..."}
        ],
        "action_en": "Transmit Statutory Petition to Cabinet",
        "action_sgn": "Транзмито Пэтитио ад Кабино",
        "token_prefix": "SNG-PET"
    },
    "protocol": {
        "type": "form",
        "icon": "🎖️",
        "title_en": "Ceremonial Protocol & Dignitary Accreditation",
        "title_sgn": "Церемониало Протоколо & Дигнитаро Акрэдитатио",
        "fields": [
            {"name": "delegation", "label_en": "Sending Sovereign State or International Body", "label_sgn": "Сувэрэно Стато вэл Корпо", "type": "text", "placeholder_en": "e.g., Swiss Confederation, United Nations", "placeholder_sgn": "наприм., Конфэдэратио Хэльвэтика"},
            {"name": "envoy_name", "label_en": "Head of Delegation / Envoy Name", "label_sgn": "Номэ эк Дэлегатио Лидэро", "type": "text", "placeholder_en": "Full diplomatic name and credentials", "placeholder_sgn": "Дипломатико номэ"},
            {"name": "protocol_tier", "label_en": "Protocol Tier", "label_sgn": "Протоколо Градо", "type": "select", "options": [
                {"val": "tier1", "en": "Head of State / Monarch / President (Full Honor Guard)", "sgn": "Капо эк Стато (Плэно Оноро Гардо)"},
                {"val": "tier2", "en": "Prime Minister / Foreign Minister (Executive Reception)", "sgn": "Примо Министро / Дипломатико Капо"},
                {"val": "tier3", "en": "Ambassador Plenipotentiary (Letters of Credence)", "sgn": "Амбасадоро Плэнипотэнциаро"}
            ]}
        ],
        "action_en": "Issue Ceremonial Clearance Docket",
        "action_sgn": "Эмито Церемониало Докэто",
        "token_prefix": "SNG-PROT"
    },
    "kpi": {
        "type": "telemetry",
        "icon": "📈",
        "title_en": "National Progress Telemetry & Sovereign KPIs",
        "title_sgn": "Национало Прогрэсо Тэлэмэтриа & Сувэрэно КПИ",
        "metrics": [
            {"name_en": "GDP Growth Rate (Real)", "name_sgn": "ГДП Крэсцито (Реало)", "val": "+4.18%", "sub_en": "Zero inflationary distortion", "sub_sgn": "Син-инфлатио дистортио"},
            {"name_en": "Sovereign External Debt", "name_sgn": "Сувэрэно Экстэрнало Дэбито", "val": "$ 0.00", "sub_en": "Constitutional 0% debt ceiling met", "sub_sgn": "Конституционало 0% цэлинг"},
            {"name_en": "Universal Healthcare Coverage", "name_sgn": "Универсало Салуто Кувэрта", "val": "99.82%", "sub_en": "Zero citizen out-of-pocket medical debt", "sub_sgn": "0 цивикано мэдикало дэбито"},
            {"name_en": "Protected Biome Canopy Cover", "name_sgn": "Протэктадо Биом Сильва", "val": "88.64%", "sub_en": "Forest preservation & renewal index", "sub_sgn": "Сильва салво & рэнэвадо индэксо"}
        ],
        "action_en": "Refresh Live Telemetry Stream",
        "action_sgn": "Рэфрэско Тэлэмэтриа",
        "token_prefix": "SNG-KPI"
    },
    "whitepapers": {
        "type": "search",
        "icon": "📑",
        "title_en": "Public Policy Whitepapers & Strategic Research",
        "title_sgn": "Публико Политико Бланко-Либро & Стратэгико Сциэнциа",
        "fields": [
            {"name": "query", "label_en": "Search Whitepapers & Empirical Briefs", "label_sgn": "Скэро Бланко-Либро & Сциэнциа", "type": "text", "placeholder_en": "e.g., zero-debt, eco-housing, public transit", "placeholder_sgn": "наприм., син-дэбито, эко-домо, транзито"}
        ],
        "action_en": "Filter Whitepapers",
        "action_sgn": "Фильтро Бланко-Либро",
        "sample_results_en": [
            {"ref": "WP-2026-04", "date": "Aug 2026", "title": "Sovereign Liquidity Without Fiat Inflation: The Sangaian Model", "desc": "Analysis of asset-backed provincial exchange reserves and debt-free public infrastructure funding."},
            {"ref": "WP-2026-02", "date": "Jun 2026", "title": "Decentralized Provincial Energy Grids & Geothermal Transition", "desc": "Field telemetry on 100% renewable municipal grids in Western Highland communities."}
        ],
        "sample_results_sgn": [
            {"ref": "WP-2026-04", "date": "Авг 2026", "title": "Сувэрэно Ликвидито Син-Инфлатио: Сангайа Модэло", "desc": "Анализо эк акордо-гаранто провинциало рэзэрва инкаи син-дэбито инфраструкт."},
            {"ref": "WP-2026-02", "date": "Јун 2026", "title": "Дэцэнтрэ Провинциало Энэргиа & Гэотэрмало Транзитио", "desc": "Тэлэмэтриа эк 100% рэнэвадо муниципио гридо ин Алпино комунитиа."}
        ]
    },
    "taskforce": {
        "type": "form",
        "icon": "🤝",
        "title_en": "Cross-Agency Coordination Task Force Portal",
        "title_sgn": "Интер-Министро Координатио Таск-Форс Портало",
        "fields": [
            {"name": "officer_id", "label_en": "Ministerial Liaison Officer ID", "label_sgn": "Министро Лиаисон Офицэро ИД", "type": "text", "placeholder_en": "e.g., OFF-MOEX-771", "placeholder_sgn": "наприм., OFF-MOEX-771"},
            {"name": "taskforce_code", "label_en": "Active Task Force Unit", "label_sgn": "Активо Таск-Форс Унито", "type": "select", "options": [
                {"val": "tf_water", "en": "TF-101: Trans-Provincial Aquifer & Biome Watershed", "sgn": "ТФ-101: Транз-Провинциало Аквифэро & Биом"},
                {"val": "tf_rail", "en": "TF-104: High-Speed Magnetic Transit & Road Integration", "sgn": "ТФ-104: Магнэтико Транзито & Виа"},
                {"val": "tf_food", "en": "TF-109: National Grain Reserve & Regenerative Soil Security", "sgn": "ТФ-109: Национало Грано Рэзэрва & Агро"}
            ]}
        ],
        "action_en": "Access Task Force Workspace",
        "action_sgn": "Интро Таск-Форс Спацио",
        "token_prefix": "SNG-TASK"
    },

    # TREASURY
    "taxcalc": {
        "type": "calc",
        "icon": "🧮",
        "title_en": "Interactive Individual & Corporate Tax Calculator",
        "title_sgn": "Интерактиво Цивикано & Корпоративо Такса Калкулаторо",
        "fields": [
            {"name": "income", "label_en": "Annual Gross Income / Net Profit ($)", "label_sgn": "Ануало Гросо Инкомо ($)", "type": "number", "default": 48000},
            {"name": "bracket", "label_en": "Filing Classification", "label_sgn": "Такса Класификатио", "type": "select", "options": [
                {"val": "individual", "en": "Citizen Individual (Standard Sangaia Allowance)", "sgn": "Цивикано Индивидуало"},
                {"val": "artisan", "en": "Artisan Cooperative / Family Enterprise", "sgn": "Артизано Коопэративо / Фамилиа"},
                {"val": "corp", "en": "Corporate / Industrial Entity", "sgn": "Корпоративо / Индустриало"}
            ]}
        ],
        "action_en": "Compute Progressive Tax & Solidarity Offsets",
        "action_sgn": "Калкуло Такса & Солидарито",
        "token_prefix": "SNG-TAX"
    },
    "taxfile": {
        "type": "form",
        "icon": "📑",
        "title_en": "Digital Tax Filing & Clearance Verification",
        "title_sgn": "Дигитало Такса Филинг & Ликуидадо Вэрификатио",
        "fields": [
            {"name": "taxpayer_id", "label_en": "Taxpayer Sangaia ID / Enterprise TIN", "label_sgn": "Такса-пагаторо ИД / ТИН", "type": "text", "placeholder_en": "e.g., TAX-9941-SNG", "placeholder_sgn": "наприм., TAX-9941-SNG"},
            {"name": "fiscal_year", "label_en": "Taxation Year", "label_sgn": "Фискало Ано", "type": "select", "options": [
                {"val": "2026", "en": "FY 2026 (Current Statutory Filing)", "sgn": "ФА 2026 (Активо)"},
                {"val": "2025", "en": "FY 2025 (Annual Review / Adjustments)", "sgn": "ФА 2025 (Рэвизио)"}
            ]},
            {"name": "declaration", "label_en": "Cryptographic Ledger Checksum", "label_sgn": "Криптографико Лэджер Чэксум", "type": "text", "placeholder_en": "Auto-filled or manual ledger hash", "placeholder_sgn": "Лэджер хэш"}
        ],
        "action_en": "Submit Tax Return & Issue Clearance",
        "action_sgn": "Субмито Такса & Эмито Ликуидадо",
        "token_prefix": "SNG-CLR"
    },
    "taxappeal": {
        "type": "form",
        "icon": "⚖️",
        "title_en": "Electronic Tax Appeal & Dispute Resolution Submission",
        "title_sgn": "Элэктронико Такса Апэло & Диспуто Субмисио",
        "fields": [
            {"name": "assessment_no", "label_en": "Notice of Assessment #", "label_sgn": "Такса Нотициа Номэро", "type": "text", "placeholder_en": "e.g., ASM-2026-4412", "placeholder_sgn": "наприм., ASM-2026-4412"},
            {"name": "disputed_amount", "label_en": "Disputed Amount ($)", "label_sgn": "Диспутадо Сума ($)", "type": "number", "placeholder_en": "1200", "placeholder_sgn": "1200"},
            {"name": "appeal_reason", "label_en": "Statutory Ground for Appeal", "label_sgn": "Кауза эк Апэло", "type": "textarea", "placeholder_en": "Specify miscalculation, exemption eligibility, or cooperative credit...", "placeholder_sgn": "Скрибо кауза эк апэло..."}
        ],
        "action_en": "File Electronic Tax Appeal",
        "action_sgn": "Филинг Элэктронико Апэло",
        "token_prefix": "SNG-APL"
    },
    "debtscreen": {
        "type": "telemetry",
        "icon": "🛑",
        "title_en": "Live Sovereign Debt Tracker & Bond Yield Telemetry",
        "title_sgn": "Ливо Сувэрэно Дэбито Тракэро & Бондо Тэлэмэтриа",
        "metrics": [
            {"name_en": "Sovereign Debt Outstanding", "name_sgn": "Сувэрэно Дэбито Тотало", "val": "$ 0.00", "sub_en": "Debt Ceiling: $ 0.00 (Article III)", "sub_sgn": "Дэбито Цэлинг: $ 0.00 (Артикло III)"},
            {"name_en": "10-Year Citizen Development Bond", "name_sgn": "10-Ано Цивикано Дэвэлопо Бондо", "val": "3.24%", "sub_en": "100% asset-backed infrastructure coupon", "sub_sgn": "100% акордо-гаранто купон"},
            {"name_en": "Statutory Cash Reserve Ratio", "name_sgn": "Статуторо Каша Рэзэрва Ратио", "val": "148.5%", "sub_en": "Supreme liquidity surplus in treasury vaults", "sub_sgn": "Сувэрэно ликвидито сурплус"},
            {"name_en": "National Inflation Rate (CPI)", "name_sgn": "Национало Инфлатио Индэксо", "val": "0.12%", "sub_en": "Hard commodity-weighted price index", "sub_sgn": "Стабило праисо индэксо"}
        ],
        "action_en": "Verify Treasury Ledger Integrity",
        "action_sgn": "Вэрифико Трэзоро Лэджер",
        "token_prefix": "SNG-DEBT"
    },
    "bondhub": {
        "type": "form",
        "icon": "🏛️",
        "title_en": "Citizen Sovereign Bond Purchase & Redemption Hub",
        "title_sgn": "Цивикано Сувэрэно Бондо Компра & Рэдэмптио Хуб",
        "fields": [
            {"name": "investor_id", "label_en": "Citizen Sangaia ID", "label_sgn": "Цивикано Сангайа ИД", "type": "text", "placeholder_en": "e.g., SNG-55219-B", "placeholder_sgn": "наприм., SNG-55219-B"},
            {"name": "bond_series", "label_en": "Bond Series", "label_sgn": "Бондо Сэриа", "type": "select", "options": [
                {"val": "b_rail", "en": "Series IX: High-Speed Clean Rail Transit (3.24% Coupon, 5 Yr)", "sgn": "Сэриа IX: Алто-Спидо Транзито (3.24%, 5 Ан)"},
                {"val": "b_hydro", "en": "Series XII: Geothermal & Hydro Micro-Grids (3.40% Coupon, 10 Yr)", "sgn": "Сэриа XII: Гэотэрмало & Хидро (3.40%, 10 Ан)"},
                {"val": "b_agri", "en": "Series VII: Regenerative Silviculture & Agro-Forestry (3.10% Coupon, 3 Yr)", "sgn": "Сэриа VII: Сильва & Агро-Форест (3.10%, 3 Ан)"}
            ]},
            {"name": "amount", "label_en": "Subscription Amount ($)", "label_sgn": "Субскриптио Сума ($)", "type": "number", "placeholder_en": "5000", "placeholder_sgn": "5000"}
        ],
        "action_en": "Execute Sovereign Bond Subscription",
        "action_sgn": "Исполнито Бондо Субскриптио",
        "token_prefix": "SNG-BND"
    },
    "econbulletin": {
        "type": "search",
        "icon": "📊",
        "title_en": "Quarterly Economic Outlook & Sovereign Bulletins",
        "title_sgn": "Квартало Экономико Прогнозо & Сувэрэно Булэтино",
        "fields": [
            {"name": "quarter", "label_en": "Select Fiscal Quarter", "label_sgn": "Селекто Фискало Квартало", "type": "select", "options": [
                {"val": "2026_q3", "en": "Q3 2026: Inter-Provincial Trade & Currency Velocity", "sgn": "К3 2026: Интер-Провинциало Трэйд & Валута"},
                {"val": "2026_q2", "en": "Q2 2026: Agricultural Yields & Grain Stabilization", "sgn": "К2 2026: Агро Кроп & Грано Стабилита"},
                {"val": "2026_q1", "en": "Q1 2026: Annual Budget Review & Surplus Allocation", "sgn": "К1 2026: Ануало Бюджет & Сурплус"}
            ]}
        ],
        "action_en": "Open Statistical Bulletin",
        "action_sgn": "Апэри Статистико Булэтино",
        "token_prefix": "SNG-BUL"
    },
    "tenders": {
        "type": "search",
        "icon": "📑",
        "title_en": "Open Sovereign Government Procurement Listings",
        "title_sgn": "Апэрто Публико Трэзоро Тэндэры & Прокурэмэнт",
        "fields": [
            {"name": "sector", "label_en": "Procurement Sector", "label_sgn": "Прокурэмэнт Сэкторо", "type": "select", "options": [
                {"val": "all", "en": "All Open Sovereign Tenders", "sgn": "Холо Апэрто Тэндэры"},
                {"val": "transit", "en": "Highways, Bridges & Transit Materials", "sgn": "Виа, Понто & Транзито"},
                {"val": "health", "en": "Pharmaceuticals & Clinical Machinery", "sgn": "Фармациа & Клинико Макино"},
                {"val": "infra", "en": "Classroom Construction & Clean Tech", "sgn": "Эдукатио Конструкто & Тэк"}
            ]}
        ],
        "action_en": "Query Open Government Tenders",
        "action_sgn": "Скэро Апэрто Тэндэры",
        "sample_results_en": [
            {"ref": "TND-2026-902", "date": "Closes 30 Nov 2026", "title": "Magnetic Levitation Rail Bridge Over Azure Fjord", "desc": "Statutory ceiling: $ 14,200,000. Open to domestic worker cooperatives and qualified engineering consortiums."},
            {"ref": "TND-2026-884", "date": "Closes 15 Nov 2026", "title": "50,000 Next-Gen High-Efficiency Solar Roof Assemblies", "desc": "Statutory ceiling: $ 6,800,000. Priority given to regional provincial fabricators."}
        ],
        "sample_results_sgn": [
            {"ref": "TND-2026-902", "date": "Клаудо 30 Нов 2026", "title": "Магнэтико Транзито Понто супра Азуро Фиордо", "desc": "Статуторо цэлинг: $ 14,200,000. Апэрто про домистико коопэративо."},
            {"ref": "TND-2026-884", "date": "Клаудо 15 Нов 2026", "title": "50,000 Соларо Тэкто Матэриало про Школа", "desc": "Статуторо цэлинг: $ 6,800,000. Приоритето про провинциало фабрика."}
        ]
    },
    "auditledger": {
        "type": "search",
        "icon": "🔍",
        "title_en": "Ministry Expenditure Audit Reports & Public Ledger",
        "title_sgn": "Министро Дапано Аудито Рэпорто & Публико Лэджер",
        "fields": [
            {"name": "ministry", "label_en": "Select Ministry to Audit", "label_sgn": "Селекто Министро про Аудито", "type": "select", "options": [
                {"val": "all", "en": "Consolidated All-Ministries Audit Ledger", "sgn": "Консолидадо Холо Министро"},
                {"val": "executive", "en": "Ministry of the Executive (Zero-Waste: 99.8%)", "sgn": "Министро эк Эксэкуто (99.8%)"},
                {"val": "treasury", "en": "Ministry of the Treasury (Zero-Waste: 100%)", "sgn": "Министро эк Трэзоро (100%)"},
                {"val": "healthcare", "en": "Ministry of Healthcare (Zero-Waste: 99.4%)", "sgn": "Министро эк Салуто (99.4%)"},
                {"val": "education", "en": "Ministry of Education (Zero-Waste: 99.7%)", "sgn": "Министро эк Эдукатио (99.7%)"}
            ]}
        ],
        "action_en": "Generate Transparent Audit Extract",
        "action_sgn": "Гэнэрато Транспарэнто Аудито",
        "token_prefix": "SNG-AUD"
    },
    "budgetreq": {
        "type": "form",
        "icon": "📋",
        "title_en": "Administrative Budget Request & Tracking Portal",
        "title_sgn": "Административо Бюджет Пэтитио & Тракэро",
        "fields": [
            {"name": "req_agency", "label_en": "Department / Municipal Agency Name", "label_sgn": "Дэпарто / Муниципио Номэ", "type": "text", "placeholder_en": "e.g., Highland Alpine Highway Maintenance Unit", "placeholder_sgn": "наприм., Алпино Виа Унито"},
            {"name": "allocation_type", "label_en": "Statutory Appropriation Tier", "label_sgn": "Апроприатио Градо", "type": "select", "options": [
                {"val": "capital", "en": "Capital Infrastructure (Zero-debt funded)", "sgn": "Капитало Инфраструкт"},
                {"val": "operational", "en": "Operational & Essential Equipment", "sgn": "Оперативо & Эккипаж"},
                {"val": "research", "en": "Scientific & Ecological Conservation Grant", "sgn": "Сциэнциа & Биом Гранто"}
            ]},
            {"name": "amount", "label_en": "Requested Allocation ($)", "label_sgn": "Пэтито Сума ($)", "type": "number", "placeholder_en": "240000", "placeholder_sgn": "240000"}
        ],
        "action_en": "Submit Statutory Budget Request",
        "action_sgn": "Субмито Бюджет Пэтитио",
        "token_prefix": "SNG-BDG"
    },

    # WORK
    "whistleblower": {
        "type": "form",
        "icon": "🛡️",
        "title_en": "Anonymous Whistleblower & Labor Violation Report",
        "title_sgn": "Анонимо Виолатио Рэпорто & Лаборо Салво",
        "fields": [
            {"name": "employer", "label_en": "Employer / Company / Cooperative Name", "label_sgn": "Эмплойэро / Фирма / Коопэративо Номэ", "type": "text", "placeholder_en": "Name of enterprise or workplace facility", "placeholder_sgn": "Номэ эк компаниа"},
            {"name": "violation_type", "label_en": "Violation Category", "label_sgn": "Виолатио Катэгорио", "type": "select", "options": [
                {"val": "wage", "en": "Unpaid Overtime / Sub-Minimum Wage Underpayment", "sgn": "Нон-пагато Овэртаим / Саларио Фалу"},
                {"val": "safety", "en": "Dangerous Unchecked Working Conditions (OSHA-S)", "sgn": "Пэрикуло Салуто & Салво Кондицио"},
                {"val": "union", "en": "Union Suppression / Retaliation Against Organizing", "sgn": "Унион Супрэсио / Рэванш Контра Лаборо"},
                {"val": "hours", "en": "Violation of 36-Hour Statutory Workweek Cap", "sgn": "Виолатио эк 36-Хора Сепмана Цэлинг"}
            ]},
            {"name": "details", "label_en": "Factual Details (Strictly Encrypted)", "label_sgn": "Факуло Дэтало (Криптографико Салво)", "type": "textarea", "placeholder_en": "Describe locations, shift dates, and evidence without disclosing your identity...", "placeholder_sgn": "Дэтало син-дэкларо персоно..."}
        ],
        "action_en": "Transmit Encrypted Whistleblower Docket",
        "action_sgn": "Транзмито Крипто-Рэпорто",
        "token_prefix": "SNG-WBL"
    },
    "standards": {
        "type": "search",
        "icon": "📚",
        "title_en": "Workplace Standard Guidelines (OSHA-S)",
        "title_sgn": "Лаборо Салво Стандарто Руло (OSHA-S)",
        "fields": [
            {"name": "industry", "label_en": "Select Industry Safety Code", "label_sgn": "Селекто Индустриа Кодо", "type": "select", "options": [
                {"val": "heavy", "en": "Heavy Manufacturing & High-Voltage Systems", "sgn": "Грави Индустриа & Алто-Волтаж"},
                {"val": "agri", "en": "Agro-Forestry & Organic Harvesting Equipment", "sgn": "Агро-Форест & Макино"},
                {"val": "office", "en": "Civic Offices, Ergonomics & Air Purity", "sgn": "Официо, Эргономико & Аэро"},
                {"val": "bio", "en": "Alpine Science Labs & Biological Containment", "sgn": "Алпино Лабораторио & Био"}
            ]}
        ],
        "action_en": "Download Official Standard Manual",
        "action_sgn": "Дэскарго Стандарто Мануало",
        "token_prefix": "SNG-STD"
    },
    "mediation": {
        "type": "form",
        "icon": "⚖️",
        "title_en": "Union Registry & Online Mediation Booking",
        "title_sgn": "Лаборо Унион Рэгистро & Медиатио Скэдуло",
        "fields": [
            {"name": "union_name", "label_en": "Labor Union / Worker Council Name", "label_sgn": "Лаборо Унион / Консилио Номэ", "type": "text", "placeholder_en": "e.g., Sangaian Railway Workers Brotherhood", "placeholder_sgn": "наприм., Сангайа Транзито Унион"},
            {"name": "counterpart", "label_en": "Enterprise / Management Counterpart", "label_sgn": "Эмплойэро / Манаджмэнт", "type": "text", "placeholder_en": "Enterprise name", "placeholder_sgn": "Компаниа номэ"},
            {"name": "hearing_date", "label_en": "Preferred Mediation Hearing Date", "label_sgn": "Дэсидо Дата про Аудитио", "type": "date"}
        ],
        "action_en": "Schedule State Mediation Hearing",
        "action_sgn": "Скэдуло Медиатио Аудитио",
        "token_prefix": "SNG-MED"
    },
    "jobs": {
        "type": "search",
        "icon": "💼",
        "title_en": "National Public Job Board & Cooperative Placement",
        "title_sgn": "Национало Лаборо Бордо & Коопэративо Эмплоймэнт",
        "fields": [
            {"name": "skill", "label_en": "Vocation / Skill Area", "label_sgn": "Профэсио / Скил Спацио", "type": "text", "placeholder_en": "e.g., railway, agronomist, nurse, forestry", "placeholder_sgn": "наприм., транзито, агроном, инфирмаро"},
            {"name": "province", "label_en": "Preferred Province", "label_sgn": "Провинциа", "type": "select", "options": [
                {"val": "all", "en": "All 5 Provinces (Relocation Allowance Available)", "sgn": "Холо 5 Провинциа"},
                {"val": "new_jasper", "en": "New Jasper (Shesk Central)", "sgn": "Ново Јаспэр (Шэск)"},
                {"val": "new_madison", "en": "New Madison (Madison City)", "sgn": "Ново Мадисон (Мадисон)"},
                {"val": "liveland", "en": "Liveland (Oaks Agricultural Hub)", "sgn": "Ливланд (Оакс)"},
                {"val": "sentinel", "en": "Sentinel (Alpine Ecological Reserve)", "sgn": "Сэнтинэл (Алпино)"},
                {"val": "columbia", "en": "Columbia (Maritime Harbor)", "sgn": "Колумбиа (Харбор)"}
            ]}
        ],
        "action_en": "Search Public Openings",
        "action_sgn": "Скэро Лаборо Вакансиа",
        "sample_results_en": [
            {"ref": "JOB-2026-118", "date": "Pay: $ 4,800/mo", "title": "Senior High-Speed Rail Systems Technician", "desc": "Capitol Central Depot. Statutory pension, comprehensive family healthcare, and housing allowance included."},
            {"ref": "JOB-2026-094", "date": "Pay: $ 4,200/mo", "title": "Regenerative Forest Ranger & Alpine Warden", "desc": "Northern High Ridge Reserve. Autonomous lodge accommodation, research stipend, and winter gear provided."}
        ],
        "sample_results_sgn": [
            {"ref": "JOB-2026-118", "date": "Пага: $ 4,800/м", "title": "Сэниор Магнэтико Транзито Тэкнико", "desc": "Капитоло Дэпо. Статуторо пэнсио, 100% салуто кувэрта, инкаи хабитатио."},
            {"ref": "JOB-2026-094", "date": "Пага: $ 4,200/м", "title": "Биом Вардэно & Алпино Сильва Офицэро", "desc": "Нордо Алпино Рэзэрва. Локало хабитатио, сциэнциа стипэнд, инкаи эккипаж."}
        ]
    },
    "unemployment": {
        "type": "calc",
        "icon": "🪙",
        "title_en": "Unemployment Benefit & Transitional Security Calculator",
        "title_sgn": "Транзитио Секурита & Бэнэфито Калкулаторо",
        "fields": [
            {"name": "last_wage", "label_en": "Previous Monthly Base Pay ($)", "label_sgn": "Превио Менсио Пага ($)", "type": "number", "default": 3600},
            {"name": "dependents", "label_en": "Number of Dependents in Household", "label_sgn": "Нумеро эк Фамилиа Депендэнти", "type": "number", "default": 1}
        ],
        "action_en": "Calculate Guaranteed Transitional Stipend",
        "action_sgn": "Калкуло Гарантадо Стипэнд",
        "token_prefix": "SNG-UNEMP"
    },
    "retraining": {
        "type": "form",
        "icon": "🎓",
        "title_en": "Subsidized Vocational Retraining Enrollment Hub",
        "title_sgn": "Субсидиадо Профэсио Рэтрэининг Инскриптио",
        "fields": [
            {"name": "candidate_id", "label_en": "Citizen Sangaia ID", "label_sgn": "Цивикано Сангайа ИД", "type": "text", "placeholder_en": "e.g., SNG-44102-W", "placeholder_sgn": "наприм., SNG-44102-W"},
            {"name": "track", "label_en": "Vocational Specialization Track", "label_sgn": "Профэсио Тракто", "type": "select", "options": [
                {"val": "hydrogen", "en": "Green Hydrogen & Geothermal Power Engineering", "sgn": "Виридо Хидрогэн & Гэотэрмало Тэк"},
                {"val": "transit", "en": "Automated Rail & Clean Highway Logistics", "sgn": "Аввтоматико Транзито & Логистико"},
                {"val": "agro", "en": "Agro-Ecological Robotics & Hydroponic Management", "sgn": "Агро-Экологико Роботикс & Хидропоник"}
            ]}
        ],
        "action_en": "Enroll in Fully-Funded Retraining Academy",
        "action_sgn": "Инскриптио ин Академиа",
        "token_prefix": "SNG-TRAIN"
    },
    "visacheck": {
        "type": "calc",
        "icon": "🛂",
        "title_en": "International Work Visa Eligibility Evaluator",
        "title_sgn": "Интернационало Лаборо Виса Калкулаторо",
        "fields": [
            {"name": "origin_nation", "label_en": "Country of Citizenship", "label_sgn": "Патриа эк Цивикана", "type": "text", "placeholder_en": "e.g., United Kingdom, Canada, France", "placeholder_sgn": "наприм., Франциа, Канада"},
            {"name": "profession", "label_en": "Skill Classification", "label_sgn": "Профэсио Класификатио", "type": "select", "options": [
                {"val": "medical", "en": "Healthcare / Physician / Specialist Nurse", "sgn": "Салуто / Мэдико / Инфирмаро"},
                {"val": "tech", "en": "Renewable Energy / Civil Engineering", "sgn": "Рэнэвадо Энэргиа / Тэк"},
                {"val": "education", "en": "University Professor / Research Scientist", "sgn": "Унивэрсито Профэсоро / Сциэнциа"}
            ]},
            {"name": "exp_years", "label_en": "Years of Verified Professional Experience", "label_sgn": "Ано эк Вэрификадо Экспэриэнциа", "type": "number", "default": 5}
        ],
        "action_en": "Evaluate Visa Point Tier",
        "action_sgn": "Эвалуато Виса Градо",
        "token_prefix": "SNG-VSA"
    },
    "credentials": {
        "type": "form",
        "icon": "📜",
        "title_en": "Foreign Professional Credential Verification",
        "title_sgn": "Экстэрнало Профэсио Дипломо Вэрификатио",
        "fields": [
            {"name": "inst_name", "label_en": "Foreign Degree-Granting University / Board", "label_sgn": "Экстэрнало Унивэрсито / Академиа", "type": "text", "placeholder_en": "e.g., Sorbonne, Oxford, ETH Zurich", "placeholder_sgn": "наприм., Сорбонэ, Оксфорд"},
            {"name": "diploma_id", "label_en": "Diploma / License Identifier", "label_sgn": "Дипломо / Лицэнсиа Кодо", "type": "text", "placeholder_en": "License registration number", "placeholder_sgn": "Лицэнсиа номэро"}
        ],
        "action_en": "Issue Sangaian Equivalency Docket",
        "action_sgn": "Эмито Эквивалэнтиа Докэто",
        "token_prefix": "SNG-EQUIV"
    },
    "hotlines": {
        "type": "telemetry",
        "icon": "📞",
        "title_en": "Multilingual Foreign Worker Protection & Legal Hotline",
        "title_sgn": "Мултилингво Экстэрнало Лаборо Хэлплине & Јуридо",
        "metrics": [
            {"name_en": "24/7 Toll-Free Hotline", "name_sgn": "24/7 Либэро Хэлплине", "val": "0800-SANGAIA", "sub_en": "Dial 1 for English, 2 for Spanish, 3 for French", "sub_sgn": "Аудио лингва селекто"},
            {"name_en": "Average Dispatch Wait", "name_sgn": "Мэдиа Еспаро Тэмпоро", "val": "14 Seconds", "sub_en": "Immediate connection to licensed labor attorneys", "sub_sgn": "Конэксо ад адвокато"},
            {"name_en": "Free Legal Representation", "name_sgn": "Либэро Јуридо Салво", "val": "100% State Paid", "sub_en": "Statutory legal aid under Article VII", "sub_sgn": "100% Стато дапано"}
        ],
        "action_en": "Connect to Live Secure Web Chat",
        "action_sgn": "Конэкто ад Ливо Салво Чат",
        "token_prefix": "SNG-HL"
    },

    # HEALTHCARE
    "healthcard": {
        "type": "form",
        "icon": "💳",
        "title_en": "Digital Sovereign Health Card Management",
        "title_sgn": "Дигитало Сувэрэно Салуто Карта Мануго",
        "fields": [
            {"name": "citizen_id", "label_en": "Citizen Sangaia ID", "label_sgn": "Цивикано Сангайа ИД", "type": "text", "placeholder_en": "e.g., SNG-12948-H", "placeholder_sgn": "наприм., SNG-12948-H"},
            {"name": "dob", "label_en": "Date of Birth", "label_sgn": "Дата эк Насито", "type": "date"}
        ],
        "action_en": "Render Digital Holographic Health Card",
        "action_sgn": "Гэнэрато Дигитало Салуто Карта",
        "token_prefix": "SNG-MED"
    },
    "provider": {
        "type": "search",
        "icon": "🏥",
        "title_en": "Primary Care Provider Directory Lookup",
        "title_sgn": "Примаро Салуто Клинико & Мэдико Дирэкторио",
        "fields": [
            {"name": "province", "label_en": "Province / District", "label_sgn": "Провинциа / Дистрикто", "type": "select", "options": [
                {"val": "all", "en": "All 5 Provincial Hospitals & Polyclinics", "sgn": "Холо 5 Провинциало Клиника"},
                {"val": "new_jasper", "en": "Watson Healthcare / New Jasper Hospital (Shesk)", "sgn": "Ново Јаспэр Хоспитало (Шэск)"},
                {"val": "new_madison", "en": "New Madison Hospital (Madison City)", "sgn": "Ново Мадисон Хоспитало (Мадисон)"},
                {"val": "liveland", "en": "Suwannee Emergency Hospital (Oaks, Liveland)", "sgn": "Суванни ЕР Хоспитало (Оакс, Ливланд)"},
                {"val": "sentinel", "en": "Sentinel Regional Trauma Center", "sgn": "Сэнтинэл Рэгионало Травма"},
                {"val": "columbia", "en": "Columbia Maritime Regional Medical Center", "sgn": "Колумбиа Маритимо Генерало"}
            ]}
        ],
        "action_en": "Search Available Doctors & Clinics",
        "action_sgn": "Скэро Мэдико & Клиника",
        "sample_results_en": [
            {"ref": "MED-CL-01", "date": "Open 24/7", "title": "St. Aelred Metropolitan Medical Polyclinic", "desc": "Accepting new patients. On-site imaging, trauma triage, pediatric wing, and sovereign dental pavilion."},
            {"ref": "MED-CL-04", "date": "Open 07:00 - 22:00", "title": "Azure Maritime Community Health Haven", "desc": "Accepting new patients. Family medicine, aquatic rehabilitation, cardiovascular care, 100% state covered."}
        ],
        "sample_results_sgn": [
            {"ref": "MED-CL-01", "date": "Апэрто 24/7", "title": "Санто Аэльрэд Мэтрополитано Поликлиника", "desc": "Ацэпто ново патиэнто. Мэдикало имагинг, пэдиятро, инкаи солит дэнтало спацио."},
            {"ref": "MED-CL-04", "date": "07:00 - 22:00", "title": "Азуро Маритимо Комунитиа Салуто Клиника", "desc": "Ацэпто ново патиэнто. Фамилиа мэдицина, кардиоваскуларо, 100% стато кувэрта."}
        ]
    },
    "formulary": {
        "type": "search",
        "icon": "💊",
        "title_en": "Prescription Benefit & Sovereign Formulary Tracker",
        "title_sgn": "Рэцэпто Мэдицина & Сувэрэно Формуларио",
        "fields": [
            {"name": "med_name", "label_en": "Generic or Brand Drug Name", "label_sgn": "Мэдицина Номэ (Гэнэрико вэл Брандо)", "type": "text", "placeholder_en": "e.g., Insulin, Amoxicillin, Metformin, Salbutamol", "placeholder_sgn": "наприм., Инсулин, Амоксицилин, Салбутамол"}
        ],
        "action_en": "Lookup Coverage",
        "action_sgn": "Инспэкто Кувэрта",
        "sample_results_en": [
            {"ref": "Rx-901", "date": "100% Subsidized", "title": "Human Biosimilar Insulin (All Formats)", "desc": "Classification: Essential Life-Support Therapeutic. 100% subsidized by federal sovereign healthcare fund."},
            {"ref": "Rx-412", "date": "Tier 1 Essential", "title": "Broad-Spectrum Antibiotics (Amoxicillin / Clavulanate)", "desc": "Classification: Tier 1 Essential Anti-Infective. Available at all licensed community pharmacies."}
        ],
        "sample_results_sgn": [
            {"ref": "Rx-901", "date": "100% Субсидиадо", "title": "Хумано Биосимиларо Инсулин (Холо Формато)", "desc": "Класификатио: Эсэнциало Салуто Тэрапи. 100% субсидиадо эк федерало фондо."},
            {"ref": "Rx-412", "date": "Градо 1 Эсэнциало", "title": "Антибиотико (Амоксицилин / Клавуланат)", "desc": "Класификатио: Градо 1 Эсэнциало Анти-Инфэктиво. Либэро ин холо фармациа."}
        ]
    },
    "ercapacity": {
        "type": "telemetry",
        "icon": "🚨",
        "title_en": "Live Hospital ER Capacity & Ambulance Telemetry",
        "title_sgn": "Ливо Хоспитало ЕР Капацито & Амбуланциа Тэлэмэтриа",
        "metrics": [
            {"name_en": "Capitol General Emergency Center", "name_sgn": "Капитоло Генерало ЕР", "val": "74% Occupancy", "sub_en": "Wait time: 6 min • 8 ICU beds ready", "sub_sgn": "Еспаро: 6 мин • 8 ИЦУ апэрто"},
            {"name_en": "St. Aelred Trauma Pavilion", "name_sgn": "Санто Аэльрэд Травма", "val": "68% Occupancy", "sub_en": "Wait time: 4 min • Level 1 Trauma active", "sub_sgn": "Еспаро: 4 мин • Левел 1 Травма"},
            {"name_en": "Highland Alpine Air Ambulance", "name_sgn": "Алпино Аэро Амбуланциа", "val": "100% Operational", "sub_en": "3 Helicopters airborne / on alert", "sub_sgn": "3 Хэликоптэро ин волито"}
        ],
        "action_en": "Refresh Live Hospital Telemetry",
        "action_sgn": "Рэфрэско Хоспитало Тэлэмэтриа",
        "token_prefix": "SNG-ER"
    },
    "transport": {
        "type": "form",
        "icon": "🚐",
        "title_en": "Non-Emergency Medical Transport Booking",
        "title_sgn": "Нон-Сургэнциа Мэдикало Транспорто Скэдуло",
        "fields": [
            {"name": "patient_id", "label_en": "Patient Sangaia ID", "label_sgn": "Патиэнто Сангайа ИД", "type": "text", "placeholder_en": "e.g., SNG-88123-P", "placeholder_sgn": "наприм., SNG-88123-P"},
            {"name": "pickup", "label_en": "Pickup Residential Address", "label_sgn": "Пикап Домицилио Адрэсо", "type": "text", "placeholder_en": "Street, Building, Municipality", "placeholder_sgn": "Виа, Домо, Муниципио"},
            {"name": "clinic", "label_en": "Destination Hospital / Polyclinic", "label_sgn": "Мэдико Дэстинатио", "type": "text", "placeholder_en": "Name of clinic or therapy wing", "placeholder_sgn": "Номэ эк клиника"},
            {"name": "mobility", "label_en": "Mobility Accommodation", "label_sgn": "Мобилито Аккомодатио", "type": "select", "options": [
                {"val": "wheelchair", "en": "Wheelchair Accessible Van with Hydraulic Lift", "sgn": "Рота-Катэдра Адаптадо Ауто"},
                {"val": "stretcher", "en": "Stretcher / Supine Transport with Paramedic", "sgn": "Литиро Транспорто куно Парамедико"},
                {"val": "standard", "en": "Standard Low-Step Assisted Sedan", "sgn": "Стандарто Асистидо Ауто"}
            ]}
        ],
        "action_en": "Dispatch Medical Transport Vehicle",
        "action_sgn": "Диспатчо Мэдикало Транспорто",
        "token_prefix": "SNG-AMB"
    },
    "verifyclinician": {
        "type": "form",
        "icon": "👨‍⚕️",
        "title_en": "Paramedic & Clinician Licensing Verification",
        "title_sgn": "Парамедико & Мэдико Лицэнсиа Вэрификатио",
        "fields": [
            {"name": "clinician_name", "label_en": "Clinician Full Name", "label_sgn": "Мэдико Номэ", "type": "text", "placeholder_en": "e.g., Dr. Elena Vane, Paramedic Mikhail Cole", "placeholder_sgn": "наприм., Др. Елена Ванэ"},
            {"name": "license_no", "label_en": "Board Registration / License #", "label_sgn": "Лицэнсиа Номэро", "type": "text", "placeholder_en": "e.g., MED-LIC-2026-784", "placeholder_sgn": "наприм., MED-LIC-2026-784"}
        ],
        "action_en": "Verify Standing on Sovereign Medical Board",
        "action_sgn": "Вэрифико Мэдикало Лицэнсиа",
        "token_prefix": "SNG-LIC"
    },

    # EDUCATION
    "textbooks": {
        "type": "search",
        "icon": "📖",
        "title_en": "Open Digital Textbooks & Instructional Frameworks",
        "title_sgn": "Апэрто Дигитало Либро & Эдукатио Стандарто",
        "fields": [
            {"name": "grade", "label_en": "Academic Grade Level", "label_sgn": "Академико Градо", "type": "select", "options": [
                {"val": "all", "en": "All Academic Levels", "sgn": "Холо Градо"},
                {"val": "primary", "en": "Primary School (Years 1 to 6)", "sgn": "Примаро Школа (Ано 1-6)"},
                {"val": "secondary", "en": "Secondary College (Years 7 to 12)", "sgn": "Секондаро Коледжио (Ано 7-12)"},
                {"val": "polytech", "en": "Higher Polytech & University", "sgn": "Унивэрсито & Политэкнико"}
            ]}
        ],
        "action_en": "Search Textbook Repositories",
        "action_sgn": "Скэро Либро Рэпозиторио",
        "sample_results_en": [
            {"ref": "TB-MATH-04", "date": "Edition 2026", "title": "Sovereign Geometry & Applied Ecological Physics", "desc": "Official curriculum for Year 9. Open CC-BY-SA license with integrated interactive modeling suites."},
            {"ref": "TB-CIV-02", "date": "Edition 2026", "title": "Sangaian Civics: The Aretocratic Constitution & Zero-Debt Economy", "desc": "Foundational civic education manual exploring constitutional democracy and moral excellence."}
        ],
        "sample_results_sgn": [
            {"ref": "TB-MATH-04", "date": "Эдитио 2026", "title": "Сувэрэно Гэомэтриа & Экологико Физика", "desc": "Официало курикуло про Ано 9. Либэро лиценсиа куно интерактиво модэл."},
            {"ref": "TB-CIV-02", "date": "Эдитио 2026", "title": "Сангайа Цивика: Арэтократико Конститутио & Син-Дэбито", "desc": "Базо цивикано мануало експозито конституционало дрэкто инкаи морал."}
        ]
    },
    "teachercert": {
        "type": "form",
        "icon": "📜",
        "title_en": "Teacher Certification & Licensure Renewal",
        "title_sgn": "Магистро Лицэнсиа Рэнэвадо & Вэрификатио",
        "fields": [
            {"name": "teacher_id", "label_en": "Educator License #", "label_sgn": "Магистро Лицэнсиа Номэро", "type": "text", "placeholder_en": "e.g., EDU-LIC-4482-T", "placeholder_sgn": "наприм., EDU-LIC-4482-T"},
            {"name": "school_district", "label_en": "School District / Institution", "label_sgn": "Школа Дистрикто / Институто", "type": "text", "placeholder_en": "Name of school or district", "placeholder_sgn": "Номэ эк школа"},
            {"name": "ceu_hours", "label_en": "Completed Professional Development Hours (Min 40)", "label_sgn": "Континуо Прогрэсо Хора (Мин 40)", "type": "number", "default": 45}
        ],
        "action_en": "Submit License Renewal Application",
        "action_sgn": "Субмито Рэнэвадо Лицэнсиа",
        "token_prefix": "SNG-TCH"
    },
    "schoolscores": {
        "type": "search",
        "icon": "🏫",
        "title_en": "School Performance & Equity Scorecards",
        "title_sgn": "Школа Пэрформансо & Эквита Карто",
        "fields": [
            {"name": "district", "label_en": "Search District / School Name", "label_sgn": "Скэро Школа вэл Дистрикто", "type": "text", "placeholder_en": "e.g., Capitol Academy, Azure Maritime College", "placeholder_sgn": "наприм., Капитоло Академиа"}
        ],
        "action_en": "Query Equity Scorecard",
        "action_sgn": "Инспэкто Эквита Карто",
        "sample_results_en": [
            {"ref": "SCH-081", "date": "Equity Score: 98.4%", "title": "Capitol High School of Applied Technology", "desc": "Student-teacher ratio: 1:11. Zero student food debt. 100% digital textbook coverage and green energy campus."},
            {"ref": "SCH-142", "date": "Equity Score: 99.1%", "title": "Highland Valley Agricultural & Ecological Academy", "desc": "Student-teacher ratio: 1:9. Fully equipped bio-labs, indoor botanical arboretum, zero tuition fees."}
        ],
        "sample_results_sgn": [
            {"ref": "SCH-081", "date": "Эквита: 98.4%", "title": "Капитоло Алто Школа эк Апликадо Тэк", "desc": "Ратио: 1:11. 0 студент фуд дэбито. 100% дигитало либро инкаи виридо энэргиа."},
            {"ref": "SCH-142", "date": "Эквита: 99.1%", "title": "Алпино Вале Агро & Экологико Академиа", "desc": "Ратио: 1:9. Плэно био-лабораторио, ботанико сардо, 0 туитио дапано."}
        ]
    },
    "studentgrant": {
        "type": "form",
        "icon": "🎓",
        "title_en": "Centralized Student Grant & Bursary Portal",
        "title_sgn": "Универсало Студент Гранто & Бурсарио Портало",
        "fields": [
            {"name": "student_id", "label_en": "Student Sangaia ID", "label_sgn": "Студент Сангайа ИД", "type": "text", "placeholder_en": "e.g., SNG-99120-STU", "placeholder_sgn": "наприм., SNG-99120-STU"},
            {"name": "university", "label_en": "Enrolled University / Institute", "label_sgn": "Унивэрсито / Институто", "type": "text", "placeholder_en": "e.g., National University of Sangaia", "placeholder_sgn": "наприм., Национало Унивэрсито"},
            {"name": "grant_type", "label_en": "Statutory Grant Tier", "label_sgn": "Гранто Катэгорио", "type": "select", "options": [
                {"val": "living", "en": "Monthly Living Cost Stipend ($ 1,400/mo non-repayable)", "sgn": "Вита Стипэнд ($ 1,400/м либэро)"},
                {"val": "research", "en": "STEM / Ecological Field Research Grant ($ 8,000/yr)", "sgn": "Сциэнциа & Биом Гранто ($ 8,000/ан)"},
                {"val": "equipment", "en": "Advanced Tech & Computing Allowance ($ 2,500 one-off)", "sgn": "Компуторо & Эккипаж ($ 2,500)"}
            ]}
        ],
        "action_en": "Issue Non-Repayable Grant Certificate",
        "action_sgn": "Эмито Гранто Сэртификато",
        "token_prefix": "SNG-GRT"
    },
    "debtcalc": {
        "type": "calc",
        "icon": "⚖️",
        "title_en": "Zero-Interest Student Debt Servicing Calculator",
        "title_sgn": "Син-Интересо Студент Дэбито Калкулаторо",
        "fields": [
            {"name": "prior_debt", "label_en": "Foreign / Prior Student Balance ($)", "label_sgn": "Экстэрнало Студент Дэбито ($)", "type": "number", "default": 12000},
            {"name": "income", "label_en": "Monthly Net Earnings ($)", "label_sgn": "Менсио Саларио ($)", "type": "number", "default": 3200}
        ],
        "action_en": "Compute Statutory Zero-Interest Paydown Schedule",
        "action_sgn": "Калкуло Син-Интересо План",
        "token_prefix": "SNG-SCHED"
    },
    "researchpapers": {
        "type": "search",
        "icon": "🔬",
        "title_en": "Peer-Reviewed Sovereign Research Repository",
        "title_sgn": "Пэер-Рэвиудо Сциэнциа Рэпозиторио",
        "fields": [
            {"name": "field", "label_en": "Academic Field", "label_sgn": "Сциэнциа Кампо", "type": "select", "options": [
                {"val": "all", "en": "All Peer-Reviewed Publications", "sgn": "Холо Публикатио"},
                {"val": "eco", "en": "Regenerative Ecology & Biome Engineering", "sgn": "Экологиа & Биом Тэк"},
                {"val": "energy", "en": "Zero-Carbon Geothermal & Solar Dynamics", "sgn": "Гэотэрмало & Соларо Энэргиа"},
                {"val": "med", "en": "Public Health & Preventative Epidemiology", "sgn": "Публико Салуто & Эпидэмиологиа"}
            ]}
        ],
        "action_en": "Search Open-Access Research Archive",
        "action_sgn": "Скэро Сциэнциа Архиво",
        "sample_results_en": [
            {"ref": "DOI-2026-004", "date": "Sept 2026", "title": "High-Efficiency Silvicultural Soil Rejuvenation via Mycelial Networks", "desc": "Published by National Academy of Sciences. 100% open-access raw datasets included."},
            {"ref": "DOI-2026-081", "date": "Aug 2026", "title": "Zero-Emission Mag-Lev Transit Mechanics on Alpine Gradients", "desc": "Empirical field analysis of energy regeneration across the Trans-Sangaian rail spine."}
        ],
        "sample_results_sgn": [
            {"ref": "DOI-2026-004", "date": "Сэп 2026", "title": "Сильва Хум-Рэкуператио виа Мицэлиал Грид", "desc": "Публикадо эк Национало Академиа эк Сциэнциа. Либэро датасет."},
            {"ref": "DOI-2026-081", "date": "Авг 2026", "title": "Син-Эмисио Маг-Лев Транзито супра Алпино Градо", "desc": "Эмпирико анализа эк энэргиа рэнэвадо ин Транз-Сангайа транзито."}
        ]
    },
    "facilitygrant": {
        "type": "form",
        "icon": "🏗️",
        "title_en": "Capital Modernization Grant Submission",
        "title_sgn": "Капитало Модэрнизатио Гранто Субмисио",
        "fields": [
            {"name": "institution_name", "label_en": "School / College Facility Name", "label_sgn": "Школа / Коледжио Номэ", "type": "text", "placeholder_en": "e.g., North Shore Comprehensive School", "placeholder_sgn": "наприм., Нордо Школа"},
            {"name": "project_type", "label_en": "Infrastructure Project", "label_sgn": "Проекто Катэгорио", "type": "select", "options": [
                {"val": "solar", "en": "Rooftop Solar Array & Battery Microgrid", "sgn": "Соларо Тэкто & Батэриа Грид"},
                {"val": "lab", "en": "Advanced Robotics & Chemistry Lab Upgrade", "sgn": "Роботикс & Химиа Лабораторио"},
                {"val": "hvac", "en": "HEPA Air Filtration & Clean Heat Pumps", "sgn": "ХЕПА Аэро Фильтратио & Тэрмало"}
            ]},
            {"name": "cost", "label_en": "Estimated Capital Cost ($)", "label_sgn": "Естимадо Капитало Дапано ($)", "type": "number", "placeholder_en": "180000", "placeholder_sgn": "180000"}
        ],
        "action_en": "File Facility Grant Docket",
        "action_sgn": "Субмито Фасилитатио Гранто",
        "token_prefix": "SNG-FAC"
    },
    "safetyaudits": {
        "type": "search",
        "icon": "🛡️",
        "title_en": "School Safety & Air Quality Inspection Audits",
        "title_sgn": "Школа Салво & Аэро Калита Аудито",
        "fields": [
            {"name": "school_name", "label_en": "Enter School Name", "label_sgn": "Школа Номэ", "type": "text", "placeholder_en": "e.g., St. Justin Academy", "placeholder_sgn": "наприм., Санто Јустин Академиа"}
        ],
        "action_en": "View Safety Scorecard & Inspection Report",
        "action_sgn": "Визо Салво Карто & Аудито",
        "sample_results_en": [
            {"ref": "AUD-SCH-99", "date": "Inspected Oct 2026", "title": "St. Justin Metropolitan Academy", "desc": "Overall Safety Grade: A+ • Particulate Matter (PM2.5): 4 µg/m³ (Pristine) • Seismic rating: Category IV Reinforced."}
        ],
        "sample_results_sgn": [
            {"ref": "AUD-SCH-99", "date": "Аудито Окт 2026", "title": "Санто Јустин Мэтрополитано Академиа", "desc": "Салво Градо: А+ • Аэро ПМ2.5: 4 µг/м³ (Пуро) • Сэисмико рэйтинг: Градо IV Фортис."}
        ]
    },
    "equipswap": {
        "type": "search",
        "icon": "🔄",
        "title_en": "Regional Educational Equipment & Tech Exchange Network",
        "title_sgn": "Рэгионало Эккипаж & Тэк Школа Камбио",
        "fields": [
            {"name": "category", "label_en": "Available Surplus Category", "label_sgn": "Сурплус Эккипаж Катэгорио", "type": "select", "options": [
                {"val": "all", "en": "All Educational Hardware", "sgn": "Холо Школа Хардвэр"},
                {"val": "lab", "en": "Laboratory Microscopes & Centrifuges", "sgn": "Микроскопо & Лабораторио"},
                {"val": "music", "en": "Orchestral Band Instruments", "sgn": "Оркэстрало Музика Инструмэнто"},
                {"val": "robotics", "en": "Microcontroller & 3D Printer Kits", "sgn": "3Д Принтэро & Роботикс Кито"}
            ]}
        ],
        "action_en": "Search Exchange Ledger",
        "action_sgn": "Скэро Камбио Лэджер",
        "sample_results_en": [
            {"ref": "SWAP-2026-44", "date": "Surplus from: Capitol Secondary", "title": "24 Carl Zeiss Compound Optical Microscopes", "desc": "Mint condition. Available for transfer to rural or regional primary schools at zero financial cost."},
            {"ref": "SWAP-2026-19", "date": "Surplus from: High Polytech", "title": "8 Industrial Resin 3D Printers + Filaments", "desc": "Calibrated and ready for student vocational engineering labs."}
        ],
        "sample_results_sgn": [
            {"ref": "SWAP-2026-44", "date": "Сурплус эк: Капитоло Школа", "title": "24 Карл Зэис Оптико Микроскопо", "desc": "Оптимо кондицио. Либэро про транзфэро ад рурало школа син-пага."},
            {"ref": "SWAP-2026-19", "date": "Сурплус эк: Алто Политэк", "title": "8 Индустриало 3Д Принтэро + Матэриало", "desc": "Калибрадо про студент инжениро лабораторио."}
        ]
    },

    # DOMESTIC AFFAIRS
    "hazardmap": {
        "type": "telemetry",
        "icon": "🛣️",
        "title_en": "Live Highway Cameras & Road Hazard Map",
        "title_sgn": "Ливо Виа Камера & Хазардо Карто",
        "metrics": [
            {"name_en": "Highway S-1: Jasper-Madison Arterial", "name_sgn": "Виа С-1: Јаспэр-Мадисон", "val": "Clear & Dry (74 Кмн/h / 110 km/h)", "sub_en": "Shesk &harr; Madison City • 0 obstructions", "sub_sgn": "Шэск &harr; Мадисон • 0 блокадо"},
            {"name_en": "Highway S-2: Liveland Trunk", "name_sgn": "Виа С-2: Ливланд Транзито", "val": "Clear & Shaded (60 Кмн/h / 90 km/h)", "sub_en": "Oaks &harr; Shesk Corridor", "sub_sgn": "Оакс &harr; Шэск Коридоро"},
            {"name_en": "Highway S-3: Sentinel Alpine Pass", "name_sgn": "Виа С-3: Сэнтинэл Пасо", "val": "Clear & Dry (40 Кмн/h / 60 km/h)", "sub_en": "Heated roadbeds active • Sentinel Ridge", "sub_sgn": "Тэрмало виа • Сэнтинэл Ридж"}
        ],
        "action_en": "Refresh Live Roadway Feeds",
        "action_sgn": "Рэфрэско Виа Камера",
        "token_prefix": "SNG-TRAF"
    },
    "transitpass": {
        "type": "form",
        "icon": "💳",
        "title_en": "Automated Transponder & Transit Pass",
        "title_sgn": "Аввтоматико Транспондэро & Транзито Пасо",
        "fields": [
            {"name": "vehicle_plate", "label_en": "Vehicle License Plate # or Pass ID", "label_sgn": "Ауто Таблицо вэл Пасо ИД", "type": "text", "placeholder_en": "e.g., SNG-CAP-4091", "placeholder_sgn": "наприм., SNG-CAP-4091"},
            {"name": "recharge_amount", "label_en": "Top-Up Balance in $ (0% Commute Fee Policy)", "label_sgn": "Рэкарга Сума ин $", "type": "number", "default": 50}
        ],
        "action_en": "Link Transponder & Update Balance",
        "action_sgn": "Конэкто Транспондэро & Активо",
        "token_prefix": "SNG-TOLL"
    },
    "roaddefect": {
        "type": "form",
        "icon": "🚧",
        "title_en": "Road Defect & Hazard Rapid Reporting",
        "title_sgn": "Виа Фалу & Потхол Рапидо Рэпорто",
        "fields": [
            {"name": "route_name", "label_en": "Highway or Municipal Street Name", "label_sgn": "Виа вэл Муниципио Номэ", "type": "text", "placeholder_en": "e.g., Route 1 Milepost 42, Alpine Way", "placeholder_sgn": "наприм., Маршруто 1 Киломэтро 42"},
            {"name": "defect_type", "label_en": "Hazard Category", "label_sgn": "Хазардо Катэгорио", "type": "select", "options": [
                {"val": "pothole", "en": "Pothole / Surface Degradation", "sgn": "Потхол / Асфалто Фалу"},
                {"val": "rockfall", "en": "Fallen Rock / Landslide Obstruction", "sgn": "Пэтра Рока / Мудо Блокадо"},
                {"val": "guardrail", "en": "Damaged Guardrail / Safety Barrier", "sgn": "Дамагидо Салво Бариэро"},
                {"val": "ice", "en": "Black Ice / Malfunctioning Road Heating", "sgn": "Гласио / Тэрмало Фалу"}
            ]},
            {"name": "description", "label_en": "Specific Milepost / Visual Landmark", "label_sgn": "Дэтало & Ладмарко", "type": "textarea", "placeholder_en": "Provide landmarks or nearby exits...", "placeholder_sgn": "Скрибо ландмарко..."}
        ],
        "action_en": "Dispatch Highway Maintenance Crew",
        "action_sgn": "Диспатчо Виа Маинтэнанс",
        "token_prefix": "SNG-RWD"
    },
    "dmvlicense": {
        "type": "form",
        "icon": "🪪",
        "title_en": "Driver's License Renewal & Digital Permit",
        "title_sgn": "Драивэро Лицэнсиа Рэнэвадо & Дигитало Пасо",
        "fields": [
            {"name": "license_no", "label_en": "Current License #", "label_sgn": "Лицэнсиа Номэро", "type": "text", "placeholder_en": "e.g., DL-SNG-889102", "placeholder_sgn": "наприм., DL-SNG-889102"},
            {"name": "class", "label_en": "Operator License Classification", "label_sgn": "Лицэнсиа Градо", "type": "select", "options": [
                {"val": "class_c", "en": "Class C: Standard Passenger Automobile", "sgn": "Класо Ц: Пасагэро Ауто"},
                {"val": "class_cdl", "en": "Class A: Commercial Heavy Hauler / Clean Transit Bus", "sgn": "Класо А: Комэрциало Грави Транзито"},
                {"val": "class_m", "en": "Class M: Electric Motorcycle & Light Vehicle", "sgn": "Класо М: Элэктрико Мотоцикло"}
            ]}
        ],
        "action_en": "Issue Digital Driver's License Docket",
        "action_sgn": "Эмито Дигитало Лицэнсиа",
        "token_prefix": "SNG-DMV"
    },
    "dmvreg": {
        "type": "form",
        "icon": "🚗",
        "title_en": "Vehicle Registration & Title Transfer",
        "title_sgn": "Ауто Рэгистро & Титуло Транзфэро",
        "fields": [
            {"name": "vin", "label_en": "Vehicle Identification Number (VIN)", "label_sgn": "Ауто ИД Номэро (ВИН)", "type": "text", "placeholder_en": "17-character VIN", "placeholder_sgn": "17-символо ВИН"},
            {"name": "propulsion", "label_en": "Propulsion Standard", "label_sgn": "Энэргиа Стандарто", "type": "select", "options": [
                {"val": "ev", "en": "100% Electric Vehicle (Zero Registration Duty)", "sgn": "100% Элэктрико Ауто (0 Такса)"},
                {"val": "hydrogen", "en": "Hydrogen Fuel Cell (Zero Registration Duty)", "sgn": "Хидрогэн Сел (0 Такса)"},
                {"val": "hybrid", "en": "Ultra-Low Emission Bio-Hybrid", "sgn": "Ултра-Басо Эмисио Хибрид"}
            ]}
        ],
        "action_en": "Register Sovereign Vehicle Title",
        "action_sgn": "Рэгистро Ауто Титуло",
        "token_prefix": "SNG-VEH"
    },
    "dmvcitation": {
        "type": "calc",
        "icon": "⚖️",
        "title_en": "Traffic Citation Adjudication & Payment",
        "title_sgn": "Трафико Цитатио Адјудикатио & Пага",
        "fields": [
            {"name": "citation_no", "label_en": "Citation Number", "label_sgn": "Цитатио Номэро", "type": "text", "placeholder_en": "e.g., CIT-2026-9041", "placeholder_sgn": "наприм., CIT-2026-9041"},
            {"name": "plate", "label_en": "Vehicle Plate #", "label_sgn": "Ауто Таблицо", "type": "text", "placeholder_en": "e.g., SNG-CAP-4091", "placeholder_sgn": "наприм., SNG-CAP-4091"}
        ],
        "action_en": "Adjudicate Fine or Submit Judicial Review",
        "action_sgn": "Адјудико Фалу вэл Јуридо Рэвизио",
        "token_prefix": "SNG-CIT"
    },
    "shippingmanifest": {
        "type": "form",
        "icon": "📦",
        "title_en": "Inter-Provincial Shipping Manifest Portal",
        "title_sgn": "Интер-Провинциало Карго Манифэсто Портало",
        "fields": [
            {"name": "origin_prov", "label_en": "Origin Province", "label_sgn": "Оригино Провинциа", "type": "select", "options": [
                {"val": "new_jasper", "en": "New Jasper Province (Shesk)", "sgn": "Ново Јаспэр (Шэск)"},
                {"val": "new_madison", "en": "New Madison Province (Madison City)", "sgn": "Ново Мадисон (Мадисон)"},
                {"val": "liveland", "en": "Liveland Province (Oaks)", "sgn": "Ливланд (Оакс)"},
                {"val": "sentinel", "en": "Sentinel Province (Sentinel Ridge)", "sgn": "Сэнтинэл (Сэнтинэл)"},
                {"val": "columbia", "en": "Columbia Province (Columbia City)", "sgn": "Колумбиа (Колумбиа)"}
            ]},
            {"name": "dest_prov", "label_en": "Destination Province", "label_sgn": "Дэстинатио Провинциа", "type": "select", "options": [
                {"val": "columbia", "en": "Columbia Province (Columbia City)", "sgn": "Колумбиа (Колумбиа)"},
                {"val": "new_jasper", "en": "New Jasper Province (Shesk)", "sgn": "Ново Јаспэр (Шэск)"},
                {"val": "new_madison", "en": "New Madison Province (Madison City)", "sgn": "Ново Мадисон (Мадисон)"},
                {"val": "liveland", "en": "Liveland Province (Oaks)", "sgn": "Ливланд (Оакс)"},
                {"val": "sentinel", "en": "Sentinel Province (Sentinel Ridge)", "sgn": "Сэнтинэл (Сэнтинэл)"}
            ]},
            {"name": "commodity", "label_en": "Cargo Description & Weight (Tonnes)", "label_sgn": "Карго Дэтало & Пондо (Тон)", "type": "text", "placeholder_en": "e.g., 40 Tonnes Hydroponic Wheat, Clean Batteries", "placeholder_sgn": "наприм., 40 Тон Грано, Батэриа"}
        ],
        "action_en": "Issue Inter-Provincial Transit Manifest",
        "action_sgn": "Эмито Провинциало Карго Манифэсто",
        "token_prefix": "SNG-TRD"
    },
    "trademap": {
        "type": "telemetry",
        "icon": "🗺️",
        "title_en": "Internal Trade & Jurisdiction Boundary Map",
        "title_sgn": "Интерно Трэйд & Граница Карто",
        "metrics": [
            {"name_en": "Internal Tariff Rate", "name_sgn": "Интерно Тарифо Градо", "val": "0.00% Statutory", "sub_en": "Article IV: 0% tariffs across New Jasper, New Madison, Liveland, Sentinel, Columbia", "sub_sgn": "Артикло IV: 0% тарифо транз Ново Јаспэр, Ново Мадисон, Ливланд, Сэнтинэл, Колумбиа"},
            {"name_en": "Average Inter-Provincial Transit Time", "name_sgn": "Мэдиа Карго Тэмпоро", "val": "4.2 Hours", "sub_en": "Direct zero-checkpoint green lanes", "sub_sgn": "Прямо виридо коридоро"},
            {"name_en": "Active Domestic Freight Volume", "name_sgn": "Активо Домистико Карго", "val": "184,000 Tonnes/Day", "sub_en": "84% transported via clean electrified rail", "sub_sgn": "84% виа элэктрико транзито"}
        ],
        "action_en": "Inspect Provincial Trade Corridors",
        "action_sgn": "Инспэкто Трэйд Коридоро",
        "token_prefix": "SNG-MAP"
    },
    "arbitration": {
        "type": "form",
        "icon": "⚖️",
        "title_en": "Commercial Arbitration Dispute Registry",
        "title_sgn": "Комэрциало Арбитрато Диспуто Рэгистро",
        "fields": [
            {"name": "plaintiff", "label_en": "Complainant Enterprise / Cooperative", "label_sgn": "Пэтиторо Фирма / Коопэративо", "type": "text", "placeholder_en": "Enterprise name and provincial seat", "placeholder_sgn": "Фирма номэ"},
            {"name": "defendant", "label_en": "Respondent Enterprise", "label_sgn": "Рэспондэнто Фирма", "type": "text", "placeholder_en": "Enterprise name and provincial seat", "placeholder_sgn": "Фирма номэ"},
            {"name": "dispute_type", "label_en": "Commercial Dispute Category", "label_sgn": "Диспуто Катэгорио", "type": "select", "options": [
                {"val": "contract", "en": "Inter-Provincial Supply Contract Breach", "sgn": "Контракто Брэач"},
                {"val": "spec", "en": "Material Quality or Ecological Non-Compliance", "sgn": "Калита вэл Экологико Фалу"},
                {"val": "freight", "en": "Logistical Delay or Transit Damage", "sgn": "Логистико Еспаро вэл Дамагидо"}
            ]}
        ],
        "action_en": "Submit to Federal Commercial Arbitrator",
        "action_sgn": "Субмито ад Федерало Арбитраторо",
        "token_prefix": "SNG-ARB"
    },

    # EXTERNAL AFFAIRS
    "passportportal": {
        "type": "form",
        "icon": "🛂",
        "title_en": "Passport Application & Renewal Portal",
        "title_sgn": "Паспорто Апликатио & Рэнэвадо Портало",
        "fields": [
            {"name": "citizen_id", "label_en": "Citizen Sangaia ID", "label_sgn": "Цивикано Сангайа ИД", "type": "text", "placeholder_en": "e.g., SNG-88910-PAS", "placeholder_sgn": "наприм., SNG-88910-PAS"},
            {"name": "passport_type", "label_en": "Passport Booklet Type", "label_sgn": "Паспорто Типо", "type": "select", "options": [
                {"val": "standard", "en": "Standard Sovereign Citizen Passport (36 Pages)", "sgn": "Стандарто Цивикано Паспорто (36 Пагина)"},
                {"val": "frequent", "en": "Frequent Traveler Passport (52 Pages)", "sgn": "Фрэквэнто Паспорто (52 Пагина)"},
                {"val": "diplomatic", "en": "Official / Diplomatic Service Passport", "sgn": "Дипломатико Сэрвицо Паспорто"}
            ]},
            {"name": "delivery", "label_en": "Dispatch Option", "label_sgn": "Дэливери Оптио", "type": "select", "options": [
                {"val": "provincial", "en": "Pickup at Provincial Passport Registry", "sgn": "Пикап ин Провинциало Рэгистро"},
                {"val": "courier", "en": "Secure State Courier to Home Address", "sgn": "Салво Куриэро ад Домо"}
            ]}
        ],
        "action_en": "Issue Biometric Passport Docket",
        "action_sgn": "Эмито Биомэтрико Паспорто Докэто",
        "token_prefix": "SNG-PAS"
    },
    "embassydir": {
        "type": "search",
        "icon": "🏛️",
        "title_en": "Global Embassy Directory & Consular Registry",
        "title_sgn": "Глобало Амбасада Дирэкторио & Консуларо",
        "fields": [
            {"name": "country", "label_en": "Select Nation / Territory", "label_sgn": "Селекто Патриа", "type": "select", "options": [
                {"val": "all", "en": "All Sovereign Missions Worldwide", "sgn": "Холо Мисио ин Мундо"},
                {"val": "uk", "en": "United Kingdom (London - Embassy of Sangaia)", "sgn": "Унито Рэгино (Лондон)"},
                {"val": "ch", "en": "Switzerland (Bern & Geneva Permanent Mission)", "sgn": "Хэльвэциа (Бэрн & Жэнэва)"},
                {"val": "fr", "en": "France (Paris - Embassy of Sangaia)", "sgn": "Франциа (Парис)"},
                {"val": "jp", "en": "Japan (Tokyo - Embassy of Sangaia)", "sgn": "Јапан (Токио)"},
                {"val": "us", "en": "United States (Washington, D.C.)", "sgn": "Унито Стато (Вашингтон)"}
            ]}
        ],
        "action_en": "View Mission Coordinates & Emergency Phone",
        "action_sgn": "Визо Мисио Адрэсо & Тэлефоно",
        "sample_results_en": [
            {"ref": "EMB-LON", "date": "Consular Hours: 09:00 - 16:30", "title": "Embassy of the United Provinces of Sangaia - London", "desc": "Ambassador: Her Excellency Marianne Laurent • 24/7 Citizen Emergency Consular Dispatch: +44 20 7946 0991 • Direct encrypted video link available."},
            {"ref": "EMB-GVA", "date": "Consular Hours: 08:30 - 17:00", "title": "Permanent Mission to the United Nations - Geneva", "desc": "Permanent Representative: Dr. Alexis Thorne • Diplomatic protocol, multilateral treaties & emergency pass issuing."}
        ],
        "sample_results_sgn": [
            {"ref": "EMB-LON", "date": "Официо Хора: 09:00 - 16:30", "title": "Амбасада эк Сангайа ин Лондон (Унито Рэгино)", "desc": "Амбасадоро: Мариан Лаурэнт • 24/7 Сургэнциа Тэлефоно: +44 20 7946 0991 • Криптографико видео канало."},
            {"ref": "EMB-GVA", "date": "Официо Хора: 08:30 - 17:00", "title": "Пэрмананто Мисио ад Унито Натио - Жэнэва", "desc": "Др. Алексис Торнэ • Дипломатико протоколо & сургэнциа паспорто."}
        ]
    },
    "emergencyconsular": {
        "type": "form",
        "icon": "🆘",
        "title_en": "Emergency Overseas Consular Assistance Hotline",
        "title_sgn": "24/7 Сургэнциа Консуларо Асистансо Хэлплине",
        "fields": [
            {"name": "traveler_id", "label_en": "Citizen Passport # / Sangaia ID", "label_sgn": "Паспорто Номэро / Сангайа ИД", "type": "text", "placeholder_en": "e.g., SNG-PAS-90412", "placeholder_sgn": "наприм., SNG-PAS-90412"},
            {"name": "curr_country", "label_en": "Current Foreign Location (City & Country)", "label_sgn": "Локало Ситадо (Урби & Патриа)", "type": "text", "placeholder_en": "e.g., Marseille, France; Cairo, Egypt", "placeholder_sgn": "наприм., Марсэль, Франциа"},
            {"name": "nature", "label_en": "Emergency Type", "label_sgn": "Сургэнциа Катэгорио", "type": "select", "options": [
                {"val": "medical", "en": "Severe Medical Emergency / Evacuation Needed", "sgn": "Грави Мэдикало Сургэнциа / Эвакуатио"},
                {"val": "lost_doc", "en": "Stolen / Lost Passport & Stranded", "sgn": "Пэрдидо Паспорто / Блокадо"},
                {"val": "detention", "en": "Legal Detainment / Custody Without Representation", "sgn": "Јуридо Дэтентио Син-Адвокато"},
                {"val": "disaster", "en": "Natural Disaster / Armed Civil Unrest", "sgn": "Натурало Каласа / Конфликто"}
            ]},
            {"name": "contact_phone", "label_en": "Local Contact Phone or Embassy Contact", "label_sgn": "Локало Тэлефоно Номэро", "type": "text", "placeholder_en": "+ country code and local number", "placeholder_sgn": "+ кодо инкаи номэро"}
        ],
        "action_en": "Trigger Immediate Consular Rescue Protocol",
        "action_sgn": "Активо Сургэнциа Консуларо Протоколо",
        "token_prefix": "SNG-SOS"
    },
    "treatyarchive": {
        "type": "search",
        "icon": "📜",
        "title_en": "Searchable Ratified International Treaties Archive",
        "title_sgn": "Ратифико Интернационало Трактато Архиво",
        "fields": [
            {"name": "topic", "label_en": "Treaty Classification", "label_sgn": "Трактато Катэгорио", "type": "select", "options": [
                {"val": "all", "en": "All Bilateral & Multilateral Accords", "sgn": "Холо Трактато & Акордо"},
                {"val": "peace", "en": "Non-Aggression, Sovereignty & Neutrality", "sgn": "Пако, Сувэрэнито & Нэутрало"},
                {"val": "climate", "en": "Global Biome & Ecological Protection Pacts", "sgn": "Глобало Биом & Климато"},
                {"val": "trade", "en": "Fair Trade & Maritime Navigation Conventions", "sgn": "Јусто Трэйд & Маритимо"}
            ]}
        ],
        "action_en": "Search Ratified Accords",
        "action_sgn": "Скэро Ратифико Трактато",
        "sample_results_en": [
            {"ref": "TRY-2025-01", "date": "Ratified 2025", "title": "Alpine Trans-Oceanic Neutrality Convention", "desc": "Signatories: Sangaia and 18 Sovereign Republics. Binding perpetual neutrality and ban on offensive weapons transit."},
            {"ref": "TRY-2024-09", "date": "Ratified 2024", "title": "Global Biome Corridors & Migratory Species Accord", "desc": "Commitment to maintain unfenced ecological corridors across international territorial frontiers."}
        ],
        "sample_results_sgn": [
            {"ref": "TRY-2025-01", "date": "Ратифико 2025", "title": "Алпино Транз-Оцэано Нэутрало Конвэнтио", "desc": "Сигнаторо: Сангайа инкаи 18 Сувэрэно Рэпублика. Пэрмананто нэутрало & син-милитаро."},
            {"ref": "TRY-2024-09", "date": "Ратифико 2024", "title": "Глобало Биом Коридоро & Мигратио Спэциэ Акордо", "desc": "Облигатио про салво эк экологико коридоро транз интернационало граница."}
        ]
    },
    "compliance": {
        "type": "telemetry",
        "icon": "⚖️",
        "title_en": "Treaty Compliance & Sovereign Legal Advisory",
        "title_sgn": "Трактато Комплиансо & Јуридо Адвисори",
        "metrics": [
            {"name_en": "Sovereign Compliance Index", "name_sgn": "Сувэрэно Комплиансо", "val": "100.0% Perfect", "sub_en": "Zero sanctions, zero international tribunal breaches", "sub_sgn": "0 санкцио, 0 трибунало фалу"},
            {"name_en": "Active Bilateral Treaties", "name_sgn": "Активо Билатэрало Трактато", "val": "64 Treaties", "sub_en": "Full diplomatic reciprocity established", "sub_sgn": "Плэно дипломатико рэципроко"},
            {"name_en": "Global Neutrality Rating", "name_sgn": "Глобало Нэутрало Градо", "val": "AAA Sovereign", "sub_en": "Recognized sanctuary of peaceful mediation", "sub_sgn": "Рэкогнито пако медиатио"}
        ],
        "action_en": "Verify Treaty Ledger Hash",
        "action_sgn": "Вэрифико Трактато Лэджер",
        "token_prefix": "SNG-LAW"
    },
    "protocolreg": {
        "type": "search",
        "icon": "🎖️",
        "title_en": "Diplomatic Protocol & Immunity Register",
        "title_sgn": "Дипломатико Протоколо & Имунито Рэгистро",
        "fields": [
            {"name": "mission", "label_en": "Accredited Foreign Diplomatic Mission", "label_sgn": "Акрэдитадо Дипломатико Мисио", "type": "text", "placeholder_en": "e.g., Embassy of the French Republic", "placeholder_sgn": "наприм., Амбасада Франциа"}
        ],
        "action_en": "Verify Diplomatic Standing",
        "action_sgn": "Вэрифико Дипломатико Статуто",
        "sample_results_en": [
            {"ref": "DIP-REG-104", "date": "Active 2026", "title": "Embassy of the French Republic to Sangaia", "desc": "Dean of Corps: Amb. Jean-Luc Mercier • 14 accredited diplomatic staff members with registered sovereign immunity plates (CD-01 to CD-14)."}
        ],
        "sample_results_sgn": [
            {"ref": "DIP-REG-104", "date": "Активо 2026", "title": "Амбасада эк Франциа ад Сангайа", "desc": "Амбасадоро Жан-Люк Мэрсиэ • 14 акрэдитадо дипломато куно ЦД таблицо (ЦД-01 ад ЦД-14)."}
        ]
    },
    "tariffcalc": {
        "type": "calc",
        "icon": "🧮",
        "title_en": "Import / Export Tariff Rate Calculator",
        "title_sgn": "Импорто / Экспорто Тарифо Калкулаторо",
        "fields": [
            {"name": "goods_type", "label_en": "Harmonized Category", "label_sgn": "Карго Катэгорио", "type": "select", "options": [
                {"val": "clean_tech", "en": "Clean Energy Machinery / Solar / Batteries (0% Duty)", "sgn": "Виридо Энэргиа / Соларо / Батэриа (0%)"},
                {"val": "medical", "en": "Pharmaceuticals & Clinical Devices (0% Duty)", "sgn": "Фармациа & Мэдико Эккипаж (0%)"},
                {"val": "luxury", "en": "Non-Essential Consumer Luxury (12% Sovereign Tariff)", "sgn": "Луксусо Продукто (12% Тарифо)"},
                {"val": "raw", "en": "Certified Sustainable Raw Timber / Ore (3% Duty)", "sgn": "Биом-Салво Сильва & Минерало (3%)"}
            ]},
            {"name": "cif_value", "label_en": "Declared Customs Value in $ (CIF)", "label_sgn": "Дэкларадо Валорэ ин $ (ЦИФ)", "type": "number", "default": 10000}
        ],
        "action_en": "Calculate Statutory Customs Duty & Offsets",
        "action_sgn": "Калкуло Тарифо & Офсэт",
        "token_prefix": "SNG-TRF"
    },
    "dossiers": {
        "type": "search",
        "icon": "📁",
        "title_en": "Exporters Market Intelligence Dossiers",
        "title_sgn": "Экспорто Маркэто Информатио Досиэры",
        "fields": [
            {"name": "region", "label_en": "Target Export Market", "label_sgn": "Дэстинатио Маркэто", "type": "select", "options": [
                {"val": "eu", "en": "European Union (EFTA & Common Market)", "sgn": "Эуропэо Унион (ЕФТА)"},
                {"val": "asia", "en": "East Asia & Pacific Green Trade Bloc", "sgn": "Ориэнто Асиа & Пацифико"},
                {"val": "americas", "en": "Americas Sustainable Agritech Consortium", "sgn": "Америкас Агро-Тэк"}
            ]}
        ],
        "action_en": "Download Trade Intelligence Dossier",
        "action_sgn": "Дэскарго Трэйд Досиэ",
        "sample_results_en": [
            {"ref": "DOS-2026-EU", "date": "Updated Oct 2026", "title": "Exporting Sangaian Organic Specialty Crops to Central Europe", "desc": "Zero-pesticide certification compliance, phytosanitary clearance pathways, and rapid green corridor clearance."}
        ],
        "sample_results_sgn": [
            {"ref": "DOS-2026-EU", "date": "Активо Окт 2026", "title": "Экспорто эк Сангайа Био-Кроп ад Эуропа", "desc": "Син-химико сэртификатио, фитосанитаро канало, инкаи рапидо коридоро."}
        ]
    },
    "fdi": {
        "type": "form",
        "icon": "💼",
        "title_en": "Foreign Ethical Investment Registration Portal",
        "title_sgn": "Экстэрнало Морало Инвэститио Рэгистро",
        "fields": [
            {"name": "investor_name", "label_en": "Foreign Enterprise / Investment Fund", "label_sgn": "Экстэрнало Фирма / Фондо Номэ", "type": "text", "placeholder_en": "e.g., Zurich Nordic Clean Infrastructure Fund", "placeholder_sgn": "наприм., Нордик Климато Фондо"},
            {"name": "sector", "label_en": "Investment Target Sector (Must satisfy ESG Article II)", "label_sgn": "Инвэститио Сэкторо", "type": "select", "options": [
                {"val": "geo", "en": "Deep Geothermal & Clean District Heat (100% Asset-Backed)", "sgn": "Гэотэрмало & Тэрмало Дистрикто"},
                {"val": "agro", "en": "Regenerative Agro-Forestry & Organic Orchards", "sgn": "Агро-Форест & Органик"},
                {"val": "rail", "en": "Inter-City Magnetic Levitation Line Expansion", "sgn": "Магнэтико Транзито Экспансио"}
            ]},
            {"name": "capital", "label_en": "Proposed Direct Capital Injection ($)", "label_sgn": "Капитало Сума ин $", "type": "number", "placeholder_en": "5000000", "placeholder_sgn": "5000000"}
        ],
        "action_en": "Submit Ethical Investment Dossier for Cabinet Review",
        "action_sgn": "Субмито Инвэститио Досиэ",
        "token_prefix": "SNG-FDI"
    },

    # ENVIRONMENT
    "biomemap": {
        "type": "telemetry",
        "icon": "🌲",
        "title_en": "Interactive Biome Health & Forest Canopy Map",
        "title_sgn": "Интерактиво Биом Салуто & Сильва Карто",
        "metrics": [
            {"name_en": "National Forest Canopy Density", "name_sgn": "Национало Сильва Дэнсито", "val": "88.64% Pristine", "sub_en": "+1.2% year-over-year canopy regeneration", "sub_sgn": "+1.2% ануало рэнэвадо"},
            {"name_en": "Soil Microbial Health Index", "name_sgn": "Хумо Микробио Салуто", "val": "9.4 / 10.0", "sub_en": "Zero synthetic pesticide contamination", "sub_sgn": "0 синтетико пэстицидо"},
            {"name_en": "Freshwater Watershed Purity", "name_sgn": "Аква Салво Индэксо", "val": "99.8% Potable", "sub_en": "Direct alpine glacial melt telemetry", "sub_sgn": "Дирэкто алпино аква"}
        ],
        "action_en": "Refresh Biome Sensor Satellite Telemetry",
        "action_sgn": "Рэфрэско Сатэлито Тэлэмэтриа",
        "token_prefix": "SNG-BIO"
    },
    "camppermit": {
        "type": "form",
        "icon": "⛺",
        "title_en": "Wilderness Entry & Alpine Camping Permits",
        "title_sgn": "Биом Интро & Алпино Кампинг Пэрмито",
        "fields": [
            {"name": "citizen_id", "label_en": "Leader Sangaia ID / Passport #", "label_sgn": "Лидэро Сангайа ИД / Паспорто", "type": "text", "placeholder_en": "e.g., SNG-99124-E", "placeholder_sgn": "наприм., SNG-99124-E"},
            {"name": "biome_zone", "label_en": "Designated Biome Reserve", "label_sgn": "Биом Зона", "type": "select", "options": [
                {"val": "highland", "en": "Northern High Ridge Alpine Sanctuary (Zero Leave-Behind)", "sgn": "Нордо Алпино Санктуаро"},
                {"val": "emerald", "en": "Emerald Rainforest Glade & Wetland Corridor", "sgn": "Эмэральдо Сильва & Аква"},
                {"val": "coastal", "en": "Azure Maritime Fjord Trail & Island Reserve", "sgn": "Азуро Маритимо Фиордо"}
            ]},
            {"name": "hikers", "label_en": "Number of Campers (Max 6 per party)", "label_sgn": "Нумеро эк Камперо (Макс 6)", "type": "number", "default": 2},
            {"name": "entry_date", "label_en": "Permit Start Date", "label_sgn": "Пэрмито Дата", "type": "date"}
        ],
        "action_en": "Issue Cryptographic Wilderness Camping Pass",
        "action_sgn": "Эмито Крипто-Пэрмито",
        "token_prefix": "SNG-CAMP"
    },
    "treeplant": {
        "type": "form",
        "icon": "🌱",
        "title_en": "National Tree-Planting Registry & Tracker",
        "title_sgn": "Национало Арборо Планто Рэгистро",
        "fields": [
            {"name": "planter_name", "label_en": "Citizen or School Cooperative Name", "label_sgn": "Цивикано вэл Школа Номэ", "type": "text", "placeholder_en": "e.g., Green Valley Primary School, Elena Ward", "placeholder_sgn": "наприм., Виридо Школа"},
            {"name": "species", "label_en": "Native Native Tree Species Planted", "label_sgn": "Арборо Спэциэ", "type": "select", "options": [
                {"val": "pine", "en": "Sangaian Alpine Mountain Pine (Pinus sangaiensis)", "sgn": "Сангайа Алпино Пино"},
                {"val": "oak", "en": "Silver Mountain Oak (Quercus argentea)", "sgn": "Аргенто Монтана Робуро"},
                {"val": "cedar", "en": "Highland Red Cedar (Thuja montis)", "sgn": "Алпино Рубро Цедро"}
            ]},
            {"name": "quantity", "label_en": "Number of Saplings Planted", "label_sgn": "Нумеро эк Арборо", "type": "number", "default": 25}
        ],
        "action_en": "Record Trees on Sovereign Living Ledger",
        "action_sgn": "Записадо ин Живо Лэджер",
        "token_prefix": "SNG-TREE"
    },
    "wildlifereport": {
        "type": "form",
        "icon": "🦉",
        "title_en": "24/7 Wildlife Incident & Poaching Hotline",
        "title_sgn": "24/7 Фауна Сургэнциа & Салво Хэлплине",
        "fields": [
            {"name": "location", "label_en": "Incident Location / GPS or Landmark", "label_sgn": "Инцидэнто Локало / ГПС вэл Виа", "type": "text", "placeholder_en": "e.g., Trail 4 near Crystal Lake, Milepost 18", "placeholder_sgn": "наприм., Пасо 4 пропе Лако"},
            {"name": "incident", "label_en": "Incident Category", "label_sgn": "Инцидэнто Катэгорио", "type": "select", "options": [
                {"val": "injured", "en": "Injured or Distressed Native Fauna (Ranger Rescue)", "sgn": "Вулнэрадо Фауна (Ранджер Салво)"},
                {"val": "poaching", "en": "Suspected Illegal Trapping, Fishing or Poaching", "sgn": "Илегало Каса вэл Пыска"},
                {"val": "conflict", "en": "Fauna Near Residential Area (Non-Lethal Relocation)", "sgn": "Фауна пропе Домо (Салво Рэлокадо)"}
            ]},
            {"name": "species_desc", "label_en": "Animal Description / Condition", "label_sgn": "Анимало Дэтало & Кондицио", "type": "textarea", "placeholder_en": "Describe animal condition, approximate size, markings...", "placeholder_sgn": "Скрибо анимало кондицио..."}
        ],
        "action_en": "Dispatch Nearest Ecological Ranger Unit",
        "action_sgn": "Диспатчо Биом Ранджер Унито",
        "token_prefix": "SNG-WILD"
    },
    "harvesttag": {
        "type": "form",
        "icon": "🎣",
        "title_en": "Seasonal Ecological Harvest & Fishing Tags",
        "title_sgn": "Сезоно Экологико Пыска & Харвэст Таблицо",
        "fields": [
            {"name": "citizen_id", "label_en": "Citizen Sangaia ID", "label_sgn": "Цивикано Сангайа ИД", "type": "text", "placeholder_en": "e.g., SNG-55819-F", "placeholder_sgn": "наприм., SNG-55819-F"},
            {"name": "harvest_type", "label_en": "Authorized Sustainable Harvest Tier", "label_sgn": "Ауторисадо Харвэст Градо", "type": "select", "options": [
                {"val": "trout", "en": "Alpine Glacial Trout (Catch-and-Release / 2 Limit)", "sgn": "Алпино Трута (Макс 2)"},
                {"val": "forage", "en": "Wild Forest Mushroom & Herbal Foraging (5 kg cap)", "sgn": "Сильва Фунго & Эрби (5 кг цэлинг)"},
                {"val": "berries", "en": "Alpine Bilberry & Cloudberry Gathering", "sgn": "Алпино Бака Колектио"}
            ]}
        ],
        "action_en": "Issue Verified Sustainable Harvest Tag",
        "action_sgn": "Эмито Салво Харвэст Таблицо",
        "token_prefix": "SNG-TAG"
    },
    "species": {
        "type": "search",
        "icon": "🐾",
        "title_en": "Interactive Protected Species Profiles & Interventions",
        "title_sgn": "Протэктадо Фауна Профило & Салво Статуто",
        "fields": [
            {"name": "species_query", "label_en": "Search Protected Fauna & Flora", "label_sgn": "Скэро Фауна & Флора", "type": "text", "placeholder_en": "e.g., Highland Lynx, Golden Osprey, Alpine Chamois", "placeholder_sgn": "наприм., Алпино Линкс, Оспрэй, Шамоис"}
        ],
        "action_en": "Inspect Biological Protection Profile",
        "action_sgn": "Инспэкто Фауна Профило",
        "sample_results_en": [
            {"ref": "FAUNA-01", "date": "Status: Thriving", "title": "Sangaian Highland Lynx (Lynx lynx sangaiensis)", "desc": "Population: 840 individuals (+18% since 2021). Strict zero-disturbance zones across Northern High Ridge."},
            {"ref": "FAUNA-04", "date": "Status: Monitored", "title": "Azure Coastal Golden Osprey (Pandion haliaetus)", "desc": "Nesting pairs: 210. 100% telemetry tagging on fledglings with automated ship-radar protection."}
        ],
        "sample_results_sgn": [
            {"ref": "FAUNA-01", "date": "Статуто: Крэсцито", "title": "Сангайа Алпино Линкс (Lynx lynx sangaiensis)", "desc": "Популатио: 840 (+18% пост 2021). 0-дистурбансо зона транз Нордо Алпино."},
            {"ref": "FAUNA-04", "date": "Статуто: Мониторадо", "title": "Азуро Коста Ауро Оспрэй (Pandion haliaetus)", "desc": "210 нидо пара. 100% тэлэмэтриа таблицо куно аутоматико шип-радаро салво."}
        ]
    },
    "airsensors": {
        "type": "telemetry",
        "icon": "💨",
        "title_en": "Live Air & Watershed Quality Sensor Network",
        "title_sgn": "Ливо Аэро & Аква Калита Сэнсоро Грид",
        "metrics": [
            {"name_en": "New Jasper (Shesk Basin) PM2.5", "name_sgn": "Ново Јаспэр (Шэск) ПМ2.5", "val": "4.2 µg/m³", "sub_en": "Pristine WHO Class 1 clean air", "sub_sgn": "Пуро ВХО Класо 1 аэро"},
            {"name_en": "Sentinel Ridge Ozone", "name_sgn": "Сэнтинэл Ридж Озоно", "val": "0.018 ppm", "sub_en": "Ultra-clean alpine air purity", "sub_sgn": "Ултра-пуро алпино аэро"},
            {"name_en": "Columbia Maritime Basin Oxygen", "name_sgn": "Колумбиа Оксигэн ин Аква", "val": "9.8 mg/L", "sub_en": "Super-oxygenated freshwater & marine vitality", "sub_sgn": "Оптимо марино & аква виталито"}
        ],
        "action_en": "Poll Sensor Grid Stations",
        "action_sgn": "Инспэкто Сэнсоро Грид",
        "token_prefix": "SNG-AIR"
    },
    "emissions": {
        "type": "form",
        "icon": "🏭",
        "title_en": "Industrial Emissions Permitting & Scrubbing Audits",
        "title_sgn": "Индустриало Эмисио Пэрмито & Скрубэро Аудито",
        "fields": [
            {"name": "facility_name", "label_en": "Industrial Facility / Processing Plant", "label_sgn": "Индустриало Фасилитатио / Фабрика", "type": "text", "placeholder_en": "e.g., Trans-Sangaia Rail Foundry #2", "placeholder_sgn": "наприм., Транзито Фабрика 2"},
            {"name": "scrubbing_tech", "label_en": "Installed Scrubbing / Filtration Standard", "label_sgn": "Скрубэро & Фильтратио Стандарто", "type": "select", "options": [
                {"val": "zero", "en": "Closed-Loop Hydro-Scrubber (99.9% Particulate Capture)", "sgn": "Клаудо Хидро-Скрубэро (99.9%)"},
                {"val": "electro", "en": "Electrostatic Precipitator & Catalytic Clean Burn", "sgn": "Элэктростатико Прэципитаторо"},
                {"val": "biofilter", "en": "Biological Algae Bio-Reactor Off-Gas Scrubbing", "sgn": "Био-Алгэ Рэакторо"}
            ]}
        ],
        "action_en": "Certify Emissions Compliance Clearance",
        "action_sgn": "Сэртифико Эмисио Салво",
        "token_prefix": "SNG-EMS"
    },
    "recycling": {
        "type": "search",
        "icon": "♻️",
        "title_en": "Hazardous Waste Drop-Off & Advanced Circularity Locator",
        "title_sgn": "Пэрикуло Васто & Циркуларо Рэциклинг Локаторо",
        "fields": [
            {"name": "waste_type", "label_en": "Material Classification", "label_sgn": "Матэриало Катэгорио", "type": "select", "options": [
                {"val": "battery", "en": "Lithium / Clean Energy Energy Storage Cells", "sgn": "Литиум / Батэриа Сел"},
                {"val": "electronic", "en": "Decommissioned Computing Hardware & PCBs", "sgn": "Компуторо & Елэктронико"},
                {"val": "chemical", "en": "Non-Toxic Solvents & Organic Biocides", "sgn": "Солвэнто & Био-Химиа"}
            ]}
        ],
        "action_en": "Find Nearest Municipal Eco-Depot",
        "action_sgn": "Скэро Эко-Дэпо",
        "sample_results_en": [
            {"ref": "ECO-DEP-01", "date": "Open Mon-Sat 08:00 - 18:00", "title": "Capitol Eco-Circularity Center #4", "desc": "Full precious metal reclamation line, zero landfill destination guarantee. Free drop-off for all citizens."},
            {"ref": "ECO-DEP-07", "date": "Open Mon-Sat 08:30 - 17:30", "title": "Azure Coastal Marine Circularity Haven", "desc": "Specialized lithium cell deconstruction and glass recycling pavilion."}
        ],
        "sample_results_sgn": [
            {"ref": "ECO-DEP-01", "date": "08:00 - 18:00 (Лун-Саб)", "title": "Капитоло Эко-Циркуларита Цэнтро 4", "desc": "Плэно мэтал рэкуператио, 0 васто гаранто. Либэро про холо цивикано."},
            {"ref": "ECO-DEP-07", "date": "08:30 - 17:30 (Лун-Саб)", "title": "Азуро Маритимо Циркуларита Дэпо", "desc": "Литиум батэриа дэконструкто инкаи витро рэциклинг."}
        ]
    },

    # PROPAGANDA
    "livestreams": {
        "type": "media",
        "icon": "📻",
        "title_en": "Live State Broadcast & Assembly Streams",
        "title_sgn": "Ливо Стато Эмито & Асэмблеа Канало",
        "channels": [
            {"id": "sng1", "name_en": "Sangaia National Television (HD-1)", "name_sgn": "Сангайа Национало Тэлэвизио (ХД-1)", "desc_en": "Live parliamentary debates, cabinet briefings, and national news bulletin.", "desc_sgn": "Ливо парламэнт дэбато, кабино нотициа, инкаи национало бюлэтино.", "stream_status": "ON AIR • 1080p50"},
            {"id": "rad_cult", "name_en": "Cultural Radio Sangaia (FM 98.4 MHz)", "name_sgn": "Културало Радио Сангайа (ФМ 98.4)", "desc_en": "Classical orchestral performances, choral hymns, poetry and civic history.", "desc_sgn": "Класико оркэстра, корало химно, поэсиа инкаи цивикано историа.", "stream_status": "LIVE BROADCAST • 320 kbps"},
            {"id": "rad_youth", "name_en": "Youth Educational Audio Stream", "name_sgn": "Јувэнило Эдукатио Аудио Канало", "desc_en": "Science exploration, mathematics lectures, language practice.", "desc_sgn": "Сциэнциа, матэматика, лингва практика.", "stream_status": "LIVE BROADCAST • 256 kbps"}
        ],
        "action_en": "Connect Audio/Video Feed",
        "action_sgn": "Конэкто Аудио/Видео Канало",
        "token_prefix": "SNG-CAST"
    },
    "mediaassets": {
        "type": "search",
        "icon": "🖼️",
        "title_en": "Civic Campaign Media Assets & Vector Graphics",
        "title_sgn": "Цивикано Мэдиа Асэто & Вэкторо Графика",
        "fields": [
            {"name": "asset_type", "label_en": "Asset Classification", "label_sgn": "Асэто Катэгорио", "type": "select", "options": [
                {"val": "all", "en": "All High-Resolution Civic Assets", "sgn": "Холо Цивикано Асэто"},
                {"val": "flags", "en": "National & Provincial Flags (SVG & 8K PNG)", "sgn": "Флаго & Провинциало Символо"},
                {"val": "seals", "en": "Aretocratic Seal & Ministerial Emblems", "sgn": "Арэтократико Сигило & Емблемо"},
                {"val": "posters", "en": "Frutiger Aero Public Health & Ecology Posters", "sgn": "Фрутигер Аэро Салуто & Экологиа Постэро"}
            ]}
        ],
        "action_en": "Browse Digital Asset Library",
        "action_sgn": "Скэро Мэдиа Либро",
        "sample_results_en": [
            {"ref": "AST-VEC-01", "date": "Format: SVG / Vector", "title": "Official Coat of Arms of the United Provinces of Sangaia", "desc": "Master cryptographic vector file with authentic gold foil gradients and Frutiger Aero water sheen."},
            {"ref": "AST-POS-14", "date": "Format: 300 DPI Print", "title": "Zero-Debt Sovereign Harmony: Civic Pride Banner Suite", "desc": "Complete municipal street banner artwork in English and Sangaian Cyrillic."}
        ],
        "sample_results_sgn": [
            {"ref": "AST-VEC-01", "date": "Формато: СВГ / Вэкторо", "title": "Официало Эскудо эк Унито Провинциа эк Сангайа", "desc": "Мастэро вэкторо фаило куно авро градиэнто инкаи Фрутигер Аэро шеен."},
            {"ref": "AST-POS-14", "date": "Формато: 300 ДПИ Принт", "title": "Син-Дэбито Сувэрэно Хармониа: Цивикано Банэро", "desc": "Муниципио банэро арт ин Англико инкаи Сангайа Кирилико."}
        ]
    },
    "civiccal": {
        "type": "search",
        "icon": "📅",
        "title_en": "National Calendar of Civic & Cultural Celebrations",
        "title_sgn": "Национало Калэндарио эк Цивикано Дио",
        "fields": [
            {"name": "month", "label_en": "Select Month", "label_sgn": "Селекто Менсо", "type": "select", "options": [
                {"val": "all", "en": "Full Annual Civic Calendar (2026)", "sgn": "Холо Ануало Калэндарио (2026)"},
                {"val": "oct", "en": "October: Constitution & Civic Harmony Month", "sgn": "Октобро: Конститутио & Хармониа"},
                {"val": "nov", "en": "November: Harvest Bounty & Soil Gratitude", "sgn": "Новэмбро: Харвэст & Хумо Гратиа"},
                {"val": "dec", "en": "December: Winter Solstice & Peace Assemblies", "sgn": "Дэцэмбро: Солстицио & Пако Асэмблеа"}
            ]}
        ],
        "action_en": "View Civic Calendar Schedule",
        "action_sgn": "Визо Цивикано Калэндарио",
        "sample_results_en": [
            {"ref": "CAL-OCT-24", "date": "24 October 2026", "title": "National Constitution & Aretocratic Charter Day", "desc": "Nationwide public festival celebrating sovereign freedom, moral excellence, and the zero-debt economy."},
            {"ref": "CAL-NOV-11", "date": "11 November 2026", "title": "Sovereign Peace & Universal Reconciliation Vigil", "desc": "Interfaith candlelit civic ceremonies in all municipal town squares."}
        ],
        "sample_results_sgn": [
            {"ref": "CAL-OCT-24", "date": "24 Октобро 2026", "title": "Национало Конститутио & Арэтократико Карта Дио", "desc": "Плэно рэпубликано фэстивало цэлэбранто сувэрэно либэрта инкаи син-дэбито."},
            {"ref": "CAL-NOV-11", "date": "11 Новэмбро 2026", "title": "Сувэрэно Пако & Универсало Конкордиа Вигило", "desc": "Интер-крэдо цэрэмониа ин холо муниципио пласа."}
        ]
    },
    "presspass": {
        "type": "form",
        "icon": "🪪",
        "title_en": "Journalist Press Pass Accreditation Portal",
        "title_sgn": "Журналисто Прэс Пасо Акрэдитатио Портало",
        "fields": [
            {"name": "journalist_name", "label_en": "Journalist Full Name", "label_sgn": "Журналисто Номэ", "type": "text", "placeholder_en": "e.g., Katherine Miller, David Cruz", "placeholder_sgn": "наприм., Катэрин Милэр"},
            {"name": "news_org", "label_en": "News Organization / Syndicate", "label_sgn": "Нотициа Организатио / Синдикато", "type": "text", "placeholder_en": "e.g., Sangaia Courier, Alpine Independent Daily", "placeholder_sgn": "наприм., Сангайа Куриэро"},
            {"name": "pass_type", "label_en": "Accreditation Tier", "label_sgn": "Акрэдитатио Градо", "type": "select", "options": [
                {"val": "full", "en": "Class A: Full Executive & Assembly Gallery Access", "sgn": "Класо А: Эксэкуто & Парламэнт Акцэсо"},
                {"val": "provincial", "en": "Class B: Provincial & Municipal Press Galleries", "sgn": "Класо Б: Провинциало Прэс Акцэсо"},
                {"val": "photo", "en": "Class P: Official Photographic & Broadcast Tech", "sgn": "Класо П: Фото & Видео Тэк"}
            ]}
        ],
        "action_en": "Submit Press Credential Application",
        "action_sgn": "Субмито Прэс Лицэнсиа",
        "token_prefix": "SNG-PRS"
    },
    "pressreg": {
        "type": "search",
        "icon": "📰",
        "title_en": "Public Registry of Accredited News Agencies",
        "title_sgn": "Публико Рэгистро эк Акрэдитадо Нотициа",
        "fields": [
            {"name": "agency_name", "label_en": "Search Accredited Media Agency", "label_sgn": "Скэро Нотициа Агэнциа", "type": "text", "placeholder_en": "e.g., Sangaia State Press, Alpine Herald", "placeholder_sgn": "наприм., Сангайа Стато Прэс"}
        ],
        "action_en": "Verify News Agency Standing",
        "action_sgn": "Вэрифико Нотициа Статуто",
        "sample_results_en": [
            {"ref": "NEWS-REG-01", "date": "Status: 100% Verified", "title": "Sangaian State Press Syndicate (SSPS)", "desc": "Editorial Board: Elected Journalist Council • Fact-checking score: 99.8% • Zero corporate lobbyist ownership."},
            {"ref": "NEWS-REG-08", "date": "Status: 100% Verified", "title": "The Northern Highland Tribune", "desc": "Independent worker-owned cooperative newspaper. Headquartered in High Ridge City."}
        ],
        "sample_results_sgn": [
            {"ref": "NEWS-REG-01", "date": "Статуто: 100% Вэрификадо", "title": "Сангайа Стато Прэс Синдикато (ССПС)", "desc": "Едиторо Консилио: Електо журналисто • Факт-чэк: 99.8% • 0 лобинг проприето."},
            {"ref": "NEWS-REG-08", "date": "Статуто: 100% Вэрификадо", "title": "Нордо Алпино Трибунэ", "desc": "Индипэндэнто коопэративо газэта. Сэдэ ин Алпино Урби."}
        ]
    },
    "infoviolation": {
        "type": "form",
        "icon": "⚖️",
        "title_en": "Broadcast Code Violation & Misinformation Hotline",
        "title_sgn": "Эмито Фалу & Мисинформатио Хэлплине",
        "fields": [
            {"name": "outlet", "label_en": "Broadcaster / Publication / Web Domain", "label_sgn": "Эмито / Газэта / Вэб Домаин", "type": "text", "placeholder_en": "e.g., Channel 4, newsfeed.online", "placeholder_sgn": "наприм., Канало 4, вэбсаит"},
            {"name": "violation_type", "label_en": "Violation Category", "label_sgn": "Фалу Катэгорио", "type": "select", "options": [
                {"val": "paid_lobby", "en": "Undisclosed Paid Lobbying / Foreign Oligarchic Promotion", "sgn": "Нон-дэкларо Лобинг вэл Олигархико"},
                {"val": "unlabeled_ai", "en": "Unlabeled AI Synthetic Deepfake / Voice Cloning", "sgn": "Син-ватэрмарко АИ Синтэтико / Дипфэйк"},
                {"val": "defamation", "en": "Malicious Defamation / Knowingly Falsified Evidence", "sgn": "Малициозо Фалу & Калумниа"}
            ]},
            {"name": "broadcast_date", "label_en": "Date & Approximate Broadcast Time", "label_sgn": "Дата & Тэмпоро эк Эмито", "type": "text", "placeholder_en": "e.g., 18 Oct 2026, 19:30 UTC", "placeholder_sgn": "наприм., 18 Окт 2026, 19:30"},
            {"name": "evidence", "label_en": "Description & Evidence URL / Reference", "label_sgn": "Дэтало & Эвидэнциа Ссылко", "type": "textarea", "placeholder_en": "Provide transcript excerpt or recording timestamp...", "placeholder_sgn": "Скрибо транскрипто вэл тэмпоро..."}
        ],
        "action_en": "File Misinformation Docket with Integrity Board",
        "action_sgn": "Субмито Фалу Докэто ад Консилио",
        "token_prefix": "SNG-VIOL"
    },
    "churchreg": {
        "type": "form",
        "icon": "⛪",
        "title_en": "Religious Construct Charter Registration",
        "title_sgn": "Рэлигио Конструкто Карта Рэгистро",
        "fields": [
            {"name": "congregation_name", "label_en": "Congregation / Spiritual Community Name", "label_sgn": "Конгрэгатио / Духовно Комунитиа Номэ", "type": "text", "placeholder_en": "e.g., Chapel of the Eternal Dawn, St. Benedict Parish", "placeholder_sgn": "наприм., Капэла эк Аврора"},
            {"name": "faith_tradition", "label_en": "Faith / Philosophical Tradition", "label_sgn": "Крэдо / Философико Традитио", "type": "text", "placeholder_en": "e.g., Christian Ecumenical, Interfaith Contemplative, Buddhist", "placeholder_sgn": "наприм., Кристиано, Интер-крэдо"},
            {"name": "redistribution_commitment", "label_en": "Mandatory 85%+ Wealth Return Statutory Clause", "label_sgn": "85%+ Рико-Рэдивидо Статуторо Клаузуло", "type": "select", "options": [
                {"val": "full_compliance", "en": "Fully Agree: 85%+ of all tithes dedicated to soup kitchens, shelters & community aid", "sgn": "Плэно Акордо: 85%+ ад фуд-кучина, салво & комунитиа"},
                {"val": "audit_consent", "en": "Full Statutory Consent to Annual Open Treasury Audits", "sgn": "Плэно Акордо ад Ануало Трэзоро Аудито"}
            ]}
        ],
        "action_en": "Register Sovereign Spiritual Construct",
        "action_sgn": "Рэгистро Сувэрэно Экклэсиа",
        "token_prefix": "SNG-REL"
    },
    "churchaudit": {
        "type": "search",
        "icon": "📊",
        "title_en": "Digital Ledger of Recognized Chapels & Wealth Redistribution Audits",
        "title_sgn": "Дигитало Леджер эк Экклэсиа & Рико-Рэдивидо Аудито",
        "fields": [
            {"name": "chapel_name", "label_en": "Search Chapel / Congregation", "label_sgn": "Скэро Экклэсиа / Капэла", "type": "text", "placeholder_en": "e.g., Chapel of St. Julian, Holy Trinity Commune", "placeholder_sgn": "наприм., Капэла эк Санто Јулиан"}
        ],
        "action_en": "Inspect Financial Audit Ledger",
        "action_sgn": "Инспэкто Фискало Аудито",
        "sample_results_en": [
            {"ref": "REL-AUD-04", "date": "FY 2026 Audit: PASSED", "title": "Chapel of St. Julian the Hospitaller (Capitol)", "desc": "Total Tithes Collected: $ 184,000 • Community Redistribution: $ 168,200 (91.4% returned to public soup kitchen and unhoused shelter). Approved by Treasury."},
            {"ref": "REL-AUD-11", "date": "FY 2026 Audit: PASSED", "title": "Azure Coastal Interfaith Contemplative Fellowship", "desc": "Total Tithes Collected: $ 92,000 • Community Redistribution: $ 81,400 (88.5% returned to marine cleanup and elderly care). Approved by Treasury."}
        ],
        "sample_results_sgn": [
            {"ref": "REL-AUD-04", "date": "Аудито 2026: ПРОБАДО", "title": "Капэла эк Санто Јулиан Хоспиталэро (Капитоло)", "desc": "Тотало Даро: $ 184,000 • Комунитиа Дапано: $ 168,200 (91.4% ад фуд-кучина & салво домо). Пробадо эк Трэзоро."},
            {"ref": "REL-AUD-11", "date": "Аудито 2026: ПРОБАДО", "title": "Азуро Маритимо Интер-Крэдо Комунитиа", "desc": "Тотало Даро: $ 92,000 • Комунитиа Дапано: $ 81,400 (88.5% ад марино салво & сэниор). Пробадо эк Трэзоро."}
        ]
    },
    "interfaithcal": {
        "type": "search",
        "icon": "🕊️",
        "title_en": "Interfaith Calendar & Civic Unity Roster",
        "title_sgn": "Интэр-Крэдо Калэндарио & Сонит Ростро",
        "fields": [
            {"name": "season", "label_en": "Select Sacred Season", "label_sgn": "Селекто Сезоно", "type": "select", "options": [
                {"val": "all", "en": "All Recognized Faith Traditions", "sgn": "Холо Рэкогнито Традитио"},
                {"val": "autumn", "en": "Autumn: Festival of the Harvest Solace & Compassion", "sgn": "Автумно: Харвэст & Комписио"},
                {"val": "winter", "en": "Winter: Sacred Light & Peaceful Reflection", "sgn": "Хиверно: Сакро Люкс & Пако"},
                {"val": "spring", "en": "Spring: Renewal, Resurrection & New Life", "sgn": "Вэрано: Рэнэвадо & Насито"}
            ]}
        ],
        "action_en": "Open Interfaith Holy Calendar",
        "action_sgn": "Апэри Интер-Крэдо Калэндарио",
        "sample_results_en": [
            {"ref": "CAL-FAITH-01", "date": "04 November 2026", "title": "All Souls Interfaith Charity & Meal Drive", "desc": "Coordinated volunteer day across all 80 registered chapels, synagogues, and contemplative societies."},
            {"ref": "CAL-FAITH-03", "date": "21 December 2026", "title": "Winter Solstice Community Vigil for Universal Peace", "desc": "Public multi-denominational choral gathering in Capitol Unity Square."}
        ],
        "sample_results_sgn": [
            {"ref": "CAL-FAITH-01", "date": "04 Новэмбро 2026", "title": "Холо Анимас Интер-Крэдо Карита Дио", "desc": "Координадо волунтаро дио транз холо 80 экклэсиа, синагога, инкаи солит спацио."},
            {"ref": "CAL-FAITH-03", "date": "21 Дэцэмбро 2026", "title": "Хиверно Солстицио Вигило про Универсало Пако", "desc": "Публико мулти-крэдо корало асэмблеа ин Капитоло Сонит Пласа."}
        ]
    }
}

print(f"Loaded {len(MODAL_CONFIGS)} rich modal tool configurations.")


def get_page_css(theme):
    return f"""
    /* --- SANGAIA FRUTIGER AERO & SKEUOMORPHIC STYLES --- */
    :root {{
        --theme-primary: {theme['primary']};
        --theme-dark: {theme['dark']};
        --theme-deep: {theme['deep']};
        --theme-light: {theme['light']};
        --theme-pale: {theme['pale']};
        --theme-border: {theme['border']};
        --theme-accent: {theme['accent']};
        --text-dark: #0f172a;
        --text-muted: #475569;
        --card-bg: rgba(255, 255, 255, 0.92);
        --border-panel: #cbd5e1;
        --shadow-gloss: 0 4px 20px rgba(0,0,0,0.08), inset 0 1px 0 rgba(255,255,255,0.9);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
        background: #f1f5f9 radial-gradient(circle at 50% 0%, #ffffff 0%, #e2e8f0 100%) no-repeat fixed;
        min-height: 100vh;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        font-family: 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        color: var(--text-dark);
        line-height: 1.6;
        -webkit-font-smoothing: antialiased;
    }}

    .main-container {{
        width: 100%;
        margin: 0;
        padding: 0;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
    }}

    /* --- GLOBAL HEADER --- */
    #globalheader {{
        display: flex;
        align-items: center;
        position: relative;
        width: 100%;
        height: 38px;
        background: linear-gradient(to bottom, #5e5e5e 0%, #3e3e3e 50%, #2d2d2d 51%, #1f1f1f 100%);
        border-top: 1px solid #222;
        border-bottom: 1px solid #000;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.15), 0 2px 4px rgba(0,0,0,0.2);
        font-size: 11px;
        z-index: 100;
    }}

    #globalnav {{
        flex-grow: 1;
        margin: 0;
        padding: 0;
        list-style: none;
        display: flex;
        justify-content: center;
        height: 100%;
    }}

    #globalnav li {{ position: relative; height: 100%; display: flex; align-items: center; }}
    #globalnav li::after {{
        content: ""; position: absolute; right: 0; width: 1px; height: 100%;
        background: linear-gradient(to bottom, #333, #111); box-shadow: 1px 0 0 rgba(255,255,255,0.08);
    }}
    #globalnav li:first-child::before {{
        content: ""; position: absolute; left: 0; width: 1px; height: 100%;
        background: linear-gradient(to bottom, #333, #111); box-shadow: 1px 0 0 rgba(255,255,255,0.08);
    }}

    #globalnav li a {{
        display: block; color: #e8e8e8; text-decoration: none; text-shadow: 0 -1px 0 rgba(0,0,0,0.8);
        font-weight: bold; padding: 0 14px; line-height: 38px;
        transition: all 0.2s ease;
        white-space: nowrap;
    }}

    #globalnav li a:hover {{
        color: #fff;
        background: linear-gradient(rgba(255,255,255,0.08), rgba(255,255,255,0));
        text-shadow: 0 0 8px rgba(255, 255, 255, 0.8), 0 -1px 0 rgba(0,0,0,0.8);
    }}

    #globalnav li a.active {{
        color: #fff;
        background: rgba(0,0,0,0.3);
        box-shadow: inset 0 2px 5px rgba(0,0,0,0.4);
        border-bottom: 2px solid var(--theme-accent);
    }}

    /* --- SKEUOMORPHIC BUTTONS --- */
    .sangaia-btn {{
        font-size: 0.88rem;
        font-family: inherit;
        height: 2.3em;
        padding: 0 1.2em;
        border-radius: 5px;
        position: relative;
        cursor: pointer;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        transition: all 0.2s ease;
        border: 1px solid #94a3b8;
        background: linear-gradient(to bottom, #ffffff 0%, #f1f5f9 45%, #e2e8f0 100%);
        box-shadow: 0 1px 3px rgba(0,0,0,0.1), inset 0 1px 0 rgba(255,255,255,0.9);
        color: #0f172a;
        font-weight: bold;
    }}

    .sangaia-btn:hover {{
        background: linear-gradient(to bottom, #ffffff 0%, #f8fafc 45%, #cbd5e1 100%);
        box-shadow: 0 2px 6px rgba(15, 23, 42, 0.15), inset 0 1px 0 #ffffff;
        color: #020617;
        transform: translateY(-1px);
    }}

    .sangaia-btn:active {{
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.25);
        transform: translateY(1px);
    }}

    .btn-theme {{
        background: linear-gradient(to bottom, var(--theme-light) 0%, var(--theme-primary) 60%, var(--theme-dark) 100%);
        border: 1px solid var(--theme-deep);
        color: #ffffff !important;
        text-shadow: 0 -1px 1px rgba(0,0,0,0.5);
        box-shadow: 0 2px 5px rgba(0,0,0,0.2), inset 0 1px 0 rgba(255,255,255,0.4);
    }}

    .btn-theme:hover {{
        background: linear-gradient(to bottom, #ffffff 0%, var(--theme-light) 20%, var(--theme-primary) 100%);
        box-shadow: 0 4px 10px rgba(0,0,0,0.25), inset 0 1px 0 rgba(255,255,255,0.6);
        color: #ffffff !important;
    }}

    .btn-gold {{
        background: linear-gradient(to bottom, #fbbf24 0%, #d97706 60%, #92400e 100%);
        border: 1px solid #78350f;
        color: #ffffff !important;
        text-shadow: 0 -1px 1px rgba(0,0,0,0.4);
        box-shadow: 0 2px 5px rgba(217, 119, 6, 0.25), inset 0 1px 0 rgba(255,255,255,0.5);
    }}

    .btn-gold:hover {{
        background: linear-gradient(to bottom, #fef3c7 0%, #f59e0b 40%, #b45309 100%);
        box-shadow: 0 4px 10px rgba(217, 119, 6, 0.35);
        color: #ffffff !important;
    }}

    .btn-dark {{
        background: linear-gradient(to bottom, #475569 0%, #1e293b 60%, #0f172a 100%);
        border: 1px solid #020617;
        color: #ffffff !important;
        text-shadow: 0 -1px 1px rgba(0,0,0,0.6);
    }}

    /* --- CONTENT WRAPPER --- */
    .content-wrapper {{
        max-width: 1240px;
        width: 100%;
        margin: 0 auto;
        padding: 24px 20px 60px 20px;
        display: flex;
        flex-direction: column;
        gap: 32px;
    }}

    /* --- HERO BANNER --- */
    .hero-banner {{
        background: linear-gradient(135deg, var(--theme-dark) 0%, var(--theme-primary) 50%, var(--theme-deep) 100%);
        border: 1px solid var(--theme-border);
        border-radius: 12px;
        padding: 36px 32px;
        position: relative;
        overflow: hidden;
        color: #ffffff;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2), inset 0 1px 0 rgba(255,255,255,0.3);
    }}

    .hero-banner::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; height: 50%;
        background: linear-gradient(to bottom, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 100%);
        pointer-events: none;
    }}

    .hero-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: bold;
        letter-spacing: 0.8px;
        text-transform: uppercase;
        margin-bottom: 12px;
        backdrop-filter: blur(4px);
    }}

    .hero-title {{
        font-size: 2.3rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 8px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.4);
    }}

    .hero-sub {{
        font-size: 1.05rem;
        color: rgba(255, 255, 255, 0.9);
        max-width: 860px;
        margin-bottom: 24px;
        text-shadow: 0 1px 2px rgba(0,0,0,0.3);
    }}

    /* --- FILTER BAR & PILLS --- */
    .filter-section {{
        display: flex;
        flex-direction: column;
        gap: 16px;
    }}

    .search-box-wrap {{
        position: relative;
        width: 100%;
    }}

    .search-input {{
        width: 100%;
        padding: 14px 20px 14px 44px;
        border-radius: 8px;
        border: 1px solid #cbd5e1;
        font-size: 0.95rem;
        font-family: inherit;
        background: #ffffff;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05), inset 0 1px 2px rgba(0,0,0,0.05);
        outline: none;
        transition: all 0.2s ease;
    }}

    .search-input:focus {{
        border-color: var(--theme-light);
        box-shadow: 0 0 0 3px var(--theme-pale), 0 2px 6px rgba(0,0,0,0.08);
    }}

    .search-icon-pos {{
        position: absolute;
        left: 16px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 1.1rem;
        color: #94a3b8;
    }}

    .jump-pills-row {{
        display: flex;
        gap: 10px;
        flex-wrap: wrap;
    }}

    .jump-pill {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 7px 15px;
        border-radius: 20px;
        background: #ffffff;
        border: 1px solid #cbd5e1;
        font-size: 0.82rem;
        font-weight: bold;
        color: var(--text-dark);
        text-decoration: none;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        transition: all 0.2s ease;
        cursor: pointer;
    }}

    .jump-pill:hover {{
        background: var(--theme-pale);
        border-color: var(--theme-border);
        color: var(--theme-primary);
        transform: translateY(-1px);
    }}

    .jump-pill.active {{
        background: var(--theme-primary);
        color: #ffffff;
        border-color: var(--theme-deep);
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.25);
    }}

    /* --- DEPARTMENT CONTAINER --- */
    .dept-card {{
        background: var(--card-bg);
        border: 1px solid var(--border-panel);
        border-radius: 12px;
        padding: 30px;
        box-shadow: var(--shadow-gloss);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        display: flex;
        flex-direction: column;
        gap: 22px;
        transition: all 0.25s ease;
        position: relative;
    }}

    .dept-card:hover {{
        border-color: var(--theme-border);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1), inset 0 1px 0 #ffffff;
    }}

    .dept-header {{
        display: flex;
        flex-direction: column;
        gap: 8px;
        border-bottom: 2px solid var(--theme-pale);
        padding-bottom: 18px;
    }}

    .dept-badge-row {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 8px;
    }}

    .dept-badge {{
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 3px 10px;
        border-radius: 12px;
        font-size: 0.72rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        background: var(--theme-pale);
        color: var(--theme-primary);
        border: 1px solid var(--theme-border);
    }}

    .dept-title {{
        font-size: 1.65rem;
        font-weight: 800;
        color: var(--theme-deep);
        line-height: 1.25;
    }}

    .mandate-box {{
        background: linear-gradient(to right, #f8fafc 0%, #ffffff 100%);
        border-left: 4px solid var(--theme-primary);
        border-top: 1px solid #e2e8f0;
        border-right: 1px solid #e2e8f0;
        border-bottom: 1px solid #e2e8f0;
        border-radius: 0 8px 8px 0;
        padding: 16px 20px;
        display: flex;
        flex-direction: column;
        gap: 6px;
    }}

    .mandate-label {{
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        color: var(--theme-primary);
        display: flex;
        align-items: center;
        gap: 6px;
    }}

    .mandate-text {{
        font-size: 0.95rem;
        color: var(--text-dark);
        line-height: 1.55;
    }}

    /* --- FUNCTIONS GRID --- */
    .functions-header {{
        font-size: 0.85rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0.6px;
        color: var(--text-muted);
        display: flex;
        align-items: center;
        gap: 6px;
    }}

    .functions-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
        gap: 20px;
    }}

    .function-card {{
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 22px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        gap: 16px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.04);
        transition: all 0.2s ease;
        position: relative;
        overflow: hidden;
    }}

    .function-card:hover {{
        border-color: var(--theme-border);
        box-shadow: 0 6px 16px rgba(0,0,0,0.08);
        transform: translateY(-2px);
    }}

    .function-card::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; height: 3px;
        background: linear-gradient(to right, var(--theme-primary), var(--theme-light));
        opacity: 0;
        transition: opacity 0.2s ease;
    }}

    .function-card:hover::before {{ opacity: 1; }}

    .func-top {{
        display: flex;
        gap: 14px;
        align-items: flex-start;
    }}

    .func-icon-wrap {{
        font-size: 1.8rem;
        width: 48px;
        height: 48px;
        flex-shrink: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        background: var(--theme-pale);
        border: 1px solid var(--theme-border);
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.8);
    }}

    .func-info {{
        display: flex;
        flex-direction: column;
        gap: 6px;
    }}

    .func-title {{
        font-size: 1.05rem;
        font-weight: 700;
        color: var(--theme-deep);
        line-height: 1.3;
    }}

    .func-desc {{
        font-size: 0.88rem;
        color: var(--text-muted);
        line-height: 1.5;
    }}

    /* --- FOOTER --- */
    .page-footer {{
        width: 100%;
        background: linear-gradient(to bottom, #1e293b 0%, #0f172a 100%);
        color: #94a3b8;
        padding: 32px 20px;
        border-top: 1px solid #334155;
        font-size: 0.85rem;
        text-align: center;
        margin-top: 40px;
    }}

    .footer-content {{
        max-width: 900px;
        margin: 0 auto;
        display: flex;
        flex-direction: column;
        gap: 8px;
    }}

    /* --- SKEUOMORPHIC MODAL SYSTEM --- */
    .modal-overlay {{
        position: fixed;
        inset: 0;
        background: rgba(15, 23, 42, 0.72);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        display: none;
        align-items: center;
        justify-content: center;
        z-index: 10000;
        padding: 16px;
        opacity: 0;
        transition: opacity 0.2s ease;
    }}

    .modal-overlay.active {{
        display: flex;
        opacity: 1;
    }}

    .modal-window {{
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-radius: 12px;
        width: 100%;
        max-width: 660px;
        max-height: 90vh;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.45), inset 0 1px 0 #ffffff;
        transform: scale(0.96);
        transition: transform 0.2s ease;
    }}

    .modal-overlay.active .modal-window {{
        transform: scale(1);
    }}

    .modal-header {{
        background: linear-gradient(135deg, var(--theme-dark) 0%, var(--theme-primary) 100%);
        color: #ffffff;
        padding: 18px 24px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: relative;
        border-bottom: 1px solid var(--theme-deep);
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.3);
    }}

    .modal-header-info {{
        display: flex;
        align-items: center;
        gap: 12px;
    }}

    .modal-header-icon {{
        font-size: 1.6rem;
    }}

    .modal-header-title {{
        font-size: 1.15rem;
        font-weight: 700;
        line-height: 1.2;
    }}

    .modal-close-btn {{
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.3);
        color: #ffffff;
        width: 32px;
        height: 32px;
        border-radius: 6px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.2s ease;
    }}

    .modal-close-btn:hover {{
        background: rgba(255, 255, 255, 0.3);
        transform: scale(1.05);
    }}

    .modal-body {{
        padding: 24px;
        overflow-y: auto;
        display: flex;
        flex-direction: column;
        gap: 20px;
    }}

    .form-group {{
        display: flex;
        flex-direction: column;
        gap: 6px;
    }}

    .form-label {{
        font-size: 0.85rem;
        font-weight: 700;
        color: var(--text-dark);
    }}

    .form-input, .form-select, .form-textarea {{
        width: 100%;
        padding: 10px 14px;
        border-radius: 6px;
        border: 1px solid #cbd5e1;
        font-family: inherit;
        font-size: 0.92rem;
        background: #f8fafc;
        box-shadow: inset 0 1px 2px rgba(0,0,0,0.05);
        outline: none;
        transition: all 0.2s ease;
    }}

    .form-input:focus, .form-select:focus, .form-textarea:focus {{
        background: #ffffff;
        border-color: var(--theme-light);
        box-shadow: 0 0 0 3px var(--theme-pale);
    }}

    .form-textarea {{
        min-height: 90px;
        resize: vertical;
    }}

    .modal-telemetry-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 14px;
    }}

    .telemetry-card {{
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 14px;
        display: flex;
        flex-direction: column;
        gap: 4px;
        border-left: 3px solid var(--theme-primary);
    }}

    .telemetry-name {{
        font-size: 0.8rem;
        color: var(--text-muted);
        font-weight: bold;
        text-transform: uppercase;
    }}

    .telemetry-val {{
        font-size: 1.35rem;
        font-weight: 800;
        color: var(--theme-deep);
    }}

    .telemetry-sub {{
        font-size: 0.75rem;
        color: #64748b;
    }}

    .modal-results-box {{
        background: #f1f5f9;
        border: 1px solid #cbd5e1;
        border-radius: 8px;
        padding: 18px;
        display: none;
        flex-direction: column;
        gap: 12px;
        animation: fadeIn 0.3s ease;
    }}

    .modal-results-box.active {{
        display: flex;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(4px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    .verified-banner {{
        background: linear-gradient(to right, #065f46, #047857);
        color: #ffffff;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.8px;
        padding: 6px 12px;
        border-radius: 4px;
        text-align: center;
        text-transform: uppercase;
        box-shadow: 0 1px 3px rgba(0,0,0,0.15);
    }}

    .result-token-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.85rem;
        padding-bottom: 8px;
        border-bottom: 1px dashed #cbd5e1;
    }}

    .token-hash {{
        font-family: 'Courier New', monospace;
        font-weight: bold;
        color: var(--theme-deep);
        background: #ffffff;
        padding: 2px 8px;
        border-radius: 4px;
        border: 1px solid #cbd5e1;
    }}

    .modal-footer {{
        background: #f8fafc;
        border-top: 1px solid #e2e8f0;
        padding: 14px 24px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        gap: 12px;
    }}

    @media (max-width: 768px) {{
        .hero-title {{ font-size: 1.7rem; }}
        .dept-title {{ font-size: 1.35rem; }}
        .functions-grid {{ grid-template-columns: 1fr; }}
        .content-wrapper {{ padding: 16px 12px 40px 12px; }}
        .dept-card {{ padding: 20px 16px; }}
    }}
    """

print("Added get_page_css to generator.")

def get_page_js(lang, ui):
    return f"""
    // Client-side Interactive Engine
    document.addEventListener('DOMContentLoaded', () => {{
        const modalOverlay = document.getElementById('interactive-modal-overlay');
        const modalWindow = document.getElementById('interactive-modal-window');
        const modalCloseBtn = document.getElementById('modal-close-btn');
        const modalCancelBtn = document.getElementById('modal-cancel-btn');
        const modalActionBtn = document.getElementById('modal-action-btn');
        const modalIcon = document.getElementById('modal-icon');
        const modalTitle = document.getElementById('modal-title');
        const modalDynamicFields = document.getElementById('modal-dynamic-fields');
        const modalResultsBox = document.getElementById('modal-results-box');
        const searchInput = document.getElementById('dept-search-input');
        const jumpPills = document.querySelectorAll('.jump-pill');

        let activeModalConfig = null;
        let activeModalId = null;

        // Instant Page Search Filter
        if (searchInput) {{
            searchInput.addEventListener('input', (e) => {{
                const q = e.target.value.toLowerCase().trim();
                const deptCards = document.querySelectorAll('.dept-card');

                deptCards.forEach(card => {{
                    const deptText = card.innerText.toLowerCase();
                    if (!q || deptText.includes(q)) {{
                        card.style.display = 'flex';
                        // Filter individual function cards
                        const funcCards = card.querySelectorAll('.function-card');
                        funcCards.forEach(fc => {{
                            if (!q || fc.innerText.toLowerCase().includes(q)) {{
                                fc.style.display = 'flex';
                            }} else {{
                                fc.style.display = 'none';
                            }}
                        }});
                    }} else {{
                        card.style.display = 'none';
                    }}
                }});
            }});
        }}

        // Jump Pill Smooth Scroll
        jumpPills.forEach(pill => {{
            pill.addEventListener('click', (e) => {{
                const targetId = pill.getAttribute('data-target');
                if (targetId === 'all') {{
                    window.scrollTo({{ top: 0, behavior: 'smooth' }});
                    return;
                }}
                const targetEl = document.getElementById(targetId);
                if (targetEl) {{
                    targetEl.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                    targetEl.style.outline = '3px solid var(--theme-light)';
                    setTimeout(() => {{
                        targetEl.style.outline = 'none';
                    }}, 1500);
                }}
            }});
        }});

        // Open Modal Engine
        function openModal(modalId) {{
            const cfg = MODAL_CONFIGS[modalId];
            if (!cfg) return;

            activeModalId = modalId;
            activeModalConfig = cfg;

            // Reset modal state
            modalResultsBox.classList.remove('active');
            modalResultsBox.innerHTML = '';
            modalDynamicFields.innerHTML = '';

            modalIcon.textContent = cfg.icon || '🏛️';
            modalTitle.textContent = CURRENT_LANG === 'sgn' ? (cfg.title_sgn || cfg.title_en) : cfg.title_en;
            modalActionBtn.textContent = CURRENT_LANG === 'sgn' ? (cfg.action_sgn || cfg.action_en) : cfg.action_en;

            // Render form / fields based on type
            if (cfg.fields && cfg.fields.length > 0) {{
                cfg.fields.forEach(f => {{
                    const group = document.createElement('div');
                    group.className = 'form-group';

                    const label = document.createElement('label');
                    label.className = 'form-label';
                    label.textContent = CURRENT_LANG === 'sgn' ? (f.label_sgn || f.label_en) : f.label_en;
                    group.appendChild(label);

                    if (f.type === 'select') {{
                        const select = document.createElement('select');
                        select.className = 'form-select';
                        select.id = `input-${{f.name}}`;
                        f.options.forEach(opt => {{
                            const option = document.createElement('option');
                            option.value = opt.val;
                            option.textContent = CURRENT_LANG === 'sgn' ? (opt.sgn || opt.en) : opt.en;
                            select.appendChild(option);
                        }});
                        group.appendChild(select);
                    }} else if (f.type === 'textarea') {{
                        const ta = document.createElement('textarea');
                        ta.className = 'form-textarea';
                        ta.id = `input-${{f.name}}`;
                        ta.placeholder = CURRENT_LANG === 'sgn' ? (f.placeholder_sgn || f.placeholder_en || '') : (f.placeholder_en || '');
                        group.appendChild(ta);
                    }} else {{
                        const input = document.createElement('input');
                        input.type = f.type || 'text';
                        input.className = 'form-input';
                        input.id = `input-${{f.name}}`;
                        if (f.default !== undefined) input.value = f.default;
                        input.placeholder = CURRENT_LANG === 'sgn' ? (f.placeholder_sgn || f.placeholder_en || '') : (f.placeholder_en || '');
                        group.appendChild(input);
                    }}

                    modalDynamicFields.appendChild(group);
                }});
            }}

            // Render telemetry metrics if applicable
            if (cfg.metrics && cfg.metrics.length > 0) {{
                const grid = document.createElement('div');
                grid.className = 'modal-telemetry-grid';
                cfg.metrics.forEach(m => {{
                    const card = document.createElement('div');
                    card.className = 'telemetry-card';
                    card.innerHTML = `
                        <div class="telemetry-name">${{CURRENT_LANG === 'sgn' ? (m.name_sgn || m.name_en) : m.name_en}}</div>
                        <div class="telemetry-val">${{m.val}}</div>
                        <div class="telemetry-sub">${{CURRENT_LANG === 'sgn' ? (m.sub_sgn || m.sub_en) : m.sub_en}}</div>
                    `;
                    grid.appendChild(card);
                }});
                modalDynamicFields.appendChild(grid);
            }}

            // Render channels if media type
            if (cfg.channels && cfg.channels.length > 0) {{
                const chanGrid = document.createElement('div');
                chanGrid.style.display = 'flex';
                chanGrid.style.flexDirection = 'column';
                chanGrid.style.gap = '12px';
                cfg.channels.forEach(ch => {{
                    const card = document.createElement('div');
                    card.className = 'telemetry-card';
                    card.style.borderLeftColor = '#f97316';
                    card.innerHTML = `
                        <div style="display:flex; justify-content:space-between; align-items:center;">
                            <strong style="color:var(--theme-deep);">${{CURRENT_LANG === 'sgn' ? ch.name_sgn : ch.name_en}}</strong>
                            <span style="font-size:0.75rem; background:#fed7aa; color:#9a3412; padding:2px 8px; border-radius:12px; font-weight:bold;">${{ch.stream_status}}</span>
                        </div>
                        <p style="font-size:0.85rem; color:#475569; margin-top:4px;">${{CURRENT_LANG === 'sgn' ? ch.desc_sgn : ch.desc_en}}</p>
                    `;
                    chanGrid.appendChild(card);
                }});
                modalDynamicFields.appendChild(chanGrid);
            }}

            modalOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        }}

        function closeModal() {{
            modalOverlay.classList.remove('active');
            document.body.style.overflow = '';
            activeModalConfig = null;
            activeModalId = null;
        }}

        // Attach Click to all action buttons on page
        document.querySelectorAll('.open-modal-btn').forEach(btn => {{
            btn.addEventListener('click', () => {{
                const modalId = btn.getAttribute('data-modal');
                if (modalId) openModal(modalId);
            }});
        }});

        if (modalCloseBtn) modalCloseBtn.addEventListener('click', closeModal);
        if (modalCancelBtn) modalCancelBtn.addEventListener('click', closeModal);
        modalOverlay.addEventListener('click', (e) => {{
            if (e.target === modalOverlay) closeModal();
        }});

        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {{
                closeModal();
            }}
        }});

        // Action Button Execution Handler
        if (modalActionBtn) {{
            modalActionBtn.addEventListener('click', () => {{
                if (!activeModalConfig) return;
                const cfg = activeModalConfig;

                const token = `${{cfg.token_prefix || 'SNG-SOV'}}-2026-${{Math.floor(10000 + Math.random() * 90000)}}`;
                const now = new Date().toISOString().replace('T', ' ').substring(0, 19) + ' UTC';

                let customOutput = '';

                // Custom Calculation Engine
                if (cfg.type === 'calc') {{
                    if (activeModalId === 'taxcalc') {{
                        const incEl = document.getElementById('input-income');
                        const income = incEl ? parseFloat(incEl.value) || 48000 : 48000;
                        const baseTax = income * 0.10;
                        const progTax = income > 60000 ? (income - 60000) * 0.05 : 0;
                        const totalTax = baseTax + progTax;
                        const netPay = income - totalTax;
                        customOutput = `
                            <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:12px; font-size:0.88rem; display:flex; flex-direction:column; gap:4px;">
                                <div><strong>${{CURRENT_LANG === 'sgn' ? 'Гросо Инкомо' : 'Gross Annual Income'}}:</strong> $ ${{income.toLocaleString()}}</div>
                                <div><strong>${{CURRENT_LANG === 'sgn' ? 'Базо Такса (10%)' : 'Base Statutory Tax (10%)'}}:</strong> $ ${{baseTax.toLocaleString()}}</div>
                                <div><strong>${{CURRENT_LANG === 'sgn' ? 'Солидарито Леви' : 'Solidarity Levy'}}:</strong> $ 0.00 (Zero Deficit Rule)</div>
                                <div style="border-top:1px dashed #cbd5e1; margin-top:4px; padding-top:4px; color:var(--theme-primary); font-weight:bold;">
                                    ${{CURRENT_LANG === 'sgn' ? 'Нэтоо Саларио' : 'Net Take-Home'}}: $ ${{netPay.toLocaleString()}}
                                </div>
                            </div>
                        `;
                    }} else if (activeModalId === 'unemployment') {{
                        const wageEl = document.getElementById('input-last_wage');
                        const wage = wageEl ? parseFloat(wageEl.value) || 3600 : 3600;
                        const stipend = Math.min(wage * 0.82, 3200);
                        customOutput = `
                            <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:12px; font-size:0.88rem;">
                                <strong>${{CURRENT_LANG === 'sgn' ? 'Гарантадо Менсио Стипэнд' : 'Statutory Guaranteed Monthly Stipend'}}:</strong> 
                                <span style="font-size:1.1rem; color:#15803d; font-weight:bold;">$ ${{stipend.toFixed(2)}} / mo</span>
                                <div style="font-size:0.75rem; color:#64748b; margin-top:4px;">${{CURRENT_LANG === 'sgn' ? '100% покритие на медицински услуги включено' : '100% universal healthcare and transit pass included.'}}</div>
                            </div>
                        `;
                    }} else if (activeModalId === 'tariffcalc') {{
                        const valEl = document.getElementById('input-cif_value');
                        const val = valEl ? parseFloat(valEl.value) || 10000 : 10000;
                        customOutput = `
                            <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:12px; font-size:0.88rem;">
                                <strong>${{CURRENT_LANG === 'sgn' ? 'Мито & Тарифо' : 'Calculated Import Duty'}}:</strong> 
                                <span style="font-size:1.1rem; color:#15803d; font-weight:bold;">$ 0.00</span>
                                <div style="font-size:0.75rem; color:#64748b; margin-top:4px;">${{CURRENT_LANG === 'sgn' ? '0% тарифо съгласно Конституция на Сангайа' : 'Eligible for 0% statutory clean transit / essential good exemption.'}}</div>
                            </div>
                        `;
                    }} else if (activeModalId === 'visacheck') {{
                        customOutput = `
                            <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:12px; font-size:0.88rem;">
                                <strong>${{CURRENT_LANG === 'sgn' ? 'Виса Квалификатио' : 'Visa Qualification Standing'}}:</strong> 
                                <span style="font-size:1.1rem; color:#15803d; font-weight:bold;">CLASS A PRIORITY</span>
                                <div style="font-size:0.75rem; color:#64748b; margin-top:4px;">${{CURRENT_LANG === 'sgn' ? 'Квалифициран за незабавно пребиваване' : 'Qualified for streamlined 14-day residency clearance with full labor rights.'}}</div>
                            </div>
                        `;
                    }} else if (activeModalId === 'debtcalc') {{
                        customOutput = `
                            <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:12px; font-size:0.88rem;">
                                <strong>${{CURRENT_LANG === 'sgn' ? 'Лихва (Интересо)' : 'Statutory Interest Rate'}}:</strong> 
                                <span style="font-size:1.1rem; color:#15803d; font-weight:bold;">0.00% (Article V Cap)</span>
                                <div style="font-size:0.75rem; color:#64748b; margin-top:4px;">${{CURRENT_LANG === 'sgn' ? 'Месечна вноска: $ 120.00 фиксирана' : 'Monthly income-contingent paydown: $ 120.00 fixed, zero interest compounding.'}}</div>
                            </div>
                        `;
                    }}
                }}

                // Search Results Simulation
                if (cfg.type === 'search') {{
                    const sampleList = CURRENT_LANG === 'sgn' ? (cfg.sample_results_sgn || cfg.sample_results_en) : cfg.sample_results_en;
                    if (sampleList && sampleList.length > 0) {{
                        let resHtml = '<div style="display:flex; flex-direction:column; gap:8px;">';
                        sampleList.forEach(s => {{
                            resHtml += `
                                <div style="background:#ffffff; border:1px solid #cbd5e1; border-radius:6px; padding:10px; font-size:0.85rem;">
                                    <div style="display:flex; justify-content:space-between; font-weight:bold; color:var(--theme-deep);">
                                        <span>${{s.title}}</span>
                                        <span style="font-size:0.75rem; color:#64748b;">${{s.date}}</span>
                                    </div>
                                    <p style="color:#475569; font-size:0.8rem; margin-top:4px;">${{s.desc}}</p>
                                </div>
                            `;
                        }});
                        resHtml += '</div>';
                        customOutput = resHtml;
                    }}
                }}

                modalResultsBox.innerHTML = `
                    <div class="verified-banner">${{CURRENT_LANG === 'sgn' ? 'КРИПТОГРАФИКО ВЭРИФИКАДО • САНГАЙА СУВЭРЭНО ЛЕДЖЕР' : 'CRYPTOGRAPHICALLY VERIFIED • SANGAIA SOVEREIGN LEDGER'}}</div>
                    <div class="result-token-row">
                        <span>${{CURRENT_LANG === 'sgn' ? 'Вэрификатио Докэто ИД' : 'Verification Docket ID'}}:</span>
                        <span class="token-hash">${{token}}</span>
                    </div>
                    <div class="result-token-row">
                        <span>${{CURRENT_LANG === 'sgn' ? 'Тэмпоро-Нота' : 'Timestamp'}}:</span>
                        <span>${{now}}</span>
                    </div>
                    <div class="result-token-row">
                        <span>${{CURRENT_LANG === 'sgn' ? 'Статуто' : 'Status'}}:</span>
                        <span style="color:#15803d; font-weight:bold;">${{CURRENT_LANG === 'sgn' ? 'ПРОЦЕСАДО & ЗАПИСАДО' : 'PROCESSED & RECORDED'}}</span>
                    </div>
                    ${{customOutput}}
                    <div style="display:flex; gap:10px; justify-content:flex-end; margin-top:6px;">
                        <button class="sangaia-btn" onclick="alert('${{CURRENT_LANG === 'sgn' ? 'Сувэрэно докэто е запазен локално.' : 'Official sovereign receipt saved to your Sangaia ID keychain.'}}')">
                            <span>📥 ${{CURRENT_LANG === 'sgn' ? 'Дэскарго Рэцэпто' : 'Download Sovereign Receipt'}}</span>
                        </button>
                    </div>
                `;
                modalResultsBox.classList.add('active');
                modalResultsBox.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
            }});
        }}
    }});
    """

print("Added get_page_js to generator.")

def render_department_html(ministry, lang="en", is_subdomain=True, is_sgn_dir=False):
    ui = UI_STRINGS[lang]
    theme = ministry["theme"]
    slug = ministry["slug"]

    page_title = f"{ministry['title_en'] if lang == 'en' else ministry['title_sgn']} - {ministry['ministry_en'] if lang == 'en' else ministry['ministry_sgn']} - {ui['title_suffix']}"
    
    # Path resolution
    if is_subdomain:
        if is_sgn_dir:
            home_href = "index.html"
            dept_href = "departments.html"
            switch_href = "../departments.html"
            switch_label = "ENGLISH (EN)"
            logo_src = "../../media/nav_logo.png"
            logo_fallback = "../media/nav_logo.png"
        else:
            home_href = "index.html"
            dept_href = "departments.html"
            switch_href = "sgn/departments.html"
            switch_label = "САНГАЙА (SGN)"
            logo_src = "../media/nav_logo.png"
            logo_fallback = "media/nav_logo.png"
        id_href = "https://sangaia.org/id.html"
        services_href = "https://sangaia.org/services.html"
    else:
        # Root files
        if is_sgn_dir:
            home_href = f"{slug}.html" if slug != "healthcare" else "services.html"
            dept_href = f"{slug}_departments.html"
            switch_href = f"../{slug}_departments.html"
            switch_label = "ENGLISH (EN)"
            logo_src = "../media/nav_logo.png"
            logo_fallback = "nav_logo.png"
            id_href = "id.html"
            services_href = "services.html"
        else:
            home_href = f"{slug}.html" if slug != "healthcare" else "services.html"
            dept_href = f"{slug}_departments.html"
            switch_href = f"sgn/{slug}_departments.html"
            switch_label = "САНГАЙА (SGN)"
            logo_src = "media/nav_logo.png"
            logo_fallback = "nav_logo.png"
            id_href = "id.html"
            services_href = "services.html"

    # Jump Pills HTML
    pills_html = f'<button class="jump-pill active" data-target="all">🏛️ {ui["filter_all"]}</button>'
    for d in ministry["departments"]:
        d_name = d["name_en"] if lang == "en" else d["name_sgn"]
        pills_html += f'<button class="jump-pill" data-target="{d["id"]}">🏢 {d_name}</button>'

    # Departments HTML
    depts_html = ""
    for d in ministry["departments"]:
        d_name = d["name_en"] if lang == "en" else d["name_sgn"]
        d_mandate = d["mandate_en"] if lang == "en" else d["mandate_sgn"]

        funcs_html = ""
        for f in d["functions"]:
            f_title = f["title_en"] if lang == "en" else f["title_sgn"]
            f_desc = f["desc_en"] if lang == "en" else f["desc_sgn"]
            f_action = f["action_en"] if lang == "en" else f["action_sgn"]

            funcs_html += f"""
                <div class="function-card">
                    <div class="func-top">
                        <div class="func-icon-wrap">{f.get('icon', '⚙️')}</div>
                        <div class="func-info">
                            <h3 class="func-title">{f_title}</h3>
                            <p class="func-desc">{f_desc}</p>
                        </div>
                    </div>
                    <button class="sangaia-btn btn-theme open-modal-btn" data-modal="{f['modal']}">
                        <span>{f.get('icon', '⚙️')} {f_action} &rarr;</span>
                    </button>
                </div>
            """

        depts_html += f"""
            <section class="dept-card" id="{d['id']}">
                <div class="dept-header">
                    <div class="dept-badge-row">
                        <span class="dept-badge">🏛️ {ui['dept_badge']}</span>
                        <a href="#overview" class="jump-pill" style="font-size:0.75rem; padding:3px 10px;">↑ Top</a>
                    </div>
                    <h2 class="dept-title">{d_name}</h2>
                </div>
                <div class="mandate-box">
                    <span class="mandate-label">🛡️ {ui['mandate_label']}</span>
                    <p class="mandate-text">{d_mandate}</p>
                </div>
                <div class="functions-header">⚙️ {ui['functions_label']}</div>
                <div class="functions-grid">
                    {funcs_html}
                </div>
            </section>
        """

    modal_configs_json = json.dumps(MODAL_CONFIGS)
    css_str = get_page_css(theme)
    js_str = get_page_js(lang, ui)

    return f"""<!DOCTYPE html>
<html lang="{ 'cu' if lang == 'sgn' else 'en' }">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    <style>
{css_str}
    </style>
</head>
<body>

<div class="main-container">

    <!-- GLOBAL METAL HEADER -->
    <nav id="globalheader">
        <div style="position: absolute; left: 15px; display: flex; align-items: center; height: 100%;">
            <a href="https://sangaia.org/index.html">
                <img src="{logo_src}" onerror="this.onerror=null; this.src='{logo_fallback}';" style="height: 22px; width: auto;" alt="Sangaia Logo">
            </a>
        </div>
        <div style="position: absolute; right: 15px; display: flex; align-items: center; gap: 12px; height: 100%; z-index: 100;">
            <div id="auth-widget">
                <a href="{id_href}" style="color: #bbb; text-decoration: none; font-size: 11px; font-weight: bold; letter-spacing: 0.5px; padding: 3px 8px; border: 1px solid #444; border-radius: 4px; background: linear-gradient(to bottom, #555, #333); box-shadow: 0 1px 2px rgba(0,0,0,0.3); transition: all 0.2s ease;">{ui['sangaia_id']}</a>
            </div>
            <a href="{switch_href}" style="color: #bbb; text-decoration: none; font-size: 11px; font-weight: bold; letter-spacing: 0.5px; padding: 3px 8px; border: 1px solid #444; border-radius: 4px; background: linear-gradient(to bottom, #555, #333); box-shadow: 0 1px 2px rgba(0,0,0,0.3); transition: all 0.2s ease;">{switch_label}</a>
        </div>
        <ul id="globalnav">
            <li><a href="{home_href}">{ui['home']}</a></li>
            <li><a href="{dept_href}" class="active">{ui['departments']}</a></li>
            <li><a href="{services_href}">{ui['services']}</a></li>
            <li><a href="{id_href}">{ui['sangaia_id']}</a></li>
        </ul>
    </nav>

    <div class="content-wrapper">

        <!-- HERO BANNER -->
        <header class="hero-banner" id="overview">
            <span class="hero-badge">🏛️ {ui['hero_badge']}</span>
            <h1 class="hero-title">{ministry['ministry_en'] if lang == 'en' else ministry['ministry_sgn']}</h1>
            <p class="hero-sub">{ui['hero_sub']}</p>

            <div class="filter-section">
                <div class="search-box-wrap">
                    <span class="search-icon-pos">🔍</span>
                    <input type="text" class="search-input" id="dept-search-input" placeholder="{ui['search_placeholder']}">
                </div>
                <div class="jump-pills-row">
                    {pills_html}
                </div>
            </div>
        </header>

        <!-- DEPARTMENTS LIST -->
        {depts_html}

    </div>

    <!-- SKEUOMORPHIC FOOTER -->
    <footer class="page-footer">
        <div class="footer-content">
            <p>{ui['footer_text']}</p>
            <p style="font-size:0.75rem; color:#64748b;">{ui['footer_sub']}</p>
        </div>
    </footer>

</div>

<!-- INTERACTIVE MODAL OVERLAY -->
<div class="modal-overlay" id="interactive-modal-overlay">
    <div class="modal-window" id="interactive-modal-window">
        <div class="modal-header">
            <div class="modal-header-info">
                <span class="modal-header-icon" id="modal-icon">🏛️</span>
                <span class="modal-header-title" id="modal-title">Interactive Service</span>
            </div>
            <button class="modal-close-btn" id="modal-close-btn">&times;</button>
        </div>
        <div class="modal-body">
            <div id="modal-dynamic-fields" style="display:flex; flex-direction:column; gap:16px;"></div>
            <div class="modal-results-box" id="modal-results-box"></div>
        </div>
        <div class="modal-footer">
            <button class="sangaia-btn" id="modal-cancel-btn">{ui['close']}</button>
            <button class="sangaia-btn btn-theme" id="modal-action-btn">{ui['submit']}</button>
        </div>
    </div>
</div>

<script>
const CURRENT_LANG = "{lang}";
const MODAL_CONFIGS = {modal_configs_json};

{js_str}
</script>

</body>
</html>
"""

def generate_all_department_portals():
    print("Beginning generation of all 9 Ministries department portals...")
    count = 0

    for key, ministry in MINISTRIES.items():
        print(f"\nProcessing {ministry['ministry_en']} ({key})...")

        # 1. Subdomain Targets
        for target_dir in ministry.get("target_dirs", []):
            dir_path = os.path.join(BASE_DIR, target_dir)
            if not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)

            # English Subdomain file
            en_file = os.path.join(dir_path, "departments.html")
            en_html = render_department_html(ministry, lang="en", is_subdomain=True, is_sgn_dir=False)
            with open(en_file, "w", encoding="utf-8") as f:
                f.write(en_html)
            print(f"  [OK] Wrote: {en_file}")
            count += 1

            # Sangaian Subdomain file
            sgn_dir = os.path.join(dir_path, "sgn")
            os.makedirs(sgn_dir, exist_ok=True)
            sgn_file = os.path.join(sgn_dir, "departments.html")
            sgn_html = render_department_html(ministry, lang="sgn", is_subdomain=True, is_sgn_dir=True)
            with open(sgn_file, "w", encoding="utf-8") as f:
                f.write(sgn_html)
            print(f"  [OK] Wrote: {sgn_file}")
            count += 1

        # 2. Root Files
        root_file = ministry.get("root_file")
        if root_file:
            root_path = os.path.join(BASE_DIR, root_file)
            root_html = render_department_html(ministry, lang="en", is_subdomain=False, is_sgn_dir=False)
            with open(root_path, "w", encoding="utf-8") as f:
                f.write(root_html)
            print(f"  [OK] Wrote Root EN: {root_path}")
            count += 1

        root_sgn = ministry.get("root_sgn_file")
        if root_sgn:
            root_sgn_path = os.path.join(BASE_DIR, root_sgn)
            os.makedirs(os.path.dirname(root_sgn_path), exist_ok=True)
            root_sgn_html = render_department_html(ministry, lang="sgn", is_subdomain=False, is_sgn_dir=True)
            with open(root_sgn_path, "w", encoding="utf-8") as f:
                f.write(root_sgn_html)
            print(f"  [OK] Wrote Root SGN: {root_sgn_path}")
            count += 1

    print(f"\nSuccessfully generated {count} department portal files across all 9 ministries!")

if __name__ == "__main__":
    generate_all_department_portals()
