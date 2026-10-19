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

    // 4. Sub-Navigation Tab State Handling
    setupSubnavTabs();
});

// Sub-Navigation Tab State Handling
function setupSubnavTabs() {
    function updateActiveTab() {
        const hash = window.location.hash;
        if (!hash) return;
        const subnavLinks = document.querySelectorAll('.subnav a');
        subnavLinks.forEach(link => {
            const href = link.getAttribute('href');
            if (href === hash || (href && href.endsWith(hash))) {
                subnavLinks.forEach(l => l.classList.remove('active'));
                link.classList.add('active');
            }
        });
    }

    document.querySelectorAll('.subnav a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function() {
            document.querySelectorAll('.subnav a').forEach(a => a.classList.remove('active'));
            this.classList.add('active');
        });
    });

    window.addEventListener('hashchange', updateActiveTab);
    updateActiveTab();
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
    // 1. Rich Temperature Engine: inPt, inC, inF
    const inPt = document.getElementById('inPt');
    const inC = document.getElementById('inC');
    const inF = document.getElementById('inF');
    const tempText = document.getElementById('tempMentalText');

    if (inPt && inC && inF) {
        function updateTemp(c, source) {
            const pt = c * 0.9;
            const f = c * 1.8 + 32;

            if (source !== 'pt') inPt.value = (Math.round(pt * 10) / 10).toFixed(1).replace('.0','');
            if (source !== 'c') inC.value = (Math.round(c * 10) / 10).toFixed(1).replace('.0','');
            if (source !== 'f') inF.value = (Math.round(f * 10) / 10).toFixed(1).replace('.0','');

            const ptR = Math.round(pt);
            const fR = Math.round(f);
            const cR = Math.round(c);
            if (tempText) {
                tempText.innerHTML = `• <strong>from fahrenheit (${fR}&deg;f)</strong>: drop 32 (${fR - 32}), cut in half &rarr; <strong>${ptR}&deg;пт</strong>.<br>• <strong>from celsius (${cR}&deg;c)</strong>: subtract 10% (-${(cR*0.1).toFixed(1)}) &rarr; <strong>${ptR}&deg;пт</strong>.`;
            }
        }

        inPt.addEventListener('input', () => {
            const v = parseFloat(inPt.value);
            if (!isNaN(v)) updateTemp(v / 0.9, 'pt');
        });
        inC.addEventListener('input', () => {
            const v = parseFloat(inC.value);
            if (!isNaN(v)) updateTemp(v, 'c');
        });
        inF.addEventListener('input', () => {
            const v = parseFloat(inF.value);
            if (!isNaN(v)) updateTemp((v - 32) / 1.8, 'f');
        });
    }

    // 2. Rich Distance Engine: distVal, distUnit, distOutputGrid, distMentalText
    const distVal = document.getElementById('distVal');
    const distUnit = document.getElementById('distUnit');
    const grid = document.getElementById('distOutputGrid');
    const distText = document.getElementById('distMentalText');

    if (distVal && distUnit && grid) {
        const toMn = {
            'mn': 1.0, 'dmn': 10.0, 'trideka': 30.0, 'kvadrodeka': 40.0, 'kmn': 60000.0,
            'cm': 0.4, 'm': 40.0, 'in': 1.016, 'ft': 12.192, 'mi': 64373.76
        };

        function updateDist() {
            const v = parseFloat(distVal.value) || 0;
            const u = distUnit.value;
            const mn = v * (toMn[u] || 1.0);

            const dmn = mn / 10.0;
            const tri = mn / 30.0;
            const kva = mn / 40.0;
            const kmn = mn / 60000.0;

            const cm = mn * 2.5;
            const m = cm / 100.0;
            const inches = cm / 2.54;
            const feet = inches / 12.0;
            const miles = feet / 5280.0;

            function fmt(n) {
                if (n === 0) return '0';
                if (Math.abs(n) >= 1000) return n.toLocaleString('en-US', { maximumFractionDigits: 2 });
                return (Math.round(n * 1000) / 1000).toString();
            }

            grid.innerHTML = `
                <div class="ol-metric-box">
                    <div class="ol-metric-val">${fmt(mn)} мн</div>
                    <div class="ol-metric-lbl">мономер (knuckle ~1 in)</div>
                </div>
                <div class="ol-metric-box">
                    <div class="ol-metric-val">${fmt(dmn)} дмн</div>
                    <div class="ol-metric-lbl">декамер (foot ~1 ft)</div>
                </div>
                <div class="ol-metric-box">
                    <div class="ol-metric-val">${fmt(tri)} 3дмн</div>
                    <div class="ol-metric-lbl">тридека (stride ~1 yd)</div>
                </div>
                <div class="ol-metric-box">
                    <div class="ol-metric-val">${fmt(kva)} 4дмн</div>
                    <div class="ol-metric-lbl">квадродека (exactly 1.0 m)</div>
                </div>
                <div class="ol-metric-box">
                    <div class="ol-metric-val">${fmt(kmn)} кмн</div>
                    <div class="ol-metric-lbl">киломер (walk ~1 mi)</div>
                </div>
                <div class="ol-metric-box" style="background:#f1f5f9;">
                    <div class="ol-metric-val" style="font-size:18px; color:#334155;">${fmt(cm)} cm / ${fmt(feet)} ft</div>
                    <div class="ol-metric-lbl">legacy metric / imperial</div>
                </div>
            `;

            if (distText) {
                distText.innerHTML = `• <strong>monomers to centimeters</strong>: multiply by 2.5 (${fmt(mn)} мн &times; 2.5 = <strong>${fmt(cm)} cm</strong>).<br>• <strong>kilomers to miles</strong>: drop last three zeros and divide by 6 (${fmt(kmn*60000)} мн &rarr; ${fmt(kmn*60)} &divide; 6 = <strong>${fmt(kmn*10)} mi</strong>).`;
            }
        }

        distVal.addEventListener('input', updateDist);
        distUnit.addEventListener('change', updateDist);
        updateDist();
    }

    // 3. Fallback / Sidebar Temperature: calc-pt, calc-c, calc-f
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

    // 4. Fallback / Sidebar Distance: calc-mn, calc-cm, etc.
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

