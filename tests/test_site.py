import requests
import random

BASE_URL = f"https://www.digital-land.info"


def test_get_healthcheck_status():
    json_url = f"{BASE_URL}/health"
    resp = requests.get(json_url)
    resp.raise_for_status()
    data = resp.json()

    assert data["status"] == "OK"


def test_get_healthcheck_entities():
    json_url = f"{BASE_URL}/health"
    resp = requests.get(json_url)
    resp.raise_for_status()
    data = resp.json()

    assert data["entities_present"] == "OK"


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

    # sample a few early pages (avoid last/huge offsets — they often 504)
    count = data.get("count")
    max_offset = min(count, 1000)
    if max_offset > 1:
        sample_offsets = random.sample(
            range(1, max_offset), min(5, max_offset - 1)
        )
    else:
        sample_offsets = []
    for offset in sample_offsets:
        url = f"{json_url}?limit=10&offset={offset}"
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        assert data.get("entities") is not None

