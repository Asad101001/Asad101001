import datetime

readme_path = "README.md"

with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

new_info = f"Last updated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} (UTC)\n"

if "<!--update-time-start-->" in content:
    start = content.index("<!--update-time-start-->") + len("<!--update-time-start-->")
    end = content.index("<!--update-time-end-->")
    content = content[:start] + "\n" + new_info + content[end:]
else:
    content += f"\n<!--update-time-start-->\n{new_info}<!--update-time-end-->\n"

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)

print("✅ README updated with latest timestamp!")
