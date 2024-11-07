import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_open_google():
    # Set up ChromeDriver using WebDriverManager
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/chromium-browser"  # Ensure Chromium is available

    chrome_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)
    
    driver.get("https://www.google.com")
    
    assert "Google" in driver.title
    
    # Example: Look for a specific element on the page
    search_box = driver.find_element(By.NAME, "q")
    assert search_box is not None

    driver.quit()
