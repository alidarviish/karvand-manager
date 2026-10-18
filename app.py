import json
import os


def setup_files():
    if not os.path.exists("data"):
        os.mkdir("data")

    if not os.path.exists("data/karvands.json"):
        data = {
            "bootcamp": "Karvand Bootcamp",
            "karvands": []
        }

        with open("data/karvands.json", "w") as file:
            json.dump(data, file, indent=4)
            
            
def load_data():
    try:
        with open("data/karvands.json", "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        data = {
            "bootcamp": "Karvand Bootcamp",
            "karvands": []
        }

        save_data(data)
        return data
    

def save_data(data):
    with open("data/karvands.json", "w") as file:
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

        except ValueError:
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
            
            
def search_by_id():
    data = load_data()

    try:
        target_id = int(input("Enter id: "))
    except ValueError:
        print("Invalid id.")
        return

    for person in data["karvands"]:
        if person["id"] == target_id:
            print(person)
            return

    print("Karvand not found.")
    
def search_by_skill():
    data = load_data()

    skill_name = input("Enter skill name: ").lower()
    found = False

    for person in data["karvands"]:
        for skill in person["skills"]:
            if skill["name"].lower() == skill_name:
                print(person["full_name"])
                found = True

    if not found:
        print("No karvand found.")

def edit_karvand():
    data = load_data()

    try:
        target_id = int(input("Enter id: "))
    except ValueError:
        print("Invalid id.")
        return

    for person in data["karvands"]:
        if person["id"] != target_id:
            continue

        print("1. Email")
        print("2. City")
        print("3. Degree")
        print("4. Major")

        try:
            choice = int(input("Choose what to edit: "))
        except ValueError:
            print("Please enter a number.")
            return

        if choice == 1:
            person["email"] = input("New email: ")

        elif choice == 2:
            person["city"] = input("New city: ")

        elif choice == 3:
            person["education"]["degree"] = input("New degree: ")

        elif choice == 4:
            person["education"]["major"] = input("New major: ")

        else:
            print("Invalid choice.")
            return

        save_data(data)
        print("Karvand updated.")
        return

    print("Karvand not found.")
    

def delete_karvand():
    data = load_data()

    try:
        target_id = int(input("Enter id: "))
    except ValueError:
        print("Invalid id.")
        return

    for person in data["karvands"]:
        if person["id"] == target_id:
            data["karvands"].remove(person)
            save_data(data)
            print("Karvand deleted.")
            return

    print("Karvand not found.")


def create_report():
    data = load_data()

    total_karvands = len(data["karvands"])
    total_skills = 0
    total_score = 0
    cities = []
    unique_skills = []

    for person in data["karvands"]:
        if person["city"] not in cities:
            cities.append(person["city"])

        for skill in person["skills"]:
            total_skills += 1
            total_score += skill["score"]

            if skill["name"] not in unique_skills:
                unique_skills.append(skill["name"])

    average_score = 0

    if total_skills > 0:
        average_score = total_score / total_skills

    report = {
        "total_karvands": total_karvands,
        "total_skills": total_skills,
        "average_skill_score": average_score,
        "cities": cities,
        "unique_skills": unique_skills
    }

    with open("data/report.json", "w") as file:
        json.dump(report, file, indent=4)

    print(report)


def menu():
    setup_files()

    while True:
        print("\n===== Karvand Manager =====")
        print("1. Add Karvand")
        print("2. Show All Karvands")
        print("3. Search By ID")
        print("4. Search By Skill")
        print("5. Edit Karvand")
        print("6. Delete Karvand")
        print("7. Report")
        print("8. Exit")

        choice = input("Choose: ")

        if choice == "1":
            add_karvand()

        elif choice == "2":
            show_all_karvands()

        elif choice == "3":
            search_by_id()

        elif choice == "4":
            search_by_skill()

        elif choice == "5":
            edit_karvand()

        elif choice == "6":
            delete_karvand()

        elif choice == "7":
            create_report()

        elif choice == "8":
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


menu()