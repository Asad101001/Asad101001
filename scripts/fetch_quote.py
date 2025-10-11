#!/usr/bin/env python3
import requests, sys
def get_quote():
    try:
        r = requests.get("https://zenquotes.io/api/random", timeout=10)
        r.raise_for_status()
        j = r.json()
        if isinstance(j, list) and len(j)>0:
            q = j[0].get('q','')
            a = j[0].get('a','')
            return f"“{q}” — {a}"
    except Exception as e:
        return "“Keep shipping.” — Unknown"
if __name__ == '__main__':
    print(get_quote())
