import requests


BASE_URL = f"https://www.digital-land.info"


def test_get_healthcheck():
    json_url = f"{BASE_URL}/health"
    resp = requests.get(json_url)
    resp.raise_for_status()
    data = resp.json()

    assert data["status"] == "OK"
