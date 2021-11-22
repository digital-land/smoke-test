import pytest



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
