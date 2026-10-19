/**
 * SANGAIA LIVE INTERACTIVE SCRIPT
 * Provides One Live Wave 4 interactions across all portals:
 * - Profile dropdown menu
 * - Citizen dock support toggle
 * - Universal search redirect
 * - Sovereign Units telemetry helpers (°Пт and Мн)
 */

document.addEventListener('DOMContentLoaded', function () {
    // 1. Profile Dropdown Toggle
    var meChip = document.getElementById('meChip');
    var meMenu = document.getElementById('meMenu');
    if (meChip && meMenu) {
        meChip.addEventListener('click', function (e) {
            e.stopPropagation();
            var isShown = meMenu.style.display === 'block';
            meMenu.style.display = isShown ? 'none' : 'block';
        });
        document.addEventListener('click', function () {
            meMenu.style.display = 'none';
        });
    }

    // 2. Citizen Support Dock Toggle
    var dockTab = document.getElementById('olDockMessages');
    var dockList = document.getElementById('olDockList');
    var dockClose = document.getElementById('olDockListClose');
    if (dockTab && dockList) {
        dockTab.addEventListener('click', function (e) {
            e.stopPropagation();
            dockList.classList.toggle('show');
        });
        if (dockClose) {
            dockClose.addEventListener('click', function (e) {
                e.stopPropagation();
                dockList.classList.remove('show');
            });
        }
        document.addEventListener('click', function (e) {
            if (!dockList.contains(e.target) && e.target !== dockTab) {
                dockList.classList.remove('show');
            }
        });
    }

    // 3. Header Search Form Handler
    var headerSearch = document.getElementById('headerSearchForm');
    if (headerSearch) {
        headerSearch.addEventListener('submit', function (e) {
            e.preventDefault();
            var q = (document.getElementById('headerSearch') || {}).value;
            if (q) {
                window.location.href = '/services.html?q=' + encodeURIComponent(q);
            }
        });
    }
});

// Global Sovereign Conversion Helpers
window.SangaiaUnits = {
    celsiusToPt: function (c) {
        return Math.round(c * 0.9 * 10) / 10;
    },
    fahrenheitToPt: function (f) {
        return Math.round(0.5 * (f - 32) * 10) / 10;
    },
    ptToCelsius: function (pt) {
        return Math.round((pt / 9) * 10 * 10) / 10;
    },
    ptToFahrenheit: function (pt) {
        return Math.round((pt * 2 + 32) * 10) / 10;
    },
    cmToMonomer: function (cm) {
        return Math.round((cm / 2.5) * 100) / 100;
    },
    monomerToCm: function (mn) {
        return Math.round(mn * 2.5 * 100) / 100;
    },
    monomerToMiles: function (mn) {
        return Math.round((mn / 60000) * 100) / 100;
    }
};
