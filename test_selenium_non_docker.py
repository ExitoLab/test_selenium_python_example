# test_selenium.py
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def get_driver():
    browser = os.getenv("BROWSER", "chrome").lower()

    if browser == "chrome":
        options = ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )
    elif browser == "firefox":
        options = FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )
    elif browser == "edge":
        options = EdgeOptions()
        options.add_argument("--headless")
        driver = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=options
        )
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    return driver

def test_google_title():
    driver = get_driver()
    try:
        driver.get("https://www.google.com")
        assert "Google" in driver.title
    finally:
        driver.quit()

if __name__ == "__main__":
    test_google_title()
