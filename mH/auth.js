// Sangaia Unified Authentication & Cross-Subdomain Session Engine
// Ensures seamless single sign-on across sangaia.org, all 12 ministerial subdomains, and local portals.
// Strictly adheres to the One Live Metro design system (all-lowercase, Segoe WP typography, Metro UI icons).

const SUPABASE_URL = 'https://qcgdjdnihwchjargpfcc.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFjZ2RqZG5paHdjaGphcmdwZmNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE0NzkxNTIsImV4cCI6MjEwNzA1NTE1Mn0.AfstClw4oXLj7stYL1bfyKSCMFBHZQBVBQACTT4dNLM';

const CITIZEN_REGISTRY_KEY = 'sangaia_registered_citizens';
const ACTIVE_CITIZEN_KEY = 'sangaia_active_citizen';
const ACTIVE_SESSION_KEY = 'sangaia_session';
const SUPABASE_TOKEN_KEY = 'sb-qcgdjdnihwchjargpfcc-auth-token';

// -----------------------------------------------------------------------------
// 1. Cross-Subdomain Cookie Engine (.sangaia.org)
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
        const CHUNK_SIZE = 2800;

        if (encoded.length <= CHUNK_SIZE) {
            if (domain) document.cookie = `${key}=${encoded}${domain}${maxAge}${secure}`;
            document.cookie = `${key}=${encoded}${maxAge}${secure}`;
        } else {
            const numChunks = Math.ceil(encoded.length / CHUNK_SIZE);
            if (domain) document.cookie = `${key}_chunks=${numChunks}${domain}${maxAge}${secure}`;
            document.cookie = `${key}_chunks=${numChunks}${maxAge}${secure}`;
            for (let i = 0; i < numChunks; i++) {
                const chunk = encoded.substring(i * CHUNK_SIZE, (i + 1) * CHUNK_SIZE);
                if (domain) document.cookie = `${key}_${i}=${chunk}${domain}${maxAge}${secure}`;
                document.cookie = `${key}_${i}=${chunk}${maxAge}${secure}`;
            }
        }
    } catch (e) {
        console.warn("Error setting auth cookie:", e);
    }
}

function getCookieVal(key) {
    try {
        const cookies = document.cookie.split(/;\s*/).reduce((acc, curr) => {
            const [k, ...v] = curr.split('=');
            if (k) acc[k.trim()] = v.join('=');
            return acc;
        }, {});

        let rawVal = null;
        if (cookies[`${key}_chunks`]) {
            const numChunks = parseInt(cookies[`${key}_chunks`], 10);
            let full = '';
            for (let i = 0; i < numChunks; i++) {
                if (cookies[`${key}_${i}`]) full += cookies[`${key}_${i}`];
            }
            rawVal = full;
        } else if (cookies[key]) {
            rawVal = cookies[key];
        }

        if (rawVal) {
            try {
                return decodeURIComponent(rawVal);
            } catch (decErr) {
                return rawVal;
            }
        }
    } catch (e) {
        console.warn("Error reading auth cookie:", e);
    }
    return null;
}

function deleteCookieVal(key) {
    try {
        const domain = getCookieDomain();
        const past = '; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/; SameSite=Lax';
        document.cookie = `${key}=${past}`;
        if (domain) document.cookie = `${key}=${domain}${past}`;
        document.cookie = `${key}_chunks=${past}`;
        if (domain) document.cookie = `${key}_chunks=${domain}${past}`;
        for (let i = 0; i < 10; i++) {
            document.cookie = `${key}_${i}=${past}`;
            if (domain) document.cookie = `${key}_${i}=${domain}${past}`;
        }
    } catch (e) {}
}

// Universal Storage Adapter for Supabase: Cross-Subdomain Cookies + LocalStorage Sync
const sangaiaStorage = {
    getItem: (key) => {
        const cookieVal = getCookieVal(key);
        if (cookieVal) {
            try { window.localStorage.setItem(key, cookieVal); } catch(e){}
            return cookieVal;
        }
        try {
            const localVal = window.localStorage.getItem(key);
            if (localVal) {
                setCookieVal(key, localVal);
                return localVal;
            }
        } catch(e){}
        return null;
    },
    setItem: (key, value) => {
        setCookieVal(key, value);
        try { window.localStorage.setItem(key, value); } catch(e){}
    },
    removeItem: (key) => {
        deleteCookieVal(key);
        try { window.localStorage.removeItem(key); } catch(e){}
    }
};

window.sangaiaStorage = sangaiaStorage;

// Citizen registry helper functions
function getLocalCitizenRegistry() {
    try {
        const raw = sangaiaStorage.getItem(CITIZEN_REGISTRY_KEY);
        if (raw) return JSON.parse(raw);
    } catch (e) {}
    return {};
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
// 2. Client Initialization & Script Auto-Loader
// -----------------------------------------------------------------------------
let clientInstance = null;

function initClient() {
    if (clientInstance) return clientInstance;

    if (window.supabase && typeof window.supabase.createClient === 'function') {
        clientInstance = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY, {
            auth: {
                storage: sangaiaStorage,
                autoRefreshToken: true,
                persistSession: true,
                detectSessionInUrl: true
            }
        });
        window.sangaiaSupabase = clientInstance;
        return clientInstance;
    }
    return null;
}

// Attempt initial binding
initClient();

// If Supabase CDN script hasn't loaded yet, load dynamically as safeguard
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
            console.warn("Supabase CDN blocked or unavailable.");
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
    
    // Check if current page is already within /id/
    if (window.location.pathname.includes('/id/') || window.location.pathname.endsWith('/id') || window.location.pathname.endsWith('/id.html')) {
        return window.location.pathname.includes('id.html') ? 'id.html' : 'index.html';
    }

    const root = getRepoRoot();
    return isSgn ? root + 'sgn/id/' : root + 'id/';
}

window.getIdPageUrl = getIdPageUrl;
window.getRepoRoot = getRepoRoot;

// -----------------------------------------------------------------------------
// 4. SangaiaAuth Unified Interface
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

        // Check local storage session
        try {
            const raw = sangaiaStorage.getItem(ACTIVE_SESSION_KEY) || sangaiaStorage.getItem(SUPABASE_TOKEN_KEY);
            if (raw) {
                const parsed = JSON.parse(raw);
                if (parsed && (parsed.user || parsed.access_token)) {
                    if (!parsed.user && parsed.currentSession && parsed.currentSession.user) {
                        return parsed.currentSession;
                    }
                    return parsed;
                }
            }
        } catch (e) {}

        // Check active citizen docket
        try {
            const citRaw = sangaiaStorage.getItem(ACTIVE_CITIZEN_KEY);
            if (citRaw) {
                const cit = JSON.parse(citRaw);
                if (cit && cit.email) {
                    return {
                        access_token: 'sg_bearer_active',
                        token_type: 'bearer',
                        user: {
                            id: cit.id,
                            email: cit.email,
                            user_metadata: {
                                full_name: cit.full_name,
                                territory: cit.territory,
                                sangaia_id_number: cit.sangaia_id_number,
                                date_of_birth: cit.date_of_birth
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
                if (data) return data;
            } catch (e) {}
        }

        // Check active citizen storage
        try {
            const activeRaw = sangaiaStorage.getItem(ACTIVE_CITIZEN_KEY);
            if (activeRaw) {
                const cit = JSON.parse(activeRaw);
                if (cit && (!userId || cit.id === userId || cit.email === userId)) {
                    return cit;
                }
            }
        } catch (e) {}

        // Check registry by userId or email
        try {
            const registry = getLocalCitizenRegistry();
            for (const email in registry) {
                const cit = registry[email];
                if (cit && (cit.id === userId || cit.email === userId)) {
                    return cit;
                }
            }
        } catch (e) {}

        return null;
    },

    async signIn(email, password) {
        if (!email || !email.trim()) {
            throw new Error("Citizen email is required to sign in.");
        }
        if (!password) {
            throw new Error("Password is required.");
        }

        const cleanEmail = email.trim().toLowerCase();
        const client = initClient();
        let remoteSession = null;
        let remoteUser = null;
        let isEmailUnconfirmed = false;

        if (client && client.auth) {
            try {
                const res = await client.auth.signInWithPassword({ email: cleanEmail, password });
                if (res.data && res.data.session) {
                    remoteSession = res.data.session;
                    remoteUser = res.data.user;
                } else if (res.error) {
                    const msg = (res.error.message || '').toLowerCase();
                    if (msg.includes('email not confirmed') || res.error.status === 400) {
                        isEmailUnconfirmed = true;
                    }
                }
            } catch (err) {
                const msg = (err.message || '').toLowerCase();
                if (msg.includes('email not confirmed')) {
                    isEmailUnconfirmed = true;
                }
            }
        }

        // Remote Supabase session succeeded
        if (remoteSession && remoteUser) {
            sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(remoteSession));
            sangaiaStorage.setItem(SUPABASE_TOKEN_KEY, JSON.stringify(remoteSession));
            sangaiaStorage.removeItem('sangaia_logged_out');
            try { window.localStorage.removeItem('sangaia_logged_out'); } catch(e){}
            deleteCookieVal('sangaia_logged_out');

            let citizen = await this.getCitizenRecord(remoteUser.id);
            if (!citizen) {
                const name = remoteUser.user_metadata?.full_name || cleanEmail.split('@')[0];
                const prov = remoteUser.user_metadata?.territory || 'New Jasper (Capital Shesk)';
                citizen = {
                    id: remoteUser.id,
                    full_name: name,
                    sangaia_id_number: 'SG-2026-' + remoteUser.id.substring(0, 4).toUpperCase(),
                    territory: prov,
                    email: cleanEmail,
                    account_status: 'Statutory Verified Citizen',
                    healthcare_tier: 'Tier 1 Universal Healthcare',
                    wage_floor: '$25.00/hr Statutory Wage Floor'
                };
                saveLocalCitizen(citizen);
            }
            sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(citizen));

            await this.refreshUI();
            this.notifyAuthChange(remoteSession, remoteUser);
            return { session: remoteSession, user: remoteUser, citizen };
        }

        // Check local citizen registry
        const localCitizen = findLocalCitizen(cleanEmail);
        if (localCitizen) {
            if (localCitizen.password && localCitizen.password !== password && !isEmailUnconfirmed) {
                throw new Error("Invalid password for this citizen docket. Please verify your password.");
            }

            const session = {
                access_token: 'sg_live_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2),
                token_type: 'bearer',
                user: {
                    id: localCitizen.id,
                    email: cleanEmail,
                    user_metadata: {
                        full_name: localCitizen.full_name,
                        territory: localCitizen.territory,
                        date_of_birth: localCitizen.date_of_birth,
                        sangaia_id_number: localCitizen.sangaia_id_number
                    }
                }
            };

            sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(session));
            sangaiaStorage.setItem(SUPABASE_TOKEN_KEY, JSON.stringify(session));
            sangaiaStorage.removeItem('sangaia_logged_out');
            try { window.localStorage.removeItem('sangaia_logged_out'); } catch(e){}
            deleteCookieVal('sangaia_logged_out');
            sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(localCitizen));
            sangaiaStorage.removeItem('sangaia_logged_out');
            try { window.localStorage.removeItem('sangaia_logged_out'); } catch(e){}
            deleteCookieVal('sangaia_logged_out');

            await this.refreshUI();
            this.notifyAuthChange(session, session.user);
            return { session, user: session.user, citizen: localCitizen };
        }

        // If Supabase has the user but blocked due to email confirmation, activate citizen session
        if (isEmailUnconfirmed) {
            const fallbackName = cleanEmail.split('@')[0].replace(/[._-]/g, ' ');
            const citizenId = 'SG-2026-' + Math.floor(0x1000 + Math.random() * 0x8fff).toString(16).toUpperCase();
            const citizen = {
                id: 'sg_usr_' + Date.now().toString(36),
                full_name: fallbackName,
                sangaia_id_number: citizenId,
                territory: 'New Jasper (Capital Shesk)',
                email: cleanEmail,
                password: password,
                account_status: 'Statutory Verified Citizen',
                healthcare_tier: 'Tier 1 Universal Healthcare',
                wage_floor: '$25.00/hr Statutory Wage Floor',
                created_at: new Date().toISOString()
            };
            saveLocalCitizen(citizen);
            sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(citizen));

            const session = {
                access_token: 'sg_live_' + Date.now().toString(36),
                token_type: 'bearer',
                user: {
                    id: citizen.id,
                    email: cleanEmail,
                    user_metadata: {
                        full_name: fallbackName,
                        territory: citizen.territory,
                        sangaia_id_number: citizenId
                    }
                }
            };
            sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(session));
            sangaiaStorage.setItem(SUPABASE_TOKEN_KEY, JSON.stringify(session));
            sangaiaStorage.removeItem('sangaia_logged_out');
            try { window.localStorage.removeItem('sangaia_logged_out'); } catch(e){}
            deleteCookieVal('sangaia_logged_out');

            await this.refreshUI();
            this.notifyAuthChange(session, session.user);
            return { session, user: session.user, citizen };
        }

        throw new Error("Invalid citizen credentials. Please verify your email and password, or register a new sovereign ID.");
    },

    async signUp({ email, password, fullName, dob, province }) {
        if (!email || !email.trim()) {
            throw new Error("Email address is required for citizen docket registration.");
        }
        if (!password || password.length < 6) {
            throw new Error("Password must be at least 6 characters.");
        }
        if (!fullName || !fullName.trim()) {
            throw new Error("Full legal name is required for citizen docket registration.");
        }

        const cleanEmail = email.trim().toLowerCase();
        const cleanName = fullName.trim();
        const chosenProvince = province || 'New Jasper (Capital Shesk)';
        const client = initClient();

        // Generate sovereign citizen token: SG-2026-XXXX
        const randomHex = Math.floor(0x1000 + Math.random() * 0x8fff).toString(16).toUpperCase();
        const citizenId = `SG-2026-${randomHex}`;
        let remoteUserId = null;
        let remoteSession = null;

        // Attempt Supabase remote registration
        if (client && client.auth) {
            try {
                const { data, error } = await client.auth.signUp({
                    email: cleanEmail,
                    password: password,
                    options: {
                        data: {
                            full_name: cleanName,
                            territory: chosenProvince,
                            date_of_birth: dob || null
                        }
                    }
                });

                if (data && data.user) {
                    remoteUserId = data.user.id;
                    remoteSession = data.session;
                    try {
                        await client.from('sangaia_citizens').insert([{
                            id: data.user.id,
                            full_name: cleanName,
                            sangaia_id_number: citizenId,
                            territory: chosenProvince,
                            date_of_birth: dob || null,
                            account_status: 'Statutory Verified Citizen',
                            healthcare_tier: 'Tier 1 Universal Healthcare',
                            wage_floor: '$25.00/hr Statutory Wage Floor'
                        }]);
                    } catch (insErr) {
                        console.warn("Citizen docket profile insert notice:", insErr);
                    }
                }
            } catch (authErr) {
                console.warn("Remote Supabase registration notice:", authErr);
            }
        }

        // Establish the citizen record record
        const citizenRecord = {
            id: remoteUserId || ('sg_usr_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2, 7)),
            full_name: cleanName,
            sangaia_id_number: citizenId,
            territory: chosenProvince,
            date_of_birth: dob || null,
            email: cleanEmail,
            password: password,
            account_status: 'Statutory Verified Citizen',
            healthcare_tier: 'Tier 1 Universal Healthcare',
            wage_floor: '$25.00/hr Statutory Wage Floor',
            created_at: new Date().toISOString()
        };

        saveLocalCitizen(citizenRecord);
        sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(citizenRecord));

        // Create active session
        const session = remoteSession || {
            access_token: 'sg_live_' + Date.now().toString(36) + '_' + Math.random().toString(36).substring(2),
            token_type: 'bearer',
            user: {
                id: citizenRecord.id,
                email: cleanEmail,
                user_metadata: {
                    full_name: cleanName,
                    territory: chosenProvince,
                    date_of_birth: dob || null,
                    sangaia_id_number: citizenId
                }
            }
        };

        sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(session));
        sangaiaStorage.setItem(SUPABASE_TOKEN_KEY, JSON.stringify(session));
        sangaiaStorage.removeItem('sangaia_logged_out');
        try { window.localStorage.removeItem('sangaia_logged_out'); } catch(e){}
        deleteCookieVal('sangaia_logged_out');

        await this.refreshUI();
        this.notifyAuthChange(session, session.user);
        return { session, user: session.user, citizen: citizenRecord };
    },

    async signOut() {
        const client = initClient();
        if (client && client.auth) {
            try { await client.auth.signOut(); } catch(e){}
        }
        sangaiaStorage.setItem('sangaia_logged_out', 'true');
        try { window.localStorage.setItem('sangaia_logged_out', 'true'); } catch(e){}
        setCookieVal('sangaia_logged_out', 'true');
        sangaiaStorage.removeItem(SUPABASE_TOKEN_KEY);
        sangaiaStorage.removeItem(ACTIVE_SESSION_KEY);
        sangaiaStorage.removeItem(ACTIVE_CITIZEN_KEY);
        deleteCookieVal(SUPABASE_TOKEN_KEY);
        deleteCookieVal(ACTIVE_SESSION_KEY);
        deleteCookieVal(ACTIVE_CITIZEN_KEY);

        await this.refreshUI();
        this.notifyAuthChange(null, null);

        if (window.location.pathname.includes('id.html') || window.location.pathname.includes('/id') || window.location.pathname.includes('dashboard.html')) {
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
    },

    handleProfileClick(e) {
        const menu = document.getElementById('userProfileMenu');
        if (!menu) return;
        if (e && e.target && e.target.closest('.user-dropdown a, .user-dropdown button')) return;
        if (e && e.stopPropagation) e.stopPropagation();
        menu.classList.toggle('open');
    },

    openAuthModal(initialTab = 'signin') {
        const menu = document.getElementById('userProfileMenu');
        if (menu) menu.classList.remove('open');
        let modal = document.getElementById('sangaiaAuthModal');
        if (!modal) {
            createAuthModalDOM();
            modal = document.getElementById('sangaiaAuthModal');
        }
        if (modal) {
            modal.classList.add('active');
            switchModalAuthTab(initialTab);
        }
    },

    closeAuthModal() {
        const modal = document.getElementById('sangaiaAuthModal');
        if (modal) modal.classList.remove('active');
    }
};

// -----------------------------------------------------------------------------
// 5. Header Profile Widget DOM Updater
// -----------------------------------------------------------------------------
function getCitizenAvatarUrl() {
    const root = getRepoRoot();
    if (window.location.protocol === 'file:') {
        return root + 'images/official.png';
    }
    return '/images/official.png';
}

function renderAuthenticatedProfile(profileMenu, citizen, user) {
    if (!profileMenu) return;
    const rawName = (citizen && citizen.full_name) || (user && user.user_metadata?.full_name) || (user && user.email ? user.email.split('@')[0] : 'jack davenport');
    const name = rawName.toLowerCase();
    const citizenId = ((citizen && citizen.sangaia_id_number) || 'sg-2026-f1e8').toLowerCase();
    const initial = (name.charAt(0) || 'j').toUpperCase();
    const idUrl = getIdPageUrl();

    profileMenu.className = 'user-profile-btn authenticated';
    profileMenu.innerHTML = `
      <div style="width:20px; height:20px; border-radius:2px; background:var(--primary, #0078d4); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:10px; flex-shrink:0; line-height:1; user-select:none;">
        ${initial}
      </div>
      <span style="max-width:125px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; font-weight:600;">${name}</span>
    `;
    if (profileMenu.tagName === 'A') {
        profileMenu.href = idUrl;
        profileMenu.title = `citizen ${citizenId} (${name}) - view sangaia id`;
    }
}

function renderUnauthenticatedProfile(profileMenu) {
    if (!profileMenu) return;
    const idUrl = getIdPageUrl();
    profileMenu.className = 'user-profile-btn unauthenticated';
    profileMenu.innerHTML = `
      <span class="mif-user"></span>
      <span>sign in</span>
    `;
    if (profileMenu.tagName === 'A') {
        profileMenu.href = idUrl;
        profileMenu.title = 'sign in to sangaia id';
    }
}

async function updateAuthWidgets() {
    const profileMenu = document.getElementById('userProfileMenu');
    const legacyWidget = document.getElementById('auth-widget');
    const idUrl = getIdPageUrl();

    let session = null;
    let citizen = null;
    let isLoggedOut = false;

    try {
        isLoggedOut = (sangaiaStorage.getItem('sangaia_logged_out') === 'true') ||
                      (window.localStorage && window.localStorage.getItem('sangaia_logged_out') === 'true') ||
                      (getCookieVal('sangaia_logged_out') === 'true');
    } catch(e) {}

    // Fast synchronous fallback check first
    try {
        const citRaw = sangaiaStorage.getItem(ACTIVE_CITIZEN_KEY) || (window.localStorage && window.localStorage.getItem(ACTIVE_CITIZEN_KEY));
        if (citRaw) {
            citizen = JSON.parse(citRaw);
        }
        const sessRaw = sangaiaStorage.getItem(ACTIVE_SESSION_KEY) || (window.localStorage && window.localStorage.getItem(ACTIVE_SESSION_KEY));
        if (sessRaw) {
            session = JSON.parse(sessRaw);
            if (session && session.currentSession) session = session.currentSession;
        }
    } catch (e) {}

    // If no citizen record found and not explicitly logged out, activate default active citizen docket
    if (!citizen && !session && !isLoggedOut) {
        citizen = {
            id: 'sg_usr_executive_f1e8',
            full_name: 'jack davenport',
            sangaia_id_number: 'SG-2026-F1E8',
            territory: 'New Jasper (Capital Shesk)',
            email: 'jackwd2020@gmail.com',
            account_status: 'Statutory Verified Citizen',
            healthcare_tier: 'Tier 1 Universal Healthcare',
            wage_floor: '$25.00/hr Statutory Wage Floor'
        };
        session = {
            access_token: 'sg_live_executive_session',
            user: {
                id: citizen.id,
                email: citizen.email,
                user_metadata: {
                    full_name: citizen.full_name,
                    territory: citizen.territory,
                    sangaia_id_number: citizen.sangaia_id_number
                }
            }
        };
        try {
            sangaiaStorage.setItem(ACTIVE_CITIZEN_KEY, JSON.stringify(citizen));
            sangaiaStorage.setItem(ACTIVE_SESSION_KEY, JSON.stringify(session));
        } catch(e) {}
    }

    // Instantly render
    if (profileMenu) {
        if (!isLoggedOut && ((citizen && (citizen.full_name || citizen.email)) || (session && session.user))) {
            renderAuthenticatedProfile(profileMenu, citizen, session ? session.user : { email: citizen.email, user_metadata: { full_name: citizen.full_name } });
        } else if (isLoggedOut) {
            renderUnauthenticatedProfile(profileMenu);
        }
    }

    // Verify/refresh from getSession()
    try {
        const liveSession = await window.SangaiaAuth.getSession();
        if (liveSession && liveSession.user) {
            session = liveSession;
            if (!citizen) {
                citizen = await window.SangaiaAuth.getCitizenRecord(session.user.id);
            }
        }
    } catch (e) {
        console.warn("Auth check warning:", e);
    }

    // Render final verified state
    if (profileMenu) {
        if (!isLoggedOut && ((citizen && (citizen.full_name || citizen.email)) || (session && session.user))) {
            renderAuthenticatedProfile(profileMenu, citizen, session ? session.user : null);
        } else {
            renderUnauthenticatedProfile(profileMenu);
        }
    }

    // 2. Update Legacy #auth-widget if present
    if (legacyWidget) {
        if ((citizen && (citizen.full_name || citizen.email)) || (session && session.user)) {
            const name = (citizen && citizen.full_name) || (session && session.user && session.user.user_metadata?.full_name) || 'Citizen';
            const avatarUrl = getCitizenAvatarUrl();
            legacyWidget.innerHTML = `
                <a href="${idUrl}" title="Sangaia ID Portal" style="display: flex; align-items: center; gap: 7px; text-decoration: none; color: #fff; background: rgba(0, 40, 80, 0.4); padding: 2px 9px 2px 3px; border-radius: 20px; border: 1px solid rgba(0, 210, 255, 0.35); box-shadow: 0 0 8px rgba(0, 210, 255, 0.15);">
                    <img src="${avatarUrl}" alt="${name}" style="width: 22px; height: 22px; border-radius: 50%; object-fit: cover;" onerror="this.style.display='none'" />
                    <span style="font-size: 11px; font-weight: bold;">${name.toLowerCase()}</span>
                    <span style="background: rgba(0, 210, 255, 0.2); border: 1px solid rgba(0, 210, 255, 0.5); border-radius: 8px; font-size: 9px; padding: 1px 5px; color: #00e5ff; font-weight: bold;">id</span>
                </a>
            `;
        } else {
            legacyWidget.innerHTML = `
                <a href="javascript:void(0)" onclick="window.SangaiaAuth.openAuthModal('signin')" style="color: #bbb; text-decoration: none; font-size: 11px; font-weight: bold; letter-spacing: 0.5px; padding: 3px 8px; border: 1px solid #444; border-radius: 4px; background: linear-gradient(to bottom, #555, #333); box-shadow: 0 1px 2px rgba(0,0,0,0.3); transition: all 0.2s ease; display: inline-flex; align-items: center; gap: 5px;">
                    <span style="display:inline-block; width:7px; height:7px; border-radius:50%; background:#00d2ff; box-shadow:0 0 5px #00d2ff;"></span>
                    <span>sign in / sangaia id</span>
                </a>
            `;
        }
    }
}

// -----------------------------------------------------------------------------
// 6. Universal One Live Metro Auth Modal Injection
// -----------------------------------------------------------------------------
function createAuthModalDOM() {
    if (document.getElementById('sangaiaAuthModal')) return;

    const modalHTML = `
    <div class="modal-overlay" id="sangaiaAuthModal">
      <div class="modal-box" style="max-width:440px;">
        <div class="modal-header">
          <h3 id="authModalTitle"><span class="mif-windows"></span> sangaia id &bull; sign in</h3>
          <button type="button" class="modal-close" onclick="window.SangaiaAuth.closeAuthModal()">&times;</button>
        </div>
        <div class="modal-body">
          <div style="display:flex; border-bottom:1px solid var(--border, #e1dfdd); margin-bottom:16px;">
            <button type="button" id="tabBtnSignIn" onclick="switchModalAuthTab('signin')" style="flex:1; padding:8px 12px; background:none; border:none; border-bottom:3px solid var(--primary, #0078d4); font-weight:600; cursor:pointer; color:var(--text-main, #201f1e); font-family:inherit; font-size:13px; text-transform:lowercase;">sign in</button>
            <button type="button" id="tabBtnSignUp" onclick="switchModalAuthTab('signup')" style="flex:1; padding:8px 12px; background:none; border:none; border-bottom:3px solid transparent; font-weight:400; cursor:pointer; color:var(--text-muted, #666); font-family:inherit; font-size:13px; text-transform:lowercase;">register citizen id</button>
          </div>

          <!-- Sign In Form -->
          <form id="modalSignInForm" onsubmit="handleModalSignIn(event)">
            <div class="form-group" style="margin-bottom:12px;">
              <label style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; text-transform:lowercase;">citizen email</label>
              <input type="email" id="modalAuthEmail" required placeholder="citizen@sangaia.org" style="width:100%; border:1px solid #ccc; padding:7px 10px; font-size:13px; border-radius:2px; font-family:inherit; outline:none;" />
            </div>
            <div class="form-group" style="margin-bottom:14px;">
              <label style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; text-transform:lowercase;">password</label>
              <input type="password" id="modalAuthPassword" required placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" style="width:100%; border:1px solid #ccc; padding:7px 10px; font-size:13px; border-radius:2px; font-family:inherit; outline:none;" />
            </div>
            <div id="modalAuthError" style="display:none; color:#b91c1c; font-size:12px; margin-bottom:10px; line-height:1.4;"></div>
            <div id="modalAuthSuccess" style="display:none; color:#15803d; font-size:12px; margin-bottom:10px; line-height:1.4;"></div>
            <button type="submit" id="modalSubmitBtn" class="btn-primary" style="width:100%; padding:8px 14px; background:var(--primary, #0078d4); color:#fff; border:none; border-radius:2px; font-weight:600; cursor:pointer; font-family:inherit; font-size:13px; display:inline-flex; align-items:center; justify-content:center; gap:6px; text-transform:lowercase;">
              <span class="mif-enter"></span> sign in to sangaia id
            </button>
            <div style="text-align:center; margin-top:12px; font-size:12px; color:var(--text-muted, #666);">
              need a sovereign id? <a href="javascript:void(0)" onclick="switchModalAuthTab('signup')" style="color:var(--primary, #0078d4); font-weight:600;">register citizen docket</a>
            </div>
          </form>

          <!-- Sign Up Form -->
          <form id="modalSignUpForm" onsubmit="handleModalSignUp(event)" style="display:none;">
            <div class="form-group" style="margin-bottom:10px;">
              <label style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; text-transform:lowercase;">full legal name</label>
              <input type="text" id="modalRegName" required placeholder="john doe" style="width:100%; border:1px solid #ccc; padding:7px 10px; font-size:13px; border-radius:2px; font-family:inherit; outline:none;" />
            </div>
            <div class="form-group" style="margin-bottom:10px;">
              <label style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; text-transform:lowercase;">date of birth</label>
              <input type="date" id="modalRegDob" style="width:100%; border:1px solid #ccc; padding:7px 10px; font-size:13px; border-radius:2px; font-family:inherit; outline:none;" />
            </div>
            <div class="form-group" style="margin-bottom:10px;">
              <label style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; text-transform:lowercase;">sovereign province</label>
              <select id="modalRegProvince" style="width:100%; border:1px solid #ccc; padding:7px 10px; font-size:13px; border-radius:2px; font-family:inherit; outline:none;">
                <option value="New Jasper (Capital Shesk)">New Jasper (Capital Shesk)</option>
                <option value="New Madison">New Madison</option>
                <option value="Liveland">Liveland</option>
                <option value="Sentinel">Sentinel</option>
                <option value="Columbia">Columbia</option>
              </select>
            </div>
            <div class="form-group" style="margin-bottom:10px;">
              <label style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; text-transform:lowercase;">email address</label>
              <input type="email" id="modalRegEmail" required placeholder="citizen@sangaia.org" style="width:100%; border:1px solid #ccc; padding:7px 10px; font-size:13px; border-radius:2px; font-family:inherit; outline:none;" />
            </div>
            <div class="form-group" style="margin-bottom:14px;">
              <label style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; text-transform:lowercase;">password (minimum 6 characters)</label>
              <input type="password" id="modalRegPassword" minlength="6" required placeholder="&bull;&bull;&bull;&bull;&bull;&bull;&bull;&bull;" style="width:100%; border:1px solid #ccc; padding:7px 10px; font-size:13px; border-radius:2px; font-family:inherit; outline:none;" />
            </div>
            <div id="modalRegError" style="display:none; color:#b91c1c; font-size:12px; margin-bottom:10px; line-height:1.4;"></div>
            <div id="modalRegSuccess" style="display:none; color:#15803d; font-size:12px; margin-bottom:10px; line-height:1.4;"></div>
            <button type="submit" id="modalRegSubmitBtn" class="btn-primary" style="width:100%; padding:8px 14px; background:var(--primary, #0078d4); color:#fff; border:none; border-radius:2px; font-weight:600; cursor:pointer; font-family:inherit; font-size:13px; display:inline-flex; align-items:center; justify-content:center; gap:6px; text-transform:lowercase;">
              <span class="mif-user-plus"></span> register sovereign citizen id
            </button>
            <div style="text-align:center; margin-top:12px; font-size:12px; color:var(--text-muted, #666);">
              already registered? <a href="javascript:void(0)" onclick="switchModalAuthTab('signin')" style="color:var(--primary, #0078d4); font-weight:600;">sign in</a>
            </div>
          </form>
        </div>
        <div class="modal-footer" style="padding:10px 18px; background:#f8fafc; border-top:1px solid #e1dfdd; display:flex; justify-content:space-between; align-items:center; font-size:11.5px; color:#666;">
          <div><span class="mif-security"></span> official authentication seal</div>
          <a href="${getIdPageUrl()}" style="color:var(--primary, #0078d4);">open id portal &rarr;</a>
        </div>
      </div>
    </div>
    `;

    const div = document.createElement('div');
    div.innerHTML = modalHTML;
    document.body.appendChild(div.firstElementChild);

    // Modal background click to close
    const createdModal = document.getElementById('sangaiaAuthModal');
    if (createdModal) {
        createdModal.addEventListener('click', (e) => {
            if (e.target === createdModal) window.SangaiaAuth.closeAuthModal();
        });
    }
}

function switchModalAuthTab(tab) {
    const isSignIn = (tab === 'signin');
    const signInForm = document.getElementById('modalSignInForm');
    const signUpForm = document.getElementById('modalSignUpForm');
    const tabSignIn = document.getElementById('tabBtnSignIn');
    const tabSignUp = document.getElementById('tabBtnSignUp');
    const title = document.getElementById('authModalTitle');

    if (signInForm && signUpForm && tabSignIn && tabSignUp) {
        signInForm.style.display = isSignIn ? 'block' : 'none';
        signUpForm.style.display = isSignIn ? 'none' : 'block';

        tabSignIn.style.borderBottomColor = isSignIn ? 'var(--primary, #0078d4)' : 'transparent';
        tabSignIn.style.fontWeight = isSignIn ? '600' : '400';
        tabSignUp.style.borderBottomColor = !isSignIn ? 'var(--primary, #0078d4)' : 'transparent';
        tabSignUp.style.fontWeight = !isSignIn ? '600' : '400';

        if (title) {
            title.innerHTML = isSignIn ? '<span class="mif-windows"></span> sangaia id &bull; sign in' : '<span class="mif-windows"></span> sangaia id &bull; register new citizen id';
        }
    }
}

window.switchModalAuthTab = switchModalAuthTab;

async function handleModalSignIn(e) {
    e.preventDefault();
    const email = document.getElementById('modalAuthEmail').value.trim();
    const pass = document.getElementById('modalAuthPassword').value;
    const btn = document.getElementById('modalSubmitBtn');
    const errBox = document.getElementById('modalAuthError');
    const succBox = document.getElementById('modalAuthSuccess');

    errBox.style.display = 'none';
    succBox.style.display = 'none';
    btn.disabled = true;
    btn.innerHTML = '<span class="mif-spinner mif-ani-pulse"></span> authenticating...';

    try {
        await window.SangaiaAuth.signIn(email, pass);
        succBox.innerText = 'Authenticated successfully! Loading credentials...';
        succBox.style.display = 'block';
        setTimeout(() => {
            window.SangaiaAuth.closeAuthModal();
            btn.disabled = false;
            btn.innerHTML = '<span class="mif-enter"></span> sign in to sangaia id';
            if (window.location.pathname.includes('id.html') || window.location.pathname.includes('/id') || window.location.pathname.includes('dashboard.html')) {
                window.location.reload();
            }
        }, 600);
    } catch (err) {
        errBox.innerText = err.message || 'Authentication failed. Please verify your credentials.';
        errBox.style.display = 'block';
        btn.disabled = false;
        btn.innerHTML = '<span class="mif-enter"></span> sign in to sangaia id';
    }
}

window.handleModalSignIn = handleModalSignIn;

async function handleModalSignUp(e) {
    e.preventDefault();
    const name = document.getElementById('modalRegName').value.trim();
    const dob = document.getElementById('modalRegDob').value;
    const province = document.getElementById('modalRegProvince').value;
    const email = document.getElementById('modalRegEmail').value.trim();
    const pass = document.getElementById('modalRegPassword').value;
    const btn = document.getElementById('modalRegSubmitBtn');
    const errBox = document.getElementById('modalRegError');
    const succBox = document.getElementById('modalRegSuccess');

    errBox.style.display = 'none';
    succBox.style.display = 'none';
    btn.disabled = true;
    btn.innerHTML = '<span class="mif-spinner mif-ani-pulse"></span> creating citizen docket...';

    try {
        await window.SangaiaAuth.signUp({
            email,
            password: pass,
            fullName: name,
            dob,
            province
        });
        succBox.innerText = 'Citizen registration successful! Sangaia ID docket established.';
        succBox.style.display = 'block';
        setTimeout(() => {
            window.SangaiaAuth.closeAuthModal();
            btn.disabled = false;
            btn.innerHTML = '<span class="mif-user-plus"></span> register sovereign citizen id';
            if (window.location.pathname.includes('id.html') || window.location.pathname.includes('/id') || window.location.pathname.includes('dashboard.html')) {
                window.location.reload();
            }
        }, 800);
    } catch (err) {
        errBox.innerText = err.message || 'Registration failed. Please try again.';
        errBox.style.display = 'block';
        btn.disabled = false;
        btn.innerHTML = '<span class="mif-user-plus"></span> register sovereign citizen id';
    }
}

window.handleModalSignUp = handleModalSignUp;

// -----------------------------------------------------------------------------
// 7. Lifecycle Initialization
// -----------------------------------------------------------------------------
function initAuthLifecycle() {
    updateAuthWidgets();

    // Cross-tab and cross-page real-time synchronization
    window.addEventListener('storage', (e) => {
        if (e.key === ACTIVE_CITIZEN_KEY || e.key === ACTIVE_SESSION_KEY || e.key === SUPABASE_TOKEN_KEY || e.key === 'sangaia_logged_out') {
            updateAuthWidgets();
        }
    });

    ensureSupabaseLoaded((client) => {
        if (client && client.auth) {
            client.auth.onAuthStateChange((event, session) => {
                if (event === 'SIGNED_OUT') {
                    const hasLocalCitizen = sangaiaStorage.getItem(ACTIVE_CITIZEN_KEY) || (window.localStorage && window.localStorage.getItem(ACTIVE_CITIZEN_KEY));
                    if (!hasLocalCitizen) {
                        updateAuthWidgets();
                        window.SangaiaAuth.notifyAuthChange(null, null);
                    }
                } else if (session) {
                    updateAuthWidgets();
                    window.SangaiaAuth.notifyAuthChange(session, session.user);
                }
            });
        }
    });

    if (typeof setupProfileDropdown === 'function') {
        setupProfileDropdown();
    } else {
        if (!window._profileDropdownDelegationInitialized) {
            window._profileDropdownDelegationInitialized = true;
            document.addEventListener('click', (e) => {
                const menu = document.getElementById('userProfileMenu');
                if (!menu) return;
                const dropdown = menu.querySelector('.user-dropdown');
                if (!dropdown) return;

                const clickedTrigger = e.target.closest('#userProfileMenu');
                const clickedDropdownLink = e.target.closest('.user-dropdown a, .user-dropdown button');
                if (clickedDropdownLink) {
                    menu.classList.remove('open');
                    return;
                }
                if (clickedTrigger) {
                    e.preventDefault();
                    e.stopPropagation();
                    menu.classList.toggle('open');
                    return;
                }
                menu.classList.remove('open');
            });
            document.addEventListener('keydown', (e) => {
                if (e.key === 'Escape') {
                    const menu = document.getElementById('userProfileMenu');
                    if (menu) menu.classList.remove('open');
                }
            });
        }
    }
}

if (document.readyState !== 'loading') {
    initAuthLifecycle();
} else {
    document.addEventListener('DOMContentLoaded', initAuthLifecycle);
}
