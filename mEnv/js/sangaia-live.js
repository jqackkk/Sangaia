/**
 * Sangaia Live Core Interactive Script
 * Provides runtime functionality for composer, status update, user profile menu,
 * floating messages dock, interactive modals, and sovereign calculators.
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. Post Composer Handler
    const postBtn = document.getElementById('postBtn');
    const postInput = document.getElementById('postInput');
    const postsList = document.getElementById('postsList');

    if (postBtn && postInput && postsList) {
        postBtn.addEventListener('click', () => {
            const text = postInput.value.trim();
            if (!text) return;

            const newPost = document.createElement('div');
            newPost.className = 'post-item';
            newPost.innerHTML = `
                <img class="post-avatar" src="/images/default-wl.png" alt="avatar" width="44" height="44" style="width:44px; height:44px; border-radius:2px; object-fit:contain; background:#ffffff;" />
                <div class="post-content-wrap">
                    <p><a href="/id.html" class="post-author">Jqackkk</a> says: "${escapeHtml(text)}"</p>
                    <div class="post-meta">Just now &bull; Sangaia Sovereign Network</div>
                </div>
            `;

            postsList.prepend(newPost);
            postInput.value = '';
        });
    }

    // 2. Status Field Handler
    const statusField = document.getElementById('statusField');
    const clearStatusBtn = document.getElementById('clearStatusBtn');
    const updateStatusBtn = document.getElementById('updateStatusBtn');

    if (clearStatusBtn && statusField) {
        clearStatusBtn.addEventListener('click', () => {
            statusField.value = '';
            statusField.focus();
        });
    }

    if (updateStatusBtn && statusField) {
        updateStatusBtn.addEventListener('click', () => {
            const val = statusField.value.trim() || 'Serving Sangaia';
            alert(`Sovereign Status updated to: "${val}" across Sangaia Live.`);
        });
    }

    // 3. User Profile Dropdown Menu Toggle
    const userProfileMenu = document.getElementById('userProfileMenu');
    if (userProfileMenu) {
        userProfileMenu.addEventListener('click', (e) => {
            e.stopPropagation();
            userProfileMenu.classList.toggle('open');
        });

        document.addEventListener('click', () => {
            userProfileMenu.classList.remove('open');
        });
    }

    // 4. Messages Dock Handler
    const messagesDock = document.getElementById('messagesDock');
    if (messagesDock) {
        messagesDock.addEventListener('click', () => {
            alert("Citizen Dispatch: All sovereign administrative lines are operational. No pending urgent notifications for Citizen Jqackkk.");
        });
    }

    // 5. Generic Modal System Setup
    setupModalSystem();

    // 6. Interactive Unit Converter Setup (Панотерм & Мономер)
    setupUnitConverters();
});

// Format document helper for rich composer
function formatDoc(cmd) {
    document.execCommand(cmd, false, null);
}

// Utility to escape HTML
function escapeHtml(str) {
    return str.replace(/[&<>'"]/g, 
        tag => ({
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            "'": '&#39;',
            '"': '&quot;'
        }[tag] || tag)
    );
}

// Modal handling
function setupModalSystem() {
    const overlay = document.getElementById('modalOverlay');
    const closeBtn = document.getElementById('modalCloseBtn');
    const cancelBtn = document.getElementById('modalCancelBtn');

    if (!overlay) return;

    function closeModal() {
        overlay.classList.remove('active');
        const resBox = document.getElementById('modalResultsBox');
        if (resBox) resBox.classList.remove('active');
    }

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    if (cancelBtn) cancelBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) closeModal();
    });
}

// Sovereign Unit Converters (Панотерм & Мономер)
function setupUnitConverters() {
    // Temperature: °Пт = 0.9 * °C = 0.5 * (°F - 32)
    const ptInput = document.getElementById('calc-pt');
    const cInput = document.getElementById('calc-c');
    const fInput = document.getElementById('calc-f');

    if (ptInput && cInput && fInput) {
        ptInput.addEventListener('input', () => {
            const pt = parseFloat(ptInput.value);
            if (isNaN(pt)) { cInput.value = ''; fInput.value = ''; return; }
            cInput.value = (pt / 0.9).toFixed(1);
            fInput.value = ((pt * 2) + 32).toFixed(1);
        });

        cInput.addEventListener('input', () => {
            const c = parseFloat(cInput.value);
            if (isNaN(c)) { ptInput.value = ''; fInput.value = ''; return; }
            const pt = c * 0.9;
            ptInput.value = pt.toFixed(1);
            fInput.value = ((c * 9/5) + 32).toFixed(1);
        });

        fInput.addEventListener('input', () => {
            const f = parseFloat(fInput.value);
            if (isNaN(f)) { ptInput.value = ''; cInput.value = ''; return; }
            const pt = (f - 32) * 0.5;
            ptInput.value = pt.toFixed(1);
            cInput.value = ((f - 32) * 5/9).toFixed(1);
        });
    }

    // Distance: 1 Мн = 2.5 cm, 10 Мн = 1 Дмн, 30 Мн = 1 3Дмн, 40 Мн = 1 4Дмн, 60,000 Мн = 1 Кмн
    const mnInput = document.getElementById('calc-mn');
    const cmInput = document.getElementById('calc-cm');
    const inInput = document.getElementById('calc-in');
    const ftInput = document.getElementById('calc-ft');
    const mInput = document.getElementById('calc-m');
    const miInput = document.getElementById('calc-mi');

    if (mnInput) {
        mnInput.addEventListener('input', () => {
            const mn = parseFloat(mnInput.value);
            if (isNaN(mn)) {
                if (cmInput) cmInput.value = '';
                if (inInput) inInput.value = '';
                if (ftInput) ftInput.value = '';
                if (mInput) mInput.value = '';
                if (miInput) miInput.value = '';
                return;
            }
            if (cmInput) cmInput.value = (mn * 2.5).toFixed(2);
            if (inInput) inInput.value = (mn * 2.5 / 2.54).toFixed(2);
            if (ftInput) ftInput.value = (mn / 12.19).toFixed(2);
            if (mInput) mInput.value = (mn * 0.025).toFixed(3);
            if (miInput) miInput.value = (mn / 63360).toFixed(4);
        });
    }
}

    if (closeBtn) closeBtn.addEventListener('click', closeModal);
    if (cancelBtn) cancelBtn.addEventListener('click', closeModal);
    overlay.addEventListener('click', (e) => {
        if (e.target === overlay) closeModal();
    });
}

// Sovereign Unit Converters (Панотерм & Мономер)
function setupUnitConverters() {
    // Temperature: °Пт = 0.9 * °C = 0.5 * (°F - 32)
    const ptInput = document.getElementById('calc-pt');
    const cInput = document.getElementById('calc-c');
    const fInput = document.getElementById('calc-f');

    if (ptInput && cInput && fInput) {
        ptInput.addEventListener('input', () => {
            const pt = parseFloat(ptInput.value);
            if (isNaN(pt)) { cInput.value = ''; fInput.value = ''; return; }
            cInput.value = (pt / 0.9).toFixed(1);
            fInput.value = ((pt * 2) + 32).toFixed(1);
        });

        cInput.addEventListener('input', () => {
            const c = parseFloat(cInput.value);
            if (isNaN(c)) { ptInput.value = ''; fInput.value = ''; return; }
            const pt = c * 0.9;
            ptInput.value = pt.toFixed(1);
            fInput.value = ((c * 9/5) + 32).toFixed(1);
        });

        fInput.addEventListener('input', () => {
            const f = parseFloat(fInput.value);
            if (isNaN(f)) { ptInput.value = ''; cInput.value = ''; return; }
            const pt = (f - 32) * 0.5;
            ptInput.value = pt.toFixed(1);
            cInput.value = ((f - 32) * 5/9).toFixed(1);
        });
    }

    // Distance: 1 Мн = 2.5 cm, 10 Мн = 1 Дмн, 30 Мн = 1 3Дмн, 40 Мн = 1 4Дмн, 60,000 Мн = 1 Кмн
    const mnInput = document.getElementById('calc-mn');
    const cmInput = document.getElementById('calc-cm');
    const inInput = document.getElementById('calc-in');
    const ftInput = document.getElementById('calc-ft');
    const mInput = document.getElementById('calc-m');
    const miInput = document.getElementById('calc-mi');

    if (mnInput) {
        mnInput.addEventListener('input', () => {
            const mn = parseFloat(mnInput.value);
            if (isNaN(mn)) {
                if (cmInput) cmInput.value = '';
                if (inInput) inInput.value = '';
                if (ftInput) ftInput.value = '';
                if (mInput) mInput.value = '';
                if (miInput) miInput.value = '';
                return;
            }
            if (cmInput) cmInput.value = (mn * 2.5).toFixed(2);
            if (inInput) inInput.value = (mn * 2.5 / 2.54).toFixed(2);
            if (ftInput) ftInput.value = (mn / 12.19).toFixed(2);
            if (mInput) mInput.value = (mn * 0.025).toFixed(3);
            if (miInput) miInput.value = (mn / 63360).toFixed(4);
        });
    }
}

