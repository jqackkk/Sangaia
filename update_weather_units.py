#!/usr/bin/env python3
"""
Updates weather widgets in environment pages to default to Панотерм (°Пт)
and Kilomers per hour (Кмн/h), with three-way toggling (°Пт -> °C -> °F).
"""

import os

env_files = [
    'environment.html', 'MtE/index.html', 'mEnv/index.html',
    'sgn/environment.html', 'MtE/sgn/index.html', 'mEnv/sgn/index.html'
]

old_weather_js = """    let currentTempC = 21;
    let isFahrenheit = false;"""

new_weather_js = """    let currentTempC = 21;
    let currentUnitMode = 'Pt'; // 'Pt' (Панотерм), 'C' (Celsius), 'F' (Fahrenheit)"""

old_render_fn = """    function renderForecast(list) {
        const container = document.getElementById('forecast-container');
        if (!container) return;
        container.innerHTML = list.map(item => {
            const max = isFahrenheit ? Math.round(item.max * 9/5 + 32) : Math.round(item.max);
            const min = isFahrenheit ? Math.round(item.min * 9/5 + 32) : Math.round(item.min);
            const unit = isFahrenheit ? "°F" : "°";
            return `
                <div class="forecast-day-box">
                    <div class="forecast-day-name">${item.day}</div>
                    <div class="forecast-icon">${item.icon}</div>
                    <div class="forecast-temps">${max}${unit} <span style="font-size:0.75rem; color:#64748b; font-weight:normal;">/ ${min}${unit}</span></div>
                </div>
            `;
        }).join('');
    }

    function updateWeatherUI(name, tempC, feelsC, condText, icon, hum, wind, aqi, precip, forecast) {
        currentTempC = tempC;
        document.getElementById('weather-station-name').textContent = name;
        document.getElementById('weather-condition-desc').textContent = condText;
        document.getElementById('weather-icon').textContent = icon;
        document.getElementById('weather-humidity').textContent = hum;
        document.getElementById('weather-wind').textContent = wind;
        document.getElementById('weather-aqi').textContent = aqi;
        document.getElementById('weather-precip').textContent = precip;

        const dispTemp = isFahrenheit ? Math.round(tempC * 9/5 + 32) : Math.round(tempC);
        const dispFeels = isFahrenheit ? Math.round(feelsC * 9/5 + 32) : Math.round(feelsC);
        const unit = isFahrenheit ? "°F" : "°C";

        document.getElementById('weather-temp').textContent = dispTemp;
        document.getElementById('weather-unit').textContent = unit;
        document.getElementById('weather-feels').innerHTML = `Feels like ${dispFeels}${unit} &bull; Optimal Ambient Humidity`;

        if (forecast) renderForecast(forecast);
    }

    function toggleTempUnit() {
        isFahrenheit = !isFahrenheit;
        const station = document.getElementById('weather-station-name').textContent;
        const temp = isFahrenheit ? Math.round(currentTempC * 9/5 + 32) : Math.round(currentTempC);
        document.getElementById('weather-temp').textContent = temp;
        document.getElementById('weather-unit').textContent = isFahrenheit ? "°F" : "°C";
        
        // Re-render forecast with updated unit
        const activePill = document.querySelector('.station-pill.active');
        const key = activePill ? activePill.getAttribute('onclick').match(/'(.*)'/)[1] : 'veridia';
        if (provincialStations[key]) renderForecast(provincialStations[key].forecast);
    }"""

new_render_fn = """    function renderForecast(list) {
        const container = document.getElementById('forecast-container');
        if (!container) return;
        container.innerHTML = list.map(item => {
            let max, min, unit;
            if (currentUnitMode === 'Pt') {
                max = Math.round(item.max * 0.9);
                min = Math.round(item.min * 0.9);
                unit = "°Пт";
            } else if (currentUnitMode === 'F') {
                max = Math.round(item.max * 9/5 + 32);
                min = Math.round(item.min * 9/5 + 32);
                unit = "°F";
            } else {
                max = Math.round(item.max);
                min = Math.round(item.min);
                unit = "°C";
            }
            return `
                <div class="forecast-day-box">
                    <div class="forecast-day-name">${item.day}</div>
                    <div class="forecast-icon">${item.icon}</div>
                    <div class="forecast-temps">${max}${unit} <span style="font-size:0.75rem; color:#64748b; font-weight:normal;">/ ${min}${unit}</span></div>
                </div>
            `;
        }).join('');
    }

    function updateWeatherUI(name, tempC, feelsC, condText, icon, hum, wind, aqi, precip, forecast) {
        currentTempC = tempC;
        document.getElementById('weather-station-name').textContent = name;
        document.getElementById('weather-condition-desc').textContent = condText;
        document.getElementById('weather-icon').textContent = icon;
        document.getElementById('weather-humidity').textContent = hum;
        
        // Convert wind to Sangaian Kilomer/h (1 Кмн = 1.5 km)
        const windNum = parseInt(wind) || 12;
        const windKmn = Math.round(windNum / 1.5);
        document.getElementById('weather-wind').textContent = `${windKmn} Кмн/h (${windNum} km/h)`;
        document.getElementById('weather-aqi').textContent = aqi;
        document.getElementById('weather-precip').textContent = precip;

        let dispTemp, dispFeels, unit, subtext;
        if (currentUnitMode === 'Pt') {
            dispTemp = Math.round(tempC * 0.9);
            dispFeels = Math.round(feelsC * 0.9);
            unit = "°Пт";
            subtext = `Feels like ${dispFeels}°Пт (${Math.round(feelsC)}°C / ${Math.round(feelsC * 9/5 + 32)}°F) &bull; Панотерм Scale`;
        } else if (currentUnitMode === 'F') {
            dispTemp = Math.round(tempC * 9/5 + 32);
            dispFeels = Math.round(feelsC * 9/5 + 32);
            unit = "°F";
            subtext = `Feels like ${dispFeels}°F (${Math.round(tempC * 0.9)}°Пт) &bull; Fahrenheit Scale`;
        } else {
            dispTemp = Math.round(tempC);
            dispFeels = Math.round(feelsC);
            unit = "°C";
            subtext = `Feels like ${dispFeels}°C (${Math.round(tempC * 0.9)}°Пт) &bull; Celsius Scale`;
        }

        document.getElementById('weather-temp').textContent = dispTemp;
        document.getElementById('weather-unit').textContent = unit;
        document.getElementById('weather-feels').innerHTML = subtext;

        if (forecast) renderForecast(forecast);
    }

    function toggleTempUnit() {
        if (currentUnitMode === 'Pt') {
            currentUnitMode = 'C';
        } else if (currentUnitMode === 'C') {
            currentUnitMode = 'F';
        } else {
            currentUnitMode = 'Pt';
        }
        
        let temp, unit, feels;
        if (currentUnitMode === 'Pt') {
            temp = Math.round(currentTempC * 0.9);
            unit = "°Пт";
            feels = `Feels like ${temp}°Пт (${Math.round(currentTempC)}°C) &bull; Панотерм Scale`;
        } else if (currentUnitMode === 'F') {
            temp = Math.round(currentTempC * 9/5 + 32);
            unit = "°F";
            feels = `Feels like ${temp}°F (${Math.round(currentTempC * 0.9)}°Пт) &bull; Fahrenheit Scale`;
        } else {
            temp = Math.round(currentTempC);
            unit = "°C";
            feels = `Feels like ${temp}°C (${Math.round(currentTempC * 0.9)}°Пт) &bull; Celsius Scale`;
        }

        document.getElementById('weather-temp').textContent = temp;
        document.getElementById('weather-unit').textContent = unit;
        document.getElementById('weather-feels').innerHTML = feels;
        
        // Re-render forecast with updated unit
        const activePill = document.querySelector('.station-pill.active');
        const key = activePill ? activePill.getAttribute('onclick').match(/'(.*)'/)[1] : 'veridia';
        if (provincialStations[key]) renderForecast(provincialStations[key].forecast);
    }"""

for fpath in env_files:
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update initial HTML values
        content = content.replace('<span class="weather-degrees" id="weather-temp">21</span>', '<span class="weather-degrees" id="weather-temp">19</span>')
        content = content.replace('<span class="weather-unit-toggle" onclick="toggleTempUnit()" id="weather-unit">°C</span>', '<span class="weather-unit-toggle" onclick="toggleTempUnit()" id="weather-unit" title="Click to cycle °Пт / °C / °F">°Пт</span>')
        content = content.replace('Feels like 21°C &bull; Optimal Ambient Humidity', 'Feels like 19°Пт (21°C / 70°F) &bull; Панотерм Scale')

        # Replace JS definitions
        content = content.replace(old_weather_js, new_weather_js)
        content = content.replace(old_render_fn, new_render_fn)

        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated weather in {fpath}')
