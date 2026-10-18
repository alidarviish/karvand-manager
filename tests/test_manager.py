import pytest

import manager


@pytest.fixture
def data():
    """Two karvands to start each test with. A fresh copy is made for every test."""
    data = {"bootcamp": "Karvand Bootcamp", "karvands": []}
    manager.add_karvand(data, "Ali", "ali@x.com", "Shiraz", "BSc", "CS",
                        "Python", "pro", 90)
    manager.add_karvand(data, "Sara", "sara@x.com", "Tehran", "MSc", "AI",
                        "SQL", "mid", 70)
    return data


def test_next_id_on_empty_list():
    assert manager.next_id([]) == 1


def test_next_id_uses_largest_id():
    karvands = [{"id": 5}, {"id": 2}]
    assert manager.next_id(karvands) == 6


def test_add_karvand_gives_new_id(data):
    person = manager.add_karvand(data, "Reza", "r@x.com", "Karaj", "BSc",
                                 "EE", "C", "low", 50)
    assert person["id"] == 3
    assert len(data["karvands"]) == 3


def test_add_karvand_rejects_bad_score(data):
    with pytest.raises(ValueError):
        manager.add_karvand(data, "X", "x@x.com", "C", "D", "M", "S", "L", 150)
    assert len(data["karvands"]) == 2


def test_find_by_id(data):
    assert manager.find_by_id(data, 2)["full_name"] == "Sara"
    assert manager.find_by_id(data, 99) is None


def test_find_by_skill_ignores_case(data):
    people = manager.find_by_skill(data, "pYtHoN")
    assert [p["full_name"] for p in people] == ["Ali"]


def test_find_by_skill_no_match(data):
    assert manager.find_by_skill(data, "Java") == []


def test_update_field_changes_only_that_person(data):
    sara = manager.find_by_id(data, 2)
    manager.update_field(sara, "city", "Karaj")
    assert sara["city"] == "Karaj"
    assert manager.find_by_id(data, 1)["city"] == "Shiraz"


def test_update_field_education(data):
    ali = manager.find_by_id(data, 1)
    manager.update_field(ali, "major", "Data Science")
    assert ali["education"]["major"] == "Data Science"


def test_update_field_unknown_field(data):
    with pytest.raises(ValueError):
        manager.update_field(manager.find_by_id(data, 1), "age", "30")


def test_delete_karvand(data):
    assert manager.delete_karvand(data, 1) is True
    assert manager.find_by_id(data, 1) is None
    assert manager.delete_karvand(data, 1) is False


def test_id_not_reused_after_delete(data):
    manager.delete_karvand(data, 1)
    person = manager.add_karvand(data, "Reza", "r@x.com", "Karaj", "BSc",
                                 "EE", "C", "low", 50)
    assert person["id"] == 3


def test_build_report(data):
    report = manager.build_report(data)
    assert report["total_karvands"] == 2
    assert report["total_skills"] == 2
    assert report["average_skill_score"] == 80
    assert report["cities"] == ["Shiraz", "Tehran"]
    assert report["unique_skills"] == ["Python", "SQL"]


def test_build_report_empty():
    report = manager.build_report({"karvands": []})
    assert report["total_karvands"] == 0
    assert report["average_skill_score"] == 0
