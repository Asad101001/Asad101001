#!/usr/bin/env python3
import os, re, io, sys, subprocess, datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
TEMPLATE = BASE / 'README_TEMPLATE.md'
OUT = BASE / 'README.md'

def run_py(script):
    try:
        out = subprocess.check_output([sys.executable, str(script)], stderr=subprocess.STDOUT, timeout=30)
        return out.decode().strip()
    except Exception as e:
        return None

def replace_between(text, start_marker, end_marker, new_content):
    pattern = re.compile(re.escape(start_marker) + r".*?" + re.escape(end_marker), re.DOTALL)
    replacement = start_marker + "\n" + new_content.strip() + "\n" + end_marker
    new_text, n = pattern.subn(replacement, text, count=1)
    return new_text, n

def main():
    tpl = TEMPLATE.read_text(encoding='utf-8')

    # Quote
    quote = run_py(BASE/'scripts'/'fetch_quote.py') or "Keep shipping."
    tpl, n = replace_between(tpl, "<!-- QUOTE_START -->", "<!-- QUOTE_END -->", quote)

    # Weather
    weather = run_py(BASE/'scripts'/'fetch_weather.py') or "Weather unavailable"
    tpl, n = replace_between(tpl, "<!-- WEATHER_START -->", "<!-- WEATHER_END -->", weather)

    # Write output README
    OUT.write_text(tpl, encoding='utf-8')
    print("Wrote README.md")

if __name__ == '__main__':
    main()
