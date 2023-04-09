import json
from dataclasses import asdict
from parse import build_hotkeys
import shutil

hotkeys = build_hotkeys("shortcuts.csv")

# Rm assets
shutil.rmtree("build/assets", ignore_errors=True)

with open("build/hotkeys.json", "w") as f:
    json.dump([asdict(h) for h in hotkeys], f)

# Copy assets
shutil.copytree("assets", "build/assets")

# Copy shortcuts.csv
shutil.copy("shortcuts.csv", "build/shortcuts.csv")

# Copy index.html
shutil.copy("templates/index.html", "build/index.html")