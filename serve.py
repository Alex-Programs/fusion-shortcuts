from waitress import serve
from flask import Flask, render_template, send_from_directory
from parse import build_hotkeys
import json
from dataclasses import asdict

app = Flask(__name__)

hotkeys = build_hotkeys("shortcuts.csv")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hotkeys.json")
def hotkeys_json():
    return json.dumps([asdict(h) for h in hotkeys])


@app.route("/assets/<path:path>")
def assets(path):
    return send_from_directory("assets/", path)

print("Starting")
serve(app, host="0.0.0.0", port=8072)