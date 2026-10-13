// Ensure global variable exists to prevent ReferenceErrors if CDN is blocked
if (typeof window.supabase === 'undefined') {
    window.supabase = null;
}

const supabaseUrl = 'https://qcgdjdnihwchjargpfcc.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFjZ2RqZG5paHdjaGphcmdwZmNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE0NzkxNTIsImV4cCI6MjEwNzA1NTE1Mn0.AfstClw4oXLj7stYL1bfyKSCMFBHZQBVBQACTT4dNLM';

// Overwrite the global library object with the initialized client
if (window.supabase && typeof window.supabase.createClient === 'function') {
    window.supabase = window.supabase.createClient(supabaseUrl, supabaseKey);
}

const scripts = document.getElementsByTagName('script');
let rootPath = '';
for (let i = 0; i < scripts.length; i++) {
    const src = scripts[i].getAttribute('src');
    if (src && src.endsWith('auth.js')) {
        rootPath = src.replace('auth.js', '');
        break;
    }
}

async function updateAuthWidget() {
    const widget = document.getElementById('auth-widget');
    if (!widget) return;

    const defaultBtn = `<a href="${rootPath}dashboard.html" style="color: #bbb; text-decoration: none; font-size: 11px; font-weight: bold; letter-spacing: 0.5px; padding: 3px 8px; border: 1px solid #444; border-radius: 4px; background: linear-gradient(to bottom, #555, #333); transition: all 0.2s ease;">Sign In / Register</a>`;

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

            const name = citizen ? citizen.full_name : 'Citizen';
            
            widget.innerHTML = `
                <a href="${rootPath}dashboard.html" style="display: flex; align-items: center; gap: 8px; text-decoration: none; color: #fff; background: rgba(0,0,0,0.2); padding: 2px 8px 2px 2px; border-radius: 20px; border: 1px solid rgba(255,255,255,0.1);">
                    <div style="width: 22px; height: 22px; border-radius: 50%; background: #0077be; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: bold; color: white;">
                        ${name.charAt(0).toUpperCase()}
                    </div>
                    <span style="font-size: 11px; font-weight: bold; font-family: 'Lucida Grande', sans-serif;">${name}</span>
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
