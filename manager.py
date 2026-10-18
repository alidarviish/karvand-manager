"""Core logic. No input() or print() here, so every function is easy to test."""


def next_id(karvands):
    if not karvands:
        return 1
    return max(person["id"] for person in karvands) + 1


def add_karvand(data, full_name, email, city, degree, major,
                skill_name, skill_level, skill_score):
    if not 0 <= skill_score <= 100:
        raise ValueError("Skill score must be between 0 and 100.")

    person = {
        "id": next_id(data["karvands"]),
        "full_name": full_name,
        "email": email,
        "city": city,
        "education": {"degree": degree, "major": major},
        "skills": [
            {"name": skill_name, "level": skill_level, "score": skill_score}
        ],
    }
    data["karvands"].append(person)
    return person


def find_by_id(data, karvand_id):
    for person in data["karvands"]:
        if person["id"] == karvand_id:
            return person
    return None


def find_by_skill(data, skill_name):
    skill_name = skill_name.lower()
    result = []
    for person in data["karvands"]:
        for skill in person["skills"]:
            if skill["name"].lower() == skill_name:
                result.append(person)
                break
    return result


EDITABLE_FIELDS = ["email", "city", "degree", "major"]


def update_field(person, field, value):
    if field in ("email", "city"):
        person[field] = value
    elif field in ("degree", "major"):
        person["education"][field] = value
    else:
        raise ValueError(f"Unknown field: {field}")


def delete_karvand(data, karvand_id):
    person = find_by_id(data, karvand_id)
    if person is None:
        return False
    data["karvands"].remove(person)
    return True


def build_report(data):
    cities = []
    unique_skills = []
    total_skills = 0
    total_score = 0

    for person in data["karvands"]:
        if person["city"] not in cities:
            cities.append(person["city"])
        for skill in person["skills"]:
            total_skills += 1
            total_score += skill["score"]
            if skill["name"] not in unique_skills:
                unique_skills.append(skill["name"])

    average_score = total_score / total_skills if total_skills else 0

    return {
        "total_karvands": len(data["karvands"]),
        "total_skills": total_skills,
        "average_skill_score": average_score,
        "cities": cities,
        "unique_skills": unique_skills,
    }
