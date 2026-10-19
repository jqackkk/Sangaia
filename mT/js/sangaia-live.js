/**
 * Sangaia Live Core Interactive Script
 * Provides runtime functionality for user profile menu,
 * interactive statutory modals, and sovereign calculators.
 */

document.addEventListener('DOMContentLoaded', () => {
    // 1. User Profile Dropdown Menu Toggle
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

    // 2. Generic Modal System Setup
    setupModalSystem();

    // 3. Interactive Unit Converter Setup (Панотерм & Мономер)
    setupUnitConverters();
});

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
