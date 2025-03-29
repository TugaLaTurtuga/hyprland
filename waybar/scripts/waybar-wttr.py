#!/usr/bin/env python

import json
import requests
from datetime import datetime

# Put your place like this:
# Country, City
place = 'YOUR_PLACE'

WEATHER_CODES = {
    '113': '☀️', '116': '⛅', '119': '☁️', '122': '☁️', '143': '☁️', '176': '🌧️',
    '179': '🌧️', '182': '🌧️', '185': '🌧️', '200': '⛈️', '227': '🌨️', '230': '🌨️',
    '248': '☁️', '260': '☁️', '263': '🌧️', '266': '🌧️', '281': '🌧️', '284': '🌧️',
    '293': '🌧️', '296': '🌧️', '299': '🌧️', '302': '🌧️', '305': '🌧️', '308': '🌧️',
    '311': '🌧️', '314': '🌧️', '317': '🌧️', '320': '🌨️', '323': '🌨️', '326': '🌨️',
    '329': '❄️', '332': '❄️', '335': '❄️', '338': '❄️', '350': '🌧️', '353': '🌧️',
    '356': '🌧️', '359': '🌧️', '362': '🌧️', '365': '🌧️', '368': '🌧️', '371': '❄️',
    '374': '🌨️', '377': '🌨️', '386': '🌨️', '389': '🌨️', '392': '🌧️', '395': '❄️'
}

# Fetch weather data
weather = requests.get(f"https://wttr.in/{place}?format=j1").json() if place != 'YOUR_PLACE' else requests.get("https://wttr.in/?format=j1").json()

def format_time(time):
    return str(int(time) // 100).zfill(2)  # Fixing hour formatting

def format_temp(hour):
    return f"{hour['FeelsLikeC']}°C"

def format_chances(hour):
    chances = {
        "chanceoffog": "Fog",
        "chanceoffrost": "Frost",
        "chanceofovercast": "Overcast",
        "chanceofrain": "Rain",
        "chanceofsnow": "Snow",
        "chanceofsunshine": "Sunshine",
        "chanceofthunder": "Thunder",
        "chanceofwindy": "Wind"
    }
    return ", ".join(f"{chances[event]} {hour[event]}%" for event in chances if int(hour[event]) > 0)

# Current weather
current_weather = weather['current_condition'][0]
weather_icon = WEATHER_CODES.get(current_weather['weatherCode'], "🌥️")  # Default if code is missing
data = {
    'text': f"{weather_icon} {format_temp(current_weather)}",
    'tooltip': f"<b>{weather['nearest_area'][0]['country'][0]['value']}, {weather['nearest_area'][0]['areaName'][0]['value']}</b>\n"
               f"{current_weather['weatherDesc'][0]['value']} {current_weather['temp_C']}°C\n"
               f"Wind: {current_weather['windspeedKmph']} Km/h\n"
               f"Humidity: {current_weather['humidity']}%\n"
}

# Forecast data
for i, day in enumerate(weather['weather']):
    data['tooltip'] += f"\n<b>{'Today' if i == 0 else 'Tomorrow' if i == 1 else day['date']}</b>\n"
    data['tooltip'] += f"⬆️ {day['maxtempC']}° ⬇️ {day['mintempC']}° "
    data['tooltip'] += f"🌅 {day['astronomy'][0]['sunrise']} 🌇 {day['astronomy'][0]['sunset']}\n"

    for hour in day['hourly']:
        formatted_hour = int(format_time(hour['time']))
        if i == 0 and formatted_hour < datetime.now().hour - 2:
            continue  # Skip past hours
        data['tooltip'] += f"{formatted_hour:02d} {WEATHER_CODES.get(hour['weatherCode'], '🌥️')} {format_temp(hour)} {hour['weatherDesc'][0]['value'].strip()}, {format_chances(hour)}"
        if i != 2 or formatted_hour != 21:
            data['tooltip'] += '\n'

# Output JSON for Waybar
print(json.dumps(data))
