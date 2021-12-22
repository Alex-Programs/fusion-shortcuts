from waitress import serve
from flask import Flask, render_template, send_from_directory, send_file
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


@app.route("/shortcuts.csv")
def shortcuts():
    return send_file("shortcuts.csv")


HOST = "0.0.0.0"
PORT = 8072
print(f"Starting on {HOST}:{PORT}")
serve(app, host=HOST, port=PORT)
