
from playwright.sync_api import sync_playwright
from os import environ
        
def test_login_saucedemo(app_pages):
    app_pages["login_pg"].open(environ.get("BASE_URL"))
    app_pages["login_pg"].login(environ.get("STANDARD_USER"), environ.get("PASSWORD"))
    
        