```python
import data as dd
import sys
import os
from datetime import datetime
import time
import json

# ADMINISTRATIVE FUNCTIONS -------------------------------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_time():
    now = datetime.now()
    br = now.strftime("%d/%m/%Y - %H:%M:%S")
    return br

def write_slow(word):
    for letter in word:
        print(letter, end='', flush=True)
        time.sleep(0.05)
    print()

def write_menu(text, skip_line=True):
    for letter in text:
        print(letter, end='', flush=True)
        time.sleep(0.05)

    if skip_line:
        print()

# JSON file path
JSON_FILE = "votes.json"

def load_data():
    """Reads the JSON file. If it doesn't exist, creates one with default data."""
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
    """Writes the updated data back to the JSON file."""
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# SYSTEMS -------------------------------------

def show_candidates():
    for t, c in enumerate(dd.candidates, start=1):
        print(f"{t} - {c['candidate']:<14} | Number of votes: {c['votes']}")

def exit_program():
    print("=" * 10)
    print("SHUTTING DOWN...")
    print("=" * 10)
```
