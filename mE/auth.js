// Sangaia Unified Authentication & Database Engine
// Supports Supabase PostgreSQL schema: sangaia_citizens, id_cards, government_benefits,
// education_courses, community_service_records, health_records, jail_criminal_records, citizen_history.
// Adheres strictly to the One Live Metro design system (all-lowercase, Segoe WP typography, Metro UI icons).

const SUPABASE_URL = 'https://qcgdjdnihwchjargpfcc.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFjZ2RqZG5paHdjaGphcmdwZmNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE0NzkxNTIsImV4cCI6MjEwNzA1NTE1Mn0.AfstClw4oXLj7stYL1bfyKSCMFBHZQBVBQACTT4dNLM';

const CITIZEN_REGISTRY_KEY = 'sangaia_registered_citizens';
const ACTIVE_CITIZEN_KEY = 'sangaia_active_citizen';
const ACTIVE_SESSION_KEY = 'sangaia_session';
const SUPABASE_TOKEN_KEY = 'sb-qcgdjdnihwchjargpfcc-auth-token';

// -----------------------------------------------------------------------------
// 1. Cross-Subdomain Storage & Cookie Synchronization
// -----------------------------------------------------------------------------
function getCookieDomain() {
    try {
        const host = window.location.hostname;
        if (host.endsWith('sangaia.org')) {
            return '; domain=.sangaia.org';
        }
    } catch (e) {}
    return '';
}

function setCookieVal(key, value) {
    try {
        const domain = getCookieDomain();
        const secure = (window.location.protocol === 'https:') ? '; Secure' : '';
        const maxAge = '; max-age=31536000; path=/; SameSite=Lax';
        const encoded = encodeURIComponent(value);
        if (domain) document.cookie = key + '=' + encoded + domain + maxAge + secure;
        document.cookie = key + '=' + encoded + maxAge + secure;
    } catch (e) {}
}

function getCookieVal(key) {
    try {
        const cookies = document.cookie.split(/;\s*/).reduce((acc, curr) => {
            const [k, ...v] = curr.split('=');
            if (k) acc[k.trim()] = v.join('=');
            return acc;
        }, {});
        if (cookies[key]) {
            try { return decodeURIComponent(cookies[key]); } catch (e) { return cookies[key]; }
        }
    } catch (e) {}
    return null;
}

function deleteCookieVal(key) {
    try {
        const domain = getCookieDomain();
        const past = '; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; SameSite=Lax';
        document.cookie = key + '=' + past;
        if (domain) document.cookie = key + '=' + domain + past;
    } catch (e) {}
}

const sangaiaStorage = {
    getItem: (key) => {
        try {
            const localVal = window.localStorage.getItem(key);
            if (localVal) return localVal;
        } catch(e){}
        const cookieVal = getCookieVal(key);
        if (cookieVal) {
            try { window.localStorage.setItem(key, cookieVal); } catch(e){}
            return cookieVal;
        }
        return null;
    },
    setItem: (key, value) => {
        try { window.localStorage.setItem(key, value); } catch(e){}
        setCookieVal(key, value);
    },
    removeItem: (key) => {
        try { window.localStorage.removeItem(key); } catch(e){}
        deleteCookieVal(key);
    }
};

window.sangaiaStorage = sangaiaStorage;

// -----------------------------------------------------------------------------
// 2. Citizen Registry Helper Engine (Tracks registered users across portals)
// -----------------------------------------------------------------------------
function getLocalCitizenRegistry() {
    let registry = {};
    try {
        const raw = sangaiaStorage.getItem(CITIZEN_REGISTRY_KEY);
        if (raw) registry = JSON.parse(raw);
    } catch (e) {}

    // Seed default sample verified citizen if missing
    if (!registry['john.doe@sangaia.org']) {
        registry['john.doe@sangaia.org'] = {
            id: 'sg_usr_john_doe',
            email: 'john.doe@sangaia.org',
            password: 'password123',
            full_name: 'john doe',
            sangaia_id_number: 'SGN-09FDA816',
            date_of_birth: '06/22/2010',
            issue_date: '2024-01-01',
            account_status: 'ACTIVE',
            phone_number: '+1 (555) 019-2834',
            physical_address: '402 Constitution Way, Sector 4, Capital Shesk',
            blood_type: 'O+',
            allergies: 'No Known Allergies (NKDA)',
            primary_doctor: 'Dr. Elena Vance, Shesk Sovereign Medical Center',
            education_level: 'Higher Polytechnic (B.Sc. Computational Systems)',
            territory: 'SHESK',
            province: 'SHESK',
            sex: 'M',
            height: "5'8\"",
            hair: 'Bld',
            languages: 'SGN, ENG, RUS, CHN, GER',
            under21_notice: 'not twenty-one until 06/22/2031',
            photo_url: ''
        };
    }
    return registry;
}

function saveLocalCitizen(citizen) {
    if (!citizen || !citizen.email) return;
    try {
        const registry = getLocalCitizenRegistry();
        registry[citizen.email.toLowerCase().trim()] = citizen;
        sangaiaStorage.setItem(CITIZEN_REGISTRY_KEY, JSON.stringify(registry));
    } catch (e) {}
}

function findLocalCitizen(email) {
    if (!email) return null;
    try {
        const registry = getLocalCitizenRegistry();
        return registry[email.toLowerCase().trim()] || null;
    } catch (e) {
        return null;
    }
}

// -----------------------------------------------------------------------------
// 3. Client Initialization & Supabase Client Factory
// -----------------------------------------------------------------------------
let clientInstance = null;

function initClient() {
    if (clientInstance) return clientInstance;
    if (window.supabase && typeof window.supabase.createClient === 'function') {
        try {
            clientInstance = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY, {
                auth: {
                    storage: window.localStorage,
                    autoRefreshToken: true,
                    persistSession: true,
                    detectSessionInUrl: true
                }
            });
            window.sangaiaSupabase = clientInstance;
            return clientInstance;
        } catch (e) {
            console.warn("Supabase init error:", e);
        }
    }
    return null;
}

initClient();

function ensureSupabaseLoaded(callback) {
    if (initClient()) {
        if (callback) callback(clientInstance);
        return;
    }
    if (!document.querySelector('script[data-sangaia-supabase]')) {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2';
        script.setAttribute('data-sangaia-supabase', 'true');
        script.onload = () => {
            initClient();
            if (callback) callback(clientInstance);
            if (window.SangaiaAuth) window.SangaiaAuth.refreshUI();
        };
        script.onerror = () => {
            console.warn("Supabase CDN unavailable.");
            if (callback) callback(null);
        };
        document.head.appendChild(script);
    } else {
        setTimeout(() => {
            initClient();
            if (callback) callback(clientInstance);
        }, 300);
    }
}

// -----------------------------------------------------------------------------
// 4. Navigation & Path Helpers
// -----------------------------------------------------------------------------
function getRepoRoot() {
    const path = window.location.pathname;
    if (path.includes('/mH/ddcr/sgn/')) return '../../../';
    if (path.includes('/mH/ddcr/') || path.includes('/mH/sgn/')) return '../../';
    if (path.includes('/mH/') || path.includes('/sgn/') || path.includes('/id/') || path.includes('/mE/') || path.includes('/mT/') || path.includes('/mW/') || path.includes('/mP/') || path.includes('/MdA/') || path.includes('/MiA/') || path.includes('/MoEX/') || path.includes('/MtE/') || path.includes('/articles/')) return '../';
    return './';
}

function getIdPageUrl() {
    const isSgn = window.location.pathname.includes('/sgn/') || window.location.pathname.endsWith('/sgn');
    const isHosted = window.location.hostname.endsWith('sangaia.org');
    
    if (isHosted) {
        return isSgn ? 'https://sangaia.org/sgn/id/' : 'https://sangaia.org/id/';
    }
    if (window.location.pathname.includes('/id/') || window.location.pathname.endsWith('/id') || window.location.pathname.endsWith('/id.html')) {
        return window.location.pathname.includes('id.html') ? 'id.html' : 'index.html';
    }
    const root = getRepoRoot();
    return isSgn ? root + 'sgn/id/' : root + 'id/';
}

window.getIdPageUrl = getIdPageUrl;
window.getRepoRoot = getRepoRoot;

// -----------------------------------------------------------------------------
// 5. Stored Session & Token Helpers
// -----------------------------------------------------------------------------
function getSupabaseStoredSession() {
    try {
        let raw = window.localStorage.getItem(SUPABASE_TOKEN_KEY);
        if (!raw) {
            for (let i = 0; i < window.localStorage.length; i++) {
                const k = window.localStorage.key(i);
                if (k && k.startsWith('sb-') && k.endsWith('-auth-token')) {
                    raw = window.localStorage.getItem(k);
                    break;
                }
            }
        }
        if (raw) {
            const parsed = JSON.parse(raw);
            if (parsed && (parsed.user || parsed.access_token)) {
                return parsed;
            }
        }
    } catch (e) {}
    return null;
}

const SAMPLE_CITIZEN = {
    id: 'sg_usr_sample_01',
    sangaia_id_number: 'SGN-09FDA816',
    full_name: 'john doe',
    date_of_birth: '06/22/2010',
    issue_date: '2024-01-01',
    account_status: 'ACTIVE',
    phone_number: '+1 (555) 019-2834',
    physical_address: '402 Constitution Way, Sector 4, Capital Shesk',
    blood_type: 'O+',
    allergies: 'No Known Allergies (NKDA)',
    primary_doctor: 'Dr. Elena Vance, Shesk Sovereign Medical Center',
    education_level: 'Higher Polytechnic (B.Sc. Computational Systems)',
    territory: 'SHESK',
    province: 'SHESK',
    sex: 'M',
    height: "5'8\"",
    hair: 'Bld',
    languages: 'SGN, ENG, RUS, CHN, GER',
    under21_notice: 'not twenty-one until 06/22/2031',
    photo_url: '',
    healthcare_tier: 'Tier 1 Universal Healthcare',
    wage_floor: '$25.00/hr Statutory Wage Floor'
};

// -----------------------------------------------------------------------------
// 6. SangaiaAuth Unified Interface
// -----------------------------------------------------------------------------
window.SangaiaAuth = {
    client: () => initClient(),

    async getSession() {
        // 1. Check Supabase client
        const client = initClient();
        if (client && client.auth) {
            try {
                const { data: { session }, error } = await client.auth.getSession();
                if (session && session.user) return session;
            } catch (e) {}
        }

        // 2. Check Supabase localStorage token
        const supaSession = getSupabaseStoredSession();
        if (supaSession && supaSession.user) return supaSession;

        // 3. Check custom active session
        try {
            const raw = sangaiaStorage.getItem(ACTIVE_SESSION_KEY);
            if (raw) {
                const parsed = JSON.parse(raw);
                if (parsed && (parsed.user || parsed.access_token)) {
                    return parsed.user ? parsed : { user: parsed };
                }
            }
        } catch (e) {}

        // 4. Check active citizen
        try {
            const rawCit = sangaiaStorage.getItem(ACTIVE_CITIZEN_KEY);
            if (rawCit) {
                const cit = JSON.parse(rawCit);
                if (cit && cit.full_name) {
                    return {
                        access_token: 'sg_bearer_active',
                        token_type: 'bearer',
                        user: {
                            id: cit.id || 'sg_usr_active',
                            email: cit.email || 'citizen@sangaia.org',
                            user_metadata: {
                                full_name: cit.full_name,
                                territory: cit.territory || cit.province || 'SHESK',
                                sangaia_id_number: cit.sangaia_id_number
                            }
                        }
                    };
                }
            }
        } catch (e) {}

        return null;
    },

    async getUser() {
        const session = await this.getSession();
        return session ? session.user : null;
    },

    async getCitizenRecord(userId) {
        const client = initClient();
        if (client && userId) {
            try {
                const { data, error } = await client
                    .from('sangaia_citizens')
                    .select('*')
                    .eq('id', userId)
                    .single();
                if (data && data.full_name) return data;
            } catch (e) {}
        }

        // Check local storage active citizen
        try {
            const raw = sangaiaStorage.getItem(ACTIVE_CITIZEN_KEY);
            if (raw) {
                const cit = JSON.parse(raw);
                if (cit && cit.full_name && (!userId || cit.id === userId)) return cit;
            }
        } catch (e) {}

        return null;
    },

    // Query all related dockets from Supabase
    async getFullCitizenProfile(userId) {
        const client = initClient();
        let citizen = await this.getCitizenRecord(userId);
        let idCard = null;
        let benefits = [];
        let courses = [];
        let healthRecords = [];
        let communityRecords = [];
        let criminalRecords = [];
        let citizenHistory = [];

        if (client) {
            try {
                const promises = [
                    (async () => {
                        try {
                            let q = client.from('id_cards').select('*');
                            if (citizen?.sangaia_id_number) {
                                q = q.eq('id_number', citizen.sangaia_id_number);
                            } else if (citizen?.full_name) {
                                q = q.ilike('full_name', citizen.full_name);
                            }
                            const res = await q.order('created_at', { ascending: false }).limit(1).maybeSingle();
                            return res?.data || null;
                        } catch(e) { return null; }
                    })(),
                    userId ? client.from('government_benefits').select('*').eq('citizen_id', userId) : Promise.resolve({ data: [] }),
                    userId ? client.from('education_courses').select('*').eq('citizen_id', userId) : Promise.resolve({ data: [] }),
                    userId ? client.from('health_records').select('*').eq('citizen_id', userId) : Promise.resolve({ data: [] }),
                    userId ? client.from('community_service_records').select('*').eq('citizen_id', userId) : Promise.resolve({ data: [] }),
                    userId ? client.from('jail_criminal_records').select('*').eq('citizen_id', userId) : Promise.resolve({ data: [] }),
                    userId ? client.from('citizen_history').select('*').eq('citizen_id', userId).order('changed_at', { ascending: false }) : Promise.resolve({ data: [] })
                ];

                const [cardData, benRes, eduRes, hltRes, comRes, crmRes, hisRes] = await Promise.all(promises);

                if (cardData) idCard = cardData;
                if (benRes?.data && benRes.data.length) benefits = benRes.data;
                if (eduRes?.data && eduRes.data.length) courses = eduRes.data;
                if (hltRes?.data && hltRes.data.length) healthRecords = hltRes.data;
                if (comRes?.data && comRes.data.length) communityRecords = comRes.data;
                if (crmRes?.data && crmRes.data.length) criminalRecords = crmRes.data;
                if (hisRes?.data && hisRes.data.length) citizenHistory = hisRes.data;
            } catch (e) {
                console.warn("Supabase profile load warning:", e);
            }
        }

        if (!citizen) {
            citizen = { ...SAMPLE_CITIZEN, id: userId };
        }

        if (!idCard) {
            idCard = {
                id_number: citizen.sangaia_id_number || SAMPLE_CITIZEN.sangaia_id_number,
                full_name: citizen.full_name || SAMPLE_CITIZEN.full_name,
                dob: citizen.date_of_birth || SAMPLE_CITIZEN.date_of_birth,
                sex: citizen.sex || SAMPLE_CITIZEN.sex,
                status: citizen.account_status || SAMPLE_CITIZEN.account_status,
                hair: citizen.hair || SAMPLE_CITIZEN.hair,
                height: citizen.height || SAMPLE_CITIZEN.height,
                province: citizen.territory || citizen.province || SAMPLE_CITIZEN.province,
                languages: citizen.languages || SAMPLE_CITIZEN.languages,
                under21_notice: citizen.under21_notice || SAMPLE_CITIZEN.under21_notice,
                photo_url: citizen.photo_url || SAMPLE_CITIZEN.photo_url
            };
        }

        if (!benefits.length) {
            benefits = [
                { id: 'ben-01', benefit_name: 'Universal Healthcare Tier 1', description: 'Comprehensive state-funded emergency, specialist, dental, and pharmaceutical coverage.', status: 'Active', granted_at: '2024-01-01' },
                { id: 'ben-02', benefit_name: 'Statutory Living Wage Guarantee', description: 'Guaranteed wage protection floor of $25.00/hr ($1,000/week) across all registered employers.', status: 'Active', granted_at: '2024-01-01' },
                { id: 'ben-03', benefit_name: 'Tuition-Free Higher Education Grant', description: 'Article 9 statutory education voucher for accredited provincial universities.', status: 'Active', granted_at: '2024-01-01' },
                { id: 'ben-04', benefit_name: 'Inter-Provincial Rapid Rail Pass', description: 'Zero-fare public passenger transit across New Jasper, New Madison, Liveland, Sentinel, and Columbia.', status: 'Active', granted_at: '2024-01-01' }
            ];
        }

        if (!courses.length) {
            courses = [
                { id: 'edu-01', course_code: 'SNG-101', course_title: 'Constitutional Virtues & Meritocracy', institution: 'Ministry of Education', credits: 3, grade: 'A', status: 'Completed', enrolled_at: '2024-09-01', completed_at: '2024-12-15' },
                { id: 'edu-02', course_code: 'SNG-204', course_title: 'Macroeconomics & Public Debt Solvency', institution: 'Shesk Sovereign University', credits: 4, grade: 'A-', status: 'Completed', enrolled_at: '2025-01-15', completed_at: '2025-05-20' },
                { id: 'edu-03', course_code: 'SNG-310', course_title: 'Provincial Biome Conservation & Ecology', institution: 'Madison Agricultural Institute', credits: 3, grade: 'Enrolled', status: 'Enrolled', enrolled_at: '2026-02-01', completed_at: null }
            ];
        }

        if (!healthRecords.length) {
            healthRecords = [
                { id: 'hlt-01', record_type: 'Annual Preventative Exam', title: 'Comprehensive Wellness & Biometrics Check', facility_name: 'Shesk Sovereign University Hospital', doctor_name: 'Dr. Elena Vance', record_date: '2025-11-10', description: 'Routine statutory physical examination. Blood pressure 118/76, ECG nominal, blood panel within normal limits.' },
                { id: 'hlt-02', record_type: 'Immunization Registry', title: 'Universal Respiratory & Seasonal Protection', facility_name: 'Capital Shesk Public Health Center', doctor_name: 'Dr. Marcus Hall', record_date: '2025-10-04', description: 'Administered annual statutory influenza and seasonal booster under national hygiene protocol.' },
                { id: 'hlt-03', record_type: 'Clinical Laboratory', title: 'Comprehensive Metabolic & Lipid Panel', facility_name: 'Ministry of Healthcare Diagnostic Hub', doctor_name: 'Dr. Elena Vance', record_date: '2025-04-18', description: 'Lipid panel normal, metabolic indices optimal. Zero chronic contraindications.' }
            ];
        }

        if (!communityRecords.length) {
            communityRecords = [
                { id: 'com-01', organization_name: 'Shesk River Biome Restoration Corps', activity_description: 'Native riparian flora replanting and water runoff telemetry inspection.', hours: 32.5, supervisor_name: 'Alden Thorne', supervisor_contact: 'thorne.a@sentinel.sangaia.org', status: 'Approved', served_on: '2025-08-14' },
                { id: 'com-02', organization_name: 'Provincial Food Sovereignty Cooperative', activity_description: 'Agricultural harvest sorting and civic meal delivery coordination in Madison Basin.', hours: 24.0, supervisor_name: 'Lydia Croft', supervisor_contact: 'croft.l@madison.sangaia.org', status: 'Approved', served_on: '2025-12-02' }
            ];
        }

        if (!criminalRecords.length) {
            criminalRecords = []; // Clean record!
        }

        if (!citizenHistory.length) {
            citizenHistory = [
                { id: 'his-01', change_type: 'Biometric Credential Issued', old_value: 'Unregistered', new_value: 'Statutory Active Citizen', notes: 'Naturalization oath administered and sovereign identity credential activated.', changed_at: '2024-01-01T09:00:00Z' },
                { id: 'his-02', change_type: 'Address Verification', old_value: 'Sector 2, Shesk', new_value: citizen.physical_address || SAMPLE_CITIZEN.physical_address, notes: 'Residential registry updated with Provincial Civil Registrar.', changed_at: '2025-03-15T14:30:00Z' }
            ];
        }

        return {
            citizen,
            idCard,
            benefits,
            courses,
            healthRecords,
            communityRecords,
            criminalRecords,
            citizenHistory
        };
    },

    // Strict Sign-In Verification matching exact requirements:
    // - "user not found" if there isn't a user with that email
    // - "incorrect password" if the password is wrong
    // - "This info doesn't exist" if both are wrong
    async signIn(email, password) {
        const cleanEmail = (email || '').trim().toLowerCase();
        const cleanPassword = (password || '').trim();

        if (!cleanEmail && !cleanPassword) {
            throw new Error("This info doesn't exist");
        }
        if (!cleanEmail) {
            throw new Error("user not found");
        }
        if (!cleanPassword) {
            throw new Error("incorrect password");
        }

        const client = initClient();
        const registry = getLocalCitizenRegistry();
        let remoteSession = null;
        let remoteUser = null;
        let supabaseSuccess = false;

        // Try Supabase authentication if client is available
        if (client && client.auth) {
            try {
                const res = await client.auth.signInWithPassword({ email: cleanEmail, password: cleanPassword });
                if (res.data && res.data.session) {
                    remoteSession = res.data.session;
                    remoteUser = res.data.user;
                    supabaseSuccess = true;
                }
            } catch (err) {
                // Handled in three-way verification below
            }
        }

        // If Supabase authentication succeeded
        if (supabaseSuccess && remoteSession && remoteUser) {
            let citizen = await this.getCitizenRecord(remoteUser.id);
            if (!citizen) {
                const name = remoteUser.user_metadata?.full_name || cleanEmail.split('@')[0].replace(/[._-]/g, ' ');
                citizen = {
                    id: remoteUser.id,
                    email: cleanEmail,
                    password: cleanPassword,
                    full_name: name,
                    sangaia_id_number: 'SGN-' + remoteUser.id.replace(/-/g, '').substring(0, 8).toUpperCase(),
                    date_of_birth: '06/22/2010',
                    issue_date: new Date().toISOString().split('T')[0],
                    account_status: 'ACTIVE',
                    phone_number: '+1 (555) 019-2834',
                    physical_address: '402 Constitution Way, Sector 4, Capital Shesk',
                    blood_type: 'O+',
                    allergies: 'No Known Allergies (NKDA)',
                    primary_doctor: 'Dr. Elena Vance, Shesk Sovereign Medical Center',
                    education_level: 'Higher Polytechnic',
                    province: 'SHESK',
                    territory: 'SHESK'
                };
            }
            citizen.password = cleanPassword;
            saveLocalCitizen(citizen);
            sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(citizen));
            sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(remoteSession));
            await this.refreshUI();
            this.notifyAuthChange(remoteSession, remoteUser);
            return { session: remoteSession, user: remoteUser, citizen };
        }

        // Three-way verification against registered citizen registry:
        const userWithEmail = cleanEmail ? registry[cleanEmail] : null;
        const anyUserWithPassword = cleanPassword ? Object.values(registry).some(u => u.password && u.password === cleanPassword) : false;

        // Case 1: Email exists in system
        if (userWithEmail) {
            if (userWithEmail.password && userWithEmail.password === cleanPassword) {
                const session = {
                    access_token: 'sg_live_' + Date.now().toString(36),
                    user: {
                        id: userWithEmail.id,
                        email: cleanEmail,
                        user_metadata: {
                            full_name: userWithEmail.full_name,
                            territory: userWithEmail.territory || userWithEmail.province,
                            sangaia_id_number: userWithEmail.sangaia_id_number
                        }
                    }
                };
                sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(userWithEmail));
                sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(session));
                await this.refreshUI();
                this.notifyAuthChange(session, session.user);
                return { session, user: session.user, citizen: userWithEmail };
            } else {
                throw new Error("incorrect password");
            }
        }

        // Case 2 & 3: Email does NOT exist in system
        if (anyUserWithPassword) {
            throw new Error("user not found");
        } else {
            throw new Error("This info doesn't exist");
        }
    },

    async signUp(params) {
        const { email, password, fullName, dob, province, address, phone } = params;
        if (!email || !email.trim()) throw new Error("Email is required.");
        if (!password) throw new Error("Password is required.");

        const cleanEmail = email.trim().toLowerCase();
        const client = initClient();
        let remoteUserId = null;
        let remoteSession = null;

        if (client && client.auth) {
            try {
                const res = await client.auth.signUp({
                    email: cleanEmail,
                    password: password,
                    options: {
                        data: {
                            full_name: fullName,
                            territory: province
                        }
                    }
                });
                if (res.data && res.data.user) {
                    remoteUserId = res.data.user.id;
                    remoteSession = res.data.session;
                }
            } catch (err) {
                console.warn("Supabase remote signup error, creating local docket:", err);
            }
        }

        const citizenId = 'SGN-' + Math.floor(0x10000000 + Math.random() * 0x8fffffff).toString(16).toUpperCase();
        const userId = remoteUserId || ('sg_usr_' + Date.now().toString(36));

        const citizenRecord = {
            id: userId,
            sangaia_id_number: citizenId,
            full_name: fullName.toLowerCase(),
            date_of_birth: dob || '06/22/2010',
            issue_date: new Date().toISOString().split('T')[0],
            account_status: 'ACTIVE',
            phone_number: phone || '+1 (555) 019-2834',
            physical_address: address || '101 Republic Avenue, Capital Shesk',
            blood_type: 'O+',
            allergies: 'No Known Allergies (NKDA)',
            primary_doctor: 'Dr. Elena Vance, Shesk Sovereign Medical Center',
            education_level: 'Higher Polytechnic',
            territory: (province || 'SHESK').toUpperCase(),
            province: (province || 'SHESK').toUpperCase(),
            sex: 'M',
            height: "5'8\"",
            hair: 'Bld',
            languages: 'SGN, ENG, RUS, CHN, GER',
            under21_notice: 'not twenty-one until 06/22/2031',
            photo_url: '',
            email: cleanEmail,
            password: password
        };

        saveLocalCitizen(citizenRecord);
        sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(citizenRecord));
        const session = remoteSession || {
            access_token: 'sg_bearer_' + Date.now(),
            user: { id: userId, email: cleanEmail, user_metadata: { full_name: fullName, territory: province } }
        };
        sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(session));

        // Insert into Supabase id_cards table if client available
        if (client) {
            try {
                await client.from('id_cards').insert({
                    full_name: fullName.toLowerCase(),
                    id_number: citizenId,
                    dob: dob || '06/22/2010',
                    sex: 'M',
                    status: 'ACTIVE',
                    hair: 'Bld',
                    height: "5'8\"",
                    province: (province || 'SHESK').toUpperCase(),
                    languages: 'SGN, ENG, RUS, CHN, GER',
                    under21_notice: 'not twenty-one until 06/22/2031',
                    photo_url: ''
                });
            } catch (e) {}
        }

        await this.refreshUI();
        this.notifyAuthChange(session, session.user);
        return { session, user: session.user, citizen: citizenRecord };
    },

    async signOut() {
        const client = initClient();
        if (client && client.auth) {
            try { await client.auth.signOut(); } catch(e){}
        }
        sangaiaStorage.removeItem(SUPABASE_TOKEN_KEY);
        sangaiaStorage.removeItem(ACTIVE_SESSION_KEY);
        sangaiaStorage.removeItem(ACTIVE_CITIZEN_KEY);

        await this.refreshUI();
        this.notifyAuthChange(null, null);

        if (window.location.pathname.includes('/id/') || window.location.pathname.endsWith('/id') || window.location.pathname.includes('id.html')) {
            window.location.reload();
        }
    },

    notifyAuthChange(session, user) {
        const event = new CustomEvent('sangaia:auth-changed', {
            detail: { session, user }
        });
        document.dispatchEvent(event);
    },

    async refreshUI() {
        await updateAuthWidgets();
    }
};

// -----------------------------------------------------------------------------
// 7. Header Profile Widget DOM Updater
// -----------------------------------------------------------------------------
function renderAuthenticatedProfile(profileMenu, citizen, user) {
    if (!profileMenu) return;
    const rawName = (citizen && citizen.full_name) || (user && user.user_metadata?.full_name) || (user && user.email ? user.email.split('@')[0] : 'john doe');
    const name = rawName.toLowerCase();
    const citizenId = ((citizen && citizen.sangaia_id_number) || 'SGN-09FDA816').toLowerCase();
    const initial = (name.charAt(0) || 'j').toUpperCase();
    const idUrl = getIdPageUrl();

    profileMenu.className = 'user-profile-btn authenticated';
    profileMenu.innerHTML = `
      <div style="width:20px; height:20px; border-radius:2px; background:var(--primary, #0078d4); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:10px; flex-shrink:0; line-height:1; user-select:none;">
        ${initial}
      </div>
      <span style="max-width:130px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; font-weight:600;">${name}</span>
    `;
    profileMenu.href = idUrl;
    profileMenu.title = 'citizen ' + citizenId + ' (' + name + ') - view sangaia id';
}

function renderUnauthenticatedProfile(profileMenu) {
    if (!profileMenu) return;
    const idUrl = getIdPageUrl();
    profileMenu.className = 'user-profile-btn unauthenticated';
    profileMenu.innerHTML = `
      <span class="mif-user"></span>
      <span>sign in</span>
    `;
    profileMenu.href = idUrl;
    profileMenu.title = 'sign in to sangaia id';
}

async function updateAuthWidgets() {
    const profileMenu = document.getElementById('userProfileMenu');
    if (!profileMenu) return;

    // Fast check if any session or citizen exists
    let supaSession = getSupabaseStoredSession();
    let citizen = null;
    try {
        const rawCit = sangaiaStorage.getItem(ACTIVE_CITIZEN_KEY);
        if (rawCit) citizen = JSON.parse(rawCit);
    } catch (e) {}

    if (citizen && citizen.full_name) {
        renderAuthenticatedProfile(profileMenu, citizen, supaSession ? supaSession.user : null);
    } else if (supaSession && supaSession.user) {
        const name = supaSession.user.user_metadata?.full_name || supaSession.user.email?.split('@')[0] || 'citizen';
        renderAuthenticatedProfile(profileMenu, { full_name: name, sangaia_id_number: 'SGN-09FDA816' }, supaSession.user);
    } else {
        renderUnauthenticatedProfile(profileMenu);
    }

    // Asynchronous verification with Supabase
    try {
        const client = initClient();
        if (client && client.auth) {
            const { data: { session } } = await client.auth.getSession();
            if (session && session.user) {
                const { data } = await client.from('sangaia_citizens').select('*').eq('id', session.user.id).single();
                if (data && data.full_name) {
                    renderAuthenticatedProfile(profileMenu, data, session.user);
                    sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(data));
                }
            } else if (!citizen) {
                renderUnauthenticatedProfile(profileMenu);
            }
        }
    } catch (e) {}
}

// -----------------------------------------------------------------------------
// 8. Lifecycle Initialization
// -----------------------------------------------------------------------------
function initAuthLifecycle() {
    updateAuthWidgets();

    window.addEventListener('storage', (e) => {
        if (e.key === ACTIVE_CITIZEN_KEY || e.key === ACTIVE_SESSION_KEY || e.key === SUPABASE_TOKEN_KEY) {
            updateAuthWidgets();
        }
    });

    ensureSupabaseLoaded((client) => {
        if (client && client.auth) {
            client.auth.onAuthStateChange((event, session) => {
                if (session) {
                    updateAuthWidgets();
                    window.SangaiaAuth.notifyAuthChange(session, session.user);
                } else if (event === 'SIGNED_OUT') {
                    updateAuthWidgets();
                    window.SangaiaAuth.notifyAuthChange(null, null);
                }
            });
        }
    });
}

if (document.readyState !== 'loading') {
    initAuthLifecycle();
} else {
    document.addEventListener('DOMContentLoaded', initAuthLifecycle);
}
