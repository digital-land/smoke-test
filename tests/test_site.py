import requests


BASE_URL = f"https://www.digital-land.info"


def test_html_pages(page):

    page.goto(f"{BASE_URL}")
    page.click("text=Datasets")
    assert page.url == f"{BASE_URL}/dataset/"
    page.click("text=Brownfield site")
    assert page.url == f"{BASE_URL}/dataset/brownfield-site"
    page.click('h1:has-text("Brownfield site")')
    page.click("text=Datasets")
    assert page.url == f"{BASE_URL}/dataset/"

    page.goto(f"{BASE_URL}/entity/")
    assert page.inner_text("h1") == "Search for planning and housing data"
    page.click("text=Ancient woodland")
    page.click('button:has-text("Search")')
    assert (
        page.url
        == f"{BASE_URL}/entity/?dataset=ancient-woodland&entries=all&entry_entry_date_day=&entry_entry_date_month=&entry_entry_date_year="
    )

    page.click("text=11345")
    assert page.url == f"{BASE_URL}/entity/11345"


def test_get_json():
    json_url = f"{BASE_URL}/entity/11345.json"
    resp = requests.get(json_url)
    resp.raise_for_status()
    data = resp.json()

    assert data['entity'] == '11345'
    assert data['entry-date'] == '2021-05-26'
    assert data['name'] == 'WILK WOOD'
    assert data['dataset'] == 'ancient-woodland'
    assert data['typology'] == 'geographee'
    assert data.get('geojson')