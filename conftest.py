import pytest
from playwright.sync_api import sync_playwright, Page
from dotenv import load_dotenv

load_dotenv()  # make sure .env is loaded

from pages.login_page import LoginPage  # your page object class

# --- Browser Fixture ---
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# --- Page Fixture ---
@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

# --- App Pages Fixture ---
@pytest.fixture
def app_pages(page: Page):
    my_pages = {
        "login_pg": LoginPage(page)
    }
    yield my_pages
