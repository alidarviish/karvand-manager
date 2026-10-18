"""Text menu. All input() and print() calls live here."""
import manager
import storage


def ask_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter a number.")
        return None


def print_karvand(person):
    print("-" * 30)
    print("ID:", person["id"])
    print("Name:", person["full_name"])
    print("Email:", person["email"])
    print("City:", person["city"])
    print("Education:", person["education"]["degree"], "-",
          person["education"]["major"])
    print("Skills:")
    for skill in person["skills"]:
        print(skill["name"], "-", skill["level"], "-", skill["score"])


def add_menu(data):
    full_name = input("Full name: ")
    email = input("Email: ")
    city = input("City: ")
    degree = input("Degree: ")
    major = input("Major: ")
    skill_name = input("Skill name: ")
    skill_level = input("Skill level: ")

    while True:
        score = ask_int("Skill score (0-100): ")
        if score is not None and 0 <= score <= 100:
            break
        if score is not None:
            print("Score must be between 0 and 100.")

    manager.add_karvand(data, full_name, email, city, degree, major,
                        skill_name, skill_level, score)
    storage.save_data(data)
    print("Karvand added successfully.")


def show_all_menu(data):
    if not data["karvands"]:
        print("No karvands found.")
        return
    for person in data["karvands"]:
        print_karvand(person)


def search_id_menu(data):
    karvand_id = ask_int("Enter id: ")
    if karvand_id is None:
        return
    person = manager.find_by_id(data, karvand_id)
    if person is None:
        print("Karvand not found.")
    else:
        print_karvand(person)


def search_skill_menu(data):
    people = manager.find_by_skill(data, input("Enter skill name: "))
    if not people:
        print("No karvand found.")
    for person in people:
        print(person["full_name"])


def edit_menu(data):
    karvand_id = ask_int("Enter id: ")
    if karvand_id is None:
        return
    person = manager.find_by_id(data, karvand_id)
    if person is None:
        print("Karvand not found.")
        return

    for number, field in enumerate(manager.EDITABLE_FIELDS, start=1):
        print(f"{number}. {field.capitalize()}")

    choice = ask_int("Choose what to edit: ")
    if choice is None or not 1 <= choice <= len(manager.EDITABLE_FIELDS):
        print("Invalid choice.")
        return

    field = manager.EDITABLE_FIELDS[choice - 1]
    manager.update_field(person, field, input(f"New {field}: "))
    storage.save_data(data)
    print("Karvand updated.")


def delete_menu(data):
    karvand_id = ask_int("Enter id: ")
    if karvand_id is None:
        return
    if manager.delete_karvand(data, karvand_id):
        storage.save_data(data)
        print("Karvand deleted.")
    else:
        print("Karvand not found.")


def report_menu(data):
    report = manager.build_report(data)
    storage.save_report(report)
    print(report)


ACTIONS = {
    "1": ("Add Karvand", add_menu),
    "2": ("Show All Karvands", show_all_menu),
    "3": ("Search By ID", search_id_menu),
    "4": ("Search By Skill", search_skill_menu),
    "5": ("Edit Karvand", edit_menu),
    "6": ("Delete Karvand", delete_menu),
    "7": ("Report", report_menu),
}


def menu():
    data = storage.load_data()

    while True:
        print("\n===== Karvand Manager =====")
        for key, (title, _) in ACTIONS.items():
            print(f"{key}. {title}")
        print("8. Exit")

        choice = input("Choose: ")
        if choice == "8":
            print("Goodbye.")
            break
        if choice in ACTIONS:
            ACTIONS[choice][1](data)
        else:
            print("Invalid choice.")
