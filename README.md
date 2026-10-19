# Skills Manager

[![Tests](https://github.com/alidarviish/skills-manager/actions/workflows/tests.yml/badge.svg)](https://github.com/alidarviish/skills-manager/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)

A command-line app for managing people and their skills, with data stored in a
JSON file.

It started as a single script. Later I came back to it to fix a bug, split it into
modules, and add tests and CI.

## Features

- Add, view, edit and delete people
- Search by ID or by skill name (case-insensitive)
- Input validation (numeric IDs, skill score between 0 and 100)
- Generate a summary report (total people, average skill score, cities, unique skills)
- Data saved to `data/people.json`, created automatically on first run

## Project Structure

```
skills-manager/
├── app.py          # entry point
├── cli.py          # text menu: all input() and print() calls
├── manager.py      # core logic: add, search, edit, delete, report
├── storage.py      # reading and writing JSON files
├── tests/
│   ├── test_manager.py
│   └── test_storage.py
└── .github/workflows/tests.yml   # runs the tests on every push
```

The main idea is that `manager.py` has no `input()` or `print()`. It only takes
data and returns results, so it can be tested directly, and the menu in `cli.py`
could be replaced (for example with a web UI) without touching the logic.

## Getting Started

Requires Python 3.10 or newer. No external packages are needed to run the app.

```bash
git clone https://github.com/alidarviish/skills-manager.git
cd skills-manager
python app.py
```

```
===== Skills Manager =====
1. Add Person
2. Show All People
3. Search By ID
4. Search By Skill
5. Edit Person
6. Delete Person
7. Report
8. Exit
Choose:
```

## Data Format

```json
{
    "people": [
        {
            "id": 1,
            "full_name": "Ali Ahmadi",
            "email": "ali@example.com",
            "city": "Shiraz",
            "education": { "degree": "BSc", "major": "Computer Science" },
            "skills": [
                { "name": "Python", "level": "advanced", "score": 90 }
            ]
        }
    ]
}
```

The `data/` folder is in `.gitignore`, so personal records never end up in the repository.

## Running Tests

```bash
pip install -r requirements-dev.txt
pytest
```

The tests cover the core logic and file handling, including a regression test for
an early bug where editing one person changed a different one.
