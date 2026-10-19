#!/usr/bin/env python3
"""
Sangaia Full Government Department Generator
Builds department portals for all 9 ministries in English and Sangaian Cyrillic.
"""

import os
import json

BASE = "/Users/jackdavenport/Sangaia"

MINISTRIES = {
    "executive": {
        "slug": "executive",
        "theme": {
            "name": "Ministry of the Executive",
            "primary": "#1e3a8a",
            "dark": "#0f172a",
            "deep": "#090d16",
            "light": "#3b82f6",
            "pale": "#eff6ff",
            "border": "#bfdbfe",
            "accent": "#d97706"
        },
        "title_en": "Departments & Executive Agencies",
        "title_sgn": "Дэпартамэнто & Эксэкуто Агэнциа",
        "ministry_en": "Ministry of the Executive",
        "ministry_sgn": "Министро эк свои Эксэкуто",
        "subdomain": "https://executive.sangaia.org",
        "target_dirs": ["MoEX", "mEx"],
        "root_file": "executive_departments.html",
        "root_sgn_file": "sgn/executive_departments.html",
        "departments": [
            {
                "id": "state-cabinet",
                "name_en": "Department of State & Department of the Cabinet",
                "name_sgn": "Дэпарто эк Стато & Дэпарто эк Кабино",
                "mandate_en": "Administering cabinet affairs, official state gazettes, executive decrees, and ceremonial protocols for foreign and domestic dignitaries.",
                "mandate_sgn": "Мануго кабино прагма, официало стато газэта, эксэкуто дэкрито, инкаи церемониало протоколо про дигнитаро.",
                "functions": [
                    {
                        "icon": "📜",
                        "title_en": "Executive Orders & Decrees Archive",
                        "title_sgn": "Эксэкуто Дэкрито & Ордо Архиво",
                        "desc_en": "Searchable, cryptographic full-text registry of all signed Aretocratic proclamations, cabinet minutes, and ministerial directives.",
                        "desc_sgn": "Скэро-гаранто криптографико архиво эк холо Арэтократико прокламатио инкаи кабино минютэ.",
                        "action_en": "Browse Official Gazette",
                        "action_sgn": "Визо Стато Газэта",
                        "modal": "gazette"
                    },
                    {
                        "icon": "📥",
                        "title_en": "Citizen Petition & Feedback Pipeline",
                        "title_sgn": "Цивикано Пэтитио & Рэспонсо Канало",
                        "desc_en": "Direct statutory submission channel for citizens to transmit grievances, policy feedback, or reform petitions to the cabinet.",
                        "desc_sgn": "Дирэкто канало про цивикано ад транзмито пэтитио, грава, инкаи рэформо пропоситио ад свои кабино.",
                        "action_en": "File Citizen Petition",
                        "action_sgn": "Субмито Пэтитио",
                        "modal": "petition"
                    },
                    {
                        "icon": "🏛️",
                        "title_en": "Ceremonial Protocol & State Dignitaries",
                        "title_sgn": "Церемониало Протоколо & Стато Дигнитаро",
                        "desc_en": "Official state guidelines governing diplomatic honors, provincial gubernatorial processions, and ceremonial state banquets.",
                        "desc_sgn": "Официало стато рэгла про дипломатико оноро, провиткия губэрнаторо просесио, инкаи сонит банкэто.",
                        "action_en": "View Protocol Manual",
                        "action_sgn": "Визо Протоколо Мануало",
                        "modal": "protocol"
                    }
                ]
            },
            {
                "id": "planning-coordination",
                "name_en": "Department of Planning & Department of Coordination",
                "name_sgn": "Дэпарто эк Планификатио & Дэпарто эк Координатио",
                "mandate_en": "Aligning multi-ministry policy goals, monitoring national performance metrics, and resolving cross-agency jurisdictional overlaps.",
                "mandate_sgn": "Хармонио мулти-министро политикиа голо, монито натио кпи тэлэмэтриа, инкаи рэзолво агэнциа диспуто.",
                "functions": [
                    {
                        "icon": "📊",
                        "title_en": "Interactive National Progress Dashboard",
                        "title_sgn": "Интэракто Натио Прогрэсо Табула",
                        "desc_en": "Real-time KPI telemetry monitoring healthcare capacity, renewable grid output, educational outcomes, and fiscal surplus.",
                        "desc_sgn": "Виво тэлэмэтриа супэр салутиа капасита, соларо рэти, эдукатио студио, инкаи фискало плус.",
                        "action_en": "Launch KPI Dashboard",
                        "action_sgn": "Лапидо КПИ Табула",
                        "modal": "kpi"
                    },
                    {
                        "icon": "📑",
                        "title_en": "Public Policy Whitepapers & Research",
                        "title_sgn": "Публико Политикиа Вайтпапэро & Инвэстиго",
                        "desc_en": "Peer-reviewed strategic frameworks on demographic resilience, climate adaptation, and long-range sovereign planning.",
                        "desc_sgn": "Стратэгико докумэнти супэр демографиа, клима адаптатио, инкаи сувэрэнита планификатио.",
                        "action_en": "Access Whitepapers",
                        "action_sgn": "Адито Вайтпапэро",
                        "modal": "whitepapers"
                    },
                    {
                        "icon": "🤝",
                        "title_en": "Cross-Agency Task Force Portal",
                        "title_sgn": "Интэр-Агэнциа Таск Форса Портало",
                        "desc_en": "Collaborative inter-ministerial task force pipeline uniting Work, Environment, and Treasury on complex infrastructure directives.",
                        "desc_sgn": "Мулти-министро портало куно Лаборо, Амбито, инкаи Аэрарио про комплексо инфраструктура.",
                        "action_en": "Task Force Access",
                        "action_sgn": "Таск Форса Портало",
                        "modal": "taskforce"
                    }
                ]
            }
        ]
    },

    "treasury": {
        "slug": "treasury",
        "theme": {
            "name": "Ministry of the Treasury",
            "primary": "#334155",
            "dark": "#1e293b",
            "deep": "#0f172a",
            "light": "#64748b",
            "pale": "#f1f5f9",
            "border": "#cbd5e1",
            "accent": "#10b981"
        },
        "title_en": "Departments of the Treasury",
        "title_sgn": "Дэпартамэнто эк Аэрарио",
        "ministry_en": "Ministry of the Treasury",
        "ministry_sgn": "Министриа эк Аэрарио",
        "subdomain": "https://treasury.sangaia.org",
        "target_dirs": ["mT"],
        "root_file": "treasury_departments.html",
        "root_sgn_file": "sgn/treasury_departments.html",
        "departments": [
            {
                "id": "taxation",
                "name_en": "Department of Taxation",
                "name_sgn": "Дэпарто эк Таксатио",
                "mandate_en": "Collecting federal taxes, managing audits, and enforcing fiscal compliance under a progressive, zero-corporate-lobby tax code.",
                "mandate_sgn": "Колго фэдэро таксо, мануго аудито, инкаи фортис фискало комплио суб прогрэсиво рэгла.",
                "functions": [
                    {
                        "icon": "🧮",
                        "title_en": "Interactive Individual & Corporate Tax Calculator",
                        "title_sgn": "Интэракто Таксо Калкулаторо",
                        "desc_en": "Calculate statutory income, land resource royalty, or progressive enterprise surcharge brackets in Sangaian Dollars.",
                        "desc_sgn": "Калкуло персоно инкаи комэрцио таксо суб Сангаиа Долларо нормо.",
                        "action_en": "Launch Tax Calculator",
                        "action_sgn": "Калкуло Таксо",
                        "modal": "taxcalc"
                    },
                    {
                        "icon": "📑",
                        "title_en": "Digital Tax Filing & Clearance Verification",
                        "title_sgn": "Дигитало Таксо Филинг & Кларансо",
                        "desc_en": "Submit Form A-Tax electronic returns or verify immediate tax compliance certificate status using your Sangaia ID.",
                        "desc_sgn": "Субмито Форм А-Таксо вэл вэрифико кларансо статус куно Сангаиа ИД.",
                        "action_en": "Verify Clearance / File",
                        "action_sgn": "Вэрифико / Филинг",
                        "modal": "taxfile"
                    },
                    {
                        "icon": "⚖️",
                        "title_en": "Electronic Tax Appeal Submission",
                        "title_sgn": "Элэктронико Таксо Апэло Портало",
                        "desc_en": "Formal dispute adjudication portal to contest assessment discrepancies directly before the Board of Tax Magistrates.",
                        "desc_sgn": "Официало апэло канало ад диспуто таксо ано антэо Аэрарио Магистрато.",
                        "action_en": "File Tax Appeal",
                        "action_sgn": "Субмито Апэло",
                        "modal": "taxappeal"
                    }
                ]
            },
            {
                "id": "fiscal-management",
                "name_en": "Department of Fiscal Management",
                "name_sgn": "Дэпарто эк Фискало Мануго",
                "mandate_en": "Safeguarding zero foreign sovereign debt, issuing national solidarity bonds, and forecasting national liquidity reserves.",
                "mandate_sgn": "Сэкуро зэро фориэро дэбито, эмито сонит бондо, инкаи калкуло ликуидита рэзэрво.",
                "functions": [
                    {
                        "icon": "📈",
                        "title_en": "Live Debt Tracker & Bond Yield Telemetry",
                        "title_sgn": "Виво Дэбито & Бондо Рэйтио Тэлэмэтриа",
                        "desc_en": "Real-time verification of Sangaia's 100% solvency ($0 foreign debt) alongside 10-year domestic bond yields (3.2% silver-backed).",
                        "desc_sgn": "Виво пробо эк 100% сонита ($ 0 фориэро дэбито) инкаи 10-анно бондо рэйтио.",
                        "action_en": "View Debt & Yields",
                        "action_sgn": "Визо Бондо Тэлэмэтриа",
                        "modal": "debtscreen"
                    },
                    {
                        "icon": "🏦",
                        "title_en": "Citizen Bond Purchase & Redemption Hub",
                        "title_sgn": "Цивикано Бондо Эмпто & Рэдэмтио Хэб",
                        "desc_en": "Direct citizen portal to purchase non-transferable Sovereign Solidarity Bonds that directly fund provincial green infrastructure.",
                        "desc_sgn": "Дирэкто портало про цивикано ад эмпто Сонит Бондо про финансио провиткия понто инкаи виа.",
                        "action_en": "Manage Bonds",
                        "action_sgn": "Мануго Бондо",
                        "modal": "bondhub"
                    },
                    {
                        "icon": "📰",
                        "title_en": "Quarterly Economic Outlook Bulletins",
                        "title_sgn": "Три-Мэнсо Экономиа Оутлуко Булэтино",
                        "desc_en": "Exhaustive macro forecasting detailing real GDP expansion, resource reserves, and inter-provincial trade surpluses.",
                        "desc_sgn": "Три-мэнсо макро-анализ эк ГДП эволутио, рэсурсо рэзэрво, инкаи мэрко балансо.",
                        "action_en": "Read Bulletins",
                        "action_sgn": "Лэго Булэтино",
                        "modal": "econbulletin"
                    }
                ]
            },
            {
                "id": "appropriations",
                "name_en": "Department of Ministerial Appropriations",
                "name_sgn": "Дэпарто эк Министро Апроприатио",
                "mandate_en": "Allocating statutory funding to executive ministries, publishing expenditure audits, and vetting open public tenders.",
                "mandate_sgn": "Алоко пэкуниа ад министро, публико дапано аудито, инкаи инспэкто публико тэндэро.",
                "functions": [
                    {
                        "icon": "📋",
                        "title_en": "Open Government Procurement Listings",
                        "title_sgn": "Апэрта Губэрно Тэндэро & Прокурэмэнто",
                        "desc_en": "Live transparent register of all state construction, technological, and medical tenders with zero backroom bidding.",
                        "desc_sgn": "Виво тэндэро эк конструктио, тэк, инкаи хоспитало син шэно кклаузо коррупцио.",
                        "action_en": "Browse Active Tenders",
                        "action_sgn": "Скэро Тэндэро",
                        "modal": "tenders"
                    },
                    {
                        "icon": "🔍",
                        "title_en": "Ministry Expenditure Audit Reports",
                        "title_sgn": "Министро Дапано Аудито Рэпорто",
                        "desc_en": "Line-by-line disbursement ledger auditing ministerial outlays against approved Body of Electives statutory ceilings.",
                        "desc_sgn": "Тото леджер эк дапано про шэно министро компоро куно Корпо эк Элэкто лимито.",
                        "action_en": "Inspect Audit Ledger",
                        "action_sgn": "Инспэкто Дапано",
                        "modal": "auditledger"
                    },
                    {
                        "icon": "💼",
                        "title_en": "Budget Request Tracking Portal",
                        "title_sgn": "Бугэтио Пэтитио Тракинго Портало",
                        "desc_en": "Internal workflow tracker for administrative bodies submitting statutory supplemental funding requests.",
                        "desc_sgn": "Тракинго канало про агэнциа субмито эксэпционало бугэтио пэтитио.",
                        "action_en": "Track Request",
                        "action_sgn": "Трако Пэтитио",
                        "modal": "budgetreq"
                    }
                ]
            }
        ]
    },

    "work": {
        "slug": "work",
        "theme": {
            "name": "Ministry of Work",
            "primary": "#7e22ce",
            "dark": "#581c87",
            "deep": "#3b0764",
            "light": "#a855f7",
            "pale": "#faf5ff",
            "border": "#e9d5ff",
            "accent": "#f59e0b"
        },
        "title_en": "Departments of Labor & Employment",
        "title_sgn": "Дэпартамэнто эк Лабориа",
        "ministry_en": "Ministry of Work",
        "ministry_sgn": "Министриа эк Лабориа",
        "subdomain": "https://work.sangaia.org",
        "target_dirs": ["mW"],
        "root_file": "work_departments.html",
        "root_sgn_file": "sgn/work_departments.html",
        "departments": [
            {
                "id": "labor-standards",
                "name_en": "Department of Labor Standards & Worker Protections",
                "name_sgn": "Дэпарто эк Лаборо Стандарто & Лаборано Протэктио",
                "mandate_en": "Enforcing statutory wage floors, workplace safety rules, union organizing guarantees, and anti-exploitation protocols.",
                "mandate_sgn": "Фортис минимо пэкуниа, лаборо сэкуро рэгла, синдикато жусо, инкаи анти-эксплоитатио.",
                "functions": [
                    {
                        "icon": "📣",
                        "title_en": "Anonymous Whistleblower Violation Report",
                        "title_sgn": "Анонимо Лаборо Виолатио Рэпорто",
                        "desc_en": "Encrypted direct pipeline to report unpaid overtime, workplace hazards, or union suppression without fear of retaliation.",
                        "desc_sgn": "Криптографико канало ад рэпорто пэкуниа фуро вэл дангэро лаборо син тимор.",
                        "action_en": "File Whistleblower Report",
                        "action_sgn": "Субмито Рэпорто",
                        "modal": "whistleblower"
                    },
                    {
                        "icon": "📖",
                        "title_en": "Workplace Standard Guidelines (OSHA-S)",
                        "title_sgn": "Лаборо-Локус Стандарто Гуида",
                        "desc_en": "Complete statutory manuals governing maritime rigging, timber felling, chemical handling, and digital ergonomic standards.",
                        "desc_sgn": "Статуто мануало про марино, лигно, кемико, инкаи дигитало лаборо сэкуро.",
                        "action_en": "Download Standards",
                        "action_sgn": "Даунлоадо Стандарто",
                        "modal": "standards"
                    },
                    {
                        "icon": "🤝",
                        "title_en": "Union Registry & Mediation Booking",
                        "title_sgn": "Синдикато Рэгистро & Мэдиатио Скэдуло",
                        "desc_en": "Public roster of certified trade unions and online calendar to schedule binding labor dispute arbitration hearings.",
                        "desc_sgn": "Публико синдикато ростро инкаи онлаин калэндарио про лаборо диспуто арбитро.",
                        "action_en": "Book Mediation / Registry",
                        "action_sgn": "Рэгистро / Скэдуло",
                        "modal": "mediation"
                    }
                ]
            },
            {
                "id": "workforce-dev",
                "name_en": "Department of Workforce Development",
                "name_sgn": "Дэпарто эк Лаборо-Форса Эволутио",
                "mandate_en": "Facilitating public employment placement, state apprentice guilds, and unemployment transitional allowances.",
                "mandate_sgn": "Мануго публико лаборо локус, гилда студиозо, инкаи инэмпломэнто транзито пэкуниа.",
                "functions": [
                    {
                        "icon": "💼",
                        "title_en": "National Public Job Board",
                        "title_sgn": "Натио Публико Лаборо Табула",
                        "desc_en": "Searchable registry of verified openings across public administration, green engineering, timber crafts, and health networks.",
                        "desc_sgn": "Скэро лаборо ин губэрно, инжэниа, лигно фабро, инкаи хоспитало куно $ пэкуниа.",
                        "action_en": "Search Job Board",
                        "action_sgn": "Скэро Лаборо",
                        "modal": "jobs"
                    },
                    {
                        "icon": "🛡️",
                        "title_en": "Unemployment Benefit & Transitional Security",
                        "title_sgn": "Инэмпломэнто Бэнефито & Сэкуро",
                        "desc_en": "Fast-track relief application granting up to 75% wage preservation during involuntary career transitions.",
                        "desc_sgn": "Апликатио про 75% пэкуниа сэкуро дурантэ инволунтаро лаборо транзито.",
                        "action_en": "File Benefit Claim",
                        "action_sgn": "Субмито Клэймо",
                        "modal": "unemployment"
                    },
                    {
                        "icon": "🎓",
                        "title_en": "Subsidized Vocational Retraining Hub",
                        "title_sgn": "Субсидиа Профэсио Докэно Хэб",
                        "desc_en": "Enroll in state-funded academies for maritime solar engineering, robotic agriculture, or software development.",
                        "desc_sgn": "Энроло ин либэро скола про соларо инжэниа, робото агрикултура, инкаи кодинго.",
                        "action_en": "Enroll in Training",
                        "action_sgn": "Энроло Докэно",
                        "modal": "retraining"
                    }
                ]
            },
            {
                "id": "foreign-labor",
                "name_en": "Department of Foreign Labor",
                "name_sgn": "Дэпарто эк Фориэро Лаборо",
                "mandate_en": "Regulating international work permits, credential equivalency transfers, and migrant worker legal safeguards.",
                "mandate_sgn": "Рэгуло фориэро лаборо пэрмито, квалификатио трансфэро, инкаи мигранто жусо.",
                "functions": [
                    {
                        "icon": "🛂",
                        "title_en": "Work Visa Eligibility Evaluation Tool",
                        "title_sgn": "Лаборо Виса Элигио Калкулаторо",
                        "desc_en": "Interactive questionnaire determining eligibility for Specialist, Seasonal Agricultural, or Marine Technician visas.",
                        "desc_sgn": "Интэракто тэсто про Спесиалисто, Агрикултура, вэл Марино лаборо виса.",
                        "action_en": "Check Visa Eligibility",
                        "action_sgn": "Элигио Тэсто",
                        "modal": "visacheck"
                    },
                    {
                        "icon": "📜",
                        "title_en": "Foreign Professional Credential Verification",
                        "title_sgn": "Фориэро Квалификатио Вэрификатио",
                        "desc_en": "Cross-reference foreign engineering, medical, and maritime licenses for automatic Sangaian statutory equivalency.",
                        "desc_sgn": "Вэрифико фориэро диплом инкаи лицэнсиа про Сангаиа эквивалэнто.",
                        "action_en": "Verify Credentials",
                        "action_sgn": "Вэрифико Диплом",
                        "modal": "credentials"
                    },
                    {
                        "icon": "☎️",
                        "title_en": "Multilingual Foreign Worker Legal Hotline",
                        "title_sgn": "Мултилингво Фориэро Лаборано Хэлплине",
                        "desc_en": "24/7 dedicated legal assistance directory in English, Sangaian, Spanish, and French protecting foreign laborers from coercion.",
                        "desc_sgn": "24-ора юридико канало ад протэкто фориэро лаборано апо коэрцио.",
                        "action_en": "Access Legal Hotlines",
                        "action_sgn": "Юридико Канало",
                        "modal": "hotlines"
                    }
                ]
            }
        ]
    },

    "healthcare": {
        "slug": "healthcare",
        "theme": {
            "name": "Ministry of Healthcare",
            "primary": "#c62828",
            "dark": "#991b1b",
            "deep": "#7f1d1d",
            "light": "#ef4444",
            "pale": "#fef2f2",
            "border": "#fecaca",
            "accent": "#0284c7"
        },
        "title_en": "Healthcare Departments & Clinical Systems",
        "title_sgn": "Салутиа Дэпартамэнто & Клинико Систэма",
        "ministry_en": "Ministry of Healthcare",
        "ministry_sgn": "Министриа эк Салутиа",
        "subdomain": "https://healthcare.sangaia.org",
        "target_dirs": ["mH"],
        "root_file": "healthcare_departments.html",
        "root_sgn_file": "sgn/healthcare_departments.html",
        "departments": [
            {
                "id": "universal-coverage",
                "name_en": "Department of Universal Coverage",
                "name_sgn": "Дэпарто эк Унивэрсало Салутиа-Кура",
                "mandate_en": "Administering constitutional 100% state-sponsored healthcare, digital insurance cards, and essential prescription co-pay elimination.",
                "mandate_sgn": "Мануго 100% либэро салутиа-кура, дигитало кардо, инкаи фармако бэнефито син ко-пай.",
                "functions": [
                    {
                        "icon": "💳",
                        "title_en": "Digital Health Card & Coverage Portal",
                        "title_sgn": "Дигитало Салутиа Кардо & Портало",
                        "desc_en": "Synchronize your Universal Healthcare ID with your master Sangaia ID wallet for immediate hospital intake verification.",
                        "desc_sgn": "Синхронисо тус Салутиа ИД куно Сангаиа ИД про статим хоспитало адито.",
                        "action_en": "Manage Health Card",
                        "action_sgn": "Мануго Кардо",
                        "modal": "healthcard"
                    },
                    {
                        "icon": "🏥",
                        "title_en": "Primary Care Provider Directory Lookup",
                        "title_sgn": "Прото Салутиа Мэдико Дирэкторио",
                        "desc_en": "Find verified provincial family doctors, pediatric clinics, and dental dispensaries accepting walk-in citizen consultations.",
                        "desc_sgn": "Скэро фамозио мэдико, педиатрэ клиника, инкаи дэнтаро дуло суб тус Провиткия.",
                        "action_en": "Find a Doctor",
                        "action_sgn": "Скэро Мэдико",
                        "modal": "provider"
                    },
                    {
                        "icon": "💊",
                        "title_en": "Prescription Benefit & Formulary Tracker",
                        "title_sgn": "Фармако Бэнефито & Формуларо Тракер",
                        "desc_en": "Search the 4,200 subsidized essential medicines covered under Sangaian national pharmacare with zero out-of-pocket fees.",
                        "desc_sgn": "Скэро 4,200 фармако ти эст 100% либэро суб ностэр натио прагма.",
                        "action_en": "Search Formulary",
                        "action_sgn": "Скэро Фармако",
                        "modal": "formulary"
                    }
                ]
            },
            {
                "id": "hospitals",
                "name_en": "Department of Hospitals & Emergency Dispatch",
                "name_sgn": "Дэпарто эк Хоспитало & Эмэрго Диспачо",
                "mandate_en": "Coordinating regional hospital networks, paramedic emergency dispatch triage, and hospital acute care accreditation.",
                "mandate_sgn": "Координато хоспитало рэти, амбуланто триаге, инкаи клинико акредитатио.",
                "functions": [
                    {
                        "icon": "🚨",
                        "title_en": "Live Hospital ER Capacity & Triage Telemetry",
                        "title_sgn": "Виво Хоспитало ЭР Капасита Тэлэмэтриа",
                        "desc_en": "Real-time bed availability, trauma team status, and estimated emergency wait times across all 4 provincial medical centers.",
                        "desc_sgn": "Виво монито эк лэкто диспэнобило, траума тимо, инкаи экпэкто тэмпус ин 4 хоспитало.",
                        "action_en": "View ER Capacity",
                        "action_sgn": "Визо ЭР Тэлэмэтриа",
                        "modal": "ercapacity"
                    },
                    {
                        "icon": "🚑",
                        "title_en": "Non-Emergency Medical Transport Booking",
                        "title_sgn": "Нон-Эмэрго Мэдико Транзито Скэдуло",
                        "desc_en": "Book state-funded medical shuttles and rural patient vans for specialist visits, dialysis, and mobility assistance.",
                        "desc_sgn": "Скэдуло либэро мэдико транспорт про диализ инкаи сэниоро консултатио.",
                        "action_en": "Book Transport",
                        "action_sgn": "Скэдуло Транспорт",
                        "modal": "transport"
                    },
                    {
                        "icon": "🩺",
                        "title_en": "Paramedic & Clinical Licensing Verification",
                        "title_sgn": "Парамэдико & Мэдико Лицэнсиа Пробо",
                        "desc_en": "Instant credential verification for emergency responders, specialized trauma surgeons, and registered nurses.",
                        "desc_sgn": "Статим вэрификатио эк парамэдико лицэнсиа инкаи хирурго акредитатио.",
                        "action_en": "Verify Clinician",
                        "action_sgn": "Вэрифико Мэдико",
                        "modal": "verifyclinician"
                    }
                ]
            }
        ]
    },

    "education": {
        "slug": "education",
        "theme": {
            "name": "Ministry of Education",
            "primary": "#00838f",
            "dark": "#006064",
            "deep": "#164e63",
            "light": "#06b6d4",
            "pale": "#ecfeff",
            "border": "#a5f3fc",
            "accent": "#f59e0b"
        },
        "title_en": "Educational Departments & Academic Authority",
        "title_sgn": "Дэпартамэнто эк Эдукатио & Академико",
        "ministry_en": "Ministry of Education",
        "ministry_sgn": "Министриа эк Эдукатио",
        "subdomain": "https://education.sangaia.org",
        "target_dirs": ["mE", "mEd"],
        "root_file": "education_departments.html",
        "root_sgn_file": "sgn/education_departments.html",
        "departments": [
            {
                "id": "curriculum-standards",
                "name_en": "Department of Curriculum Development & Academic Standards",
                "name_sgn": "Дэпарто эк Курикулум & Академико Стандарто",
                "mandate_en": "Authoring nationwide bilingual curricula, certifying textbooks, and establishing non-partisan graduation competencies.",
                "mandate_sgn": "Формо билингво курикулум, акредито либро, инкаи сэкуро студиозо градус.",
                "functions": [
                    {
                        "icon": "📚",
                        "title_en": "Open Digital Textbook & Syllabi Repository",
                        "title_sgn": "Апэрта Либро & Курикулум Архиво",
                        "desc_en": "Download certified primary, secondary, and polytechnic syllabi and digitized public domain educational textbooks.",
                        "desc_sgn": "Даунлоадо либэро скола либро инкаи унивэрсита курсо.",
                        "action_en": "Browse Digital Books",
                        "action_sgn": "Скэро Либро",
                        "modal": "textbooks"
                    },
                    {
                        "icon": "🎖️",
                        "title_en": "Teacher Certification & Licensure Renewal",
                        "title_sgn": "Магистро Лицэнсиа & Рэнэво Канало",
                        "desc_en": "Official credential renewal portal for educators fulfilling continuing pedagogical and bilingual instruction standards.",
                        "desc_sgn": "Официало лицэнсиа рэнэво про скола магистро инкаи професоро.",
                        "action_en": "Renew Certification",
                        "action_sgn": "Рэнэво Лицэнсиа",
                        "modal": "teachercert"
                    },
                    {
                        "icon": "🏫",
                        "title_en": "School Performance & Equity Scorecards",
                        "title_sgn": "Скола Прогрэсо & Балансо Скорекардо",
                        "desc_en": "Interactive performance diagnostics for all public academies measuring literacy, STEM attainment, and facility equity.",
                        "desc_sgn": "Интэракто скола диагнозис про литэратура, СТЕМ, инкаи студиозо капасита.",
                        "action_en": "View Scorecards",
                        "action_sgn": "Визо Скорекардо",
                        "modal": "schoolscores"
                    }
                ]
            },
            {
                "id": "higher-ed-grants",
                "name_en": "Department of Higher Education & Research Grants",
                "name_sgn": "Дэпарто эк Алто Эдукатио & Инвэстиго Гранто",
                "mandate_en": "Financing sovereign universities, administering tuition-free student bursaries, and underwriting sovereign scientific research.",
                "mandate_sgn": "Финансио унивэрсита, либэро студиозо гранто, инкаи натио сапэнсо инвэстиго.",
                "functions": [
                    {
                        "icon": "🎓",
                        "title_en": "Centralized Student Grant & Bursary Portal",
                        "title_sgn": "Студиозо Гранто & Бурсарио Портало",
                        "desc_en": "Apply for non-repayable living stipends, housing subsidies, and academic merit endowments for university scholars.",
                        "desc_sgn": "Апликатио про либэро студиозо пэкуниа, домо субсидиа, инкаи стипэндо.",
                        "action_en": "Apply for Grant",
                        "action_sgn": "Субмито Гранто",
                        "modal": "studentgrant"
                    },
                    {
                        "icon": "💸",
                        "title_en": "Zero-Interest Debt Servicing Calculator",
                        "title_sgn": "Зэро-Интэрэст Дэбито Калкулаторо",
                        "desc_en": "Calculate statutory debt-free credits under Sangaian law, ensuring zero interest accrual and automated service offsets.",
                        "desc_sgn": "Калкуло студиозо пэкуниа син шэно интэрэст суб Сангаиа лэксо.",
                        "action_en": "Calculate Repayment",
                        "action_sgn": "Калкуло Крэдито",
                        "modal": "debtcalc"
                    },
                    {
                        "icon": "🔬",
                        "title_en": "Peer-Reviewed Sovereign Research Repository",
                        "title_sgn": "Пеэр-Рэвисо Натио Сапэнсо Архиво",
                        "desc_en": "Open-access archive of state-funded scientific discoveries in ocean thermal energy, agriculture, and computational mathematics.",
                        "desc_sgn": "Либэро архиво эк натио инвэстиго ин соларо инжэниа, биомо, инкаи математико.",
                        "action_en": "Search Research Papers",
                        "action_sgn": "Скэро Сапэнсо",
                        "modal": "researchpapers"
                    }
                ]
            },
            {
                "id": "facilities",
                "name_en": "Department of Institutional Facilities",
                "name_sgn": "Дэпарто эк Институто Инфраструктура",
                "mandate_en": "Distributing capital grants for school modernization, lab technology, broadband networks, and safety infrastructure.",
                "mandate_sgn": "Алоко капитал про скола конструктио, лабораторио, фибра рэти, инкаи сэкуро.",
                "functions": [
                    {
                        "icon": "🏗️",
                        "title_en": "Capital Modernization Grant Submission",
                        "title_sgn": "Капитал Модэрнизо Гранто Субмито",
                        "desc_en": "Portal for provincial headmasters to submit blueprints for clean geothermal heating, seismic upgrades, and sports grounds.",
                        "desc_sgn": "Портало про скола дуксо ад субмито гео-калоро инкаи конструктио проекто.",
                        "action_en": "Submit Facility Grant",
                        "action_sgn": "Субмито Проекто",
                        "modal": "facilitygrant"
                    },
                    {
                        "icon": "🛡️",
                        "title_en": "Safety & Air Quality Inspection Audits",
                        "title_sgn": "Сэкуро & Аэр Инспэктио Аудито",
                        "desc_en": "Public transparency ledger recording annual structural soundness, fire drills, and clean classroom ventilation metrics.",
                        "desc_sgn": "Публико леджер эк скола сэкуро инспэктио инкаи чилан аэр стандарто.",
                        "action_en": "Inspect Audit Reports",
                        "action_sgn": "Визо Инспэктио",
                        "modal": "safetyaudits"
                    },
                    {
                        "icon": "🔄",
                        "title_en": "Regional Equipment & Tech Exchange Network",
                        "title_sgn": "Рэгионо Компюто & Инструмэнто Мэрко",
                        "desc_en": "Surplus reallocation network transferring scientific microscopes, Stucal tablets, and musical instruments between schools.",
                        "desc_sgn": "Рэти ад трансфэро микроскопо, Стукал компюто, инкаи музико инструмэнто.",
                        "action_en": "Equipment Exchange",
                        "action_sgn": "Инструмэнто Рэти",
                        "modal": "equipswap"
                    }
                ]
            }
        ]
    },

    "domesticaffairs": {
        "slug": "domesticaffairs",
        "theme": {
            "name": "Ministry of Domestic Affairs",
            "primary": "#102a54",
            "dark": "#0d2346",
            "deep": "#0a192f",
            "light": "#2563eb",
            "pale": "#eff6ff",
            "border": "#bfdbfe",
            "accent": "#d97706"
        },
        "title_en": "Domestic Affairs Departments",
        "title_sgn": "Дэпартамэнто эк Домэстико",
        "ministry_en": "Ministry of Domestic Affairs",
        "ministry_sgn": "Министриа эк Домэстико",
        "subdomain": "https://domesticaffairs.sangaia.org",
        "target_dirs": ["MiA"],
        "root_file": "domesticaffairs_departments.html",
        "root_sgn_file": "sgn/domesticaffairs_departments.html",
        "departments": [
            {
                "id": "transit",
                "name_en": "Department of Transit Infrastructure",
                "name_sgn": "Дэпарто эк Транзито Инфраструктура",
                "mandate_en": "Maintaining federal toll-free highways, railway networks, passenger ferries, and automated roadway hazard telemetry.",
                "mandate_sgn": "Сэрво фэдэро виа, фэрро-виа, нави, инкаи автоматико клима тэлэмэтриа.",
                "functions": [
                    {
                        "icon": "🎥",
                        "title_en": "Live Highway Cameras & Hazard Map",
                        "title_sgn": "Виво Виа Камера & Дангэро Мапа",
                        "desc_en": "Interactive live CCTV camera network and road condition maps tracking snowfall, fog, and road closures in real time.",
                        "desc_sgn": "Виво камера рэти инкаи виа мапа тракинго ниво, нэбула, инкаи виа статус.",
                        "action_en": "Launch Hazard Map",
                        "action_sgn": "Лапидо Виа Мапа",
                        "modal": "hazardmap"
                    },
                    {
                        "icon": "🛣️",
                        "title_en": "Automated Transponder & Transit Pass",
                        "title_sgn": "Автоматико Транзито Пасо Портало",
                        "desc_en": "Manage digital electronic vehicle transponders for automated maritime ferry boarding and zero-delay municipal corridors.",
                        "desc_sgn": "Мануго дигитало транспорт пасо про нави инкаи провиткия коридоро.",
                        "action_en": "Manage Transit Pass",
                        "action_sgn": "Мануго Пасо",
                        "modal": "transitpass"
                    },
                    {
                        "icon": "🚧",
                        "title_en": "Road Defect & Hazard Rapid Reporting",
                        "title_sgn": "Виа Фалу & Дангэро Рапидо Рэпорто",
                        "desc_en": "Geolocated citizen reporting tool to dispatch maintenance road crews for potholes, rockfalls, or fallen timber within 24 hours.",
                        "desc_sgn": "Геолокасио канало ад диспачо виа фабро про фалу инкаи саксо ин 24 ора.",
                        "action_en": "Report Road Hazard",
                        "action_sgn": "Рэпорто Фалу",
                        "modal": "roaddefect"
                    }
                ]
            },
            {
                "id": "dmv",
                "name_en": "Department of Motor Vehicles & Operator Licensing",
                "name_sgn": "Дэпарто эк Аутомэтико & Кондукто Лицэнсиа",
                "mandate_en": "Issuing operator licenses, registering vehicles, conducting road safety inspections, and processing traffic citations.",
                "mandate_sgn": "Эмито кондукто лицэнсиа, рэгистро аутомэтико, инспэкто сэкуро, инкаи ситатио.",
                "functions": [
                    {
                        "icon": "🪪",
                        "title_en": "Driver's License Renewal & Digital Permit",
                        "title_sgn": "Кондукто Лицэнсиа Рэнэво & Дигитало",
                        "desc_en": "Renew operator licenses online with biological photo verification and synchronized mobile wallet credential pass.",
                        "desc_sgn": "Рэнэво лицэнсиа онлаин куно фото инкаи Сангаиа ИД синхронисатио.",
                        "action_en": "Renew Driver's License",
                        "action_sgn": "Рэнэво Лицэнсиа",
                        "modal": "dmvlicense"
                    },
                    {
                        "icon": "🚗",
                        "title_en": "Vehicle Registration & Title Transfer",
                        "title_sgn": "Аутомэтико Рэгистро & Титуло Трансфэро",
                        "desc_en": "Register private, agricultural, or commercial vehicles with integrated emissions check certificates.",
                        "desc_sgn": "Рэгистро привато вэл агрикултура аутомэтико куно эколожико тэсто.",
                        "action_en": "Register Vehicle",
                        "action_sgn": "Рэгистро Ауто",
                        "modal": "dmvreg"
                    },
                    {
                        "icon": "💳",
                        "title_en": "Traffic Citation Adjudication & Payment",
                        "title_sgn": "Транзито Ситатио & Пагамо Портало",
                        "desc_en": "Review traffic camera evidence, contest civil road penalties, or settle municipal fines electronically.",
                        "desc_sgn": "Визо камера эвидэнсо, контэсто ситатио, вэл паго мулта онлаин.",
                        "action_en": "Review Citations",
                        "action_sgn": "Визо Ситатио",
                        "modal": "dmvcitation"
                    }
                ]
            },
            {
                "id": "inter-provincial",
                "name_en": "Department of Inter-Provincial Relations",
                "name_sgn": "Дэпарто эк Интэр-Провиткия Рэлатио",
                "mandate_en": "Harmonizing inter-provincial trade agreements, maintaining open internal borders, and arbitrating commercial disputes.",
                "mandate_sgn": "Хармонио провиткия мэрко, сэкуро апэрта виа, инкаи арбитро комэрцио диспуто.",
                "functions": [
                    {
                        "icon": "📦",
                        "title_en": "Inter-Provincial Shipping Manifest Portal",
                        "title_sgn": "Интэр-Провиткия Транспорт Манифэсто",
                        "desc_en": "Expedited digital clearance for commercial cargo transiting between Coastal, Highlands, Central, and Island boundaries.",
                        "desc_sgn": "Дигитало манифэсто про комэрциало карго транзито интэр Провиткия.",
                        "action_en": "File Manifest",
                        "action_sgn": "Субмито Манифэсто",
                        "modal": "shippingmanifest"
                    },
                    {
                        "icon": "🗺️",
                        "title_en": "Internal Trade & Jurisdiction Boundary Map",
                        "title_sgn": "Интэрно Мэрко & Журисдиктио Мапа",
                        "desc_en": "Interactive cartography delineating provincial tax harmonization corridors, port authorities, and municipal water compacts.",
                        "desc_sgn": "Интэракто мапа эк провиткия мэрко зона, порто ауторита, инкаи аква пакто.",
                        "action_en": "Explore Trade Map",
                        "action_sgn": "Визо Мэрко Мапа",
                        "modal": "trademap"
                    },
                    {
                        "icon": "⚖️",
                        "title_en": "Commercial Arbitration Dispute Registry",
                        "title_sgn": "Комэрциало Арбитро Диспуто Рэгистро",
                        "desc_en": "File disputes between inter-provincial businesses for binding, zero-cost resolution by the Federal Mediation Board.",
                        "desc_sgn": "Субмито диспуто интэр провиткия комэрцио про либэро фэдэро арбитро.",
                        "action_en": "File Arbitration Claim",
                        "action_sgn": "Субмито Арбитро",
                        "modal": "arbitration"
                    }
                ]
            }
        ]
    },

    "externalaffairs": {
        "slug": "externalaffairs",
        "theme": {
            "name": "Ministry of External Affairs",
            "primary": "#ad1457",
            "dark": "#880e4f",
            "deep": "#700b39",
            "light": "#ec4899",
            "pale": "#fdf2f8",
            "border": "#fbcfe8",
            "accent": "#c2410c"
        },
        "title_en": "Diplomatic Departments & Global Missions",
        "title_sgn": "Дипломатико Дэпартамэнто & Мундо Мисио",
        "ministry_en": "Ministry of External Affairs",
        "ministry_sgn": "Министриа эк Экстэрно",
        "subdomain": "https://externalaffairs.sangaia.org",
        "target_dirs": ["MdA"],
        "root_file": "externalaffairs_departments.html",
        "root_sgn_file": "sgn/externalaffairs_departments.html",
        "departments": [
            {
                "id": "diplomatic-missions",
                "name_en": "Department of Diplomatic Missions",
                "name_sgn": "Дэпарто эк Дипломатико Мисио",
                "mandate_en": "Operating Sangaia’s worldwide embassies, assisting traveling citizens, and issuing sovereign passports and diplomatic visas.",
                "mandate_sgn": "Мануго Сангаиа эмбасо суб холо мундо, асисто виагио цивикано, инкаи эмито паспорто.",
                "functions": [
                    {
                        "icon": "🛂",
                        "title_en": "Passport Application & Renewal Portal",
                        "title_sgn": "Паспорто Апликатио & Рэнэво Портало",
                        "desc_en": "Fast-track biometric e-passport issuance with cryptographic virtue watermark and emergency 48-hour consular dispatch.",
                        "desc_sgn": "Биомэтрико паспорто эмито куно криптографико ватэрмарко инкаи 48-ора диспачо.",
                        "action_en": "Apply for Passport",
                        "action_sgn": "Аплико про Паспорто",
                        "modal": "passportportal"
                    },
                    {
                        "icon": "🌍",
                        "title_en": "Global Embassy Directory & Consular Registry",
                        "title_sgn": "Мундо Эмбасо Дирэкторио & Консуларо",
                        "desc_en": "Searchable 24/7 contact directory for all Sangaian diplomatic missions, emergency hotlines, and citizen check-ins abroad.",
                        "desc_sgn": "24-ора дирэкторио эк холо Сангаиа эмбасо, конто, инкаи эмэрго канало ин экстро.",
                        "action_en": "Locate Embassy",
                        "action_sgn": "Скэро Эмбасо",
                        "modal": "embassydir"
                    },
                    {
                        "icon": "🆘",
                        "title_en": "Emergency Overseas Consular Assistance",
                        "title_sgn": "Эмэрго Экстро Консуларо Асисто",
                        "desc_en": "Urgent repatriation assistance, legal representation coordination, and emergency travel loans for citizens in distress abroad.",
                        "desc_sgn": "Эмэрго рэпатриатио, юридико асисто, инкаи виагио субсидиа про цивикано ин экстро.",
                        "action_en": "Request Emergency Aid",
                        "action_sgn": "Пэтитио про Асисто",
                        "modal": "emergencyconsular"
                    }
                ]
            },
            {
                "id": "treaties-law",
                "name_en": "Department of International Treaties & Global Law",
                "name_sgn": "Дэпарто эк Интэр-Натио Трактато & Мундо Лэксо",
                "mandate_en": "Negotiating bilateral covenants, safeguarding sovereignty under international law, and maintaining diplomatic immunities.",
                "mandate_sgn": "Трактато диалого, сэкуро сувэрэнита суб мундо лэксо, инкаи дипломатико иммунита.",
                "functions": [
                    {
                        "icon": "📜",
                        "title_en": "Searchable Ratified Treaties Archive",
                        "title_sgn": "Скэро-Гаранто Ратификато Трактато Архиво",
                        "desc_en": "Full-text repository of active and historical bilateral peace accords, maritime fishery compacts, and extradition agreements.",
                        "desc_sgn": "Тото тэксто архиво эк пакто, марино пискато пакто, инкаи дипломатико трактато.",
                        "action_en": "Search Treaties Archive",
                        "action_sgn": "Скэро Трактато",
                        "modal": "treatyarchive"
                    },
                    {
                        "icon": "⚖️",
                        "title_en": "Treaty Compliance & Legal Advisory",
                        "title_sgn": "Трактато Комплио & Юридико Ависо",
                        "desc_en": "Official compliance monitoring reports ensuring all foreign pacts adhere to Article V anti-subjugation clauses.",
                        "desc_sgn": "Рэпорто монито эк трактато комплио суб Артикуло V эк ностэр Своротицания.",
                        "action_en": "View Compliance Logs",
                        "action_sgn": "Визо Комплио Леджер",
                        "modal": "compliance"
                    },
                    {
                        "icon": "🕊️",
                        "title_en": "Diplomatic Protocol & Immunity Register",
                        "title_sgn": "Дипломатико Протоколо & Иммунита Рэгистро",
                        "desc_en": "Verified register of foreign diplomatic credentials, immunity protections, and bilateral consular treaties.",
                        "desc_sgn": "Официало рэгистро эк фориэро дипломатико лицэнсиа инкаи иммунита.",
                        "action_en": "Inspect Protocol Register",
                        "action_sgn": "Инспэкто Протоколо",
                        "modal": "protocolreg"
                    }
                ]
            },
            {
                "id": "foreign-commerce",
                "name_en": "Department of Foreign Commerce",
                "name_sgn": "Дэпарто эк Фориэро Мэрко",
                "mandate_en": "Expanding sustainable export markets, negotiating reciprocal tariff reductions, and attracting ethical foreign investment.",
                "mandate_sgn": "Экспандо экспорт, тариф рэдуктио диалого, инкаи сонит инвэститио.",
                "functions": [
                    {
                        "icon": "🚢",
                        "title_en": "Import / Export Tariff Rate Calculator",
                        "title_sgn": "Импорт / Экспорт Тариф Калкулаторо",
                        "desc_en": "Look up statutory customs duties, carbon border adjustments, and duty-free exemptions by Harmonized System (HS) code.",
                        "desc_sgn": "Калкуло кустомо тариф, карбоно адюсто, инкаи либэро экспорт суб ХС кодэ.",
                        "action_en": "Calculate Tariffs",
                        "action_sgn": "Калкуло Тариф",
                        "modal": "tariffcalc"
                    },
                    {
                        "icon": "📊",
                        "title_en": "Exporters Market Intelligence Dossiers",
                        "title_sgn": "Экспорторо Мэрко Интелигэнто Досиэ",
                        "desc_en": "Comprehensive trade briefings for Sangaian timber, ocean seafood, and clean tech companies seeking foreign market access.",
                        "desc_sgn": "Мэрко анализо про Сангаиа лигно, пискато, инкаи соларо экспорт.",
                        "action_en": "Access Dossiers",
                        "action_sgn": "Визо Досиэ",
                        "modal": "dossiers"
                    },
                    {
                        "icon": "🌱",
                        "title_en": "Foreign Ethical Investment Registration",
                        "title_sgn": "Фориэро Морало Инвэститио Рэгистро",
                        "desc_en": "Statutory vetting pipeline ensuring foreign capital complies with zero-pollution and non-exploitative labor standards.",
                        "desc_sgn": "Вэрификатио канало ад сэкуро фориэро пэкуниа комплио куно зэро-полутио.",
                        "action_en": "Register Investment",
                        "action_sgn": "Рэгистро Инвэститио",
                        "modal": "fdi"
                    }
                ]
            }
        ]
    },

    "environment": {
        "slug": "environment",
        "theme": {
            "name": "Ministry of the Environment",
            "primary": "#2e7d32",
            "dark": "#1b5e20",
            "deep": "#14532d",
            "light": "#4ade80",
            "pale": "#f0fdf4",
            "border": "#bbf7d0",
            "accent": "#e65100"
        },
        "title_en": "Environmental Departments & Ecological Authorities",
        "title_sgn": "Амбиэто Дэпартамэнто & Экологико",
        "ministry_en": "Ministry of the Environment",
        "ministry_sgn": "Министриа эк Амбиэто",
        "subdomain": "https://environment.sangaia.org",
        "target_dirs": ["MtE", "mEnv"],
        "root_file": "environment_departments.html",
        "root_sgn_file": "sgn/environment_departments.html",
        "departments": [
            {
                "id": "biome-stewardship",
                "name_en": "Department of Biome Stewardship",
                "name_sgn": "Дэпарто эк Биомо Сэрво",
                "mandate_en": "Protecting national parks, managing cloud forest restoration, and issuing sustainable wilderness and camping permits.",
                "mandate_sgn": "Сэрво натио парко, силва рэсторато, инкаи кампинго пэрмито эмито.",
                "functions": [
                    {
                        "icon": "🗺️",
                        "title_en": "Interactive Biome Health & Forest Canopy Map",
                        "title_sgn": "Интэракто Биомо Клима & Силва Мапа",
                        "desc_en": "High-resolution satellite telemetry tracking canopy density, wetland moisture, and watershed rehabilitation across the 4 provinces.",
                        "desc_sgn": "Сателито тэлэмэтриа эк силва дэнцита, аква балансо, инкаи биомо салутиа.",
                        "action_en": "Launch Biome Map",
                        "action_sgn": "Лапидо Биомо Мапа",
                        "modal": "biomemap"
                    },
                    {
                        "icon": "🏕️",
                        "title_en": "Wilderness Entry & Alpine Camping Permits",
                        "title_sgn": "Силва Адито & Кампинго Пэрмито",
                        "desc_en": "Instant digital backcountry access passes ensuring trail quotas are preserved and leave-no-trace covenants honored.",
                        "desc_sgn": "Статим дигитало кампинго пэрмито ад протэкто виа апо эксцэсо сяни.",
                        "action_en": "Request Camping Permit",
                        "action_sgn": "Пэрмито Пэтитио",
                        "modal": "camppermit"
                    },
                    {
                        "icon": "🌲",
                        "title_en": "National Tree-Planting Registry & Tracker",
                        "title_sgn": "Натио Арборо-Плано Тракер & Сэкуро",
                        "desc_en": "Log your native pine and coastal mangrove sapling contributions under the 'One Citizen, Ten Trees' sovereign campaign.",
                        "desc_sgn": "Рэгистро тус арборо суб 'Унус Цивикано, Дэкум Арборо' натио прагма.",
                        "action_en": "Register Planted Trees",
                        "action_sgn": "Рэгистро Арборо",
                        "modal": "treeplant"
                    }
                ]
            },
            {
                "id": "wildlife-protection",
                "name_en": "Department of Wildlife Protection",
                "name_sgn": "Дэпарто эк Фэра Протэктио",
                "mandate_en": "Operating the wildlife rescue brigade, managing ethical harvest tags, and stewarding endangered coastal ecosystems.",
                "mandate_sgn": "Мануго фэра салво бригада, эколожико пискато таги, инкаи дангэро спесиэс сэрво.",
                "functions": [
                    {
                        "icon": "🦅",
                        "title_en": "24/7 Wildlife Incident & Poaching Hotline",
                        "title_sgn": "24-Ора Фэра Инсидэто & Салво Лине",
                        "desc_en": "Rapid dispatch pipeline for injured raptors, stranded marine mammals, or illegal predator encroachment reporting.",
                        "desc_sgn": "Рапидо диспачо про вунэро авис, марино фэра, вэл илегало капто.",
                        "action_en": "Report Wildlife Incident",
                        "action_sgn": "Рэпорто Инсидэто",
                        "modal": "wildlifereport"
                    },
                    {
                        "icon": "🎣",
                        "title_en": "Seasonal Ecological Harvest & Fishing Tags",
                        "title_sgn": "Сесоно Эколожико Пискато Таги Портало",
                        "desc_en": "Apply for strictly quota-regulated artisanal marine fishing permits and sustainable seasonal deer tags.",
                        "desc_sgn": "Апликатио про куота-рэгуло пискато лицэнсиа инкаи сустэнабило таги.",
                        "action_en": "Apply for Harvest Tag",
                        "action_sgn": "Аплико про Таг",
                        "modal": "harvesttag"
                    },
                    {
                        "icon": "🐬",
                        "title_en": "Interactive Endangered Species Profiles",
                        "title_sgn": "Интэракто Дангэро Спесиэс Профило",
                        "desc_en": "Live ecological trackers following recovery populations of the Sangaian Silver Seal, Cloud Leopard, and Reef Mantas.",
                        "desc_sgn": "Виво монито эк Сангаиа Аргэнто Фоко, Клауд Леопардо, инкаи Скопуло Манта.",
                        "action_en": "View Species Profiles",
                        "action_sgn": "Визо Спесиэс",
                        "modal": "species"
                    }
                ]
            },
            {
                "id": "environmental-standards",
                "name_en": "Department of Environmental Standards",
                "name_sgn": "Дэпарто эк Амбито Стандарто",
                "mandate_en": "Enforcing air and water purity mandates, monitoring industrial effluents, and managing zero-landfill recycling initiatives.",
                "mandate_sgn": "Фортис аэр инкаи аква пурита, монито индустриало дапано, инкаи зэро-ланфило.",
                "functions": [
                    {
                        "icon": "🧪",
                        "title_en": "Live Air & Watershed Quality Sensor Network",
                        "title_sgn": "Виво Аэр & Аква Квалита Сэнсоро Рэти",
                        "desc_en": "Public IoT sensor grid reporting real-time particulate matter (PM2.5), dissolved oxygen, and ocean pH telemetry.",
                        "desc_sgn": "Виво сэнсоро тэлэмэтриа эк PM2.5, аква оксигэн, инкаи осеано pH суб холо порт.",
                        "action_en": "View Sensor Telemetry",
                        "action_sgn": "Визо Сэнсоро",
                        "modal": "airsensors"
                    },
                    {
                        "icon": "🏭",
                        "title_en": "Industrial Emissions Permitting & Audits",
                        "title_sgn": "Индустриало Эмисио Пэрмито & Аудито",
                        "desc_en": "Mandatory emissions filing portal for factories, shipyards, and smelters with automated zero-pollution penalty audits.",
                        "desc_sgn": "Мандаторио эмисио филинг про фабрика куно автоматико штрафо про полутио.",
                        "action_en": "File Emissions Report",
                        "action_sgn": "Субмито Эмисио",
                        "modal": "emissions"
                    },
                    {
                        "icon": "♻️",
                        "title_en": "Hazardous Waste Drop-Off & Recycling Locator",
                        "title_sgn": "Дангэро Дапано & Рэциклинг Локаторо",
                        "desc_en": "Interactive map locating regional solar panel recycling centers, battery recovery bins, and organic composting depots.",
                        "desc_sgn": "Мапа про соларо панэло рэциклинг, батариа колго, инкаи орган-компосто.",
                        "action_en": "Find Recycling Depot",
                        "action_sgn": "Скэро Рэциклинг",
                        "modal": "recycling"
                    }
                ]
            }
        ]
    },

    "propaganda": {
        "slug": "propaganda",
        "theme": {
            "name": "Ministry of Propaganda",
            "primary": "#ea580c",
            "dark": "#c2410c",
            "deep": "#9a3412",
            "light": "#f97316",
            "pale": "#fff7ed",
            "border": "#fed7aa",
            "accent": "#f59e0b"
        },
        "title_en": "Broadcasting, Press & Religious Departments",
        "title_sgn": "Эмито, Пресо & Рэлигио Дэпартамэнто",
        "ministry_en": "Ministry of Propaganda",
        "ministry_sgn": "Министро эк Пропаго",
        "subdomain": "https://propaganda.sangaia.org",
        "target_dirs": ["mP"],
        "root_file": "propaganda_departments.html",
        "root_sgn_file": "sgn/propaganda_departments.html",
        "departments": [
            {
                "id": "state-broadcasting",
                "name_en": "Department of State Broadcasting",
                "name_sgn": "Дэпарто эк Стато Эмито",
                "mandate_en": "Operating public SPTV television channels and SNR radio transmitters, distributing civic alerts, and archiving state broadcasts.",
                "mandate_sgn": "Опэро СПТВ тэлэвизо инкаи СНР радио, дистрибуто цивико ависо, инкаи архиво эмито.",
                "functions": [
                    {
                        "icon": "📺",
                        "title_en": "Live State Broadcast & Assembly Streams",
                        "title_sgn": "Виво Стато Эмито & Парламэнто Стреам",
                        "desc_en": "Direct unedited audio/video relays of legislative sessions, presidential addresses, and provincial hearings free from advertising.",
                        "desc_sgn": "Дирэкто аудио/видео эк Корпо эк Элэкто, Арэтократ диспачи, син комэрцио.",
                        "action_en": "Watch Live Streams",
                        "action_sgn": "Визо Виво Стреам",
                        "modal": "livestreams"
                    },
                    {
                        "icon": "📦",
                        "title_en": "Civic Campaign Media Assets Archive",
                        "title_sgn": "Цивико Кампаниа Мэдиа Архиво",
                        "desc_en": "Downloadable broadcast-quality public health posters, educational audiobooks, and historical documentary footage.",
                        "desc_sgn": "Либэро даунлоадо эк салутиа постэро, эдукатио аудио-либро, инкаи историко видео.",
                        "action_en": "Download Media Assets",
                        "action_sgn": "Даунлоадо Мэдиа",
                        "modal": "mediaassets"
                    },
                    {
                        "icon": "📅",
                        "title_en": "National Calendar of Civic & Cultural Events",
                        "title_sgn": "Натио Калэндарио эк Цивико & Културал",
                        "desc_en": "Comprehensive schedule of nationwide elections, parliamentary question times, provincial folk festivals, and holiday addresses.",
                        "desc_sgn": "Тото скэдуло эк элэктио, парламэнто куэстио ора, инкаи провиткия фэстивало.",
                        "action_en": "View Civic Calendar",
                        "action_sgn": "Визо Калэндарио",
                        "modal": "civiccal"
                    }
                ]
            },
            {
                "id": "press-integrity",
                "name_en": "Department of Press Accreditation & Information Integrity",
                "name_sgn": "Дэпарто эк Пресо Акредито & Вэрита Сэкуро",
                "mandate_en": "Certifying non-partisan journalists, enforcing the anti-lobbying firewall, and maintaining transparent provenance over AI media.",
                "mandate_sgn": "Акредито журналикано син политико лоби, инкаи сэкуро АИ ватэрмарко.",
                "functions": [
                    {
                        "icon": "🪪",
                        "title_en": "Journalist Press Pass Accreditation Portal",
                        "title_sgn": "Журналикано Пресо Пасо Портало",
                        "desc_en": "Submit investigative portfolio, dual-source verification clearance, and statutory ethics oaths for Class A/B/C press credentials.",
                        "desc_sgn": "Апликатио про Пресо Пасо суб Градо А, Б, вэл Ц суб ностэр Вэрита Карта.",
                        "action_en": "Apply for Press Pass",
                        "action_sgn": "Аплико про Пасо",
                        "modal": "presspass"
                    },
                    {
                        "icon": "📰",
                        "title_en": "Public Registry of Accredited News Agencies",
                        "title_sgn": "Публико Рэгистро эк Акредито Мэдиа",
                        "desc_en": "Verify ownership transparency, independent funding disclosures, and editorial compliance for all registered newspapers and stations.",
                        "desc_sgn": "Вэрифико овнэршип транспарэнсиа инкаи финансио про шэно публико газэта.",
                        "action_en": "Inspect Registry",
                        "action_sgn": "Инспэкто Рэгистро",
                        "modal": "pressreg"
                    },
                    {
                        "icon": "⚖️",
                        "title_en": "Broadcast Code Violation & Misinformation Hotline",
                        "title_sgn": "Эмито Фалу & Мисинформатио Хэлплине",
                        "desc_en": "Citizen pipeline to report undisclosed paid lobbying, uncorrected factual inaccuracies, or un-watermarked AI deepfakes.",
                        "desc_sgn": "Канало ад рэпорто комэрциало лобинг вэл син-ватэрмарко АИ фалу ин эмито.",
                        "action_en": "Report Violation",
                        "action_sgn": "Рэпорто Фалу",
                        "modal": "infoviolation"
                    }
                ]
            },
            {
                "id": "religious-affairs",
                "name_en": "Department of Religious Affairs",
                "name_sgn": "Дэпарто эк Рэлигио Прагма",
                "mandate_en": "Overseeing spiritual construct registrations and enforcing the mandatory 85%+ community wealth-redistribution threshold.",
                "mandate_sgn": "Супэрвидо экклэсиа рэгистро инкаи фортис 85%+ рико-рэдивидо ад комунитиа.",
                "functions": [
                    {
                        "icon": "⛪",
                        "title_en": "Religious Construct Charter Registration",
                        "title_sgn": "Рэлигио Конструкто Карта Рэгистро",
                        "desc_en": "Statutory registration pipeline for new religious congregations with community shelter, soup kitchen, and audit commitments.",
                        "desc_sgn": "Рэгистро канало про ново конгрэгатио куно комунитиа салво плано.",
                        "action_en": "Register Religious Body",
                        "action_sgn": "Рэгистро Экклэсиа",
                        "modal": "churchreg"
                    },
                    {
                        "icon": "📊",
                        "title_en": "Digital Ledger of Recognized Chapels & Audits",
                        "title_sgn": "Дигитало Леджер эк Экклэсиа & Аудито",
                        "desc_en": "Searchable financial audit breakdowns of all recognized places of worship confirming adherence to wealth redistribution mandates.",
                        "desc_sgn": "Скэро-гаранто фискало аудито эк холо экклэсиа пробо 85%+ комунитиа дапано.",
                        "action_en": "Inspect Audit Ledger",
                        "action_sgn": "Инспэкто Аудито",
                        "modal": "churchaudit"
                    },
                    {
                        "icon": "🕊️",
                        "title_en": "Interfaith Calendar & Civic Unity Roster",
                        "title_sgn": "Интэр-Крэдо Калэндарио & Сонит Ростро",
                        "desc_en": "Published schedules of interfaith holy days, community charity drives, and inter-religious disaster relief coordinates.",
                        "desc_sgn": "Публико скэдуло эк сакро дио, карита инициатива, инкаи салво координатио.",
                        "action_en": "View Interfaith Calendar",
                        "action_sgn": "Визо Калэндарио",
                        "modal": "interfaithcal"
                    }
                ]
            }
        ]
    }
}

print("Loaded all 9 ministries definitions.")

