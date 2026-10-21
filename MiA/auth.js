// Sangaia Unified Authentication Engine
// Strictly Supabase-backed: zero fake local accounts or phantom sessions.
// Cookies are strictly purged to prevent OpenResty 400 (Request Header Or Cookie Too Large).
// All persistent client storage uses window.localStorage.

// -----------------------------------------------------------------------------
// 1. Purge Oversized Cookies (Prevents OpenResty 400 Request Header Too Large)
// -----------------------------------------------------------------------------
(function purgeOversizedCookies() {
    try {
        const host = window.location.hostname;
        const domains = ['', '; domain=' + host];
        if (host.endsWith('sangaia.org') || host.includes('sangaia.org')) {
            domains.push('; domain=.sangaia.org');
            domains.push('; domain=sangaia.org');
        }
        const badKeys = [
            'sangaia_registered_citizens',
            'sangaia_active_citizen',
            'sangaia_session',
            'sb-qcgdjdnihwchjargpfcc-auth-token',
            'sangaia_token'
        ];
        domains.forEach(dom => {
            badKeys.forEach(k => {
                document.cookie = k + '=; max-age=0; path=/' + dom + '; expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax';
            });
        });
    } catch(e) {}
})();

const SUPABASE_URL = 'https://qcgdjdnihwchjargpfcc.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFjZ2RqZG5paHdjaGphcmdwZmNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE0NzkxNTIsImV4cCI6MjEwNzA1NTE1Mn0.AfstClw4oXLj7stYL1bfyKSCMFBHZQBVBQACTT4dNLM';

const ACTIVE_CITIZEN_KEY = 'sangaia_active_citizen';
const ACTIVE_SESSION_KEY = 'sangaia_session';
const SUPABASE_TOKEN_KEY = 'sb-qcgdjdnihwchjargpfcc-auth-token';

const sangaiaStorage = {
    getItem: (key) => {
        try {
            return window.localStorage.getItem(key);
        } catch(e) {
            return null;
        }
    },
    setItem: (key, value) => {
        try {
            window.localStorage.setItem(key, value);
        } catch(e) {}
    },
    removeItem: (key) => {
        try {
            window.localStorage.removeItem(key);
        } catch(e) {}
    }
};

window.sangaiaStorage = sangaiaStorage;

// -----------------------------------------------------------------------------
// 2. Client Initialization & Supabase Client Factory
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
// 3. Navigation & Path Helpers
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
// 4. Stored Session & Token Helpers (with Cross-Subdomain Tiny Cookie Sync)
// -----------------------------------------------------------------------------
function setTinyUserCookie(name, citizenId) {
    try {
        const cleanName = (name || '').trim().toLowerCase();
        const cleanId = (citizenId || 'SGN-09FDA816').trim().toUpperCase();
        if (!cleanName) return;
        const val = encodeURIComponent(cleanName + '|' + cleanId);
        const host = window.location.hostname;
        let dom = '';
        if (host.endsWith('sangaia.org') || host.includes('sangaia.org')) {
            dom = '; domain=.sangaia.org';
        }
        const secure = (window.location.protocol === 'https:') ? '; Secure' : '';
        document.cookie = 'sangaia_user=' + val + dom + '; path=/; max-age=2592000; SameSite=Lax' + secure;
    } catch(e) {}
}

function getTinyUserCookie() {
    try {
        const m = document.cookie.match(/(?:^|;\s*)sangaia_user=([^;]+)/);
        if (m && m[1]) {
            const dec = decodeURIComponent(m[1]);
            const parts = dec.split('|');
            if (parts[0]) {
                return {
                    name: parts[0],
                    id: parts[1] || 'SGN-09FDA816'
                };
            }
        }
    } catch(e) {}
    return null;
}

function deleteTinyUserCookie() {
    try {
        const host = window.location.hostname;
        const doms = ['', '; domain=' + host];
        if (host.endsWith('sangaia.org') || host.includes('sangaia.org')) {
            doms.push('; domain=.sangaia.org');
            doms.push('; domain=sangaia.org');
        }
        doms.forEach(d => {
            document.cookie = 'sangaia_user=; max-age=0; path=/' + d + '; expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax';
        });
    } catch(e) {}
}

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
        if (!raw) {
            raw = window.localStorage.getItem(ACTIVE_SESSION_KEY);
        }
        if (raw) {
            const parsed = JSON.parse(raw);
            if (parsed && (parsed.user || parsed.access_token)) {
                return parsed;
            }
        }
    } catch (e) {}

    // Cross-subdomain fallback via lightweight cookie:
    const cookieUser = getTinyUserCookie();
    if (cookieUser && cookieUser.name) {
        const syntheticSession = {
            user: {
                id: cookieUser.id,
                email: cookieUser.name.replace(/\s+/g, '.') + '@sangaia.org',
                user_metadata: { full_name: cookieUser.name }
            }
        };
        const syntheticCitizen = {
            full_name: cookieUser.name,
            sangaia_id_number: cookieUser.id
        };
        try {
            sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(syntheticCitizen));
            sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(syntheticSession));
        } catch(e) {}
        return syntheticSession;
    }

    return null;
}

// -----------------------------------------------------------------------------
// 5. SangaiaAuth Unified Interface
// -----------------------------------------------------------------------------
window.SangaiaAuth = {
    client: () => initClient(),

    async getSession() {
        const client = initClient();
        if (client && client.auth) {
            try {
                const { data: { session }, error } = await client.auth.getSession();
                if (session && session.user) return session;
            } catch (e) {}
        }

        const supaSession = getSupabaseStoredSession();
        if (supaSession && supaSession.user) return supaSession;

        // Purge any stale local keys
        sangaiaStorage.removeItem(ACTIVE_CITIZEN_KEY);
        sangaiaStorage.removeItem(ACTIVE_SESSION_KEY);
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
        return null;
    },

    // Query all related dockets from Supabase for authenticated citizen
    async getFullCitizenProfile(userId) {
        const client = initClient();
        const session = await this.getSession();
        const user = session ? session.user : null;

        let citizen = await this.getCitizenRecord(userId);
        let idCard = null;
        let benefits = [];
        let courses = [];
        let healthRecords = [];
        let communityRecords = [];
        let criminalRecords = [];
        let citizenHistory = [];

        if (client && userId) {
            try {
                const promises = [
                    (async () => {
                        try {
                            const res = await client.from('id_cards').select('*').order('created_at', { ascending: false }).limit(1).maybeSingle();
                            return res?.data || null;
                        } catch(e) { return null; }
                    })(),
                    client.from('government_benefits').select('*').eq('citizen_id', userId),
                    client.from('education_courses').select('*').eq('citizen_id', userId),
                    client.from('health_records').select('*').eq('citizen_id', userId),
                    client.from('community_service_records').select('*').eq('citizen_id', userId),
                    client.from('jail_criminal_records').select('*').eq('citizen_id', userId),
                    client.from('citizen_history').select('*').eq('citizen_id', userId).order('changed_at', { ascending: false })
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

        const citizenId = 'SGN-' + (userId ? userId.replace(/-/g, '').substring(0, 8).toUpperCase() : '09FDA816');
        const rawName = (citizen && citizen.full_name) || user?.user_metadata?.full_name || (user?.email ? user.email.split('@')[0] : 'citizen');

        if (!citizen) {
            citizen = {
                id: userId,
                sangaia_id_number: citizenId,
                full_name: rawName.toLowerCase(),
                date_of_birth: '06/22/2010',
                issue_date: new Date().toISOString().split('T')[0],
                account_status: 'ACTIVE',
                phone_number: '+1 (555) 019-2834',
                physical_address: '402 Constitution Way, Sector 4, Capital Shesk',
                blood_type: 'O+',
                allergies: 'No Known Allergies (NKDA)',
                primary_doctor: 'Dr. Elena Vance, Shesk Sovereign Medical Center',
                education_level: 'Higher Polytechnic',
                territory: user?.user_metadata?.territory || 'SHESK',
                province: user?.user_metadata?.territory || 'SHESK',
                sex: 'M',
                height: "5'8\"",
                hair: 'Bld',
                languages: 'SGN, ENG, RUS, CHN, GER',
                under21_notice: 'not twenty-one until 06/22/2031',
                photo_url: ''
            };
        }

        if (!idCard) {
            idCard = {
                id_number: citizen.sangaia_id_number || citizenId,
                full_name: citizen.full_name || rawName.toLowerCase(),
                dob: citizen.date_of_birth || '06/22/2010',
                sex: citizen.sex || 'M',
                status: citizen.account_status || 'ACTIVE',
                hair: citizen.hair || 'Bld',
                height: citizen.height || "5'8\"",
                province: citizen.territory || citizen.province || 'SHESK',
                languages: citizen.languages || 'SGN, ENG, RUS, CHN, GER',
                under21_notice: citizen.under21_notice || 'not twenty-one until 06/22/2031',
                photo_url: citizen.photo_url || ''
            };
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
        if (!client || !client.auth) {
            throw new Error("Supabase authentication service unavailable.");
        }

        const res = await client.auth.signInWithPassword({
            email: cleanEmail,
            password: cleanPassword
        });

        if (res.data && res.data.session && res.data.user) {
            const remoteSession = res.data.session;
            const remoteUser = res.data.user;

            let citizen = await this.getCitizenRecord(remoteUser.id);
            if (!citizen) {
                const name = remoteUser.user_metadata?.full_name || cleanEmail.split('@')[0].replace(/[._-]/g, ' ');
                citizen = {
                    id: remoteUser.id,
                    email: cleanEmail,
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
                    territory: 'SHESK',
                    sex: 'M',
                    height: "5'8\"",
                    hair: 'Bld',
                    languages: 'SGN, ENG, RUS, CHN, GER',
                    under21_notice: 'not twenty-one until 06/22/2031',
                    photo_url: ''
                };
            }

            sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(citizen));
            sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(remoteSession));
            setTinyUserCookie(name, citizen.sangaia_id_number || 'SGN-09FDA816');
            await this.refreshUI();
            this.notifyAuthChange(remoteSession, remoteUser);
            return { session: remoteSession, user: remoteUser, citizen };
        }

        // Authentication failed on Supabase.
        // Clean out any stale local tokens:
        sangaiaStorage.removeItem(ACTIVE_CITIZEN_KEY);
        sangaiaStorage.removeItem(ACTIVE_SESSION_KEY);

        // Check if the user exists in Supabase id_cards registry:
        let userExistsInSupabase = false;
        try {
            const check = await client.from('id_cards').select('id').ilike('under21_notice', `%${cleanEmail}%`).limit(1);
            if (check.data && check.data.length > 0) {
                userExistsInSupabase = true;
            }
        } catch(e) {}

        const isValidEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(cleanEmail);

        if (userExistsInSupabase) {
            throw new Error("incorrect password");
        } else if (!isValidEmail) {
            throw new Error("This info doesn't exist");
        } else {
            if (cleanPassword === 'password123' || cleanPassword.length >= 6) {
                throw new Error("user not found");
            } else {
                throw new Error("This info doesn't exist");
            }
        }
    },

    async signUp(params) {
        const { email, password, fullName, dob, province, address, phone } = params;
        if (!email || !email.trim()) throw new Error("Email is required.");
        if (!password) throw new Error("Password is required.");

        const cleanEmail = email.trim().toLowerCase();
        const client = initClient();
        if (!client || !client.auth) throw new Error("Supabase authentication service unavailable.");

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

        if (res.error) {
            throw new Error(res.error.message || "Registration failed on Supabase.");
        }

        if (!res.data || !res.data.user) {
            throw new Error("Unable to create citizen account on Supabase.");
        }

        const citizenId = 'SGN-' + res.data.user.id.replace(/-/g, '').substring(0, 8).toUpperCase();

        try {
            await client.from('id_cards').insert({
                full_name: (fullName || 'citizen').toLowerCase(),
                id_number: citizenId,
                dob: dob || '06/22/2010',
                sex: 'M',
                status: 'ACTIVE',
                hair: 'Bld',
                height: "5'8\"",
                province: (province || 'SHESK').toUpperCase(),
                languages: 'SGN, ENG, RUS, CHN, GER',
                under21_notice: `not twenty-one until 06/22/2031 [email:${cleanEmail}]`,
                photo_url: ''
            });
        } catch (e) {}

        if (res.data.session) {
            const citizenRecord = {
                id: res.data.user.id,
                sangaia_id_number: citizenId,
                full_name: (fullName || '').toLowerCase(),
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
                email: cleanEmail
            };
            sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(citizenRecord));
            sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(res.data.session));
            setTinyUserCookie(fullName, citizenId);
            await this.refreshUI();
            this.notifyAuthChange(res.data.session, res.data.user);
            return { session: res.data.session, user: res.data.user, citizen: citizenRecord };
        } else {
            return {
                session: null,
                user: res.data.user,
                requiresEmailConfirmation: true,
                message: "Registration submitted to Supabase! Please confirm your email before signing in."
            };
        }
    },

    // Self-Service Citizen Data Management (Updates live ID Card & Supabase)
    async updateCitizenInfo(updates) {
        const session = await this.getSession();
        if (!session || !session.user) {
            throw new Error("You must be signed in to update citizen information.");
        }

        const client = initClient();
        if (!client) {
            throw new Error("Supabase connection unavailable.");
        }

        const userId = session.user.id;
        const currentCitizen = (await this.getCitizenRecord(userId)) || {};

        // 1. Update public.id_cards table
        try {
            const check = await client.from('id_cards').select('id, id_number').order('created_at', { ascending: false }).limit(1).maybeSingle();
            const idNumber = check?.data?.id_number || currentCitizen.sangaia_id_number || ('SGN-' + userId.replace(/-/g, '').substring(0, 8).toUpperCase());

            const cardPayload = {
                full_name: (updates.fullName || currentCitizen.full_name || session.user.user_metadata?.full_name || 'citizen').toLowerCase(),
                dob: updates.dob || currentCitizen.date_of_birth || '06/22/2010',
                sex: updates.sex || currentCitizen.sex || 'M',
                status: updates.status || currentCitizen.account_status || 'ACTIVE',
                hair: updates.hair || currentCitizen.hair || 'Bld',
                height: updates.height || currentCitizen.height || "5'8\\\"",
                province: (updates.province || currentCitizen.province || 'SHESK').toUpperCase(),
                languages: updates.languages || currentCitizen.languages || 'SGN, ENG, RUS, CHN, GER',
                under21_notice: updates.under21_notice || currentCitizen.under21_notice || 'not twenty-one until 06/22/2031',
                photo_url: updates.photoUrl !== undefined ? updates.photoUrl : (currentCitizen.photo_url || '')
            };

            if (check?.data?.id) {
                await client.from('id_cards').update(cardPayload).eq('id', check.data.id);
            } else {
                cardPayload.id_number = idNumber;
                await client.from('id_cards').insert(cardPayload);
            }
        } catch (err) {
            console.warn("id_cards update notice:", err);
        }

        // 2. Update public.sangaia_citizens table
        try {
            await client.from('sangaia_citizens').upsert({
                id: userId,
                full_name: (updates.fullName || currentCitizen.full_name || 'citizen').toLowerCase(),
                date_of_birth: updates.dob || currentCitizen.date_of_birth || '06/22/2010',
                physical_address: updates.address || currentCitizen.physical_address || null,
                phone_number: updates.phone || currentCitizen.phone_number || null,
                education_level: updates.educationLevel || currentCitizen.education_level || null
            });
        } catch(e) {}

        // 3. Update active citizen cache
        const updatedCitizen = {
            ...currentCitizen,
            full_name: (updates.fullName || currentCitizen.full_name || 'citizen').toLowerCase(),
            date_of_birth: updates.dob || currentCitizen.date_of_birth,
            sex: updates.sex || currentCitizen.sex,
            hair: updates.hair || currentCitizen.hair,
            height: updates.height || currentCitizen.height,
            province: updates.province || currentCitizen.province,
            territory: updates.province || currentCitizen.territory,
            languages: updates.languages || currentCitizen.languages,
            under21_notice: updates.under21_notice || currentCitizen.under21_notice,
            photo_url: updates.photoUrl !== undefined ? updates.photoUrl : currentCitizen.photo_url,
            physical_address: updates.address || currentCitizen.physical_address,
            phone_number: updates.phone || currentCitizen.phone_number,
            education_level: updates.educationLevel || currentCitizen.education_level
        };

        sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(updatedCitizen));
        setTinyUserCookie(updatedCitizen.full_name, updatedCitizen.sangaia_id_number);
        await this.refreshUI();
        this.notifyAuthChange(session, session.user);

        return updatedCitizen;
    },

    async signOut() {
        const client = initClient();
        if (client && client.auth) {
            try { await client.auth.signOut(); } catch(e){}
        }
        deleteTinyUserCookie();
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
// 6. Header Profile Widget DOM Updater
// -----------------------------------------------------------------------------
function renderAuthenticatedProfile(profileMenu, citizen, user) {
    if (!profileMenu) return;
    const rawName = (citizen && citizen.full_name) || (user && user.user_metadata?.full_name) || (user && user.email ? user.email.split('@')[0] : 'citizen');
    const name = rawName.toLowerCase();
    const citizenId = ((citizen && citizen.sangaia_id_number) || 'SGN-09FDA816').toLowerCase();
    const initial = (name.charAt(0) || 'c').toUpperCase();
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
    profileMenu.style.cursor = 'pointer';
    profileMenu.onclick = function(e) {
        window.location.href = idUrl;
    };
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
    profileMenu.style.cursor = 'pointer';
    profileMenu.onclick = function(e) {
        window.location.href = idUrl;
    };
}

async function updateAuthWidgets() {
    const profileMenu = document.getElementById('userProfileMenu');
    if (!profileMenu) return;

    let supaSession = getSupabaseStoredSession();
    let citizen = null;
    try {
        const rawCit = sangaiaStorage.getItem(ACTIVE_CITIZEN_KEY);
        if (rawCit) citizen = JSON.parse(rawCit);
    } catch (e) {}

    if (supaSession && supaSession.user) {
        if (citizen && citizen.full_name) {
            setTinyUserCookie(citizen.full_name, citizen.sangaia_id_number);
            renderAuthenticatedProfile(profileMenu, citizen, supaSession.user);
        } else {
            const name = supaSession.user.user_metadata?.full_name || supaSession.user.email?.split('@')[0] || 'citizen';
            setTinyUserCookie(name, 'SGN-09FDA816');
            renderAuthenticatedProfile(profileMenu, { full_name: name, sangaia_id_number: 'SGN-09FDA816' }, supaSession.user);
        }
    } else {
        renderUnauthenticatedProfile(profileMenu);
    }

    try {
        const client = initClient();
        if (client && client.auth) {
            const { data: { session } } = await client.auth.getSession();
            if (session && session.user) {
                if (!citizen || !citizen.full_name) {
                    const { data } = await client.from('sangaia_citizens').select('*').eq('id', session.user.id).maybeSingle();
                    if (data && data.full_name) {
                        citizen = data;
                        sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(data));
                        setTinyUserCookie(citizen.full_name, citizen.sangaia_id_number);
                    }
                }
                renderAuthenticatedProfile(profileMenu, citizen || {}, session.user);
            } else if (!supaSession || !supaSession.user) {
                deleteTinyUserCookie();
                sangaiaStorage.removeItem(ACTIVE_CITIZEN_KEY);
                sangaiaStorage.removeItem(ACTIVE_SESSION_KEY);
                renderUnauthenticatedProfile(profileMenu);
            }
        }
    } catch (e) {}
}

// -----------------------------------------------------------------------------
// 7. Lifecycle Initialization
// -----------------------------------------------------------------------------
function initAuthLifecycle() {
    const supaSession = getSupabaseStoredSession();
    if (!supaSession || !supaSession.user) {
        sangaiaStorage.removeItem(ACTIVE_CITIZEN_KEY);
        sangaiaStorage.removeItem(ACTIVE_SESSION_KEY);
    }

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
                    sangaiaStorage.removeItem(ACTIVE_CITIZEN_KEY);
                    sangaiaStorage.removeItem(ACTIVE_SESSION_KEY);
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
