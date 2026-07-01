import json
import os

DATA_FOLDER = "data"
DATA_FILE = "data/karvands.json"


def setup_files():
    if not os.path.exists(DATA_FOLDER):
        os.mkdir(DATA_FOLDER)

    if not os.path.exists(DATA_FILE):
        data = {
            "bootcamp": "Karvand Bootcamp",
            "karvands": []
        }

        with open(DATA_FILE, "w") as file:
            json.dump(data, file, indent=4)
            
            
def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except:
        data = {
            "bootcamp": "Karvand Bootcamp",
            "karvands": []
        }

        save_data(data)
        return data  
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


def generate_id(karvands):
    if not karvands:
        return 1

    return karvands[-1]["id"] + 1


def add_karvand():
    data = load_data()

    full_name = input("Full name: ")
    email = input("Email: ")
    city = input("City: ")
    degree = input("Degree: ")
    major = input("Major: ")
    skill_name = input("Skill name: ")
    skill_level = input("Skill level: ")
    
    while True:
        try:
            skill_score = int(input("Skill score (0-100): "))

            if 0 <= skill_score <= 100:
                break

            print("Score must be between 0 and 100.")

        except:
            print("Please enter a number.")

    new_karvand = {
        "id": generate_id(data["karvands"]),
        "full_name": full_name,
        "email": email,
        "city": city,
        "education": {
            "degree": degree,
            "major": major
        },
        "skills": [
            {
                "name": skill_name,
                "level": skill_level,
                "score": skill_score
            }
        ]
    }

    data["karvands"].append(new_karvand)
    save_data(data)

    print("Karvand added successfully.")
    
    
def get_skill_score():
    while True:
        try:
            score = int(input("Skill score (0-100): "))

            if 0 <= score <= 100:
                return score

            print("Score must be between 0 and 100.")

        except:
            print("Please enter a number.")

def show_all_karvands():
    data = load_data()

    if len(data["karvands"]) == 0:
        print("No karvands found.")
        return

    for person in data["karvands"]:
        print("-" * 30)
        print("ID:", person["id"])
        print("Name:", person["full_name"])
        print("Email:", person["email"])
        print("City:", person["city"])
        print(
            "Education:",
            person["education"]["degree"],
            "-",
            person["education"]["major"]
        )

        print("Skills:")
        for skill in person["skills"]:
            print(
                skill["name"],
                "-",
                skill["level"],
                "-",
                skill["score"]
            )
            
add_karvand()