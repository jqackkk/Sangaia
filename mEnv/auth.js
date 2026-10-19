// Sangaia Unified Authentication & Cross-Subdomain Session Engine
// Ensures seamless single sign-on between sangaia.org, healthcare.sangaia.org, and all department portals

if (typeof window.supabase === 'undefined') {
    window.supabase = null;
}

const supabaseUrl = 'https://qcgdjdnihwchjargpfcc.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFjZ2RqZG5paHdjaGphcmdwZmNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE0NzkxNTIsImV4cCI6MjEwNzA1NTE1Mn0.AfstClw4oXLj7stYL1bfyKSCMFBHZQBVBQACTT4dNLM';

// Cross-subdomain cookie domain helper (.sangaia.org allows sharing between sangaia.org & healthcare.sangaia.org)
function getCookieDomain() {
    try {
        const host = window.location.hostname;
        if (host.endsWith('sangaia.org')) {
            return '; domain=.sangaia.org';
        }
    } catch(e) {}
    return '';
}

function setCookieVal(key, value) {
    try {
        const domain = getCookieDomain();
        const secure = (window.location.protocol === 'https:') ? '; Secure' : '';
        const maxAge = '; max-age=31536000; path=/; SameSite=Lax';

        // Clear previous chunks
        deleteCookieVal(key);

        const encoded = encodeURIComponent(value);
        const CHUNK_SIZE = 2800; // Well below standard 4096-byte cookie limit

        if (encoded.length <= CHUNK_SIZE) {
            document.cookie = `${key}=${encoded}${domain}${maxAge}${secure}`;
        } else {
            const numChunks = Math.ceil(encoded.length / CHUNK_SIZE);
            document.cookie = `${key}_chunks=${numChunks}${domain}${maxAge}${secure}`;
            for (let i = 0; i < numChunks; i++) {
                const chunk = encoded.substring(i * CHUNK_SIZE, (i + 1) * CHUNK_SIZE);
                document.cookie = `${key}_${i}=${chunk}${domain}${maxAge}${secure}`;
            }
        }
    } catch (e) {
        console.warn("Error setting auth cookie:", e);
    }
}

function getCookieVal(key) {
    try {
        const cookies = document.cookie.split('; ').reduce((acc, curr) => {
            const [k, ...v] = curr.split('=');
            if (k) acc[k.trim()] = v.join('=');
            return acc;
        }, {});

        if (cookies[`${key}_chunks`]) {
            const numChunks = parseInt(cookies[`${key}_chunks`], 10);
            let full = '';
            for (let i = 0; i < numChunks; i++) {
                if (cookies[`${key}_${i}`]) full += cookies[`${key}_${i}`];
            }
            return decodeURIComponent(full);
        } else if (cookies[key]) {
            return decodeURIComponent(cookies[key]);
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
        document.cookie = `${key}=${domain}${past}`;
        document.cookie = `${key}_chunks=${domain}${past}`;
        for (let i = 0; i < 10; i++) {
            document.cookie = `${key}_${i}=${domain}${past}`;
        }
    } catch (e) {}
}

// Universal Storage Adapter for Supabase: Cross-Subdomain Cookies + LocalStorage Sync
const sangaiaStorage = {
    getItem: (key) => {
        // 1. Try cross-subdomain cookie first
        const cookieVal = getCookieVal(key);
        if (cookieVal) {
            try { window.localStorage.setItem(key, cookieVal); } catch(e){}
            return cookieVal;
        }
        // 2. Fallback to localStorage and sync back to cookie
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

// Overwrite the global library object with initialized client using cross-subdomain storage
if (window.supabase && typeof window.supabase.createClient === 'function') {
    window.supabase = window.supabase.createClient(supabaseUrl, supabaseKey, {
        auth: {
            storage: sangaiaStorage,
            autoRefreshToken: true,
            persistSession: true,
            detectSessionInUrl: true
        }
    });
}

// Determine relative path to repository root
function getRepoRoot() {
    const path = window.location.pathname;
    if (path.includes('/mH/ddcr/sgn/')) return '../../../';
    if (path.includes('/mH/ddcr/') || path.includes('/mH/sgn/')) return '../../';
    if (path.includes('/mH/') || path.includes('/sgn/')) return '../';
    return './';
}

function getIdPageUrl() {
    const isSgn = window.location.pathname.includes('/sgn/') || window.location.pathname.endsWith('/sgn');
    const isHosted = window.location.hostname.endsWith('sangaia.org');
    
    if (isHosted) {
        return isSgn ? 'https://sangaia.org/sgn/id.html' : 'https://sangaia.org/id.html';
    }
    
    const root = getRepoRoot();
    return isSgn ? root + 'sgn/id.html' : root + 'id.html';
}

window.getIdPageUrl = getIdPageUrl;

async function updateAuthWidget() {
    const widget = document.getElementById('auth-widget');
    if (!widget) return;

    const idUrl = getIdPageUrl();
    const defaultBtn = `<a href="${idUrl}" style="color: #bbb; text-decoration: none; font-size: 11px; font-weight: bold; letter-spacing: 0.5px; padding: 3px 8px; border: 1px solid #444; border-radius: 4px; background: linear-gradient(to bottom, #555, #333); box-shadow: 0 1px 2px rgba(0,0,0,0.3); transition: all 0.2s ease; display: inline-flex; align-items: center; gap: 5px;">
        <span style="display:inline-block; width:7px; height:7px; border-radius:50%; background:#00d2ff; box-shadow:0 0 5px #00d2ff;"></span>
        <span>Sangaia ID</span>
    </a>`;

    if (!supabase || !supabase.auth) {
        widget.innerHTML = defaultBtn;
        return;
    }

    try {
        const { data: { session }, error } = await supabase.auth.getSession();
        
        if (session) {
            const { data: citizen } = await supabase
                .from('sangaia_citizens')
                .select('full_name')
                .eq('id', session.user.id)
                .single();

            const name = citizen ? citizen.full_name : (session.user.user_metadata?.full_name || 'Citizen');
            
            widget.innerHTML = `
                <a href="${idUrl}" title="Sangaia ID Portal" style="display: flex; align-items: center; gap: 7px; text-decoration: none; color: #fff; background: rgba(0, 40, 80, 0.4); padding: 2px 9px 2px 3px; border-radius: 20px; border: 1px solid rgba(0, 210, 255, 0.35); box-shadow: 0 0 8px rgba(0, 210, 255, 0.15);">
                    <div style="width: 22px; height: 22px; border-radius: 50%; background: linear-gradient(135deg, #0077be 0%, #00d2ff 100%); display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; color: white; text-shadow: 0 1px 2px rgba(0,0,0,0.5);">
                        ${name.charAt(0).toUpperCase()}
                    </div>
                    <span style="font-size: 11px; font-weight: bold; font-family: 'Lucida Grande', sans-serif;">${name}</span>
                    <span style="background: rgba(0, 210, 255, 0.2); border: 1px solid rgba(0, 210, 255, 0.5); border-radius: 8px; font-size: 9px; padding: 1px 5px; color: #00e5ff; font-weight: bold; letter-spacing: 0.5px;">ID</span>
                </a>
            `;
        } else {
            widget.innerHTML = defaultBtn;
        }
    } catch (e) {
        console.error("Supabase auth error:", e);
        widget.innerHTML = defaultBtn;
    }
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', updateAuthWidget);
} else {
    updateAuthWidget();
}

if (window.supabase && window.supabase.auth) {
    window.supabase.auth.onAuthStateChange((event, session) => {
        updateAuthWidget();
    });
}
