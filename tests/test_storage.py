import storage


def test_save_then_load(tmp_path):
    path = tmp_path / "karvands.json"
    data = {"bootcamp": "Test", "karvands": [{"id": 1, "full_name": "علی"}]}

    storage.save_data(data, path)

    assert storage.load_data(path) == data


def test_load_missing_file_creates_empty_data(tmp_path):
    path = tmp_path / "karvands.json"

    data = storage.load_data(path)

    assert data == storage.empty_data()
    assert path.exists()


def test_load_broken_json_returns_empty_data(tmp_path):
    path = tmp_path / "karvands.json"
    path.write_text("{ this is not json", encoding="utf-8")

    assert storage.load_data(path) == storage.empty_data()


def test_save_creates_missing_folder(tmp_path):
    path = tmp_path / "new_folder" / "karvands.json"

    storage.save_data({"karvands": []}, path)

    assert path.exists()
