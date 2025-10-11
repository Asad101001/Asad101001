#!/usr/bin/env python3
import os, requests, sys
def get_weather():
    key = os.getenv("OPENWEATHER_KEY", "").strip()
    if not key:
        return "Weather: API key not set"
    try:
        q = "Karachi,PK"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={q}&appid={key}&units=metric"
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        j = r.json()
        temp = j['main']['temp']
        desc = j['weather'][0]['description'].capitalize()
        return f"🌤 Current Weather in Karachi: {temp}°C | {desc}"
    except Exception as e:
        return "Weather unavailable"
if __name__ == '__main__':
    print(get_weather())
