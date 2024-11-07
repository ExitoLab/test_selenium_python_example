import os
import time
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

def get_driver():
    browser = os.getenv("BROWSER", "chrome").lower()

    options = None
    if browser == "chrome":
        options = ChromeOptions()
    elif browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Retry connection to Selenium server
    driver = None
    for attempt in range(5):
        try:
            driver = webdriver.Remote(
                command_executor='http://selenium:4444/wd/hub',
                options=options
            )
            break
        except WebDriverException:
            print("Retrying connection to Selenium server...")
            time.sleep(3)
    
    if not driver:
        raise RuntimeError("Failed to connect to the Selenium server after multiple attempts.")
    
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
