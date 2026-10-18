import json
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
KARVANDS_FILE = DATA_DIR / "karvands.json"
REPORT_FILE = DATA_DIR / "report.json"


def empty_data():
    return {"bootcamp": "Karvand Bootcamp", "karvands": []}


def save_data(data, path=KARVANDS_FILE):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_data(path=KARVANDS_FILE):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = empty_data()
        save_data(data, path)
        return data


def save_report(report, path=REPORT_FILE):
    save_data(report, path)
