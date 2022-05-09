import requests
import random

BASE_URL = f"https://www.digital-land.info"


def test_get_healthcheck():
    json_url = f"{BASE_URL}/health"
    resp = requests.get(json_url)
    resp.raise_for_status()
    data = resp.json()

    assert data["status"] == "OK"


def test_get_datasets():
    json_url = f"{BASE_URL}/dataset.json"
    resp = requests.get(json_url)
    resp.raise_for_status()
    data = resp.json()
    assert data.get("datasets") is not None


def test_get_enities():
    json_url = f"{BASE_URL}/entity.json"
    resp = requests.get(json_url)
    resp.raise_for_status()
    data = resp.json()
    assert data.get("entities") is not None
    assert data.get("count") is not None
    assert data.get("links") is not None
    assert data.get("links").get("last") is not None

    resp = requests.get(data.get("links").get("last"))
    resp.raise_for_status()
    data = resp.json()
    assert data.get("entities") is not None
    assert data.get("count") is not None
    assert data.get("links") is not None

    # try a few random offsets
    count = data.get("count")
    sample_offsets = random.sample(range(1, count), 5)
    for offset in sample_offsets:
        url = f"{json_url}/?limit=10&offset={offset}"
        resp.raise_for_status()
        data = resp.json()
        assert data.get("entities") is not None

