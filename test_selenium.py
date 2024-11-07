import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_open_google():
    # Set up the ChromeDriver using WebDriverManager
    chrome_service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Optional: Run in headless mode (no GUI)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Initialize WebDriver with options and the correct service
    driver = webdriver.Chrome(service=chrome_service, options=options)
    
    driver.get("https://www.google.com")
    
    assert "Google" in driver.title
    
    # Example: Look for a specific element on the page
    search_box = driver.find_element(By.NAME, "q")
    assert search_box is not None

    driver.quit()
