from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)
JSON_FILE = "votes.json"

def load_data():
    if not os.path.exists(JSON_FILE):
        default_data = [
            {"candidate": "FELIPE", "votes": 0},
            {"candidate": "GONZALEZ", "votes": 0}
        ]
        with open(JSON_FILE, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4, ensure_ascii=False)
        return default_data

    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

@app.route('/')
def index():
    candidates = load_data()
    return render_template('index.html', candidates=candidates)

@app.route('/vote', methods=['POST'])
def vote():
    candidate_name = request.form.get('candidate')
    candidates = load_data()

    for c in candidates:
        if c['candidate'] == candidate_name:
            c['votes'] += 1
            break

    save_data(candidates)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
