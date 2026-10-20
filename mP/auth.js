// Sangaia Unified Authentication & Cross-Subdomain Session Engine
// Ensures seamless single sign-on across sangaia.org, all 12 ministerial subdomains, and local portals.
// Strictly adheres to the One Live Metro design system (all-lowercase, Segoe WP typography, Metro UI icons).

const SUPABASE_URL = 'https://qcgdjdnihwchjargpfcc.supabase.co';
const SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFjZ2RqZG5paHdjaGphcmdwZmNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE0NzkxNTIsImV4cCI6MjEwNzA1NTE1Mn0.AfstClw4oXLj7stYL1bfyKSCMFBHZQBVBQACTT4dNLM';

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

        deleteCookieVal(key);

        const encoded = encodeURIComponent(value);
        const CHUNK_SIZE = 2800;

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
        // Wait briefly for existing script tag
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
window.getRepoRoot = getRepoRoot;

// -----------------------------------------------------------------------------
// 4. SangaiaAuth Unified Interface
// -----------------------------------------------------------------------------
window.SangaiaAuth = {
    client: () => initClient(),

    async getSession() {
        const client = initClient();
        if (!client || !client.auth) return null;
        try {
            const { data: { session }, error } = await client.auth.getSession();
            if (error) throw error;
            return session;
        } catch (e) {
            console.warn("Error getting session:", e);
            return null;
        }
    },

    async getUser() {
        const session = await this.getSession();
        return session ? session.user : null;
    },

    async getCitizenRecord(userId) {
        const client = initClient();
        if (!client || !userId) return null;
        try {
            const { data, error } = await client
                .from('sangaia_citizens')
                .select('*')
                .eq('id', userId)
                .single();
            if (error) return null;
            return data;
        } catch (e) {
            return null;
        }
    },

    async signIn(email, password) {
        const client = initClient();
        if (!client || !client.auth) {
            throw new Error("Unable to establish secure cryptographic connection. Please check your network connection.");
        }
        const { data, error } = await client.auth.signInWithPassword({ email, password });
        if (error) throw error;

        await this.refreshUI();
        this.notifyAuthChange(data.session, data.user);
        return data;
    },

    async signUp({ email, password, fullName, dob, province }) {
        const client = initClient();
        if (!client || !client.auth) {
            throw new Error("Unable to establish secure cryptographic connection.");
        }
        if (!fullName || !fullName.trim()) {
            throw new Error("Full legal name is required for citizen docket registration.");
        }

        const { data, error } = await client.auth.signUp({
            email,
            password,
            options: {
                data: {
                    full_name: fullName.trim(),
                    territory: province || 'New Jasper',
                    date_of_birth: dob || null
                }
            }
        });

        if (error) throw error;

        if (data.user) {
            // Generate sovereign citizen token: SG-2026-XXXX
            const randomHex = Math.floor(0x1000 + Math.random() * 0x8fff).toString(16).toUpperCase();
            const citizenId = `SG-2026-${randomHex}`;

            try {
                await client.from('sangaia_citizens').insert([{
                    id: data.user.id,
                    full_name: fullName.trim(),
                    sangaia_id_number: citizenId,
                    territory: province || 'New Jasper (Capital Shesk)',
                    date_of_birth: dob || null,
                    account_status: 'Statutory Verified Citizen',
                    healthcare_tier: 'Tier 1 Universal Healthcare',
                    wage_floor: '$25.00/hr Statutory Wage Floor'
                }]);
            } catch (insErr) {
                console.warn("Citizen docket profile insert notice:", insErr);
            }
        }

        await this.refreshUI();
        this.notifyAuthChange(data.session, data.user);
        return data;
    },

    async signOut() {
        const client = initClient();
        if (client && client.auth) {
            try { await client.auth.signOut(); } catch(e){}
        }
        sangaiaStorage.removeItem('sb-qcgdjdnihwchjargpfcc-auth-token');
        deleteCookieVal('sb-qcgdjdnihwchjargpfcc-auth-token');

        await this.refreshUI();
        this.notifyAuthChange(null, null);

        // If on ID page or dashboard, refresh to update card state
        if (window.location.pathname.includes('id.html') || window.location.pathname.includes('dashboard.html')) {
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
        // Don't toggle if clicking directly on a dropdown link
        if (e.target.closest('.user-dropdown')) return;
        menu.classList.toggle('open');
    },

    openAuthModal(initialTab = 'signin') {
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
async function updateAuthWidgets() {
    const profileMenu = document.getElementById('userProfileMenu');
    const legacyWidget = document.getElementById('auth-widget');
    const idUrl = getIdPageUrl();

    let session = null;
    let citizen = null;

    try {
        session = await window.SangaiaAuth.getSession();
        if (session && session.user) {
            citizen = await window.SangaiaAuth.getCitizenRecord(session.user.id);
        }
    } catch (e) {
        console.warn("Auth check warning:", e);
    }

    // 1. Update Modern One Live #userProfileMenu
    if (profileMenu) {
        if (session && session.user) {
            const rawName = (citizen && citizen.full_name) || session.user.user_metadata?.full_name || session.user.email.split('@')[0];
            const name = rawName.toLowerCase();
            const citizenId = ((citizen && citizen.sangaia_id_number) || 'sg-2026-f1e8').toLowerCase();
            const initial = name.charAt(0).toUpperCase();

            profileMenu.className = 'user-profile-menu authenticated';
            profileMenu.innerHTML = `
              <div style="width:28px; height:28px; border-radius:2px; background:var(--primary, #0078d4); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:12px; border:1px solid rgba(255,255,255,0.7); flex-shrink:0;">
                ${initial}
              </div>
              <span style="max-width:110px; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${name}</span>
              <span class="mif-arrow-drop-down" style="font-size: 14px;"></span>
              <div class="user-dropdown">
                <div class="user-dropdown-header">citizen: ${citizenId}</div>
                <a href="${idUrl}"><span class="mif-profile"></span> sangaia id card</a>
                <a href="/citizenship.html"><span class="mif-checkmark"></span> citizenship status</a>
                <a href="/index.html#units"><span class="mif-compass"></span> units &amp; measures</a>
                <a href="/dashboard.html"><span class="mif-chart-bars"></span> sovereign registry</a>
                <div style="border-top:1px solid #e1dfdd; margin:4px 0;"></div>
                <a href="javascript:void(0)" onclick="window.SangaiaAuth.signOut()"><span class="mif-exit"></span> sign out</a>
              </div>
            `;
        } else {
            profileMenu.className = 'user-profile-menu unauthenticated';
            profileMenu.innerHTML = `
              <span class="mif-user" style="font-size:15px; color:#fff;"></span>
              <span>sign in</span>
              <span class="mif-arrow-drop-down" style="font-size: 14px;"></span>
              <div class="user-dropdown">
                <div class="user-dropdown-header">sangaia id portal</div>
                <a href="javascript:void(0)" onclick="window.SangaiaAuth.openAuthModal('signin')"><span class="mif-enter"></span> sign in to sangaia id</a>
                <a href="javascript:void(0)" onclick="window.SangaiaAuth.openAuthModal('signup')"><span class="mif-user-plus"></span> register new citizen id</a>
                <a href="${idUrl}"><span class="mif-profile"></span> sovereign citizen directory</a>
                <a href="${idUrl}#verify"><span class="mif-security"></span> verify citizen docket</a>
                <div style="border-top:1px solid #e1dfdd; margin:4px 0;"></div>
                <a href="/index.html"><span class="mif-home"></span> federal home</a>
              </div>
            `;
        }
    }

    // 2. Update Legacy #auth-widget if present
    if (legacyWidget) {
        if (session && session.user) {
            const name = (citizen && citizen.full_name) || session.user.user_metadata?.full_name || 'Citizen';
            legacyWidget.innerHTML = `
                <a href="${idUrl}" title="Sangaia ID Portal" style="display: flex; align-items: center; gap: 7px; text-decoration: none; color: #fff; background: rgba(0, 40, 80, 0.4); padding: 2px 9px 2px 3px; border-radius: 20px; border: 1px solid rgba(0, 210, 255, 0.35); box-shadow: 0 0 8px rgba(0, 210, 255, 0.15);">
                    <div style="width: 22px; height: 22px; border-radius: 50%; background: linear-gradient(135deg, #0077be 0%, #00d2ff 100%); display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; color: white;">
                        ${name.charAt(0).toUpperCase()}
                    </div>
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
              need a sovereign id? <a href="javascript:void(0)" onclick="switchModalAuthTab('signup')" style="color:var(--primary, #0078d4); font-weight:600;">register new id</a>
            </div>
          </form>

          <!-- Register Form -->
          <form id="modalSignUpForm" onsubmit="handleModalSignUp(event)" style="display:none;">
            <div class="form-group" style="margin-bottom:10px;">
              <label style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; text-transform:lowercase;">full legal name</label>
              <input type="text" id="modalRegName" required placeholder="e.g. Jack Davenport" style="width:100%; border:1px solid #ccc; padding:7px 10px; font-size:13px; border-radius:2px; font-family:inherit; outline:none;" />
            </div>
            <div class="form-group" style="margin-bottom:10px;">
              <label style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; text-transform:lowercase;">date of birth</label>
              <input type="date" id="modalRegDob" style="width:100%; border:1px solid #ccc; padding:7px 10px; font-size:13px; border-radius:2px; font-family:inherit; outline:none;" />
            </div>
            <div class="form-group" style="margin-bottom:10px;">
              <label style="display:block; font-size:12px; font-weight:600; margin-bottom:4px; text-transform:lowercase;">provincial jurisdiction</label>
              <select id="modalRegProvince" style="width:100%; border:1px solid #ccc; padding:7px 10px; font-size:13px; border-radius:2px; font-family:inherit; outline:none; background:#fff;">
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
          <div><span class="mif-security"></span> aeretocratic cryptographic seal</div>
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
            if (window.location.pathname.includes('id.html') || window.location.pathname.includes('dashboard.html')) {
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
            if (window.location.pathname.includes('id.html') || window.location.pathname.includes('dashboard.html')) {
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
document.addEventListener('DOMContentLoaded', () => {
    // 1. Initial auth check
    updateAuthWidgets();

    // 2. Ensure Supabase client is initialized
    ensureSupabaseLoaded((client) => {
        if (client && client.auth) {
            client.auth.onAuthStateChange((event, session) => {
                updateAuthWidgets();
                window.SangaiaAuth.notifyAuthChange(session, session ? session.user : null);
            });
        }
    });

    // 3. User profile click handler
    const menu = document.getElementById('userProfileMenu');
    if (menu) {
        menu.addEventListener('click', (e) => {
            window.SangaiaAuth.handleProfileClick(e);
        });
        document.addEventListener('click', (e) => {
            if (!menu.contains(e.target)) {
                menu.classList.remove('open');
            }
        });
    }
});
