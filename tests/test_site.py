import requests


BASE_URL = f"https://www.digital-land.info"


def test_html_pages(page):

    page.goto(BASE_URL)

    page.click("text=Datasets")
    assert page.url == f"{BASE_URL}/dataset/"
    assert page.text_content("h1") == "Datasets"
    page.goto(BASE_URL)

    page.click("text=Map")
    assert page.url == f"{BASE_URL}/map/"
    assert page.text_content("h1") == "National map of planning data"
    page.goto(BASE_URL)

    page.click("text=Search")
    assert page.url == f"{BASE_URL}/entity/"
    assert page.text_content("h1") == "Search for planning and housing data"
    page.goto(BASE_URL)

    page.click("text=Datasets")
    assert page.url == f"{BASE_URL}/dataset/"
    page.click("text=Green belt")
    assert page.url == f"{BASE_URL}/dataset/green-belt"
    assert page.text_content("h1") == "Green belt"

    page.click("text=Datasets")
    assert page.url == f"{BASE_URL}/dataset/"


def test_get_json():
    json_url = f"{BASE_URL}/dataset/local-authority-eng.json"
    resp = requests.get(json_url)
    resp.raise_for_status()
    data = resp.json()

    assert data["collection"] == "organisation"
    assert data["dataset"] == "local-authority-eng"
