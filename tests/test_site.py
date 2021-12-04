import requests


BASE_URL = f"https://www.digital-land.info"


def test_get_healthcheck():
    json_url = f"{BASE_URL}/health"
    resp = requests.get(json_url)
    resp.raise_for_status()
    data = resp.json()

    assert data["status"] == "OK"
    assert data["dataset_count"] > 0
    assert data["entity_count"] > 0


def test_get_json():
    json_url = f"{BASE_URL}/dataset/local-authority-eng.json"
    resp = requests.get(json_url)
    resp.raise_for_status()
    data = resp.json()

    assert data["collection"] == "organisation"
    assert data["dataset"] == "local-authority-eng"
